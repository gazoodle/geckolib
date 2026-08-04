"""Unit tests for the status block resync safety net."""  # noqa: INP001

import asyncio
import contextlib
import time
from typing import Any, ClassVar
from unittest import IsolatedAsyncioTestCase, main

from context import (
    GeckoAsyncSpa,
    GeckoAsyncSpaDescriptor,
    GeckoAsyncSpaMan,
    GeckoConfig,
    GeckoSpaEvent,
    GeckoSpaState,
)

from geckolib import config as gecko_config

STATP_DATA = b"\x09\x09"


class FakeLogClass:
    """Just enough of a GeckoLogStruct for resync range computation."""

    begin = 0
    end = 4


class FakeStatpHandler:
    """Just enough of a partial status block handler for the spa callback."""

    changes: ClassVar[list[tuple[int, bytes]]] = [(2, STATP_DATA)]


class SpaHarness:
    """Host a GeckoAsyncSpa wired for resync testing without a network."""

    def __init__(self) -> None:
        """Initialize the harness with a connected-looking spa."""
        self.events: list[GeckoSpaEvent] = []
        descriptor = GeckoAsyncSpaDescriptor(b"TestID", "Test Name", (1, 2))
        self.spa = GeckoAsyncSpa(b"CLIENT", descriptor, None, self._on_event)
        self.spa._is_connected = True
        self.spa._protocol = object()
        self.spa.struct.log_class = FakeLogClass()
        self.change_notifications = 0
        self.spa.watch(self._on_spa_change)

    async def _on_event(self, event: GeckoSpaEvent, **_kwargs: Any) -> None:
        self.events.append(event)

    def _on_spa_change(self, *_args: Any) -> None:
        self.change_notifications += 1

    def install_fake_get(
        self,
        *,
        result: bool = True,
        mutate: bool = False,
        statp_during: bool = False,
    ) -> None:
        """
        Replace struct.get with a fake, optionally mutating the block.

        When mutate is True every call writes fresh bytes, so each resync
        sees drift (as if the spa changed state between reads).
        """
        call_count = [0]

        async def fake_get(
            _protocol: Any, _create_func: Any, _packet_timeout: Any = None
        ) -> bool:
            call_count[0] += 1
            if statp_during:
                self.spa._last_statp_monotonic = time.monotonic()
            if mutate:
                fresh = bytes([call_count[0], call_count[0] + 1])
                self.spa.struct.replace_status_block_segment(0, fresh)
            return result

        self.spa.struct.get = fake_get


class TestPartialStatusUpdate(IsolatedAsyncioTestCase):
    """The STATP receipt hook must stamp both data clocks."""

    async def test_statp_stamps_clocks_and_applies_changes(self) -> None:
        harness = SpaHarness()
        self.assertIsNone(harness.spa.last_statp_at)
        self.assertIsNone(harness.spa.last_data_at)

        await harness.spa._async_on_partial_status_update(FakeStatpHandler(), (1, 2))

        self.assertIsNotNone(harness.spa.last_statp_at)
        self.assertEqual(harness.spa.last_data_at, harness.spa.last_statp_at)
        self.assertIsNotNone(harness.spa._last_statp_monotonic)
        self.assertEqual(harness.spa.struct.status_block[2:4], STATP_DATA)
        self.assertGreater(harness.change_notifications, 0)


class TestAsyncResync(IsolatedAsyncioTestCase):
    """Behavior of the in-place status block resync."""

    async def test_success_without_drift_is_silent(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=True)

        self.assertTrue(await harness.spa.async_resync())

        self.assertListEqual(harness.events, [])
        self.assertIsNotNone(harness.spa.last_data_at)
        self.assertIsNone(harness.spa.last_statp_at)

    async def test_first_stale_resync_rearms_without_escalating(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=True, mutate=True)

        self.assertTrue(await harness.spa.async_resync())

        # The read itself re-arms the subscription; no reconnect on strike one
        self.assertListEqual(harness.events, [])
        self.assertEqual(harness.spa._consecutive_stale_resyncs, 1)

    async def test_second_consecutive_stale_resync_escalates(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=True, mutate=True)

        self.assertTrue(await harness.spa.async_resync())
        self.assertTrue(await harness.spa.async_resync())

        self.assertListEqual(
            harness.events, [GeckoSpaEvent.RUNNING_SPA_STALE_SUBSCRIPTION]
        )

    async def test_statp_between_stale_resyncs_resets_counter(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=True, mutate=True)
        self.assertListEqual(harness.events, [])

        self.assertTrue(await harness.spa.async_resync())
        self.assertListEqual(harness.events, [])

        # Push traffic resumes - the re-arm worked
        await harness.spa._async_on_partial_status_update(FakeStatpHandler(), (1, 2))
        self.assertListEqual(
            harness.events, [GeckoSpaEvent.RUNNING_SPA_PACK_UPDATED]
        )
        harness.events.clear()
        self.assertEqual(harness.spa._consecutive_stale_resyncs, 0)
        # A later stale resync is strike one again, not strike two
        self.assertTrue(await harness.spa.async_resync())

        self.assertListEqual(harness.events, [])

    async def test_drift_with_concurrent_statp_does_not_escalate(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=True, mutate=True, statp_during=True)

        self.assertTrue(await harness.spa.async_resync())
        self.assertTrue(await harness.spa.async_resync())

        self.assertListEqual(harness.events, [])
        self.assertEqual(harness.spa._consecutive_stale_resyncs, 0)

    async def test_drift_with_escalation_disabled_is_silent(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=True, mutate=True)

        self.assertTrue(await harness.spa.async_resync(escalate=False))
        self.assertTrue(await harness.spa.async_resync(escalate=False))
        self.assertTrue(await harness.spa.async_resync(escalate=False))

        self.assertListEqual(harness.events, [])

    async def test_failure_fires_retry_time_exceeded(self) -> None:
        harness = SpaHarness()
        harness.install_fake_get(result=False)

        self.assertFalse(await harness.spa.async_resync())

        self.assertListEqual(
            harness.events, [GeckoSpaEvent.ERROR_PROTOCOL_RETRY_TIME_EXCEEDED]
        )
        self.assertIsNone(harness.spa.last_data_at)

    async def test_not_connected_returns_false(self) -> None:
        harness = SpaHarness()
        harness.spa._is_connected = False
        harness.install_fake_get(result=True)

        self.assertFalse(await harness.spa.async_resync())

        self.assertListEqual(harness.events, [])


class SpaManImpl(GeckoAsyncSpaMan):
    """Spa manager to test with."""

    def __init__(self) -> None:
        """Initialize the spaman class."""
        super().__init__("CLIENT_UUID", spa_identifier="TestID", spa_name="Test Name")
        self.events: list[GeckoSpaEvent] = []

    async def handle_event(self, event: GeckoSpaEvent, **_kwargs: object) -> None:
        self.events.append(event)


class TestErrorWatchdog(IsolatedAsyncioTestCase):
    """The error watchdog must recover states the ping loop cannot."""

    def setUp(self) -> None:
        self._saved_retry = GeckoConfig.SPA_RECONNECT_RETRY_FREQUENCY_IN_SECONDS
        GeckoConfig.SPA_RECONNECT_RETRY_FREQUENCY_IN_SECONDS = 0.05
        # The module-global event binds to the first loop that waits on it;
        # IsolatedAsyncioTestCase runs every test in a fresh loop
        gecko_config.ConfigChangeEvent = asyncio.Event()

    def tearDown(self) -> None:
        GeckoConfig.SPA_RECONNECT_RETRY_FREQUENCY_IN_SECONDS = self._saved_retry

    async def test_watchdog_recovers_stuck_error_state(self) -> None:
        spaman = SpaManImpl()
        reset_done = asyncio.Event()

        async def fake_reset() -> None:
            reset_done.set()

        spaman.async_reset = fake_reset
        spaman.set_spa_state(GeckoSpaState.ERROR_NEEDS_ATTENTION)

        task = asyncio.create_task(spaman._error_watchdog())
        try:
            await asyncio.wait_for(reset_done.wait(), timeout=5)
        finally:
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task

    async def test_watchdog_leaves_healthy_state_alone(self) -> None:
        spaman = SpaManImpl()
        resets: list[int] = []

        async def fake_reset() -> None:
            resets.append(1)

        spaman.async_reset = fake_reset
        self.assertEqual(spaman.spa_state, GeckoSpaState.IDLE)

        task = asyncio.create_task(spaman._error_watchdog())
        await asyncio.sleep(0.2)
        task.cancel()
        with contextlib.suppress(asyncio.CancelledError):
            await task

        self.assertListEqual(resets, [])


class TestScheduledReset(IsolatedAsyncioTestCase):
    """Reset scheduling must serialize and never run inside SPA tasks."""

    async def test_schedule_reset_runs_and_dedups(self) -> None:
        spaman = SpaManImpl()
        started = asyncio.Event()
        release = asyncio.Event()
        calls: list[int] = []

        async def fake_reset() -> None:
            calls.append(1)
            started.set()
            await release.wait()

        spaman.async_reset = fake_reset

        spaman._try_schedule_reset("Test reset")
        await asyncio.wait_for(started.wait(), timeout=2)
        # Second request while the first is still running is dropped
        spaman._try_schedule_reset("Test reset")
        release.set()
        await asyncio.sleep(0)

        self.assertListEqual(calls, [1])
        await spaman.gather()

    async def test_auto_resets_are_rate_limited(self) -> None:
        spaman = SpaManImpl()
        calls: list[int] = []

        async def fake_reset() -> None:
            calls.append(1)

        spaman.async_reset = fake_reset

        spaman._try_schedule_reset("Test reset")
        await asyncio.sleep(0.05)
        # Within the rate-limit window: dropped
        spaman._try_schedule_reset("Test reset")
        await asyncio.sleep(0.05)
        self.assertListEqual(calls, [1])

        # Outside the window: runs again
        spaman._last_auto_reset_at = (
            time.monotonic() - spaman.AUTO_RESET_MIN_INTERVAL_IN_SECONDS - 1
        )
        spaman._try_schedule_reset("Test reset")
        await asyncio.sleep(0.05)
        self.assertListEqual(calls, [1, 1])
        await spaman.gather()

    async def test_stale_subscription_event_schedules_reset(self) -> None:
        spaman = SpaManImpl()
        reset_done = asyncio.Event()

        async def fake_reset() -> None:
            reset_done.set()

        spaman.async_reset = fake_reset

        await spaman._handle_event(GeckoSpaEvent.RUNNING_SPA_STALE_SUBSCRIPTION)
        await asyncio.wait_for(reset_done.wait(), timeout=2)

        self.assertIn(GeckoSpaEvent.RUNNING_SPA_STALE_SUBSCRIPTION, spaman.events)
        await spaman.gather()


if __name__ == "__main__":
    main()

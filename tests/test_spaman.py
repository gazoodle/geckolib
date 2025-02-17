"""Unit tests for the SpaMan class."""  # noqa: INP001

from typing import Any
from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import patch

from context import GeckoAsyncSpaDescriptor, GeckoAsyncSpaMan, GeckoSpaEvent


class SpaManImpl(GeckoAsyncSpaMan):
    """Spa Manager to test with."""

    def __init__(self) -> None:
        """Initialize the spaman class."""
        super().__init__("CLIENT_UUID", spa_identifier="TestID")
        self.events = []

    async def handle_event(self, event: GeckoSpaEvent, **_kwargs: object) -> None:
        self.events.append(event)


mock_spa_descriptor = GeckoAsyncSpaDescriptor(b"TestID", "Test Name", (1, 2))
mock_spas = [mock_spa_descriptor]


async def mock_discover(self: Any) -> None:
    """Mock discovery."""
    await self._event_handler(GeckoSpaEvent.LOCATING_DISCOVERED_SPA)


async def mock_connect(self: Any) -> None:
    """Mock connection."""
    # await self._event_handler(GeckoSpaEvent.CONNECTION_SPA_COMPLETE)  # noqa: ERA001


@patch("context.GeckoAsyncSpa._connect", mock_connect)
@patch("context.GeckoAsyncLocator.discover", mock_discover)
@patch("context.GeckoAsyncLocator.spas", mock_spas)
class TestSpaMan(IsolatedAsyncioTestCase):
    """Test the SpaMan class."""

    def setUp(self) -> None:
        self.spaman = SpaManImpl()

    async def asyncSetUp(self) -> None:
        await self.spaman.__aenter__()

    async def asyncTearDown(self) -> None:
        await self.spaman.__aexit__(None)

    def tearDown(self) -> None:
        del self.spaman

    #####################################################

    def test_facade_on_start(self) -> None:
        self.assertIsNone(self.spaman.facade)

    async def test_locate_spas(self) -> None:
        spas = await self.spaman.async_locate_spas()
        self.assertEqual(len(spas), 1)
        self.assertEqual(spas[0].identifier_as_string, "TestID")
        self.assertEqual(spas[0].name, "Test Name")
        self.assertListEqual(
            self.spaman.events,
            [
                GeckoSpaEvent.SPA_MAN_ENTER,
                GeckoSpaEvent.LOCATING_STARTED,
                GeckoSpaEvent.LOCATING_STARTED,
                GeckoSpaEvent.LOCATING_DISCOVERED_SPA,
                GeckoSpaEvent.LOCATING_FINISHED,
            ],
        )

    async def test_connect_spa(self) -> None:
        facade = await self.spaman.async_connect_to_spa(mock_spa_descriptor)
        self.assertListEqual(
            self.spaman.events,
            [
                GeckoSpaEvent.SPA_MAN_ENTER,
                GeckoSpaEvent.LOCATING_STARTED,
                GeckoSpaEvent.CLIENT_HAS_STATUS_SENSOR,
                GeckoSpaEvent.CLIENT_HAS_RECONNECT_BUTTON,
                GeckoSpaEvent.CONNECTION_STARTED,
                GeckoSpaEvent.CONNECTION_FINISHED,
            ],
        )
        self.assertIsNone(facade)


if __name__ == "__main__":
    main()

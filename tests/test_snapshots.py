"""Unit tests for the actual snapshots."""  # noqa: INP001

import pathlib
from unittest import IsolatedAsyncioTestCase, main

from context import (
    GeckoAsyncFacade,
    GeckoAsyncStructure,
    GeckoAsyncTaskMan,
    GeckoSnapshot,
)

from geckolib.driver.accessor import GeckoStructAccessor


class GeckoAsyncSpa:
    """Mock spa for testing."""

    def __init__(self, snapshotfile: str) -> None:
        """Initialize the class."""
        self.struct = GeckoAsyncStructure(None)

        cwd = pathlib.Path(__file__).parent.resolve()
        snapshots = GeckoSnapshot.parse_log_file(f"{cwd}/{snapshotfile}")
        assert len(snapshots) == 1

        snapshot = snapshots[0]
        self.struct.replace_status_block_segment(0, snapshot.bytes)

        # Attempt to get config and log classes
        self.plateform_key = snapshot.packtype.lower()
        self.config_version = snapshot.config_version
        self.log_version = snapshot.log_version

    @property
    def accessors(self) -> list[GeckoStructAccessor]:
        """Get the accessors."""
        return self.struct.accessors

    @property
    def is_responding_to_pings(self) -> bool:
        """Is the remote end responding to pings."""
        return True

    async def async_init(self) -> None:
        """Init async."""
        await self.struct.load_pack_class(self.plateform_key)
        await self.struct.load_config_module(self.config_version)
        await self.struct.load_log_module(self.log_version)
        await self.struct.check_for_accessories()
        self.struct.build_accessors()


class TestSnapshots(IsolatedAsyncioTestCase):
    """Test all the snapshots."""

    def setUp(self) -> None:
        self.taskman = GeckoAsyncTaskMan()

    async def asyncSetUp(self) -> None:
        await self.taskman.__aenter__()

    async def asyncTearDown(self) -> None:
        await self.taskman.__aexit__(None)

    def tearDown(self) -> None:
        del self.taskman

    async def build_facade(self, snapshotfile: str) -> GeckoAsyncFacade:
        spa = GeckoAsyncSpa(snapshotfile)
        await spa.async_init()
        return GeckoAsyncFacade(spa, self.taskman)

    async def test_default(self) -> None:
        facade = await self.build_facade("snapshots/default.snapshot")
        self.assertTrue(facade.pump_1.is_available)
        self.assertTrue(facade.pump_2.is_available)
        self.assertFalse(facade.pump_3.is_available)
        self.assertTrue(facade.blower.is_available)
        self.assertTrue(facade.light.is_available)
        self.assertFalse(facade.light2.is_available)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertFalse(facade.blowers[0].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(39.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)

    async def test_inYT_Pump1Low(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYT-Pump1Lo-2020-12-13 11_19_35.snapshot"
        )
        self.assertTrue(facade.pump_1.is_available)
        self.assertTrue(facade.pump_2.is_available)
        self.assertTrue(facade.light.is_available)
        self.assertEqual("LO", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertTrue(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertTrue(facade.lights[0].is_on)
        self.assertEqual(70.0, facade.water_heater.current_temperature)
        self.assertEqual("°F", facade.water_heater.temperature_unit)

    async def test_inYT_Pump1High(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYT-Pump1Hi-2020-12-13 11_19_35.snapshot"
        )
        self.assertTrue(facade.pump_1.is_available)
        self.assertTrue(facade.pump_2.is_available)
        self.assertTrue(facade.light.is_available)
        self.assertEqual("HI", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertTrue(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertTrue(facade.lights[0].is_on)
        self.assertEqual(70.0, facade.water_heater.current_temperature)
        self.assertEqual("°F", facade.water_heater.temperature_unit)

    async def test_inYT_WaterFall_On(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYT-waterfall on-2020-10-23 18_01_30.snapshot"
        )
        self.assertTrue(facade.pump_1.is_available)
        self.assertTrue(facade.pump_2.is_available)
        self.assertTrue(facade.waterfall.is_available)
        self.assertTrue(facade.light.is_available)
        self.assertEqual("OFF", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertEqual("ON", facade.pumps[2].mode)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(37.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)

    async def test_inYJ_All_Off(self) -> None:  # noqa: N802
        facade = await self.build_facade(
            "snapshots/inYJ-All off-2020-12-18 11_24_09.snapshot"
        )
        self.assertTrue(facade.pump_1.is_available)
        self.assertTrue(facade.light.is_available)
        self.assertEqual("OFF", facade.pumps[0].mode)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(37.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)


if __name__ == "__main__":
    main()

""" Unit tests for the actual snapshots """

from unittest import IsolatedAsyncioTestCase, main
import importlib
import pathlib


from context import GeckoStructure, GeckoSnapshot, GeckoConstants, GeckoAsyncFacade, AsyncTasks  # type: ignore


class GeckoAsyncSpa:
    """Mock spa for testing"""

    def __init__(self, snapshotfile):
        self.struct = GeckoStructure(None)

        cwd = pathlib.Path(__file__).parent.resolve()
        snapshots = GeckoSnapshot.parse_log_file(f"{cwd}/{snapshotfile}")
        assert len(snapshots) == 1

        snapshot = snapshots[0]
        self.struct.replace_status_block_segment(0, snapshot.bytes)

        # Attempt to get config and log classes
        plateform_key = snapshot.packtype.lower()

        pack_module_name = f"geckolib.driver.packs.{plateform_key}"
        try:
            GeckoPack = importlib.import_module(pack_module_name).GeckoPack
            self.pack_class = GeckoPack(self.struct)
            self.pack_type = self.pack_class.type
        except ModuleNotFoundError:
            raise Exception(
                GeckoConstants.EXCEPTION_MESSAGE_NO_SPA_PACK.format(
                    self.snapshot.packtype
                )
            )

        config_module_name = (
            f"geckolib.driver.packs.{plateform_key}-cfg-{snapshot.config_version}"
        )
        try:
            GeckoConfigStruct = importlib.import_module(
                config_module_name
            ).GeckoConfigStruct
            self.config_class = GeckoConfigStruct(self.struct)
        except ModuleNotFoundError:
            raise Exception(
                f"Cannot find GeckoConfigStruct module for {snapshot.packtype} v{snapshot.config_version}"
            )

        log_module_name = (
            f"geckolib.driver.packs.{plateform_key}-log-{snapshot.log_version}"
        )
        try:
            GeckoLogStruct = importlib.import_module(log_module_name).GeckoLogStruct
            self.log_class = GeckoLogStruct(self.struct)
        except ModuleNotFoundError:
            raise Exception(
                f"Cannot find GeckoLogStruct module for {snapshot.packtype} v{snapshot.log_version}"
            )

        self.struct.build_accessors(self.config_class, self.log_class)

    @property
    def accessors(self):
        return self.struct.accessors


class TestSnapshots(IsolatedAsyncioTestCase):
    """Test all the snapshots"""

    def setUp(self) -> None:
        self.taskman = AsyncTasks()

    async def asyncSetUp(self) -> None:
        await self.taskman.__aenter__()

    async def asyncTearDown(self) -> None:
        await self.taskman.__aexit__(None)

    def tearDown(self) -> None:
        del self.taskman

    async def build_facade(self, snapshotfile):
        spa = GeckoAsyncSpa(snapshotfile)
        return GeckoAsyncFacade(spa, self.taskman)

    async def test_default(self):
        facade = await self.build_facade("snapshots/default.snapshot")
        self.assertListEqual(
            ["P1", "P2", "BL", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertFalse(facade.blowers[0].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(39.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)

    async def test_inYT_Pump1Low(self):
        facade = await self.build_facade(
            "snapshots/inYT-Pump1Lo-2020-12-13 11_19_35.snapshot"
        )
        self.assertListEqual(
            ["P1", "P2", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("LOW", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertTrue(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertTrue(facade.lights[0].is_on)
        self.assertEqual(70.0, facade.water_heater.current_temperature)
        self.assertEqual("°F", facade.water_heater.temperature_unit)

    async def test_inYT_Pump1High(self):
        facade = await self.build_facade(
            "snapshots/inYT-Pump1Hi-2020-12-13 11_19_35.snapshot"
        )
        self.assertListEqual(
            ["P1", "P2", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("HIGH", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertTrue(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertTrue(facade.lights[0].is_on)
        self.assertEqual(70.0, facade.water_heater.current_temperature)
        self.assertEqual("°F", facade.water_heater.temperature_unit)

    async def test_inYT_WaterFall_On(self):
        facade = await self.build_facade(
            "snapshots/inYT-waterfall on-2020-10-23 18_01_30.snapshot"
        )
        self.assertListEqual(
            ["P1", "P2", "Waterfall", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("OFF", facade.pumps[0].mode)
        self.assertEqual("OFF", facade.pumps[1].mode)
        self.assertEqual("ON", facade.pumps[2].mode)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.pumps[1].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(37.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)

    async def test_inYJ_All_Off(self):
        facade = await self.build_facade(
            "snapshots/inYJ-All off-2020-12-18 11_24_09.snapshot"
        )
        self.assertListEqual(
            ["P1", "LI"],
            [device["device"] for device in facade.actual_user_devices],
        )
        self.assertEqual("OFF", facade.pumps[0].mode)
        self.assertFalse(facade.pumps[0].is_on)
        self.assertFalse(facade.lights[0].is_on)
        self.assertEqual(37.0, facade.water_heater.current_temperature)
        self.assertEqual("°C", facade.water_heater.temperature_unit)
        print(facade.all_user_devices)


if __name__ == "__main__":
    main()

""" Unit tests for the SpaMan class """

from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import patch

from context import GeckoAsyncSpaMan, GeckoAsyncSpaDescriptor, GeckoSpaConnectionEvent


class SpaManImpl(GeckoAsyncSpaMan):
    """A Spa Manager to test with"""

    def __init__(self):
        super().__init__("CLIENT_UUID")
        self.events = []

    async def handle_event(self, event: GeckoSpaConnectionEvent, **kwargs) -> None:
        self.events.append(event)


mock_spa_descriptor = GeckoAsyncSpaDescriptor(b"TestID", "Test Name", (1, 2))
mock_spas = [mock_spa_descriptor]


async def mock_discover(self) -> None:
    await self._event_handler(GeckoSpaConnectionEvent.LOCATING_DISCOVERED_SPA)


@patch("context.GeckoAsyncLocator.discover", mock_discover)
@patch("context.GeckoAsyncLocator.spas", mock_spas)
class TestSpaMan(IsolatedAsyncioTestCase):
    """Test the SpaMan class"""

    def setUp(self) -> None:
        self.spaman = SpaManImpl()

    async def asyncSetUp(self) -> None:
        await self.spaman.__aenter__()

    async def asyncTearDown(self) -> None:
        await self.spaman.__aexit__(None)

    def tearDown(self) -> None:
        del self.spaman

    #####################################################

    def test_facade_on_start(self):
        self.assertIsNone(self.spaman.facade)

    async def test_locate_spas(self):
        spas = await self.spaman.async_locate_spas()
        self.assertEqual(len(spas), 1)
        self.assertEqual(spas[0].identifier_as_string, "TestID")
        self.assertEqual(spas[0].name, "Test Name")
        self.assertListEqual(
            self.spaman.events,
            [
                GeckoSpaConnectionEvent.LOCATING_STARTED,
                GeckoSpaConnectionEvent.LOCATING_DISCOVERED_SPA,
                GeckoSpaConnectionEvent.LOCATING_FINISHED,
            ],
        )

    async def test_connect_spa(self):
        facade = await self.spaman.connect_to_spa(mock_spa_descriptor)
        self.assertIsNotNone(facade)
        self.assertListEqual(
            self.spaman.events,
            [
                GeckoSpaConnectionEvent.LOCATING_STARTED,
                GeckoSpaConnectionEvent.LOCATING_DISCOVERED_SPA,
                GeckoSpaConnectionEvent.LOCATING_FINISHED,
            ],
        )

    async def test_connect_twice_fails(self):
        await self.spaman.connect_to_spa(mock_spa_descriptor)
        with self.assertRaises(AssertionError):
            await self.spaman.connect_to_spa(mock_spa_descriptor)

        self.assertTrue(True)


if __name__ == "__main__":
    main()
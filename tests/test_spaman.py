""" Unit tests for the SpaMan class """

from unittest import IsolatedAsyncioTestCase, main
from unittest.mock import patch

from context import GeckoAsyncSpaMan, GeckoAsyncSpaDescriptor


class SpaManImpl(GeckoAsyncSpaMan):
    """A Spa Manager to test with"""

    def __init__(self):
        super().__init__()
        self.events = []

    async def handle_event(self, event: GeckoAsyncSpaMan.Event, **kwargs) -> None:
        self.events.append(event)


mock_spas = [GeckoAsyncSpaDescriptor(b"TestID", "Test Name", (1, 2))]


async def mock_discover(self) -> None:
    return


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

    async def test_locate_spas(self):
        spas = await self.spaman.async_locate_spas()
        self.assertEqual(len(spas), 1)
        self.assertEqual(spas[0].identifier_as_string, "TestID")
        self.assertEqual(spas[0].name, "Test Name")
        self.assertListEqual(
            self.spaman.events,
            [
                GeckoAsyncSpaMan.Event.LOCATING_STARTED,
                GeckoAsyncSpaMan.Event.LOCATING_FINISHED,
            ],
        )


if __name__ == "__main__":
    main()

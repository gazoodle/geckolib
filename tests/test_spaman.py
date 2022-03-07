""" Unit tests for the SpaMan class """

from unittest import IsolatedAsyncioTestCase, TestCase, main
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

    async def test_startup(self):
        # By the time we're here, the spa manager must be started, so
        # lets just check the default state now
        print(await self.spaman.async_locate_spas())
        self.assertListEqual(self.spaman.events, [1, 2])
        self.assertListEqual(await self.spaman.async_locate_spas(), ["Ib"])

    async def test_again(self):
        print(await self.spaman.async_locate_spas())
        self.assertListEqual(self.spaman.events, [1, 2])


class Inner:
    def inner_func(self):
        return 10

    def another_inner_func(self):
        return 11


class Outer:
    def outer_func(self):
        inner = Inner()
        return inner.inner_func()


def mock_inner_func():
    return 2


class TestPatch(TestCase):
    """ff"""

    @patch("__main__.Inner.inner_func")
    def test_it(self, mock_func):
        mock_func.side_effect = mock_inner_func
        item = Outer()
        self.assertEqual(item.outer_func(), 2)


if __name__ == "__main__":
    main()

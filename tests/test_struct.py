""" Unit tests for the structure class """

from context import GeckoStructure
import unittest
import unittest.mock
import xml.etree.ElementTree as ET


class TestStruct(unittest.TestCase):
    """ Test the GeckoStruct class """

    def setUp(self):
        self.struct = GeckoStructure(None)
        self.xml = ET.fromstring(
            """<UserDemands>
            <QuietState Type="Enum" Pos="362" Items="NOT_SET|QUIET|DRAIN|SOAK|OFF" RW="ALL" />
            <UdP1 Type="Enum" Pos="275" BitPos="14" Size="2" MaxItems="4" Items="OFF|LO|HI" RW="ALL" />
            <UdP2 Type="Enum" Pos="275" BitPos="12" Size="2" MaxItems="4" Items="OFF|LO|HI" RW="ALL" />
            <UdP3 Type="Enum" Pos="275" BitPos="11" Size="2" MaxItems="2" Items="OFF|HI" RW="ALL" />
            <UdP4 Type="Enum" Pos="275" BitPos="10" Size="2" MaxItems="2" Items="OFF|HI" RW="ALL" />
            <UdP5 Type="Enum" Pos="275" BitPos="9" Size="2" MaxItems="2" Items="OFF|HI" RW="ALL" />
            <UdBL Type="Enum" Pos="275" BitPos="8" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
            <UdL120 Type="Enum" Pos="275" BitPos="1" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
            <UdLi Type="Enum" Pos="306" BitPos="0" MaxItems="4" Items="OFF|LO|MED|HI" RW="ALL" />
            <UdValve Type="Enum" Pos="275" BitPos="7" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
            <UdTvLift Type="Enum" Pos="275" BitPos="5" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
            <UdSpkrLift Type="Enum" Pos="275" BitPos="4" Size="2" MaxItems="2" Items="OFF|ON" RW="ALL" />
            <UdVSP1 Type="Byte" Pos="303" Min="0" Max="100" RW="ALL" />
            <UdVSP3 Type="Byte" Pos="304" Min="0" Max="100" RW="ALL" />
            <UdPumpTime Type="Byte" Pos="358" RW="ALL" />
            <UdQuietTime Type="Byte" Pos="359" Max="90" RW="ALL" />
            <UdLightTime Type="Byte" Pos="360" RW="ALL" />
            <UdL120Time Type="Byte" Pos="361" RW="ALL" />
            </UserDemands>
        """  # noqa: E501
        )
        self.struct.build_accessors([self.xml])
        self.struct._on_set_value = self.set_value_cb
        self.last_pos = None
        self.last_len = None
        self.last_value = None

    def set_value_cb(self, pos, len_, newvalue):
        self.last_pos = pos
        self.last_len = len_
        self.last_value = newvalue

    def test_constructor(self):
        self.assertEqual(self.struct.status_block, b"\0" * 1024)
        self.assertEqual(len(self.struct.accessors), 18)
        self.assertEqual(self.struct.accessors["UdL120"].value, "OFF")

    def atest_set_value_callback(self):
        self.struct.accessors["UdP1"].value = "HI"
        self.assertEqual(self.last_pos, 275)
        self.assertEqual(self.last_len, 2)
        self.assertEqual(self.last_value, 0b1000000000000000)

    def test_observer_callback(self):
        P2_info = {"oldvalue": None, "newvalue": None}

        def P2_Watch(sender, oldvalue, newvalue):
            P2_info["oldvalue"] = oldvalue
            P2_info["newvalue"] = newvalue

        self.struct.accessors["UdP2"].watch(P2_Watch)
        self.struct.replace_status_block_segment(275, b"\x20\x00")
        self.assertEqual(P2_info["newvalue"], "HI")


if __name__ == "__main__":
    unittest.main()

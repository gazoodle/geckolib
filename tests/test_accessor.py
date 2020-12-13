""" Unit tests for the structure accessor class """

import struct
import unittest
import xml.etree.ElementTree as ET

from context import GeckoStructAccessor, GeckoStructure


class TestStructAccessor(unittest.TestCase):
    """ Test the GeckoStructAccessor class """

    def setUp(self):
        # self.spa = MockSpa()
        self.struct = GeckoStructure(self._on_set_value)
        self.struct.set_status_block(
            # Bytes 0-16 are identity values
            b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
            # Bytes 17-18 are a temperature in farenheight 10ths from freezing
            b"\x02\xbe"
            # Bytes 19-20 are a sized bitpos enum
            b"\x11\x70"
            # Bytes 21-22 are an empty sized bitpos enum
            b"\x00\x00"
        )
        self.last_pos = None
        self.last_len = None
        self.last_data = None
        self.last_value = None

    def _on_set_value(self, pos, len_, newvalue):
        self.last_pos = pos
        self.last_len = len_
        self.last_data = struct.pack(">B" if len_ == 1 else ">H", newvalue)
        self.struct.replace_status_block_segment(pos, self.last_data)
        self.last_value = newvalue

    def test_read_byte(self):
        """ Can we read a byte from the structure """
        element = ET.fromstring('<PackBootRev Type="Byte" Pos="5" />')
        accessor = GeckoStructAccessor(self.struct, element)
        self.assertEqual(5, accessor.value)

    @unittest.expectedFailure
    def test_write_byte_fails(self):
        """ Can we write a byte to the structure without the RW tag? """
        element = ET.fromstring('<PackBootRev Type="Byte" Pos="5" />')
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = 6

    def test_write_byte(self):
        """ Can we write a byte to the structure """
        element = ET.fromstring('<PackBootRev Type="Byte" Pos="5" RW="ALL" />')
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = 6
        self.assertEqual(5, self.last_pos)
        self.assertEqual(b"\x06", self.last_data)

    def test_read_word(self):
        """ Can we read a word from the structure """
        element = ET.fromstring('<RealSetPointG Type="Word" Pos="17" />')
        accessor = GeckoStructAccessor(self.struct, element)
        self.assertEqual(702, accessor.value)

    def test_write_word(self):
        """ Can we write a word to the structure """
        element = ET.fromstring('<RealSetPointG Type="Word" Pos="17" RW="ALL"/>')
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = 726
        self.assertEqual(17, self.last_pos)
        self.assertEqual(b"\x02\xd6", self.last_data)

    def test_read_enum(self):
        """ Can we read an enum from the structure """
        element = ET.fromstring(
            '<PackType Type="Enum" Pos="6" '
            'Items="Unknown|inXE|MasIBC|MIA|DJS4|inClear|inXM|K600'
            '|inTerface|inTouch|inYT|K800|inYJ" />'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        self.assertEqual("inXM", accessor.value)

    def test_write_enum(self):
        """ Can we write an enum to the structure """
        element = ET.fromstring(
            '<PackType Type="Enum" Pos="6" '
            'Items="Unknown|inXE|MasIBC|MIA|DJS4|inClear|inXM|K600'
            '|inTerface|inTouch|inYT|K800|inYJ" RW="ALL"/>'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = "inYJ"
        self.assertEqual(6, self.last_pos)
        self.assertEqual(b"\x0c", self.last_data)

    @unittest.expectedFailure
    def test_write_enum_not_member(self):
        """ Can we write an enum to the structure """
        element = ET.fromstring(
            '<PackType Type="Enum" Pos="6" '
            'Items="Unknown|inXE|MasIBC|MIA|DJS4|inClear|inXM|K600'
            '|inTerface|inTouch|inYT|K800|inYJ" RW="ALL"/>'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = "Not A Member"

    def test_read_bool(self):
        """ Can we read a bool from the structure """
        element = ET.fromstring('<RelayStuck Type="Bool" Pos="2" BitPos="6" />')
        accessor = GeckoStructAccessor(self.struct, element)
        self.assertFalse(accessor.value)

    def test_write_bool(self):
        """ Can we write a bool to the structure """
        element = ET.fromstring(
            '<RelayStuck Type="Bool" Pos="2" BitPos="6" RW="ALL" />'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = True
        self.assertEqual(2, self.last_pos)
        self.assertEqual(b"B", self.last_data)

    def test_read_bitpos_enum(self):
        """ Can we read a bitpos enum from the structure """
        element = ET.fromstring(
            '<UdP3 Type="Enum" Pos="3" BitPos="4" MaxItems="4"'
            ' Items="OFF|LO|HI" RW="ALL" />'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        self.assertEqual("OFF", accessor.value)

    def test_write_bitpos_enum(self):
        """ Can we write an enum to the structure """
        element = ET.fromstring(
            '<UdP3 Type="Enum" Pos="3" BitPos="4" MaxItems="4"'
            ' Items="OFF|LO|HI" RW="ALL" />'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = "HI"
        self.assertEqual(3, self.last_pos)
        self.assertEqual(b"#", self.last_data)
        accessor.value = "LO"
        self.assertEqual(b"\x13", self.last_data)
        accessor.value = "OFF"
        self.assertEqual(b"\x03", self.last_data)

    def test_read_sized_bitpos_enum(self):
        """ Can we read a sized bitpos enum from the structure """
        element = ET.fromstring(
            '<UdP2 Type="Enum" Pos="19" BitPos="12" Size="2" '
            'MaxItems="4" Items="OFF|LO|HI" RW="ALL" />'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        self.assertEqual("LO", accessor.value)

    def test_write_sized_bitpos_enum(self):
        """ Can we write a sized bitpos enum to the structure """
        element = ET.fromstring(
            '<UdP2 Type="Enum" Pos="19" BitPos="12" Size="2" '
            'MaxItems="4" Items="OFF|LO|HI" RW="ALL" />'
        )
        accessor = GeckoStructAccessor(self.struct, element)
        accessor.value = "HI"
        self.assertEqual(19, self.last_pos)
        self.assertEqual(
            chr(0b00100001) + chr(0b01110000), self.last_data.decode("latin-1")
        )
        accessor.value = "LO"
        self.assertEqual(
            chr(0b00010001) + chr(0b01110000), self.last_data.decode("latin-1")
        )
        accessor.value = "OFF"
        self.assertEqual(
            chr(0b00000001) + chr(0b01110000), self.last_data.decode("latin-1")
        )

    def test_multiple_write_bitpos_enum(self):
        """ Can we write multiple bitpos enums to the structure """

        element_p1 = ET.fromstring(
            '<UdP1 Type="Enum" Pos="21" BitPos="14" Size="2" '
            'MaxItems="4" Items="OFF|LO|HI" RW="ALL" />'
        )
        element_p2 = ET.fromstring(
            '<UdP2 Type="Enum" Pos="21" BitPos="12" Size="2" '
            'MaxItems="4" Items="OFF|LO|HI" RW="ALL" />'
        )

        accessor_p1 = GeckoStructAccessor(self.struct, element_p1)
        accessor_p2 = GeckoStructAccessor(self.struct, element_p2)

        accessor_p2.value = "HI"
        self.assertEqual(21, self.last_pos)
        self.assertEqual(b"\x20\x00", self.last_data)
        self.assertEqual(2, self.last_len)
        self.assertEqual(2, len(self.last_data))

        accessor_p1.value = "HI"
        self.assertEqual(21, self.last_pos)
        self.assertEqual(b"\xA0\x00", self.last_data)
        self.assertEqual(2, self.last_len)
        self.assertEqual(2, len(self.last_data))


if __name__ == "__main__":
    unittest.main()

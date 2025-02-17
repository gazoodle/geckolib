"""Unit tests for the UDP protocol handlers."""  # noqa: INP001

# ruff: noqa: E501

import unittest
import unittest.mock

from context import (
    GeckoConfigFileProtocolHandler,
)

PARMS = (1, 2, b"SRCID", b"DESTID")


class TestGeckoConfigFileHandler(unittest.TestCase):
    """Config file tests."""

    def test_send_construct_request(self) -> None:
        handler = GeckoConfigFileProtocolHandler.request(1, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>SFILE\x01</DATAS></PACKT>",
        )

    def test_send_construct_response(self) -> None:
        handler = GeckoConfigFileProtocolHandler.response("inXM", 7, 8, parms=PARMS)
        self.assertEqual(
            handler.send_bytes,
            b"<PACKT><SRCCN>DESTID</SRCCN><DESCN>SRCID</DESCN>"
            b"<DATAS>FILES,inXM_C07.xml,inXM_S08.xml</DATAS></PACKT>",
        )

    def test_recv_can_handle(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        self.assertTrue(handler.can_handle(b"SFILE", PARMS))
        self.assertTrue(handler.can_handle(b"FILES", PARMS))
        self.assertFalse(handler.can_handle(b"OTHER", PARMS))

    def test_recv_handle_request(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        handler.handle(b"SFILE\x01", PARMS)
        self.assertFalse(handler.should_remove_handler)
        self.assertEqual(handler._sequence, 1)

    def test_recv_handle_response(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        handler.handle(b"FILES,inXM_C09.xml,inXM_S09.xml", PARMS)
        self.assertTrue(handler.should_remove_handler)
        self.assertEqual(handler.plateform_key, "inXM")
        self.assertEqual(handler.config_version, 9)
        self.assertEqual(handler.log_version, 9)

    @unittest.expectedFailure
    def test_recv_handle_response_error(self) -> None:
        handler = GeckoConfigFileProtocolHandler()
        self.assertTrue(handler.handle(b"FILES,inXM_C09.xml,inYE_S09.xml", PARMS))


if __name__ == "__main__":
    unittest.main()

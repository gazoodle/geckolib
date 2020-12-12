""" Unit tests for the snapshot handlers """

import unittest
import unittest.mock


from context import GeckoSnapshot

LOG_LINES = [
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Snapshot (Heating)",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO SpaPackStruct.xml revision 19.00",  # noqa: E501
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO intouch version EN 88 v15.0",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO intouch version CO 89 v11.0",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Spa pack inXM 186 v3.0",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Low level configuration # 4",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Config version 9",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Log version 9",
    "2020-12-08 19:53:28,310 geckolib.utils.shell INFO Pack type 6",
    "2020-12-08 19:53:28,311 geckolib.utils.shell INFO ['0x4', '0x0', '0x78', '0x0', '0x14', '0x0', '0x14', '0xa', '0x0', '0x28', '0x3c', '0x64', '0x0', '0x10', '0x21', '0x2', '0xbe', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x51', '0x1', '0x2', '0x8', '0x0', '0x2', '0x0', '0x0', '0x0', '0x0', '0x0', '0xc', '0x0', '0x2', '0x0', '0x2', '0x0', '0x0', '0x0', '0x2', '0x1e', '0x14', '0x14', '0x2', '0x14', '0x14', '0x3', '0x9', '0x28', '0x0', '0x0', '0x1', '0x1', '0x28', '0x0', '0x5f', '0x1e', '0xc8', '0x17', '0x0', '0xf', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0xf', '0x2', '0x1', '0x4', '0x2', '0x10', '0x14', '0x20', '0x28', '0x0', '0x1', '0x0', '0x3', '0x0', '0x0', '0xc', '0xa', '0xb', '0x0', '0xe', '0xf', '0x0', '0x0', '0x64', '0x0', '0x50', '0x0', '0x0', '0x0', '0x28', '0xa', '0x0', '0x0', '0x0', '0x0', '0xfc', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x13', '0x0', '0x0', '0x0', '0x8', '0x2', '0xbb', '0x2', '0xd1', '0x2', '0xbe', '0x0', '0x0', '0x0', '0x80', '0x0', '0x2', '0xbe', '0xc8', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x1', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0xe', '0x2', '0x0', '0x6', '0x7', '0x9', '0x9', '0x1', '0xe3', '0xa', '0x0', '0x0', '0xba', '0x3', '0x0', '0x0', '0x1a', '0x2', '0x38', '0x5', '0x0', '0x4', '0x81', '0x8', '0x62', '0x0', '0x0', '0x0', '0x0', '0x0', '0x5', '0x0', '0xff', '0xff', '0xff', '0x0', '0x0', '0x4', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x14', '0xa0', '0xc', '0x0', '0x2', '0xac', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7', '0x8', '0x9', '0xa', '0xb', '0xc', '0xd', '0xe', '0xf', '0x10', '0x11', '0x12', '0x13', '0x14', '0x15', '0x16', '0x17', '0x18', '0x19', '0x1a', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0x69', '0x6e', '0x58', '0x4d', '0x5f', '0x43', '0x30', '0x39', '0x2e', '0x78', '0x6d', '0x6c', '0x0', '0x0', '0x0', '0x0', '0x69', '0x6e', '0x58', '0x4d', '0x5f', '0x53', '0x30', '0x39', '0x2e', '0x78', '0x6d', '0x6c', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0']",  # noqa: E501
]

LOG_LINES_ALT = [
    "INFO:geckolib.utils.shell:Snapshot (EconomyModeActive)",
    "INFO:geckolib.utils.shell:SpaPackStruct.xml revision 19.00",
    "INFO:geckolib.utils.shell:intouch version EN 70 v14.0",
    "INFO:geckolib.utils.shell:intouch version CO 69 v11.0",
    "INFO:geckolib.utils.shell:Spa pack inYT 177 v3.0",
    "INFO:geckolib.utils.shell:Low level configuration # 5",
    "INFO:geckolib.utils.shell:Config version 53",
    "INFO:geckolib.utils.shell:Log version 53",
    "INFO:geckolib.utils.shell:Pack type 10",
    "INFO:geckolib.utils.shell:['0x5', '0x1', '0xe', '0x2', '0xc', '0x0', '0x2', '0x0', '0xc', '0x0', '0x6', '0x0', '0x0', '0x1', '0x0', '0x3', '0x2', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0xe', '0x1', '0x0', '0x0', '0x0', '0x1', '0x2', '0x0', '0x1', '0x1e', '0x0', '0xa', '0x0', '0xa', '0x4', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x11', '0x0', '0x1', '0x30', '0x14', '0x78', '0xf0', '0x2', '0x14', '0x2', '0x4', '0x2', '0x28', '0x28', '0x0', '0x73', '0x1', '0xe', '0x2', '0xd0', '0x0', '0x1', '0x6', '0x1', '0x0', '0x0', '0x0', '0x0', '0x0', '0xf', '0x2', '0x5', '0x0', '0x2', '0x0', '0x2', '0x1', '0x1', '0x3', '0x3', '0x3', '0x5', '0x5', '0x4', '0x4', '0x1', '0x3', '0x6', '0x14', '0xf', '0xf', '0xf', '0xf', '0xf', '0x6', '0x6', '0x6', '0x6', '0x6', '0x6', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x11', '0x0', '0x0', '0x0', '0x0', '0x0', '0x5', '0x0', '0x0', '0x0', '0x0', '0x4', '0x14', '0x23', '0xff', '0xff', '0xff', '0x0', '0x0', '0x1', '0xe', '0x1', '0x40', '0x0', '0x0', '0x6', '0x40', '0x0', '0x0', '0x0', '0x15', '0x6', '0x0', '0xa', '0x3', '0x0', '0x14', '0x17', '0x0', '0x35', '0x35', '0x0', '0xb1', '0x3', '0x0', '0x0', '0x5', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x15', '0x18', '0x1', '0x0', '0x0', '0x0', '0x1', '0x39', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x2', '0x30', '0x1', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x1', '0x2', '0x3', '0x4', '0x5', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0xff', '0x69', '0x6e', '0x59', '0x54', '0x5f', '0x43', '0x35', '0x33', '0x2e', '0x78', '0x6d', '0x6c', '0x0', '0x0', '0x0', '0x0', '0x69', '0x6e', '0x59', '0x54', '0x5f', '0x53', '0x35', '0x33', '0x2e', '0x78', '0x6d', '0x6c', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0']",  # noqa: E501
]

LOG_LINES_CONNECTION = [
    r"2020-11-11 12:49:48,064 geckolib.spa INFO Starting spa connection handshake...",
    r"2020-11-11 12:49:48,064 geckolib.driver.comms DEBUG Send message b'<PACKT><SRCCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</SRCCN><DESCN>SPAXX:XX:XX:XX:XX:XX</DESCN><DATAS>AVERS\x02</DATAS></PACKT>' to ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,108 geckolib.driver.comms DEBUG Receive answer b'<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>APING\x00</DATAS></PACKT>' from ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,124 geckolib.driver.responses DEBUG Ping response received",
    r"2020-11-11 12:49:48,171 geckolib.driver.comms DEBUG Receive answer b'<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>SVERS\x00F\x0e\x00\x00E\x0b\x00</DATAS></PACKT>' from ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,186 geckolib.driver.responses DEBUG Got software version 70 v14.0/69 v11.0, now get channel",  # noqa: E501
    r"2020-11-11 12:49:48,186 geckolib.driver.comms DEBUG Send message b'<PACKT><SRCCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</SRCCN><DESCN>SPAXX:XX:XX:XX:XX:XX</DESCN><DATAS>CURCH\x03</DATAS></PACKT>' to ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,218 geckolib.driver.comms DEBUG Receive answer b'<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>CHCUR\x17F</DATAS></PACKT>' from ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,219 geckolib.driver.responses DEBUG Got channel 23/70, get config",  # noqa: E501
    r"2020-11-11 12:49:48,219 geckolib.driver.comms DEBUG Send message b'<PACKT><SRCCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</SRCCN><DESCN>SPAXX:XX:XX:XX:XX:XX</DESCN><DATAS>SFILE\x04</DATAS></PACKT>' to ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,423 geckolib.driver.comms DEBUG Receive answer b'<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>FILES,inYT_C61.xml,inYT_S61.xml</DATAS></PACKT>' from ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,438 geckolib.driver.responses DEBUG Got spa configuration Type 10 - CFG 61/LOG 61, now ask for initial status block",  # noqa: E501
    r"2020-11-11 12:49:48,438 geckolib.driver.comms DEBUG Send message b'<PACKT><SRCCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</SRCCN><DESCN>SPAXX:XX:XX:XX:XX:XX</DESCN><DATAS>STATU\x05\x00\x00\x04\x00</DATAS></PACKT>' to ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:48,700 geckolib.driver.comms DEBUG Receive answer b",
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x00\x01'\x05\x02\xa8\x02\x0c\x00\x02\x00\x18\x00\t\x00\x00\x01\n\x0c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x01\x00\x01\x02\x00\x01\x1e\x00\x0c\x08</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:48,716 geckolib.driver.responses DEBUG Status block segment # 0 (then #1) length 39, was expecting 0",  # noqa: E501
    r"2020-11-11 12:49:48,812 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x01\x02'\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x00\x010\x1exx\x02\x14\x02\x04\x08((\x00s\x01\x0e\x02\xe4\x00\x01 \x01\x00\x00\x01\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:48,812 geckolib.driver.responses DEBUG Status block segment # 1 (then #2) length 39, was expecting 1",  # noqa: E501
    r"2020-11-11 12:49:48,966 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x02\x03'\x00\x0f\x02\xe5\x00\x02\x00\x02\x01\x01\x03\x03\x03\x05\x05\x04\x04\x01\x03\x06\x14\x0f\x18\x0f\x0f\x14\x06\x06\x06\x06\x06\x06\xf4\x00\x02\x00\x01\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:48,967 geckolib.driver.responses DEBUG Status block segment # 2 (then #3) length 39, was expecting 2",  # noqa: E501
    r"2020-11-11 12:49:49,091 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x03\x04'\x00\x14\x00\x1e\x01\n0@\x80\x00\x83\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,107 geckolib.driver.responses DEBUG Status block segment # 3 (then #4) length 39, was expecting 3",  # noqa: E501
    r"2020-11-11 12:49:49,246 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x04\x05'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,262 geckolib.driver.responses DEBUG Status block segment # 4 (then #5) length 39, was expecting 4",  # noqa: E501
    r"2020-11-11 12:49:49,385 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x05\x06'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,385 geckolib.driver.responses DEBUG Status block segment # 5 (then #6) length 39, was expecting 5",  # noqa: E501
    r"2020-11-11 12:49:49,493 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x06\x07'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,494 geckolib.driver.responses DEBUG Status block segment # 6 (then #7) length 39, was expecting 6",  # noqa: E501
    r"2020-11-11 12:49:49,648 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x07\x08'\x00\x00\x02\xa8\x02\xa8\x00\x00\x00\x00\x00\x00\x00@\n\x00\nK\x00=.\x00==\x01c\x04\x00\x00\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x03</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,663 geckolib.driver.responses DEBUG Status block segment # 7 (then #8) length 39, was expecting 7",  # noqa: E501
    r"2020-11-11 12:49:49,788 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x08\t'\x84\x00\x00\x00\x00\x02\xa4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,804 geckolib.driver.responses DEBUG Status block segment # 8 (then #9) length 39, was expecting 8",  # noqa: E501
    r"2020-11-11 12:49:49,927 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\t\n'\x00\x00\x00\x00\x01\x89\r\x00\x00\x00\x00\x00\x00\x00v\xce\x00\x00\x00\x00\x15\xb2\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:49,928 geckolib.driver.responses DEBUG Status block segment # 9 (then #10) length 39, was expecting 9",  # noqa: E501
    r"2020-11-11 12:49:50,069 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\n\x0b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,069 geckolib.driver.responses DEBUG Status block segment # 10 (then #11) length 39, was expecting 10",  # noqa: E501
    r"2020-11-11 12:49:50,194 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x0b\x0c'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,194 geckolib.driver.responses DEBUG Status block segment # 11 (then #12) length 39, was expecting 11",  # noqa: E501
    r"2020-11-11 12:49:50,333 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x0c\r'\x153456\x97\x98\x99\x9a\xff\xff\xffinYT_C61.xml\x00\x00\x00\x00inYT_S61.xm</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,349 geckolib.driver.responses DEBUG Status block segment # 12 (then #13) length 39, was expecting 12",  # noqa: E501
    r"2020-11-11 12:49:50,474 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\r\x0e'l\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,474 geckolib.driver.responses DEBUG Status block segment # 13 (then #14) length 39, was expecting 13",  # noqa: E501
    r"2020-11-11 12:49:50,613 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x0e\x0f'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,613 geckolib.driver.responses DEBUG Status block segment # 14 (then #15) length 39, was expecting 14",  # noqa: E501
    r"2020-11-11 12:49:50,752 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x0f\x10'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,768 geckolib.driver.responses DEBUG Status block segment # 15 (then #16) length 39, was expecting 15",  # noqa: E501
    r"2020-11-11 12:49:50,894 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x10\x11'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:50,894 geckolib.driver.responses DEBUG Status block segment # 16 (then #17) length 39, was expecting 16",  # noqa: E501
    r"2020-11-11 12:49:51,035 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x11\x12'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,051 geckolib.driver.responses DEBUG Status block segment # 17 (then #18) length 39, was expecting 17",  # noqa: E501
    r"2020-11-11 12:49:51,160 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x12\x13'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,176 geckolib.driver.responses DEBUG Status block segment # 18 (then #19) length 39, was expecting 18",  # noqa: E501
    r"2020-11-11 12:49:51,300 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x13\x14'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,316 geckolib.driver.responses DEBUG Status block segment # 19 (then #20) length 39, was expecting 19",  # noqa: E501
    r"2020-11-11 12:49:51,441 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x14\x15'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,456 geckolib.driver.responses DEBUG Status block segment # 20 (then #21) length 39, was expecting 20",  # noqa: E501
    r"2020-11-11 12:49:51,580 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x15\x16'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,580 geckolib.driver.responses DEBUG Status block segment # 21 (then #22) length 39, was expecting 21",  # noqa: E501
    r"2020-11-11 12:49:51,722 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x16\x17'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,738 geckolib.driver.responses DEBUG Status block segment # 22 (then #23) length 39, was expecting 22",  # noqa: E501
    r"2020-11-11 12:49:51,864 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x17\x18'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:51,879 geckolib.driver.responses DEBUG Status block segment # 23 (then #24) length 39, was expecting 23",  # noqa: E501
    r"2020-11-11 12:49:51,990 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x18\x19'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:52,006 geckolib.driver.responses DEBUG Status block segment # 24 (then #25) length 39, was expecting 24",  # noqa: E501
    r"2020-11-11 12:49:52,114 geckolib.driver.comms DEBUG Receive answer b"
    r"<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x19\x1a'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>"  # noqa: E501
    r" from ('192.168.XXX.XXX', 10022)",
    r"2020-11-11 12:49:52,130 geckolib.driver.responses DEBUG Status block segment # 25 (then #26) length 39, was expecting 25",  # noqa: E501
    r"2020-11-11 12:49:52,224 geckolib.driver.comms DEBUG Receive answer b'<PACKT><SRCCN>SPAXX:XX:XX:XX:XX:XX</SRCCN><DESCN>IOS02ac6d28-42d0-41e3-ad22-274d0aa491da</DESCN><DATAS>STATV\x1a\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00</DATAS></PACKT>' from ('192.168.XXX.XXX', 10022)",  # noqa: E501
    r"2020-11-11 12:49:52,240 geckolib.driver.responses DEBUG Status block segment # 26 (then #0) length 10, was expecting 26",  # noqa: E501
    r"2020-11-11 12:49:52,261 geckolib.spa DEBUG Temperature keys to decorate {'MaxSetpointG', 'MinSetpointG', 'DisplayedTempG', 'SetpointG', 'RhWaterTemp', 'RealSetPointG'}",  # noqa: E501
    r"2020-11-11 12:49:52,261 geckolib.driver.spastruct DEBUG Accessor PackType @ 289, Enum raw data = a",  # noqa: E501
    r"2020-11-11 12:49:52,262 geckolib.driver.spastruct DEBUG Enum accessor PackType adjusted data = inYT\n",  # noqa: E501
    r"2020-11-11 12:49:52,262 geckolib.driver.spastruct DEBUG Accessor PackConfID @ 297, Word raw data = 163",  # noqa: E501
    r"2020-11-11 12:49:52,262 geckolib.driver.spastruct DEBUG Accessor PackConfRev @ 299, Byte raw data = 4",  # noqa: E501
    r"2020-11-11 12:49:52,262 geckolib.driver.spastruct DEBUG Accessor PackConfRel @ 300, Byte raw data = 0",  # noqa: E501
    r"2020-11-11 12:49:52,262 geckolib.driver.spastruct DEBUG Accessor ConfigNumber @ 0, Byte raw data = 5",  # noqa: E501
    r"2020-11-11 12:49:52,262 geckolib.spa INFO Spa is connected",
]


class TestGeckoSnapshot(unittest.TestCase):
    """ Test the GeckoSnapshot classes """

    def test_constructor(self):
        snapshot = GeckoSnapshot()
        self.assertTrue(snapshot)

    def test_parselines(self):
        snapshot = GeckoSnapshot()
        for line in LOG_LINES:
            snapshot.parse(line)
        self.assertEqual(snapshot.name, "Heating")
        self.assertEqual(snapshot.timestamp, "2020-12-08 19:53:28")
        self.assertEqual(snapshot.spapack, "inXM 186 v3.0")
        self.assertTupleEqual(snapshot.intouch_EN, (88, 15, 0))
        self.assertTupleEqual(snapshot.intouch_CO, (89, 11, 0))
        self.assertEqual(snapshot.config_version, 9)
        self.assertEqual(snapshot.log_version, 9)
        self.assertEqual(snapshot.bytes[6:8], b"\x14\x0a")
        self.assertEqual(
            snapshot.bytes[29:39], b"\x00\x02\x00\x00\x00\x00\x00\x0c\x00\x02"
        )

    def test_parselines_alt(self):
        snapshot = GeckoSnapshot()
        for line in LOG_LINES_ALT:
            snapshot.parse(line)
        self.assertEqual(snapshot.name, "EconomyModeActive")
        self.assertEqual(snapshot.spapack, "inYT 177 v3.0")
        self.assertTupleEqual(snapshot.intouch_EN, (70, 14, 0))
        self.assertTupleEqual(snapshot.intouch_CO, (69, 11, 0))
        self.assertEqual(snapshot.config_version, 53)
        self.assertEqual(snapshot.log_version, 53)
        self.assertEqual(snapshot.bytes[6:8], b"\x02\x00")
        self.assertEqual(
            snapshot.bytes[29:39], b"\x00\x00\x01\x02\x00\x01\x1e\x00\n\x00"
        )

    def test_parselines_connection(self):
        snapshot = GeckoSnapshot()
        for line in LOG_LINES_CONNECTION:
            snapshot.parse(line)
        self.assertEqual(snapshot.spapack, "inYT 163 v4.0")
        self.assertTupleEqual(snapshot.intouch_EN, (70, 14, 0))
        self.assertTupleEqual(snapshot.intouch_CO, (69, 11, 0))
        self.assertEqual(snapshot.config_version, 61)
        self.assertEqual(snapshot.log_version, 61)
        self.assertEqual(snapshot.bytes[6:8], b"\x02\x00")
        self.assertEqual(
            snapshot.bytes[29:39], b"\x01\x00\x01\x02\x00\x01\x1e\x00\x0c\x08"
        )
        self.assertEqual(snapshot.packtype, "inYT")


if __name__ == "__main__":
    unittest.main()
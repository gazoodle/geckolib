#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v2'
"""

from . import (
    GeckoByteStructAccessor,
    GeckoWordStructAccessor,
    GeckoTimeStructAccessor,
    GeckoBoolStructAccessor,
    GeckoEnumStructAccessor,
    GeckoTempStructAccessor,
)

# Constants for this class
ASSAKQ = 11
BMJVHF = "".join(
    chr(c) for c in [80, 114, 111, 103, 49, 82, 117, 110, 116, 105, 109, 101]
)
CQBMJV = 0
CVYYPI = "".join(
    chr(c) for c in [80, 114, 111, 103, 50, 82, 117, 110, 116, 105, 109, 101]
)
ECVYYP = 5
FTHECV = "".join(chr(c) for c in [79, 78])
HECVYY = "".join(
    chr(c) for c in [80, 114, 111, 103, 50, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
HFTHEC = "".join(chr(c) for c in [79, 70, 70])
IPIVLA = 10
IVLASS = "".join(chr(c) for c in [67])
JVHFTH = "".join(chr(c) for c in [80, 114, 111, 103, 49, 65, 114, 111, 109, 97])
KQXPIC = "".join(chr(c) for c in [76, 73])
LASSAK = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
MJVHFT = 2
PIPIVL = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
PIVLAS = "".join(chr(c) for c in [70])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
SAKQXP = 13
SSAKQX = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
VHFTHE = 4
VYYPIP = 7
XPICXQ = 2
YPIPIV = 9
YYPIPI = "".join(chr(c) for c in [80, 114, 111, 103, 50, 65, 114, 111, 109, 97])
ZCQBMJ = "".join(
    chr(c) for c in [80, 114, 111, 103, 49, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
AKQXPI = []
QXPICX = [KQXPIC]
THECVY = [HFTHEC, FTHECV]
VLASSA = [PIVLAS, IVLASS]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return XPICXQ

    @property
    def output_keys(self):
        return AKQXPI

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoTempStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoWordStructAccessor(self.struct, BMJVHF, MJVHFT, QBMJVH),
            JVHFTH: GeckoEnumStructAccessor(
                self.struct, JVHFTH, VHFTHE, None, THECVY, None, None, QBMJVH
            ),
            HECVYY: GeckoTempStructAccessor(self.struct, HECVYY, ECVYYP, QBMJVH),
            CVYYPI: GeckoWordStructAccessor(self.struct, CVYYPI, VYYPIP, QBMJVH),
            YYPIPI: GeckoEnumStructAccessor(
                self.struct, YYPIPI, YPIPIV, None, THECVY, None, None, QBMJVH
            ),
            PIPIVL: GeckoEnumStructAccessor(
                self.struct, PIPIVL, IPIVLA, None, VLASSA, None, None, QBMJVH
            ),
            LASSAK: GeckoTempStructAccessor(self.struct, LASSAK, ASSAKQ, QBMJVH),
            SSAKQX: GeckoTempStructAccessor(self.struct, SSAKQX, SAKQXP, QBMJVH),
        }

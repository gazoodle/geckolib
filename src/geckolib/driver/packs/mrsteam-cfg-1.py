#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'MrSteam v1'
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
ASSAKQ = "".join(chr(c) for c in [76, 73])
BMJVHF = "".join(
    chr(c) for c in [80, 114, 111, 103, 49, 82, 117, 110, 116, 105, 109, 101]
)
CQBMJV = 0
CVYYPI = "".join(
    chr(c) for c in [80, 114, 111, 103, 50, 82, 117, 110, 116, 105, 109, 101]
)
ECVYYP = 4
FTHECV = "".join(chr(c) for c in [79, 78])
HECVYY = "".join(
    chr(c) for c in [80, 114, 111, 103, 50, 83, 101, 116, 112, 111, 105, 110, 116]
)
HFTHEC = "".join(chr(c) for c in [79, 70, 70])
IPIVLA = 8
IVLASS = "".join(chr(c) for c in [67])
JVHFTH = "".join(chr(c) for c in [80, 114, 111, 103, 49, 65, 114, 111, 109, 97])
MJVHFT = 1
PIPIVL = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
PIVLAS = "".join(chr(c) for c in [70])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
SAKQXP = 1
VHFTHE = 3
VYYPIP = 5
YPIPIV = 7
YYPIPI = "".join(chr(c) for c in [80, 114, 111, 103, 50, 65, 114, 111, 109, 97])
ZCQBMJ = "".join(
    chr(c) for c in [80, 114, 111, 103, 49, 83, 101, 116, 112, 111, 105, 110, 116]
)
LASSAK = []
SSAKQX = [ASSAKQ]
THECVY = [HFTHEC, FTHECV]
VLASSA = [PIVLAS, IVLASS]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return SAKQXP

    @property
    def output_keys(self):
        return LASSAK

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoWordStructAccessor(self.struct, BMJVHF, MJVHFT, QBMJVH),
            JVHFTH: GeckoEnumStructAccessor(
                self.struct, JVHFTH, VHFTHE, None, THECVY, None, None, QBMJVH
            ),
            HECVYY: GeckoByteStructAccessor(self.struct, HECVYY, ECVYYP, QBMJVH),
            CVYYPI: GeckoWordStructAccessor(self.struct, CVYYPI, VYYPIP, QBMJVH),
            YYPIPI: GeckoEnumStructAccessor(
                self.struct, YYPIPI, YPIPIV, None, THECVY, None, None, QBMJVH
            ),
            PIPIVL: GeckoEnumStructAccessor(
                self.struct, PIPIVL, IPIVLA, None, VLASSA, None, None, QBMJVH
            ),
        }

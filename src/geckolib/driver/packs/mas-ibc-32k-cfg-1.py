#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'MAS-IBC-32K v1'
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
AHEOCT = 8
AKQXPI = "".join(chr(c) for c in [66, 65, 83, 73, 67])
ASSAKQ = "".join(chr(c) for c in [76, 76, 95, 67, 104, 114, 111, 109, 111])
BMJVHF = "".join(chr(c) for c in [68, 85, 65, 76])
CQBMJV = 0
CTHBSK = 1
CVYYPI = "".join(chr(c) for c in [73, 110, 116, 101, 110, 115, 105, 116, 121, 52])
ECVYYP = "".join(chr(c) for c in [73, 110, 116, 101, 110, 115, 105, 116, 121, 51])
EOCTHB = "".join(chr(c) for c in [76, 73])
FTHECV = 1
FXQGLR = "".join(
    chr(c) for c in [76, 76, 95, 67, 111, 109, 102, 111, 114, 116, 74, 101, 116]
)
GLRAHE = "".join(chr(c) for c in [65, 67, 84, 73, 86, 65, 84, 69])
HECVYY = "".join(chr(c) for c in [73, 110, 116, 101, 110, 115, 105, 116, 121, 50])
HFTHEC = "".join(chr(c) for c in [76, 76, 95, 72, 101, 97, 116, 101, 114, 95, 49])
ICXQIE = "".join(chr(c) for c in [77, 80, 51])
IEFXQG = "".join(chr(c) for c in [72, 79, 84, 69, 76])
IPIVLA = 3
IVLASS = "".join(chr(c) for c in [72, 73, 71, 72])
JVHFTH = "".join(
    chr(c) for c in [68, 85, 65, 76, 95, 76, 73, 84, 69, 83, 84, 82, 69, 77, 69]
)
KQXPIC = "".join(chr(c) for c in [68, 69, 76, 85, 88, 69])
MJVHFT = "".join(
    chr(c) for c in [68, 85, 65, 76, 95, 84, 72, 69, 82, 77, 79, 80, 76, 65, 67, 69]
)
PICXQI = 5
PIPIVL = "".join(chr(c) for c in [76, 76, 95, 66, 108, 111, 119, 101, 114])
PIVLAS = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
QBMJVH = "".join(chr(c) for c in [83, 73, 78, 71, 76, 69])
QGLRAH = "".join(chr(c) for c in [68, 69, 65, 67, 84, 73, 86, 65, 84, 69])
QIEFXQ = 6
RAHEOC = "".join(
    chr(c) for c in [76, 76, 95, 65, 114, 111, 109, 97, 99, 108, 111, 117, 100]
)
SAKQXP = "".join(chr(c) for c in [78, 79, 78, 69])
SSAKQX = 4
THECVY = "".join(chr(c) for c in [73, 110, 116, 101, 110, 115, 105, 116, 121, 49])
VLASSA = "".join(chr(c) for c in [76, 79, 87])
XPICXQ = "".join(chr(c) for c in [76, 76, 95, 65, 117, 100, 105, 111])
XQGLRA = 7
XQIEFX = "".join(chr(c) for c in [76, 76, 95, 77, 101, 110, 117])
YPIPIV = 2
YYPIPI = "".join(chr(c) for c in [76, 76, 95, 72, 101, 97, 116, 101, 114, 95, 50])
ZCQBMJ = "".join(chr(c) for c in [76, 76, 95, 66, 97, 99, 107, 114, 101, 115, 116])
CXQIEF = [SAKQXP, ICXQIE]
EFXQGL = [PIVLAS, IEFXQG]
HEOCTH = []
LASSAK = [PIVLAS, IVLASS, VLASSA]
LRAHEO = [QGLRAH, GLRAHE]
OCTHBS = [EOCTHB]
QXPICX = [SAKQXP, AKQXPI, KQXPIC]
VHFTHE = [QBMJVH, BMJVHF, MJVHFT, JVHFTH]
VYYPIP = [THECVY, HECVYY, ECVYYP, CVYYPI]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return CTHBSK

    @property
    def output_keys(self):
        return HEOCTH

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoEnumStructAccessor(
                self.struct, ZCQBMJ, CQBMJV, None, VHFTHE, None, None, None
            ),
            HFTHEC: GeckoEnumStructAccessor(
                self.struct, HFTHEC, FTHECV, None, VYYPIP, None, None, None
            ),
            YYPIPI: GeckoEnumStructAccessor(
                self.struct, YYPIPI, YPIPIV, None, VYYPIP, None, None, None
            ),
            PIPIVL: GeckoEnumStructAccessor(
                self.struct, PIPIVL, IPIVLA, None, LASSAK, None, None, None
            ),
            ASSAKQ: GeckoEnumStructAccessor(
                self.struct, ASSAKQ, SSAKQX, None, QXPICX, None, None, None
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, CXQIEF, None, None, None
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, QIEFXQ, None, EFXQGL, None, None, None
            ),
            FXQGLR: GeckoEnumStructAccessor(
                self.struct, FXQGLR, XQGLRA, None, LRAHEO, None, None, None
            ),
            RAHEOC: GeckoEnumStructAccessor(
                self.struct, RAHEOC, AHEOCT, None, LRAHEO, None, None, None
            ),
        }

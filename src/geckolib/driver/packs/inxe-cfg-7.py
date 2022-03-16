#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v7'
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
AHEOCT = 1
AKQXPI = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        79,
        84,
        68,
        117,
        114,
        97,
        116,
        105,
        111,
        110,
        50,
        52,
        72,
    ]
)
ASSAKQ = 36
BFEGZU = 0
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
CBFEGZ = 51
CQBMJV = 0
CTHBSK = 18
CVYYPI = 17
CXQIEF = "".join(chr(c) for c in [67, 80])
ECVYYP = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
EFXQGL = 15
EGZUQE = 1
EOCTHB = 16
EXLSXU = "".join(chr(c) for c in [65, 109, 80, 109])
FEGZUQ = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
FTHECV = 31
FXQGLR = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
GLRAHE = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
GZUQEX = "".join(
    chr(c)
    for c in [
        69,
        99,
        111,
        110,
        67,
        111,
        110,
        116,
        114,
        111,
        108,
        97,
        98,
        108,
        101,
        77,
        97,
        110,
        117,
        97,
        108,
        108,
        121,
    ]
)
HBSKSO = "".join(chr(c) for c in [67])
HECVYY = 32
HEOCTH = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
HFTHEC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
HIUSOO = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
HUOJRJ = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
ICXQIE = 14
IEFXQG = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
IPIVLA = "".join(
    chr(c) for c in [79, 84, 65, 99, 116, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IUSOOQ = 3
IVLASS = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
JHIUSO = 5
JRJHIU = 4
JUTYEK = "".join(chr(c) for c in [76, 73])
JVHFTH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
KPHUOJ = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
KQXPIC = 40
KSOKPH = 46
LASSAK = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 110, 84, 105, 109, 101]
)
LRAHEO = 43
MCBFEG = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
MJVHFT = 27
NRSJMC = 50
OCTHBS = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
OJRJHI = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
OKPHUO = 48
OOQNRS = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
OQNRSJ = 8
PHUOJR = 29
PICXQI = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
PIVLAS = 33
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 19
QNRSJM = "".join(
    chr(c)
    for c in [
        69,
        99,
        111,
        110,
        80,
        114,
        111,
        103,
        65,
        118,
        97,
        105,
        108,
        97,
        98,
        108,
        101,
    ]
)
QXPICX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
RAHEOC = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
RJHIUS = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
RSJMCB = "".join(chr(c) for c in [78, 65])
SAKQXP = 38
SJMCBF = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
SKSOKP = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SOKPHU = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SOOQNR = 7
SSAKQX = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 102, 102, 84, 105, 109, 101]
)
SXUJUT = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
THBSKS = "".join(chr(c) for c in [70])
THECVY = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
TYEKCW = 7
UOJRJH = 30
UQEXLS = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
USOOQN = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
VHFTHE = 26
VLASSA = 35
VYYPIP = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
XLSXUJ = "".join(chr(c) for c in [50, 52, 104])
XPICXQ = 42
XQGLRA = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
XQIEFX = "".join(chr(c) for c in [80, 49])
XUJUTY = 44
YPIPIV = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
YYPIPI = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZUQEXL = 2
BSKSOK = [THBSKS, HBSKSO]
JMCBFE = [RSJMCB, SJMCBF]
LSXUJU = [RSJMCB, EXLSXU, XLSXUJ]
PIPIVL = [VYYPIP, YYPIPI, YPIPIV]
QGLRAH = [FXQGLR, XQGLRA]
QIEFXQ = [CXQIEF, XQIEFX]
UJUTYE = []
UTYEKC = [JUTYEK]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return TYEKCW

    @property
    def output_keys(self):
        return UJUTYE

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoByteStructAccessor(self.struct, BMJVHF, MJVHFT, QBMJVH),
            JVHFTH: GeckoByteStructAccessor(self.struct, JVHFTH, VHFTHE, QBMJVH),
            HFTHEC: GeckoByteStructAccessor(self.struct, HFTHEC, FTHECV, QBMJVH),
            THECVY: GeckoByteStructAccessor(self.struct, THECVY, HECVYY, QBMJVH),
            ECVYYP: GeckoEnumStructAccessor(
                self.struct, ECVYYP, CVYYPI, None, PIPIVL, None, None, QBMJVH
            ),
            IPIVLA: GeckoTempStructAccessor(self.struct, IPIVLA, PIVLAS, QBMJVH),
            IVLASS: GeckoByteStructAccessor(self.struct, IVLASS, VLASSA, QBMJVH),
            LASSAK: GeckoWordStructAccessor(self.struct, LASSAK, ASSAKQ, QBMJVH),
            SSAKQX: GeckoWordStructAccessor(self.struct, SSAKQX, SAKQXP, QBMJVH),
            AKQXPI: GeckoWordStructAccessor(self.struct, AKQXPI, KQXPIC, QBMJVH),
            QXPICX: GeckoByteStructAccessor(self.struct, QXPICX, XPICXQ, QBMJVH),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, QIEFXQ, None, None, QBMJVH
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, None, QGLRAH, None, None, QBMJVH
            ),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoTempStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, EOCTHB, None, QIEFXQ, None, None, QBMJVH
            ),
            OCTHBS: GeckoEnumStructAccessor(
                self.struct, OCTHBS, CTHBSK, None, BSKSOK, None, None, QBMJVH
            ),
            SKSOKP: GeckoTempStructAccessor(self.struct, SKSOKP, KSOKPH, QBMJVH),
            SOKPHU: GeckoTempStructAccessor(self.struct, SOKPHU, OKPHUO, QBMJVH),
            KPHUOJ: GeckoByteStructAccessor(self.struct, KPHUOJ, PHUOJR, QBMJVH),
            HUOJRJ: GeckoByteStructAccessor(self.struct, HUOJRJ, UOJRJH, QBMJVH),
            OJRJHI: GeckoByteStructAccessor(self.struct, OJRJHI, JRJHIU, QBMJVH),
            RJHIUS: GeckoTimeStructAccessor(self.struct, RJHIUS, JHIUSO, QBMJVH),
            HIUSOO: GeckoTimeStructAccessor(self.struct, HIUSOO, IUSOOQ, QBMJVH),
            USOOQN: GeckoTimeStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoTimeStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, NRSJMC, None, JMCBFE, None, None, QBMJVH
            ),
            MCBFEG: GeckoBoolStructAccessor(
                self.struct, MCBFEG, CBFEGZ, BFEGZU, QBMJVH
            ),
            FEGZUQ: GeckoBoolStructAccessor(
                self.struct, FEGZUQ, CBFEGZ, EGZUQE, QBMJVH
            ),
            GZUQEX: GeckoBoolStructAccessor(
                self.struct, GZUQEX, CBFEGZ, ZUQEXL, QBMJVH
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, None, LSXUJU, None, None, QBMJVH
            ),
            SXUJUT: GeckoWordStructAccessor(self.struct, SXUJUT, XUJUTY, QBMJVH),
        }

#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v1'
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
AHEOCT = "".join(chr(c) for c in [72, 50, 79, 50, 69, 114, 114])
AKQXPI = "".join(chr(c) for c in [72, 111, 117, 114, 115])
AONPYY = 279
ASSAKQ = 263
BFEGZU = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
BMJVHF = "".join(chr(c) for c in [79, 78])
BSKSOK = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 51])
CBFEGZ = "".join(chr(c) for c in [75, 54, 48, 48])
CQBMJV = 257
CTHBSK = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 57])
CVYYPI = 3
CWAONP = 278
CXQIEF = "".join(chr(c) for c in [78, 111, 75, 101, 121, 112, 97, 100])
ECVYYP = "".join(chr(c) for c in [67, 104, 114, 111, 109, 97, 83, 116, 97, 116, 101])
EFXQGL = "".join(chr(c) for c in [83, 108, 97, 118, 101, 77, 111, 100, 101])
EGZUQE = "".join(chr(c) for c in [105, 110, 89, 84])
EKCWAO = 277
EOCTHB = 4
EXLSXU = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
FEGZUQ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
FTHECV = "".join(chr(c) for c in [80, 97, 117, 115, 101])
FXQGLR = 259
GLRAHE = 260
GZUQEX = "".join(
    chr(c) for c in [67, 111, 108, 111, 114, 95, 75, 101, 121, 112, 97, 100]
)
HBSKSO = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 50])
HECVYY = "".join(chr(c) for c in [68, 105, 97, 103, 110, 111, 115, 116, 105, 99])
HEOCTH = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 50, 79, 50, 69, 114, 114])
HFTHEC = "".join(chr(c) for c in [65, 76, 76])
HIUSOO = 271
HUOJRJ = 7
ICXQIE = 2658
IEFXQG = 5
IPIVLA = "".join(chr(c) for c in [80, 114, 111, 103, 50])
IUSOOQ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
IUXFEF = 256
IVLASS = "".join(
    chr(c) for c in [85, 115, 101, 114, 83, 101, 116, 112, 111, 105, 110, 116]
)
JHIUSO = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
JMCBFE = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
JRJHIU = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
JVHFTH = 0
KCWAON = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
KPHUOJ = 6
KQXPIC = 256
KSOKPH = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 53])
LASSAK = "".join(chr(c) for c in [85, 115, 101, 114, 82, 117, 110, 116, 105, 109, 101])
LRAHEO = "".join(chr(c) for c in [80, 114, 114, 50, 69, 114, 114])
LSXUJU = "".join(chr(c) for c in [49, 54, 75])
MCBFEG = "".join(chr(c) for c in [105, 110, 88, 77])
NPYYLI = 280
NRSJMC = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
OCTHBS = "".join(chr(c) for c in [75, 101, 121, 83, 116, 117, 99, 107, 69, 114, 114])
OJRJHI = 267
OKPHUO = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 55])
ONPYYL = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
OOQNRS = 273
OQNRSJ = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
PHUOJR = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 56])
PICXQI = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 68, 101, 116, 101, 99, 116, 101, 100]
)
PIPIVL = "".join(chr(c) for c in [80, 114, 111, 103, 49])
QBMJVH = "".join(chr(c) for c in [79, 70, 70])
QGLRAH = "".join(
    chr(c) for c in [80, 111, 119, 101, 114, 70, 97, 105, 108, 69, 114, 114]
)
QIEFXQ = "".join(
    chr(c) for c in [69, 120, 112, 114, 101, 115, 115, 67, 121, 99, 108, 101]
)
QNRSJM = "".join(chr(c) for c in [105, 110, 88, 69])
QXPICX = "".join(
    chr(c) for c in [69, 120, 116, 101, 114, 110, 97, 108, 80, 114, 111, 98, 101]
)
RAHEOC = "".join(chr(c) for c in [80, 114, 114, 49, 69, 114, 114])
RJHIUS = 269
RSJMCB = "".join(chr(c) for c in [77, 73, 65])
SAKQXP = 265
SJMCBF = "".join(chr(c) for c in [68, 74, 83, 52])
SKSOKP = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 52])
SOKPHU = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 54])
SOOQNR = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
SSAKQX = "".join(chr(c) for c in [85, 115, 101, 114, 65, 114, 111, 109, 97])
SXUJUT = "".join(chr(c) for c in [51, 50, 75])
THBSKS = 266
THECVY = 1
TYEKCW = 275
UJUTYE = "".join(chr(c) for c in [54, 52, 75])
UOJRJH = "".join(chr(c) for c in [77, 97, 120, 82, 117, 110, 116, 105, 109, 101])
UQEXLS = "".join(chr(c) for c in [77, 114, 83, 116, 101, 97, 109])
USOOQN = 272
UTYEKC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
UXFEFJ = 280
VHFTHE = 2
VLASSA = 262
VYYPIP = "".join(
    chr(c) for c in [83, 101, 108, 101, 99, 116, 101, 100, 80, 114, 111, 103]
)
WAONPY = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
XLSXUJ = 274
XPICXQ = 258
XQGLRA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 72, 101, 97, 116, 101, 114, 83, 116, 97, 116, 101]
)
XQIEFX = "".join(
    chr(c) for c in [78, 111, 82, 101, 103, 117, 108, 97, 116, 105, 111, 110]
)
XUJUTY = "".join(chr(c) for c in [52, 56, 75])
YEKCWA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
YPIPIV = "".join(chr(c) for c in [85, 115, 101, 114])
YYLIUX = "".join(chr(c) for c in [76, 73])
YYPIPI = 261
ZCQBMJ = "".join(chr(c) for c in [77, 111, 100, 101])
ZUQEXL = "".join(chr(c) for c in [105, 110, 89, 74])
JUTYEK = [LSXUJU, SXUJUT, XUJUTY, UJUTYE]
LIUXFE = [QGLRAH, AHEOCT, RAHEOC, LRAHEO, HEOCTH, OCTHBS]
MJVHFT = [QBMJVH, BMJVHF]
PIVLAS = [YPIPIV, PIPIVL, IPIVLA]
PYYLIU = []
QEXLSX = [
    OQNRSJ,
    QNRSJM,
    NRSJMC,
    RSJMCB,
    SJMCBF,
    JMCBFE,
    MCBFEG,
    CBFEGZ,
    BFEGZU,
    FEGZUQ,
    EGZUQE,
    GZUQEX,
    ZUQEXL,
    UQEXLS,
]
YLIUXF = [YYLIUX]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return THECVY

    @property
    def begin(self):
        return IUXFEF

    @property
    def end(self):
        return UXFEFJ

    @property
    def all_device_keys(self):
        return YLIUXF

    @property
    def user_demand_keys(self):
        return PYYLIU

    @property
    def error_keys(self):
        return LIUXFE

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoEnumStructAccessor(
                self.struct, ZCQBMJ, CQBMJV, JVHFTH, MJVHFT, None, VHFTHE, HFTHEC
            ),
            FTHECV: GeckoBoolStructAccessor(
                self.struct, FTHECV, CQBMJV, THECVY, HFTHEC
            ),
            HECVYY: GeckoBoolStructAccessor(
                self.struct, HECVYY, CQBMJV, VHFTHE, HFTHEC
            ),
            ECVYYP: GeckoEnumStructAccessor(
                self.struct, ECVYYP, CQBMJV, CVYYPI, MJVHFT, None, VHFTHE, HFTHEC
            ),
            VYYPIP: GeckoEnumStructAccessor(
                self.struct, VYYPIP, YYPIPI, None, PIVLAS, None, None, HFTHEC
            ),
            IVLASS: GeckoByteStructAccessor(self.struct, IVLASS, VLASSA, HFTHEC),
            LASSAK: GeckoWordStructAccessor(self.struct, LASSAK, ASSAKQ, HFTHEC),
            SSAKQX: GeckoEnumStructAccessor(
                self.struct, SSAKQX, SAKQXP, None, MJVHFT, None, None, HFTHEC
            ),
            AKQXPI: GeckoByteStructAccessor(self.struct, AKQXPI, KQXPIC, None),
            QXPICX: GeckoBoolStructAccessor(self.struct, QXPICX, XPICXQ, JVHFTH, None),
            PICXQI: GeckoBoolStructAccessor(self.struct, PICXQI, ICXQIE, THECVY, None),
            CXQIEF: GeckoBoolStructAccessor(self.struct, CXQIEF, XPICXQ, VHFTHE, None),
            XQIEFX: GeckoBoolStructAccessor(self.struct, XQIEFX, XPICXQ, CVYYPI, None),
            QIEFXQ: GeckoBoolStructAccessor(self.struct, QIEFXQ, XPICXQ, IEFXQG, None),
            EFXQGL: GeckoEnumStructAccessor(
                self.struct, EFXQGL, FXQGLR, THECVY, MJVHFT, None, VHFTHE, None
            ),
            XQGLRA: GeckoEnumStructAccessor(
                self.struct, XQGLRA, FXQGLR, CVYYPI, MJVHFT, None, VHFTHE, None
            ),
            QGLRAH: GeckoBoolStructAccessor(self.struct, QGLRAH, GLRAHE, JVHFTH, None),
            LRAHEO: GeckoBoolStructAccessor(self.struct, LRAHEO, GLRAHE, THECVY, None),
            RAHEOC: GeckoBoolStructAccessor(self.struct, RAHEOC, GLRAHE, VHFTHE, None),
            AHEOCT: GeckoBoolStructAccessor(self.struct, AHEOCT, GLRAHE, CVYYPI, None),
            HEOCTH: GeckoBoolStructAccessor(self.struct, HEOCTH, GLRAHE, EOCTHB, None),
            OCTHBS: GeckoBoolStructAccessor(self.struct, OCTHBS, GLRAHE, IEFXQG, None),
            CTHBSK: GeckoBoolStructAccessor(self.struct, CTHBSK, THBSKS, JVHFTH, None),
            HBSKSO: GeckoBoolStructAccessor(self.struct, HBSKSO, THBSKS, THECVY, None),
            BSKSOK: GeckoBoolStructAccessor(self.struct, BSKSOK, THBSKS, VHFTHE, None),
            SKSOKP: GeckoBoolStructAccessor(self.struct, SKSOKP, THBSKS, CVYYPI, None),
            KSOKPH: GeckoBoolStructAccessor(self.struct, KSOKPH, THBSKS, EOCTHB, None),
            SOKPHU: GeckoBoolStructAccessor(self.struct, SOKPHU, THBSKS, IEFXQG, None),
            OKPHUO: GeckoBoolStructAccessor(self.struct, OKPHUO, THBSKS, KPHUOJ, None),
            PHUOJR: GeckoBoolStructAccessor(self.struct, PHUOJR, THBSKS, HUOJRJ, None),
            UOJRJH: GeckoWordStructAccessor(self.struct, UOJRJH, OJRJHI, None),
            JRJHIU: GeckoWordStructAccessor(self.struct, JRJHIU, RJHIUS, None),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, None),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, None),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, None, QEXLSX, None, None, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, JVHFTH, JUTYEK, None, EOCTHB, None
            ),
            UTYEKC: GeckoWordStructAccessor(self.struct, UTYEKC, TYEKCW, None),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, None),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, None),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, None),
            ONPYYL: GeckoByteStructAccessor(self.struct, ONPYYL, NPYYLI, None),
        }

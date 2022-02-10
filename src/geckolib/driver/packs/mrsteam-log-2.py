#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v2'
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
ACCPQI = "".join(chr(c) for c in [68, 74, 83, 52])
AKQXPI = "".join(chr(c) for c in [72, 111, 117, 114, 115])
AONPYY = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 79, 117, 116, 112, 117, 116]
)
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 103, 49])
BFEGZU = "".join(chr(c) for c in [78, 79, 95, 84, 83, 67])
BLKXSJ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
BMJVHF = "".join(chr(c) for c in [79, 78])
BSKSOK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 72, 101, 97, 116, 101, 114, 83, 116, 97, 116, 101]
)
CBFEGZ = 277
CCPQIP = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
CPQIPO = "".join(chr(c) for c in [105, 110, 88, 77])
CQBMJV = 256
CTHBSK = "".join(
    chr(c) for c in [69, 120, 112, 114, 101, 115, 115, 67, 121, 99, 108, 101]
)
CWAONP = 295
CXQIEF = "".join(chr(c) for c in [80, 97, 117, 115, 101, 83, 116, 97, 116, 101])
ECVYYP = 258
EFJTAC = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
EFXQGL = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 68, 101, 116, 101, 99, 116, 101, 100]
)
EGZUQE = "".join(chr(c) for c in [84, 83, 67, 95, 53, 51])
EKCWAO = 293
EOCTHB = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 80, 114, 111, 98, 101])
EXLSXU = 298
FEFJTA = 285
FEGZUQ = "".join(chr(c) for c in [83, 67, 95, 53, 52])
FJTACC = "".join(chr(c) for c in [105, 110, 88, 69])
FTHECV = 257
FXQGLR = 4
GLRAHE = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
GYOUSP = 256
GZUQEX = "".join(chr(c) for c in [65, 85, 88, 95, 83, 87])
HBSKSO = 271
HECVYY = "".join(chr(c) for c in [85, 115, 101, 114, 65, 114, 111, 109, 97])
HEOCTH = 6
HFTHEC = "".join(chr(c) for c in [85, 115, 101, 114, 80, 97, 117, 115, 101])
HIUSOO = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 57])
HUOJRJ = "".join(chr(c) for c in [75, 101, 121, 83, 116, 117, 99, 107, 69, 114, 114])
ICXQIE = 2
IEFXQG = 3
IPIVLA = "".join(chr(c) for c in [85, 115, 101, 114, 82, 117, 110, 116, 105, 109, 101])
IPOUYN = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
IUSOOQ = 274
IUXFEF = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
IVLASS = "".join(chr(c) for c in [85, 115, 101, 114, 80, 114, 111, 103])
JHIUSO = 273
JIGYOU = "".join(chr(c) for c in [76, 73])
JMCBFE = 275
JRJHIU = 7
JTACCP = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
JUTYEK = 278
JWMNZM = 290
JYMOUN = 286
KCWAON = "".join(
    chr(c)
    for c in [68, 114, 97, 105, 110, 86, 97, 108, 118, 101, 79, 117, 116, 112, 117, 116]
)
KPHUOJ = "".join(chr(c) for c in [72, 50, 79, 50, 69, 114, 114])
KQXPIC = 268
KSOKPH = 272
KXSJWM = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
LASSAK = "".join(chr(c) for c in [85, 115, 101, 114])
LIUXFE = 283
LKXSJW = 287
LRAHEO = "".join(chr(c) for c in [83, 76, 65, 86, 69])
LSXUJU = 300
MCBFEG = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
MJVHFT = "".join(chr(c) for c in [68, 73, 65, 71, 78, 79, 83, 84, 73, 67])
MNZMJI = 291
MOUNBL = "".join(chr(c) for c in [51, 50, 75])
NPYYLI = "".join(
    chr(c) for c in [67, 104, 114, 111, 109, 97, 79, 117, 116, 112, 117, 116]
)
NRSJMC = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 55])
NZMJIG = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
OCTHBS = 270
OJRJHI = "".join(chr(c) for c in [80, 114, 114, 51, 69, 114, 114])
OKPHUO = "".join(chr(c) for c in [80, 114, 114, 49, 69, 114, 114])
ONPYYL = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 86, 97, 108, 118, 101, 79, 117, 116, 112, 117, 116]
)
OOQNRS = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 52])
OQNRSJ = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 53])
OUNBLK = "".join(chr(c) for c in [52, 56, 75])
OUYNQJ = "".join(
    chr(c) for c in [67, 111, 108, 111, 114, 95, 75, 101, 121, 112, 97, 100]
)
PHUOJR = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 50, 79, 50, 69, 114, 114])
PICXQI = 0
PIPIVL = 264
PIVLAS = 261
POUYNQ = "".join(chr(c) for c in [105, 110, 89, 84])
PQIPOU = "".join(chr(c) for c in [75, 54, 48, 48])
PYYLIU = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
QBMJVH = "".join(chr(c) for c in [79, 70, 70])
QEXLSX = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
QGLRAH = 5
QIEFXQ = "".join(
    chr(c) for c in [69, 120, 116, 101, 114, 110, 97, 108, 80, 114, 111, 98, 101]
)
QIPOUY = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
QJYMOU = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
QNRSJM = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 54])
QXPICX = "".join(chr(c) for c in [77, 111, 100, 101, 83, 116, 97, 116, 101])
RAHEOC = "".join(chr(c) for c in [77, 65, 83, 84, 69, 82])
RJHIUS = "".join(chr(c) for c in [80, 114, 114, 52, 69, 114, 114])
RSJMCB = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 56])
SJMCBF = "".join(chr(c) for c in [77, 97, 120, 82, 117, 110, 116, 105, 109, 101])
SJWMNZ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
SKSOKP = "".join(
    chr(c) for c in [80, 111, 119, 101, 114, 70, 97, 105, 108, 69, 114, 114]
)
SOKPHU = "".join(chr(c) for c in [80, 114, 114, 50, 69, 114, 114])
SOOQNR = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 51])
SSAKQX = "".join(chr(c) for c in [80, 114, 111, 103, 50])
SXUJUT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
TACCPQ = "".join(chr(c) for c in [77, 73, 65])
THBSKS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 110, 83, 116, 97, 116, 101]
)
THECVY = 1
TYEKCW = 296
UJUTYE = "".join(chr(c) for c in [82, 111, 111, 109, 84, 101, 109, 112, 71])
UNBLKX = "".join(chr(c) for c in [54, 52, 75])
UOJRJH = "".join(chr(c) for c in [70, 108, 97, 115, 104, 69, 114, 114])
USOOQN = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 50])
UTYEKC = "".join(chr(c) for c in [75, 49, 48, 48, 48, 84, 101, 109, 112, 71])
UXFEFJ = 284
UYNQJY = "".join(chr(c) for c in [105, 110, 89, 74])
VHFTHE = "".join(chr(c) for c in [65, 76, 76])
VLASSA = 263
VYYPIP = "".join(chr(c) for c in [85, 115, 101, 114, 67, 104, 114, 111, 109, 97])
WAONPY = "".join(chr(c) for c in [65, 114, 111, 109, 97, 79, 117, 116, 112, 117, 116])
WMNZMJ = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
XFEFJT = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
XLSXUJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
XPICXQ = 269
XQGLRA = "".join(
    chr(c) for c in [78, 111, 82, 101, 103, 117, 108, 97, 116, 105, 111, 110]
)
XQIEFX = "".join(
    chr(c)
    for c in [68, 105, 97, 103, 110, 111, 115, 116, 105, 99, 83, 116, 97, 116, 101]
)
XSJWMN = 289
XUJUTY = 301
YEKCWA = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        97,
        105,
        110,
        105,
        110,
        103,
        82,
        117,
        110,
        116,
        105,
        109,
        101,
    ]
)
YLIUXF = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
YMOUNB = "".join(chr(c) for c in [49, 54, 75])
YNQJYM = "".join(chr(c) for c in [77, 114, 83, 116, 101, 97, 109])
YOUSPB = 301
YPIPIV = "".join(
    chr(c) for c in [85, 115, 101, 114, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
YYLIUX = 281
YYPIPI = 259
ZCQBMJ = "".join(chr(c) for c in [85, 115, 101, 114, 77, 111, 100, 101])
ZMJIGY = 292
ZUQEXL = "".join(chr(c) for c in [67, 79, 76, 79, 82, 95, 83, 69, 82, 73, 69, 83])
AHEOCT = [LRAHEO, RAHEOC]
CVYYPI = [QBMJVH, BMJVHF]
IGYOUS = [JIGYOU]
JVHFTH = [QBMJVH, BMJVHF, MJVHFT]
MJIGYO = []
NBLKXS = [YMOUNB, MOUNBL, OUNBLK, UNBLKX]
NQJYMO = [
    EFJTAC,
    FJTACC,
    JTACCP,
    TACCPQ,
    ACCPQI,
    CCPQIP,
    CPQIPO,
    PQIPOU,
    QIPOUY,
    IPOUYN,
    POUYNQ,
    OUYNQJ,
    UYNQJY,
    YNQJYM,
]
SAKQXP = [LASSAK, ASSAKQ, SSAKQX]
UQEXLS = [BFEGZU, FEGZUQ, EGZUQE, GZUQEX, ZUQEXL]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return ICXQIE

    @property
    def begin(self):
        return GYOUSP

    @property
    def end(self):
        return YOUSPB

    @property
    def all_device_keys(self):
        return IGYOUS

    @property
    def user_demand_keys(self):
        return MJIGYO

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoEnumStructAccessor(
                self.struct, ZCQBMJ, CQBMJV, None, JVHFTH, None, None, VHFTHE
            ),
            HFTHEC: GeckoBoolStructAccessor(
                self.struct, HFTHEC, FTHECV, THECVY, VHFTHE
            ),
            HECVYY: GeckoEnumStructAccessor(
                self.struct, HECVYY, ECVYYP, None, CVYYPI, None, None, VHFTHE
            ),
            VYYPIP: GeckoEnumStructAccessor(
                self.struct, VYYPIP, YYPIPI, None, CVYYPI, None, None, VHFTHE
            ),
            YPIPIV: GeckoTempStructAccessor(self.struct, YPIPIV, PIPIVL, VHFTHE),
            IPIVLA: GeckoWordStructAccessor(self.struct, IPIVLA, PIVLAS, VHFTHE),
            IVLASS: GeckoEnumStructAccessor(
                self.struct, IVLASS, VLASSA, None, SAKQXP, None, None, VHFTHE
            ),
            AKQXPI: GeckoByteStructAccessor(self.struct, AKQXPI, KQXPIC, None),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, PICXQI, CVYYPI, None, ICXQIE, None
            ),
            CXQIEF: GeckoBoolStructAccessor(self.struct, CXQIEF, XPICXQ, THECVY, None),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, XPICXQ, ICXQIE, CVYYPI, None, ICXQIE, None
            ),
            QIEFXQ: GeckoBoolStructAccessor(self.struct, QIEFXQ, XPICXQ, IEFXQG, None),
            EFXQGL: GeckoBoolStructAccessor(self.struct, EFXQGL, XPICXQ, FXQGLR, None),
            XQGLRA: GeckoBoolStructAccessor(self.struct, XQGLRA, XPICXQ, QGLRAH, None),
            GLRAHE: GeckoEnumStructAccessor(
                self.struct, GLRAHE, XPICXQ, HEOCTH, AHEOCT, None, ICXQIE, None
            ),
            EOCTHB: GeckoBoolStructAccessor(self.struct, EOCTHB, OCTHBS, PICXQI, None),
            CTHBSK: GeckoBoolStructAccessor(self.struct, CTHBSK, OCTHBS, THECVY, None),
            THBSKS: GeckoBoolStructAccessor(self.struct, THBSKS, HBSKSO, THECVY, None),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, HBSKSO, IEFXQG, CVYYPI, None, ICXQIE, None
            ),
            SKSOKP: GeckoBoolStructAccessor(self.struct, SKSOKP, KSOKPH, PICXQI, None),
            SOKPHU: GeckoBoolStructAccessor(self.struct, SOKPHU, KSOKPH, THECVY, None),
            OKPHUO: GeckoBoolStructAccessor(self.struct, OKPHUO, KSOKPH, ICXQIE, None),
            KPHUOJ: GeckoBoolStructAccessor(self.struct, KPHUOJ, KSOKPH, IEFXQG, None),
            PHUOJR: GeckoBoolStructAccessor(self.struct, PHUOJR, KSOKPH, FXQGLR, None),
            HUOJRJ: GeckoBoolStructAccessor(self.struct, HUOJRJ, KSOKPH, QGLRAH, None),
            UOJRJH: GeckoBoolStructAccessor(self.struct, UOJRJH, KSOKPH, HEOCTH, None),
            OJRJHI: GeckoBoolStructAccessor(self.struct, OJRJHI, KSOKPH, JRJHIU, None),
            RJHIUS: GeckoBoolStructAccessor(self.struct, RJHIUS, JHIUSO, PICXQI, None),
            HIUSOO: GeckoBoolStructAccessor(self.struct, HIUSOO, IUSOOQ, PICXQI, None),
            USOOQN: GeckoBoolStructAccessor(self.struct, USOOQN, IUSOOQ, THECVY, None),
            SOOQNR: GeckoBoolStructAccessor(self.struct, SOOQNR, IUSOOQ, ICXQIE, None),
            OOQNRS: GeckoBoolStructAccessor(self.struct, OOQNRS, IUSOOQ, IEFXQG, None),
            OQNRSJ: GeckoBoolStructAccessor(self.struct, OQNRSJ, IUSOOQ, FXQGLR, None),
            QNRSJM: GeckoBoolStructAccessor(self.struct, QNRSJM, IUSOOQ, QGLRAH, None),
            NRSJMC: GeckoBoolStructAccessor(self.struct, NRSJMC, IUSOOQ, HEOCTH, None),
            RSJMCB: GeckoBoolStructAccessor(self.struct, RSJMCB, IUSOOQ, JRJHIU, None),
            SJMCBF: GeckoWordStructAccessor(self.struct, SJMCBF, JMCBFE, None),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, UQEXLS, None, None, None
            ),
            QEXLSX: GeckoWordStructAccessor(self.struct, QEXLSX, EXLSXU, None),
            XLSXUJ: GeckoByteStructAccessor(self.struct, XLSXUJ, LSXUJU, None),
            SXUJUT: GeckoByteStructAccessor(self.struct, SXUJUT, XUJUTY, None),
            UJUTYE: GeckoTempStructAccessor(self.struct, UJUTYE, JUTYEK, None),
            UTYEKC: GeckoTempStructAccessor(self.struct, UTYEKC, TYEKCW, VHFTHE),
            YEKCWA: GeckoWordStructAccessor(self.struct, YEKCWA, EKCWAO, None),
            KCWAON: GeckoBoolStructAccessor(self.struct, KCWAON, CWAONP, PICXQI, None),
            WAONPY: GeckoBoolStructAccessor(self.struct, WAONPY, CWAONP, THECVY, None),
            AONPYY: GeckoBoolStructAccessor(self.struct, AONPYY, CWAONP, ICXQIE, None),
            ONPYYL: GeckoBoolStructAccessor(self.struct, ONPYYL, CWAONP, IEFXQG, None),
            NPYYLI: GeckoBoolStructAccessor(self.struct, NPYYLI, CWAONP, FXQGLR, None),
            PYYLIU: GeckoWordStructAccessor(self.struct, PYYLIU, YYLIUX, None),
            YLIUXF: GeckoByteStructAccessor(self.struct, YLIUXF, LIUXFE, None),
            IUXFEF: GeckoByteStructAccessor(self.struct, IUXFEF, UXFEFJ, None),
            XFEFJT: GeckoEnumStructAccessor(
                self.struct, XFEFJT, FEFJTA, None, NQJYMO, None, None, None
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, PICXQI, NBLKXS, None, FXQGLR, None
            ),
            BLKXSJ: GeckoWordStructAccessor(self.struct, BLKXSJ, LKXSJW, None),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, None),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, None),
            WMNZMJ: GeckoByteStructAccessor(self.struct, WMNZMJ, MNZMJI, None),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, None),
        }

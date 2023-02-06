#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'MrSteam v3'
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
ACCPQI = "".join(
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
AHEOCT = "".join(chr(c) for c in [65, 108, 108])
AKQXPI = "".join(
    chr(c) for c in [85, 115, 101, 114, 86, 97, 108, 118, 101, 80, 111, 119, 101, 114]
)
AMJMAO = 292
AOAWBS = 336
AONPYY = "".join(chr(c) for c in [83, 67, 95, 53, 52])
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 103, 49])
AWBSIR = 337
BFEGZU = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 50, 79, 50, 69, 114, 114])
BIAMJM = 291
BLKXSJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
BMJVHF = "".join(chr(c) for c in [79, 78])
BSIRYX = "".join(chr(c) for c in [76, 73])
BSKSOK = 0
BWJYKL = "".join(
    chr(c) for c in [67, 111, 108, 111, 114, 95, 75, 101, 121, 112, 97, 100]
)
CBFEGZ = "".join(chr(c) for c in [72, 50, 79, 50, 69, 114, 114])
CCPQIP = 293
CPQIPO = "".join(
    chr(c)
    for c in [68, 114, 97, 105, 110, 86, 97, 108, 118, 101, 79, 117, 116, 112, 117, 116]
)
CQBMJV = 256
CTHBSK = 268
CWAONP = 277
CXQIEF = 304
ECVYYP = 258
EFJTAC = "".join(chr(c) for c in [82, 111, 111, 109, 84, 101, 109, 112, 71])
EFXQGL = 307
EGZUQE = "".join(chr(c) for c in [70, 108, 97, 115, 104, 69, 114, 114])
EKCWAO = 275
EOCTHB = 311
EXLSXU = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 57])
FEFJTA = 301
FEGZUQ = "".join(chr(c) for c in [75, 101, 121, 83, 116, 117, 99, 107, 69, 114, 114])
FJBIAM = 290
FJTACC = 278
FTHECV = 257
FTSIFJ = 287
FXQGLR = "".join(
    chr(c)
    for c in [85, 115, 101, 114, 86, 97, 108, 118, 101, 84, 101, 109, 112, 85, 112]
)
GLRAHE = 309
GQPLSP = "".join(chr(c) for c in [49, 54, 75])
GYOUSP = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
GZUQEX = "".join(chr(c) for c in [80, 114, 114, 51, 69, 114, 114])
HBSKSO = 269
HECVYY = "".join(chr(c) for c in [85, 115, 101, 114, 65, 114, 111, 109, 97])
HEOCTH = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        86,
        97,
        108,
        118,
        101,
        65,
        117,
        116,
        111,
        67,
        108,
        101,
        97,
        110,
    ]
)
HFTHEC = "".join(chr(c) for c in [85, 115, 101, 114, 80, 97, 117, 115, 101])
HUOJRJ = 4
IAMJMA = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
ICXQIE = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        86,
        97,
        108,
        118,
        101,
        68,
        105,
        115,
        105,
        110,
        102,
        101,
        99,
        116,
        105,
        111,
        110,
    ]
)
IEFXQG = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        86,
        97,
        108,
        118,
        101,
        70,
        108,
        111,
        119,
        68,
        111,
        119,
        110,
    ]
)
IFJBIA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
IGYOUS = "".join(chr(c) for c in [68, 74, 83, 52])
IPIVLA = "".join(chr(c) for c in [85, 115, 101, 114, 82, 117, 110, 116, 105, 109, 101])
IPOUYN = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 79, 117, 116, 112, 117, 116]
)
IUSOOQ = 6
IUXFEF = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
IVLASS = "".join(chr(c) for c in [85, 115, 101, 114, 80, 114, 111, 103])
JBIAMJ = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
JHIUSO = "".join(chr(c) for c in [77, 65, 83, 84, 69, 82])
JIGYOU = "".join(chr(c) for c in [77, 73, 65])
JMAOAW = 334
JMCBFE = "".join(chr(c) for c in [80, 114, 114, 50, 69, 114, 114])
JRJHIU = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
JTACCP = "".join(chr(c) for c in [75, 49, 48, 48, 48, 84, 101, 109, 112, 71])
JUTYEK = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 54])
JWMNZM = 284
JYKLGQ = "".join(chr(c) for c in [77, 114, 83, 116, 101, 97, 109])
JYMOUN = "".join(
    chr(c) for c in [83, 104, 111, 119, 101, 114, 70, 108, 111, 119, 82, 97, 116, 101]
)
KCWAON = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
KLGQPL = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
KPHUOJ = 3
KQXPIC = 302
KSOKPH = "".join(chr(c) for c in [80, 97, 117, 115, 101, 83, 116, 97, 116, 101])
KXSJWM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
LASSAK = "".join(chr(c) for c in [85, 115, 101, 114])
LGQPLS = 286
LIUXFE = 298
LKXSJW = 281
LRAHEO = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        86,
        97,
        108,
        118,
        101,
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
    ]
)
LSPFTS = "".join(chr(c) for c in [54, 52, 75])
LSXUJU = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 50])
MAOAWB = "".join(
    chr(c)
    for c in [
        73,
        50,
        67,
        116,
        111,
        82,
        83,
        52,
        56,
        53,
        67,
        111,
        110,
        118,
        101,
        114,
        116,
        101,
        114,
        82,
        101,
        118,
    ]
)
MCBFEG = "".join(chr(c) for c in [80, 114, 114, 49, 69, 114, 114])
MJIGYO = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
MJMAOA = "".join(
    chr(c)
    for c in [
        73,
        50,
        67,
        116,
        111,
        82,
        83,
        52,
        56,
        53,
        67,
        111,
        110,
        118,
        101,
        114,
        116,
        101,
        114,
        73,
        68,
    ]
)
MJVHFT = "".join(chr(c) for c in [68, 73, 65, 71, 78, 79, 83, 84, 73, 67])
MNZMJI = 285
MOUNBL = "".join(
    chr(c)
    for c in [65, 118, 97, 105, 108, 97, 98, 108, 101, 79, 117, 116, 108, 101, 116]
)
NBLKXS = 322
NPYYLI = "".join(chr(c) for c in [65, 85, 88, 95, 83, 87])
NQJYMO = "".join(
    chr(c)
    for c in [83, 104, 111, 119, 101, 114, 86, 97, 108, 118, 101, 84, 101, 109, 112, 67]
)
NRSJMC = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 72, 101, 97, 116, 101, 114, 83, 116, 97, 116, 101]
)
NZMJIG = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
OAWBSI = "".join(
    chr(c)
    for c in [
        73,
        50,
        67,
        116,
        111,
        82,
        83,
        52,
        56,
        53,
        67,
        111,
        110,
        118,
        101,
        114,
        116,
        101,
        114,
        82,
        101,
        108,
    ]
)
OCTHBS = "".join(chr(c) for c in [72, 111, 117, 114, 115])
OJRJHI = 5
OKPHUO = "".join(
    chr(c) for c in [69, 120, 116, 101, 114, 110, 97, 108, 80, 114, 111, 98, 101]
)
ONPYYL = "".join(chr(c) for c in [84, 83, 67, 95, 53, 51])
OOQNRS = "".join(
    chr(c) for c in [69, 120, 112, 114, 101, 115, 115, 67, 121, 99, 108, 101]
)
OQNRSJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 110, 83, 116, 97, 116, 101]
)
OUNBLK = 318
OUSPBW = "".join(chr(c) for c in [75, 54, 48, 48])
OUYNQJ = "".join(
    chr(c) for c in [67, 104, 114, 111, 109, 97, 79, 117, 116, 112, 117, 116]
)
PBWJYK = "".join(chr(c) for c in [105, 110, 89, 84])
PFTSIF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
PHUOJR = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 68, 101, 116, 101, 99, 116, 101, 100]
)
PICXQI = 303
PIPIVL = 264
PIVLAS = 261
PLSPFT = "".join(chr(c) for c in [52, 56, 75])
POUYNQ = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 86, 97, 108, 118, 101, 79, 117, 116, 112, 117, 116]
)
PQIPOU = 295
PYYLIU = "".join(chr(c) for c in [67, 79, 76, 79, 82, 95, 83, 69, 82, 73, 69, 83])
QBMJVH = "".join(chr(c) for c in [79, 70, 70])
QEXLSX = 273
QGLRAH = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        86,
        97,
        108,
        118,
        101,
        84,
        101,
        109,
        112,
        68,
        111,
        119,
        110,
    ]
)
QIEFXQ = 306
QIPOUY = "".join(chr(c) for c in [65, 114, 111, 109, 97, 79, 117, 116, 112, 117, 116])
QJYMOU = 314
QNRSJM = 271
QPLSPF = "".join(chr(c) for c in [51, 50, 75])
RAHEOC = 310
RJHIUS = "".join(chr(c) for c in [83, 76, 65, 86, 69])
RSJMCB = "".join(
    chr(c) for c in [80, 111, 119, 101, 114, 70, 97, 105, 108, 69, 114, 114]
)
RYXBQF = 256
SIFJBI = 289
SJMCBF = 272
SJWMNZ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
SKSOKP = 2
SOKPHU = "".join(
    chr(c)
    for c in [68, 105, 97, 103, 110, 111, 115, 116, 105, 99, 83, 116, 97, 116, 101]
)
SOOQNR = 270
SPBWJY = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
SSAKQX = "".join(chr(c) for c in [80, 114, 111, 103, 50])
SXUJUT = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 51])
TACCPQ = 296
THBSKS = "".join(chr(c) for c in [77, 111, 100, 101, 83, 116, 97, 116, 101])
THECVY = 1
TSIFJB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
TYEKCW = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 56])
UJUTYE = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 53])
UNBLKX = "".join(
    chr(c)
    for c in [83, 104, 111, 119, 101, 114, 86, 97, 108, 118, 101, 65, 108, 97, 114, 109]
)
UOJRJH = "".join(
    chr(c) for c in [78, 111, 82, 101, 103, 117, 108, 97, 116, 105, 111, 110]
)
UQEXLS = "".join(chr(c) for c in [80, 114, 114, 52, 69, 114, 114])
USOOQN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 80, 114, 111, 98, 101])
USPBWJ = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
UTYEKC = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 55])
UXFEFJ = 300
UYNQJY = "".join(
    chr(c)
    for c in [
        83,
        104,
        111,
        119,
        101,
        114,
        86,
        97,
        108,
        118,
        101,
        83,
        116,
        97,
        116,
        117,
        115,
    ]
)
VHFTHE = "".join(chr(c) for c in [65, 76, 76])
VLASSA = 263
VYYPIP = "".join(chr(c) for c in [85, 115, 101, 114, 67, 104, 114, 111, 109, 97])
WAONPY = "".join(chr(c) for c in [78, 79, 95, 84, 83, 67])
WJYKLG = "".join(chr(c) for c in [105, 110, 89, 74])
WMNZMJ = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
XFEFJT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
XLSXUJ = 274
XPICXQ = "".join(
    chr(c)
    for c in [85, 115, 101, 114, 86, 97, 108, 118, 101, 79, 117, 116, 112, 117, 116]
)
XQGLRA = 308
XQIEFX = "".join(
    chr(c)
    for c in [85, 115, 101, 114, 86, 97, 108, 118, 101, 70, 108, 111, 119, 85, 112]
)
XSJWMN = 283
XUJUTY = "".join(chr(c) for c in [74, 117, 109, 112, 101, 114, 52])
YEKCWA = "".join(chr(c) for c in [77, 97, 120, 82, 117, 110, 116, 105, 109, 101])
YLIUXF = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
YMOUNB = 316
YNQJYM = 312
YOUSPB = "".join(chr(c) for c in [105, 110, 88, 77])
YPIPIV = "".join(
    chr(c) for c in [85, 115, 101, 114, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
YXBQFY = 337
YYPIPI = 259
ZCQBMJ = "".join(chr(c) for c in [85, 115, 101, 114, 77, 111, 100, 101])
ZMJIGY = "".join(chr(c) for c in [105, 110, 88, 69])
ZUQEXL = 7
CVYYPI = [QBMJVH, BMJVHF]
HIUSOO = [RJHIUS, JHIUSO]
IRYXBQ = [RSJMCB, EGZUQE, CBFEGZ, MCBFEG, GZUQEX, UQEXLS, JMCBFE, BFEGZU, FEGZUQ]
JVHFTH = [QBMJVH, BMJVHF, MJVHFT]
QXPICX = [BMJVHF, QBMJVH]
SAKQXP = [LASSAK, ASSAKQ, SSAKQX]
SIRYXB = [BSIRYX]
SPFTSI = [GQPLSP, QPLSPF, PLSPFT, LSPFTS]
WBSIRY = []
YKLGQP = [
    NZMJIG,
    ZMJIGY,
    MJIGYO,
    JIGYOU,
    IGYOUS,
    GYOUSP,
    YOUSPB,
    OUSPBW,
    USPBWJ,
    SPBWJY,
    PBWJYK,
    BWJYKL,
    WJYKLG,
    JYKLGQ,
]
YYLIUX = [WAONPY, AONPYY, ONPYYL, NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return KPHUOJ

    @property
    def begin(self):
        return RYXBQF

    @property
    def end(self):
        return YXBQFY

    @property
    def all_device_keys(self):
        return SIRYXB

    @property
    def user_demand_keys(self):
        return WBSIRY

    @property
    def error_keys(self):
        return IRYXBQ

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
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, None, QXPICX, None, None, VHFTHE
            ),
            XPICXQ: GeckoByteStructAccessor(self.struct, XPICXQ, PICXQI, VHFTHE),
            ICXQIE: GeckoBoolStructAccessor(self.struct, ICXQIE, CXQIEF, None, VHFTHE),
            XQIEFX: GeckoBoolStructAccessor(self.struct, XQIEFX, QIEFXQ, None, VHFTHE),
            IEFXQG: GeckoBoolStructAccessor(self.struct, IEFXQG, EFXQGL, None, VHFTHE),
            FXQGLR: GeckoBoolStructAccessor(self.struct, FXQGLR, XQGLRA, None, VHFTHE),
            QGLRAH: GeckoBoolStructAccessor(self.struct, QGLRAH, GLRAHE, None, VHFTHE),
            LRAHEO: GeckoBoolStructAccessor(self.struct, LRAHEO, RAHEOC, None, AHEOCT),
            HEOCTH: GeckoBoolStructAccessor(self.struct, HEOCTH, EOCTHB, None, AHEOCT),
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, None),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, HBSKSO, BSKSOK, CVYYPI, None, SKSOKP, None
            ),
            KSOKPH: GeckoBoolStructAccessor(self.struct, KSOKPH, HBSKSO, THECVY, None),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, HBSKSO, SKSOKP, CVYYPI, None, SKSOKP, None
            ),
            OKPHUO: GeckoBoolStructAccessor(self.struct, OKPHUO, HBSKSO, KPHUOJ, None),
            PHUOJR: GeckoBoolStructAccessor(self.struct, PHUOJR, HBSKSO, HUOJRJ, None),
            UOJRJH: GeckoBoolStructAccessor(self.struct, UOJRJH, HBSKSO, OJRJHI, None),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, HBSKSO, IUSOOQ, HIUSOO, None, SKSOKP, None
            ),
            USOOQN: GeckoBoolStructAccessor(self.struct, USOOQN, SOOQNR, BSKSOK, None),
            OOQNRS: GeckoBoolStructAccessor(self.struct, OOQNRS, SOOQNR, THECVY, None),
            OQNRSJ: GeckoBoolStructAccessor(self.struct, OQNRSJ, QNRSJM, THECVY, None),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, QNRSJM, KPHUOJ, CVYYPI, None, SKSOKP, None
            ),
            RSJMCB: GeckoBoolStructAccessor(self.struct, RSJMCB, SJMCBF, BSKSOK, None),
            JMCBFE: GeckoBoolStructAccessor(self.struct, JMCBFE, SJMCBF, THECVY, None),
            MCBFEG: GeckoBoolStructAccessor(self.struct, MCBFEG, SJMCBF, SKSOKP, None),
            CBFEGZ: GeckoBoolStructAccessor(self.struct, CBFEGZ, SJMCBF, KPHUOJ, None),
            BFEGZU: GeckoBoolStructAccessor(self.struct, BFEGZU, SJMCBF, HUOJRJ, None),
            FEGZUQ: GeckoBoolStructAccessor(self.struct, FEGZUQ, SJMCBF, OJRJHI, None),
            EGZUQE: GeckoBoolStructAccessor(self.struct, EGZUQE, SJMCBF, IUSOOQ, None),
            GZUQEX: GeckoBoolStructAccessor(self.struct, GZUQEX, SJMCBF, ZUQEXL, None),
            UQEXLS: GeckoBoolStructAccessor(self.struct, UQEXLS, QEXLSX, BSKSOK, None),
            EXLSXU: GeckoBoolStructAccessor(self.struct, EXLSXU, XLSXUJ, BSKSOK, None),
            LSXUJU: GeckoBoolStructAccessor(self.struct, LSXUJU, XLSXUJ, THECVY, None),
            SXUJUT: GeckoBoolStructAccessor(self.struct, SXUJUT, XLSXUJ, SKSOKP, None),
            XUJUTY: GeckoBoolStructAccessor(self.struct, XUJUTY, XLSXUJ, KPHUOJ, None),
            UJUTYE: GeckoBoolStructAccessor(self.struct, UJUTYE, XLSXUJ, HUOJRJ, None),
            JUTYEK: GeckoBoolStructAccessor(self.struct, JUTYEK, XLSXUJ, OJRJHI, None),
            UTYEKC: GeckoBoolStructAccessor(self.struct, UTYEKC, XLSXUJ, IUSOOQ, None),
            TYEKCW: GeckoBoolStructAccessor(self.struct, TYEKCW, XLSXUJ, ZUQEXL, None),
            YEKCWA: GeckoWordStructAccessor(self.struct, YEKCWA, EKCWAO, None),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, CWAONP, None, YYLIUX, None, None, None
            ),
            YLIUXF: GeckoWordStructAccessor(self.struct, YLIUXF, LIUXFE, None),
            IUXFEF: GeckoByteStructAccessor(self.struct, IUXFEF, UXFEFJ, None),
            XFEFJT: GeckoByteStructAccessor(self.struct, XFEFJT, FEFJTA, None),
            EFJTAC: GeckoTempStructAccessor(self.struct, EFJTAC, FJTACC, None),
            JTACCP: GeckoTempStructAccessor(self.struct, JTACCP, TACCPQ, VHFTHE),
            ACCPQI: GeckoWordStructAccessor(self.struct, ACCPQI, CCPQIP, None),
            CPQIPO: GeckoBoolStructAccessor(self.struct, CPQIPO, PQIPOU, BSKSOK, None),
            QIPOUY: GeckoBoolStructAccessor(self.struct, QIPOUY, PQIPOU, THECVY, None),
            IPOUYN: GeckoBoolStructAccessor(self.struct, IPOUYN, PQIPOU, SKSOKP, None),
            POUYNQ: GeckoBoolStructAccessor(self.struct, POUYNQ, PQIPOU, KPHUOJ, None),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, PQIPOU, HUOJRJ, None),
            UYNQJY: GeckoWordStructAccessor(self.struct, UYNQJY, YNQJYM, None),
            NQJYMO: GeckoTempStructAccessor(self.struct, NQJYMO, QJYMOU, None),
            JYMOUN: GeckoWordStructAccessor(self.struct, JYMOUN, YMOUNB, None),
            MOUNBL: GeckoWordStructAccessor(self.struct, MOUNBL, OUNBLK, None),
            UNBLKX: GeckoWordStructAccessor(self.struct, UNBLKX, NBLKXS, None),
            BLKXSJ: GeckoWordStructAccessor(self.struct, BLKXSJ, LKXSJW, None),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, None),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, None),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, MNZMJI, None, YKLGQP, None, None, None
            ),
            KLGQPL: GeckoEnumStructAccessor(
                self.struct, KLGQPL, LGQPLS, BSKSOK, SPFTSI, None, HUOJRJ, None
            ),
            PFTSIF: GeckoWordStructAccessor(self.struct, PFTSIF, FTSIFJ, None),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, None),
            IFJBIA: GeckoByteStructAccessor(self.struct, IFJBIA, FJBIAM, None),
            JBIAMJ: GeckoByteStructAccessor(self.struct, JBIAMJ, BIAMJM, None),
            IAMJMA: GeckoByteStructAccessor(self.struct, IAMJMA, AMJMAO, None),
            MJMAOA: GeckoWordStructAccessor(self.struct, MJMAOA, JMAOAW, None),
            MAOAWB: GeckoByteStructAccessor(self.struct, MAOAWB, AOAWBS, None),
            OAWBSI: GeckoByteStructAccessor(self.struct, OAWBSI, AWBSIR, None),
        }

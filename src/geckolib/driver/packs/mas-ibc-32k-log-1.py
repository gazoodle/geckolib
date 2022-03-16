#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'MAS-IBC-32K v1'
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
ACCPQI = "".join(chr(c) for c in [52, 52])
AHEOCT = 265
AKQXPI = 260
AONPYY = "".join(chr(c) for c in [50, 54])
ASSAKQ = "".join(chr(c) for c in [72, 73, 71, 72])
BFEGZU = "".join(
    chr(c)
    for c in [80, 117, 114, 103, 101, 68, 101, 108, 97, 121, 84, 105, 109, 101, 114]
)
BLKXSJ = 6
BMJVHF = "".join(chr(c) for c in [85, 115, 101, 114, 67, 104, 114, 111, 109, 97])
BSKSOK = "".join(chr(c) for c in [49, 53])
BWJYKL = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
CBFEGZ = 1
CCPQIP = "".join(chr(c) for c in [52, 54])
CPQIPO = "".join(chr(c) for c in [52, 55])
CQBMJV = 256
CTHBSK = "".join(chr(c) for c in [])
CVYYPI = "".join(chr(c) for c in [83, 67, 65, 78])
CWAONP = "".join(chr(c) for c in [50, 51])
CXQIEF = 262
ECVYYP = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
EFJTAC = "".join(chr(c) for c in [51, 57])
EFXQGL = 0
EGZUQE = "".join(chr(c) for c in [50])
EKCWAO = "".join(chr(c) for c in [50, 49])
EOCTHB = 266
EXLSXU = "".join(chr(c) for c in [56])
FEFJTA = "".join(chr(c) for c in [51, 56])
FEGZUQ = "".join(chr(c) for c in [49])
FJTACC = "".join(chr(c) for c in [52, 49])
FTHECV = "".join(chr(c) for c in [71, 82, 69, 69, 78])
FTSIFJ = "".join(chr(c) for c in [49, 54, 75])
FXQGLR = 2
GLRAHE = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        68,
        114,
        121,
        105,
        110,
        103,
        77,
        105,
        110,
        117,
        116,
        101,
    ]
)
GQPLSP = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
GYOUSP = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
GZUQEX = "".join(chr(c) for c in [51])
HBSKSO = "".join(chr(c) for c in [49, 48])
HECVYY = "".join(chr(c) for c in [80, 85, 82, 80, 76, 69])
HEOCTH = "".join(
    chr(c)
    for c in [85, 115, 101, 114, 68, 114, 121, 105, 110, 103, 68, 101, 108, 97, 121]
)
HFTHEC = "".join(chr(c) for c in [82, 69, 68])
HIUSOO = 267
HUOJRJ = "".join(chr(c) for c in [53, 48])
IAMJMA = "".join(chr(c) for c in [76, 73])
ICXQIE = "".join(
    chr(c)
    for c in [85, 115, 101, 114, 68, 114, 121, 105, 110, 103, 67, 121, 99, 108, 101]
)
IFJBIA = "".join(chr(c) for c in [54, 52, 75])
IGYOUS = 278
IPIVLA = 258
IPOUYN = "".join(chr(c) for c in [53, 49])
IUSOOQ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
IUXFEF = "".join(chr(c) for c in [51, 52])
IVLASS = 259
JBIAMJ = 4
JHIUSO = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
JIGYOU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
JMAOAW = 285
JMCBFE = "".join(chr(c) for c in [65, 67, 84, 73, 86, 65, 84, 69])
JTACCP = "".join(chr(c) for c in [52, 50])
JUTYEK = "".join(chr(c) for c in [49, 54])
JVHFTH = "".join(chr(c) for c in [79, 70, 70])
JWMNZM = "".join(chr(c) for c in [66, 111, 111, 116, 73, 68])
JYKLGQ = "".join(chr(c) for c in [68, 74, 83, 52])
JYMOUN = "".join(chr(c) for c in [53, 57])
KCWAON = "".join(chr(c) for c in [50, 50])
KLGQPL = "".join(chr(c) for c in [105, 110, 88, 77])
KPHUOJ = "".join(chr(c) for c in [52, 48])
KQXPIC = "".join(chr(c) for c in [85, 115, 101, 114, 71, 101, 121, 115, 97, 105, 114])
KSOKPH = "".join(chr(c) for c in [50, 53])
KXSJWM = 283
LASSAK = "".join(chr(c) for c in [77, 69, 68])
LGQPLS = "".join(chr(c) for c in [75, 54, 48, 48])
LIUXFE = "".join(chr(c) for c in [51, 51])
LKXSJW = "".join(chr(c) for c in [80, 111, 119, 101, 114, 83, 116, 97, 116, 101])
LRAHEO = 264
LSXUJU = "".join(chr(c) for c in [49, 49])
MJIGYO = 276
MJMAOA = 256
MJVHFT = 257
MNZMJI = "".join(chr(c) for c in [66, 111, 111, 116, 82, 101, 118])
MOUNBL = "".join(
    chr(c) for c in [80, 117, 114, 103, 101, 83, 116, 97, 110, 100, 98, 121]
)
NPYYLI = "".join(chr(c) for c in [50, 56])
NQJYMO = "".join(chr(c) for c in [53, 55])
NZMJIG = 274
OCTHBS = "".join(chr(c) for c in [48])
OJRJHI = "".join(chr(c) for c in [54, 48])
OKPHUO = "".join(chr(c) for c in [51, 53])
ONPYYL = "".join(chr(c) for c in [50, 55])
OOQNRS = 271
OQNRSJ = "".join(chr(c) for c in [82, 85, 78])
OUNBLK = "".join(chr(c) for c in [83, 84, 79, 80])
OUSPBW = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
OUYNQJ = "".join(chr(c) for c in [53, 51])
PBWJYK = "".join(chr(c) for c in [105, 110, 88, 69])
PFTSIF = 282
PHUOJR = "".join(chr(c) for c in [52, 53])
PIPIVL = "".join(
    chr(c) for c in [85, 115, 101, 114, 66, 97, 116, 104, 84, 105, 109, 101]
)
PIVLAS = "".join(chr(c) for c in [85, 115, 101, 114, 72, 101, 97, 116, 101, 114, 49])
PLSPFT = "".join(chr(c) for c in [105, 110, 89, 84])
POUYNQ = "".join(chr(c) for c in [53, 50])
PQIPOU = "".join(chr(c) for c in [52, 56])
PYYLIU = "".join(chr(c) for c in [50, 57])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [55])
QGLRAH = 263
QIEFXQ = "".join(chr(c) for c in [68, 97, 105, 108, 121])
QIPOUY = "".join(chr(c) for c in [52, 57])
QJYMOU = "".join(chr(c) for c in [53, 56])
QNRSJM = "".join(chr(c) for c in [83, 84, 65, 84, 69, 49, 48])
QPLSPF = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
QXPICX = 261
RAHEOC = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        68,
        114,
        121,
        105,
        110,
        103,
        83,
        101,
        99,
        111,
        110,
        100,
    ]
)
RJHIUS = 63
RSJMCB = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 116, 97, 114, 116])
SAKQXP = "".join(chr(c) for c in [85, 115, 101, 114, 72, 101, 97, 116, 101, 114, 50])
SIFJBI = "".join(chr(c) for c in [52, 56, 75])
SJMCBF = "".join(chr(c) for c in [68, 69, 65, 67, 84, 73, 86, 65, 84, 69])
SJWMNZ = 284
SKSOKP = "".join(chr(c) for c in [50, 48])
SOKPHU = "".join(chr(c) for c in [51, 48])
SOOQNR = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 83, 116, 97, 116, 101])
SPBWJY = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
SPFTSI = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
SXUJUT = "".join(chr(c) for c in [49, 50])
TACCPQ = "".join(chr(c) for c in [52, 51])
THBSKS = "".join(chr(c) for c in [53])
THECVY = "".join(chr(c) for c in [66, 76, 85, 69])
TSIFJB = "".join(chr(c) for c in [51, 50, 75])
TYEKCW = "".join(chr(c) for c in [49, 56])
UJUTYE = "".join(chr(c) for c in [49, 52])
UNBLKX = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UOJRJH = "".join(chr(c) for c in [53, 53])
UQEXLS = "".join(chr(c) for c in [54])
USOOQN = 269
USPBWJ = 281
UTYEKC = "".join(chr(c) for c in [49, 55])
UXFEFJ = "".join(chr(c) for c in [51, 54])
UYNQJY = "".join(chr(c) for c in [53, 52])
VHFTHE = "".join(chr(c) for c in [87, 72, 73, 84, 69])
VLASSA = "".join(chr(c) for c in [76, 79, 87])
VYYPIP = "".join(chr(c) for c in [79, 82, 65, 78, 71, 69])
WAONPY = "".join(chr(c) for c in [50, 52])
WJYKLG = "".join(chr(c) for c in [77, 73, 65])
WMNZMJ = 272
XFEFJT = "".join(chr(c) for c in [51, 55])
XLSXUJ = "".join(chr(c) for c in [57])
XPICXQ = "".join(chr(c) for c in [79, 78])
XQGLRA = "".join(
    chr(c) for c in [85, 115, 101, 114, 68, 114, 121, 105, 110, 103, 72, 111, 117, 114]
)
XQIEFX = "".join(chr(c) for c in [65, 102, 116, 101, 114, 66, 97, 116, 104])
XSJWMN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 76, 111, 99, 107])
XUJUTY = "".join(chr(c) for c in [49, 51])
YEKCWA = "".join(chr(c) for c in [49, 57])
YKLGQP = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
YLIUXF = "".join(chr(c) for c in [51, 50])
YNQJYM = "".join(chr(c) for c in [53, 54])
YOUSPB = 280
YYLIUX = "".join(chr(c) for c in [51, 49])
YYPIPI = "".join(chr(c) for c in [80, 65, 85, 83, 69])
ZCQBMJ = "".join(
    chr(c)
    for c in [
        85,
        115,
        101,
        114,
        66,
        108,
        111,
        119,
        101,
        114,
        73,
        110,
        116,
        101,
        110,
        115,
        105,
        116,
        121,
    ]
)
ZMJIGY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
ZUQEXL = "".join(chr(c) for c in [52])
AMJMAO = [JHIUSO, IUSOOQ, SOOQNR, RSJMCB, BFEGZU, MOUNBL, LKXSJW, XSJWMN, IAMJMA]
BIAMJM = []
FJBIAM = [FTSIFJ, TSIFJB, SIFJBI, IFJBIA]
IEFXQG = [XQIEFX, QIEFXQ]
JRJHIU = [
    OCTHBS,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    THBSKS,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    HBSKSO,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    BSKSOK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    SKSOKP,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    KSOKPH,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    SOKPHU,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    OKPHUO,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    KPHUOJ,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    PHUOJR,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    HUOJRJ,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    UOJRJH,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    CTHBSK,
    OJRJHI,
]
LSPFTS = [
    SPBWJY,
    PBWJYK,
    BWJYKL,
    WJYKLG,
    JYKLGQ,
    YKLGQP,
    KLGQPL,
    LGQPLS,
    GQPLSP,
    QPLSPF,
    PLSPFT,
]
MCBFEG = [SJMCBF, JMCBFE]
NBLKXS = [OUNBLK, UNBLKX]
NRSJMC = [YYPIPI, OQNRSJ, QNRSJM]
PICXQI = [JVHFTH, XPICXQ]
SSAKQX = [JVHFTH, VLASSA, LASSAK, ASSAKQ]
YMOUNB = [
    OCTHBS,
    FEGZUQ,
    EGZUQE,
    GZUQEX,
    ZUQEXL,
    THBSKS,
    UQEXLS,
    QEXLSX,
    EXLSXU,
    XLSXUJ,
    HBSKSO,
    LSXUJU,
    SXUJUT,
    XUJUTY,
    UJUTYE,
    BSKSOK,
    JUTYEK,
    UTYEKC,
    TYEKCW,
    YEKCWA,
    SKSOKP,
    EKCWAO,
    KCWAON,
    CWAONP,
    WAONPY,
    KSOKPH,
    AONPYY,
    ONPYYL,
    NPYYLI,
    PYYLIU,
    SOKPHU,
    YYLIUX,
    YLIUXF,
    LIUXFE,
    IUXFEF,
    OKPHUO,
    UXFEFJ,
    XFEFJT,
    FEFJTA,
    EFJTAC,
    KPHUOJ,
    FJTACC,
    JTACCP,
    TACCPQ,
    ACCPQI,
    PHUOJR,
    CCPQIP,
    CPQIPO,
    PQIPOU,
    QIPOUY,
    HUOJRJ,
    IPOUYN,
    POUYNQ,
    OUYNQJ,
    UYNQJY,
    UOJRJH,
    YNQJYM,
    NQJYMO,
    QJYMOU,
    JYMOUN,
    OJRJHI,
]
YPIPIV = [
    JVHFTH,
    VHFTHE,
    HFTHEC,
    FTHECV,
    THECVY,
    HECVYY,
    ECVYYP,
    CVYYPI,
    VYYPIP,
    YYPIPI,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return CBFEGZ

    @property
    def begin(self):
        return MJMAOA

    @property
    def end(self):
        return JMAOAW

    @property
    def all_device_keys(self):
        return AMJMAO

    @property
    def user_demand_keys(self):
        return BIAMJM

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, YPIPIV, None, None, QBMJVH
            ),
            PIPIVL: GeckoByteStructAccessor(self.struct, PIPIVL, IPIVLA, QBMJVH),
            PIVLAS: GeckoEnumStructAccessor(
                self.struct, PIVLAS, IVLASS, None, SSAKQX, None, None, QBMJVH
            ),
            SAKQXP: GeckoEnumStructAccessor(
                self.struct, SAKQXP, AKQXPI, None, SSAKQX, None, None, QBMJVH
            ),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, PICXQI, None, None, None
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, EFXQGL, IEFXQG, None, FXQGLR, QBMJVH
            ),
            XQGLRA: GeckoByteStructAccessor(self.struct, XQGLRA, QGLRAH, QBMJVH),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoByteStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, EOCTHB, EFXQGL, JRJHIU, None, RJHIUS, QBMJVH
            ),
            JHIUSO: GeckoWordStructAccessor(self.struct, JHIUSO, HIUSOO, None),
            IUSOOQ: GeckoWordStructAccessor(self.struct, IUSOOQ, USOOQN, None),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, None, NRSJMC, None, None, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, CXQIEF, CBFEGZ, MCBFEG, None, None, None
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, CXQIEF, FXQGLR, YMOUNB, None, None, None
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, EOCTHB, BLKXSJ, NBLKXS, None, None, None
            ),
            LKXSJW: GeckoEnumStructAccessor(
                self.struct, LKXSJW, KXSJWM, None, PICXQI, None, None, None
            ),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, SJWMNZ, None, PICXQI, None, None, None
            ),
            JWMNZM: GeckoWordStructAccessor(self.struct, JWMNZM, WMNZMJ, None),
            MNZMJI: GeckoWordStructAccessor(self.struct, MNZMJI, NZMJIG, None),
            ZMJIGY: GeckoWordStructAccessor(self.struct, ZMJIGY, MJIGYO, None),
            JIGYOU: GeckoWordStructAccessor(self.struct, JIGYOU, IGYOUS, None),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, None),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, USPBWJ, None, LSPFTS, None, None, None
            ),
            SPFTSI: GeckoEnumStructAccessor(
                self.struct, SPFTSI, PFTSIF, EFXQGL, FJBIAM, None, JBIAMJ, None
            ),
        }

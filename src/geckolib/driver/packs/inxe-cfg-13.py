#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v13'
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
ACCPQI = 53
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AKQXPI = 11
AONPYY = 48
ASSAKQ = "".join(chr(c) for c in [79, 117, 116, 50])
BFEGZU = 45
BLKXSJ = 5
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BSKSOK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BWJYKL = "".join(
    chr(c) for c in [85, 110, 99, 111, 110, 102, 105, 103, 117, 114, 101, 100]
)
CBFEGZ = "".join(
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
CCPQIP = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
CPQIPO = 55
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CXQIEF = 14
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 24
EFXQGL = 25
EGZUQE = 47
EKCWAO = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
FEFJTA = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
FEGZUQ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
FJBIAM = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
FJTACC = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 23
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
GLRAHE = 27
GQPLSP = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
GYOUSP = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
GZUQEX = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 29
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = 37
IAMJMA = "".join(chr(c) for c in [76, 73])
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IGYOUS = 57
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
IUSOOQ = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
IUXFEF = "".join(chr(c) for c in [70])
IVLASS = "".join(chr(c) for c in [])
JBIAMJ = 49
JHIUSO = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
JIGYOU = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
JMAOAW = 13
JMCBFE = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 102, 102, 84, 105, 109, 101]
)
JRJHIU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
JTACCP = 51
JUTYEK = 18
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
JYKLGQ = "".join(chr(c) for c in [83, 108, 97, 118, 101])
JYMOUN = 59
KCWAON = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
KLGQPL = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
KPHUOJ = 36
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 52])
KSOKPH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KXSJWM = 3
LGQPLS = 60
LIUXFE = 22
LKXSJW = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
LSXUJU = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
MCBFEG = 43
MJVHFT = 9
MNZMJI = "".join(
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
NBLKXS = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
NPYYLI = 1
NQJYMO = 34
NRSJMC = 40
NZMJIG = 56
OCTHBS = 30
OJRJHI = 21
OKPHUO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
ONPYYL = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
OOQNRS = "".join(
    chr(c) for c in [79, 84, 65, 99, 116, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
OQNRSJ = 38
OUNBLK = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
OUSPBW = "".join(
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
OUYNQJ = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
PBWJYK = 58
PFTSIF = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
PICXQI = 13
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
POUYNQ = 62
PQIPOU = "".join(chr(c) for c in [78, 105, 103, 104, 116])
PYYLIU = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QJYMOU = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
QNRSJM = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
QPLSPF = 61
QXPICX = 12
RAHEOC = 28
RJHIUS = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
RSJMCB = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 110, 84, 105, 109, 101]
)
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 51])
SIFJBI = "".join(chr(c) for c in [50, 52, 104])
SJMCBF = 41
SJWMNZ = 7
SKSOKP = 31
SOKPHU = 35
SOOQNR = 0
SPBWJY = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
SSAKQX = 10
SXUJUT = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
TACCPQ = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
THBSKS = 15
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = "".join(chr(c) for c in [65, 109, 80, 109])
TYEKCW = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
UJUTYE = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
UNBLKX = 4
UOJRJH = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
UQEXLS = "".join(chr(c) for c in [80, 49])
USOOQN = 16
USPBWJ = 2
UXFEFJ = "".join(chr(c) for c in [67])
UYNQJY = 33
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
WJYKLG = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
WMNZMJ = 8
XLSXUJ = 17
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 53])
XQGLRA = 26
XQIEFX = "".join(chr(c) for c in [72, 84, 82])
XSJWMN = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
YEKCWA = 19
YLIUXF = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
YMOUNB = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
YNQJYM = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
YOUSPB = 1
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YYLIUX = 20
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
ZUQEXL = 63
AMJMAO = [IAMJMA]
BIAMJM = [BMJVHF, ASSAKQ, SAKQXP, KQXPIC, XPICXQ, ICXQIE, CTHBSK]
CWAONP = [EKCWAO, KCWAON]
HBSKSO = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    PIPIVL,
]
HIUSOO = [JRJHIU, RJHIUS, JHIUSO]
IFJBIA = [JVHFTH, TSIFJB, SIFJBI]
LASSAK = [
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
    YPIPIV,
    PIPIVL,
    IPIVLA,
    PIVLAS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    VLASSA,
]
MJIGYO = [JVHFTH, ZMJIGY]
MJMAOA = []
MOUNBL = [EKCWAO, YMOUNB]
QEXLSX = [JVHFTH, UQEXLS, PIPIVL]
QIEFXQ = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    XQIEFX,
]
QIPOUY = [EKCWAO, PQIPOU]
SPFTSI = [PLSPFT, LSPFTS]
UTYEKC = [PIPIVL, UQEXLS]
XFEFJT = [IUXFEF, UXFEFJ]
XUJUTY = [LSXUJU, SXUJUT]
YKLGQP = [BWJYKL, WJYKLG, JYKLGQ]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return JMAOAW

    @property
    def output_keys(self):
        return BIAMJM

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, LASSAK, None, None, QBMJVH
            ),
            ASSAKQ: GeckoEnumStructAccessor(
                self.struct, ASSAKQ, SSAKQX, None, LASSAK, None, None, QBMJVH
            ),
            SAKQXP: GeckoEnumStructAccessor(
                self.struct, SAKQXP, AKQXPI, None, LASSAK, None, None, QBMJVH
            ),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, LASSAK, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, LASSAK, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, QIEFXQ, None, None, QBMJVH
            ),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, THBSKS, None, HBSKSO, None, None, QBMJVH
            ),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, QBMJVH),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, QBMJVH),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, QBMJVH),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, QBMJVH),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, HIUSOO, None, None, QBMJVH
            ),
            IUSOOQ: GeckoBoolStructAccessor(
                self.struct, IUSOOQ, USOOQN, SOOQNR, QBMJVH
            ),
            OOQNRS: GeckoTempStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, QBMJVH),
            RSJMCB: GeckoWordStructAccessor(self.struct, RSJMCB, SJMCBF, QBMJVH),
            JMCBFE: GeckoWordStructAccessor(self.struct, JMCBFE, MCBFEG, QBMJVH),
            CBFEGZ: GeckoWordStructAccessor(self.struct, CBFEGZ, BFEGZU, QBMJVH),
            FEGZUQ: GeckoByteStructAccessor(self.struct, FEGZUQ, EGZUQE, QBMJVH),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, QEXLSX, None, None, QBMJVH
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, None, XUJUTY, None, None, QBMJVH
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, JUTYEK, None, UTYEKC, None, None, QBMJVH
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, None, CWAONP, None, None, QBMJVH
            ),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, QBMJVH),
            ONPYYL: GeckoTempStructAccessor(self.struct, ONPYYL, NPYYLI, QBMJVH),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, YYLIUX, None, UTYEKC, None, None, QBMJVH
            ),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, XFEFJT, None, None, QBMJVH
            ),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, QBMJVH),
            FJTACC: GeckoTempStructAccessor(self.struct, FJTACC, JTACCP, QBMJVH),
            TACCPQ: GeckoTempStructAccessor(self.struct, TACCPQ, ACCPQI, QBMJVH),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, QIPOUY, None, None, QBMJVH
            ),
            IPOUYN: GeckoByteStructAccessor(self.struct, IPOUYN, POUYNQ, QBMJVH),
            OUYNQJ: GeckoByteStructAccessor(self.struct, OUYNQJ, UYNQJY, QBMJVH),
            YNQJYM: GeckoByteStructAccessor(self.struct, YNQJYM, NQJYMO, QBMJVH),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, MOUNBL, None, None, QBMJVH
            ),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, QBMJVH),
            NBLKXS: GeckoTimeStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoTimeStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoTimeStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoTimeStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, MJIGYO, None, None, QBMJVH
            ),
            JIGYOU: GeckoBoolStructAccessor(
                self.struct, JIGYOU, IGYOUS, SOOQNR, QBMJVH
            ),
            GYOUSP: GeckoBoolStructAccessor(
                self.struct, GYOUSP, IGYOUS, YOUSPB, QBMJVH
            ),
            OUSPBW: GeckoBoolStructAccessor(
                self.struct, OUSPBW, IGYOUS, USPBWJ, QBMJVH
            ),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, YKLGQP, None, None, QBMJVH
            ),
            KLGQPL: GeckoByteStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, QPLSPF, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, IFJBIA, None, None, QBMJVH
            ),
            FJBIAM: GeckoWordStructAccessor(self.struct, FJBIAM, JBIAMJ, QBMJVH),
        }

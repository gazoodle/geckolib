#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v12'
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
ACCPQI = "".join(chr(c) for c in [78, 105, 103, 104, 116])
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AKQXPI = 11
AONPYY = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
ASSAKQ = "".join(chr(c) for c in [79, 117, 116, 50])
BFEGZU = 45
BLKXSJ = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BSKSOK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
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
CPQIPO = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
CXQIEF = 14
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
EFXQGL = 25
EGZUQE = 47
EKCWAO = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
FEFJTA = 51
FEGZUQ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
FJBIAM = "".join(chr(c) for c in [76, 73])
FJTACC = 53
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
GLRAHE = 27
GQPLSP = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
GYOUSP = 2
GZUQEX = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 29
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = 37
IAMJMA = 12
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IGYOUS = "".join(
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
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 33
IUSOOQ = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
IUXFEF = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
IVLASS = "".join(chr(c) for c in [])
JHIUSO = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
JIGYOU = 1
JMCBFE = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 102, 102, 84, 105, 109, 101]
)
JRJHIU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
JTACCP = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
JUTYEK = 19
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = 56
JYKLGQ = 60
JYMOUN = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
KCWAON = 48
KLGQPL = 61
KPHUOJ = 36
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 52])
KSOKPH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KXSJWM = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
LGQPLS = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
LKXSJW = 7
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = 23
LSXUJU = 18
MCBFEG = 43
MJIGYO = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
MJVHFT = 9
MOUNBL = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
NBLKXS = 3
NPYYLI = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
NQJYMO = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
NRSJMC = 40
NZMJIG = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
OCTHBS = 30
OJRJHI = 21
OKPHUO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
ONPYYL = 20
OOQNRS = "".join(
    chr(c) for c in [79, 84, 65, 99, 116, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
OQNRSJ = 38
OUNBLK = 5
OUSPBW = 58
OUYNQJ = 34
PBWJYK = "".join(chr(c) for c in [83, 108, 97, 118, 101])
PFTSIF = "".join(chr(c) for c in [50, 52, 104])
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
PICXQI = 13
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
POUYNQ = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
PQIPOU = 62
PYYLIU = 22
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
QNRSJM = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
QXPICX = 12
RAHEOC = 28
RJHIUS = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
RSJMCB = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 110, 84, 105, 109, 101]
)
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 51])
SIFJBI = 49
SJMCBF = 41
SJWMNZ = "".join(
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
SKSOKP = 31
SOKPHU = 35
SOOQNR = 0
SPBWJY = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
SPFTSI = "".join(chr(c) for c in [65, 109, 80, 109])
SSAKQX = 10
SXUJUT = "".join(chr(c) for c in [80, 49])
TACCPQ = 55
THBSKS = 15
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
TYEKCW = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
UJUTYE = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
UNBLKX = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
UOJRJH = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
UQEXLS = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
USOOQN = 16
USPBWJ = "".join(
    chr(c) for c in [85, 110, 99, 111, 110, 102, 105, 103, 117, 114, 101, 100]
)
UTYEKC = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
UXFEFJ = 24
UYNQJY = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = 1
WJYKLG = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
WMNZMJ = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
XFEFJT = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
XLSXUJ = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 53])
XQGLRA = 26
XQIEFX = "".join(chr(c) for c in [72, 84, 82])
XSJWMN = 8
YKLGQP = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
YLIUXF = "".join(chr(c) for c in [67])
YMOUNB = 4
YNQJYM = 59
YOUSPB = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YYLIUX = "".join(chr(c) for c in [70])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = 57
ZUQEXL = 17
BIAMJM = []
BWJYKL = [USPBWJ, SPBWJY, PBWJYK]
CCPQIP = [UTYEKC, ACCPQI]
EXLSXU = [UQEXLS, QEXLSX]
FTSIFJ = [JVHFTH, SPFTSI, PFTSIF]
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
IFJBIA = [BMJVHF, ASSAKQ, SAKQXP, KQXPIC, XPICXQ, ICXQIE, CTHBSK]
JBIAMJ = [FJBIAM]
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
LIUXFE = [YYLIUX, YLIUXF]
MNZMJI = [JVHFTH, WMNZMJ]
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
QJYMOU = [UTYEKC, NQJYMO]
QPLSPF = [LGQPLS, GQPLSP]
XUJUTY = [PIPIVL, SXUJUT]
YEKCWA = [UTYEKC, TYEKCW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return IAMJMA

    @property
    def output_keys(self):
        return IFJBIA

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
                self.struct, GZUQEX, ZUQEXL, None, EXLSXU, None, None, QBMJVH
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, XUJUTY, None, None, QBMJVH
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, JUTYEK, None, YEKCWA, None, None, QBMJVH
            ),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoTempStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, ONPYYL, None, XUJUTY, None, None, QBMJVH
            ),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, LIUXFE, None, None, QBMJVH
            ),
            IUXFEF: GeckoByteStructAccessor(self.struct, IUXFEF, UXFEFJ, QBMJVH),
            XFEFJT: GeckoTempStructAccessor(self.struct, XFEFJT, FEFJTA, QBMJVH),
            EFJTAC: GeckoTempStructAccessor(self.struct, EFJTAC, FJTACC, QBMJVH),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, None, CCPQIP, None, None, QBMJVH
            ),
            CPQIPO: GeckoByteStructAccessor(self.struct, CPQIPO, PQIPOU, QBMJVH),
            QIPOUY: GeckoByteStructAccessor(self.struct, QIPOUY, IPOUYN, QBMJVH),
            POUYNQ: GeckoByteStructAccessor(self.struct, POUYNQ, OUYNQJ, QBMJVH),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, QJYMOU, None, None, QBMJVH
            ),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoTimeStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoTimeStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoTimeStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoTimeStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, MNZMJI, None, None, QBMJVH
            ),
            NZMJIG: GeckoBoolStructAccessor(
                self.struct, NZMJIG, ZMJIGY, SOOQNR, QBMJVH
            ),
            MJIGYO: GeckoBoolStructAccessor(
                self.struct, MJIGYO, ZMJIGY, JIGYOU, QBMJVH
            ),
            IGYOUS: GeckoBoolStructAccessor(
                self.struct, IGYOUS, ZMJIGY, GYOUSP, QBMJVH
            ),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, None, BWJYKL, None, None, QBMJVH
            ),
            WJYKLG: GeckoByteStructAccessor(self.struct, WJYKLG, JYKLGQ, QBMJVH),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, QPLSPF, None, None, QBMJVH
            ),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, FTSIFJ, None, None, QBMJVH
            ),
            TSIFJB: GeckoWordStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
        }

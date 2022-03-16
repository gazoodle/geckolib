#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v9'
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
ACCPQI = 32
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AKQXPI = 11
AONPYY = 21
ASSAKQ = "".join(chr(c) for c in [79, 117, 116, 50])
BFEGZU = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BSKSOK = 33
CBFEGZ = 45
CCPQIP = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
CPQIPO = 57
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 19
CXQIEF = 14
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFXQGL = 23
EGZUQE = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
EKCWAO = 1
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = "".join(chr(c) for c in [80, 49])
FEFJTA = "".join(chr(c) for c in [78, 105, 103, 104, 116])
FEGZUQ = 16
FJTACC = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 9
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
GLRAHE = 25
GQPLSP = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
GYOUSP = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
GZUQEX = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
HBSKSO = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 27
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 0
HUOJRJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
IUSOOQ = "".join(
    chr(c) for c in [79, 84, 65, 99, 116, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IUXFEF = 51
IVLASS = "".join(chr(c) for c in [])
JHIUSO = 15
JIGYOU = "".join(chr(c) for c in [83, 108, 97, 118, 101])
JMCBFE = 43
JTACCP = 31
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = "".join(
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
JYKLGQ = 22
JYMOUN = 7
KCWAON = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
KLGQPL = "".join(chr(c) for c in [50, 52, 104])
KPHUOJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 52])
KSOKPH = 34
KXSJWM = 55
LIUXFE = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
LKXSJW = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [76, 73])
LSXUJU = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
MCBFEG = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
MJIGYO = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
MJVHFT = 9
MNZMJI = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
MOUNBL = 8
NBLKXS = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
NPYYLI = "".join(chr(c) for c in [67])
NQJYMO = 3
NRSJMC = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 102, 102, 84, 105, 109, 101]
)
NZMJIG = 56
OCTHBS = 28
OJRJHI = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
OKPHUO = 35
ONPYYL = "".join(chr(c) for c in [70])
OOQNRS = 38
OQNRSJ = "".join(
    chr(c) for c in [67, 80, 79, 84, 77, 97, 120, 79, 110, 84, 105, 109, 101]
)
OUNBLK = "".join(
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
OUSPBW = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
OUYNQJ = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
PBWJYK = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
PHUOJR = 20
PICXQI = 13
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
POUYNQ = 4
PQIPOU = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 17
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QJYMOU = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
QNRSJM = 39
QPLSPF = 47
QXPICX = 12
RAHEOC = 26
RJHIUS = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
RSJMCB = 41
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 51])
SJMCBF = "".join(
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
SJWMNZ = 1
SKSOKP = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
SOKPHU = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
SOOQNR = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
SPBWJY = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
SSAKQX = 10
SXUJUT = 18
TACCPQ = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
THBSKS = 29
THECVY = "".join(chr(c) for c in [80, 50, 76])
TYEKCW = 46
UJUTYE = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
UNBLKX = 54
UOJRJH = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
UQEXLS = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
USOOQN = 36
USPBWJ = 59
UTYEKC = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
UXFEFJ = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
UYNQJY = 5
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
WJYKLG = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
WMNZMJ = 2
XFEFJT = 53
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 53])
XQGLRA = 24
XQIEFX = "".join(chr(c) for c in [72, 84, 82])
XSJWMN = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
XUJUTY = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
YEKCWA = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
YKLGQP = "".join(chr(c) for c in [65, 109, 80, 109])
YLIUXF = 49
YMOUNB = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
YNQJYM = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
YOUSPB = 58
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YYLIUX = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = "".join(
    chr(c) for c in [85, 110, 99, 111, 110, 102, 105, 103, 117, 114, 101, 100]
)
BLKXSJ = [JVHFTH, NBLKXS]
BWJYKL = [SPBWJY, PBWJYK]
EFJTAC = [XUJUTY, FEFJTA]
IGYOUS = [ZMJIGY, MJIGYO, JIGYOU]
JRJHIU = [HUOJRJ, UOJRJH, OJRJHI]
JUTYEK = [XUJUTY, UJUTYE]
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
LGQPLS = [JVHFTH, YKLGQP, KLGQPL]
PFTSIF = []
PLSPFT = [BMJVHF, ASSAKQ, SAKQXP, KQXPIC, XPICXQ, ICXQIE]
PYYLIU = [ONPYYL, NPYYLI]
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
QIPOUY = [XUJUTY, PQIPOU]
SPFTSI = [LSPFTS]
XLSXUJ = [PIPIVL, EXLSXU]
ZUQEXL = [EGZUQE, GZUQEX]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return FTSIFJ

    @property
    def output_keys(self):
        return PLSPFT

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
            CTHBSK: GeckoByteStructAccessor(self.struct, CTHBSK, THBSKS, QBMJVH),
            HBSKSO: GeckoByteStructAccessor(self.struct, HBSKSO, BSKSOK, QBMJVH),
            SKSOKP: GeckoByteStructAccessor(self.struct, SKSOKP, KSOKPH, QBMJVH),
            SOKPHU: GeckoByteStructAccessor(self.struct, SOKPHU, OKPHUO, QBMJVH),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, JRJHIU, None, None, QBMJVH
            ),
            RJHIUS: GeckoBoolStructAccessor(
                self.struct, RJHIUS, JHIUSO, HIUSOO, QBMJVH
            ),
            IUSOOQ: GeckoTempStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoWordStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoWordStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoWordStructAccessor(self.struct, SJMCBF, JMCBFE, QBMJVH),
            MCBFEG: GeckoByteStructAccessor(self.struct, MCBFEG, CBFEGZ, QBMJVH),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, FEGZUQ, None, ZUQEXL, None, None, QBMJVH
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, None, XLSXUJ, None, None, QBMJVH
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, None, JUTYEK, None, None, QBMJVH
            ),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoTempStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, CWAONP, None, XLSXUJ, None, None, QBMJVH
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, PYYLIU, None, None, QBMJVH
            ),
            YYLIUX: GeckoTempStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoTempStructAccessor(self.struct, LIUXFE, IUXFEF, QBMJVH),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, None, EFJTAC, None, None, QBMJVH
            ),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, QBMJVH),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, QBMJVH),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, QIPOUY, None, None, QBMJVH
            ),
            IPOUYN: GeckoByteStructAccessor(self.struct, IPOUYN, POUYNQ, QBMJVH),
            OUYNQJ: GeckoTimeStructAccessor(self.struct, OUYNQJ, UYNQJY, QBMJVH),
            YNQJYM: GeckoTimeStructAccessor(self.struct, YNQJYM, NQJYMO, QBMJVH),
            QJYMOU: GeckoTimeStructAccessor(self.struct, QJYMOU, JYMOUN, QBMJVH),
            YMOUNB: GeckoTimeStructAccessor(self.struct, YMOUNB, MOUNBL, QBMJVH),
            OUNBLK: GeckoEnumStructAccessor(
                self.struct, OUNBLK, UNBLKX, None, BLKXSJ, None, None, QBMJVH
            ),
            LKXSJW: GeckoBoolStructAccessor(
                self.struct, LKXSJW, KXSJWM, HIUSOO, QBMJVH
            ),
            XSJWMN: GeckoBoolStructAccessor(
                self.struct, XSJWMN, KXSJWM, SJWMNZ, QBMJVH
            ),
            JWMNZM: GeckoBoolStructAccessor(
                self.struct, JWMNZM, KXSJWM, WMNZMJ, QBMJVH
            ),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, IGYOUS, None, None, QBMJVH
            ),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, USPBWJ, None, BWJYKL, None, None, QBMJVH
            ),
            WJYKLG: GeckoEnumStructAccessor(
                self.struct, WJYKLG, JYKLGQ, None, LGQPLS, None, None, QBMJVH
            ),
            GQPLSP: GeckoWordStructAccessor(self.struct, GQPLSP, QPLSPF, QBMJVH),
        }

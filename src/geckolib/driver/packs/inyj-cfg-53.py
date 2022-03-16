#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v53'
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
ACCPQI = 63
AHEOCT = 39
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = 3
AOAWBS = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
AWBSIR = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
BFEGZU = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
BIAMJM = 1
BLKXSJ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 34
BQSNQL = 45
BSIRYX = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
BSKSOK = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
BWJYKL = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
BXYBQS = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
CBFEGZ = 57
CCPQIP = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
CPQIPO = 1
CQBMJV = 0
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 78
CXQIEF = 36
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
EFXQGL = 38
EGZUQE = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
EKCWAO = 62
EOCTHB = 79
FEFJTA = 30
FEGZUQ = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
FJBIAM = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
FJTACC = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [50, 52, 104])
GLRAHE = 15
GQPLSP = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
GYOUSP = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
HBSKSO = 80
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
HUOJRJ = 81
IAMJMA = "".join(
    chr(c)
    for c in [
        67,
        108,
        101,
        97,
        110,
        117,
        112,
        79,
        110,
        67,
        117,
        115,
        116,
        111,
        109,
        75,
        101,
        121,
    ]
)
IBXYBQ = 43
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
IFJBIA = 72
IGYOUS = 53
IKFWRK = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
INEJNI = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [70])
IUSOOQ = 32
IUXFEF = 29
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
JHIUSO = 2
JIGYOU = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
JMAOAW = 76
JNIBXY = 5
JUIKFW = 64
JUTYEK = 60
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = 51
JYKLGQ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
JYMOUN = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
KCWAON = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
KFWRKI = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
KINEJN = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
KLGQPL = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
KPHUOJ = 56
KQXPIC = 14
KSOKPH = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
KXSJWM = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = 8
LIUXFE = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
LJUIKF = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
LSPFTS = 71
LSXUJU = 58
MAOAWB = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
MCBFEG = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
MJIGYO = 52
MJMAOA = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
MJVHFT = 12
MNZMJI = "".join(chr(c) for c in [67, 69])
MOUNBL = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
NBLKXS = 70
NEJNIB = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
NIBXYB = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
NMHXEK = 53
NPYYLI = 28
NQJYMO = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
NRSJMC = 27
OCTHBS = "".join(chr(c) for c in [76, 73])
OJRJHI = "".join(chr(c) for c in [79, 119, 110])
OKPHUO = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
ONPYYL = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
OOQNRS = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
OUNBLK = 68
OUSPBW = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
PBWJYK = 3
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
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
POUYNQ = "".join(chr(c) for c in [67])
PQIPOU = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
PYYLIU = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [72, 105])
QFYLJU = "".join(chr(c) for c in [65, 109, 80, 109])
QGLRAH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
QIEFXQ = 37
QIPOUY = 33
QJYMOU = 35
QNRSJM = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
QPLSPF = 10
QSNQLN = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
QXPICX = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
RAHEOC = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
RJHIUS = 0
RKINEJ = 4
RSJMCB = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
RYXBQF = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
SAKQXP = 13
SIFJBI = "".join(
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
SIRYXB = "".join(chr(c) for c in [83, 108, 97, 118, 101])
SJMCBF = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
SJWMNZ = "".join(chr(c) for c in [85, 76, 95, 67, 69])
SKSOKP = 54
SNQLNM = 46
SOKPHU = 55
SOOQNR = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
SPBWJY = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
SPFTSI = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SXUJUT = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
TACCPQ = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
THBSKS = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = 82
TYEKCW = 61
UIKFWR = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
UJUTYE = "".join(
    chr(c)
    for c in [
        67,
        112,
        79,
        102,
        102,
        84,
        105,
        109,
        101,
        68,
        117,
        114,
        105,
        110,
        103,
        79,
        84,
    ]
)
UNBLKX = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
UOJRJH = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
UQEXLS = "".join(chr(c) for c in [76, 111])
USOOQN = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
UTYEKC = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        79,
        110,
        84,
        105,
        109,
        101,
        68,
        117,
        114,
        105,
        110,
        103,
        79,
        84,
    ]
)
UYNQJY = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VLASSA = "".join(chr(c) for c in [])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(chr(c) for c in [80, 49])
WBSIRY = 73
WJYKLG = 4
WMNZMJ = "".join(chr(c) for c in [85, 76])
WRKINE = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
XBQFYL = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
XFEFJT = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
XLSXUJ = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
XPICXQ = 16
XQGLRA = 40
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
XSJWMN = 77
XUJUTY = 59
XYBQSN = 44
YBQSNQ = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
YEKCWA = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
YKLGQP = 6
YMOUNB = 66
YNQJYM = 31
YOUSPB = 74
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = 75
YYLIUX = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
ZUQEXL = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
AONPYY = [JVHFTH, WAONPY, PIPIVL]
ASSAKQ = [
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
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    LASSAK,
]
CTHBSK = [
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    OCTHBS,
]
EJNIBX = [INEJNI, NEJNIB]
EXLSXU = [UQEXLS, QEXLSX]
FWRKIN = [IKFWRK, KFWRKI]
GZUQEX = [BFEGZU, FEGZUQ, EGZUQE]
IRYXBQ = [VLASSA, BSIRYX, SIRYXB]
JMCBFE = [RSJMCB, SJMCBF]
JRJHIU = [UOJRJH, OJRJHI]
JTACCP = [EFJTAC, FJTACC]
LKXSJW = [EFJTAC, BLKXSJ]
LNMHXE = []
LRAHEO = [
    JVHFTH,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    PIPIVL,
]
NQLNMH = [BMJVHF, SSAKQX, AKQXPI, QXPICX, QGLRAH, HEOCTH]
NZMJIG = [WMNZMJ, MNZMJI]
OAWBSI = [MAOAWB, AOAWBS]
OQNRSJ = [USOOQN, SOOQNR, OOQNRS]
OUYNQJ = [IPOUYN, POUYNQ]
PFTSIF = [JVHFTH, SPFTSI]
PICXQI = [
    JVHFTH,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    IVLASS,
]
QLNMHX = [OCTHBS]
USPBWJ = [EFJTAC, OUSPBW]
UXFEFJ = [PIPIVL, WAONPY]
YLIUXF = [PYYLIU, YYLIUX]
YLJUIK = [JVHFTH, QFYLJU, FYLJUI]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return NMHXEK

    @property
    def output_keys(self):
        return NQLNMH

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, ASSAKQ, None, None, QBMJVH
            ),
            SSAKQX: GeckoEnumStructAccessor(
                self.struct, SSAKQX, SAKQXP, None, ASSAKQ, None, None, QBMJVH
            ),
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, None, ASSAKQ, None, None, QBMJVH
            ),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, None, PICXQI, None, None, QBMJVH
            ),
            ICXQIE: GeckoByteStructAccessor(self.struct, ICXQIE, CXQIEF, QBMJVH),
            XQIEFX: GeckoByteStructAccessor(self.struct, XQIEFX, QIEFXQ, QBMJVH),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoEnumStructAccessor(
                self.struct, QGLRAH, GLRAHE, None, LRAHEO, None, None, QBMJVH
            ),
            RAHEOC: GeckoByteStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, EOCTHB, None, CTHBSK, None, None, None
            ),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, None),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, QBMJVH),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, QBMJVH),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, QBMJVH),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, RJHIUS, JRJHIU, None, JHIUSO, QBMJVH
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, IUSOOQ, None, OQNRSJ, None, None, QBMJVH
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, NRSJMC, None, JMCBFE, None, None, QBMJVH
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, GZUQEX, None, None, QBMJVH
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, HUOJRJ, JHIUSO, EXLSXU, None, JHIUSO, QBMJVH
            ),
            XLSXUJ: GeckoByteStructAccessor(self.struct, XLSXUJ, LSXUJU, QBMJVH),
            SXUJUT: GeckoByteStructAccessor(self.struct, SXUJUT, XUJUTY, QBMJVH),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, QBMJVH),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, CWAONP, None, AONPYY, None, None, QBMJVH
            ),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, NPYYLI, None, YLIUXF, None, None, QBMJVH
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, UXFEFJ, None, None, QBMJVH
            ),
            XFEFJT: GeckoEnumStructAccessor(
                self.struct, XFEFJT, FEFJTA, None, JTACCP, None, None, QBMJVH
            ),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, QBMJVH),
            CCPQIP: GeckoTempStructAccessor(self.struct, CCPQIP, CPQIPO, QBMJVH),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, UXFEFJ, None, None, QBMJVH
            ),
            NQJYMO: GeckoByteStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoTempStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoTempStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, NBLKXS, None, LKXSJW, None, None, QBMJVH
            ),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, NZMJIG, None, None, QBMJVH
            ),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoEnumStructAccessor(
                self.struct, GYOUSP, YOUSPB, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoByteStructAccessor(self.struct, SPBWJY, PBWJYK, QBMJVH),
            BWJYKL: GeckoTimeStructAccessor(self.struct, BWJYKL, WJYKLG, QBMJVH),
            JYKLGQ: GeckoTimeStructAccessor(self.struct, JYKLGQ, YKLGQP, QBMJVH),
            KLGQPL: GeckoTimeStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoTimeStructAccessor(self.struct, GQPLSP, QPLSPF, QBMJVH),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, PFTSIF, None, None, QBMJVH
            ),
            FTSIFJ: GeckoBoolStructAccessor(
                self.struct, FTSIFJ, TSIFJB, RJHIUS, QBMJVH
            ),
            SIFJBI: GeckoBoolStructAccessor(
                self.struct, SIFJBI, IFJBIA, JHIUSO, QBMJVH
            ),
            FJBIAM: GeckoBoolStructAccessor(
                self.struct, FJBIAM, IFJBIA, RJHIUS, QBMJVH
            ),
            JBIAMJ: GeckoBoolStructAccessor(
                self.struct, JBIAMJ, IFJBIA, BIAMJM, QBMJVH
            ),
            IAMJMA: GeckoBoolStructAccessor(
                self.struct, IAMJMA, IFJBIA, AMJMAO, QBMJVH
            ),
            MJMAOA: GeckoEnumStructAccessor(
                self.struct, MJMAOA, JMAOAW, None, OAWBSI, None, None, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, IRYXBQ, None, None, QBMJVH
            ),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, YLJUIK, None, None, QBMJVH
            ),
            LJUIKF: GeckoWordStructAccessor(self.struct, LJUIKF, JUIKFW, QBMJVH),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, HUOJRJ, BIAMJM, FWRKIN, None, JHIUSO, QBMJVH
            ),
            WRKINE: GeckoBoolStructAccessor(
                self.struct, WRKINE, HUOJRJ, RKINEJ, QBMJVH
            ),
            KINEJN: GeckoEnumStructAccessor(
                self.struct, KINEJN, HUOJRJ, JNIBXY, EJNIBX, None, JHIUSO, QBMJVH
            ),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoByteStructAccessor(self.struct, BXYBQS, XYBQSN, QBMJVH),
            YBQSNQ: GeckoByteStructAccessor(self.struct, YBQSNQ, BQSNQL, QBMJVH),
            QSNQLN: GeckoByteStructAccessor(self.struct, QSNQLN, SNQLNM, QBMJVH),
        }

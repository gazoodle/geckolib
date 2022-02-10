#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v53'
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
ACCPQI = 29
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
AOAWBS = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
AONPYY = 60
AWBSIR = 1
BIAMJM = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
BLKXSJ = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
BQSNQL = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
BSIRYX = 3
BSKSOK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BWJYKL = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
BXYBQS = 4
CBFEGZ = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
CPQIPO = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 59
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
EFXQGL = 36
EGZUQE = 27
EJNIBX = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
EKCWAO = 58
EKVKZI = 46
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = 57
FEFJTA = 28
FEGZUQ = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
FJBIAM = "".join(
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
FJTACC = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
FWRKIN = "".join(chr(c) for c in [65, 109, 80, 109])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
GLRAHE = 38
GQPLSP = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
GYOUSP = 51
GZUQEX = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 56
HUOJRJ = 80
HXEKVK = 45
IBXYBQ = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
ICXQIE = 16
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = 10
IGYOUS = "".join(chr(c) for c in [85, 76, 95, 67, 69])
IKFWRK = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
INEJNI = 64
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
IRYXBQ = 76
IUSOOQ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
IUXFEF = "".join(chr(c) for c in [80, 49])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = 71
JHIUSO = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
JIGYOU = 77
JMAOAW = "".join(
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
JMCBFE = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
JNIBXY = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
JRJHIU = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
JUIKFW = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
JUTYEK = "".join(chr(c) for c in [76, 111])
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = 68
JYKLGQ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
JYMOUN = 33
KCWAON = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
KFWRKI = 34
KINEJN = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
KLGQPL = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
KQXPIC = 14
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
KXSJWM = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LIUXFE = 78
LKXSJW = 35
LNMHXE = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = 4
LSXUJU = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
MAOAWB = 72
MCBFEG = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
MHXEKV = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
MJIGYO = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
MJMAOA = 82
MJVHFT = 12
MNZMJI = 70
MOUNBL = "".join(chr(c) for c in [67])
NBLKXS = 31
NEJNIB = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
NMHXEK = 44
NPYYLI = 61
NQJYMO = 1
NQLNMH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
NRSJMC = 2
NZMJIG = "".join(chr(c) for c in [78, 105, 103, 104, 116])
OAWBSI = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
OCTHBS = 42
OJRJHI = 54
OKPHUO = "".join(chr(c) for c in [76, 73])
ONPYYL = "".join(
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
OOQNRS = "".join(chr(c) for c in [79, 119, 110])
OUSPBW = "".join(chr(c) for c in [67, 69])
OUYNQJ = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
PBWJYK = 52
PFTSIF = 6
PHUOJR = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
PQIPOU = 30
PYYLIU = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
QFYLJU = 73
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
QJYMOU = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
QLNMHX = 43
QNRSJM = 0
QPLSPF = 3
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = 55
RSJMCB = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
RYXBQF = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
SAKQXP = 13
SIFJBI = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
SIRYXB = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
SJMCBF = 32
SJWMNZ = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SKSOKP = 41
SNQLNM = 5
SOKPHU = 79
SOOQNR = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
SPBWJY = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
SPFTSI = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SXUJUT = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
TACCPQ = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = 8
UIKFWR = 75
UJUTYE = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
UNBLKX = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
UOJRJH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
USOOQN = 81
UTYEKC = "".join(chr(c) for c in [72, 105])
UYNQJY = 63
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VLASSA = "".join(chr(c) for c in [])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(
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
WBSIRY = "".join(
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
WJYKLG = 53
WMNZMJ = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
WRKINE = "".join(chr(c) for c in [50, 52, 104])
XEKVKZ = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
XFEFJT = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
XLSXUJ = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
XPICXQ = 15
XQGLRA = 37
XQIEFX = 18
XSJWMN = 66
XYBQSN = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
YBQSNQ = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
YEKCWA = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
YKLGQP = 74
YLIUXF = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
YLJUIK = "".join(chr(c) for c in [83, 108, 97, 118, 101])
YMOUNB = "".join(chr(c) for c in [70])
YNQJYM = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
YOUSPB = "".join(chr(c) for c in [85, 76])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
YYLIUX = 62
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 53
ZUQEXL = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
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
BFEGZU = [JMCBFE, MCBFEG, CBFEGZ]
CCPQIP = [PIPIVL, IUXFEF]
HBSKSO = [
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
IAMJMA = [JVHFTH, BIAMJM]
JTACCP = [EFJTAC, FJTACC]
KPHUOJ = [
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
    OKPHUO,
]
KVKZIL = [BMJVHF, SSAKQX, AKQXPI, QXPICX, PICXQI, CXQIEF, CTHBSK, KSOKPH]
KZILXW = []
LGQPLS = [QIPOUY, KLGQPL]
LJUIKF = [VLASSA, FYLJUI, YLJUIK]
NIBXYB = [EJNIBX, JNIBXY]
OQNRSJ = [SOOQNR, OOQNRS]
OUNBLK = [YMOUNB, MOUNBL]
POUYNQ = [QIPOUY, IPOUYN]
QIEFXQ = [
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
QSNQLN = [YBQSNQ, BQSNQL]
RKINEJ = [JVHFTH, FWRKIN, WRKINE]
TYEKCW = [JUTYEK, UTYEKC]
UQEXLS = [GZUQEX, ZUQEXL]
USPBWJ = [YOUSPB, OUSPBW]
UXFEFJ = [JVHFTH, IUXFEF, PIPIVL]
VKZILX = [OKPHUO]
XBQFYL = [RYXBQF, YXBQFY]
XUJUTY = [XLSXUJ, LSXUJU, SXUJUT]
ZMJIGY = [QIPOUY, NZMJIG]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return ZILXWA

    @property
    def output_keys(self):
        return KVKZIL

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
                self.struct, QXPICX, XPICXQ, None, ASSAKQ, None, None, QBMJVH
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, ASSAKQ, None, None, QBMJVH
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, QIEFXQ, None, None, QBMJVH
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
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, KPHUOJ, None, None, None
            ),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, None),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, QBMJVH),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, QBMJVH),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, QBMJVH),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, QNRSJM, OQNRSJ, None, NRSJMC, QBMJVH
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, SJMCBF, None, BFEGZU, None, None, QBMJVH
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, EGZUQE, None, UQEXLS, None, None, QBMJVH
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, EXLSXU, None, XUJUTY, None, None, QBMJVH
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, USOOQN, NRSJMC, TYEKCW, None, NRSJMC, QBMJVH
            ),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, QBMJVH),
            ONPYYL: GeckoByteStructAccessor(self.struct, ONPYYL, NPYYLI, QBMJVH),
            PYYLIU: GeckoByteStructAccessor(self.struct, PYYLIU, YYLIUX, QBMJVH),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, UXFEFJ, None, None, QBMJVH
            ),
            XFEFJT: GeckoEnumStructAccessor(
                self.struct, XFEFJT, FEFJTA, None, JTACCP, None, None, QBMJVH
            ),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, None, CCPQIP, None, None, QBMJVH
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, PQIPOU, None, POUYNQ, None, None, QBMJVH
            ),
            OUYNQJ: GeckoByteStructAccessor(self.struct, OUYNQJ, UYNQJY, QBMJVH),
            YNQJYM: GeckoTempStructAccessor(self.struct, YNQJYM, NQJYMO, QBMJVH),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, OUNBLK, None, None, QBMJVH
            ),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, NBLKXS, None, CCPQIP, None, None, QBMJVH
            ),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoTempStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoTempStructAccessor(self.struct, SJWMNZ, JWMNZM, QBMJVH),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, MNZMJI, None, ZMJIGY, None, None, QBMJVH
            ),
            MJIGYO: GeckoByteStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoEnumStructAccessor(
                self.struct, IGYOUS, GYOUSP, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoByteStructAccessor(self.struct, SPBWJY, PBWJYK, QBMJVH),
            BWJYKL: GeckoByteStructAccessor(self.struct, BWJYKL, WJYKLG, QBMJVH),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, YKLGQP, None, LGQPLS, None, None, QBMJVH
            ),
            GQPLSP: GeckoByteStructAccessor(self.struct, GQPLSP, QPLSPF, QBMJVH),
            PLSPFT: GeckoTimeStructAccessor(self.struct, PLSPFT, LSPFTS, QBMJVH),
            SPFTSI: GeckoTimeStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoTimeStructAccessor(self.struct, FTSIFJ, TSIFJB, QBMJVH),
            SIFJBI: GeckoTimeStructAccessor(self.struct, SIFJBI, IFJBIA, QBMJVH),
            FJBIAM: GeckoEnumStructAccessor(
                self.struct, FJBIAM, JBIAMJ, None, IAMJMA, None, None, QBMJVH
            ),
            AMJMAO: GeckoBoolStructAccessor(
                self.struct, AMJMAO, MJMAOA, QNRSJM, QBMJVH
            ),
            JMAOAW: GeckoBoolStructAccessor(
                self.struct, JMAOAW, MAOAWB, NRSJMC, QBMJVH
            ),
            AOAWBS: GeckoBoolStructAccessor(
                self.struct, AOAWBS, MAOAWB, QNRSJM, QBMJVH
            ),
            OAWBSI: GeckoBoolStructAccessor(
                self.struct, OAWBSI, MAOAWB, AWBSIR, QBMJVH
            ),
            WBSIRY: GeckoBoolStructAccessor(
                self.struct, WBSIRY, MAOAWB, BSIRYX, QBMJVH
            ),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, IRYXBQ, None, XBQFYL, None, None, QBMJVH
            ),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, LJUIKF, None, None, QBMJVH
            ),
            JUIKFW: GeckoByteStructAccessor(self.struct, JUIKFW, UIKFWR, QBMJVH),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, None, RKINEJ, None, None, QBMJVH
            ),
            KINEJN: GeckoWordStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, USOOQN, AWBSIR, NIBXYB, None, NRSJMC, QBMJVH
            ),
            IBXYBQ: GeckoBoolStructAccessor(
                self.struct, IBXYBQ, USOOQN, BXYBQS, QBMJVH
            ),
            XYBQSN: GeckoEnumStructAccessor(
                self.struct, XYBQSN, USOOQN, SNQLNM, QSNQLN, None, NRSJMC, QBMJVH
            ),
            NQLNMH: GeckoByteStructAccessor(self.struct, NQLNMH, QLNMHX, QBMJVH),
            LNMHXE: GeckoByteStructAccessor(self.struct, LNMHXE, NMHXEK, QBMJVH),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoByteStructAccessor(self.struct, XEKVKZ, EKVKZI, QBMJVH),
        }

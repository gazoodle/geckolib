#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v54'
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
ACCPQI = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AJVDQL = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = 3
AOAWBS = 6
AONPYY = "".join(
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
AWBSIR = 23
BFEGZU = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
BLKXSJ = 31
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQSNQL = 34
BSIRYX = 8
BSKSOK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BWJYKL = "".join(chr(c) for c in [78, 105, 103, 104, 116])
BXYBQS = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
CBFEGZ = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
CCPQIP = 29
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
DNIBXT = 54
DQLAII = 45
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 28
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
EJNIBX = 73
EKCWAO = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
EKVKZI = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
FEFJTA = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
FJBIAM = 74
FJTACC = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 52
FWRKIN = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = 82
GLRAHE = 38
GQPLSP = "".join(chr(c) for c in [85, 76, 95, 67, 69])
GYOUSP = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
GZUQEX = 27
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 56
HUOJRJ = 80
HXEKVK = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
IAMJMA = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
ICXQIE = 16
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
IGYOUS = 35
IKFWRK = 1
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
IRYXBQ = 10
IUSOOQ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
IUXFEF = 78
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
JHIUSO = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
JIGYOU = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
JMAOAW = 4
JMCBFE = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
JNIBXY = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
JRJHIU = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
JTACCP = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
JUIKFW = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
JUTYEK = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
JVDQLA = 44
JVHFTH = "".join(chr(c) for c in [78, 65])
JYKLGQ = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
JYMOUN = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
KCWAON = 58
KFWRKI = "".join(
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
KINEJN = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
KLGQPL = "".join(
    chr(c)
    for c in [
        77,
        97,
        120,
        78,
        117,
        109,
        98,
        101,
        114,
        79,
        102,
        80,
        104,
        97,
        115,
        101,
        115,
    ]
)
KQXPIC = 14
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
KVKZIL = 4
KXSJWM = 25
KZILXW = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
LAIIDN = 46
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = 26
LIUXFE = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
LJUIKF = 72
LKXSJW = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
LNMHXE = 64
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [67, 69])
LSXUJU = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
LXWAJV = 5
MAOAWB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
MCBFEG = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
MHXEKV = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
MJIGYO = 3
MJMAOA = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
MJVHFT = 12
MNZMJI = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
MOUNBL = "".join(chr(c) for c in [70])
NBLKXS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
NEJNIB = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
NIBXYB = "".join(chr(c) for c in [83, 108, 97, 118, 101])
NMHXEK = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
NPYYLI = "".join(
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
NQJYMO = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
NRSJMC = 2
NZMJIG = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
OAWBSI = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
OCTHBS = 42
OJRJHI = 54
OKPHUO = "".join(chr(c) for c in [76, 73])
ONPYYL = 60
OOQNRS = "".join(chr(c) for c in [79, 119, 110])
OUNBLK = "".join(chr(c) for c in [67])
OUSPBW = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
PBWJYK = 70
PFTSIF = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
PHUOJR = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [85, 76])
POUYNQ = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
PQIPOU = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
PYYLIU = 61
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QFYLJU = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = 30
QJYMOU = 1
QLAIID = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
QLNMHX = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
QNRSJM = 0
QPLSPF = 51
QSNQLN = "".join(chr(c) for c in [65, 109, 80, 109])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = 55
RKINEJ = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
RSJMCB = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
RYXBQF = "".join(
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
SAKQXP = 13
SIFJBI = 53
SIRYXB = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
SJMCBF = 32
SJWMNZ = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
SKSOKP = 41
SNQLNM = "".join(chr(c) for c in [50, 52, 104])
SOKPHU = 79
SOOQNR = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
SPBWJY = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SXUJUT = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
TYEKCW = "".join(chr(c) for c in [72, 105])
UIKFWR = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
UOJRJH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UQEXLS = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
USOOQN = 81
USPBWJ = 68
UTYEKC = "".join(chr(c) for c in [76, 111])
UXFEFJ = "".join(chr(c) for c in [80, 49])
UYNQJY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
VDQLAI = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
VLASSA = "".join(chr(c) for c in [])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 43
WAONPY = 59
WBSIRY = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
WMNZMJ = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
WRKINE = 76
XBQFYL = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
XLSXUJ = 57
XPICXQ = 15
XQGLRA = 37
XQIEFX = 18
XSJWMN = "".join(chr(c) for c in [105, 110, 70, 108, 111])
XUJUTY = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
XWAJVD = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
XYBQSN = 75
YBQSNQ = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
YKLGQP = 77
YLIUXF = 62
YLJUIK = "".join(
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
YMOUNB = 33
YNQJYM = 63
YOUSPB = 66
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = 71
YYLIUX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
ZUQEXL = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
AIIDNI = [BMJVHF, SSAKQX, AKQXPI, QXPICX, PICXQI, CXQIEF, CTHBSK, KSOKPH]
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
BIAMJM = [IPOUYN, JBIAMJ]
BQFYLJ = [JVHFTH, ZUQEXL, XBQFYL]
CPQIPO = [PIPIVL, UXFEFJ]
FEGZUQ = [JMCBFE, MCBFEG, CBFEGZ, BFEGZU]
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
IBXYBQ = [VLASSA, JNIBXY, NIBXYB]
IDNIBX = []
IIDNIB = [OKPHUO]
ILXWAJ = [KZILXW, ZILXWA]
INEJNI = [RKINEJ, KINEJN]
JWMNZM = [XSJWMN, SJWMNZ]
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
NQLNMH = [JVHFTH, QSNQLN, SNQLNM]
OQNRSJ = [SOOQNR, OOQNRS]
OUYNQJ = [IPOUYN, POUYNQ]
QEXLSX = [ZUQEXL, UQEXLS]
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
SPFTSI = [PLSPFT, LSPFTS]
TACCPQ = [FJTACC, JTACCP]
UJUTYE = [LSXUJU, SXUJUT, XUJUTY]
UNBLKX = [MOUNBL, OUNBLK]
WJYKLG = [IPOUYN, BWJYKL]
XEKVKZ = [MHXEKV, HXEKVK]
XFEFJT = [JVHFTH, UXFEFJ, PIPIVL]
YEKCWA = [UTYEKC, TYEKCW]
ZMJIGY = [MNZMJI, NZMJIG]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return DNIBXT

    @property
    def output_keys(self):
        return AIIDNI

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
                self.struct, RSJMCB, SJMCBF, None, FEGZUQ, None, None, QBMJVH
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, GZUQEX, None, QEXLSX, None, None, QBMJVH
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, None, UJUTYE, None, None, QBMJVH
            ),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, USOOQN, NRSJMC, YEKCWA, None, NRSJMC, QBMJVH
            ),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoByteStructAccessor(self.struct, NPYYLI, PYYLIU, QBMJVH),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, XFEFJT, None, None, QBMJVH
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, EFJTAC, None, TACCPQ, None, None, QBMJVH
            ),
            ACCPQI: GeckoEnumStructAccessor(
                self.struct, ACCPQI, CCPQIP, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoByteStructAccessor(self.struct, UYNQJY, YNQJYM, QBMJVH),
            NQJYMO: GeckoTempStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, YMOUNB, None, UNBLKX, None, None, QBMJVH
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, BLKXSJ, None, CPQIPO, None, None, QBMJVH
            ),
            LKXSJW: GeckoEnumStructAccessor(
                self.struct, LKXSJW, KXSJWM, None, JWMNZM, None, None, QBMJVH
            ),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, USOOQN, MJIGYO, ZMJIGY, None, NRSJMC, QBMJVH
            ),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoTempStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoTempStructAccessor(self.struct, OUSPBW, USPBWJ, QBMJVH),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, WJYKLG, None, None, QBMJVH
            ),
            JYKLGQ: GeckoByteStructAccessor(self.struct, JYKLGQ, YKLGQP, QBMJVH),
            KLGQPL: GeckoByteStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, QPLSPF, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoByteStructAccessor(self.struct, PFTSIF, FTSIFJ, QBMJVH),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoEnumStructAccessor(
                self.struct, IFJBIA, FJBIAM, None, BIAMJM, None, None, QBMJVH
            ),
            IAMJMA: GeckoByteStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoTimeStructAccessor(self.struct, MJMAOA, JMAOAW, QBMJVH),
            MAOAWB: GeckoTimeStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoTimeStructAccessor(self.struct, OAWBSI, AWBSIR, QBMJVH),
            WBSIRY: GeckoTimeStructAccessor(self.struct, WBSIRY, BSIRYX, QBMJVH),
            SIRYXB: GeckoTimeStructAccessor(self.struct, SIRYXB, IRYXBQ, QBMJVH),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, YXBQFY, None, BQFYLJ, None, None, QBMJVH
            ),
            QFYLJU: GeckoBoolStructAccessor(
                self.struct, QFYLJU, FYLJUI, QNRSJM, QBMJVH
            ),
            YLJUIK: GeckoBoolStructAccessor(
                self.struct, YLJUIK, LJUIKF, NRSJMC, QBMJVH
            ),
            JUIKFW: GeckoBoolStructAccessor(
                self.struct, JUIKFW, LJUIKF, QNRSJM, QBMJVH
            ),
            UIKFWR: GeckoBoolStructAccessor(
                self.struct, UIKFWR, LJUIKF, IKFWRK, QBMJVH
            ),
            KFWRKI: GeckoBoolStructAccessor(
                self.struct, KFWRKI, LJUIKF, MJIGYO, QBMJVH
            ),
            FWRKIN: GeckoEnumStructAccessor(
                self.struct, FWRKIN, WRKINE, None, INEJNI, None, None, QBMJVH
            ),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, EJNIBX, None, IBXYBQ, None, None, QBMJVH
            ),
            BXYBQS: GeckoByteStructAccessor(self.struct, BXYBQS, XYBQSN, QBMJVH),
            YBQSNQ: GeckoEnumStructAccessor(
                self.struct, YBQSNQ, BQSNQL, None, NQLNMH, None, None, QBMJVH
            ),
            QLNMHX: GeckoWordStructAccessor(self.struct, QLNMHX, LNMHXE, QBMJVH),
            NMHXEK: GeckoEnumStructAccessor(
                self.struct, NMHXEK, USOOQN, IKFWRK, XEKVKZ, None, NRSJMC, QBMJVH
            ),
            EKVKZI: GeckoBoolStructAccessor(
                self.struct, EKVKZI, USOOQN, KVKZIL, QBMJVH
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, USOOQN, LXWAJV, ILXWAJ, None, NRSJMC, QBMJVH
            ),
            XWAJVD: GeckoByteStructAccessor(self.struct, XWAJVD, WAJVDQ, QBMJVH),
            AJVDQL: GeckoByteStructAccessor(self.struct, AJVDQL, JVDQLA, QBMJVH),
            VDQLAI: GeckoByteStructAccessor(self.struct, VDQLAI, DQLAII, QBMJVH),
            QLAIID: GeckoByteStructAccessor(self.struct, QLAIID, LAIIDN, QBMJVH),
        }

#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v55'
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
ACCPQI = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AIIDNI = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
AJVDQL = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AOAWBS = 4
AONPYY = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
AWBSIR = 6
BFEGZU = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
BIAMJM = 74
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 71
BQSNQL = 75
BSIRYX = 23
BSKSOK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BWJYKL = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
BXYBQS = "".join(chr(c) for c in [83, 108, 97, 118, 101])
CBFEGZ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
CPQIPO = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
DQLAII = 44
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFXQGL = 36
EGZUQE = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
EKCWAO = "".join(chr(c) for c in [72, 105])
EKVKZI = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
FEFJTA = "".join(chr(c) for c in [80, 49])
FEGZUQ = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FJBIAM = 53
FJTACC = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FWRKIN = 1
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
GLRAHE = 38
GQPLSP = "".join(
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
GYOUSP = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 55
HUOJRJ = 80
HXEKVK = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
IAMJMA = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
IBXTIA = 55
IBXYBQ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
ICXQIE = 16
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
IGYOUS = 3
IIDNIB = 46
IKFWRK = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
ILXWAJ = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
INEJNI = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
IRYXBQ = 8
IUSOOQ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
IUXFEF = 62
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
JHIUSO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
JMAOAW = 3
JMCBFE = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
JNIBXY = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
JRJHIU = "".join(chr(c) for c in [80, 49, 76, 84, 105, 109, 101, 79, 117, 116])
JTACCP = 28
JUIKFW = "".join(
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
JUTYEK = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
JVDQLA = 43
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = "".join(chr(c) for c in [105, 110, 70, 108, 111])
JYKLGQ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
JYMOUN = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
KFWRKI = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
KINEJN = 76
KLGQPL = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
KQXPIC = 14
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
KXSJWM = 31
KZILXW = 4
LAIIDN = 45
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = 77
LIUXFE = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
LJUIKF = 82
LKXSJW = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = 51
LSXUJU = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
LXWAJV = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
MAOAWB = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
MCBFEG = 32
MHXEKV = 64
MJIGYO = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
MJMAOA = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
MJVHFT = 12
MOUNBL = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
NBLKXS = "".join(chr(c) for c in [67])
NEJNIB = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
NIBXYB = 73
NMHXEK = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
NPYYLI = "".join(
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
NQJYMO = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
NQLNMH = "".join(chr(c) for c in [65, 109, 80, 109])
NZMJIG = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
OAWBSI = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
OCTHBS = 42
OJRJHI = 54
OKPHUO = "".join(chr(c) for c in [76, 73])
ONPYYL = 59
OOQNRS = 81
OQNRSJ = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OUNBLK = 33
OUSPBW = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
OUYNQJ = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
PBWJYK = 68
PFTSIF = "".join(chr(c) for c in [67, 69])
PHUOJR = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [85, 76, 95, 67, 69])
POUYNQ = 30
PQIPOU = 29
PYYLIU = 60
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
QFYLJU = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QJYMOU = 63
QLAIID = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
QLNMHX = "".join(chr(c) for c in [50, 52, 104])
QNRSJM = "".join(chr(c) for c in [79, 119, 110])
QPLSPF = 26
QSNQLN = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = 22
RKINEJ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
RSJMCB = 0
RYXBQF = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
SAKQXP = 13
SIFJBI = 52
SIRYXB = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
SJMCBF = 2
SJWMNZ = 25
SKSOKP = 41
SNQLNM = 34
SOKPHU = 79
SOOQNR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
SPBWJY = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SPFTSI = "".join(chr(c) for c in [85, 76])
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SXUJUT = 57
TACCPQ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
TYEKCW = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
UIKFWR = 72
UJUTYE = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
UNBLKX = "".join(chr(c) for c in [70])
UOJRJH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UQEXLS = 27
USOOQN = 56
USPBWJ = 66
UXFEFJ = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
UYNQJY = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
VDQLAI = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
VLASSA = "".join(chr(c) for c in [])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 5
WAONPY = 58
WBSIRY = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
WJYKLG = 70
WMNZMJ = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
WRKINE = "".join(
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
XBQFYL = "".join(
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
XEKVKZ = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
XFEFJT = 78
XPICXQ = 15
XQGLRA = 37
XQIEFX = 18
XSJWMN = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
XUJUTY = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
YBQSNQ = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
YEKCWA = "".join(chr(c) for c in [76, 111])
YLIUXF = 61
YLJUIK = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
YMOUNB = 1
YOUSPB = 35
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = 10
YYLIUX = "".join(
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
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
ZMJIGY = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
ZUQEXL = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
AMJMAO = [OUYNQJ, IAMJMA]
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
BLKXSJ = [UNBLKX, NBLKXS]
CCPQIP = [TACCPQ, ACCPQI]
DNIBXT = [OKPHUO]
EFJTAC = [JVHFTH, FEFJTA, PIPIVL]
EJNIBX = [INEJNI, NEJNIB]
FTSIFJ = [SPFTSI, PFTSIF]
FYLJUI = [JVHFTH, QEXLSX, QFYLJU]
GZUQEX = [CBFEGZ, BFEGZU, FEGZUQ, EGZUQE]
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
IDNIBX = [BMJVHF, SSAKQX, AKQXPI, QXPICX, PICXQI, CXQIEF, CTHBSK, KSOKPH]
JIGYOU = [ZMJIGY, MJIGYO]
KCWAON = [YEKCWA, EKCWAO]
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
KVKZIL = [XEKVKZ, EKVKZI]
LNMHXE = [JVHFTH, NQLNMH, QLNMHX]
MNZMJI = [JWMNZM, WMNZMJ]
NIBXTI = []
NRSJMC = [OQNRSJ, QNRSJM]
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
QIPOUY = [PIPIVL, FEFJTA]
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
XLSXUJ = [QEXLSX, EXLSXU]
XWAJVD = [ILXWAJ, LXWAJV]
XYBQSN = [VLASSA, IBXYBQ, BXYBQS]
YKLGQP = [OUYNQJ, JYKLGQ]
YNQJYM = [OUYNQJ, UYNQJY]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return IBXTIA

    @property
    def output_keys(self):
        return IDNIBX

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
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, RSJMCB, NRSJMC, None, SJMCBF, QBMJVH
            ),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, MCBFEG, None, GZUQEX, None, None, QBMJVH
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, UQEXLS, None, XLSXUJ, None, None, QBMJVH
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, None, UTYEKC, None, None, QBMJVH
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, OOQNRS, SJMCBF, KCWAON, None, SJMCBF, QBMJVH
            ),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoByteStructAccessor(self.struct, NPYYLI, PYYLIU, QBMJVH),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, QBMJVH),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, None, EFJTAC, None, None, QBMJVH
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, CCPQIP, None, None, QBMJVH
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, PQIPOU, None, QIPOUY, None, None, QBMJVH
            ),
            IPOUYN: GeckoEnumStructAccessor(
                self.struct, IPOUYN, POUYNQ, None, YNQJYM, None, None, QBMJVH
            ),
            NQJYMO: GeckoByteStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoTempStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, BLKXSJ, None, None, QBMJVH
            ),
            LKXSJW: GeckoEnumStructAccessor(
                self.struct, LKXSJW, KXSJWM, None, QIPOUY, None, None, QBMJVH
            ),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, SJWMNZ, None, MNZMJI, None, None, QBMJVH
            ),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, OOQNRS, IGYOUS, JIGYOU, None, SJMCBF, QBMJVH
            ),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoTempStructAccessor(self.struct, OUSPBW, USPBWJ, QBMJVH),
            SPBWJY: GeckoTempStructAccessor(self.struct, SPBWJY, PBWJYK, QBMJVH),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, YKLGQP, None, None, QBMJVH
            ),
            KLGQPL: GeckoByteStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoByteStructAccessor(self.struct, GQPLSP, QPLSPF, QBMJVH),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, FTSIFJ, None, None, QBMJVH
            ),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoByteStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoEnumStructAccessor(
                self.struct, JBIAMJ, BIAMJM, None, AMJMAO, None, None, QBMJVH
            ),
            MJMAOA: GeckoByteStructAccessor(self.struct, MJMAOA, JMAOAW, QBMJVH),
            MAOAWB: GeckoTimeStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoTimeStructAccessor(self.struct, OAWBSI, AWBSIR, QBMJVH),
            WBSIRY: GeckoTimeStructAccessor(self.struct, WBSIRY, BSIRYX, QBMJVH),
            SIRYXB: GeckoTimeStructAccessor(self.struct, SIRYXB, IRYXBQ, QBMJVH),
            RYXBQF: GeckoTimeStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, FYLJUI, None, None, QBMJVH
            ),
            YLJUIK: GeckoBoolStructAccessor(
                self.struct, YLJUIK, LJUIKF, RSJMCB, QBMJVH
            ),
            JUIKFW: GeckoBoolStructAccessor(
                self.struct, JUIKFW, UIKFWR, SJMCBF, QBMJVH
            ),
            IKFWRK: GeckoBoolStructAccessor(
                self.struct, IKFWRK, UIKFWR, RSJMCB, QBMJVH
            ),
            KFWRKI: GeckoBoolStructAccessor(
                self.struct, KFWRKI, UIKFWR, FWRKIN, QBMJVH
            ),
            WRKINE: GeckoBoolStructAccessor(
                self.struct, WRKINE, UIKFWR, IGYOUS, QBMJVH
            ),
            RKINEJ: GeckoEnumStructAccessor(
                self.struct, RKINEJ, KINEJN, None, EJNIBX, None, None, QBMJVH
            ),
            JNIBXY: GeckoEnumStructAccessor(
                self.struct, JNIBXY, NIBXYB, None, XYBQSN, None, None, QBMJVH
            ),
            YBQSNQ: GeckoByteStructAccessor(self.struct, YBQSNQ, BQSNQL, QBMJVH),
            QSNQLN: GeckoEnumStructAccessor(
                self.struct, QSNQLN, SNQLNM, None, LNMHXE, None, None, QBMJVH
            ),
            NMHXEK: GeckoWordStructAccessor(self.struct, NMHXEK, MHXEKV, QBMJVH),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, OOQNRS, FWRKIN, KVKZIL, None, SJMCBF, QBMJVH
            ),
            VKZILX: GeckoBoolStructAccessor(
                self.struct, VKZILX, OOQNRS, KZILXW, QBMJVH
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, OOQNRS, WAJVDQ, XWAJVD, None, SJMCBF, QBMJVH
            ),
            AJVDQL: GeckoByteStructAccessor(self.struct, AJVDQL, JVDQLA, QBMJVH),
            VDQLAI: GeckoByteStructAccessor(self.struct, VDQLAI, DQLAII, QBMJVH),
            QLAIID: GeckoByteStructAccessor(self.struct, QLAIID, LAIIDN, QBMJVH),
            AIIDNI: GeckoByteStructAccessor(self.struct, AIIDNI, IIDNIB, QBMJVH),
        }

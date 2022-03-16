#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v54'
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
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
ACQFFT = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
AHEOCT = 39
AJVDQL = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
AOAWBS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
AONPYY = "".join(chr(c) for c in [80, 49])
AWBSIR = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
BFEGZU = 57
BIAMJM = "".join(chr(c) for c in [76, 105, 110, 101, 50])
BLKXSJ = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
BSIRYX = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
BSKSOK = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
BSSUHB = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
BVWVUB = 46
BWJYKL = 51
BXYBQS = "".join(
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
CBFEGZ = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
CCPQIP = 63
CPQIPO = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
CXQIEF = 36
DNIBXT = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
DQLAII = 34
DUBSSU = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 30
EFXQGL = 38
EGZUQE = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
EJNIBX = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
EKCWAO = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
EKVKZI = 76
EOCTHB = 79
EXLSXU = "".join(chr(c) for c in [72, 105])
FEFJTA = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
FEGZUQ = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
FFTTID = 5
FJBIAM = "".join(chr(c) for c in [70, 51])
FJTACC = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
FTTIDU = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
FWRKIN = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
GLRAHE = 15
GQPLSP = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
GZUQEX = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
HBSKSO = 80
HBVWVU = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
HUOJRJ = 81
HXEKVK = "".join(
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
IACQFF = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
IBXTIA = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
IBXYBQ = 10
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IDNIBX = 64
IDUBSS = 7
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
IFJBIA = "".join(chr(c) for c in [70, 50])
IGYOUS = "".join(chr(c) for c in [78, 105, 103, 104, 116])
IIDNIB = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
IKFWRK = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
ILXWAJ = 73
INEJNI = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 33
IRYXBQ = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
IUSOOQ = 32
IUXFEF = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(chr(c) for c in [76, 105, 110, 101, 49])
JHIUSO = 2
JIGYOU = 70
JMAOAW = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
JMCBFE = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
JNIBXY = 8
JTACCP = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
JUIKFW = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
JUTYEK = "".join(
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
JVDQLA = 75
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = 35
JYKLGQ = "".join(chr(c) for c in [67, 69])
JYMOUN = 25
KCWAON = 62
KFWRKI = 3
KINEJN = 6
KLGQPL = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
KPHUOJ = 56
KQXPIC = 14
KSOKPH = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
KVKZIL = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
LAIIDN = "".join(chr(c) for c in [50, 52, 104])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = 52
LJUIKF = 105
LKXSJW = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
LNMHXE = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
LSPFTS = 74
LSXUJU = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
LXWAJV = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
MAOAWB = 85
MHXEKV = 1
MJIGYO = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
MJMAOA = 84
MJVHFT = 12
MNZMJI = 66
MOUNBL = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
NBLKXS = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
NEJNIB = 23
NIBXTI = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
NIBXYB = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
NMHXEK = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
NPYYLI = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
NQJYMO = 31
NQLNMH = "".join(
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
NRSJMC = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
NZMJIG = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
OAWBSI = 86
OCTHBS = "".join(chr(c) for c in [76, 73])
OJRJHI = "".join(chr(c) for c in [79, 119, 110])
OKPHUO = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
OOQNRS = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
OQNRSJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
OUNBLK = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
OUSPBW = 77
OUYNQJ = "".join(chr(c) for c in [67])
PBWJYK = "".join(chr(c) for c in [85, 76, 95, 67, 69])
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
POUYNQ = "".join(chr(c) for c in [70])
PQIPOU = 1
PYYLIU = 28
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [76, 111])
QFYLJU = 104
QGLRAH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
QIEFXQ = 37
QIPOUY = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
QJYMOU = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
QLAIID = "".join(chr(c) for c in [65, 109, 80, 109])
QLNMHX = 72
QPLSPF = 53
QSNQLN = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
RAHEOC = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
RJHIUS = 0
RKINEJ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
RSJMCB = 27
RYXBQF = 99
SAKQXP = 13
SIFJBI = "".join(chr(c) for c in [70, 49])
SIRYXB = 98
SJMCBF = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
SJWMNZ = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
SKSOKP = 54
SNQLNM = 82
SOKPHU = 55
SOOQNR = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
SPBWJY = 26
SPFTSI = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SSUHBV = 44
SUHBVW = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
SXUJUT = 58
THBSKS = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 4
TIDUBS = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
TSIFJB = 83
TTIDUB = 6
TYEKCW = "".join(
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
UBSSUH = 43
UBYGDS = 54
UHBVWV = 45
UIKFWR = 106
UJUTYE = 59
UOJRJH = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
UQEXLS = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
USOOQN = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
USPBWJ = "".join(
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
UTYEKC = 60
UXFEFJ = 29
VDQLAI = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
VLASSA = "".join(chr(c) for c in [])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = 78
WBSIRY = 87
WJYKLG = "".join(chr(c) for c in [85, 76])
WMNZMJ = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
WRKINE = 4
XBQFYL = 100
XEKVKZ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
XPICXQ = 16
XQGLRA = 40
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
XSJWMN = 3
XTIACQ = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
XUJUTY = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
XWAJVD = "".join(chr(c) for c in [83, 108, 97, 118, 101])
XYBQSN = 71
YBQSNQ = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
YEKCWA = 61
YLIUXF = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
YLJUIK = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
YMOUNB = "".join(chr(c) for c in [105, 110, 70, 108, 111])
YNQJYM = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
YOUSPB = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
YYLIUX = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
ZMJIGY = 68
AIIDNI = [JVHFTH, QLAIID, LAIIDN]
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
BQSNQL = [JVHFTH, SJMCBF, YBQSNQ]
BXTIAC = [NIBXTI, IBXTIA]
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
FYLJUI = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, JBIAMJ, BIAMJM]
GYOUSP = [FJTACC, IGYOUS]
IAMJMA = [SIFJBI, IFJBIA, FJBIAM, VLASSA, VLASSA, VLASSA, JBIAMJ, BIAMJM]
JRJHIU = [UOJRJH, OJRJHI]
KXSJWM = [BLKXSJ, LKXSJW]
KZILXW = [KVKZIL, VKZILX]
LIUXFE = [YYLIUX, YLIUXF]
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
MCBFEG = [SJMCBF, JMCBFE]
ONPYYL = [JVHFTH, AONPYY, PIPIVL]
PFTSIF = [FJTACC, SPFTSI]
PICXQI = [
    JVHFTH,
    VHFTHE,
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
QFFTTI = [ACQFFT, CQFFTT]
QNRSJM = [USOOQN, SOOQNR, OOQNRS, OQNRSJ]
TACCPQ = [FJTACC, JTACCP]
UNBLKX = [YMOUNB, MOUNBL, OUNBLK]
UYNQJY = [POUYNQ, OUYNQJ]
VUBYGD = []
VWVUBY = [BMJVHF, SSAKQX, AKQXPI, QXPICX, QGLRAH, HEOCTH]
WAJVDQ = [VLASSA, LXWAJV, XWAJVD]
WVUBYG = [OCTHBS]
XFEFJT = [PIPIVL, AONPYY]
XLSXUJ = [QEXLSX, EXLSXU]
YKLGQP = [WJYKLG, JYKLGQ]
ZUQEXL = [FEGZUQ, EGZUQE, GZUQEX]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return UBYGDS

    @property
    def output_keys(self):
        return VWVUBY

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
                self.struct, HIUSOO, IUSOOQ, None, QNRSJM, None, None, QBMJVH
            ),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, RSJMCB, None, MCBFEG, None, None, QBMJVH
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, None, ZUQEXL, None, None, QBMJVH
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, HUOJRJ, JHIUSO, XLSXUJ, None, JHIUSO, QBMJVH
            ),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoByteStructAccessor(self.struct, XUJUTY, UJUTYE, QBMJVH),
            JUTYEK: GeckoByteStructAccessor(self.struct, JUTYEK, UTYEKC, QBMJVH),
            TYEKCW: GeckoByteStructAccessor(self.struct, TYEKCW, YEKCWA, QBMJVH),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoEnumStructAccessor(
                self.struct, CWAONP, WAONPY, None, ONPYYL, None, None, QBMJVH
            ),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, LIUXFE, None, None, QBMJVH
            ),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, UXFEFJ, None, XFEFJT, None, None, QBMJVH
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, EFJTAC, None, TACCPQ, None, None, QBMJVH
            ),
            ACCPQI: GeckoByteStructAccessor(self.struct, ACCPQI, CCPQIP, QBMJVH),
            CPQIPO: GeckoTempStructAccessor(self.struct, CPQIPO, PQIPOU, QBMJVH),
            QIPOUY: GeckoEnumStructAccessor(
                self.struct, QIPOUY, IPOUYN, None, UYNQJY, None, None, QBMJVH
            ),
            YNQJYM: GeckoEnumStructAccessor(
                self.struct, YNQJYM, NQJYMO, None, XFEFJT, None, None, QBMJVH
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, UNBLKX, None, None, QBMJVH
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, HUOJRJ, XSJWMN, KXSJWM, None, JHIUSO, QBMJVH
            ),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, QBMJVH),
            WMNZMJ: GeckoTempStructAccessor(self.struct, WMNZMJ, MNZMJI, QBMJVH),
            NZMJIG: GeckoTempStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoEnumStructAccessor(
                self.struct, MJIGYO, JIGYOU, None, GYOUSP, None, None, QBMJVH
            ),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoByteStructAccessor(self.struct, USPBWJ, SPBWJY, QBMJVH),
            PBWJYK: GeckoEnumStructAccessor(
                self.struct, PBWJYK, BWJYKL, None, YKLGQP, None, None, QBMJVH
            ),
            KLGQPL: GeckoByteStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoByteStructAccessor(self.struct, GQPLSP, QPLSPF, QBMJVH),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, PFTSIF, None, None, QBMJVH
            ),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, TSIFJB, None, IAMJMA, None, None, QBMJVH
            ),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, MJMAOA, None, IAMJMA, None, None, QBMJVH
            ),
            JMAOAW: GeckoEnumStructAccessor(
                self.struct, JMAOAW, MAOAWB, None, IAMJMA, None, None, QBMJVH
            ),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, None, IAMJMA, None, None, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, IAMJMA, None, None, QBMJVH
            ),
            BSIRYX: GeckoByteStructAccessor(self.struct, BSIRYX, SIRYXB, QBMJVH),
            IRYXBQ: GeckoByteStructAccessor(self.struct, IRYXBQ, RYXBQF, QBMJVH),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, FYLJUI, None, None, QBMJVH
            ),
            YLJUIK: GeckoEnumStructAccessor(
                self.struct, YLJUIK, LJUIKF, None, FYLJUI, None, None, QBMJVH
            ),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, UIKFWR, None, FYLJUI, None, None, QBMJVH
            ),
            IKFWRK: GeckoByteStructAccessor(self.struct, IKFWRK, KFWRKI, QBMJVH),
            FWRKIN: GeckoTimeStructAccessor(self.struct, FWRKIN, WRKINE, QBMJVH),
            RKINEJ: GeckoTimeStructAccessor(self.struct, RKINEJ, KINEJN, QBMJVH),
            INEJNI: GeckoTimeStructAccessor(self.struct, INEJNI, NEJNIB, QBMJVH),
            EJNIBX: GeckoTimeStructAccessor(self.struct, EJNIBX, JNIBXY, QBMJVH),
            NIBXYB: GeckoTimeStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, None, BQSNQL, None, None, QBMJVH
            ),
            QSNQLN: GeckoBoolStructAccessor(
                self.struct, QSNQLN, SNQLNM, RJHIUS, QBMJVH
            ),
            NQLNMH: GeckoBoolStructAccessor(
                self.struct, NQLNMH, QLNMHX, JHIUSO, QBMJVH
            ),
            LNMHXE: GeckoBoolStructAccessor(
                self.struct, LNMHXE, QLNMHX, RJHIUS, QBMJVH
            ),
            NMHXEK: GeckoBoolStructAccessor(
                self.struct, NMHXEK, QLNMHX, MHXEKV, QBMJVH
            ),
            HXEKVK: GeckoBoolStructAccessor(
                self.struct, HXEKVK, QLNMHX, XSJWMN, QBMJVH
            ),
            XEKVKZ: GeckoEnumStructAccessor(
                self.struct, XEKVKZ, EKVKZI, None, KZILXW, None, None, QBMJVH
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, ILXWAJ, None, WAJVDQ, None, None, QBMJVH
            ),
            AJVDQL: GeckoByteStructAccessor(self.struct, AJVDQL, JVDQLA, QBMJVH),
            VDQLAI: GeckoEnumStructAccessor(
                self.struct, VDQLAI, DQLAII, None, AIIDNI, None, None, QBMJVH
            ),
            IIDNIB: GeckoWordStructAccessor(self.struct, IIDNIB, IDNIBX, QBMJVH),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, HUOJRJ, MHXEKV, BXTIAC, None, JHIUSO, QBMJVH
            ),
            XTIACQ: GeckoBoolStructAccessor(
                self.struct, XTIACQ, HUOJRJ, TIACQF, QBMJVH
            ),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, HUOJRJ, FFTTID, QFFTTI, None, JHIUSO, QBMJVH
            ),
            FTTIDU: GeckoBoolStructAccessor(
                self.struct, FTTIDU, HUOJRJ, TTIDUB, QBMJVH
            ),
            TIDUBS: GeckoBoolStructAccessor(
                self.struct, TIDUBS, HUOJRJ, IDUBSS, QBMJVH
            ),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, QBMJVH),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, QBMJVH),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, QBMJVH),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, QBMJVH),
        }

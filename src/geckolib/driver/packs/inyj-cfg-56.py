#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v56'
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
ACQFFT = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
AHEOCT = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
AIIDNI = "".join(chr(c) for c in [50, 52, 104])
AKQXPI = 13
AOAWBS = 85
AONPYY = 78
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 116, 101, 99, 116, 105, 111, 110])
AWBSIR = 86
BFEGZU = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
BIAMJM = "".join(chr(c) for c in [76, 105, 110, 101, 49])
BLKXSJ = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 100
BQSNQL = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
BSIRYX = 87
BSKSOK = 80
BSSUHB = 43
BVWVUB = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
BWJYKL = "".join(chr(c) for c in [85, 76, 95, 67, 69])
BXTIAC = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
BXYBQS = 10
BYGDSB = 56
CCPQIP = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
CPQIPO = 63
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
CTHBSK = "".join(chr(c) for c in [76, 73])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 62
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
DNIBXT = 64
DQLAII = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
DUBSSU = 7
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
EGZUQE = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
EJNIBX = 23
EKCWAO = 61
EKVKZI = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 76, 105])
EXLSXU = "".join(chr(c) for c in [76, 111])
FEGZUQ = 57
FJBIAM = "".join(chr(c) for c in [70, 50])
FJTACC = 30
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTTIDU = 5
FWRKIN = 3
FXQGLR = 38
FYLJUI = 104
GLRAHE = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
GQPLSP = 52
GYOUSP = "".join(chr(c) for c in [78, 105, 103, 104, 116])
GZUQEX = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
HBSKSO = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
HBVWVU = 45
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 39
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 2
HUOJRJ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
HXEKVK = 1
IACQFF = 4
IAMJMA = "".join(chr(c) for c in [76, 105, 110, 101, 50])
IBXTIA = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
IBXYBQ = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
IDNIBX = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
IDUBSS = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
IEFXQG = 37
IFJBIA = "".join(chr(c) for c in [70, 49])
IGYOUS = 70
IKFWRK = 106
ILXWAJ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
INEJNI = 6
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
IRYXBQ = 98
IUSOOQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(chr(c) for c in [70, 51])
JHIUSO = 0
JIGYOU = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
JMAOAW = 84
JMCBFE = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
JNIBXY = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
JRJHIU = "".join(chr(c) for c in [79, 119, 110])
JTACCP = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
JUIKFW = 105
JUTYEK = 59
JVDQLA = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
JYKLGQ = "".join(chr(c) for c in [85, 76])
JYMOUN = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
KCWAON = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
KFWRKI = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
KINEJN = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
KPHUOJ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 51])
KSOKPH = 54
KVKZIL = 76
KXSJWM = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
KZILXW = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
LAIIDN = "".join(chr(c) for c in [65, 109, 80, 109])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
LIUXFE = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
LJUIKF = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
LKXSJW = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
LNMHXE = 72
LRAHEO = 15
LSPFTS = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
LXWAJV = 73
MAOAWB = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
MCBFEG = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
MHXEKV = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
MJIGYO = 68
MJMAOA = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
MJVHFT = 12
MNZMJI = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
MOUNBL = "".join(chr(c) for c in [105, 110, 70, 108, 111])
NEJNIB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
NIBXTI = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
NIBXYB = 8
NMHXEK = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
NQJYMO = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
NQLNMH = 82
NZMJIG = 66
OAWBSI = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
OCTHBS = 79
OJRJHI = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OKPHUO = 55
ONPYYL = "".join(chr(c) for c in [80, 49])
OOQNRS = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
OQNRSJ = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
OUNBLK = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
OUSPBW = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
OUYNQJ = "".join(chr(c) for c in [70])
PBWJYK = 26
PFTSIF = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
PHUOJR = 56
PICXQI = 16
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 53
POUYNQ = 33
PQIPOU = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
PYYLIU = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
QFFTTI = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
QFYLJU = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
QGLRAH = 40
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
QIPOUY = 1
QJYMOU = 31
QLAIID = 34
QLNMHX = "".join(
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
QNRSJM = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
QPLSPF = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
QXPICX = 14
RKINEJ = 4
RSJMCB = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
RYXBQF = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 50])
SIFJBI = 83
SIRYXB = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
SJMCBF = 27
SJWMNZ = 3
SKSOKP = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
SNQLNM = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
SOKPHU = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
SOOQNR = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
SPBWJY = "".join(
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
SPFTSI = 74
SSUHBV = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
SUHBVW = 44
SXUJUT = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
TACCPQ = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
TIDUBS = 6
TSIFJB = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
TTIDUB = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
TYEKCW = 60
UBSSUH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
UHBVWV = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
UIKFWR = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
UJUTYE = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
UNBLKX = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
UOJRJH = 81
USOOQN = 32
USPBWJ = 77
UTYEKC = "".join(
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
UXFEFJ = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
UYNQJY = "".join(chr(c) for c in [67])
VDQLAI = 75
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
VLASSA = "".join(chr(c) for c in [])
VWVUBY = 46
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [83, 108, 97, 118, 101])
WAONPY = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
WBSIRY = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
WJYKLG = 51
WMNZMJ = 35
WRKINE = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
XBQFYL = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
XEKVKZ = "".join(
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
XFEFJT = 29
XLSXUJ = "".join(chr(c) for c in [72, 105])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
XQIEFX = 36
XUJUTY = 58
XWAJVD = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
XYBQSN = "".join(
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
YBQSNQ = 71
YEKCWA = "".join(
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
YKLGQP = "".join(chr(c) for c in [67, 69])
YLIUXF = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
YMOUNB = 25
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = 99
YYLIUX = 28
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
ZUQEXL = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
ACCPQI = [JTACCP, TACCPQ]
AJVDQL = [VLASSA, XWAJVD, WAJVDQ]
AMJMAO = [IFJBIA, FJBIAM, JBIAMJ, VLASSA, VLASSA, VLASSA, BIAMJM, IAMJMA]
CBFEGZ = [JMCBFE, MCBFEG]
FEFJTA = [PIPIVL, ONPYYL]
FFTTID = [CQFFTT, QFFTTI]
FTSIFJ = [JTACCP, PFTSIF]
ICXQIE = [
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
IIDNIB = [JVHFTH, LAIIDN, AIIDNI]
IUXFEF = [YLIUXF, LIUXFE]
KLGQPL = [JYKLGQ, YKLGQP]
LSXUJU = [EXLSXU, XLSXUJ]
NBLKXS = [MOUNBL, OUNBLK, UNBLKX]
NPYYLI = [JVHFTH, ONPYYL, PIPIVL]
NRSJMC = [SOOQNR, OOQNRS, OQNRSJ, QNRSJM]
QSNQLN = [JVHFTH, JMCBFE, BQSNQL]
RAHEOC = [
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
RJHIUS = [OJRJHI, JRJHIU]
SSAKQX = [
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
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    ASSAKQ,
]
THBSKS = [
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
    CTHBSK,
]
UBYGDS = []
UQEXLS = [EGZUQE, GZUQEX, ZUQEXL]
VUBYGD = [CTHBSK]
WVUBYG = [BMJVHF, SAKQXP, KQXPIC, XPICXQ, GLRAHE, EOCTHB]
XSJWMN = [LKXSJW, KXSJWM]
XTIACQ = [IBXTIA, BXTIAC]
YLJUIK = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, BIAMJM, IAMJMA]
YNQJYM = [OUYNQJ, UYNQJY]
YOUSPB = [JTACCP, GYOUSP]
ZILXWA = [VKZILX, KZILXW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return BYGDSB

    @property
    def output_keys(self):
        return WVUBYG

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, SSAKQX, None, None, QBMJVH
            ),
            SAKQXP: GeckoEnumStructAccessor(
                self.struct, SAKQXP, AKQXPI, None, SSAKQX, None, None, QBMJVH
            ),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, SSAKQX, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, ICXQIE, None, None, QBMJVH
            ),
            CXQIEF: GeckoByteStructAccessor(self.struct, CXQIEF, XQIEFX, QBMJVH),
            QIEFXQ: GeckoByteStructAccessor(self.struct, QIEFXQ, IEFXQG, QBMJVH),
            EFXQGL: GeckoByteStructAccessor(self.struct, EFXQGL, FXQGLR, QBMJVH),
            XQGLRA: GeckoByteStructAccessor(self.struct, XQGLRA, QGLRAH, QBMJVH),
            GLRAHE: GeckoEnumStructAccessor(
                self.struct, GLRAHE, LRAHEO, None, RAHEOC, None, None, QBMJVH
            ),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoEnumStructAccessor(
                self.struct, EOCTHB, OCTHBS, None, THBSKS, None, None, None
            ),
            HBSKSO: GeckoByteStructAccessor(self.struct, HBSKSO, BSKSOK, None),
            SKSOKP: GeckoByteStructAccessor(self.struct, SKSOKP, KSOKPH, QBMJVH),
            SOKPHU: GeckoByteStructAccessor(self.struct, SOKPHU, OKPHUO, QBMJVH),
            KPHUOJ: GeckoByteStructAccessor(self.struct, KPHUOJ, PHUOJR, QBMJVH),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, JHIUSO, RJHIUS, None, HIUSOO, QBMJVH
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, None, NRSJMC, None, None, QBMJVH
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, SJMCBF, None, CBFEGZ, None, None, QBMJVH
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, FEGZUQ, None, UQEXLS, None, None, QBMJVH
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, UOJRJH, HIUSOO, LSXUJU, None, HIUSOO, QBMJVH
            ),
            SXUJUT: GeckoByteStructAccessor(self.struct, SXUJUT, XUJUTY, QBMJVH),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, QBMJVH),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, NPYYLI, None, None, QBMJVH
            ),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, YYLIUX, None, IUXFEF, None, None, QBMJVH
            ),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, None, FEFJTA, None, None, QBMJVH
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, None, ACCPQI, None, None, QBMJVH
            ),
            CCPQIP: GeckoByteStructAccessor(self.struct, CCPQIP, CPQIPO, QBMJVH),
            PQIPOU: GeckoTempStructAccessor(self.struct, PQIPOU, QIPOUY, QBMJVH),
            IPOUYN: GeckoEnumStructAccessor(
                self.struct, IPOUYN, POUYNQ, None, YNQJYM, None, None, QBMJVH
            ),
            NQJYMO: GeckoEnumStructAccessor(
                self.struct, NQJYMO, QJYMOU, None, FEFJTA, None, None, QBMJVH
            ),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, YMOUNB, None, NBLKXS, None, None, QBMJVH
            ),
            BLKXSJ: GeckoEnumStructAccessor(
                self.struct, BLKXSJ, UOJRJH, SJWMNZ, XSJWMN, None, HIUSOO, QBMJVH
            ),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoTempStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoTempStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoEnumStructAccessor(
                self.struct, JIGYOU, IGYOUS, None, YOUSPB, None, None, QBMJVH
            ),
            OUSPBW: GeckoByteStructAccessor(self.struct, OUSPBW, USPBWJ, QBMJVH),
            SPBWJY: GeckoByteStructAccessor(self.struct, SPBWJY, PBWJYK, QBMJVH),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, KLGQPL, None, None, QBMJVH
            ),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoByteStructAccessor(self.struct, QPLSPF, PLSPFT, QBMJVH),
            LSPFTS: GeckoEnumStructAccessor(
                self.struct, LSPFTS, SPFTSI, None, FTSIFJ, None, None, QBMJVH
            ),
            TSIFJB: GeckoEnumStructAccessor(
                self.struct, TSIFJB, SIFJBI, None, AMJMAO, None, None, QBMJVH
            ),
            MJMAOA: GeckoEnumStructAccessor(
                self.struct, MJMAOA, JMAOAW, None, AMJMAO, None, None, QBMJVH
            ),
            MAOAWB: GeckoEnumStructAccessor(
                self.struct, MAOAWB, AOAWBS, None, AMJMAO, None, None, QBMJVH
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, AMJMAO, None, None, QBMJVH
            ),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, BSIRYX, None, AMJMAO, None, None, QBMJVH
            ),
            SIRYXB: GeckoByteStructAccessor(self.struct, SIRYXB, IRYXBQ, QBMJVH),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoByteStructAccessor(self.struct, XBQFYL, BQFYLJ, QBMJVH),
            QFYLJU: GeckoEnumStructAccessor(
                self.struct, QFYLJU, FYLJUI, None, YLJUIK, None, None, QBMJVH
            ),
            LJUIKF: GeckoEnumStructAccessor(
                self.struct, LJUIKF, JUIKFW, None, YLJUIK, None, None, QBMJVH
            ),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, IKFWRK, None, YLJUIK, None, None, QBMJVH
            ),
            KFWRKI: GeckoByteStructAccessor(self.struct, KFWRKI, FWRKIN, QBMJVH),
            WRKINE: GeckoTimeStructAccessor(self.struct, WRKINE, RKINEJ, QBMJVH),
            KINEJN: GeckoTimeStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoTimeStructAccessor(self.struct, NEJNIB, EJNIBX, QBMJVH),
            JNIBXY: GeckoTimeStructAccessor(self.struct, JNIBXY, NIBXYB, QBMJVH),
            IBXYBQ: GeckoTimeStructAccessor(self.struct, IBXYBQ, BXYBQS, QBMJVH),
            XYBQSN: GeckoEnumStructAccessor(
                self.struct, XYBQSN, YBQSNQ, None, QSNQLN, None, None, QBMJVH
            ),
            SNQLNM: GeckoBoolStructAccessor(
                self.struct, SNQLNM, NQLNMH, JHIUSO, QBMJVH
            ),
            QLNMHX: GeckoBoolStructAccessor(
                self.struct, QLNMHX, LNMHXE, HIUSOO, QBMJVH
            ),
            NMHXEK: GeckoBoolStructAccessor(
                self.struct, NMHXEK, LNMHXE, JHIUSO, QBMJVH
            ),
            MHXEKV: GeckoBoolStructAccessor(
                self.struct, MHXEKV, LNMHXE, HXEKVK, QBMJVH
            ),
            XEKVKZ: GeckoBoolStructAccessor(
                self.struct, XEKVKZ, LNMHXE, SJWMNZ, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, ZILXWA, None, None, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, LXWAJV, None, AJVDQL, None, None, QBMJVH
            ),
            JVDQLA: GeckoByteStructAccessor(self.struct, JVDQLA, VDQLAI, QBMJVH),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, QLAIID, None, IIDNIB, None, None, QBMJVH
            ),
            IDNIBX: GeckoWordStructAccessor(self.struct, IDNIBX, DNIBXT, QBMJVH),
            NIBXTI: GeckoEnumStructAccessor(
                self.struct, NIBXTI, UOJRJH, HXEKVK, XTIACQ, None, HIUSOO, QBMJVH
            ),
            TIACQF: GeckoBoolStructAccessor(
                self.struct, TIACQF, UOJRJH, IACQFF, QBMJVH
            ),
            ACQFFT: GeckoEnumStructAccessor(
                self.struct, ACQFFT, UOJRJH, FTTIDU, FFTTID, None, HIUSOO, QBMJVH
            ),
            TTIDUB: GeckoBoolStructAccessor(
                self.struct, TTIDUB, UOJRJH, TIDUBS, QBMJVH
            ),
            IDUBSS: GeckoBoolStructAccessor(
                self.struct, IDUBSS, UOJRJH, DUBSSU, QBMJVH
            ),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, QBMJVH),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, QBMJVH),
        }

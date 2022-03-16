#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v55'
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
ACCPQI = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
ACQFFT = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
AHEOCT = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
AIIDNI = 34
AJVDQL = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
AKQXPI = 13
AMJMAO = "".join(chr(c) for c in [76, 105, 110, 101, 49])
AOAWBS = 84
AONPYY = 62
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 116, 101, 99, 116, 105, 111, 110])
AWBSIR = 85
BFEGZU = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
BIAMJM = "".join(chr(c) for c in [70, 50])
BLKXSJ = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 99
BQSNQL = "".join(
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
BSIRYX = 86
BSKSOK = 80
BSSUHB = 7
BVWVUB = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
BWJYKL = "".join(
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
BXTIAC = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
BXYBQS = 8
CBFEGZ = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
CCPQIP = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
CQBMJV = 0
CQFFTT = 4
CTHBSK = "".join(chr(c) for c in [76, 73])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 61
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
DQLAII = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
DUBSSU = 6
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 29
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
EGZUQE = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
EJNIBX = 6
EKCWAO = 60
EKVKZI = 1
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 76, 105])
FEFJTA = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
FFTTID = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
FJBIAM = 83
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 74
FTTIDU = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
FWRKIN = 106
FXQGLR = 38
FYLJUI = 100
GDSBDJ = 55
GLRAHE = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
GYOUSP = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
GZUQEX = 57
HBSKSO = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
HBVWVU = 44
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 39
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
HXEKVK = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
IAMJMA = "".join(chr(c) for c in [70, 51])
IBXTIA = 64
IBXYBQ = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
IDNIBX = "".join(chr(c) for c in [50, 52, 104])
IDUBSS = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
IEFXQG = 37
IFJBIA = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
IGYOUS = 68
IIDNIB = "".join(chr(c) for c in [65, 109, 80, 109])
IKFWRK = 105
ILXWAJ = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
INEJNI = 4
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
IRYXBQ = 87
IUSOOQ = 0
IUXFEF = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(chr(c) for c in [70, 49])
JHIUSO = "".join(chr(c) for c in [79, 119, 110])
JIGYOU = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
JMCBFE = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
JNIBXY = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
JRJHIU = 81
JTACCP = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
JUTYEK = 58
JVDQLA = "".join(chr(c) for c in [83, 108, 97, 118, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JYKLGQ = "".join(chr(c) for c in [85, 76, 95, 67, 69])
JYMOUN = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
KCWAON = "".join(
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
KFWRKI = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
KINEJN = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
KLGQPL = "".join(chr(c) for c in [85, 76])
KPHUOJ = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 51])
KSOKPH = 54
KVKZIL = "".join(
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
KXSJWM = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
KZILXW = 76
LAIIDN = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(chr(c) for c in [67, 69])
LIUXFE = 28
LJUIKF = 104
LNMHXE = 82
LRAHEO = 15
LSPFTS = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
LSXUJU = "".join(chr(c) for c in [76, 111])
MAOAWB = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
MCBFEG = 27
MHXEKV = 72
MJIGYO = 66
MJMAOA = "".join(chr(c) for c in [76, 105, 110, 101, 50])
MJVHFT = 12
MNZMJI = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
MOUNBL = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
NBLKXS = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
NEJNIB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
NIBXTI = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
NIBXYB = 23
NMHXEK = "".join(
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
NPYYLI = 78
NQJYMO = "".join(chr(c) for c in [67])
NRSJMC = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
NZMJIG = 35
OAWBSI = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
OCTHBS = 79
OJRJHI = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
OKPHUO = 22
ONPYYL = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
OOQNRS = 32
OQNRSJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
OUNBLK = 25
OUSPBW = "".join(chr(c) for c in [78, 105, 103, 104, 116])
OUYNQJ = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
PBWJYK = 77
PFTSIF = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
PHUOJR = 55
PICXQI = 16
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 52
POUYNQ = 1
PQIPOU = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
PYYLIU = "".join(chr(c) for c in [80, 49])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
QFFTTI = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
QFYLJU = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
QGLRAH = 40
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
QIPOUY = 63
QLAIID = 75
QLNMHX = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
QNRSJM = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
QPLSPF = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
QSNQLN = 71
QXPICX = 14
RJHIUS = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
RKINEJ = 3
RSJMCB = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
RYXBQF = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 50])
SIRYXB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
SJWMNZ = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
SKSOKP = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
SNQLNM = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
SOKPHU = "".join(chr(c) for c in [80, 49, 76, 84, 105, 109, 101, 79, 117, 116])
SOOQNR = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
SPBWJY = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
SPFTSI = 53
SSUHBV = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
SUHBVW = 43
SXUJUT = "".join(chr(c) for c in [72, 105])
TACCPQ = 30
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
TIDUBS = 5
TSIFJB = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
TYEKCW = 59
UBSSUH = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
UHBVWV = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
UIKFWR = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
UJUTYE = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
UNBLKX = "".join(chr(c) for c in [105, 110, 70, 108, 111])
UOJRJH = 56
UQEXLS = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
USOOQN = 2
UTYEKC = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
UXFEFJ = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
UYNQJY = 33
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
VLASSA = "".join(chr(c) for c in [])
VUBYGD = 46
VWVUBY = 45
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 73
WAONPY = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
WBSIRY = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
WJYKLG = 26
WMNZMJ = 3
WRKINE = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
WVUBYG = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
XBQFYL = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
XEKVKZ = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
XLSXUJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
XQIEFX = 36
XSJWMN = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
XTIACQ = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
XWAJVD = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
XYBQSN = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
YBQSNQ = 10
YEKCWA = "".join(
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
YKLGQP = 51
YLIUXF = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
YLJUIK = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
YMOUNB = 31
YNQJYM = "".join(chr(c) for c in [70])
YOUSPB = 70
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = 98
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
ZMJIGY = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
ZUQEXL = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
BYGDSB = [CTHBSK]
CPQIPO = [ACCPQI, CCPQIP]
DNIBXT = [JVHFTH, IIDNIB, IDNIBX]
EXLSXU = [ZUQEXL, UQEXLS, QEXLSX]
FEGZUQ = [CBFEGZ, BFEGZU]
FJTACC = [PIPIVL, PYYLIU]
GQPLSP = [KLGQPL, LGQPLS]
HIUSOO = [RJHIUS, JHIUSO]
IACQFF = [XTIACQ, TIACQF]
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
JMAOAW = [JBIAMJ, BIAMJM, IAMJMA, VLASSA, VLASSA, VLASSA, AMJMAO, MJMAOA]
JUIKFW = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, AMJMAO, MJMAOA]
JWMNZM = [XSJWMN, SJWMNZ]
LKXSJW = [UNBLKX, NBLKXS, BLKXSJ]
LXWAJV = [ZILXWA, ILXWAJ]
NQLNMH = [JVHFTH, CBFEGZ, SNQLNM]
QJYMOU = [YNQJYM, NQJYMO]
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
SIFJBI = [ACCPQI, TSIFJB]
SJMCBF = [OQNRSJ, QNRSJM, NRSJMC, RSJMCB]
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
TTIDUB = [FFTTID, FTTIDU]
UBYGDS = [BMJVHF, SAKQXP, KQXPIC, XPICXQ, GLRAHE, EOCTHB]
USPBWJ = [ACCPQI, OUSPBW]
VDQLAI = [VLASSA, AJVDQL, JVDQLA]
XFEFJT = [IUXFEF, UXFEFJ]
XUJUTY = [LSXUJU, SXUJUT]
YGDSBD = []
YYLIUX = [JVHFTH, PYYLIU, PIPIVL]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return GDSBDJ

    @property
    def output_keys(self):
        return UBYGDS

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
            HUOJRJ: GeckoByteStructAccessor(self.struct, HUOJRJ, UOJRJH, QBMJVH),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, IUSOOQ, HIUSOO, None, USOOQN, QBMJVH
            ),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, None, SJMCBF, None, None, QBMJVH
            ),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, MCBFEG, None, FEGZUQ, None, None, QBMJVH
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, GZUQEX, None, EXLSXU, None, None, QBMJVH
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, JRJHIU, USOOQN, XUJUTY, None, USOOQN, QBMJVH
            ),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, QBMJVH),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, QBMJVH),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, NPYYLI, None, YYLIUX, None, None, QBMJVH
            ),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, XFEFJT, None, None, QBMJVH
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, EFJTAC, None, FJTACC, None, None, QBMJVH
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoByteStructAccessor(self.struct, PQIPOU, QIPOUY, QBMJVH),
            IPOUYN: GeckoTempStructAccessor(self.struct, IPOUYN, POUYNQ, QBMJVH),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, UYNQJY, None, QJYMOU, None, None, QBMJVH
            ),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, YMOUNB, None, FJTACC, None, None, QBMJVH
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, LKXSJW, None, None, QBMJVH
            ),
            KXSJWM: GeckoEnumStructAccessor(
                self.struct, KXSJWM, JRJHIU, WMNZMJ, JWMNZM, None, USOOQN, QBMJVH
            ),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoTempStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoTempStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoEnumStructAccessor(
                self.struct, GYOUSP, YOUSPB, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoByteStructAccessor(self.struct, SPBWJY, PBWJYK, QBMJVH),
            BWJYKL: GeckoByteStructAccessor(self.struct, BWJYKL, WJYKLG, QBMJVH),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, YKLGQP, None, GQPLSP, None, None, QBMJVH
            ),
            QPLSPF: GeckoByteStructAccessor(self.struct, QPLSPF, PLSPFT, QBMJVH),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, QBMJVH),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, SIFJBI, None, None, QBMJVH
            ),
            IFJBIA: GeckoEnumStructAccessor(
                self.struct, IFJBIA, FJBIAM, None, JMAOAW, None, None, QBMJVH
            ),
            MAOAWB: GeckoEnumStructAccessor(
                self.struct, MAOAWB, AOAWBS, None, JMAOAW, None, None, QBMJVH
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, JMAOAW, None, None, QBMJVH
            ),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, BSIRYX, None, JMAOAW, None, None, QBMJVH
            ),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, IRYXBQ, None, JMAOAW, None, None, QBMJVH
            ),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoByteStructAccessor(self.struct, XBQFYL, BQFYLJ, QBMJVH),
            QFYLJU: GeckoByteStructAccessor(self.struct, QFYLJU, FYLJUI, QBMJVH),
            YLJUIK: GeckoEnumStructAccessor(
                self.struct, YLJUIK, LJUIKF, None, JUIKFW, None, None, QBMJVH
            ),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, IKFWRK, None, JUIKFW, None, None, QBMJVH
            ),
            KFWRKI: GeckoEnumStructAccessor(
                self.struct, KFWRKI, FWRKIN, None, JUIKFW, None, None, QBMJVH
            ),
            WRKINE: GeckoByteStructAccessor(self.struct, WRKINE, RKINEJ, QBMJVH),
            KINEJN: GeckoTimeStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoTimeStructAccessor(self.struct, NEJNIB, EJNIBX, QBMJVH),
            JNIBXY: GeckoTimeStructAccessor(self.struct, JNIBXY, NIBXYB, QBMJVH),
            IBXYBQ: GeckoTimeStructAccessor(self.struct, IBXYBQ, BXYBQS, QBMJVH),
            XYBQSN: GeckoTimeStructAccessor(self.struct, XYBQSN, YBQSNQ, QBMJVH),
            BQSNQL: GeckoEnumStructAccessor(
                self.struct, BQSNQL, QSNQLN, None, NQLNMH, None, None, QBMJVH
            ),
            QLNMHX: GeckoBoolStructAccessor(
                self.struct, QLNMHX, LNMHXE, IUSOOQ, QBMJVH
            ),
            NMHXEK: GeckoBoolStructAccessor(
                self.struct, NMHXEK, MHXEKV, USOOQN, QBMJVH
            ),
            HXEKVK: GeckoBoolStructAccessor(
                self.struct, HXEKVK, MHXEKV, IUSOOQ, QBMJVH
            ),
            XEKVKZ: GeckoBoolStructAccessor(
                self.struct, XEKVKZ, MHXEKV, EKVKZI, QBMJVH
            ),
            KVKZIL: GeckoBoolStructAccessor(
                self.struct, KVKZIL, MHXEKV, WMNZMJ, QBMJVH
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, KZILXW, None, LXWAJV, None, None, QBMJVH
            ),
            XWAJVD: GeckoEnumStructAccessor(
                self.struct, XWAJVD, WAJVDQ, None, VDQLAI, None, None, QBMJVH
            ),
            DQLAII: GeckoByteStructAccessor(self.struct, DQLAII, QLAIID, QBMJVH),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AIIDNI, None, DNIBXT, None, None, QBMJVH
            ),
            NIBXTI: GeckoWordStructAccessor(self.struct, NIBXTI, IBXTIA, QBMJVH),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, JRJHIU, EKVKZI, IACQFF, None, USOOQN, QBMJVH
            ),
            ACQFFT: GeckoBoolStructAccessor(
                self.struct, ACQFFT, JRJHIU, CQFFTT, QBMJVH
            ),
            QFFTTI: GeckoEnumStructAccessor(
                self.struct, QFFTTI, JRJHIU, TIDUBS, TTIDUB, None, USOOQN, QBMJVH
            ),
            IDUBSS: GeckoBoolStructAccessor(
                self.struct, IDUBSS, JRJHIU, DUBSSU, QBMJVH
            ),
            UBSSUH: GeckoBoolStructAccessor(
                self.struct, UBSSUH, JRJHIU, BSSUHB, QBMJVH
            ),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, QBMJVH),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, QBMJVH),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, QBMJVH),
        }

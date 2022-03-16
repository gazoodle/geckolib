#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v4'
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
ACCPQI = 5
ACQFFT = "".join(chr(c) for c in [78, 111, 110, 101])
AHEOCT = "".join(
    chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114, 114, 101, 110, 116]
)
AIIDNI = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        99,
        116,
        105,
        118,
        101,
        68,
        101,
        108,
        97,
        121,
        65,
        102,
        116,
        101,
        114,
        80,
        117,
        109,
        112,
        82,
        117,
        110,
    ]
)
AJVDQL = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        99,
        116,
        105,
        118,
        101,
        79,
        110,
        65,
        109,
        98,
        105,
        97,
        110,
        116,
        79,
        84,
    ]
)
AKQXPI = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
AMJMAO = 15
AOAWBS = 85
AONPYY = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 49])
ASSAKQ = "".join(chr(c) for c in [70, 98, 77, 116, 114])
AWBSIR = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
BDJQRJ = 28
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
BJEUTO = "".join(chr(c) for c in [65, 99, 116, 105, 118, 101])
BLKXSJ = 48
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
BQNRXC = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
BQSNQL = 93
BSIRYX = 3
BSKSOK = 111
BSSUHB = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 48]
)
BVWVUB = 10
BWJYKL = "".join(
    chr(c) for c in [79, 51, 68, 117, 114, 105, 110, 103, 70, 105, 108, 116]
)
BXTIAC = 21
BXYBQS = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
BYGDSB = "".join(
    chr(c)
    for c in [78, 101, 120, 116, 70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121]
)
CBFEGZ = 106
CCPQIP = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
CPQIPO = "".join(chr(c) for c in [65, 110, 121, 85, 68])
CQBMJV = 0
CRTFMN = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
CTHBSK = "".join(
    chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114, 114, 101, 110, 116]
)
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 27
CXQIEF = 96
DJQRJJ = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
DNIBXT = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        83,
        101,
        116,
        70,
        111,
        114,
        99,
        101,
        79,
        102,
        102,
        84,
        101,
        109,
        112,
        65,
        100,
        99,
    ]
)
DNQGVU = 74
DQLAII = "".join(
    chr(c)
    for c in [70, 97, 110, 67, 108, 114, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
DSBDJQ = "".join(chr(c) for c in [75, 54, 48, 48, 70, 111, 114, 77, 97, 121])
DUBSSU = "".join(
    chr(c) for c in [86, 83, 80, 70, 105, 108, 116, 101, 114, 83, 112, 101, 101, 100]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
EFXQGL = 98
EGZUQE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
EJNIBX = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
EKCWAO = 63
EKVKZI = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
ELHBQN = 83
EOCTHB = "".join(
    chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114, 114, 101, 110, 116]
)
EUTOPH = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49])
EXLSXU = 3
FCRTFM = 41
FEFJTA = 25
FEGZUQ = 107
FFTTID = "".join(chr(c) for c in [80, 117, 109, 112, 49, 65, 115, 86, 83, 80])
FJBIAM = "".join(chr(c) for c in [67])
FJTACC = 26
FMNHTB = 67
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [83, 97, 110, 105, 79, 110, 84, 105, 109, 101])
FTTIDU = 5
FWRKIN = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 51, 65])
FYLJUI = "".join(chr(c) for c in [53, 48, 72, 90])
GDSBDJ = "".join(
    chr(c)
    for c in [
        81,
        117,
        105,
        99,
        107,
        79,
        110,
        79,
        102,
        102,
        75,
        101,
        121,
        69,
        110,
        97,
        98,
        108,
        101,
    ]
)
GLRAHE = 104
GQPLSP = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
GSELHB = 82
GTYIYW = "".join(
    chr(c) for c in [82, 101, 112, 108, 97, 99, 101, 70, 105, 108, 116, 101, 114]
)
GVUNXN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56])
GYOUSP = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
GZUQEX = 86
HBQNRX = 84
HBSKSO = "".join(
    chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114, 114, 101, 110, 116]
)
HBVWVU = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 50]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 108
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(
    chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114, 114, 101, 110, 116]
)
HTBJEU = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
HUGTYI = "".join(chr(c) for c in [67, 104, 97, 110, 103, 101, 87, 97, 116, 101, 114])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 54, 65])
HXEKVK = "".join(
    chr(c)
    for c in [
        69,
        120,
        105,
        116,
        81,
        117,
        105,
        101,
        116,
        65,
        110,
        100,
        67,
        97,
        110,
        99,
        101,
        108,
        79,
        116,
        104,
        101,
        114,
        85,
        68,
    ]
)
IACQFF = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
IAMJMA = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
IBXTIA = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        67,
        108,
        114,
        70,
        111,
        114,
        99,
        101,
        79,
        102,
        102,
        84,
        101,
        109,
        112,
        65,
        100,
        99,
    ]
)
IBXYBQ = 91
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 49, 66])
IDNIBX = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        70,
        111,
        114,
        99,
        101,
        79,
        70,
        70,
        79,
        112,
        116,
        105,
        111,
        110,
    ]
)
IDUBSS = 6
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 50, 66])
IFJBIA = 13
IGYOUS = 54
IIDNIB = 19
IJUGSE = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
IKFWRK = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
ILXWAJ = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
INEJNI = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 6
IRYXBQ = 14
IUSOOQ = 114
IUXFEF = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 80])
IVDNQG = 73
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = 70
JBIAMJ = "".join(chr(c) for c in [70])
JHIUSO = 113
JIGYOU = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
JJJVYF = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
JJVYFC = 37
JMAOAW = 12
JNIBXY = 90
JQRJJJ = 29
JRJHIU = 103
JTACCP = 4
JUGSEL = 81
JUIKFW = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
JUTYEK = "".join(chr(c) for c in [79, 119, 110])
JVDQLA = "".join(
    chr(c)
    for c in [70, 97, 110, 83, 101, 116, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
JWMNZM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
JYKLGQ = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
JYMOUN = "".join(chr(c) for c in [76, 111])
KCWAON = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
KINEJN = 88
KLGQPL = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
KMLOIJ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 53, 65])
KQXPIC = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
KSOKPH = 112
KVKZIL = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
KWIVDN = 72
KXSJWM = 49
LAIIDN = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        99,
        116,
        105,
        118,
        101,
        79,
        110,
        80,
        117,
        109,
        112,
        82,
        117,
        110,
    ]
)
LASSAK = "".join(chr(c) for c in [70, 65, 78])
LGQPLS = 59
LHBQNR = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
LIUXFE = 0
LJUIKF = 1
LKXSJW = "".join(chr(c) for c in [70, 105, 108, 116, 77, 105, 110, 68, 117, 114])
LNMHXE = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
LOIJUG = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
LRAHEO = "".join(chr(c) for c in [])
LSPFTS = 61
LSXUJU = 4
LXWAJV = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
MAOAWB = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
MHXEKV = "".join(
    chr(c)
    for c in [
        69,
        120,
        105,
        116,
        81,
        117,
        105,
        101,
        116,
        65,
        110,
        100,
        82,
        101,
        115,
        116,
        111,
        114,
        101,
        65,
        108,
        108,
        85,
        68,
    ]
)
MJIGYO = 53
MJMAOA = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
MJVHFT = 95
MLOIJU = 79
MNHTBJ = "".join(
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
MNZMJI = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 77, 105, 110, 79, 110, 84, 105, 109, 101]
)
NBLKXS = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
NEJNIB = 89
NHTBJE = "".join(
    chr(c) for c in [69, 99, 111, 110, 80, 114, 111, 103, 83, 116, 97, 116, 117, 115]
)
NIBXTI = 20
NIBXYB = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
NKMLOI = 78
NMHXEK = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
NPYYLI = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
NQGVUN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55])
NQJYMO = 7
NQLNMH = "".join(
    chr(c) for c in [67, 69, 95, 50, 120, 50, 48, 65, 108, 108, 111, 119, 101, 100]
)
NRSJMC = 117
NRXCHW = "".join(chr(c) for c in [50, 52, 104])
NXNKML = 77
NZMJIG = 52
OAWBSI = "".join(chr(c) for c in [78, 111])
OCTHBS = 109
OIJUGS = 80
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 55, 65])
OKPHUO = 100
ONPYYL = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 50])
OOQNRS = "".join(
    chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114, 114, 101, 110, 116]
)
OPHUGT = "".join(chr(c) for c in [80, 72])
OQNRSJ = 116
OUNBLK = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
OUSPBW = "".join(chr(c) for c in [80, 49])
OUYNQJ = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
PBWJYK = 56
PFTSIF = 45
PHUGTY = "".join(chr(c) for c in [67, 104, 101, 99, 107, 71, 70, 67, 73])
PHUOJR = 101
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
    chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 101, 80, 101, 114, 105, 111, 100]
)
POUYNQ = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        67,
        80,
        79,
        84,
        76,
        105,
        109,
        105,
        116,
        79,
        112,
        116,
        105,
        111,
        110,
    ]
)
PQIPOU = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [70, 105, 98, 101, 114, 84, 105, 109, 101, 79, 117, 116]
)
QFFTTI = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        115,
        67,
        111,
        111,
        108,
        105,
        110,
        103,
        68,
        101,
        118,
        105,
        99,
        101,
    ]
)
QFYLJU = "".join(chr(c) for c in [54, 48, 72, 90])
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 72, 101, 97, 116, 101, 114])
QGVUNX = 75
QIEFXQ = 97
QJYMOU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
QLAIID = 18
QLNMHX = 62
QNRSJM = "".join(
    chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114, 114, 101, 110, 116]
)
QNRXCH = "".join(chr(c) for c in [65, 109, 80, 109])
QPLSPF = 60
QRJJJV = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
QSNQLN = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
QXPICX = "".join(chr(c) for c in [83, 65, 78, 73])
RJHIUS = "".join(
    chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114, 114, 101, 110, 116]
)
RJJJVY = 31
RKINEJ = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
RSJMCB = "".join(chr(c) for c in [79, 117, 116, 76, 105])
RTFMNH = 65
RYXBQF = "".join(
    chr(c)
    for c in [
        79,
        118,
        101,
        114,
        83,
        101,
        116,
        112,
        111,
        105,
        110,
        116,
        69,
        110,
        97,
        98,
        108,
        101,
    ]
)
SAKQXP = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SBDJQR = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
SELHBQ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
SIFJBI = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
SIRYXB = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
SJMCBF = 105
SJWMNZ = 50
SKSOKP = "".join(
    chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114, 114, 101, 110, 116]
)
SKWIVD = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52])
SNQLNM = 94
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 52, 65])
SOOQNR = 115
SPBWJY = "".join(
    chr(c) for c in [79, 51, 70, 111, 108, 108, 111, 119, 80, 117, 109, 112]
)
SPFTSI = "".join(chr(c) for c in [83, 97, 110, 105, 76, 101, 118, 101, 108])
SSAKQX = "".join(chr(c) for c in [70, 98, 76, 105])
SSUHBV = 8
SUHBVW = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 49]
)
SXUJUT = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
TACCPQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 79, 112, 116, 105, 111, 110]
)
TBJEUT = "".join(chr(c) for c in [78, 111, 116, 65, 99, 116, 105, 118, 101])
TFMNHT = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
THBSKS = 110
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 22
TIDUBS = "".join(
    chr(c)
    for c in [86, 83, 80, 67, 104, 101, 99, 107, 102, 108, 111, 83, 112, 101, 101, 100]
)
TOPHUG = "".join(chr(c) for c in [67, 108, 101, 97, 110, 70, 105, 108, 116, 101, 114])
TSIFJB = 46
TTIDUB = "".join(chr(c) for c in [80, 117, 109, 112, 51, 65, 115, 86, 83, 80])
TYEKCW = 2
UBSSUH = 7
UBYGDS = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
UGSELH = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
UGTYIY = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 111, 118, 101, 114])
UHBVWV = 9
UIKFWR = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
UJUTYE = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
UNBLKX = 47
UNXNKM = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
UOJRJH = 102
UQEXLS = 2
USOOQN = "".join(
    chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114, 114, 101, 110, 116]
)
UTOPHU = 69
UXFEFJ = 24
UYNQJY = "".join(
    chr(c)
    for c in [
        76,
        105,
        109,
        105,
        116,
        101,
        100,
        73,
        102,
        83,
        80,
        66,
        101,
        108,
        111,
        119,
        57,
        53,
        70,
    ]
)
VDNQGV = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54])
VDQLAI = 17
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [80, 97, 117, 115, 101])
VLASSA = "".join(chr(c) for c in [76, 73])
VUBYGD = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
VUNXNK = 76
VWVUBY = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 51]
)
VYFCRT = 39
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(chr(c) for c in [83, 116, 97, 114, 116, 68, 117, 114, 70, 114, 101])
WIVDNQ = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53])
WJYKLG = 57
WMNZMJ = 51
WRKINE = 87
WSKWIV = 71
WVUBYG = 11
XBQFYL = 64
XCHWDA = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 84, 69, 110, 97, 98, 108, 101]
)
XFEFJT = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
XLSXUJ = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
XNKMLO = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
XPICXQ = "".join(chr(c) for c in [79, 78, 90, 69, 78])
XQGLRA = 99
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 50, 65])
XSJWMN = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
XTIACQ = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        70,
        111,
        114,
        99,
        101,
        79,
        102,
        102,
        73,
        110,
        104,
        105,
        98,
        105,
        116,
        68,
        101,
        108,
        97,
        121,
    ]
)
XUJUTY = 1
XWAJVD = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
XYBQSN = 92
YBQSNQ = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
YEKCWA = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
YFCRTF = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
YIYWSK = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50])
YKLGQP = 58
YLIUXF = 23
YMOUNB = "".join(chr(c) for c in [72, 105])
YOUSPB = 55
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51])
YXBQFY = "".join(
    chr(c)
    for c in [
        69,
        99,
        111,
        110,
        66,
        101,
        108,
        111,
        119,
        83,
        101,
        116,
        112,
        111,
        105,
        110,
        116,
    ]
)
YYLIUX = "".join(chr(c) for c in [67, 108, 101, 97, 110, 80, 49])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(
    chr(c)
    for c in [
        81,
        117,
        105,
        101,
        116,
        65,
        99,
        116,
        105,
        111,
        110,
        79,
        110,
        72,
        101,
        97,
        116,
        101,
        114,
    ]
)
ZMJIGY = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 77, 97, 120, 68, 117, 114]
)
ZUQEXL = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
BIAMJM = [FJBIAM, JBIAMJ]
CHWDAF = [
    BMJVHF,
    ICXQIE,
    XQIEFX,
    IEFXQG,
    FXQGLR,
    QGLRAH,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RSJMCB,
    MCBFEG,
    BFEGZU,
]
CQFFTT = [ACQFFT, OUSPBW, PIPIVL]
HWDAFI = [VLASSA]
JEUTOP = [HTBJEU, TBJEUT, JVHFTH, BJEUTO]
JMCBFE = [
    JVHFTH,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    VLASSA,
]
KFWRKI = [UIKFWR, IKFWRK]
KZILXW = [KVKZIL, VKZILX]
MOUNBL = [JYMOUN, YMOUNB]
PICXQI = [
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
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
    KQXPIC,
    QXPICX,
    XPICXQ,
]
PYYLIU = [WAONPY, AONPYY, ONPYYL, NPYYLI]
QIPOUY = [CPQIPO, PQIPOU]
RAHEOC = [
    JVHFTH,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    LRAHEO,
    IVLASS,
]
RXCHWD = [QNRXCH, NRXCHW]
TYIYWS = [TOPHUG, OPHUGT, PHUGTY, HUGTYI, UGTYIY, GTYIYW]
USPBWJ = [PIPIVL, OUSPBW]
UTYEKC = [UJUTYE, JUTYEK]
WAJVDQ = [ILXWAJ, LXWAJV, XWAJVD, LRAHEO]
WBSIRY = [OAWBSI, AWBSIR]
WDAFIK = []
XEKVKZ = [NMHXEK, MHXEKV, JVHFTH, HXEKVK]
YGDSBD = [UBYGDS, BYGDSB]
YLJUIK = [QFYLJU, FYLJUI]
YNQJYM = [OUYNQJ, UYNQJY]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return JTACCP

    @property
    def output_keys(self):
        return CHWDAF

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, PICXQI, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, PICXQI, None, None, QBMJVH
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, QIEFXQ, None, PICXQI, None, None, QBMJVH
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, None, PICXQI, None, None, QBMJVH
            ),
            FXQGLR: GeckoEnumStructAccessor(
                self.struct, FXQGLR, XQGLRA, None, PICXQI, None, None, QBMJVH
            ),
            QGLRAH: GeckoEnumStructAccessor(
                self.struct, QGLRAH, GLRAHE, None, RAHEOC, None, None, QBMJVH
            ),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoByteStructAccessor(self.struct, CTHBSK, THBSKS, QBMJVH),
            HBSKSO: GeckoByteStructAccessor(self.struct, HBSKSO, BSKSOK, QBMJVH),
            SKSOKP: GeckoByteStructAccessor(self.struct, SKSOKP, KSOKPH, QBMJVH),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, OKPHUO, None, PICXQI, None, None, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, PICXQI, None, None, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, PICXQI, None, None, QBMJVH
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, PICXQI, None, None, QBMJVH
            ),
            RJHIUS: GeckoByteStructAccessor(self.struct, RJHIUS, JHIUSO, QBMJVH),
            HIUSOO: GeckoByteStructAccessor(self.struct, HIUSOO, IUSOOQ, QBMJVH),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, QBMJVH),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, SJMCBF, None, JMCBFE, None, None, QBMJVH
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, PICXQI, None, None, QBMJVH
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, FEGZUQ, None, PICXQI, None, None, QBMJVH
            ),
            EGZUQE: GeckoByteStructAccessor(self.struct, EGZUQE, GZUQEX, QBMJVH),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QBMJVH),
            QEXLSX: GeckoByteStructAccessor(self.struct, QEXLSX, EXLSXU, QBMJVH),
            XLSXUJ: GeckoByteStructAccessor(self.struct, XLSXUJ, LSXUJU, QBMJVH),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XUJUTY, TYEKCW, UTYEKC, None, TYEKCW, QBMJVH
            ),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, CWAONP, None, PYYLIU, None, None, QBMJVH
            ),
            YYLIUX: GeckoBoolStructAccessor(
                self.struct, YYLIUX, YLIUXF, LIUXFE, QBMJVH
            ),
            IUXFEF: GeckoBoolStructAccessor(
                self.struct, IUXFEF, UXFEFJ, LIUXFE, QBMJVH
            ),
            XFEFJT: GeckoBoolStructAccessor(
                self.struct, XFEFJT, FEFJTA, LIUXFE, QBMJVH
            ),
            EFJTAC: GeckoBoolStructAccessor(
                self.struct, EFJTAC, FJTACC, JTACCP, QBMJVH
            ),
            TACCPQ: GeckoBoolStructAccessor(
                self.struct, TACCPQ, FJTACC, ACCPQI, QBMJVH
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, FJTACC, IPOUYN, QIPOUY, None, TYEKCW, QBMJVH
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, FJTACC, NQJYMO, YNQJYM, None, TYEKCW, QBMJVH
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, FJTACC, LIUXFE, MOUNBL, None, TYEKCW, QBMJVH
            ),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, QBMJVH),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoEnumStructAccessor(
                self.struct, GYOUSP, YOUSPB, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoBoolStructAccessor(
                self.struct, SPBWJY, PBWJYK, LIUXFE, QBMJVH
            ),
            BWJYKL: GeckoBoolStructAccessor(
                self.struct, BWJYKL, WJYKLG, LIUXFE, QBMJVH
            ),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, YKLGQP, None, QIPOUY, None, None, QBMJVH
            ),
            KLGQPL: GeckoByteStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoByteStructAccessor(self.struct, GQPLSP, QPLSPF, QBMJVH),
            PLSPFT: GeckoByteStructAccessor(self.struct, PLSPFT, LSPFTS, QBMJVH),
            SPFTSI: GeckoByteStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoByteStructAccessor(self.struct, FTSIFJ, TSIFJB, QBMJVH),
            SIFJBI: GeckoEnumStructAccessor(
                self.struct, SIFJBI, IFJBIA, TYEKCW, BIAMJM, None, TYEKCW, QBMJVH
            ),
            IAMJMA: GeckoTempStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoEnumStructAccessor(
                self.struct, MJMAOA, JMAOAW, None, USPBWJ, None, None, QBMJVH
            ),
            MAOAWB: GeckoEnumStructAccessor(
                self.struct, MAOAWB, AOAWBS, BSIRYX, WBSIRY, None, TYEKCW, QBMJVH
            ),
            SIRYXB: GeckoBoolStructAccessor(
                self.struct, SIRYXB, IRYXBQ, JTACCP, QBMJVH
            ),
            RYXBQF: GeckoBoolStructAccessor(
                self.struct, RYXBQF, IRYXBQ, ACCPQI, QBMJVH
            ),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, AOAWBS, LJUIKF, YLJUIK, None, TYEKCW, QBMJVH
            ),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, AOAWBS, TYEKCW, KFWRKI, None, TYEKCW, QBMJVH
            ),
            FWRKIN: GeckoByteStructAccessor(self.struct, FWRKIN, WRKINE, None),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, None),
            INEJNI: GeckoByteStructAccessor(self.struct, INEJNI, NEJNIB, None),
            EJNIBX: GeckoByteStructAccessor(self.struct, EJNIBX, JNIBXY, QBMJVH),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoByteStructAccessor(self.struct, BXYBQS, XYBQSN, QBMJVH),
            YBQSNQ: GeckoByteStructAccessor(self.struct, YBQSNQ, BQSNQL, QBMJVH),
            QSNQLN: GeckoByteStructAccessor(self.struct, QSNQLN, SNQLNM, QBMJVH),
            NQLNMH: GeckoBoolStructAccessor(
                self.struct, NQLNMH, QLNMHX, IPOUYN, QBMJVH
            ),
            LNMHXE: GeckoEnumStructAccessor(
                self.struct, LNMHXE, QLNMHX, LJUIKF, XEKVKZ, None, JTACCP, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, QLNMHX, LIUXFE, KZILXW, None, TYEKCW, QBMJVH
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, IFJBIA, BSIRYX, WAJVDQ, None, JTACCP, QBMJVH
            ),
            AJVDQL: GeckoBoolStructAccessor(
                self.struct, AJVDQL, IFJBIA, ACCPQI, QBMJVH
            ),
            JVDQLA: GeckoByteStructAccessor(self.struct, JVDQLA, VDQLAI, QBMJVH),
            DQLAII: GeckoByteStructAccessor(self.struct, DQLAII, QLAIID, QBMJVH),
            LAIIDN: GeckoBoolStructAccessor(
                self.struct, LAIIDN, IFJBIA, IPOUYN, QBMJVH
            ),
            AIIDNI: GeckoByteStructAccessor(self.struct, AIIDNI, IIDNIB, QBMJVH),
            IDNIBX: GeckoBoolStructAccessor(
                self.struct, IDNIBX, IFJBIA, NQJYMO, QBMJVH
            ),
            DNIBXT: GeckoByteStructAccessor(self.struct, DNIBXT, NIBXTI, QBMJVH),
            IBXTIA: GeckoByteStructAccessor(self.struct, IBXTIA, BXTIAC, QBMJVH),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, QBMJVH),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, IRYXBQ, LJUIKF, CQFFTT, None, JTACCP, QBMJVH
            ),
            QFFTTI: GeckoBoolStructAccessor(
                self.struct, QFFTTI, IRYXBQ, BSIRYX, QBMJVH
            ),
            FFTTID: GeckoBoolStructAccessor(
                self.struct, FFTTID, FTTIDU, LIUXFE, QBMJVH
            ),
            TTIDUB: GeckoBoolStructAccessor(
                self.struct, TTIDUB, FTTIDU, TYEKCW, QBMJVH
            ),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, QBMJVH),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, QBMJVH),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, QBMJVH),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, QBMJVH),
            VWVUBY: GeckoByteStructAccessor(self.struct, VWVUBY, WVUBYG, QBMJVH),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, XUJUTY, LIUXFE, YGDSBD, None, TYEKCW, QBMJVH
            ),
            GDSBDJ: GeckoBoolStructAccessor(
                self.struct, GDSBDJ, XUJUTY, LJUIKF, QBMJVH
            ),
            SBDJQR: GeckoByteStructAccessor(self.struct, SBDJQR, BDJQRJ, QBMJVH),
            DJQRJJ: GeckoTimeStructAccessor(self.struct, DJQRJJ, JQRJJJ, QBMJVH),
            QRJJJV: GeckoTimeStructAccessor(self.struct, QRJJJV, RJJJVY, QBMJVH),
            JJJVYF: GeckoTimeStructAccessor(self.struct, JJJVYF, JJVYFC, QBMJVH),
            JVYFCR: GeckoTimeStructAccessor(self.struct, JVYFCR, VYFCRT, QBMJVH),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, QBMJVH),
            CRTFMN: GeckoTimeStructAccessor(self.struct, CRTFMN, RTFMNH, QBMJVH),
            TFMNHT: GeckoTimeStructAccessor(self.struct, TFMNHT, FMNHTB, QBMJVH),
            MNHTBJ: GeckoBoolStructAccessor(
                self.struct, MNHTBJ, QLNMHX, BSIRYX, QBMJVH
            ),
            NHTBJE: GeckoEnumStructAccessor(
                self.struct, NHTBJE, QLNMHX, JTACCP, JEUTOP, None, JTACCP, QBMJVH
            ),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, AOAWBS, LIUXFE, RXCHWD, None, TYEKCW, QBMJVH
            ),
            XCHWDA: GeckoBoolStructAccessor(
                self.struct, XCHWDA, IRYXBQ, LIUXFE, QBMJVH
            ),
        }

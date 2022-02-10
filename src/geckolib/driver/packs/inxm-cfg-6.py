#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v6'
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
ACCPQI = 25
ACQFFT = 18
AFIKJP = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 69, 110, 97, 98, 108, 101]
)
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114])
AIIDNI = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
AJVDQL = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
AKQXPI = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
AMJMAO = "".join(chr(c) for c in [83, 97, 110, 105, 79, 110, 84, 105, 109, 101])
AOAWBS = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
AONPYY = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
ASSAKQ = "".join(chr(c) for c in [70, 98, 76, 105])
AWBSIR = "".join(chr(c) for c in [67])
BDJQRJ = 28
BFEGZU = "".join(chr(c) for c in [76, 73])
BIAMJM = "".join(chr(c) for c in [83, 97, 110, 105, 76, 101, 118, 101, 108])
BJEUTO = "".join(
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
BLKXSJ = "".join(chr(c) for c in [72, 105])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
BQNRXC = 82
BQSNQL = 89
BSKSOK = 111
BSSUHB = 5
BVWVUB = 7
BWJYKL = 119
BXTIAC = "".join(
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
BXYBQS = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
BYGDSB = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 50]
)
CBFEGZ = 105
CCPQIP = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
CHWDAF = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
CPQIPO = 26
CQBMJV = 0
CQFFTT = "".join(
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
CRTFMN = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c) for c in [70, 105, 98, 101, 114, 84, 105, 109, 101, 79, 117, 116]
)
CXQIEF = 96
DJQRJJ = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
DNIBXT = "".join(
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
DNQGVU = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52])
DQLAII = "".join(
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
DSBDJQ = 11
DUBSSU = 22
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 0
EFXQGL = 98
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
EJNIBX = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
EKVKZI = 94
ELHBQN = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114])
EUTOPH = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
EXLSXU = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
FCRTFM = 41
FEFJTA = 23
FFTTID = "".join(
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
FJBIAM = "".join(
    chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 101, 80, 101, 114, 105, 111, 100]
)
FJTACC = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 80])
FMNHTB = 67
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
FTTIDU = 20
FWRKIN = "".join(chr(c) for c in [54, 48, 72, 90])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 51, 65])
FYLJUI = 3
GDSBDJ = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 51]
)
GLRAHE = 104
GQPLSP = "".join(
    chr(c) for c in [79, 51, 70, 111, 108, 108, 111, 119, 80, 117, 109, 112]
)
GSELHB = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
GTYIYW = "".join(chr(c) for c in [67, 108, 101, 97, 110, 70, 105, 108, 116, 101, 114])
GVUNXN = 73
GYOUSP = 53
GZUQEX = 106
HBQNRX = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114])
HBVWVU = "".join(
    chr(c) for c in [86, 83, 80, 70, 105, 108, 116, 101, 114, 83, 112, 101, 101, 100]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 108
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUGTYI = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 54, 65])
HWDAFI = "".join(chr(c) for c in [65, 109, 80, 109])
HXEKVK = 93
IACQFF = "".join(
    chr(c)
    for c in [70, 97, 110, 67, 108, 114, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
IAMJMA = 45
IBXTIA = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
IBXYBQ = 87
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 49, 66])
IDNIBX = "".join(
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
IDUBSS = "".join(
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
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 50, 66])
IFJBIA = 59
IGYOUS = "".join(
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
IJUGSE = 78
IKFWRK = 64
ILXWAJ = "".join(
    chr(c) for c in [82, 101, 115, 116, 111, 114, 101, 65, 108, 108, 85, 68]
)
INEJNI = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 5
IRYXBQ = 12
IUSOOQ = "".join(chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114])
IUXFEF = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
IVDNQG = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51])
IVLASS = "".join(chr(c) for c in [])
IYWSKW = "".join(chr(c) for c in [67, 104, 97, 110, 103, 101, 87, 97, 116, 101, 114])
JBIAMJ = 61
JEUTOP = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
JHIUSO = 118
JIGYOU = 52
JJJVYF = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
JJVYFC = 37
JMAOAW = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
JMCBFE = 117
JQRJJJ = 29
JRJHIU = 103
JTACCP = 24
JUGSEL = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
JUIKFW = "".join(
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
JUTYEK = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
JVDQLA = "".join(chr(c) for c in [80, 97, 117, 115, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
JWMNZM = 48
JYMOUN = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
KCWAON = 2
KFWRKI = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
KINEJN = 1
KLGQPL = 55
KMLOIJ = 76
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 53, 65])
KQXPIC = "".join(chr(c) for c in [83, 65, 78, 73])
KSOKPH = 112
KVKZIL = "".join(
    chr(c) for c in [67, 69, 95, 50, 120, 50, 48, 65, 108, 108, 111, 119, 101, 100]
)
KWIVDN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50])
KXSJWM = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
KZILXW = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
LAIIDN = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
LASSAK = "".join(chr(c) for c in [70, 98, 77, 116, 114])
LHBQNR = 81
LIUXFE = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 50])
LJUIKF = 14
LNMHXE = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
LOIJUG = 77
LRAHEO = "".join(chr(c) for c in [72, 84, 82])
LSPFTS = 57
LSXUJU = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
LXWAJV = "".join(
    chr(c) for c in [67, 97, 110, 99, 101, 108, 79, 116, 104, 101, 114, 85, 68]
)
MAOAWB = 15
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 76, 105])
MHXEKV = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
MJIGYO = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
MJMAOA = 46
MJVHFT = 95
MLOIJU = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
MNHTBJ = "".join(
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
MNZMJI = 50
NBLKXS = "".join(chr(c) for c in [76, 111])
NEJNIB = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
NHTBJE = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
NIBXTI = "".join(
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
NIBXYB = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
NKMLOI = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56])
NMHXEK = 92
NPYYLI = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
NQGVUN = 72
NQJYMO = 6
NQLNMH = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114])
NRXCHW = 83
NXNKML = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55])
NZMJIG = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
OAWBSI = 13
OCTHBS = 109
OIJUGS = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 55, 65])
OKPHUO = 100
ONPYYL = 63
OOQNRS = 114
OPHUGT = "".join(
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
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114])
OUNBLK = 7
OUSPBW = 49
OUYNQJ = "".join(chr(c) for c in [65, 110, 121, 85, 68])
PBWJYK = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
PFTSIF = 60
PHUGTY = "".join(chr(c) for c in [75, 54, 48, 48, 70, 111, 114, 77, 97, 121])
PHUOJR = 101
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
    chr(c) for c in [79, 51, 68, 117, 114, 105, 110, 103, 70, 105, 108, 116]
)
POUYNQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
PQIPOU = 4
PYYLIU = 27
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 107
QFFTTI = 19
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
QGVUNX = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53])
QIEFXQ = 97
QIPOUY = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 79, 112, 116, 105, 111, 110]
)
QJYMOU = "".join(
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
QLAIID = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
QLNMHX = 91
QNRSJM = 115
QNRXCH = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
QPLSPF = 56
QRJJJV = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
QSNQLN = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
QXPICX = "".join(chr(c) for c in [79, 78, 90, 69, 78])
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RJJJVY = 31
RSJMCB = 116
RTFMNH = 65
RXCHWD = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
RYXBQF = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
SAKQXP = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
SBDJQR = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
SELHBQ = 80
SIFJBI = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
SIRYXB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
SJMCBF = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
SJWMNZ = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114])
SNQLNM = 90
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 52, 65])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114])
SPBWJY = 54
SPFTSI = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
SSAKQX = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SSUHBV = "".join(chr(c) for c in [80, 117, 109, 112, 51, 65, 115, 86, 83, 80])
SUHBVW = "".join(
    chr(c)
    for c in [86, 83, 80, 67, 104, 101, 99, 107, 102, 108, 111, 83, 112, 101, 101, 100]
)
SXUJUT = 4
TACCPQ = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
TBJEUT = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
TFMNHT = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
THBSKS = 110
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 17
TIDUBS = 21
TSIFJB = 58
TTIDUB = "".join(
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
TYEKCW = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
TYIYWS = "".join(chr(c) for c in [80, 72])
UBSSUH = "".join(chr(c) for c in [80, 117, 109, 112, 49, 65, 115, 86, 83, 80])
UBYGDS = 9
UGSELH = 79
UGTYIY = 69
UHBVWV = 6
UIKFWR = "".join(
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
UJUTYE = 2
UNBLKX = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
UNXNKM = 74
UOJRJH = 102
UQEXLS = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
USOOQN = 113
USPBWJ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
UTOPHU = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
UTYEKC = 1
UYNQJY = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
VDNQGV = 71
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 62
VLASSA = "".join(chr(c) for c in [70, 65, 78])
VUBYGD = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 49]
)
VUNXNK = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54])
VWVUBY = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 48]
)
VYFCRT = 39
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
WAONPY = 3
WBSIRY = "".join(chr(c) for c in [70])
WDAFIK = "".join(chr(c) for c in [50, 52, 104])
WIVDNQ = 70
WJYKLG = "".join(chr(c) for c in [80, 49])
WMNZMJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
WRKINE = "".join(chr(c) for c in [53, 48, 72, 90])
WSKWIV = "".join(
    chr(c) for c in [82, 101, 112, 108, 97, 99, 101, 70, 105, 108, 116, 101, 114]
)
WVUBYG = 8
XBQFYL = "".join(chr(c) for c in [78, 111])
XCHWDA = 84
XEKVKZ = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
XFEFJT = "".join(chr(c) for c in [67, 108, 101, 97, 110, 80, 49])
XLSXUJ = 86
XNKMLO = 75
XPICXQ = "".join(chr(c) for c in [86, 65, 76, 86, 69])
XQGLRA = 99
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 50, 65])
XSJWMN = 47
XTIACQ = "".join(
    chr(c)
    for c in [70, 97, 110, 83, 101, 116, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
XUJUTY = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
XYBQSN = 88
YBQSNQ = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
YEKCWA = "".join(chr(c) for c in [79, 119, 110])
YFCRTF = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
YGDSBD = 10
YIYWSK = "".join(chr(c) for c in [67, 104, 101, 99, 107, 71, 70, 67, 73])
YKLGQP = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
YLIUXF = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 49])
YLJUIK = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
YMOUNB = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
YOUSPB = "".join(
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
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 111, 118, 101, 114])
YXBQFY = 85
YYLIUX = "".join(chr(c) for c in [83, 116, 97, 114, 116, 68, 117, 114, 70, 114, 101])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
ZMJIGY = 51
BSIRYX = [AWBSIR, WBSIRY]
DAFIKJ = [HWDAFI, WDAFIK]
EKCWAO = [TYEKCW, YEKCWA]
FEGZUQ = [
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
    IVLASS,
    BFEGZU,
]
FIKJPU = [
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
    RJHIUS,
    MCBFEG,
    EGZUQE,
    UQEXLS,
]
HIUSOO = [
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
HTBJEU = [JVHFTH, NHTBJE]
IIDNIB = [QLAIID, LAIIDN, AIIDNI, IVLASS]
IKJPUN = [BFEGZU]
JNIBXY = [NEJNIB, EJNIBX]
JYKLGQ = [JVHFTH, WJYKLG, PIPIVL]
KJPUNR = []
LGQPLS = [PIPIVL, WJYKLG]
LKXSJW = [NBLKXS, BLKXSJ]
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
QFYLJU = [XBQFYL, BQFYLJ]
RAHEOC = [
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
    LRAHEO,
]
RKINEJ = [FWRKIN, WRKINE]
SKWIVD = [GTYIYW, TYIYWS, YIYWSK, IYWSKW, YWSKWI, WSKWIV]
TOPHUG = [EUTOPH, UTOPHU]
UXFEFJ = [YYLIUX, YLIUXF, LIUXFE, IUXFEF]
VDQLAI = [AJVDQL, JVDQLA]
XWAJVD = [ZILXWA, ILXWAJ, JVHFTH, LXWAJV]
YNQJYM = [OUYNQJ, UYNQJY]
ZUQEXL = [
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
    BFEGZU,
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


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return NQJYMO

    @property
    def output_keys(self):
        return FIKJPU

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
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, HIUSOO, None, None, QBMJVH
            ),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoByteStructAccessor(self.struct, SJMCBF, JMCBFE, QBMJVH),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, FEGZUQ, None, None, QBMJVH
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, GZUQEX, None, ZUQEXL, None, None, QBMJVH
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, None, ZUQEXL, None, None, QBMJVH
            ),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, QBMJVH),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoByteStructAccessor(self.struct, XUJUTY, UJUTYE, QBMJVH),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, UTYEKC, KCWAON, EKCWAO, None, KCWAON, QBMJVH
            ),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, UXFEFJ, None, None, QBMJVH
            ),
            XFEFJT: GeckoBoolStructAccessor(
                self.struct, XFEFJT, FEFJTA, EFJTAC, QBMJVH
            ),
            FJTACC: GeckoBoolStructAccessor(
                self.struct, FJTACC, JTACCP, EFJTAC, QBMJVH
            ),
            TACCPQ: GeckoBoolStructAccessor(
                self.struct, TACCPQ, ACCPQI, EFJTAC, QBMJVH
            ),
            CCPQIP: GeckoBoolStructAccessor(
                self.struct, CCPQIP, CPQIPO, PQIPOU, QBMJVH
            ),
            QIPOUY: GeckoBoolStructAccessor(
                self.struct, QIPOUY, CPQIPO, IPOUYN, QBMJVH
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, CPQIPO, NQJYMO, YNQJYM, None, KCWAON, QBMJVH
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, CPQIPO, OUNBLK, MOUNBL, None, KCWAON, QBMJVH
            ),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, CPQIPO, EFJTAC, LKXSJW, None, KCWAON, QBMJVH
            ),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, QBMJVH),
            WMNZMJ: GeckoByteStructAccessor(self.struct, WMNZMJ, MNZMJI, QBMJVH),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoByteStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoByteStructAccessor(self.struct, IGYOUS, GYOUSP, QBMJVH),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoByteStructAccessor(self.struct, USPBWJ, SPBWJY, QBMJVH),
            PBWJYK: GeckoEnumStructAccessor(
                self.struct, PBWJYK, BWJYKL, None, JYKLGQ, None, None, QBMJVH
            ),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, LGQPLS, None, None, QBMJVH
            ),
            GQPLSP: GeckoBoolStructAccessor(
                self.struct, GQPLSP, QPLSPF, EFJTAC, QBMJVH
            ),
            PLSPFT: GeckoBoolStructAccessor(
                self.struct, PLSPFT, LSPFTS, EFJTAC, QBMJVH
            ),
            SPFTSI: GeckoByteStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, TSIFJB, None, YNQJYM, None, None, QBMJVH
            ),
            SIFJBI: GeckoByteStructAccessor(self.struct, SIFJBI, IFJBIA, QBMJVH),
            FJBIAM: GeckoByteStructAccessor(self.struct, FJBIAM, JBIAMJ, QBMJVH),
            BIAMJM: GeckoByteStructAccessor(self.struct, BIAMJM, IAMJMA, QBMJVH),
            AMJMAO: GeckoByteStructAccessor(self.struct, AMJMAO, MJMAOA, QBMJVH),
            JMAOAW: GeckoTempStructAccessor(self.struct, JMAOAW, MAOAWB, QBMJVH),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, KCWAON, BSIRYX, None, KCWAON, QBMJVH
            ),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, IRYXBQ, None, LGQPLS, None, None, QBMJVH
            ),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, YXBQFY, FYLJUI, QFYLJU, None, KCWAON, QBMJVH
            ),
            YLJUIK: GeckoBoolStructAccessor(
                self.struct, YLJUIK, LJUIKF, PQIPOU, QBMJVH
            ),
            JUIKFW: GeckoBoolStructAccessor(
                self.struct, JUIKFW, LJUIKF, IPOUYN, QBMJVH
            ),
            UIKFWR: GeckoByteStructAccessor(self.struct, UIKFWR, IKFWRK, QBMJVH),
            KFWRKI: GeckoEnumStructAccessor(
                self.struct, KFWRKI, YXBQFY, KINEJN, RKINEJ, None, KCWAON, QBMJVH
            ),
            INEJNI: GeckoEnumStructAccessor(
                self.struct, INEJNI, YXBQFY, KCWAON, JNIBXY, None, KCWAON, QBMJVH
            ),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, None),
            BXYBQS: GeckoByteStructAccessor(self.struct, BXYBQS, XYBQSN, None),
            YBQSNQ: GeckoByteStructAccessor(self.struct, YBQSNQ, BQSNQL, None),
            QSNQLN: GeckoByteStructAccessor(self.struct, QSNQLN, SNQLNM, QBMJVH),
            NQLNMH: GeckoByteStructAccessor(self.struct, NQLNMH, QLNMHX, QBMJVH),
            LNMHXE: GeckoByteStructAccessor(self.struct, LNMHXE, NMHXEK, QBMJVH),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoByteStructAccessor(self.struct, XEKVKZ, EKVKZI, QBMJVH),
            KVKZIL: GeckoBoolStructAccessor(
                self.struct, KVKZIL, VKZILX, NQJYMO, QBMJVH
            ),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, VKZILX, KINEJN, XWAJVD, None, PQIPOU, QBMJVH
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, VKZILX, EFJTAC, VDQLAI, None, KCWAON, QBMJVH
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, OAWBSI, FYLJUI, IIDNIB, None, PQIPOU, QBMJVH
            ),
            IDNIBX: GeckoBoolStructAccessor(
                self.struct, IDNIBX, OAWBSI, IPOUYN, QBMJVH
            ),
            DNIBXT: GeckoBoolStructAccessor(
                self.struct, DNIBXT, OAWBSI, NQJYMO, QBMJVH
            ),
            NIBXTI: GeckoBoolStructAccessor(
                self.struct, NIBXTI, OAWBSI, OUNBLK, QBMJVH
            ),
            IBXTIA: GeckoEnumStructAccessor(
                self.struct, IBXTIA, LJUIKF, KINEJN, JYKLGQ, None, PQIPOU, QBMJVH
            ),
            BXTIAC: GeckoBoolStructAccessor(
                self.struct, BXTIAC, LJUIKF, FYLJUI, QBMJVH
            ),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, QBMJVH),
            IACQFF: GeckoByteStructAccessor(self.struct, IACQFF, ACQFFT, QBMJVH),
            CQFFTT: GeckoByteStructAccessor(self.struct, CQFFTT, QFFTTI, QBMJVH),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, QBMJVH),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, QBMJVH),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, QBMJVH),
            UBSSUH: GeckoBoolStructAccessor(
                self.struct, UBSSUH, BSSUHB, EFJTAC, QBMJVH
            ),
            SSUHBV: GeckoBoolStructAccessor(
                self.struct, SSUHBV, BSSUHB, KCWAON, QBMJVH
            ),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, QBMJVH),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, QBMJVH),
            VWVUBY: GeckoByteStructAccessor(self.struct, VWVUBY, WVUBYG, QBMJVH),
            VUBYGD: GeckoByteStructAccessor(self.struct, VUBYGD, UBYGDS, QBMJVH),
            BYGDSB: GeckoByteStructAccessor(self.struct, BYGDSB, YGDSBD, QBMJVH),
            GDSBDJ: GeckoByteStructAccessor(self.struct, GDSBDJ, DSBDJQ, QBMJVH),
            SBDJQR: GeckoByteStructAccessor(self.struct, SBDJQR, BDJQRJ, QBMJVH),
            DJQRJJ: GeckoTimeStructAccessor(self.struct, DJQRJJ, JQRJJJ, QBMJVH),
            QRJJJV: GeckoTimeStructAccessor(self.struct, QRJJJV, RJJJVY, QBMJVH),
            JJJVYF: GeckoTimeStructAccessor(self.struct, JJJVYF, JJVYFC, QBMJVH),
            JVYFCR: GeckoTimeStructAccessor(self.struct, JVYFCR, VYFCRT, QBMJVH),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, QBMJVH),
            CRTFMN: GeckoTimeStructAccessor(self.struct, CRTFMN, RTFMNH, QBMJVH),
            TFMNHT: GeckoTimeStructAccessor(self.struct, TFMNHT, FMNHTB, QBMJVH),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, VKZILX, PQIPOU, HTBJEU, None, KCWAON, QBMJVH
            ),
            TBJEUT: GeckoBoolStructAccessor(
                self.struct, TBJEUT, VKZILX, IPOUYN, QBMJVH
            ),
            BJEUTO: GeckoBoolStructAccessor(
                self.struct, BJEUTO, VKZILX, FYLJUI, QBMJVH
            ),
            JEUTOP: GeckoEnumStructAccessor(
                self.struct, JEUTOP, UTYEKC, EFJTAC, TOPHUG, None, KCWAON, QBMJVH
            ),
            OPHUGT: GeckoBoolStructAccessor(
                self.struct, OPHUGT, UTYEKC, KINEJN, QBMJVH
            ),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, YXBQFY, EFJTAC, DAFIKJ, None, KCWAON, QBMJVH
            ),
            AFIKJP: GeckoBoolStructAccessor(
                self.struct, AFIKJP, LJUIKF, EFJTAC, QBMJVH
            ),
        }

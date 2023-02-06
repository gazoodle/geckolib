#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v61'
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
ACCPQI = 78
ACQFFT = "".join(chr(c) for c in [83, 108, 97, 118, 101])
AFIKJP = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
AIIDNI = "".join(
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
AJVDQL = "".join(
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
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 50])
AKSTSE = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
AMJMAO = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
AOAWBS = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
AONPYY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
ASSAKQ = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
ATDZXN = "".join(chr(c) for c in [82, 71, 66])
AWBSIR = "".join(chr(c) for c in [70, 49])
BDJQRJ = "".join(
    chr(c)
    for c in [
        75,
        101,
        121,
        112,
        97,
        100,
        84,
        104,
        101,
        114,
        97,
        112,
        121,
        83,
        117,
        112,
        112,
        111,
        114,
        116,
    ]
)
BFEGZU = 118
BHZVOA = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
BIAMJM = "".join(
    chr(c)
    for c in [
        77,
        105,
        110,
        105,
        109,
        117,
        109,
        73,
        110,
        112,
        117,
        116,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
    ]
)
BJEUTO = "".join(
    chr(c)
    for c in [
        75,
        101,
        121,
        112,
        97,
        100,
        66,
        97,
        99,
        107,
        108,
        105,
        103,
        104,
        116,
        69,
        100,
        105,
        116,
    ]
)
BLKXSJ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
BQNRXC = "".join(chr(c) for c in [73, 100, 111, 108])
BQSNQL = 106
BSIRYX = "".join(chr(c) for c in [70, 51])
BSKSOK = 17
BSSUHB = 64
BVWVUB = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
BWJYKL = 68
BXIBHZ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
BXYBQS = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
CBFEGZ = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
CCPQIP = "".join(chr(c) for c in [80, 49])
CGETIX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
CHWDAF = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
CQBMJV = 0
CRTFMN = "".join(chr(c) for c in [71, 82, 69, 69, 78])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 53])
DAFIKJ = 45
DGKEAK = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
DJQRJJ = 43
DNIBXT = 76
DNQGVU = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
DQLAII = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
DSBDJQ = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
DZXNQT = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
EAKSTS = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 61
EGZUQE = 48
EJNIBX = 100
EKCWAO = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
EKVKZI = 8
ELHBQN = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
ETIXQV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
EUTOPH = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
EXLSXU = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FCRTFM = "".join(chr(c) for c in [82, 69, 68])
FEFJTA = "".join(
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
FEGZUQ = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
FFTTID = 75
FIKJPU = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
FJBIAM = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
FJTACC = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
FMNHTB = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [67, 69])
FTTIDU = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
FWRKIN = 89
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
FZDGKE = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
GDSBDJ = 6
GETIXQ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
GKEAKS = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
GLRAHE = 37
GQPLSP = 77
GSELHB = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
GTYIYW = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
GVUNXN = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
GYOUSP = 3
GZUQEX = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
HBQNRX = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
HBSKSO = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
HBXIBH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 39
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
HUGTYI = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
HXEKVK = 23
IACQFF = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
IAMJMA = 122
IBHZVO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
IBXTIA = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
ICXQIE = 15
IDNIBX = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
IDUBSS = "".join(chr(c) for c in [50, 52, 104])
IEFXQG = 18
IFJBIA = 52
IHBXIB = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
IIDNIB = 5
IJUGSE = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
IKFWRK = 88
IKJPUN = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
ILXWAJ = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
INEJNI = 99
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
IRYXBQ = "".join(chr(c) for c in [76, 105, 110, 101, 50])
IUSOOQ = 54
IUXFEF = 59
IVDNQG = "".join(chr(c) for c in [67, 111, 97, 115, 116])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
IYWSKW = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
JBIAMJ = 53
JEUTOP = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
JHIUSO = 80
JIGYOU = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
JJJVYF = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
JMAOAW = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
JNIBXY = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
JPUNRJ = "".join(
    chr(c)
    for c in [
        76,
        111,
        119,
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
        77,
        101,
        110,
        117,
    ]
)
JQRJJJ = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
JTACCP = 62
JUGSEL = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
JUIKFW = 87
JUTYEK = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
JVDQLA = 72
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
JWMNZM = "".join(chr(c) for c in [67])
JYKLGQ = 70
JYMOUN = 30
JZTATD = 121
KCWAON = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
KEAKST = 126
KFWRKI = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
KINEJN = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
KMLOIJ = "".join(chr(c) for c in [80, 68, 67])
KPHUOJ = 47
KQXPIC = 13
KSOKPH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
KSTSEM = 127
KVKZIL = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
KWIVDN = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
KXSJWM = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
KZILXW = "".join(
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
LAIIDN = "".join(
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
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
LHBQNR = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
LIUXFE = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
LJUIKF = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
LKXSJW = 1
LNMHXE = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
LOIJUG = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [85, 76, 95, 67, 69])
MCBFEG = 0
MCGETI = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
MFZDGK = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
MHXEKV = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
MJIGYO = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
MJMAOA = 74
MJVHFT = 12
MLOIJU = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
MNHTBJ = "".join(chr(c) for c in [67, 89, 65, 78])
MNZMJI = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
MOUNBL = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
NBLKXS = 63
NEJNIB = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
NHTBJE = "".join(chr(c) for c in [87, 72, 73, 84, 69])
NIBXTI = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
NIBXYB = 104
NKMLOI = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
NMHXEK = 6
NPYYLI = "".join(chr(c) for c in [72, 105])
NQGVUN = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
NQLNMH = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
NRJZTA = "".join(
    chr(c)
    for c in [
        68,
        101,
        97,
        108,
        101,
        114,
        76,
        111,
        99,
        107,
        83,
        117,
        112,
        112,
        111,
        114,
        116,
    ]
)
NRSJMC = 81
NRXCHW = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
NXNKML = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
NZMJIG = 31
OACMCV = 61
OAWBSI = 83
OCTHBS = 40
OIHBXI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
OIJUGS = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
OJRJHI = "".join(chr(c) for c in [76, 73])
OKPHUO = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 65, 115, 67, 80]
)
ONPYYL = "".join(chr(c) for c in [76, 111])
OOQNRS = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
OPHUGT = 44
OQNRSJ = 56
OUSPBW = 35
PBWJYK = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
PFTSIF = "".join(chr(c) for c in [85, 76])
PHUGTY = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
PHUOJR = 2
PICXQI = "".join(chr(c) for c in [79, 117, 116, 52])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 26
POUYNQ = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
PQIPOU = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
PUNRJZ = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
QFFTTI = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
QFYLJU = 85
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
QGVUNX = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
QIPOUY = 28
QJYMOU = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
QLAIID = 1
QLNMHX = 4
QNRSJM = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
QNRXCH = "".join(chr(c) for c in [65, 115, 112, 101, 110])
QPLSPF = "".join(
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
QRJJJV = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
QSNQLN = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
QTMFZD = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
QVXOIH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
QXPICX = "".join(chr(c) for c in [79, 117, 116, 51])
RAHEOC = 38
RJHIUS = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
RJJJVY = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
RJZTAT = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
RKINEJ = 98
RSJMCB = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
RTFMNH = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
RXCHWD = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
SBDJQR = 7
SELHBQ = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
SEMCGE = "".join(chr(c) for c in [51])
SIFJBI = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
SIRYXB = "".join(chr(c) for c in [76, 105, 110, 101, 49])
SJMCBF = "".join(chr(c) for c in [79, 119, 110])
SJWMNZ = "".join(chr(c) for c in [70])
SKWIVD = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
SNQLNM = 3
SOKPHU = 41
SOOQNR = 55
SPBWJY = 66
SPFTSI = 51
SSAKQX = "".join(chr(c) for c in [65, 85, 88])
SSUHBV = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
STSEMC = "".join(chr(c) for c in [49])
SUHBVW = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
SXUJUT = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
TACCPQ = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
TATDZX = 123
TBJEUT = 8
TFMNHT = "".join(chr(c) for c in [66, 76, 85, 69])
THBSKS = 42
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 73
TIDUBS = "".join(chr(c) for c in [65, 109, 80, 109])
TIXQVX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
TMFZDG = 124
TOPHUG = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
TSEMCG = "".join(chr(c) for c in [50])
TTIDUB = 34
TYEKCW = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
TYIYWS = "".join(chr(c) for c in [65, 108, 112, 115])
UBSSUH = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
UBYGDS = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
UGSELH = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
UGTYIY = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
UHBVWV = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
UIKFWR = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 70, 117, 115, 101])
UJUTYE = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
UNBLKX = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
UNRJZT = 46
UNXNKM = "".join(chr(c) for c in [76, 65])
UOJRJH = 79
UQEXLS = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
USOOQN = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
USPBWJ = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
UXFEFJ = "".join(
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
UYNQJY = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
VDNQGV = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
VDQLAI = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 10
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
VUNXNK = "".join(chr(c) for c in [74, 97, 122, 122, 105])
VWVUBY = 4
VXOIHB = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
VYFCRT = "".join(
    chr(c)
    for c in [
        75,
        101,
        121,
        112,
        97,
        100,
        66,
        97,
        99,
        107,
        108,
        105,
        103,
        104,
        116,
        67,
        111,
        108,
        111,
        114,
    ]
)
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 82
WBSIRY = "".join(chr(c) for c in [70, 50])
WDAFIK = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        101,
        75,
        101,
        121,
        65,
        115,
        73,
        110,
        118,
        101,
        114,
        116,
        68,
        105,
        115,
        112,
        108,
        97,
        121,
        75,
        101,
        121,
    ]
)
WIVDNQ = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
WJYKLG = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
WRKINE = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
WSKWIV = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
WVUBYG = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
XBQFYL = 84
XCHWDA = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
XEKVKZ = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
XFEFJT = 60
XIBHZV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
XLSXUJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
XNKMLO = "".join(chr(c) for c in [77, 65, 65, 88])
XNQTMF = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
XOIHBX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
XPICXQ = 14
XQGLRA = 36
XQIEFX = 16
XQVXOI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
XSJWMN = 33
XTIACQ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
XUJUTY = 27
XWAJVD = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
XYBQSN = 105
YBQSNQ = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
YEKCWA = 57
YFCRTF = "".join(chr(c) for c in [79, 70, 70])
YGDSBD = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
YIYWSK = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
YKLGQP = "".join(chr(c) for c in [78, 105, 103, 104, 116])
YLIUXF = 58
YLJUIK = 86
YMOUNB = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
YNQJYM = 29
YOUSPB = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
YXBQFY = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
YYLIUX = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = 125
ZILXWA = 71
ZMJIGY = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
ZTATDZ = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
ZUQEXL = 32
ZXNQTM = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
BXTIAC = [NIBXTI, IBXTIA]
BYGDSB = [VUBYGD, UBYGDS]
CPQIPO = [JVHFTH, CCPQIP, PIPIVL]
CQFFTT = [VLASSA, IACQFF, ACQFFT]
DUBSSU = [JVHFTH, TIDUBS, IDUBSS]
EFXQGL = [
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
EMCGET = [VLASSA, STSEMC, TSEMCG, SEMCGE]
HBVWVU = [SUHBVW, UHBVWV]
HTBJEU = [YFCRTF, FCRTFM, CRTFMN, RTFMNH, TFMNHT, FMNHTB, MNHTBJ, NHTBJE]
HWDAFI = [
    PHUGTY,
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    KWIVDN,
    WIVDNQ,
    IVDNQG,
    VDNQGV,
    DNQGVU,
    NQGVUN,
    QGVUNX,
    GVUNXN,
    VUNXNK,
    UNXNKM,
    NXNKML,
    XNKMLO,
    NKMLOI,
    KMLOIJ,
    MLOIJU,
    LOIJUG,
    OIJUGS,
    IJUGSE,
    JUGSEL,
    UGSELH,
    GSELHB,
    SELHBQ,
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
    QNRXCH,
    NRXCHW,
    RXCHWD,
    XCHWDA,
    CHWDAF,
]
HZVOAC = [BMJVHF, AKQXPI, QXPICX, PICXQI, CXQIEF, QIEFXQ, HBSKSO, HUOJRJ]
IBXYBQ = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, SIRYXB, IRYXBQ]
IGYOUS = [MJIGYO, JIGYOU]
JJVYFC = [RJJJVY, JJJVYF]
JMCBFE = [RSJMCB, SJMCBF]
JRJHIU = [
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
    OJRJHI,
]
KJPUNR = [FIKJPU, IKJPUN, VLASSA, VLASSA]
KLGQPL = [YMOUNB, YKLGQP]
LSXUJU = [UQEXLS, QEXLSX, EXLSXU, XLSXUJ]
LXWAJV = [JVHFTH, UJUTYE, ILXWAJ]
MAOAWB = [YMOUNB, JMAOAW]
NQJYMO = [PIPIVL, CCPQIP]
NQTMFZ = [ZXNQTM, XNQTMF]
OUNBLK = [YMOUNB, MOUNBL]
OUYNQJ = [IPOUYN, POUYNQ]
PYYLIU = [ONPYYL, NPYYLI]
RYXBQF = [AWBSIR, WBSIRY, BSIRYX, VLASSA, VLASSA, VLASSA, SIRYXB, IRYXBQ]
SAKQXP = [
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
    VLASSA,
    VLASSA,
    ASSAKQ,
    SSAKQX,
]
SKSOKP = [
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
TDZXNQ = [ATDZXN, NHTBJE]
TSIFJB = [PFTSIF, FTSIFJ]
UTOPHU = [JEUTOP, EUTOPH]
UTYEKC = [UJUTYE, JUTYEK]
VOACMC = []
WAONPY = [EKCWAO, KCWAON, CWAONP]
WMNZMJ = [SJWMNZ, JWMNZM]
ZVOACM = [OJRJHI]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return OACMCV

    @property
    def output_keys(self):
        return HZVOAC

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, SAKQXP, None, None, QBMJVH
            ),
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, None, SAKQXP, None, None, QBMJVH
            ),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, None, SAKQXP, None, None, QBMJVH
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, SAKQXP, None, None, QBMJVH
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, SAKQXP, None, None, QBMJVH
            ),
            QIEFXQ: GeckoEnumStructAccessor(
                self.struct, QIEFXQ, IEFXQG, None, EFXQGL, None, None, QBMJVH
            ),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoByteStructAccessor(self.struct, CTHBSK, THBSKS, QBMJVH),
            HBSKSO: GeckoEnumStructAccessor(
                self.struct, HBSKSO, BSKSOK, None, SKSOKP, None, None, QBMJVH
            ),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, QBMJVH),
            OKPHUO: GeckoBoolStructAccessor(
                self.struct, OKPHUO, KPHUOJ, PHUOJR, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, JRJHIU, None, None, None
            ),
            RJHIUS: GeckoByteStructAccessor(self.struct, RJHIUS, JHIUSO, None),
            HIUSOO: GeckoByteStructAccessor(self.struct, HIUSOO, IUSOOQ, QBMJVH),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, NRSJMC, MCBFEG, JMCBFE, None, PHUOJR, QBMJVH
            ),
            CBFEGZ: GeckoByteStructAccessor(self.struct, CBFEGZ, BFEGZU, QBMJVH),
            FEGZUQ: GeckoByteStructAccessor(self.struct, FEGZUQ, EGZUQE, QBMJVH),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, LSXUJU, None, None, QBMJVH
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XUJUTY, None, UTYEKC, None, None, QBMJVH
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, None, WAONPY, None, None, QBMJVH
            ),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, NRSJMC, PHUOJR, PYYLIU, None, PHUOJR, QBMJVH
            ),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, QBMJVH),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, QBMJVH),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, QBMJVH),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, QBMJVH),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, NQJYMO, None, None, QBMJVH
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, OUNBLK, None, None, QBMJVH
            ),
            UNBLKX: GeckoByteStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoTempStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoEnumStructAccessor(
                self.struct, KXSJWM, XSJWMN, None, WMNZMJ, None, None, QBMJVH
            ),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, NQJYMO, None, None, QBMJVH
            ),
            ZMJIGY: GeckoEnumStructAccessor(
                self.struct, ZMJIGY, NRSJMC, GYOUSP, IGYOUS, None, PHUOJR, QBMJVH
            ),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoTempStructAccessor(self.struct, USPBWJ, SPBWJY, QBMJVH),
            PBWJYK: GeckoTempStructAccessor(self.struct, PBWJYK, BWJYKL, QBMJVH),
            WJYKLG: GeckoEnumStructAccessor(
                self.struct, WJYKLG, JYKLGQ, None, KLGQPL, None, None, QBMJVH
            ),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoByteStructAccessor(self.struct, QPLSPF, PLSPFT, QBMJVH),
            LSPFTS: GeckoEnumStructAccessor(
                self.struct, LSPFTS, SPFTSI, None, TSIFJB, None, None, QBMJVH
            ),
            SIFJBI: GeckoByteStructAccessor(self.struct, SIFJBI, IFJBIA, QBMJVH),
            FJBIAM: GeckoByteStructAccessor(self.struct, FJBIAM, JBIAMJ, QBMJVH),
            BIAMJM: GeckoByteStructAccessor(self.struct, BIAMJM, IAMJMA, QBMJVH),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, MJMAOA, None, MAOAWB, None, None, QBMJVH
            ),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, None, RYXBQF, None, None, QBMJVH
            ),
            YXBQFY: GeckoEnumStructAccessor(
                self.struct, YXBQFY, XBQFYL, None, RYXBQF, None, None, QBMJVH
            ),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, RYXBQF, None, None, QBMJVH
            ),
            FYLJUI: GeckoEnumStructAccessor(
                self.struct, FYLJUI, YLJUIK, None, RYXBQF, None, None, QBMJVH
            ),
            LJUIKF: GeckoEnumStructAccessor(
                self.struct, LJUIKF, JUIKFW, None, RYXBQF, None, None, QBMJVH
            ),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, IKFWRK, None, RYXBQF, None, None, QBMJVH
            ),
            KFWRKI: GeckoEnumStructAccessor(
                self.struct, KFWRKI, FWRKIN, None, RYXBQF, None, None, QBMJVH
            ),
            WRKINE: GeckoByteStructAccessor(self.struct, WRKINE, RKINEJ, QBMJVH),
            KINEJN: GeckoByteStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoByteStructAccessor(self.struct, NEJNIB, EJNIBX, QBMJVH),
            JNIBXY: GeckoEnumStructAccessor(
                self.struct, JNIBXY, NIBXYB, None, IBXYBQ, None, None, QBMJVH
            ),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, None, IBXYBQ, None, None, QBMJVH
            ),
            YBQSNQ: GeckoEnumStructAccessor(
                self.struct, YBQSNQ, BQSNQL, None, IBXYBQ, None, None, QBMJVH
            ),
            QSNQLN: GeckoByteStructAccessor(self.struct, QSNQLN, SNQLNM, QBMJVH),
            NQLNMH: GeckoTimeStructAccessor(self.struct, NQLNMH, QLNMHX, QBMJVH),
            LNMHXE: GeckoTimeStructAccessor(self.struct, LNMHXE, NMHXEK, QBMJVH),
            MHXEKV: GeckoTimeStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoTimeStructAccessor(self.struct, XEKVKZ, EKVKZI, QBMJVH),
            KVKZIL: GeckoTimeStructAccessor(self.struct, KVKZIL, VKZILX, QBMJVH),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, ZILXWA, None, LXWAJV, None, None, QBMJVH
            ),
            XWAJVD: GeckoBoolStructAccessor(
                self.struct, XWAJVD, WAJVDQ, MCBFEG, QBMJVH
            ),
            AJVDQL: GeckoBoolStructAccessor(
                self.struct, AJVDQL, JVDQLA, PHUOJR, QBMJVH
            ),
            VDQLAI: GeckoBoolStructAccessor(
                self.struct, VDQLAI, JVDQLA, MCBFEG, QBMJVH
            ),
            DQLAII: GeckoBoolStructAccessor(
                self.struct, DQLAII, JVDQLA, QLAIID, QBMJVH
            ),
            LAIIDN: GeckoBoolStructAccessor(
                self.struct, LAIIDN, JVDQLA, GYOUSP, QBMJVH
            ),
            AIIDNI: GeckoBoolStructAccessor(
                self.struct, AIIDNI, JVDQLA, IIDNIB, QBMJVH
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, DNIBXT, None, BXTIAC, None, None, QBMJVH
            ),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, TIACQF, None, CQFFTT, None, None, QBMJVH
            ),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, QBMJVH),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, TTIDUB, None, DUBSSU, None, None, QBMJVH
            ),
            UBSSUH: GeckoWordStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoEnumStructAccessor(
                self.struct, SSUHBV, NRSJMC, QLAIID, HBVWVU, None, PHUOJR, QBMJVH
            ),
            BVWVUB: GeckoBoolStructAccessor(
                self.struct, BVWVUB, NRSJMC, VWVUBY, QBMJVH
            ),
            WVUBYG: GeckoEnumStructAccessor(
                self.struct, WVUBYG, NRSJMC, IIDNIB, BYGDSB, None, PHUOJR, QBMJVH
            ),
            YGDSBD: GeckoBoolStructAccessor(
                self.struct, YGDSBD, NRSJMC, GDSBDJ, QBMJVH
            ),
            DSBDJQ: GeckoBoolStructAccessor(
                self.struct, DSBDJQ, NRSJMC, SBDJQR, QBMJVH
            ),
            BDJQRJ: GeckoBoolStructAccessor(
                self.struct, BDJQRJ, DJQRJJ, MCBFEG, QBMJVH
            ),
            JQRJJJ: GeckoBoolStructAccessor(
                self.struct, JQRJJJ, DJQRJJ, QLAIID, QBMJVH
            ),
            QRJJJV: GeckoEnumStructAccessor(
                self.struct, QRJJJV, DJQRJJ, PHUOJR, JJVYFC, None, PHUOJR, QBMJVH
            ),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, DJQRJJ, GYOUSP, JJVYFC, None, PHUOJR, QBMJVH
            ),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, DJQRJJ, VWVUBY, HTBJEU, None, TBJEUT, QBMJVH
            ),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, DJQRJJ, SBDJQR, UTOPHU, None, PHUOJR, QBMJVH
            ),
            WDAFIK: GeckoBoolStructAccessor(
                self.struct, WDAFIK, DAFIKJ, QLAIID, QBMJVH
            ),
            AFIKJP: GeckoEnumStructAccessor(
                self.struct, AFIKJP, DAFIKJ, PHUOJR, KJPUNR, None, VWVUBY, QBMJVH
            ),
            JPUNRJ: GeckoBoolStructAccessor(
                self.struct, JPUNRJ, DAFIKJ, VWVUBY, QBMJVH
            ),
            PUNRJZ: GeckoByteStructAccessor(self.struct, PUNRJZ, UNRJZT, QBMJVH),
            NRJZTA: GeckoBoolStructAccessor(
                self.struct, NRJZTA, KPHUOJ, MCBFEG, QBMJVH
            ),
            RJZTAT: GeckoByteStructAccessor(self.struct, RJZTAT, JZTATD, QBMJVH),
            ZTATDZ: GeckoEnumStructAccessor(
                self.struct, ZTATDZ, TATDZX, MCBFEG, TDZXNQ, None, PHUOJR, None
            ),
            DZXNQT: GeckoEnumStructAccessor(
                self.struct, DZXNQT, TATDZX, QLAIID, NQTMFZ, None, PHUOJR, None
            ),
            QTMFZD: GeckoEnumStructAccessor(
                self.struct, QTMFZD, TMFZDG, MCBFEG, TDZXNQ, None, PHUOJR, None
            ),
            MFZDGK: GeckoEnumStructAccessor(
                self.struct, MFZDGK, TMFZDG, QLAIID, NQTMFZ, None, PHUOJR, None
            ),
            FZDGKE: GeckoEnumStructAccessor(
                self.struct, FZDGKE, ZDGKEA, MCBFEG, TDZXNQ, None, PHUOJR, None
            ),
            DGKEAK: GeckoEnumStructAccessor(
                self.struct, DGKEAK, ZDGKEA, QLAIID, NQTMFZ, None, PHUOJR, None
            ),
            GKEAKS: GeckoEnumStructAccessor(
                self.struct, GKEAKS, KEAKST, MCBFEG, TDZXNQ, None, PHUOJR, None
            ),
            EAKSTS: GeckoEnumStructAccessor(
                self.struct, EAKSTS, KEAKST, QLAIID, NQTMFZ, None, PHUOJR, None
            ),
            AKSTSE: GeckoEnumStructAccessor(
                self.struct, AKSTSE, KSTSEM, MCBFEG, EMCGET, None, TBJEUT, None
            ),
            MCGETI: GeckoBoolStructAccessor(self.struct, MCGETI, KSTSEM, SBDJQR, None),
            CGETIX: GeckoBoolStructAccessor(self.struct, CGETIX, TATDZX, VWVUBY, None),
            GETIXQ: GeckoBoolStructAccessor(self.struct, GETIXQ, TATDZX, IIDNIB, None),
            ETIXQV: GeckoBoolStructAccessor(self.struct, ETIXQV, TATDZX, GDSBDJ, None),
            TIXQVX: GeckoBoolStructAccessor(self.struct, TIXQVX, TATDZX, SBDJQR, None),
            IXQVXO: GeckoBoolStructAccessor(self.struct, IXQVXO, TMFZDG, VWVUBY, None),
            XQVXOI: GeckoBoolStructAccessor(self.struct, XQVXOI, TMFZDG, IIDNIB, None),
            QVXOIH: GeckoBoolStructAccessor(self.struct, QVXOIH, TMFZDG, GDSBDJ, None),
            VXOIHB: GeckoBoolStructAccessor(self.struct, VXOIHB, TMFZDG, SBDJQR, None),
            XOIHBX: GeckoBoolStructAccessor(self.struct, XOIHBX, ZDGKEA, VWVUBY, None),
            OIHBXI: GeckoBoolStructAccessor(self.struct, OIHBXI, ZDGKEA, IIDNIB, None),
            IHBXIB: GeckoBoolStructAccessor(self.struct, IHBXIB, ZDGKEA, GDSBDJ, None),
            HBXIBH: GeckoBoolStructAccessor(self.struct, HBXIBH, ZDGKEA, SBDJQR, None),
            BXIBHZ: GeckoBoolStructAccessor(self.struct, BXIBHZ, KEAKST, VWVUBY, None),
            XIBHZV: GeckoBoolStructAccessor(self.struct, XIBHZV, KEAKST, IIDNIB, None),
            IBHZVO: GeckoBoolStructAccessor(self.struct, IBHZVO, KEAKST, GDSBDJ, None),
            BHZVOA: GeckoBoolStructAccessor(self.struct, BHZVOA, KEAKST, SBDJQR, None),
        }

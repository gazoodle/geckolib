#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ-V3 v62'
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
ACCPQI = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
ACQFFT = 108
AFIKJP = "".join(
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
AHEOCT = 15
AIIDNI = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
AKSTSE = "".join(chr(c) for c in [50])
AMJMAO = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
AOAWBS = "".join(chr(c) for c in [70, 50])
AONPYY = 58
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 116, 101, 99, 116, 105, 111, 110])
ATDZXN = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
AWBSIR = "".join(chr(c) for c in [76, 105, 110, 101, 49])
BDJQRJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
BFEGZU = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
BIAMJM = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
BJEUTO = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
BLKXSJ = "".join(chr(c) for c in [67])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 86
BQNRXC = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
BQSNQL = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
BSKSOK = "".join(chr(c) for c in [79, 117, 116, 76, 105])
BSSUHB = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
BVWVUB = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
BWJYKL = 68
BXIBHZ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
BXTIAC = "".join(chr(c) for c in [83, 76, 69, 69, 80])
BXYBQS = 23
BYGDSB = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
CBFEGZ = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
CCPQIP = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
CGETIX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
CHWDAF = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
CRTFMN = "".join(chr(c) for c in [67, 89, 65, 78])
CTHBSK = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 65, 115, 67, 80]
)
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 1
CXQIEF = 16
DGKEAK = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
DJQRJJ = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
DNIBXT = 107
DNQGVU = "".join(chr(c) for c in [74, 97, 122, 122, 105])
DQLAII = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
DSBDJQ = 43
DUBSSU = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
DZXNQT = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
EAKSTS = "".join(chr(c) for c in [49])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [80, 49])
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
EJNIBX = 4
EKVKZI = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
ELHBQN = "".join(chr(c) for c in [65, 115, 112, 101, 110])
EMCGET = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
EOCTHB = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
ETIXQV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
EUTOPH = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
FCRTFM = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
FEFJTA = 78
FEGZUQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
FFTTID = "".join(chr(c) for c in [65, 109, 80, 109])
FIKJPU = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
FJBIAM = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
FMNHTB = 8
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [67, 69])
FTTIDU = "".join(chr(c) for c in [50, 52, 104])
FXQGLR = 37
FYLJUI = 87
FZDGKE = 126
GDSBDJ = "".join(
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
GETIXQ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
GKEAKS = 127
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
GQPLSP = 77
GSELHB = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
GTYIYW = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
GVUNXN = "".join(chr(c) for c in [77, 65, 65, 88])
GYOUSP = 3
GZUQEX = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
HBQNRX = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
HBSKSO = 2
HBVWVU = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
HBXIBH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 81
HTBJEU = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
HUGTYI = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
HUOJRJ = 54
HWDAFI = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
HXEKVK = "".join(
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
IACQFF = "".join(
    chr(c) for c in [83, 105, 108, 101, 110, 116, 68, 117, 114, 97, 116, 105, 111, 110]
)
IAMJMA = 74
IBXTIA = "".join(chr(c) for c in [69, 67, 79, 78, 79, 77, 89])
IBXYBQ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IDNIBX = "".join(chr(c) for c in [83, 105, 108, 101, 110, 116, 77, 111, 100, 101])
IDUBSS = 64
IEFXQG = 36
IFJBIA = 52
IHBXIB = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
IIDNIB = 75
IJUGSE = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
IKFWRK = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
IKJPUN = 46
ILXWAJ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
INEJNI = 3
IPIVLA = "".join(chr(c) for c in [79, 51])
IRYXBQ = 84
IUSOOQ = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
IUXFEF = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
IVDNQG = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
IYWSKW = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
JBIAMJ = 53
JEUTOP = 44
JHIUSO = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
JIGYOU = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
JJJVYF = "".join(
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
JJVYFC = "".join(chr(c) for c in [82, 69, 68])
JMAOAW = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
JMCBFE = 32
JNIBXY = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
JPUNRJ = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
JQRJJJ = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
JRJHIU = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
JTACCP = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
JUGSEL = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
JUIKFW = "".join(chr(c) for c in [70, 52, 67, 117, 114, 114, 101, 110, 116])
JVDQLA = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [71, 82, 69, 69, 78])
JWMNZM = 25
JYKLGQ = 70
JYMOUN = 63
KCWAON = "".join(
    chr(c) for c in [65, 117, 120, 65, 115, 66, 117, 98, 98, 108, 101, 71, 101, 110]
)
KEAKST = "".join(chr(c) for c in [78, 111, 110, 101])
KFWRKI = 104
KINEJN = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
KJPUNR = "".join(
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
KMLOIJ = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
KPHUOJ = 80
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 50])
KSOKPH = "".join(chr(c) for c in [76, 73])
KSTSEM = "".join(chr(c) for c in [51])
KVKZIL = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
KWIVDN = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
KXSJWM = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
KZILXW = "".join(
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
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
LHBQNR = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
LIUXFE = 61
LJUIKF = 98
LOIJUG = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
LRAHEO = 40
LSPFTS = "".join(chr(c) for c in [85, 76, 95, 67, 69])
LSXUJU = 57
LXWAJV = 76
MAOAWB = 83
MCBFEG = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
MCGETI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
MFZDGK = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
MHXEKV = 82
MJIGYO = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
MJVHFT = 12
MLOIJU = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
MNHTBJ = "".join(
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
MNZMJI = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
MOUNBL = 1
NBLKXS = "".join(chr(c) for c in [70])
NEJNIB = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
NHTBJE = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
NIBXTI = "".join(chr(c) for c in [79, 70, 70])
NIBXYB = 6
NKMLOI = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
NMHXEK = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
NPYYLI = 59
NQGVUN = "".join(chr(c) for c in [76, 65])
NQLNMH = 71
NQTMFZ = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
NRJZTA = 123
NRSJMC = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
NXNKML = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
OAWBSI = "".join(chr(c) for c in [70, 52])
OCTHBS = 39
OIHBXI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
OIJUGS = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
OJRJHI = 55
OKPHUO = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
ONPYYL = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
OOQNRS = 0
OPHUGT = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
OQNRSJ = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
OUNBLK = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
OUSPBW = 35
OUYNQJ = 30
PBWJYK = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
PFTSIF = "".join(chr(c) for c in [85, 76])
PHUGTY = "".join(chr(c) for c in [65, 108, 112, 115])
PHUOJR = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
PICXQI = 14
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 26
POUYNQ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
PQIPOU = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
PUNRJZ = 121
PYYLIU = "".join(
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
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
QFFTTI = 34
QFYLJU = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
QGLRAH = 38
QGVUNX = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
QIPOUY = 29
QJYMOU = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
QLAIID = "".join(chr(c) for c in [83, 108, 97, 118, 101])
QLNMHX = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
QNRSJM = 48
QNRXCH = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
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
QSNQLN = 10
QTMFZD = 125
QVXOIH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
QXPICX = 13
RAHEOC = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RJHIUS = 56
RJJJVY = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
RJZTAT = "".join(chr(c) for c in [82, 71, 66])
RKINEJ = 105
RSJMCB = 118
RTFMNH = "".join(chr(c) for c in [87, 72, 73, 84, 69])
RXCHWD = "".join(
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
RYXBQF = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
SAKQXP = "".join(chr(c) for c in [65, 85, 88])
SBDJQR = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
SELHBQ = "".join(chr(c) for c in [73, 100, 111, 108])
SEMCGE = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
SIFJBI = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
SIRYXB = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
SJMCBF = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
SJWMNZ = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
SKSOKP = 79
SKWIVD = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
SNQLNM = "".join(
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
SPBWJY = 66
SPFTSI = 51
SSAKQX = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
STSEMC = "".join(chr(c) for c in [52])
SUHBVW = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
SXUJUT = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
TACCPQ = 28
TATDZX = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
THBSKS = 47
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIDUBS = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
TIXQVX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
TMFZDG = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
TOPHUG = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
TYEKCW = "".join(chr(c) for c in [76, 111])
TYIYWS = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
UBSSUH = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
UBYGDS = 6
UGSELH = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
UGTYIY = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
UHBVWV = 4
UIKFWR = 99
UJUTYE = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
UNBLKX = 33
UNRJZT = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
UNXNKM = "".join(chr(c) for c in [80, 68, 67])
UOJRJH = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
UQEXLS = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
USOOQN = "".join(chr(c) for c in [79, 119, 110])
USPBWJ = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
UTOPHU = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
UTYEKC = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
UXFEFJ = 62
UYNQJY = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
VDNQGV = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
VDQLAI = 73
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
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
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
VUNXNK = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
VWVUBY = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
VXOIHB = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
VYFCRT = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
WAONPY = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
WBSIRY = "".join(chr(c) for c in [76, 105, 110, 101, 50])
WDAFIK = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
WIVDNQ = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
WJYKLG = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
WMNZMJ = "".join(chr(c) for c in [105, 110, 70, 108, 111])
WRKINE = "".join(chr(c) for c in [70, 52, 76, 105, 110, 101])
WSKWIV = "".join(chr(c) for c in [67, 111, 97, 115, 116])
XBQFYL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
XCHWDA = 45
XEKVKZ = 72
XFEFJT = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
XIBHZV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
XLSXUJ = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
XNKMLO = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
XNQTMF = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
XOIHBX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 51])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
XQVXOI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
XSJWMN = 31
XTIACQ = "".join(chr(c) for c in [78, 73, 71, 72, 84])
XUJUTY = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
XWAJVD = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
XYBQSN = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
YBQSNQ = 8
YEKCWA = "".join(chr(c) for c in [72, 105])
YFCRTF = "".join(chr(c) for c in [66, 76, 85, 69])
YGDSBD = 7
YIYWSK = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
YKLGQP = "".join(chr(c) for c in [78, 105, 103, 104, 116])
YLIUXF = "".join(
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
YLJUIK = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
YMOUNB = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
YNQJYM = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
YOUSPB = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
YXBQFY = 85
YYLIUX = 60
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
ZILXWA = 5
ZMJIGY = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
ZTATDZ = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
ZUQEXL = 27
ZVOACM = 62
ZXNQTM = 124
AJVDQL = [XWAJVD, WAJVDQ]
AKQXPI = [
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
    VLASSA,
    SSAKQX,
    SAKQXP,
]
BHZVOA = [KSOKPH]
BSIRYX = [AOAWBS, OAWBSI, VLASSA, VLASSA, VLASSA, VLASSA, AWBSIR, WBSIRY]
CPQIPO = [ACCPQI, CCPQIP]
DAFIKJ = [HWDAFI, WDAFIK, VLASSA, VLASSA]
EGZUQE = [MCBFEG, CBFEGZ, BFEGZU, FEGZUQ]
EKCWAO = [TYEKCW, YEKCWA]
EXLSXU = [UQEXLS, QEXLSX]
FJTACC = [JVHFTH, EFJTAC, PIPIVL]
FWRKIN = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, AWBSIR, WBSIRY]
HEOCTH = [
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
HZVOAC = []
IBHZVO = [BMJVHF, KQXPIC, XPICXQ, ICXQIE, RAHEOC, BSKSOK]
IGYOUS = [MJIGYO, JIGYOU]
IPOUYN = [PIPIVL, EFJTAC]
JUTYEK = [SXUJUT, XUJUTY, UJUTYE]
JZTATD = [RJZTAT, RTFMNH]
KLGQPL = [UYNQJY, YKLGQP]
LAIIDN = [VLASSA, DQLAII, QLAIID]
LKXSJW = [NBLKXS, BLKXSJ]
LNMHXE = [JVHFTH, UQEXLS, QLNMHX]
MJMAOA = [UYNQJY, AMJMAO]
NQJYMO = [UYNQJY, YNQJYM]
NRXCHW = [
    EUTOPH,
    UTOPHU,
    TOPHUG,
    OPHUGT,
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
]
NZMJIG = [WMNZMJ, MNZMJI]
QRJJJV = [DJQRJJ, JQRJJJ]
SOKPHU = [
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
    KSOKPH,
]
SOOQNR = [IUSOOQ, USOOQN]
SSUHBV = [UBSSUH, BSSUHB]
TBJEUT = [NHTBJE, HTBJEU]
TDZXNQ = [TATDZX, ATDZXN]
TFMNHT = [NIBXTI, JJVYFC, JVYFCR, VYFCRT, YFCRTF, FCRTFM, CRTFMN, RTFMNH]
TIACQF = [JVHFTH, NIBXTI, IBXTIA, BXTIAC, XTIACQ]
TSEMCG = [KEAKST, EAKSTS, AKSTSE, KSTSEM, STSEMC]
TSIFJB = [PFTSIF, FTSIFJ]
TTIDUB = [JVHFTH, FFTTID, FTTIDU]
WVUBYG = [BVWVUB, VWVUBY]
XQIEFX = [
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


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return ZVOACM

    @property
    def output_keys(self):
        return IBHZVO

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, AKQXPI, None, None, QBMJVH
            ),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, AKQXPI, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, AKQXPI, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, XQIEFX, None, None, QBMJVH
            ),
            QIEFXQ: GeckoByteStructAccessor(self.struct, QIEFXQ, IEFXQG, QBMJVH),
            EFXQGL: GeckoByteStructAccessor(self.struct, EFXQGL, FXQGLR, QBMJVH),
            XQGLRA: GeckoByteStructAccessor(self.struct, XQGLRA, QGLRAH, QBMJVH),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoEnumStructAccessor(
                self.struct, RAHEOC, AHEOCT, None, HEOCTH, None, None, QBMJVH
            ),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoBoolStructAccessor(
                self.struct, CTHBSK, THBSKS, HBSKSO, QBMJVH
            ),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, SKSOKP, None, SOKPHU, None, None, None
            ),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, None),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, QBMJVH),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, QBMJVH),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, QBMJVH),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, HIUSOO, OOQNRS, SOOQNR, None, HBSKSO, QBMJVH
            ),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, None, EGZUQE, None, None, QBMJVH
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, EXLSXU, None, None, QBMJVH
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, JUTYEK, None, None, QBMJVH
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, HIUSOO, HBSKSO, EKCWAO, None, HBSKSO, QBMJVH
            ),
            KCWAON: GeckoBoolStructAccessor(
                self.struct, KCWAON, THBSKS, CWAONP, QBMJVH
            ),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, QBMJVH),
            ONPYYL: GeckoByteStructAccessor(self.struct, ONPYYL, NPYYLI, QBMJVH),
            PYYLIU: GeckoByteStructAccessor(self.struct, PYYLIU, YYLIUX, QBMJVH),
            YLIUXF: GeckoByteStructAccessor(self.struct, YLIUXF, LIUXFE, QBMJVH),
            IUXFEF: GeckoByteStructAccessor(self.struct, IUXFEF, UXFEFJ, QBMJVH),
            XFEFJT: GeckoEnumStructAccessor(
                self.struct, XFEFJT, FEFJTA, None, FJTACC, None, None, QBMJVH
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, IPOUYN, None, None, QBMJVH
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, OUYNQJ, None, NQJYMO, None, None, QBMJVH
            ),
            QJYMOU: GeckoByteStructAccessor(self.struct, QJYMOU, JYMOUN, QBMJVH),
            YMOUNB: GeckoTempStructAccessor(self.struct, YMOUNB, MOUNBL, QBMJVH),
            OUNBLK: GeckoEnumStructAccessor(
                self.struct, OUNBLK, UNBLKX, None, LKXSJW, None, None, QBMJVH
            ),
            KXSJWM: GeckoEnumStructAccessor(
                self.struct, KXSJWM, XSJWMN, None, IPOUYN, None, None, QBMJVH
            ),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, NZMJIG, None, None, QBMJVH
            ),
            ZMJIGY: GeckoEnumStructAccessor(
                self.struct, ZMJIGY, HIUSOO, GYOUSP, IGYOUS, None, HBSKSO, QBMJVH
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
            BIAMJM: GeckoEnumStructAccessor(
                self.struct, BIAMJM, IAMJMA, None, MJMAOA, None, None, QBMJVH
            ),
            JMAOAW: GeckoEnumStructAccessor(
                self.struct, JMAOAW, MAOAWB, None, BSIRYX, None, None, QBMJVH
            ),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, IRYXBQ, None, BSIRYX, None, None, QBMJVH
            ),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, YXBQFY, None, BSIRYX, None, None, QBMJVH
            ),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, BSIRYX, None, None, QBMJVH
            ),
            QFYLJU: GeckoEnumStructAccessor(
                self.struct, QFYLJU, FYLJUI, None, BSIRYX, None, None, QBMJVH
            ),
            YLJUIK: GeckoByteStructAccessor(self.struct, YLJUIK, LJUIKF, QBMJVH),
            JUIKFW: GeckoByteStructAccessor(self.struct, JUIKFW, UIKFWR, QBMJVH),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, None, FWRKIN, None, None, QBMJVH
            ),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, RKINEJ, None, FWRKIN, None, None, QBMJVH
            ),
            KINEJN: GeckoByteStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoTimeStructAccessor(self.struct, NEJNIB, EJNIBX, QBMJVH),
            JNIBXY: GeckoTimeStructAccessor(self.struct, JNIBXY, NIBXYB, QBMJVH),
            IBXYBQ: GeckoTimeStructAccessor(self.struct, IBXYBQ, BXYBQS, QBMJVH),
            XYBQSN: GeckoTimeStructAccessor(self.struct, XYBQSN, YBQSNQ, QBMJVH),
            BQSNQL: GeckoTimeStructAccessor(self.struct, BQSNQL, QSNQLN, QBMJVH),
            SNQLNM: GeckoEnumStructAccessor(
                self.struct, SNQLNM, NQLNMH, None, LNMHXE, None, None, QBMJVH
            ),
            NMHXEK: GeckoBoolStructAccessor(
                self.struct, NMHXEK, MHXEKV, OOQNRS, QBMJVH
            ),
            HXEKVK: GeckoBoolStructAccessor(
                self.struct, HXEKVK, XEKVKZ, HBSKSO, QBMJVH
            ),
            EKVKZI: GeckoBoolStructAccessor(
                self.struct, EKVKZI, XEKVKZ, OOQNRS, QBMJVH
            ),
            KVKZIL: GeckoBoolStructAccessor(
                self.struct, KVKZIL, XEKVKZ, CWAONP, QBMJVH
            ),
            VKZILX: GeckoBoolStructAccessor(
                self.struct, VKZILX, XEKVKZ, GYOUSP, QBMJVH
            ),
            KZILXW: GeckoBoolStructAccessor(
                self.struct, KZILXW, XEKVKZ, ZILXWA, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, LXWAJV, None, AJVDQL, None, None, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, VDQLAI, None, LAIIDN, None, None, QBMJVH
            ),
            AIIDNI: GeckoByteStructAccessor(self.struct, AIIDNI, IIDNIB, QBMJVH),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, DNIBXT, None, TIACQF, None, None, QBMJVH
            ),
            IACQFF: GeckoTimeStructAccessor(self.struct, IACQFF, ACQFFT, QBMJVH),
            CQFFTT: GeckoEnumStructAccessor(
                self.struct, CQFFTT, QFFTTI, None, TTIDUB, None, None, QBMJVH
            ),
            TIDUBS: GeckoWordStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoEnumStructAccessor(
                self.struct, DUBSSU, HIUSOO, CWAONP, SSUHBV, None, HBSKSO, QBMJVH
            ),
            SUHBVW: GeckoBoolStructAccessor(
                self.struct, SUHBVW, HIUSOO, UHBVWV, QBMJVH
            ),
            HBVWVU: GeckoEnumStructAccessor(
                self.struct, HBVWVU, HIUSOO, ZILXWA, WVUBYG, None, HBSKSO, QBMJVH
            ),
            VUBYGD: GeckoBoolStructAccessor(
                self.struct, VUBYGD, HIUSOO, UBYGDS, QBMJVH
            ),
            BYGDSB: GeckoBoolStructAccessor(
                self.struct, BYGDSB, HIUSOO, YGDSBD, QBMJVH
            ),
            GDSBDJ: GeckoBoolStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, OOQNRS, QBMJVH
            ),
            SBDJQR: GeckoBoolStructAccessor(
                self.struct, SBDJQR, DSBDJQ, CWAONP, QBMJVH
            ),
            BDJQRJ: GeckoEnumStructAccessor(
                self.struct, BDJQRJ, DSBDJQ, HBSKSO, QRJJJV, None, HBSKSO, QBMJVH
            ),
            RJJJVY: GeckoEnumStructAccessor(
                self.struct, RJJJVY, DSBDJQ, GYOUSP, QRJJJV, None, HBSKSO, QBMJVH
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, DSBDJQ, UHBVWV, TFMNHT, None, FMNHTB, QBMJVH
            ),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, DSBDJQ, YGDSBD, TBJEUT, None, HBSKSO, QBMJVH
            ),
            RXCHWD: GeckoBoolStructAccessor(
                self.struct, RXCHWD, XCHWDA, CWAONP, QBMJVH
            ),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, XCHWDA, HBSKSO, DAFIKJ, None, UHBVWV, QBMJVH
            ),
            AFIKJP: GeckoBoolStructAccessor(
                self.struct, AFIKJP, XCHWDA, UHBVWV, QBMJVH
            ),
            FIKJPU: GeckoByteStructAccessor(self.struct, FIKJPU, IKJPUN, QBMJVH),
            KJPUNR: GeckoBoolStructAccessor(
                self.struct, KJPUNR, THBSKS, OOQNRS, QBMJVH
            ),
            JPUNRJ: GeckoByteStructAccessor(self.struct, JPUNRJ, PUNRJZ, QBMJVH),
            UNRJZT: GeckoEnumStructAccessor(
                self.struct, UNRJZT, NRJZTA, OOQNRS, JZTATD, None, HBSKSO, None
            ),
            ZTATDZ: GeckoEnumStructAccessor(
                self.struct, ZTATDZ, NRJZTA, CWAONP, TDZXNQ, None, HBSKSO, None
            ),
            DZXNQT: GeckoEnumStructAccessor(
                self.struct, DZXNQT, ZXNQTM, OOQNRS, JZTATD, None, HBSKSO, None
            ),
            XNQTMF: GeckoEnumStructAccessor(
                self.struct, XNQTMF, ZXNQTM, CWAONP, TDZXNQ, None, HBSKSO, None
            ),
            NQTMFZ: GeckoEnumStructAccessor(
                self.struct, NQTMFZ, QTMFZD, OOQNRS, JZTATD, None, HBSKSO, None
            ),
            TMFZDG: GeckoEnumStructAccessor(
                self.struct, TMFZDG, QTMFZD, CWAONP, TDZXNQ, None, HBSKSO, None
            ),
            MFZDGK: GeckoEnumStructAccessor(
                self.struct, MFZDGK, FZDGKE, OOQNRS, JZTATD, None, HBSKSO, None
            ),
            ZDGKEA: GeckoEnumStructAccessor(
                self.struct, ZDGKEA, FZDGKE, CWAONP, TDZXNQ, None, HBSKSO, None
            ),
            DGKEAK: GeckoEnumStructAccessor(
                self.struct, DGKEAK, GKEAKS, OOQNRS, TSEMCG, None, FMNHTB, None
            ),
            SEMCGE: GeckoBoolStructAccessor(self.struct, SEMCGE, GKEAKS, YGDSBD, None),
            EMCGET: GeckoBoolStructAccessor(self.struct, EMCGET, NRJZTA, UHBVWV, None),
            MCGETI: GeckoBoolStructAccessor(self.struct, MCGETI, NRJZTA, ZILXWA, None),
            CGETIX: GeckoBoolStructAccessor(self.struct, CGETIX, NRJZTA, UBYGDS, None),
            GETIXQ: GeckoBoolStructAccessor(self.struct, GETIXQ, NRJZTA, YGDSBD, None),
            ETIXQV: GeckoBoolStructAccessor(self.struct, ETIXQV, ZXNQTM, UHBVWV, None),
            TIXQVX: GeckoBoolStructAccessor(self.struct, TIXQVX, ZXNQTM, ZILXWA, None),
            IXQVXO: GeckoBoolStructAccessor(self.struct, IXQVXO, ZXNQTM, UBYGDS, None),
            XQVXOI: GeckoBoolStructAccessor(self.struct, XQVXOI, ZXNQTM, YGDSBD, None),
            QVXOIH: GeckoBoolStructAccessor(self.struct, QVXOIH, QTMFZD, UHBVWV, None),
            VXOIHB: GeckoBoolStructAccessor(self.struct, VXOIHB, QTMFZD, ZILXWA, None),
            XOIHBX: GeckoBoolStructAccessor(self.struct, XOIHBX, QTMFZD, UBYGDS, None),
            OIHBXI: GeckoBoolStructAccessor(self.struct, OIHBXI, QTMFZD, YGDSBD, None),
            IHBXIB: GeckoBoolStructAccessor(self.struct, IHBXIB, FZDGKE, UHBVWV, None),
            HBXIBH: GeckoBoolStructAccessor(self.struct, HBXIBH, FZDGKE, ZILXWA, None),
            BXIBHZ: GeckoBoolStructAccessor(self.struct, BXIBHZ, FZDGKE, UBYGDS, None),
            XIBHZV: GeckoBoolStructAccessor(self.struct, XIBHZV, FZDGKE, YGDSBD, None),
        }

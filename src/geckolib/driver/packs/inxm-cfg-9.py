#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v9'
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
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
ACMCVD = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
ACQFFT = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 50]
)
AFIKJP = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
AHEOCT = 107
AIIDNI = 5
AJVDQL = "".join(
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
AKQXPI = "".join(chr(c) for c in [86, 65, 76, 86, 69])
AKSTSE = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
AMJMAO = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
AONPYY = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
ASSAKQ = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
ATDZXN = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
AWBSIR = 12
BDJQRJ = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
BFEGZU = 104
BHZVOA = "".join(
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
BIAMJM = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
BJEUTO = 69
BLKXSJ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = 14
BQNRXC = "".join(chr(c) for c in [82, 69, 68])
BQSNQL = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
BSIRYX = 83
BSKSOK = "".join(chr(c) for c in [79, 117, 116, 52, 65])
BSSUHB = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
BVWVUB = 40
BWJYKL = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
BXIBHZ = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
BXTIAC = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 48]
)
BXYBQS = 87
BYGDSB = "".join(
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
CBFEGZ = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
CGETIX = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
CHWDAF = "".join(chr(c) for c in [67, 89, 65, 78])
CPQIPO = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
CQBMJV = 0
CQFFTT = 10
CRTFMN = "".join(chr(c) for c in [67, 104, 101, 99, 107, 71, 70, 67, 73])
CTHBSK = 109
CVDSSR = "".join(
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
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 26
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 50, 66])
DAFIKJ = 8
DGKEAK = "".join(chr(c) for c in [77, 65, 65, 88])
DJQRJJ = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
DNIBXT = 6
DNQGVU = 79
DQLAII = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
DSBDJQ = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
DUBSSU = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
DZXNQT = "".join(chr(c) for c in [67, 111, 97, 115, 116])
EAKSTS = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [67, 112, 79, 116, 79, 112, 116, 105, 111, 110])
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
EJNIBX = 85
EKCWAO = 61
EKVKZI = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
EMCGET = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
EOCTHB = 108
ETIXQV = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
EUTOPH = 70
EXLSXU = 4
FCRTFM = "".join(chr(c) for c in [80, 72])
FEFJTA = 4
FFTTID = 11
FIKJPU = 119
FJBIAM = "".join(chr(c) for c in [83, 97, 110, 105, 79, 110, 84, 105, 109, 101])
FJTACC = 23
FMNHTB = "".join(
    chr(c) for c in [82, 101, 112, 108, 97, 99, 101, 70, 105, 108, 116, 101, 114]
)
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
FTTIDU = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
FWRKIN = 1
FXQGLR = 102
FYLJUI = 5
FZDGKE = "".join(chr(c) for c in [76, 65])
GETIXQ = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
GKEAKS = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114])
GQPLSP = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
GSELHB = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
GTYIYW = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56])
GVUNXN = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
GZUQEX = 105
HBQNRX = "".join(chr(c) for c in [79, 70, 70])
HBSKSO = 110
HBVWVU = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
HBXIBH = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114])
HTBJEU = 68
HUGTYI = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55])
HUOJRJ = 101
HWDAFI = "".join(chr(c) for c in [87, 72, 73, 84, 69])
HXEKVK = "".join(
    chr(c) for c in [67, 69, 95, 50, 120, 50, 48, 65, 108, 108, 111, 119, 101, 100]
)
HZVOAC = 120
IACQFF = 9
IAMJMA = 15
IBHZVO = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
IBXTIA = 7
IBXYBQ = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
ICXQIE = 95
IDNIBX = "".join(
    chr(c)
    for c in [86, 83, 80, 67, 104, 101, 99, 107, 102, 108, 111, 83, 112, 101, 101, 100]
)
IDUBSS = 28
IEFXQG = 97
IFJBIA = 44
IGYOUS = "".join(chr(c) for c in [80, 49])
IHBXIB = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
IIDNIB = "".join(chr(c) for c in [80, 117, 109, 112, 51, 65, 115, 86, 83, 80])
IJUGSE = "".join(
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
IKFWRK = "".join(chr(c) for c in [53, 48, 72, 90])
IKJPUN = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
ILXWAJ = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
IPIVLA = "".join(chr(c) for c in [79, 51])
IRYXBQ = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
IUSOOQ = 112
IVDNQG = 78
IVLASS = "".join(chr(c) for c in [])
IXQVXO = "".join(chr(c) for c in [65, 115, 112, 101, 110])
IYWSKW = 75
JBIAMJ = 45
JEUTOP = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52])
JHIUSO = 111
JIGYOU = 117
JJJVYF = "".join(chr(c) for c in [75, 54, 48, 48, 70, 111, 114, 77, 97, 121])
JJVYFC = 7
JMAOAW = "".join(chr(c) for c in [67])
JMCBFE = "".join(chr(c) for c in [76, 73])
JNIBXY = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
JPUNRJ = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
JQRJJJ = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
JTACCP = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
JUGSEL = 118
JUIKFW = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
JUTYEK = "".join(chr(c) for c in [79, 119, 110])
JVDQLA = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49])
JWMNZM = 52
JYMOUN = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
JZTATD = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
KCWAON = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
KEAKST = "".join(chr(c) for c in [80, 68, 67])
KINEJN = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
KJPUNR = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
KLGQPL = 59
KMLOIJ = "".join(chr(c) for c in [50, 52, 104])
KPHUOJ = 100
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 53, 65])
KSTSEM = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
KVKZIL = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
KWIVDN = 77
KXSJWM = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
KZILXW = "".join(
    chr(c) for c in [67, 97, 110, 99, 101, 108, 79, 116, 104, 101, 114, 85, 68]
)
LAIIDN = "".join(chr(c) for c in [80, 117, 109, 112, 49, 65, 115, 86, 83, 80])
LASSAK = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
LGQPLS = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
LHBQNR = "".join(
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
LIUXFE = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
LJUIKF = 62
LKXSJW = 50
LNMHXE = 91
LOIJUG = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 69, 110, 97, 98, 108, 101]
)
LRAHEO = 106
LSPFTS = 58
LSXUJU = 2
LXWAJV = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
MAOAWB = "".join(chr(c) for c in [70])
MCGETI = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
MCVDSS = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
MFZDGK = "".join(chr(c) for c in [74, 97, 122, 122, 105])
MHXEKV = 92
MJIGYO = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
MJMAOA = 13
MJVHFT = 93
MNZMJI = 48
MOUNBL = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
NBLKXS = 49
NEJNIB = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
NHTBJE = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50])
NIBXTI = "".join(
    chr(c) for c in [86, 83, 80, 70, 105, 108, 116, 101, 114, 83, 112, 101, 101, 100]
)
NIBXYB = 86
NKMLOI = "".join(chr(c) for c in [65, 109, 80, 109])
NMHXEK = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
NQGVUN = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
NQLNMH = 90
NQTMFZ = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
NRJZTA = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
NRSJMC = 115
NRXCHW = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
NXNKML = 82
NZMJIG = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
OACMCV = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
OAWBSI = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114])
OIJUGS = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
OJRJHI = 116
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 54, 65])
ONPYYL = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
OOQNRS = "".join(chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114])
OPHUGT = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54])
OQNRSJ = 114
OUNBLK = 47
OUSPBW = 55
OUYNQJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
PFTSIF = 56
PHUGTY = 72
PHUOJR = "".join(chr(c) for c in [79, 117, 116, 55, 65])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 50, 65])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
POUYNQ = 6
PQIPOU = "".join(chr(c) for c in [65, 110, 121, 85, 68])
PUNRJZ = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
PYYLIU = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
QFFTTI = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 51]
)
QFYLJU = "".join(
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
QGVUNX = 80
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 51, 65])
QIPOUY = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
QJYMOU = 0
QLNMHX = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
QNRSJM = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
QNRXCH = "".join(chr(c) for c in [71, 82, 69, 69, 78])
QSNQLN = 89
QTMFZD = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
QVXOIH = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 49, 66])
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114])
RJHIUS = "".join(chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114])
RJJJVY = "".join(
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
RJZTAT = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
RKINEJ = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
RSJMCB = "".join(chr(c) for c in [79, 117, 116, 76, 105])
RTFMNH = "".join(chr(c) for c in [67, 104, 97, 110, 103, 101, 87, 97, 116, 101, 114])
RXCHWD = "".join(chr(c) for c in [66, 76, 85, 69])
SAKQXP = "".join(chr(c) for c in [79, 78, 90, 69, 78])
SBDJQR = "".join(
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
SELHBQ = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
SEMCGE = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
SIFJBI = "".join(chr(c) for c in [83, 97, 110, 105, 76, 101, 118, 101, 108])
SIRYXB = "".join(chr(c) for c in [78, 111])
SJMCBF = 103
SJWMNZ = "".join(
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
SKSOKP = 98
SKWIVD = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
SNQLNM = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
SOKPHU = 99
SOOQNR = 113
SPBWJY = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
SPFTSI = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
SRURAZ = 9
SSAKQX = "".join(chr(c) for c in [83, 65, 78, 73])
SSUHBV = 36
STSEMC = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
SUHBVW = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
SXUJUT = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
TACCPQ = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
TATDZX = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
TBJEUT = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51])
TDZXNQ = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
TFMNHT = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 111, 118, 101, 114])
THBSKS = "".join(chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 49]
)
TIDUBS = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
TIXQVX = "".join(chr(c) for c in [73, 100, 111, 108])
TMFZDG = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
TOPHUG = 71
TSEMCG = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
TSIFJB = 57
TTIDUB = 27
TYEKCW = 2
TYIYWS = 74
UBSSUH = 30
UBYGDS = 65
UGSELH = "".join(
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
UGTYIY = 73
UHBVWV = 38
UIKFWR = "".join(chr(c) for c in [54, 48, 72, 90])
UJUTYE = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
UNBLKX = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
UNRJZT = "".join(chr(c) for c in [65, 108, 112, 115])
UNXNKM = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
UOJRJH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
UQEXLS = 84
USOOQN = "".join(chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114])
USPBWJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
UTOPHU = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53])
UXFEFJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
UYNQJY = "".join(chr(c) for c in [76, 111])
VDNQGV = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
VDQLAI = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c) for c in [82, 101, 115, 116, 111, 114, 101, 65, 108, 108, 85, 68]
)
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VOACMC = 121
VUBYGD = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
VUNXNK = 81
VWVUBY = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
VXOIHB = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
VYFCRT = 67
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
WBSIRY = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
WIVDNQ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
WJYKLG = 54
WMNZMJ = "".join(
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
WRKINE = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
WSKWIV = 76
WVUBYG = 63
XBQFYL = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
XCHWDA = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
XEKVKZ = 60
XFEFJT = 25
XLSXUJ = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
XNKMLO = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
XNQTMF = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
XOIHBX = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
XPICXQ = 94
XQGLRA = "".join(chr(c) for c in [72, 84, 82])
XQIEFX = 96
XQVXOI = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
XSJWMN = 51
XTIACQ = 8
XUJUTY = 1
XWAJVD = "".join(chr(c) for c in [80, 97, 117, 115, 101])
XYBQSN = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
YBQSNQ = 88
YEKCWA = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
YFCRTF = "".join(chr(c) for c in [67, 108, 101, 97, 110, 70, 105, 108, 116, 101, 114])
YGDSBD = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
YIYWSK = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
YKLGQP = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
YLIUXF = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
YLJUIK = "".join(
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
YMOUNB = 46
YNQJYM = "".join(chr(c) for c in [72, 105])
YOUSPB = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
YXBQFY = 3
YYLIUX = 24
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
ZMJIGY = 53
ZTATDZ = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
ZUQEXL = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
ZVOACM = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
ZXNQTM = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
AOAWBS = [JMAOAW, MAOAWB]
CCPQIP = [JTACCP, TACCPQ, ACCPQI]
CMCVDS = [OACMCV, ACMCVD, IVLASS, IVLASS]
DSSRUR = [JMCBFE]
ELHBQN = [GSELHB, SELHBQ]
FEGZUQ = [
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
    JMCBFE,
    IVLASS,
    IVLASS,
    IVLASS,
    VLASSA,
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
]
GDSBDJ = [JVHFTH, YGDSBD]
GYOUSP = [JVHFTH, IGYOUS, PIPIVL]
INEJNI = [RKINEJ, KINEJN]
IPOUYN = [PQIPOU, QIPOUY]
IUXFEF = [YLIUXF, LIUXFE]
JRJHIU = [
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
JYKLGQ = [PIPIVL, IGYOUS]
KFWRKI = [UIKFWR, IKFWRK]
KQXPIC = [
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
    IVLASS,
    IVLASS,
    IVLASS,
    VLASSA,
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
]
MCBFEG = [
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
    JMCBFE,
]
MLOIJU = [NKMLOI, KMLOIJ]
MNHTBJ = [YFCRTF, FCRTFM, CRTFMN, RTFMNH, TFMNHT, FMNHTB]
NPYYLI = [WAONPY, AONPYY, ONPYYL]
NQJYMO = [UYNQJY, YNQJYM]
OIHBXI = [
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    NRJZTA,
    RJZTAT,
    JZTATD,
    ZTATDZ,
    TATDZX,
    ATDZXN,
    TDZXNQ,
    DZXNQT,
    ZXNQTM,
    XNQTMF,
    NQTMFZ,
    QTMFZD,
    TMFZDG,
    MFZDGK,
    FZDGKE,
    ZDGKEA,
    DGKEAK,
    GKEAKS,
    KEAKST,
    EAKSTS,
    AKSTSE,
    KSTSEM,
    STSEMC,
    TSEMCG,
    SEMCGE,
    EMCGET,
    MCGETI,
    CGETIX,
    GETIXQ,
    ETIXQV,
    TIXQVX,
    IXQVXO,
    XQVXOI,
    QVXOIH,
    VXOIHB,
    XOIHBX,
]
PBWJYK = [USPBWJ, SPBWJY]
QGLRAH = [
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
    XQGLRA,
]
QLAIID = [JVDQLA, VDQLAI, DQLAII, IVLASS]
QPLSPF = [LGQPLS, GQPLSP]
QRJJJV = [DJQRJJ, JQRJJJ]
RYXBQF = [SIRYXB, IRYXBQ]
SSRURA = []
UTYEKC = [UJUTYE, JUTYEK]
VDSSRU = [
    BMJVHF,
    QXPICX,
    PICXQI,
    CXQIEF,
    QIEFXQ,
    EFXQGL,
    BSKSOK,
    KSOKPH,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    RSJMCB,
    CBFEGZ,
    EGZUQE,
]
WAJVDQ = [LXWAJV, XWAJVD]
WDAFIK = [HBQNRX, BQNRXC, QNRXCH, NRXCHW, RXCHWD, XCHWDA, CHWDAF, HWDAFI]
XIBHZV = [HBXIBH, BXIBHZ]
ZILXWA = [KVKZIL, VKZILX, JVHFTH, KZILXW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return SRURAZ

    @property
    def output_keys(self):
        return VDSSRU

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, KQXPIC, None, None, QBMJVH
            ),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, None, KQXPIC, None, None, QBMJVH
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, KQXPIC, None, None, QBMJVH
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, KQXPIC, None, None, QBMJVH
            ),
            QIEFXQ: GeckoEnumStructAccessor(
                self.struct, QIEFXQ, IEFXQG, None, KQXPIC, None, None, QBMJVH
            ),
            EFXQGL: GeckoEnumStructAccessor(
                self.struct, EFXQGL, FXQGLR, None, QGLRAH, None, None, QBMJVH
            ),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoByteStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, QBMJVH),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, QBMJVH),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, SKSOKP, None, KQXPIC, None, None, QBMJVH
            ),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, KQXPIC, None, None, QBMJVH
            ),
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, KQXPIC, None, None, QBMJVH
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, None, KQXPIC, None, None, QBMJVH
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, JRJHIU, None, None, QBMJVH
            ),
            RJHIUS: GeckoByteStructAccessor(self.struct, RJHIUS, JHIUSO, QBMJVH),
            HIUSOO: GeckoByteStructAccessor(self.struct, HIUSOO, IUSOOQ, QBMJVH),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, QBMJVH),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, SJMCBF, None, MCBFEG, None, None, QBMJVH
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, None, FEGZUQ, None, None, QBMJVH
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, GZUQEX, None, FEGZUQ, None, None, QBMJVH
            ),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QBMJVH),
            QEXLSX: GeckoByteStructAccessor(self.struct, QEXLSX, EXLSXU, QBMJVH),
            XLSXUJ: GeckoByteStructAccessor(self.struct, XLSXUJ, LSXUJU, QBMJVH),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XUJUTY, TYEKCW, UTYEKC, None, TYEKCW, QBMJVH
            ),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, CWAONP, None, NPYYLI, None, None, QBMJVH
            ),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, YYLIUX, None, IUXFEF, None, None, QBMJVH
            ),
            UXFEFJ: GeckoBoolStructAccessor(
                self.struct, UXFEFJ, XFEFJT, FEFJTA, QBMJVH
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, None, CCPQIP, None, None, QBMJVH
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, XFEFJT, POUYNQ, IPOUYN, None, TYEKCW, QBMJVH
            ),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, XFEFJT, QJYMOU, NQJYMO, None, TYEKCW, QBMJVH
            ),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoByteStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoByteStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, QBMJVH),
            WMNZMJ: GeckoByteStructAccessor(self.struct, WMNZMJ, MNZMJI, QBMJVH),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoEnumStructAccessor(
                self.struct, MJIGYO, JIGYOU, None, GYOUSP, None, None, QBMJVH
            ),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, None, PBWJYK, None, None, QBMJVH
            ),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, JYKLGQ, None, None, QBMJVH
            ),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, QPLSPF, None, None, QBMJVH
            ),
            PLSPFT: GeckoByteStructAccessor(self.struct, PLSPFT, LSPFTS, QBMJVH),
            SPFTSI: GeckoEnumStructAccessor(
                self.struct, SPFTSI, PFTSIF, None, IPOUYN, None, None, QBMJVH
            ),
            FTSIFJ: GeckoByteStructAccessor(self.struct, FTSIFJ, TSIFJB, QBMJVH),
            SIFJBI: GeckoByteStructAccessor(self.struct, SIFJBI, IFJBIA, QBMJVH),
            FJBIAM: GeckoByteStructAccessor(self.struct, FJBIAM, JBIAMJ, QBMJVH),
            BIAMJM: GeckoTempStructAccessor(self.struct, BIAMJM, IAMJMA, QBMJVH),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, MJMAOA, TYEKCW, AOAWBS, None, TYEKCW, QBMJVH
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, JYKLGQ, None, None, QBMJVH
            ),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, BSIRYX, YXBQFY, RYXBQF, None, TYEKCW, QBMJVH
            ),
            XBQFYL: GeckoBoolStructAccessor(
                self.struct, XBQFYL, BQFYLJ, FEFJTA, QBMJVH
            ),
            QFYLJU: GeckoBoolStructAccessor(
                self.struct, QFYLJU, BQFYLJ, FYLJUI, QBMJVH
            ),
            YLJUIK: GeckoByteStructAccessor(self.struct, YLJUIK, LJUIKF, QBMJVH),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, BSIRYX, FWRKIN, KFWRKI, None, TYEKCW, QBMJVH
            ),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, BSIRYX, TYEKCW, INEJNI, None, TYEKCW, QBMJVH
            ),
            NEJNIB: GeckoByteStructAccessor(self.struct, NEJNIB, EJNIBX, None),
            JNIBXY: GeckoByteStructAccessor(self.struct, JNIBXY, NIBXYB, None),
            IBXYBQ: GeckoByteStructAccessor(self.struct, IBXYBQ, BXYBQS, None),
            XYBQSN: GeckoByteStructAccessor(self.struct, XYBQSN, YBQSNQ, QBMJVH),
            BQSNQL: GeckoByteStructAccessor(self.struct, BQSNQL, QSNQLN, QBMJVH),
            SNQLNM: GeckoByteStructAccessor(self.struct, SNQLNM, NQLNMH, QBMJVH),
            QLNMHX: GeckoByteStructAccessor(self.struct, QLNMHX, LNMHXE, QBMJVH),
            NMHXEK: GeckoByteStructAccessor(self.struct, NMHXEK, MHXEKV, QBMJVH),
            HXEKVK: GeckoBoolStructAccessor(
                self.struct, HXEKVK, XEKVKZ, POUYNQ, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, XEKVKZ, FWRKIN, ZILXWA, None, FEFJTA, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, XEKVKZ, QJYMOU, WAJVDQ, None, TYEKCW, QBMJVH
            ),
            AJVDQL: GeckoEnumStructAccessor(
                self.struct, AJVDQL, MJMAOA, YXBQFY, QLAIID, None, FEFJTA, QBMJVH
            ),
            LAIIDN: GeckoBoolStructAccessor(
                self.struct, LAIIDN, AIIDNI, QJYMOU, QBMJVH
            ),
            IIDNIB: GeckoBoolStructAccessor(
                self.struct, IIDNIB, AIIDNI, TYEKCW, QBMJVH
            ),
            IDNIBX: GeckoByteStructAccessor(self.struct, IDNIBX, DNIBXT, QBMJVH),
            NIBXTI: GeckoByteStructAccessor(self.struct, NIBXTI, IBXTIA, QBMJVH),
            BXTIAC: GeckoByteStructAccessor(self.struct, BXTIAC, XTIACQ, QBMJVH),
            TIACQF: GeckoByteStructAccessor(self.struct, TIACQF, IACQFF, QBMJVH),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, QBMJVH),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, QBMJVH),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, QBMJVH),
            TIDUBS: GeckoTimeStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoTimeStructAccessor(self.struct, DUBSSU, UBSSUH, QBMJVH),
            BSSUHB: GeckoTimeStructAccessor(self.struct, BSSUHB, SSUHBV, QBMJVH),
            SUHBVW: GeckoTimeStructAccessor(self.struct, SUHBVW, UHBVWV, QBMJVH),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, QBMJVH),
            VWVUBY: GeckoTimeStructAccessor(self.struct, VWVUBY, WVUBYG, QBMJVH),
            VUBYGD: GeckoTimeStructAccessor(self.struct, VUBYGD, UBYGDS, QBMJVH),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, XEKVKZ, FEFJTA, GDSBDJ, None, TYEKCW, QBMJVH
            ),
            DSBDJQ: GeckoBoolStructAccessor(
                self.struct, DSBDJQ, XEKVKZ, FYLJUI, QBMJVH
            ),
            SBDJQR: GeckoBoolStructAccessor(
                self.struct, SBDJQR, XEKVKZ, YXBQFY, QBMJVH
            ),
            BDJQRJ: GeckoEnumStructAccessor(
                self.struct, BDJQRJ, XUJUTY, QJYMOU, QRJJJV, None, TYEKCW, QBMJVH
            ),
            RJJJVY: GeckoBoolStructAccessor(
                self.struct, RJJJVY, XUJUTY, FWRKIN, QBMJVH
            ),
            XNKMLO: GeckoEnumStructAccessor(
                self.struct, XNKMLO, BSIRYX, QJYMOU, MLOIJU, None, TYEKCW, QBMJVH
            ),
            LOIJUG: GeckoBoolStructAccessor(
                self.struct, LOIJUG, BQFYLJ, QJYMOU, QBMJVH
            ),
            OIJUGS: GeckoBoolStructAccessor(
                self.struct, OIJUGS, XFEFJT, FWRKIN, QBMJVH
            ),
            IJUGSE: GeckoBoolStructAccessor(
                self.struct, IJUGSE, JUGSEL, QJYMOU, QBMJVH
            ),
            UGSELH: GeckoEnumStructAccessor(
                self.struct, UGSELH, JUGSEL, JJVYFC, ELHBQN, None, TYEKCW, QBMJVH
            ),
            LHBQNR: GeckoEnumStructAccessor(
                self.struct, LHBQNR, JUGSEL, FEFJTA, WDAFIK, None, DAFIKJ, QBMJVH
            ),
            IHBXIB: GeckoEnumStructAccessor(
                self.struct, IHBXIB, JUGSEL, TYEKCW, XIBHZV, None, TYEKCW, QBMJVH
            ),
            IBHZVO: GeckoEnumStructAccessor(
                self.struct, IBHZVO, JUGSEL, YXBQFY, XIBHZV, None, TYEKCW, QBMJVH
            ),
            BHZVOA: GeckoBoolStructAccessor(
                self.struct, BHZVOA, HZVOAC, QJYMOU, QBMJVH
            ),
            ZVOACM: GeckoEnumStructAccessor(
                self.struct, ZVOACM, VOACMC, TYEKCW, CMCVDS, None, FEFJTA, QBMJVH
            ),
            MCVDSS: GeckoByteStructAccessor(self.struct, MCVDSS, VOACMC, QBMJVH),
            CVDSSR: GeckoBoolStructAccessor(
                self.struct, CVDSSR, BSIRYX, FEFJTA, QBMJVH
            ),
        }

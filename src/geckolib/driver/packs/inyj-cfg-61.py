#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v61'
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
ACCPQI = 30
ACQFFT = 108
AFIKJP = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
AIIDNI = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 50])
AKSTSE = "".join(chr(c) for c in [51])
AMJMAO = "".join(chr(c) for c in [70, 51])
AOAWBS = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
AONPYY = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 116, 101, 99, 116, 105, 111, 110])
ATDZXN = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
AWBSIR = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
BDJQRJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
BFEGZU = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
BIAMJM = "".join(chr(c) for c in [70, 49])
BJEUTO = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
BLKXSJ = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
BQNRXC = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
BQSNQL = 10
BSIRYX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
BSKSOK = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
BSSUHB = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
BVWVUB = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
BWJYKL = 77
BXIBHZ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
BXTIAC = "".join(chr(c) for c in [83, 76, 69, 69, 80])
BXYBQS = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
BYGDSB = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
CBFEGZ = 27
CCPQIP = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
CGETIX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
CHWDAF = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
CPQIPO = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
CRTFMN = "".join(chr(c) for c in [67, 89, 65, 78])
CTHBSK = 79
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
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
EAKSTS = "".join(chr(c) for c in [50])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
EFXQGL = 37
EJNIBX = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
EKCWAO = "".join(
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
EKVKZI = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
ELHBQN = "".join(chr(c) for c in [65, 115, 112, 101, 110])
EMCGET = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
EOCTHB = 39
ETIXQV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
EUTOPH = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
EXLSXU = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
FCRTFM = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
FEGZUQ = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
FFTTID = "".join(chr(c) for c in [65, 109, 80, 109])
FIKJPU = 46
FJBIAM = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
FJTACC = 29
FMNHTB = 8
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
FTTIDU = "".join(chr(c) for c in [50, 52, 104])
FWRKIN = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
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
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
GKEAKS = 127
GLRAHE = 40
GQPLSP = "".join(chr(c) for c in [67, 69])
GSELHB = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
GTYIYW = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
GVUNXN = "".join(chr(c) for c in [77, 65, 65, 88])
GYOUSP = 68
GZUQEX = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
HBQNRX = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
HBVWVU = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
HBXIBH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 0
HTBJEU = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
HUGTYI = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
HUOJRJ = 56
HWDAFI = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
HXEKVK = 72
HZVOAC = 61
IACQFF = "".join(
    chr(c) for c in [83, 105, 108, 101, 110, 116, 68, 117, 114, 97, 116, 105, 111, 110]
)
IAMJMA = "".join(chr(c) for c in [70, 50])
IBXTIA = "".join(chr(c) for c in [69, 67, 79, 78, 79, 77, 89])
IBXYBQ = 23
ICXQIE = 16
IDNIBX = "".join(chr(c) for c in [83, 105, 108, 101, 110, 116, 77, 111, 100, 101])
IDUBSS = 64
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
IGYOUS = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IHBXIB = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
IIDNIB = 75
IJUGSE = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
IKFWRK = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
IKJPUN = "".join(
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
ILXWAJ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
INEJNI = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 63
IRYXBQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
IUSOOQ = 2
IUXFEF = 28
IVDNQG = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
IYWSKW = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
JBIAMJ = 83
JEUTOP = 44
JIGYOU = 66
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
JMAOAW = "".join(chr(c) for c in [76, 105, 110, 101, 50])
JNIBXY = 6
JPUNRJ = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
JQRJJJ = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
JRJHIU = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
JUGSEL = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
JUIKFW = 104
JUTYEK = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
JVDQLA = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [71, 82, 69, 69, 78])
JWMNZM = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
JYKLGQ = 26
KCWAON = 60
KEAKST = "".join(chr(c) for c in [49])
KFWRKI = 105
KINEJN = 3
KJPUNR = 47
KLGQPL = 51
KMLOIJ = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
KPHUOJ = 55
KQXPIC = 13
KSOKPH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KSTSEM = "".join(chr(c) for c in [52])
KVKZIL = 1
KWIVDN = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
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
LGQPLS = "".join(chr(c) for c in [85, 76])
LHBQNR = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
LIUXFE = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
LJUIKF = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
LKXSJW = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
LNMHXE = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
LOIJUG = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
LRAHEO = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
LSPFTS = 52
LSXUJU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
LXWAJV = 76
MCBFEG = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
MCGETI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
MFZDGK = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
MHXEKV = "".join(
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
MJIGYO = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
MJMAOA = "".join(chr(c) for c in [76, 105, 110, 101, 49])
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
MNZMJI = 3
MOUNBL = 31
NBLKXS = "".join(chr(c) for c in [105, 110, 70, 108, 111])
NEJNIB = 4
NHTBJE = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
NIBXTI = "".join(chr(c) for c in [79, 70, 70])
NIBXYB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
NKMLOI = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
NMHXEK = 82
NPYYLI = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
NQGVUN = "".join(chr(c) for c in [76, 65])
NQJYMO = "".join(chr(c) for c in [70])
NQLNMH = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
NQTMFZ = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
NRJZTA = 123
NRSJMC = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
NXNKML = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
NZMJIG = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
OAWBSI = 84
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 76, 105])
OIHBXI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
OIJUGS = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
OJRJHI = 81
OKPHUO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
ONPYYL = 62
OOQNRS = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
OPHUGT = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
OQNRSJ = 32
OUNBLK = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
OUSPBW = 70
OUYNQJ = 1
PBWJYK = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
PFTSIF = 53
PHUGTY = "".join(chr(c) for c in [65, 108, 112, 115])
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
POUYNQ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
PUNRJZ = 121
PYYLIU = 78
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
QFFTTI = 34
QFYLJU = 99
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
QGVUNX = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
QIEFXQ = 36
QIPOUY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
QJYMOU = "".join(chr(c) for c in [67])
QLAIID = "".join(chr(c) for c in [83, 108, 97, 118, 101])
QNRSJM = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
QNRXCH = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
QSNQLN = "".join(
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
QTMFZD = 125
QVXOIH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
QXPICX = "".join(chr(c) for c in [79, 117, 116, 51])
RAHEOC = 15
RJHIUS = "".join(chr(c) for c in [79, 119, 110])
RJJJVY = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
RJZTAT = "".join(chr(c) for c in [82, 71, 66])
RKINEJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
RSJMCB = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
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
RYXBQF = 87
SBDJQR = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
SELHBQ = "".join(chr(c) for c in [73, 100, 111, 108])
SEMCGE = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
SIFJBI = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
SIRYXB = 86
SJMCBF = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
SJWMNZ = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
SKSOKP = 80
SKWIVD = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
SNQLNM = 71
SOKPHU = 54
SOOQNR = 48
SPFTSI = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
SSAKQX = "".join(chr(c) for c in [65, 85, 88])
SUHBVW = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
SXUJUT = "".join(chr(c) for c in [76, 111])
TACCPQ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
TATDZX = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
THBSKS = "".join(chr(c) for c in [76, 73])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIDUBS = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
TIXQVX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
TMFZDG = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
TOPHUG = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
TSEMCG = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
TSIFJB = 74
TYEKCW = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
TYIYWS = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
UBSSUH = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
UBYGDS = 6
UGSELH = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
UGTYIY = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
UHBVWV = 4
UNBLKX = 25
UNRJZT = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
UNXNKM = "".join(chr(c) for c in [80, 68, 67])
UOJRJH = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
UQEXLS = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
USOOQN = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
USPBWJ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
UTOPHU = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
UTYEKC = 58
UXFEFJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
UYNQJY = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
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
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
VYFCRT = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
WAONPY = 61
WBSIRY = 85
WDAFIK = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
WIVDNQ = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
WJYKLG = "".join(
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
WRKINE = 106
WSKWIV = "".join(chr(c) for c in [67, 111, 97, 115, 116])
XBQFYL = 98
XCHWDA = 45
XEKVKZ = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
XFEFJT = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
XNKMLO = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
XNQTMF = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
XOIHBX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
XPICXQ = 14
XQGLRA = 38
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
XQVXOI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
XSJWMN = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
XTIACQ = "".join(chr(c) for c in [78, 73, 71, 72, 84])
XUJUTY = "".join(chr(c) for c in [72, 105])
XWAJVD = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
XYBQSN = 8
YBQSNQ = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
YEKCWA = 59
YFCRTF = "".join(chr(c) for c in [66, 76, 85, 69])
YGDSBD = 7
YIYWSK = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
YKLGQP = "".join(chr(c) for c in [85, 76, 95, 67, 69])
YLJUIK = 100
YMOUNB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
YNQJYM = 33
YOUSPB = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
YXBQFY = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
YYLIUX = "".join(chr(c) for c in [80, 49])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
ZILXWA = 5
ZMJIGY = 35
ZTATDZ = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
ZUQEXL = 57
ZXNQTM = 124
AHEOCT = [
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
AJVDQL = [XWAJVD, WAJVDQ]
BHZVOA = []
CXQIEF = [
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
DAFIKJ = [HWDAFI, WDAFIK, VLASSA, VLASSA]
EGZUQE = [BFEGZU, FEGZUQ]
FEFJTA = [UXFEFJ, XFEFJT]
HBSKSO = [
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
    THBSKS,
]
IBHZVO = [THBSKS]
IFJBIA = [CCPQIP, SIFJBI]
JHIUSO = [JRJHIU, RJHIUS]
JMCBFE = [QNRSJM, NRSJMC, RSJMCB, SJMCBF]
JTACCP = [PIPIVL, YYLIUX]
JYMOUN = [NQJYMO, QJYMOU]
JZTATD = [RJZTAT, RTFMNH]
KXSJWM = [NBLKXS, BLKXSJ, LKXSJW]
LAIIDN = [VLASSA, DQLAII, QLAIID]
MAOAWB = [BIAMJM, IAMJMA, AMJMAO, VLASSA, VLASSA, VLASSA, MJMAOA, JMAOAW]
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
PQIPOU = [CCPQIP, CPQIPO]
QLNMHX = [JVHFTH, BFEGZU, NQLNMH]
QPLSPF = [LGQPLS, GQPLSP]
QRJJJV = [DJQRJJ, JQRJJJ]
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
    ASSAKQ,
    VLASSA,
    VLASSA,
    SSAKQX,
]
SPBWJY = [CCPQIP, USPBWJ]
SSUHBV = [UBSSUH, BSSUHB]
STSEMC = [VLASSA, KEAKST, EAKSTS, AKSTSE, KSTSEM]
TBJEUT = [NHTBJE, HTBJEU]
TDZXNQ = [TATDZX, ATDZXN]
TFMNHT = [NIBXTI, JJVYFC, JVYFCR, VYFCRT, YFCRTF, FCRTFM, CRTFMN, RTFMNH]
TIACQF = [JVHFTH, NIBXTI, IBXTIA, BXTIAC, XTIACQ]
TTIDUB = [JVHFTH, FFTTID, FTTIDU]
UIKFWR = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, MJMAOA, JMAOAW]
UJUTYE = [SXUJUT, XUJUTY]
WMNZMJ = [SJWMNZ, JWMNZM]
WVUBYG = [BVWVUB, VWVUBY]
XIBHZV = [BMJVHF, AKQXPI, QXPICX, PICXQI, LRAHEO, OCTHBS]
XLSXUJ = [UQEXLS, QEXLSX, EXLSXU]
YLIUXF = [JVHFTH, YYLIUX, PIPIVL]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return HZVOAC

    @property
    def output_keys(self):
        return XIBHZV

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
                self.struct, PICXQI, ICXQIE, None, CXQIEF, None, None, QBMJVH
            ),
            XQIEFX: GeckoByteStructAccessor(self.struct, XQIEFX, QIEFXQ, QBMJVH),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoEnumStructAccessor(
                self.struct, LRAHEO, RAHEOC, None, AHEOCT, None, None, QBMJVH
            ),
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoEnumStructAccessor(
                self.struct, OCTHBS, CTHBSK, None, HBSKSO, None, None, None
            ),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, None),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, QBMJVH),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, QBMJVH),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, QBMJVH),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, HIUSOO, JHIUSO, None, IUSOOQ, QBMJVH
            ),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, OQNRSJ, None, JMCBFE, None, None, QBMJVH
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, EGZUQE, None, None, QBMJVH
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, XLSXUJ, None, None, QBMJVH
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, OJRJHI, IUSOOQ, UJUTYE, None, IUSOOQ, QBMJVH
            ),
            JUTYEK: GeckoByteStructAccessor(self.struct, JUTYEK, UTYEKC, QBMJVH),
            TYEKCW: GeckoByteStructAccessor(self.struct, TYEKCW, YEKCWA, QBMJVH),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, YLIUXF, None, None, QBMJVH
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, FEFJTA, None, None, QBMJVH
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, None, JTACCP, None, None, QBMJVH
            ),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, None, PQIPOU, None, None, QBMJVH
            ),
            QIPOUY: GeckoByteStructAccessor(self.struct, QIPOUY, IPOUYN, QBMJVH),
            POUYNQ: GeckoTempStructAccessor(self.struct, POUYNQ, OUYNQJ, QBMJVH),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, JYMOUN, None, None, QBMJVH
            ),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, MOUNBL, None, JTACCP, None, None, QBMJVH
            ),
            OUNBLK: GeckoEnumStructAccessor(
                self.struct, OUNBLK, UNBLKX, None, KXSJWM, None, None, QBMJVH
            ),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, OJRJHI, MNZMJI, WMNZMJ, None, IUSOOQ, QBMJVH
            ),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoTempStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoTempStructAccessor(self.struct, IGYOUS, GYOUSP, QBMJVH),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, None, SPBWJY, None, None, QBMJVH
            ),
            PBWJYK: GeckoByteStructAccessor(self.struct, PBWJYK, BWJYKL, QBMJVH),
            WJYKLG: GeckoByteStructAccessor(self.struct, WJYKLG, JYKLGQ, QBMJVH),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, QPLSPF, None, None, QBMJVH
            ),
            PLSPFT: GeckoByteStructAccessor(self.struct, PLSPFT, LSPFTS, QBMJVH),
            SPFTSI: GeckoByteStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, TSIFJB, None, IFJBIA, None, None, QBMJVH
            ),
            FJBIAM: GeckoEnumStructAccessor(
                self.struct, FJBIAM, JBIAMJ, None, MAOAWB, None, None, QBMJVH
            ),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, None, MAOAWB, None, None, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, MAOAWB, None, None, QBMJVH
            ),
            BSIRYX: GeckoEnumStructAccessor(
                self.struct, BSIRYX, SIRYXB, None, MAOAWB, None, None, QBMJVH
            ),
            IRYXBQ: GeckoEnumStructAccessor(
                self.struct, IRYXBQ, RYXBQF, None, MAOAWB, None, None, QBMJVH
            ),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoByteStructAccessor(self.struct, BQFYLJ, QFYLJU, QBMJVH),
            FYLJUI: GeckoByteStructAccessor(self.struct, FYLJUI, YLJUIK, QBMJVH),
            LJUIKF: GeckoEnumStructAccessor(
                self.struct, LJUIKF, JUIKFW, None, UIKFWR, None, None, QBMJVH
            ),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, None, UIKFWR, None, None, QBMJVH
            ),
            FWRKIN: GeckoEnumStructAccessor(
                self.struct, FWRKIN, WRKINE, None, UIKFWR, None, None, QBMJVH
            ),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, QBMJVH),
            INEJNI: GeckoTimeStructAccessor(self.struct, INEJNI, NEJNIB, QBMJVH),
            EJNIBX: GeckoTimeStructAccessor(self.struct, EJNIBX, JNIBXY, QBMJVH),
            NIBXYB: GeckoTimeStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoTimeStructAccessor(self.struct, BXYBQS, XYBQSN, QBMJVH),
            YBQSNQ: GeckoTimeStructAccessor(self.struct, YBQSNQ, BQSNQL, QBMJVH),
            QSNQLN: GeckoEnumStructAccessor(
                self.struct, QSNQLN, SNQLNM, None, QLNMHX, None, None, QBMJVH
            ),
            LNMHXE: GeckoBoolStructAccessor(
                self.struct, LNMHXE, NMHXEK, HIUSOO, QBMJVH
            ),
            MHXEKV: GeckoBoolStructAccessor(
                self.struct, MHXEKV, HXEKVK, IUSOOQ, QBMJVH
            ),
            XEKVKZ: GeckoBoolStructAccessor(
                self.struct, XEKVKZ, HXEKVK, HIUSOO, QBMJVH
            ),
            EKVKZI: GeckoBoolStructAccessor(
                self.struct, EKVKZI, HXEKVK, KVKZIL, QBMJVH
            ),
            VKZILX: GeckoBoolStructAccessor(
                self.struct, VKZILX, HXEKVK, MNZMJI, QBMJVH
            ),
            KZILXW: GeckoBoolStructAccessor(
                self.struct, KZILXW, HXEKVK, ZILXWA, QBMJVH
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
                self.struct, DUBSSU, OJRJHI, KVKZIL, SSUHBV, None, IUSOOQ, QBMJVH
            ),
            SUHBVW: GeckoBoolStructAccessor(
                self.struct, SUHBVW, OJRJHI, UHBVWV, QBMJVH
            ),
            HBVWVU: GeckoEnumStructAccessor(
                self.struct, HBVWVU, OJRJHI, ZILXWA, WVUBYG, None, IUSOOQ, QBMJVH
            ),
            VUBYGD: GeckoBoolStructAccessor(
                self.struct, VUBYGD, OJRJHI, UBYGDS, QBMJVH
            ),
            BYGDSB: GeckoBoolStructAccessor(
                self.struct, BYGDSB, OJRJHI, YGDSBD, QBMJVH
            ),
            GDSBDJ: GeckoBoolStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, HIUSOO, QBMJVH
            ),
            SBDJQR: GeckoBoolStructAccessor(
                self.struct, SBDJQR, DSBDJQ, KVKZIL, QBMJVH
            ),
            BDJQRJ: GeckoEnumStructAccessor(
                self.struct, BDJQRJ, DSBDJQ, IUSOOQ, QRJJJV, None, IUSOOQ, QBMJVH
            ),
            RJJJVY: GeckoEnumStructAccessor(
                self.struct, RJJJVY, DSBDJQ, MNZMJI, QRJJJV, None, IUSOOQ, QBMJVH
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, DSBDJQ, UHBVWV, TFMNHT, None, FMNHTB, QBMJVH
            ),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, DSBDJQ, YGDSBD, TBJEUT, None, IUSOOQ, QBMJVH
            ),
            RXCHWD: GeckoBoolStructAccessor(
                self.struct, RXCHWD, XCHWDA, KVKZIL, QBMJVH
            ),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, XCHWDA, IUSOOQ, DAFIKJ, None, UHBVWV, QBMJVH
            ),
            AFIKJP: GeckoByteStructAccessor(self.struct, AFIKJP, FIKJPU, QBMJVH),
            IKJPUN: GeckoBoolStructAccessor(
                self.struct, IKJPUN, KJPUNR, HIUSOO, QBMJVH
            ),
            JPUNRJ: GeckoByteStructAccessor(self.struct, JPUNRJ, PUNRJZ, QBMJVH),
            UNRJZT: GeckoEnumStructAccessor(
                self.struct, UNRJZT, NRJZTA, HIUSOO, JZTATD, None, IUSOOQ, None
            ),
            ZTATDZ: GeckoEnumStructAccessor(
                self.struct, ZTATDZ, NRJZTA, KVKZIL, TDZXNQ, None, IUSOOQ, None
            ),
            DZXNQT: GeckoEnumStructAccessor(
                self.struct, DZXNQT, ZXNQTM, HIUSOO, JZTATD, None, IUSOOQ, None
            ),
            XNQTMF: GeckoEnumStructAccessor(
                self.struct, XNQTMF, ZXNQTM, KVKZIL, TDZXNQ, None, IUSOOQ, None
            ),
            NQTMFZ: GeckoEnumStructAccessor(
                self.struct, NQTMFZ, QTMFZD, HIUSOO, JZTATD, None, IUSOOQ, None
            ),
            TMFZDG: GeckoEnumStructAccessor(
                self.struct, TMFZDG, QTMFZD, KVKZIL, TDZXNQ, None, IUSOOQ, None
            ),
            MFZDGK: GeckoEnumStructAccessor(
                self.struct, MFZDGK, FZDGKE, HIUSOO, JZTATD, None, IUSOOQ, None
            ),
            ZDGKEA: GeckoEnumStructAccessor(
                self.struct, ZDGKEA, FZDGKE, KVKZIL, TDZXNQ, None, IUSOOQ, None
            ),
            DGKEAK: GeckoEnumStructAccessor(
                self.struct, DGKEAK, GKEAKS, HIUSOO, STSEMC, None, FMNHTB, None
            ),
            TSEMCG: GeckoBoolStructAccessor(self.struct, TSEMCG, GKEAKS, YGDSBD, None),
            SEMCGE: GeckoBoolStructAccessor(self.struct, SEMCGE, NRJZTA, UHBVWV, None),
            EMCGET: GeckoBoolStructAccessor(self.struct, EMCGET, NRJZTA, ZILXWA, None),
            MCGETI: GeckoBoolStructAccessor(self.struct, MCGETI, NRJZTA, UBYGDS, None),
            CGETIX: GeckoBoolStructAccessor(self.struct, CGETIX, NRJZTA, YGDSBD, None),
            GETIXQ: GeckoBoolStructAccessor(self.struct, GETIXQ, ZXNQTM, UHBVWV, None),
            ETIXQV: GeckoBoolStructAccessor(self.struct, ETIXQV, ZXNQTM, ZILXWA, None),
            TIXQVX: GeckoBoolStructAccessor(self.struct, TIXQVX, ZXNQTM, UBYGDS, None),
            IXQVXO: GeckoBoolStructAccessor(self.struct, IXQVXO, ZXNQTM, YGDSBD, None),
            XQVXOI: GeckoBoolStructAccessor(self.struct, XQVXOI, QTMFZD, UHBVWV, None),
            QVXOIH: GeckoBoolStructAccessor(self.struct, QVXOIH, QTMFZD, ZILXWA, None),
            VXOIHB: GeckoBoolStructAccessor(self.struct, VXOIHB, QTMFZD, UBYGDS, None),
            XOIHBX: GeckoBoolStructAccessor(self.struct, XOIHBX, QTMFZD, YGDSBD, None),
            OIHBXI: GeckoBoolStructAccessor(self.struct, OIHBXI, FZDGKE, UHBVWV, None),
            IHBXIB: GeckoBoolStructAccessor(self.struct, IHBXIB, FZDGKE, ZILXWA, None),
            HBXIBH: GeckoBoolStructAccessor(self.struct, HBXIBH, FZDGKE, UBYGDS, None),
            BXIBHZ: GeckoBoolStructAccessor(self.struct, BXIBHZ, FZDGKE, YGDSBD, None),
        }

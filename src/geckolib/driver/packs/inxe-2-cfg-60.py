#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE-2 v60'
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
ACQFFT = "".join(chr(c) for c in [65, 109, 80, 109])
AFIKJP = "".join(
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
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
AJVDQL = "".join(
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
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 50])
AMJMAO = "".join(chr(c) for c in [70, 50])
AONPYY = "".join(chr(c) for c in [72, 105])
ASSAKQ = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
ATDZXN = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
AWBSIR = 84
BFEGZU = 48
BIAMJM = 83
BJEUTO = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
BLKXSJ = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 88
BQNRXC = "".join(
    chr(c)
    for c in [
        81,
        117,
        105,
        99,
        107,
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
BQSNQL = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
BSIRYX = 85
BSKSOK = 17
BSSUHB = 4
BVWVUB = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
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
BXTIAC = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
BXYBQS = 4
BYGDSB = 43
CBFEGZ = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
CCPQIP = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
CHWDAF = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
CPQIPO = 28
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [50, 52, 104])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 53])
DAFIKJ = 46
DGKEAK = "".join(chr(c) for c in [49])
DJQRJJ = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
DNIBXT = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
DNQGVU = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
DQLAII = 76
DSBDJQ = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
DZXNQT = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
EAKSTS = "".join(chr(c) for c in [52])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 62
EGZUQE = 32
EJNIBX = 106
EKCWAO = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
EKVKZI = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
ELHBQN = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
EUTOPH = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
FCRTFM = "".join(chr(c) for c in [87, 72, 73, 84, 69])
FEFJTA = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
FEGZUQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
FFTTID = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
FIKJPU = 47
FJTACC = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
FMNHTB = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 122
FTTIDU = 64
FWRKIN = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
FYLJUI = 89
FZDGKE = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
GDSBDJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
GKEAKS = "".join(chr(c) for c in [50])
GLRAHE = 37
GSELHB = "".join(chr(c) for c in [65, 115, 112, 101, 110])
GTYIYW = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
GVUNXN = "".join(chr(c) for c in [80, 68, 67])
GYOUSP = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
GZUQEX = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
HBSKSO = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 39
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 55
HTBJEU = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
HUGTYI = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
HXEKVK = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
IACQFF = 34
IAMJMA = "".join(chr(c) for c in [70, 49])
IBXYBQ = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
ICXQIE = 15
IDNIBX = 73
IDUBSS = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
IEFXQG = 18
IFJBIA = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
IGYOUS = 68
IIDNIB = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
IJUGSE = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
IKFWRK = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
IKJPUN = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
ILXWAJ = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
INEJNI = 105
IPIVLA = "".join(chr(c) for c in [79, 51])
IRYXBQ = 86
IUSOOQ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
IUXFEF = 60
IVDNQG = "".join(chr(c) for c in [74, 97, 122, 122, 105])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = "".join(chr(c) for c in [67, 111, 97, 115, 116])
JBIAMJ = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
JEUTOP = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
JHIUSO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
JIGYOU = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
JJJVYF = "".join(chr(c) for c in [71, 82, 69, 69, 78])
JJVYFC = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
JMAOAW = "".join(chr(c) for c in [76, 105, 110, 101, 49])
JMCBFE = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
JNIBXY = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
JPUNRJ = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
JQRJJJ = "".join(
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
JRJHIU = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
JTACCP = 78
JUGSEL = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
JUIKFW = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
JUTYEK = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
JVDQLA = 5
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [66, 76, 85, 69])
JWMNZM = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
JYKLGQ = "".join(chr(c) for c in [85, 76, 95, 67, 69])
JYMOUN = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
JZTATD = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
KEAKST = "".join(chr(c) for c in [51])
KFWRKI = 100
KINEJN = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
KJPUNR = 121
KLGQPL = "".join(chr(c) for c in [85, 76])
KMLOIJ = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
KPHUOJ = 79
KQXPIC = 13
KSOKPH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
KVKZIL = 82
KWIVDN = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
KXSJWM = "".join(chr(c) for c in [70])
KZILXW = 72
LAIIDN = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(chr(c) for c in [67, 69])
LHBQNR = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
LIUXFE = "".join(
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
LJUIKF = 98
LKXSJW = 33
LNMHXE = 10
LOIJUG = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
LSPFTS = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
LSXUJU = 27
LXWAJV = 1
MAOAWB = "".join(chr(c) for c in [76, 105, 110, 101, 50])
MCBFEG = 118
MFZDGK = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
MHXEKV = 71
MJIGYO = 66
MJMAOA = "".join(chr(c) for c in [70, 51])
MJVHFT = 12
MLOIJU = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
MNHTBJ = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
MNZMJI = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
MOUNBL = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
NBLKXS = 1
NEJNIB = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
NIBXTI = "".join(chr(c) for c in [83, 108, 97, 118, 101])
NIBXYB = 3
NKMLOI = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
NMHXEK = "".join(
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
NPYYLI = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
NQGVUN = "".join(chr(c) for c in [77, 65, 65, 88])
NQJYMO = 30
NQLNMH = 8
NQTMFZ = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
NRXCHW = "".join(
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
NXNKML = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
NZMJIG = 35
OAWBSI = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
OCTHBS = 40
OIJUGS = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
OJRJHI = 80
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 76, 105])
OOQNRS = 81
OPHUGT = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
OQNRSJ = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OUNBLK = 63
OUSPBW = "".join(chr(c) for c in [78, 105, 103, 104, 116])
OUYNQJ = 29
PBWJYK = 77
PFTSIF = "".join(
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
PHUGTY = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
PHUOJR = "".join(chr(c) for c in [76, 73])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 52])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 52
POUYNQ = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
PQIPOU = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
PUNRJZ = 123
PYYLIU = 58
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
QFYLJU = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
QGVUNX = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
QIPOUY = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
QJYMOU = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
QLAIID = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
QLNMHX = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
QNRSJM = "".join(chr(c) for c in [79, 119, 110])
QNRXCH = 45
QPLSPF = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
QRJJJV = "".join(chr(c) for c in [79, 70, 70])
QSNQLN = 23
QTMFZD = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 51])
RAHEOC = 38
RJHIUS = 54
RJJJVY = "".join(chr(c) for c in [82, 69, 68])
RJZTAT = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
RSJMCB = 0
RTFMNH = 8
RXCHWD = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
RYXBQF = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
SBDJQR = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
SELHBQ = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
SEMCGE = 60
SIFJBI = 74
SIRYXB = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
SJMCBF = 2
SKWIVD = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
SNQLNM = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
SOKPHU = 41
SOOQNR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
SPBWJY = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
SPFTSI = 53
SSAKQX = "".join(chr(c) for c in [65, 85, 88])
SSUHBV = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
SUHBVW = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
SXUJUT = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
TACCPQ = "".join(chr(c) for c in [80, 49])
TBJEUT = 44
TDZXNQ = 124
TFMNHT = "".join(
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
THBSKS = 42
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
TIDUBS = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
TMFZDG = 126
TOPHUG = "".join(chr(c) for c in [65, 108, 112, 115])
TSIFJB = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
TTIDUB = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
TYEKCW = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
TYIYWS = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
UBSSUH = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
UBYGDS = "".join(
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
UGSELH = "".join(chr(c) for c in [73, 100, 111, 108])
UGTYIY = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
UHBVWV = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
UIKFWR = 99
UNBLKX = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
UNRJZT = "".join(chr(c) for c in [82, 71, 66])
UNXNKM = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
UOJRJH = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UQEXLS = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
USOOQN = 56
UTOPHU = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
UTYEKC = 57
UXFEFJ = "".join(
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
VDNQGV = "".join(chr(c) for c in [76, 65])
VDQLAI = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
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
VLASSA = "".join(chr(c) for c in [])
VUBYGD = 7
VUNXNK = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
VWVUBY = 6
VYFCRT = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 3
WAONPY = "".join(chr(c) for c in [76, 111])
WBSIRY = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
WDAFIK = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
WIVDNQ = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
WJYKLG = 26
WMNZMJ = 31
WRKINE = 104
WSKWIV = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
WVUBYG = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
XBQFYL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 70, 117, 115, 101])
XCHWDA = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
XFEFJT = 61
XLSXUJ = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
XNKMLO = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
XNQTMF = 125
XPICXQ = 14
XQGLRA = 36
XQIEFX = 16
XSJWMN = "".join(chr(c) for c in [67])
XTIACQ = 75
XUJUTY = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
XWAJVD = "".join(
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
XYBQSN = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
YBQSNQ = 6
YEKCWA = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
YFCRTF = "".join(chr(c) for c in [67, 89, 65, 78])
YGDSBD = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
YIYWSK = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
YKLGQP = 51
YLIUXF = 59
YLJUIK = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
YNQJYM = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
YOUSPB = 70
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
YXBQFY = 87
YYLIUX = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = 127
ZILXWA = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
ZMJIGY = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
ZTATDZ = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
ZUQEXL = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
ZXNQTM = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
ACCPQI = [JVHFTH, TACCPQ, PIPIVL]
AIIDNI = [QLAIID, LAIIDN]
AKSTSE = [VLASSA, DGKEAK, GKEAKS, KEAKST, EAKSTS]
AOAWBS = [IAMJMA, AMJMAO, MJMAOA, VLASSA, VLASSA, VLASSA, JMAOAW, MAOAWB]
BDJQRJ = [DSBDJQ, SBDJQR]
CRTFMN = [QRJJJV, RJJJVY, JJJVYF, JJVYFC, JVYFCR, VYFCRT, YFCRTF, FCRTFM]
DUBSSU = [TIDUBS, IDUBSS]
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
EXLSXU = [GZUQEX, ZUQEXL, UQEXLS, QEXLSX]
FJBIAM = [QJYMOU, IFJBIA]
GQPLSP = [KLGQPL, LGQPLS]
HBQNRX = [
    BJEUTO,
    JEUTOP,
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
]
HBVWVU = [SUHBVW, UHBVWV]
HUOJRJ = [
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
    PHUOJR,
]
HWDAFI = [XCHWDA, CHWDAF, VLASSA, VLASSA]
IBXTIA = [VLASSA, DNIBXT, NIBXTI]
IPOUYN = [PQIPOU, QIPOUY]
KCWAON = [TYEKCW, YEKCWA, EKCWAO]
KSTSEM = [BMJVHF, AKQXPI, QXPICX, PICXQI, CXQIEF, QIEFXQ, HBSKSO, OKPHUO]
NHTBJE = [FMNHTB, MNHTBJ]
NRJZTA = [UNRJZT, FCRTFM]
NRSJMC = [OQNRSJ, QNRSJM]
ONPYYL = [WAONPY, AONPYY]
QFFTTI = [JVHFTH, ACQFFT, CQFFTT]
RKINEJ = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, JMAOAW, MAOAWB]
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
SJWMNZ = [KXSJWM, XSJWMN]
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
STSEMC = [PHUOJR]
TATDZX = [JZTATD, ZTATDZ]
TSEMCG = []
UJUTYE = [SXUJUT, XUJUTY]
USPBWJ = [QJYMOU, OUSPBW]
UYNQJY = [PIPIVL, TACCPQ]
XEKVKZ = [JVHFTH, SXUJUT, HXEKVK]
YMOUNB = [QJYMOU, JYMOUN]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return SEMCGE

    @property
    def output_keys(self):
        return KSTSEM

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
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, HUOJRJ, None, None, None
            ),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, None),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, QBMJVH),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, QBMJVH),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, RSJMCB, NRSJMC, None, SJMCBF, QBMJVH
            ),
            JMCBFE: GeckoByteStructAccessor(self.struct, JMCBFE, MCBFEG, QBMJVH),
            CBFEGZ: GeckoByteStructAccessor(self.struct, CBFEGZ, BFEGZU, QBMJVH),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, EGZUQE, None, EXLSXU, None, None, QBMJVH
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, UJUTYE, None, None, QBMJVH
            ),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, UTYEKC, None, KCWAON, None, None, QBMJVH
            ),
            CWAONP: GeckoEnumStructAccessor(
                self.struct, CWAONP, OOQNRS, SJMCBF, ONPYYL, None, SJMCBF, QBMJVH
            ),
            NPYYLI: GeckoByteStructAccessor(self.struct, NPYYLI, PYYLIU, QBMJVH),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, QBMJVH),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, QBMJVH),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, QBMJVH),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, ACCPQI, None, None, QBMJVH
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, IPOUYN, None, None, QBMJVH
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, OUYNQJ, None, UYNQJY, None, None, QBMJVH
            ),
            YNQJYM: GeckoEnumStructAccessor(
                self.struct, YNQJYM, NQJYMO, None, YMOUNB, None, None, QBMJVH
            ),
            MOUNBL: GeckoByteStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoTempStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoEnumStructAccessor(
                self.struct, BLKXSJ, LKXSJW, None, SJWMNZ, None, None, QBMJVH
            ),
            JWMNZM: GeckoEnumStructAccessor(
                self.struct, JWMNZM, WMNZMJ, None, UYNQJY, None, None, QBMJVH
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
            PFTSIF: GeckoByteStructAccessor(self.struct, PFTSIF, FTSIFJ, QBMJVH),
            TSIFJB: GeckoEnumStructAccessor(
                self.struct, TSIFJB, SIFJBI, None, FJBIAM, None, None, QBMJVH
            ),
            JBIAMJ: GeckoEnumStructAccessor(
                self.struct, JBIAMJ, BIAMJM, None, AOAWBS, None, None, QBMJVH
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, AOAWBS, None, None, QBMJVH
            ),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, BSIRYX, None, AOAWBS, None, None, QBMJVH
            ),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, IRYXBQ, None, AOAWBS, None, None, QBMJVH
            ),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, YXBQFY, None, AOAWBS, None, None, QBMJVH
            ),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, AOAWBS, None, None, QBMJVH
            ),
            QFYLJU: GeckoEnumStructAccessor(
                self.struct, QFYLJU, FYLJUI, None, AOAWBS, None, None, QBMJVH
            ),
            YLJUIK: GeckoByteStructAccessor(self.struct, YLJUIK, LJUIKF, QBMJVH),
            JUIKFW: GeckoByteStructAccessor(self.struct, JUIKFW, UIKFWR, QBMJVH),
            IKFWRK: GeckoByteStructAccessor(self.struct, IKFWRK, KFWRKI, QBMJVH),
            FWRKIN: GeckoEnumStructAccessor(
                self.struct, FWRKIN, WRKINE, None, RKINEJ, None, None, QBMJVH
            ),
            KINEJN: GeckoEnumStructAccessor(
                self.struct, KINEJN, INEJNI, None, RKINEJ, None, None, QBMJVH
            ),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, EJNIBX, None, RKINEJ, None, None, QBMJVH
            ),
            JNIBXY: GeckoByteStructAccessor(self.struct, JNIBXY, NIBXYB, QBMJVH),
            IBXYBQ: GeckoTimeStructAccessor(self.struct, IBXYBQ, BXYBQS, QBMJVH),
            XYBQSN: GeckoTimeStructAccessor(self.struct, XYBQSN, YBQSNQ, QBMJVH),
            BQSNQL: GeckoTimeStructAccessor(self.struct, BQSNQL, QSNQLN, QBMJVH),
            SNQLNM: GeckoTimeStructAccessor(self.struct, SNQLNM, NQLNMH, QBMJVH),
            QLNMHX: GeckoTimeStructAccessor(self.struct, QLNMHX, LNMHXE, QBMJVH),
            NMHXEK: GeckoEnumStructAccessor(
                self.struct, NMHXEK, MHXEKV, None, XEKVKZ, None, None, QBMJVH
            ),
            EKVKZI: GeckoBoolStructAccessor(
                self.struct, EKVKZI, KVKZIL, RSJMCB, QBMJVH
            ),
            VKZILX: GeckoBoolStructAccessor(
                self.struct, VKZILX, KZILXW, SJMCBF, QBMJVH
            ),
            ZILXWA: GeckoBoolStructAccessor(
                self.struct, ZILXWA, KZILXW, RSJMCB, QBMJVH
            ),
            ILXWAJ: GeckoBoolStructAccessor(
                self.struct, ILXWAJ, KZILXW, LXWAJV, QBMJVH
            ),
            XWAJVD: GeckoBoolStructAccessor(
                self.struct, XWAJVD, KZILXW, WAJVDQ, QBMJVH
            ),
            AJVDQL: GeckoBoolStructAccessor(
                self.struct, AJVDQL, KZILXW, JVDQLA, QBMJVH
            ),
            VDQLAI: GeckoEnumStructAccessor(
                self.struct, VDQLAI, DQLAII, None, AIIDNI, None, None, QBMJVH
            ),
            IIDNIB: GeckoEnumStructAccessor(
                self.struct, IIDNIB, IDNIBX, None, IBXTIA, None, None, QBMJVH
            ),
            BXTIAC: GeckoByteStructAccessor(self.struct, BXTIAC, XTIACQ, QBMJVH),
            TIACQF: GeckoEnumStructAccessor(
                self.struct, TIACQF, IACQFF, None, QFFTTI, None, None, QBMJVH
            ),
            FFTTID: GeckoWordStructAccessor(self.struct, FFTTID, FTTIDU, QBMJVH),
            TTIDUB: GeckoEnumStructAccessor(
                self.struct, TTIDUB, OOQNRS, LXWAJV, DUBSSU, None, SJMCBF, QBMJVH
            ),
            UBSSUH: GeckoBoolStructAccessor(
                self.struct, UBSSUH, OOQNRS, BSSUHB, QBMJVH
            ),
            SSUHBV: GeckoEnumStructAccessor(
                self.struct, SSUHBV, OOQNRS, JVDQLA, HBVWVU, None, SJMCBF, QBMJVH
            ),
            BVWVUB: GeckoBoolStructAccessor(
                self.struct, BVWVUB, OOQNRS, VWVUBY, QBMJVH
            ),
            WVUBYG: GeckoBoolStructAccessor(
                self.struct, WVUBYG, OOQNRS, VUBYGD, QBMJVH
            ),
            UBYGDS: GeckoBoolStructAccessor(
                self.struct, UBYGDS, BYGDSB, RSJMCB, QBMJVH
            ),
            YGDSBD: GeckoBoolStructAccessor(
                self.struct, YGDSBD, BYGDSB, LXWAJV, QBMJVH
            ),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, BYGDSB, SJMCBF, BDJQRJ, None, SJMCBF, QBMJVH
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, BYGDSB, WAJVDQ, BDJQRJ, None, SJMCBF, QBMJVH
            ),
            JQRJJJ: GeckoEnumStructAccessor(
                self.struct, JQRJJJ, BYGDSB, BSSUHB, CRTFMN, None, RTFMNH, QBMJVH
            ),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, BYGDSB, VUBYGD, NHTBJE, None, SJMCBF, QBMJVH
            ),
            BQNRXC: GeckoBoolStructAccessor(
                self.struct, BQNRXC, QNRXCH, RSJMCB, QBMJVH
            ),
            NRXCHW: GeckoBoolStructAccessor(
                self.struct, NRXCHW, QNRXCH, LXWAJV, QBMJVH
            ),
            RXCHWD: GeckoEnumStructAccessor(
                self.struct, RXCHWD, QNRXCH, SJMCBF, HWDAFI, None, BSSUHB, QBMJVH
            ),
            WDAFIK: GeckoByteStructAccessor(self.struct, WDAFIK, DAFIKJ, QBMJVH),
            AFIKJP: GeckoBoolStructAccessor(
                self.struct, AFIKJP, FIKJPU, RSJMCB, QBMJVH
            ),
            IKJPUN: GeckoByteStructAccessor(self.struct, IKJPUN, KJPUNR, QBMJVH),
            JPUNRJ: GeckoEnumStructAccessor(
                self.struct, JPUNRJ, PUNRJZ, RSJMCB, NRJZTA, None, SJMCBF, None
            ),
            RJZTAT: GeckoEnumStructAccessor(
                self.struct, RJZTAT, PUNRJZ, LXWAJV, TATDZX, None, SJMCBF, None
            ),
            ATDZXN: GeckoEnumStructAccessor(
                self.struct, ATDZXN, TDZXNQ, RSJMCB, NRJZTA, None, SJMCBF, None
            ),
            DZXNQT: GeckoEnumStructAccessor(
                self.struct, DZXNQT, TDZXNQ, LXWAJV, TATDZX, None, SJMCBF, None
            ),
            ZXNQTM: GeckoEnumStructAccessor(
                self.struct, ZXNQTM, XNQTMF, RSJMCB, NRJZTA, None, SJMCBF, None
            ),
            NQTMFZ: GeckoEnumStructAccessor(
                self.struct, NQTMFZ, XNQTMF, LXWAJV, TATDZX, None, SJMCBF, None
            ),
            QTMFZD: GeckoEnumStructAccessor(
                self.struct, QTMFZD, TMFZDG, RSJMCB, NRJZTA, None, SJMCBF, None
            ),
            MFZDGK: GeckoEnumStructAccessor(
                self.struct, MFZDGK, TMFZDG, LXWAJV, TATDZX, None, SJMCBF, None
            ),
            FZDGKE: GeckoEnumStructAccessor(
                self.struct, FZDGKE, ZDGKEA, RSJMCB, AKSTSE, None, RTFMNH, None
            ),
        }

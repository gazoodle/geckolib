#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ-V2 v60'
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
ACQFFT = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
AFIKJP = 123
AIIDNI = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 50])
AKSTSE = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
AMJMAO = "".join(chr(c) for c in [70, 51])
AOAWBS = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
AONPYY = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 116, 101, 99, 116, 105, 111, 110])
ATDZXN = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
AWBSIR = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
BDJQRJ = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
BFEGZU = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
BIAMJM = "".join(chr(c) for c in [70, 49])
BJEUTO = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
BLKXSJ = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
BQSNQL = 10
BSIRYX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
BSKSOK = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
BSSUHB = 6
BVWVUB = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
BWJYKL = 77
BXYBQS = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
BYGDSB = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
CBFEGZ = 27
CCPQIP = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
CGETIX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
CHWDAF = "".join(chr(c) for c in [83, 105, 108, 101, 110, 116, 77, 111, 100, 101])
CPQIPO = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
CQBMJV = 0
CQFFTT = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
CRTFMN = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
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
DAFIKJ = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
DGKEAK = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
DJQRJJ = "".join(chr(c) for c in [66, 76, 85, 69])
DNIBXT = 34
DNQGVU = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
DQLAII = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
DSBDJQ = "".join(chr(c) for c in [82, 69, 68])
DZXNQT = 126
EAKSTS = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
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
ELHBQN = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
EMCGET = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
EOCTHB = 39
ETIXQV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
EUTOPH = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
EXLSXU = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
FEGZUQ = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
FFTTID = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
FIKJPU = "".join(chr(c) for c in [82, 71, 66])
FJBIAM = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
FJTACC = 29
FMNHTB = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
FTTIDU = 4
FWRKIN = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
FZDGKE = "".join(chr(c) for c in [52])
GDSBDJ = "".join(chr(c) for c in [79, 70, 70])
GETIXQ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
GKEAKS = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
GLRAHE = 40
GQPLSP = "".join(chr(c) for c in [67, 69])
GSELHB = 45
GTYIYW = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
GVUNXN = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
GYOUSP = 68
GZUQEX = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
HBQNRX = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
HBVWVU = 43
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 0
HTBJEU = "".join(chr(c) for c in [65, 108, 112, 115])
HUGTYI = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
HUOJRJ = 56
HWDAFI = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
HXEKVK = 72
IACQFF = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
IAMJMA = "".join(chr(c) for c in [70, 50])
IBXTIA = "".join(chr(c) for c in [50, 52, 104])
IBXYBQ = 23
ICXQIE = 16
IDNIBX = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
IDUBSS = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
IGYOUS = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IIDNIB = 75
IJUGSE = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
IKFWRK = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
ILXWAJ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
INEJNI = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 63
IRYXBQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
IUSOOQ = 2
IUXFEF = 28
IVDNQG = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
IYWSKW = "".join(chr(c) for c in [74, 97, 122, 122, 105])
JBIAMJ = 83
JEUTOP = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
JIGYOU = 66
JJVYFC = 8
JMAOAW = "".join(chr(c) for c in [76, 105, 110, 101, 50])
JNIBXY = 6
JPUNRJ = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
JQRJJJ = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
JRJHIU = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
JUIKFW = 104
JUTYEK = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
JVDQLA = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(
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
JWMNZM = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
JYKLGQ = 26
JZTATD = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
KCWAON = 60
KEAKST = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
KFWRKI = 105
KINEJN = 3
KJPUNR = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
KLGQPL = 51
KMLOIJ = "".join(chr(c) for c in [73, 100, 111, 108])
KPHUOJ = 55
KQXPIC = 13
KSOKPH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KSTSEM = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
KVKZIL = 1
KWIVDN = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
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
LHBQNR = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
LIUXFE = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
LJUIKF = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
LKXSJW = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
LNMHXE = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
LOIJUG = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
LRAHEO = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
LSPFTS = 52
LSXUJU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
LXWAJV = 76
MCBFEG = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
MCGETI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
MFZDGK = "".join(chr(c) for c in [51])
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
MLOIJU = "".join(chr(c) for c in [65, 115, 112, 101, 110])
MNHTBJ = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
MNZMJI = 3
MOUNBL = 31
NBLKXS = "".join(chr(c) for c in [105, 110, 70, 108, 111])
NEJNIB = 4
NHTBJE = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
NIBXTI = "".join(chr(c) for c in [65, 109, 80, 109])
NIBXYB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
NKMLOI = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
NMHXEK = 82
NPYYLI = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
NQGVUN = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
NQJYMO = "".join(chr(c) for c in [70])
NQLNMH = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
NQTMFZ = 127
NRJZTA = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
NRSJMC = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
NRXCHW = 46
NXNKML = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
NZMJIG = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
OAWBSI = 84
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 76, 105])
OIHBXI = 60
OIJUGS = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
OJRJHI = 81
OKPHUO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
ONPYYL = 62
OOQNRS = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
OPHUGT = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
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
PHUGTY = "".join(chr(c) for c in [67, 111, 97, 115, 116])
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
POUYNQ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
PUNRJZ = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
PYYLIU = 78
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
QFYLJU = 99
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
QGVUNX = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
QIEFXQ = 36
QIPOUY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
QJYMOU = "".join(chr(c) for c in [67])
QLAIID = "".join(chr(c) for c in [83, 108, 97, 118, 101])
QNRSJM = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
QNRXCH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
QRJJJV = "".join(chr(c) for c in [67, 89, 65, 78])
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
QTMFZD = "".join(chr(c) for c in [49])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 51])
RAHEOC = 15
RJHIUS = "".join(chr(c) for c in [79, 119, 110])
RJJJVY = "".join(chr(c) for c in [87, 72, 73, 84, 69])
RJZTAT = 124
RKINEJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
RSJMCB = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
RTFMNH = 44
RXCHWD = "".join(
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
RYXBQF = 87
SBDJQR = "".join(chr(c) for c in [71, 82, 69, 69, 78])
SELHBQ = "".join(
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
SEMCGE = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
SIFJBI = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
SIRYXB = 86
SJMCBF = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
SJWMNZ = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
SKSOKP = 80
SKWIVD = "".join(chr(c) for c in [77, 65, 65, 88])
SNQLNM = 71
SOKPHU = 54
SOOQNR = 48
SPFTSI = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
SSAKQX = "".join(chr(c) for c in [65, 85, 88])
SSUHBV = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
STSEMC = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
SUHBVW = 7
SXUJUT = "".join(chr(c) for c in [76, 111])
TACCPQ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
TATDZX = 125
TBJEUT = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
TDZXNQ = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
TFMNHT = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
THBSKS = "".join(chr(c) for c in [76, 73])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 64
TIDUBS = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
TIXQVX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
TMFZDG = "".join(chr(c) for c in [50])
TOPHUG = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
TSEMCG = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
TSIFJB = 74
TTIDUB = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
TYEKCW = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
TYIYWS = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
UBSSUH = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
UGSELH = "".join(
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
UGTYIY = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
UHBVWV = "".join(
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
UNBLKX = 25
UNXNKM = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
UOJRJH = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
UQEXLS = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
USOOQN = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
USPBWJ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
UTOPHU = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
UTYEKC = 58
UXFEFJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
UYNQJY = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
VDNQGV = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
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
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
VUNXNK = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
VWVUBY = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
VYFCRT = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
WAONPY = 61
WBSIRY = 85
WDAFIK = 121
WIVDNQ = "".join(chr(c) for c in [80, 68, 67])
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
WSKWIV = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
WVUBYG = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
XBQFYL = 98
XCHWDA = 47
XEKVKZ = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
XFEFJT = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
XNKMLO = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
XNQTMF = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
XPICXQ = 14
XQGLRA = 38
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
XQVXOI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
XSJWMN = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
XTIACQ = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
XUJUTY = "".join(chr(c) for c in [72, 105])
XWAJVD = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
XYBQSN = 8
YBQSNQ = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
YEKCWA = 59
YFCRTF = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
YGDSBD = "".join(
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
YIYWSK = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
YKLGQP = "".join(chr(c) for c in [85, 76, 95, 67, 69])
YLJUIK = 100
YMOUNB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
YNQJYM = 33
YOUSPB = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [76, 65])
YXBQFY = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
YYLIUX = "".join(chr(c) for c in [80, 49])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 5
ZMJIGY = 35
ZTATDZ = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
ZUQEXL = 57
ZXNQTM = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
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
BQNRXC = [LHBQNR, HBQNRX, VLASSA, VLASSA]
BXTIAC = [JVHFTH, NIBXTI, IBXTIA]
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
DUBSSU = [TIDUBS, IDUBSS]
EGZUQE = [BFEGZU, FEGZUQ]
FCRTFM = [VYFCRT, YFCRTF]
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
IFJBIA = [CCPQIP, SIFJBI]
IKJPUN = [FIKJPU, RJJJVY]
JHIUSO = [JRJHIU, RJHIUS]
JJJVYF = [GDSBDJ, DSBDJQ, SBDJQR, BDJQRJ, DJQRJJ, JQRJJJ, QRJJJV, RJJJVY]
JMCBFE = [QNRSJM, NRSJMC, RSJMCB, SJMCBF]
JTACCP = [PIPIVL, YYLIUX]
JUGSEL = [
    TFMNHT,
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
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
]
JYMOUN = [NQJYMO, QJYMOU]
KXSJWM = [NBLKXS, BLKXSJ, LKXSJW]
LAIIDN = [VLASSA, DQLAII, QLAIID]
MAOAWB = [BIAMJM, IAMJMA, AMJMAO, VLASSA, VLASSA, VLASSA, MJMAOA, JMAOAW]
PQIPOU = [CCPQIP, CPQIPO]
QFFTTI = [ACQFFT, CQFFTT]
QLNMHX = [JVHFTH, BFEGZU, NQLNMH]
QPLSPF = [LGQPLS, GQPLSP]
QVXOIH = [BMJVHF, AKQXPI, QXPICX, PICXQI, LRAHEO, OCTHBS]
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
UBYGDS = [WVUBYG, VUBYGD]
UIKFWR = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, MJMAOA, JMAOAW]
UJUTYE = [SXUJUT, XUJUTY]
UNRJZT = [JPUNRJ, PUNRJZ]
VXOIHB = [THBSKS]
WMNZMJ = [SJWMNZ, JWMNZM]
XLSXUJ = [UQEXLS, QEXLSX, EXLSXU]
XOIHBX = []
YLIUXF = [JVHFTH, YYLIUX, PIPIVL]
ZDGKEA = [VLASSA, QTMFZD, TMFZDG, MFZDGK, FZDGKE]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return OIHBXI

    @property
    def output_keys(self):
        return QVXOIH

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
                self.struct, IDNIBX, DNIBXT, None, BXTIAC, None, None, QBMJVH
            ),
            XTIACQ: GeckoWordStructAccessor(self.struct, XTIACQ, TIACQF, QBMJVH),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, OJRJHI, KVKZIL, QFFTTI, None, IUSOOQ, QBMJVH
            ),
            FFTTID: GeckoBoolStructAccessor(
                self.struct, FFTTID, OJRJHI, FTTIDU, QBMJVH
            ),
            TTIDUB: GeckoEnumStructAccessor(
                self.struct, TTIDUB, OJRJHI, ZILXWA, DUBSSU, None, IUSOOQ, QBMJVH
            ),
            UBSSUH: GeckoBoolStructAccessor(
                self.struct, UBSSUH, OJRJHI, BSSUHB, QBMJVH
            ),
            SSUHBV: GeckoBoolStructAccessor(
                self.struct, SSUHBV, OJRJHI, SUHBVW, QBMJVH
            ),
            UHBVWV: GeckoBoolStructAccessor(
                self.struct, UHBVWV, HBVWVU, HIUSOO, QBMJVH
            ),
            BVWVUB: GeckoBoolStructAccessor(
                self.struct, BVWVUB, HBVWVU, KVKZIL, QBMJVH
            ),
            VWVUBY: GeckoEnumStructAccessor(
                self.struct, VWVUBY, HBVWVU, IUSOOQ, UBYGDS, None, IUSOOQ, QBMJVH
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, HBVWVU, MNZMJI, UBYGDS, None, IUSOOQ, QBMJVH
            ),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, HBVWVU, FTTIDU, JJJVYF, None, JJVYFC, QBMJVH
            ),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, HBVWVU, SUHBVW, FCRTFM, None, IUSOOQ, QBMJVH
            ),
            UGSELH: GeckoBoolStructAccessor(
                self.struct, UGSELH, GSELHB, HIUSOO, QBMJVH
            ),
            SELHBQ: GeckoBoolStructAccessor(
                self.struct, SELHBQ, GSELHB, KVKZIL, QBMJVH
            ),
            ELHBQN: GeckoEnumStructAccessor(
                self.struct, ELHBQN, GSELHB, IUSOOQ, BQNRXC, None, FTTIDU, QBMJVH
            ),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, QBMJVH),
            RXCHWD: GeckoBoolStructAccessor(
                self.struct, RXCHWD, XCHWDA, HIUSOO, QBMJVH
            ),
            CHWDAF: GeckoBoolStructAccessor(
                self.struct, CHWDAF, XCHWDA, MNZMJI, QBMJVH
            ),
            HWDAFI: GeckoByteStructAccessor(self.struct, HWDAFI, WDAFIK, QBMJVH),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, AFIKJP, HIUSOO, IKJPUN, None, IUSOOQ, None
            ),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, AFIKJP, KVKZIL, UNRJZT, None, IUSOOQ, None
            ),
            NRJZTA: GeckoEnumStructAccessor(
                self.struct, NRJZTA, RJZTAT, HIUSOO, IKJPUN, None, IUSOOQ, None
            ),
            JZTATD: GeckoEnumStructAccessor(
                self.struct, JZTATD, RJZTAT, KVKZIL, UNRJZT, None, IUSOOQ, None
            ),
            ZTATDZ: GeckoEnumStructAccessor(
                self.struct, ZTATDZ, TATDZX, HIUSOO, IKJPUN, None, IUSOOQ, None
            ),
            ATDZXN: GeckoEnumStructAccessor(
                self.struct, ATDZXN, TATDZX, KVKZIL, UNRJZT, None, IUSOOQ, None
            ),
            TDZXNQ: GeckoEnumStructAccessor(
                self.struct, TDZXNQ, DZXNQT, HIUSOO, IKJPUN, None, IUSOOQ, None
            ),
            ZXNQTM: GeckoEnumStructAccessor(
                self.struct, ZXNQTM, DZXNQT, KVKZIL, UNRJZT, None, IUSOOQ, None
            ),
            XNQTMF: GeckoEnumStructAccessor(
                self.struct, XNQTMF, NQTMFZ, HIUSOO, ZDGKEA, None, JJVYFC, None
            ),
            DGKEAK: GeckoBoolStructAccessor(self.struct, DGKEAK, NQTMFZ, SUHBVW, None),
            GKEAKS: GeckoBoolStructAccessor(self.struct, GKEAKS, AFIKJP, FTTIDU, None),
            KEAKST: GeckoBoolStructAccessor(self.struct, KEAKST, AFIKJP, ZILXWA, None),
            EAKSTS: GeckoBoolStructAccessor(self.struct, EAKSTS, AFIKJP, BSSUHB, None),
            AKSTSE: GeckoBoolStructAccessor(self.struct, AKSTSE, AFIKJP, SUHBVW, None),
            KSTSEM: GeckoBoolStructAccessor(self.struct, KSTSEM, RJZTAT, FTTIDU, None),
            STSEMC: GeckoBoolStructAccessor(self.struct, STSEMC, RJZTAT, ZILXWA, None),
            TSEMCG: GeckoBoolStructAccessor(self.struct, TSEMCG, RJZTAT, BSSUHB, None),
            SEMCGE: GeckoBoolStructAccessor(self.struct, SEMCGE, RJZTAT, SUHBVW, None),
            EMCGET: GeckoBoolStructAccessor(self.struct, EMCGET, TATDZX, FTTIDU, None),
            MCGETI: GeckoBoolStructAccessor(self.struct, MCGETI, TATDZX, ZILXWA, None),
            CGETIX: GeckoBoolStructAccessor(self.struct, CGETIX, TATDZX, BSSUHB, None),
            GETIXQ: GeckoBoolStructAccessor(self.struct, GETIXQ, TATDZX, SUHBVW, None),
            ETIXQV: GeckoBoolStructAccessor(self.struct, ETIXQV, DZXNQT, FTTIDU, None),
            TIXQVX: GeckoBoolStructAccessor(self.struct, TIXQVX, DZXNQT, ZILXWA, None),
            IXQVXO: GeckoBoolStructAccessor(self.struct, IXQVXO, DZXNQT, BSSUHB, None),
            XQVXOI: GeckoBoolStructAccessor(self.struct, XQVXOI, DZXNQT, SUHBVW, None),
        }

#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v58'
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
ACCPQI = 32
ACMCVD = "".join(chr(c) for c in [65, 115, 112, 101, 110])
ACQFFT = 93
AFIKJP = 110
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
AIIDNI = 88
AJVDQL = 85
AKQXPI = "".join(chr(c) for c in [65, 85, 88])
AKSTSE = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
AMJMAO = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
AOAWBS = "".join(chr(c) for c in [105, 110, 70, 108, 111])
AONPYY = 55
ASSAKQ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
ATDZXN = "".join(chr(c) for c in [67, 89, 65, 78])
AWBSIR = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
AZMKQT = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
BDJQRJ = 105
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
BHZVOA = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
BIAMJM = "".join(chr(c) for c in [67])
BJEUTO = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
BLKXSJ = "".join(chr(c) for c in [76, 111])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 35
BQNRXC = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
BQSNQL = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
BSIRYX = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
BSKSOK = 50
BSSUHB = 98
BVWVUB = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
BWJYKL = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
BXIBHZ = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
BXTIAC = 91
BXYBQS = 52
BYGDSB = 103
CBFEGZ = 43
CCPQIP = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
CGETIX = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
CHWDAF = 6
CMCVDS = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
CPQIPO = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
CRTFMN = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
CVDSSR = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 54
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 52])
DAFIKJ = "".join(
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
DGKEAK = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
DJQRJJ = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
DKHTZB = 119
DNIBXT = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
DQLAII = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
DUBSSU = 97
EAKSTS = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 118
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
EJNIBX = "".join(chr(c) for c in [85, 76])
EKCWAO = 80
EKVKZI = "".join(chr(c) for c in [70, 50, 50])
EMCGET = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
ETIXQV = "".join(chr(c) for c in [74, 97, 122, 122, 105])
EUTOPH = "".join(
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
EXLSXU = 47
FCRTFM = 3
FEFJTA = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
FEGZUQ = 44
FFTTID = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
FIKJPU = "".join(
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
FJBIAM = 33
FJTACC = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
FMNHTB = 6
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 63
FTTIDU = 95
FWRKIN = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
FXQGLR = 26
FYLJUI = 66
FZDGKE = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
GDSBDJ = 104
GETIXQ = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
GKEAKS = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
GLRAHE = 36
GQPLSP = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
GSELHB = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
GTYIYW = 72
GVUNXN = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
GYOUSP = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
GZUQEX = 45
HBQNRX = 4
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
HBVWVU = 100
HBXIBH = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 38
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(chr(c) for c in [79, 117, 116, 49, 50])
HTBJEU = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
HUGTYI = 82
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 57])
HWDAFI = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
HXEKVK = "".join(chr(c) for c in [70, 51])
HZVOAC = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
IACQFF = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
IBHZVO = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
IBXTIA = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
IBXYBQ = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
ICXQIE = 14
IDNIBX = 89
IDUBSS = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
IEFXQG = 16
IFJBIA = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
IGYOUS = 62
IHBXIB = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
IIDNIB = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
IJUGSE = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
IKFWRK = "".join(chr(c) for c in [78, 105, 103, 104, 116])
IKJPUN = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
INEJNI = "".join(chr(c) for c in [85, 76, 95, 67, 69])
IPIVLA = "".join(chr(c) for c in [79, 51])
IRYXBQ = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
IUSOOQ = 23
IVDNQG = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
IYWSKW = 1
JBIAMJ = "".join(chr(c) for c in [70])
JEUTOP = 10
JHIUSO = 22
JIGYOU = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
JJJVYF = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
JJVYFC = 108
JMAOAW = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
JMCBFE = 42
JNIBXY = "".join(chr(c) for c in [67, 69])
JQRJJJ = 106
JRJHIU = 21
JTACCP = 120
JUGSEL = 64
JUIKFW = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
JUTYEK = 79
JVDQLA = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
JWMNZM = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
JYMOUN = 57
JZTATD = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
KCWAON = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KEAKST = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
KINEJN = 114
KJPUNR = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
KLGQPL = 29
KMLOIJ = 34
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 56])
KQTDKH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
KSOKPH = 17
KSTSEM = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
KVKZIL = "".join(chr(c) for c in [70, 50, 51])
KWIVDN = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
KZILXW = "".join(chr(c) for c in [76, 105, 110, 101, 50])
LAIIDN = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
LASSAK = "".join(chr(c) for c in [70, 97, 110])
LHBQNR = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
LIUXFE = "".join(chr(c) for c in [79, 119, 110])
LJUIKF = 68
LKXSJW = "".join(chr(c) for c in [72, 105])
LNMHXE = 83
LOIJUG = "".join(chr(c) for c in [50, 52, 104])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
LSXUJU = 48
LXWAJV = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
MAOAWB = 115
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
MCGETI = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
MCVDSS = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
MFZDGK = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
MHXEKV = "".join(chr(c) for c in [70, 50])
MJIGYO = 61
MJMAOA = 31
MJVHFT = 12
MLOIJU = "".join(chr(c) for c in [65, 109, 80, 109])
MNHTBJ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
MNZMJI = "".join(
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
MOUNBL = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
NBLKXS = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
NEJNIB = 51
NHTBJE = 116
NIBXTI = 90
NKMLOI = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
NMHXEK = "".join(chr(c) for c in [70, 49])
NPYYLI = 56
NQGVUN = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
NQTMFZ = 111
NRJZTA = "".join(chr(c) for c in [82, 69, 68])
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
NRXCHW = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
NXNKML = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
NZMJIG = 60
OACMCV = "".join(chr(c) for c in [73, 100, 111, 108])
OAWBSI = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
OCTHBS = 39
OIHBXI = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 48])
OKPHUO = 18
ONPYYL = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
OQNRSJ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
OUNBLK = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
OUSPBW = "".join(chr(c) for c in [80, 49])
OUYNQJ = 27
PBWJYK = 28
PFTSIF = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
PHUGTY = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
PHUOJR = 19
PICXQI = "".join(chr(c) for c in [79, 117, 116, 51])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
POUYNQ = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
PQIPOU = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
PUNRJZ = "".join(
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
PYYLIU = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
QFFTTI = 94
QFYLJU = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
QGVUNX = 73
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 53])
QIPOUY = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
QJYMOU = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
QLAIID = 87
QLNMHX = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
QNRSJM = 25
QNRXCH = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
QPLSPF = 30
QRJJJV = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
QSNQLN = 74
QTDKHT = 113
QTMFZD = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
QVXOIH = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 50])
RAHEOC = 37
RAZMKQ = 112
RJHIUS = "".join(chr(c) for c in [79, 117, 116, 49, 49])
RJJJVY = 107
RJZTAT = "".join(chr(c) for c in [71, 82, 69, 69, 78])
RKINEJ = "".join(
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
RSJMCB = 41
RTFMNH = 4
RURAZM = "".join(chr(c) for c in [65, 108, 108])
SAKQXP = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
SBDJQR = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
SELHBQ = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
SEMCGE = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
SIFJBI = 1
SIRYXB = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
SJWMNZ = 58
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 54])
SKWIVD = 5
SNQLNM = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 55])
SOOQNR = 24
SPBWJY = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
SRURAZ = "".join(
    chr(c)
    for c in [
        67,
        102,
        103,
        67,
        104,
        97,
        110,
        103,
        101,
        67,
        111,
        100,
        101,
        69,
        110,
        97,
        98,
        108,
        101,
    ]
)
SSAKQX = "".join(chr(c) for c in [72, 84, 82, 50])
SSRURA = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
SSUHBV = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
STSEMC = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
SUHBVW = 99
SXUJUT = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
TACCPQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
TATDZX = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
TBJEUT = 8
TDKHTZ = "".join(
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
TDZXNQ = "".join(chr(c) for c in [87, 72, 73, 84, 69])
TFMNHT = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
THBSKS = 40
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 92
TIDUBS = 96
TIXQVX = "".join(chr(c) for c in [76, 65])
TMFZDG = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
TOPHUG = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
TSEMCG = "".join(chr(c) for c in [67, 111, 97, 115, 116])
TSIFJB = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
TTIDUB = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
TYIYWS = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
UBSSUH = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
UBYGDS = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
UGSELH = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
UGTYIY = "".join(
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
UHBVWV = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
UIKFWR = 70
UJUTYE = "".join(chr(c) for c in [79, 117, 116, 76, 105])
UNRJZT = "".join(chr(c) for c in [79, 70, 70])
UOJRJH = 20
UQEXLS = 46
URAZMK = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
USOOQN = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
UTOPHU = 71
UTYEKC = "".join(chr(c) for c in [76, 73])
UXFEFJ = 0
UYNQJY = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
VDNQGV = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
VDQLAI = 86
VDSSRU = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [76, 105, 110, 101, 49])
VLASSA = "".join(chr(c) for c in [])
VOACMC = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
VUBYGD = 102
VUNXNK = "".join(chr(c) for c in [83, 108, 97, 118, 101])
VWVUBY = 101
VXOIHB = "".join(chr(c) for c in [80, 68, 67])
VYFCRT = 109
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
WAONPY = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
WDAFIK = 7
WIVDNQ = 76
WJYKLG = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
WMNZMJ = 59
WRKINE = 77
WSKWIV = "".join(
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
WVUBYG = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
XBQFYL = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
XCHWDA = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
XEKVKZ = "".join(chr(c) for c in [70, 50, 49])
XFEFJT = 2
XIBHZV = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
XLSXUJ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
XNKMLO = 75
XNQTMF = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
XOIHBX = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
XPICXQ = 13
XQIEFX = 15
XQVXOI = "".join(chr(c) for c in [77, 65, 65, 88])
XSJWMN = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
XTIACQ = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
XUJUTY = 49
XWAJVD = 84
XYBQSN = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
YBQSNQ = 53
YEKCWA = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
YFCRTF = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
YGDSBD = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
YIYWSK = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
YKLGQP = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
YLIUXF = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
YLJUIK = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
YMOUNB = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
YNQJYM = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
YOUSPB = 78
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
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
YXBQFY = 3
YYLIUX = 81
YYPIPI = "".join(chr(c) for c in [80, 53])
ZBBEKB = 58
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = "".join(chr(c) for c in [65, 108, 112, 115])
ZILXWA = "".join(chr(c) for c in [76, 105, 110, 101, 51])
ZMJIGY = "".join(
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
ZMKQTD = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
ZTATDZ = "".join(chr(c) for c in [66, 76, 85, 69])
ZUQEXL = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
ZVOACM = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
ZXNQTM = 8
DNQGVU = [IVDNQG, VDNQGV]
DSBDJQ = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VKZILX, KZILXW, ZILXWA]
DSSRUR = [
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
    OIHBXI,
    IHBXIB,
    HBXIBH,
    BXIBHZ,
    XIBHZV,
    IBHZVO,
    BHZVOA,
    HZVOAC,
    ZVOACM,
    VOACMC,
    OACMCV,
    ACMCVD,
    CMCVDS,
    MCVDSS,
    CVDSSR,
    VDSSRU,
]
DZXNQT = [UNRJZT, NRJZTA, RJZTAT, JZTATD, ZTATDZ, TATDZX, ATDZXN, TDZXNQ]
ELHBQN = [GSELHB, SELHBQ]
HTZBBE = [UTYEKC]
IAMJMA = [JBIAMJ, BIAMJM]
ILXWAJ = [NMHXEK, MHXEKV, HXEKVK, XEKVKZ, EKVKZI, KVKZIL, VKZILX, KZILXW, ZILXWA]
IPOUYN = [CCPQIP, CPQIPO, PQIPOU, QIPOUY]
IUXFEF = [YLIUXF, LIUXFE]
JPUNRJ = [IKJPUN, KJPUNR]
JYKLGQ = [BWJYKL, WJYKLG]
KFWRKI = [PLSPFT, IKFWRK]
KHTZBB = [
    BMJVHF,
    QXPICX,
    PICXQI,
    CXQIEF,
    QIEFXQ,
    EFXQGL,
    SKSOKP,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RJHIUS,
    HIUSOO,
    USOOQN,
    OQNRSJ,
    UJUTYE,
]
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
    VLASSA,
    LASSAK,
    VLASSA,
    VLASSA,
    ASSAKQ,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    SSAKQX,
    SAKQXP,
    AKQXPI,
]
KXSJWM = [BLKXSJ, LKXSJW]
LGQPLS = [PIPIVL, OUSPBW]
MKQTDK = [AZMKQT, ZMKQTD, VLASSA, VLASSA]
NIBXYB = [EJNIBX, JNIBXY]
NQJYMO = [UYNQJY, YNQJYM]
NQLNMH = [PLSPFT, SNQLNM]
OIJUGS = [JVHFTH, MLOIJU, LOIJUG]
OOQNRS = [
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
OPHUGT = [JVHFTH, UYNQJY, TOPHUG]
RXCHWD = [QNRXCH, NRXCHW]
RYXBQF = [SIRYXB, IRYXBQ]
SPFTSI = [PLSPFT, LSPFTS]
TYEKCW = [
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
    UTYEKC,
]
TZBBEK = []
UNBLKX = [YMOUNB, MOUNBL, OUNBLK]
UNXNKM = [VLASSA, GVUNXN, VUNXNK]
USPBWJ = [JVHFTH, OUSPBW, PIPIVL]
WBSIRY = [AOAWBS, OAWBSI, AWBSIR]
XQGLRA = [
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
    SSAKQX,
]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return ZBBEKB

    @property
    def output_keys(self):
        return KHTZBB

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
                self.struct, EFXQGL, FXQGLR, None, XQGLRA, None, None, QBMJVH
            ),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoByteStructAccessor(self.struct, CTHBSK, THBSKS, QBMJVH),
            HBSKSO: GeckoByteStructAccessor(self.struct, HBSKSO, BSKSOK, QBMJVH),
            SKSOKP: GeckoEnumStructAccessor(
                self.struct, SKSOKP, KSOKPH, None, KQXPIC, None, None, QBMJVH
            ),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, OKPHUO, None, KQXPIC, None, None, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, KQXPIC, None, None, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, KQXPIC, None, None, QBMJVH
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, KQXPIC, None, None, QBMJVH
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, KQXPIC, None, None, QBMJVH
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, IUSOOQ, None, KQXPIC, None, None, QBMJVH
            ),
            USOOQN: GeckoEnumStructAccessor(
                self.struct, USOOQN, SOOQNR, None, OOQNRS, None, None, QBMJVH
            ),
            OQNRSJ: GeckoEnumStructAccessor(
                self.struct, OQNRSJ, QNRSJM, None, OOQNRS, None, None, QBMJVH
            ),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoByteStructAccessor(self.struct, SJMCBF, JMCBFE, QBMJVH),
            MCBFEG: GeckoByteStructAccessor(self.struct, MCBFEG, CBFEGZ, QBMJVH),
            BFEGZU: GeckoByteStructAccessor(self.struct, BFEGZU, FEGZUQ, QBMJVH),
            EGZUQE: GeckoByteStructAccessor(self.struct, EGZUQE, GZUQEX, QBMJVH),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QBMJVH),
            QEXLSX: GeckoByteStructAccessor(self.struct, QEXLSX, EXLSXU, QBMJVH),
            XLSXUJ: GeckoByteStructAccessor(self.struct, XLSXUJ, LSXUJU, QBMJVH),
            SXUJUT: GeckoByteStructAccessor(self.struct, SXUJUT, XUJUTY, QBMJVH),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, JUTYEK, None, TYEKCW, None, None, None
            ),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, None),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, QBMJVH),
            ONPYYL: GeckoByteStructAccessor(self.struct, ONPYYL, NPYYLI, QBMJVH),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, YYLIUX, UXFEFJ, IUXFEF, None, XFEFJT, QBMJVH
            ),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, QBMJVH),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, QBMJVH),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, None, IPOUYN, None, None, QBMJVH
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, OUYNQJ, None, NQJYMO, None, None, QBMJVH
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, UNBLKX, None, None, QBMJVH
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, YYLIUX, XFEFJT, KXSJWM, None, XFEFJT, QBMJVH
            ),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoEnumStructAccessor(
                self.struct, GYOUSP, YOUSPB, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, JYKLGQ, None, None, QBMJVH
            ),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, LGQPLS, None, None, QBMJVH
            ),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, QPLSPF, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoByteStructAccessor(self.struct, PFTSIF, FTSIFJ, QBMJVH),
            TSIFJB: GeckoTempStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoEnumStructAccessor(
                self.struct, IFJBIA, FJBIAM, None, IAMJMA, None, None, QBMJVH
            ),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, MJMAOA, None, LGQPLS, None, None, QBMJVH
            ),
            JMAOAW: GeckoEnumStructAccessor(
                self.struct, JMAOAW, MAOAWB, None, WBSIRY, None, None, QBMJVH
            ),
            BSIRYX: GeckoEnumStructAccessor(
                self.struct, BSIRYX, YYLIUX, YXBQFY, RYXBQF, None, XFEFJT, QBMJVH
            ),
            XBQFYL: GeckoByteStructAccessor(self.struct, XBQFYL, BQFYLJ, QBMJVH),
            QFYLJU: GeckoTempStructAccessor(self.struct, QFYLJU, FYLJUI, QBMJVH),
            YLJUIK: GeckoTempStructAccessor(self.struct, YLJUIK, LJUIKF, QBMJVH),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, UIKFWR, None, KFWRKI, None, None, QBMJVH
            ),
            FWRKIN: GeckoByteStructAccessor(self.struct, FWRKIN, WRKINE, QBMJVH),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, QBMJVH),
            INEJNI: GeckoEnumStructAccessor(
                self.struct, INEJNI, NEJNIB, None, NIBXYB, None, None, QBMJVH
            ),
            IBXYBQ: GeckoByteStructAccessor(self.struct, IBXYBQ, BXYBQS, QBMJVH),
            XYBQSN: GeckoByteStructAccessor(self.struct, XYBQSN, YBQSNQ, QBMJVH),
            BQSNQL: GeckoEnumStructAccessor(
                self.struct, BQSNQL, QSNQLN, None, NQLNMH, None, None, QBMJVH
            ),
            QLNMHX: GeckoEnumStructAccessor(
                self.struct, QLNMHX, LNMHXE, None, ILXWAJ, None, None, QBMJVH
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XWAJVD, None, ILXWAJ, None, None, QBMJVH
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, AJVDQL, None, ILXWAJ, None, None, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, VDQLAI, None, ILXWAJ, None, None, QBMJVH
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, QLAIID, None, ILXWAJ, None, None, QBMJVH
            ),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AIIDNI, None, ILXWAJ, None, None, QBMJVH
            ),
            IIDNIB: GeckoEnumStructAccessor(
                self.struct, IIDNIB, IDNIBX, None, ILXWAJ, None, None, QBMJVH
            ),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, NIBXTI, None, ILXWAJ, None, None, QBMJVH
            ),
            IBXTIA: GeckoEnumStructAccessor(
                self.struct, IBXTIA, BXTIAC, None, ILXWAJ, None, None, QBMJVH
            ),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, TIACQF, None, ILXWAJ, None, None, QBMJVH
            ),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, ACQFFT, None, ILXWAJ, None, None, QBMJVH
            ),
            CQFFTT: GeckoEnumStructAccessor(
                self.struct, CQFFTT, QFFTTI, None, ILXWAJ, None, None, QBMJVH
            ),
            FFTTID: GeckoEnumStructAccessor(
                self.struct, FFTTID, FTTIDU, None, ILXWAJ, None, None, QBMJVH
            ),
            TTIDUB: GeckoEnumStructAccessor(
                self.struct, TTIDUB, TIDUBS, None, ILXWAJ, None, None, QBMJVH
            ),
            IDUBSS: GeckoEnumStructAccessor(
                self.struct, IDUBSS, DUBSSU, None, ILXWAJ, None, None, QBMJVH
            ),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, QBMJVH),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, QBMJVH),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, QBMJVH),
            UBYGDS: GeckoByteStructAccessor(self.struct, UBYGDS, BYGDSB, QBMJVH),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, GDSBDJ, None, DSBDJQ, None, None, QBMJVH
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, None, DSBDJQ, None, None, QBMJVH
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, None, DSBDJQ, None, None, QBMJVH
            ),
            QRJJJV: GeckoEnumStructAccessor(
                self.struct, QRJJJV, RJJJVY, None, DSBDJQ, None, None, QBMJVH
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, JJVYFC, None, DSBDJQ, None, None, QBMJVH
            ),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, VYFCRT, None, DSBDJQ, None, None, QBMJVH
            ),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, QBMJVH),
            CRTFMN: GeckoTimeStructAccessor(self.struct, CRTFMN, RTFMNH, QBMJVH),
            TFMNHT: GeckoTimeStructAccessor(self.struct, TFMNHT, FMNHTB, QBMJVH),
            MNHTBJ: GeckoTimeStructAccessor(self.struct, MNHTBJ, NHTBJE, QBMJVH),
            HTBJEU: GeckoTimeStructAccessor(self.struct, HTBJEU, TBJEUT, QBMJVH),
            BJEUTO: GeckoTimeStructAccessor(self.struct, BJEUTO, JEUTOP, QBMJVH),
            EUTOPH: GeckoEnumStructAccessor(
                self.struct, EUTOPH, UTOPHU, None, OPHUGT, None, None, QBMJVH
            ),
            PHUGTY: GeckoBoolStructAccessor(
                self.struct, PHUGTY, HUGTYI, UXFEFJ, QBMJVH
            ),
            UGTYIY: GeckoBoolStructAccessor(
                self.struct, UGTYIY, GTYIYW, XFEFJT, QBMJVH
            ),
            TYIYWS: GeckoBoolStructAccessor(
                self.struct, TYIYWS, GTYIYW, UXFEFJ, QBMJVH
            ),
            YIYWSK: GeckoBoolStructAccessor(
                self.struct, YIYWSK, GTYIYW, IYWSKW, QBMJVH
            ),
            YWSKWI: GeckoBoolStructAccessor(
                self.struct, YWSKWI, GTYIYW, YXBQFY, QBMJVH
            ),
            WSKWIV: GeckoBoolStructAccessor(
                self.struct, WSKWIV, GTYIYW, SKWIVD, QBMJVH
            ),
            KWIVDN: GeckoEnumStructAccessor(
                self.struct, KWIVDN, WIVDNQ, None, DNQGVU, None, None, QBMJVH
            ),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, QGVUNX, None, UNXNKM, None, None, QBMJVH
            ),
            NXNKML: GeckoByteStructAccessor(self.struct, NXNKML, XNKMLO, QBMJVH),
            NKMLOI: GeckoEnumStructAccessor(
                self.struct, NKMLOI, KMLOIJ, None, OIJUGS, None, None, QBMJVH
            ),
            IJUGSE: GeckoWordStructAccessor(self.struct, IJUGSE, JUGSEL, QBMJVH),
            UGSELH: GeckoEnumStructAccessor(
                self.struct, UGSELH, YYLIUX, IYWSKW, ELHBQN, None, XFEFJT, QBMJVH
            ),
            LHBQNR: GeckoBoolStructAccessor(
                self.struct, LHBQNR, YYLIUX, HBQNRX, QBMJVH
            ),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, YYLIUX, SKWIVD, RXCHWD, None, XFEFJT, QBMJVH
            ),
            XCHWDA: GeckoBoolStructAccessor(
                self.struct, XCHWDA, YYLIUX, CHWDAF, QBMJVH
            ),
            HWDAFI: GeckoBoolStructAccessor(
                self.struct, HWDAFI, YYLIUX, WDAFIK, QBMJVH
            ),
            DAFIKJ: GeckoBoolStructAccessor(
                self.struct, DAFIKJ, AFIKJP, UXFEFJ, QBMJVH
            ),
            FIKJPU: GeckoEnumStructAccessor(
                self.struct, FIKJPU, AFIKJP, WDAFIK, JPUNRJ, None, XFEFJT, QBMJVH
            ),
            PUNRJZ: GeckoEnumStructAccessor(
                self.struct, PUNRJZ, AFIKJP, HBQNRX, DZXNQT, None, ZXNQTM, QBMJVH
            ),
            SSRURA: GeckoBoolStructAccessor(
                self.struct, SSRURA, AFIKJP, IYWSKW, QBMJVH
            ),
            SRURAZ: GeckoBoolStructAccessor(
                self.struct, SRURAZ, AFIKJP, XFEFJT, RURAZM
            ),
            URAZMK: GeckoEnumStructAccessor(
                self.struct, URAZMK, RAZMKQ, XFEFJT, MKQTDK, None, HBQNRX, QBMJVH
            ),
            KQTDKH: GeckoByteStructAccessor(self.struct, KQTDKH, QTDKHT, QBMJVH),
            TDKHTZ: GeckoBoolStructAccessor(
                self.struct, TDKHTZ, DKHTZB, UXFEFJ, QBMJVH
            ),
        }

#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT-V2 v60'
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
ACCPQI = 120
ACMCVD = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
ACQFFT = 93
AFIKJP = 110
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
AIIDNI = 88
AIVEMV = 60
AJVDQL = 85
AKQXPI = "".join(chr(c) for c in [65, 85, 88])
AKSTSE = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
AMJMAO = 33
AOAWBS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
AONPYY = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
ASSAKQ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
ATDZXN = "".join(chr(c) for c in [66, 76, 85, 69])
AWBSIR = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
BBEKBD = 121
BDJQRJ = 105
BEKBDF = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
BHZVOA = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
BIAMJM = 1
BJEUTO = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
BJLOIN = 127
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 66
BQNRXC = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
BQSNQL = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
BSIRYX = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
BSKSOK = 50
BSSUHB = 98
BVWVUB = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
BWJYKL = "".join(chr(c) for c in [80, 49])
BXIBHZ = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
BXTIAC = 91
BXYBQS = 53
BYGDSB = 103
CBFEGZ = 43
CCPQIP = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
CGETIX = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
CHWDAF = 6
CMCVDS = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
CPQIPO = 32
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
CRTFMN = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
CVDSSR = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
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
DDPMXF = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
DFSROG = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
DGKEAK = 111
DJQRJJ = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
DNIBXT = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
DNQGVU = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
DPMXFU = 125
DQLAII = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
DSSRUR = "".join(chr(c) for c in [73, 100, 111, 108])
DUBSSU = 97
DZXNQT = "".join(chr(c) for c in [67, 89, 65, 78])
EAKSTS = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EEZFET = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
EFJTAC = 0
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
EKBDFS = 123
EKCWAO = "".join(chr(c) for c in [76, 73])
EKVKZI = "".join(chr(c) for c in [70, 50, 50])
ELHBQN = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
ELWUEU = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
EMCGET = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
ETDRXA = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
ETIXQV = "".join(chr(c) for c in [67, 111, 97, 115, 116])
EUHNNX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
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
EZFETD = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
FCRTFM = 3
FEGZUQ = 44
FETDRX = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
FFTTID = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
FIKJPU = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
FJBIAM = 63
FJTACC = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
FMNHTB = 6
FSROGM = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
FTTIDU = 95
FUBJLO = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
FWRKIN = "".join(
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
FXQGLR = 26
FYLJUI = 68
GDSBDJ = 104
GETIXQ = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
GKEAKS = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
GLRAHE = 36
GMDDPM = 124
GSELHB = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
GTYIYW = 72
GVUNXN = 73
GYOUSP = "".join(
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
GZUQEX = 45
HBQNRX = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
HBVWVU = 100
HBXIBH = "".join(chr(c) for c in [77, 65, 65, 88])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 38
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(chr(c) for c in [79, 117, 116, 49, 50])
HNNXWE = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
HTBJEU = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
HTZBBE = 113
HUGTYI = 82
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 57])
HWDAFI = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
HXEKVK = "".join(chr(c) for c in [70, 51])
HZVOAC = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
IACQFF = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
IAMJMA = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
IBHZVO = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
IBXTIA = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
IBXYBQ = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
ICXQIE = 14
IDNIBX = 89
IDUBSS = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
IEFXQG = 16
IFJBIA = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
IGYOUS = 60
IHBXIB = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
IIDNIB = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
IKFWRK = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
IKJPUN = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
INEJNI = "".join(chr(c) for c in [85, 76])
INELWU = "".join(chr(c) for c in [52])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
IRYXBQ = 3
IUSOOQ = 23
IUXFEF = 81
IVDNQG = 76
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
IYWSKW = "".join(
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
JBIAMJ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
JEUTOP = 10
JHIUSO = 22
JIGYOU = "".join(
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
JJJVYF = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
JJVYFC = 108
JLOINE = "".join(chr(c) for c in [49])
JMAOAW = "".join(chr(c) for c in [67])
JMCBFE = 42
JNIBXY = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
JPUNRJ = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
JQRJJJ = 106
JRJHIU = 21
JTACCP = 118
JUGSEL = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
JUIKFW = "".join(chr(c) for c in [78, 105, 103, 104, 116])
JUTYEK = 119
JVDQLA = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
JWMNZM = "".join(
    chr(c) for c in [65, 117, 120, 65, 115, 66, 117, 98, 98, 108, 101, 71, 101, 110]
)
JYKLGQ = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
JZTATD = "".join(chr(c) for c in [82, 69, 68])
KBDFSR = "".join(chr(c) for c in [82, 71, 66])
KEAKST = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
KFWRKI = 77
KHTZBB = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
KINEJN = 51
KJPUNR = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
KLGQPL = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
KMLOIJ = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 56])
KQTDKH = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
KSOKPH = 17
KSTSEM = "".join(chr(c) for c in [65, 108, 112, 115])
KVKZIL = "".join(chr(c) for c in [70, 50, 51])
KWIVDN = 5
KXSJWM = "".join(chr(c) for c in [76, 111])
KZILXW = "".join(chr(c) for c in [76, 105, 110, 101, 50])
LAIIDN = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
LASSAK = "".join(chr(c) for c in [70, 97, 110])
LGQPLS = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
LIUXFE = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
LJUIKF = 70
LKXSJW = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
LNMHXE = 83
LOIJUG = "".join(chr(c) for c in [65, 109, 80, 109])
LOINEL = "".join(chr(c) for c in [50])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
LSXUJU = 48
LWUEUH = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
LXWAJV = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
MCGETI = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
MCVDSS = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
MDDPMX = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
MFZDGK = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
MHXEKV = "".join(chr(c) for c in [70, 50])
MJIGYO = 59
MJMAOA = "".join(chr(c) for c in [70])
MJVHFT = 12
MKQTDK = 112
MLOIJU = 34
MNHTBJ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
MNZMJI = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
MOUNBL = 57
MXFUBJ = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
NBLKXS = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
NEJNIB = "".join(chr(c) for c in [67, 69])
NHTBJE = 116
NIBXTI = 90
NIBXYB = 52
NKMLOI = 75
NMHXEK = "".join(chr(c) for c in [70, 49])
NNXWEE = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
NPYYLI = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
NQJYMO = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
NQTMFZ = 8
NRJZTA = "".join(
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
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
NRXCHW = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
NXWEEZ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
NZMJIG = 58
OACMCV = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
OAWBSI = 31
OCTHBS = 39
OGMDDP = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
OIHBXI = "".join(chr(c) for c in [76, 65])
OIJUGS = "".join(chr(c) for c in [50, 52, 104])
OINELW = "".join(chr(c) for c in [51])
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 48])
OKPHUO = 18
ONPYYL = 54
OQNRSJ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
OUNBLK = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
OUSPBW = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
PBWJYK = 78
PFTSIF = 30
PHUGTY = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
PHUOJR = 19
PICXQI = "".join(chr(c) for c in [79, 117, 116, 51])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 29
PMXFUB = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
POUYNQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
PQIPOU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
PYYLIU = 55
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
QFFTTI = 94
QFYLJU = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
QGVUNX = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 53])
QIPOUY = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
QJYMOU = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
QLAIID = 87
QLNMHX = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
QNRSJM = 25
QNRXCH = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
QPLSPF = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
QRJJJV = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
QSNQLN = 74
QTDKHT = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
QTMFZD = "".join(
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
QVXOIH = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 50])
RAHEOC = 37
RAZMKQ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
RJHIUS = "".join(chr(c) for c in [79, 117, 116, 49, 49])
RJJJVY = 107
RJZTAT = "".join(chr(c) for c in [79, 70, 70])
RKINEJ = "".join(chr(c) for c in [85, 76, 95, 67, 69])
RSJMCB = 41
RTFMNH = 4
RURAZM = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
RYXBQF = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
SAKQXP = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
SBDJQR = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
SELHBQ = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
SEMCGE = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 54])
SKWIVD = "".join(
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
SNQLNM = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 55])
SOOQNR = 24
SPBWJY = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
SPFTSI = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
SROGMD = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
SRURAZ = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
SSAKQX = "".join(chr(c) for c in [72, 84, 82, 50])
SSRURA = "".join(chr(c) for c in [65, 115, 112, 101, 110])
SSUHBV = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
STSEMC = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
SUHBVW = 99
SXUJUT = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
TACCPQ = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
TATDZX = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
TBJEUT = 8
TDKHTZ = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
TDRXAI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
TDZXNQ = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
TFMNHT = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
THBSKS = 40
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 92
TIDUBS = 96
TIXQVX = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
TMFZDG = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
TOPHUG = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
TSEMCG = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
TSIFJB = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
TTIDUB = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
TYEKCW = "".join(chr(c) for c in [79, 117, 116, 76, 105])
TYIYWS = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
TZBBEK = "".join(
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
UBJLOI = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
UBSSUH = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
UBYGDS = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
UEUHNN = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
UGSELH = 64
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
UHNNXW = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
UJUTYE = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 65, 115, 67, 80]
)
UNBLKX = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
UNRJZT = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
UNXNKM = "".join(chr(c) for c in [83, 108, 97, 118, 101])
UOJRJH = 20
UQEXLS = 46
URAZMK = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
USOOQN = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
USPBWJ = 62
UTOPHU = 71
UTYEKC = 2
UXFEFJ = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
UYNQJY = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
VDNQGV = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
VDQLAI = 86
VDSSRU = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [76, 105, 110, 101, 49])
VLASSA = "".join(chr(c) for c in [])
VOACMC = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
VUBYGD = 102
VUNXNK = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
VWVUBY = 101
VXOIHB = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
VYFCRT = 109
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
WAONPY = 80
WBSIRY = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
WDAFIK = 7
WEEZFE = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
WIVDNQ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
WMNZMJ = 1
WRKINE = 114
WSKWIV = 4
WUEUHN = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
WVUBYG = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
XBQFYL = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
XCHWDA = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
XEKVKZ = "".join(chr(c) for c in [70, 50, 49])
XFEFJT = "".join(chr(c) for c in [79, 119, 110])
XFUBJL = 126
XIBHZV = "".join(chr(c) for c in [80, 68, 67])
XLSXUJ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
XNKMLO = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
XOIHBX = "".join(chr(c) for c in [74, 97, 122, 122, 105])
XPICXQ = 13
XQIEFX = 15
XQVXOI = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
XSJWMN = "".join(chr(c) for c in [72, 105])
XTIACQ = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
XUJUTY = 49
XWAJVD = 84
XWEEZF = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
XYBQSN = "".join(
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
YBQSNQ = 122
YEKCWA = 79
YFCRTF = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
YGDSBD = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
YIYWSK = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
YKLGQP = 28
YLIUXF = 56
YLJUIK = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
YMOUNB = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
YNQJYM = 27
YOUSPB = 61
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
    chr(c) for c in [65, 117, 120, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
YXBQFY = 35
YYLIUX = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZBBEKB = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZDGKEA = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
ZFETDR = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
ZILXWA = "".join(chr(c) for c in [76, 105, 110, 101, 51])
ZMJIGY = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
ZMKQTD = "".join(
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
ZTATDZ = "".join(chr(c) for c in [71, 82, 69, 69, 78])
ZUQEXL = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
ZVOACM = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
ZXNQTM = "".join(chr(c) for c in [87, 72, 73, 84, 69])
AZMKQT = [
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
    DSSRUR,
    SSRURA,
    SRURAZ,
    RURAZM,
    URAZMK,
    RAZMKQ,
]
BDFSRO = [KBDFSR, ZXNQTM]
BLKXSJ = [OUNBLK, UNBLKX, NBLKXS]
DKHTZB = [QTDKHT, TDKHTZ, VLASSA, VLASSA]
DRXAIV = [
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
    TYEKCW,
]
DSBDJQ = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VKZILX, KZILXW, ZILXWA]
EJNIBX = [INEJNI, NEJNIB]
FEFJTA = [UXFEFJ, XFEFJT]
FZDGKE = [TMFZDG, MFZDGK]
GQPLSP = [KLGQPL, LGQPLS]
IJUGSE = [JVHFTH, LOIJUG, OIJUGS]
ILXWAJ = [NMHXEK, MHXEKV, HXEKVK, XEKVKZ, EKVKZI, KVKZIL, VKZILX, KZILXW, ZILXWA]
JYMOUN = [NQJYMO, QJYMOU]
KCWAON = [
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
    EKCWAO,
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
LHBQNR = [SELHBQ, ELHBQN]
LSPFTS = [PIPIVL, BWJYKL]
MAOAWB = [MJMAOA, JMAOAW]
NELWUE = [VLASSA, JLOINE, LOINEL, OINELW, INELWU]
NQGVUN = [VDNQGV, DNQGVU]
NQLNMH = [FTSIFJ, SNQLNM]
NXNKML = [VLASSA, VUNXNK, UNXNKM]
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
OPHUGT = [JVHFTH, NQJYMO, TOPHUG]
OUYNQJ = [PQIPOU, QIPOUY, IPOUYN, POUYNQ]
PUNRJZ = [KJPUNR, JPUNRJ]
ROGMDD = [FSROGM, SROGMD]
RXAIVE = [EKCWAO]
RXCHWD = [QNRXCH, NRXCHW]
SIFJBI = [FTSIFJ, TSIFJB]
SIRYXB = [WBSIRY, BSIRYX]
SJWMNZ = [KXSJWM, XSJWMN]
UIKFWR = [FTSIFJ, JUIKFW]
WJYKLG = [JVHFTH, BWJYKL, PIPIVL]
XAIVEM = []
XNQTMF = [RJZTAT, JZTATD, ZTATDZ, TATDZX, ATDZXN, TDZXNQ, DZXNQT, ZXNQTM]
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
        return AIVEMV

    @property
    def output_keys(self):
        return DRXAIV

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
            UJUTYE: GeckoBoolStructAccessor(
                self.struct, UJUTYE, JUTYEK, UTYEKC, QBMJVH
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, None, KCWAON, None, None, None
            ),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, None),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoByteStructAccessor(self.struct, NPYYLI, PYYLIU, QBMJVH),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, EFJTAC, FEFJTA, None, UTYEKC, QBMJVH
            ),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, QBMJVH),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, QBMJVH),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, JYMOUN, None, None, QBMJVH
            ),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, MOUNBL, None, BLKXSJ, None, None, QBMJVH
            ),
            LKXSJW: GeckoEnumStructAccessor(
                self.struct, LKXSJW, IUXFEF, UTYEKC, SJWMNZ, None, UTYEKC, QBMJVH
            ),
            JWMNZM: GeckoBoolStructAccessor(
                self.struct, JWMNZM, JUTYEK, WMNZMJ, QBMJVH
            ),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoByteStructAccessor(self.struct, OUSPBW, USPBWJ, QBMJVH),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, WJYKLG, None, None, QBMJVH
            ),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, YKLGQP, None, GQPLSP, None, None, QBMJVH
            ),
            QPLSPF: GeckoEnumStructAccessor(
                self.struct, QPLSPF, PLSPFT, None, LSPFTS, None, None, QBMJVH
            ),
            SPFTSI: GeckoEnumStructAccessor(
                self.struct, SPFTSI, PFTSIF, None, SIFJBI, None, None, QBMJVH
            ),
            IFJBIA: GeckoByteStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoTempStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, AMJMAO, None, MAOAWB, None, None, QBMJVH
            ),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, None, LSPFTS, None, None, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, IUXFEF, IRYXBQ, SIRYXB, None, UTYEKC, QBMJVH
            ),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoTempStructAccessor(self.struct, XBQFYL, BQFYLJ, QBMJVH),
            QFYLJU: GeckoTempStructAccessor(self.struct, QFYLJU, FYLJUI, QBMJVH),
            YLJUIK: GeckoEnumStructAccessor(
                self.struct, YLJUIK, LJUIKF, None, UIKFWR, None, None, QBMJVH
            ),
            IKFWRK: GeckoByteStructAccessor(self.struct, IKFWRK, KFWRKI, QBMJVH),
            FWRKIN: GeckoByteStructAccessor(self.struct, FWRKIN, WRKINE, QBMJVH),
            RKINEJ: GeckoEnumStructAccessor(
                self.struct, RKINEJ, KINEJN, None, EJNIBX, None, None, QBMJVH
            ),
            JNIBXY: GeckoByteStructAccessor(self.struct, JNIBXY, NIBXYB, QBMJVH),
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
                self.struct, PHUGTY, HUGTYI, EFJTAC, QBMJVH
            ),
            UGTYIY: GeckoBoolStructAccessor(
                self.struct, UGTYIY, GTYIYW, UTYEKC, QBMJVH
            ),
            TYIYWS: GeckoBoolStructAccessor(
                self.struct, TYIYWS, GTYIYW, EFJTAC, QBMJVH
            ),
            YIYWSK: GeckoBoolStructAccessor(
                self.struct, YIYWSK, GTYIYW, WMNZMJ, QBMJVH
            ),
            IYWSKW: GeckoBoolStructAccessor(
                self.struct, IYWSKW, GTYIYW, IRYXBQ, QBMJVH
            ),
            YWSKWI: GeckoBoolStructAccessor(
                self.struct, YWSKWI, GTYIYW, WSKWIV, QBMJVH
            ),
            SKWIVD: GeckoBoolStructAccessor(
                self.struct, SKWIVD, GTYIYW, KWIVDN, QBMJVH
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, NQGVUN, None, None, QBMJVH
            ),
            QGVUNX: GeckoEnumStructAccessor(
                self.struct, QGVUNX, GVUNXN, None, NXNKML, None, None, QBMJVH
            ),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, QBMJVH),
            KMLOIJ: GeckoEnumStructAccessor(
                self.struct, KMLOIJ, MLOIJU, None, IJUGSE, None, None, QBMJVH
            ),
            JUGSEL: GeckoWordStructAccessor(self.struct, JUGSEL, UGSELH, QBMJVH),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, IUXFEF, WMNZMJ, LHBQNR, None, UTYEKC, QBMJVH
            ),
            HBQNRX: GeckoBoolStructAccessor(
                self.struct, HBQNRX, IUXFEF, WSKWIV, QBMJVH
            ),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, IUXFEF, KWIVDN, RXCHWD, None, UTYEKC, QBMJVH
            ),
            XCHWDA: GeckoBoolStructAccessor(
                self.struct, XCHWDA, IUXFEF, CHWDAF, QBMJVH
            ),
            HWDAFI: GeckoBoolStructAccessor(
                self.struct, HWDAFI, IUXFEF, WDAFIK, QBMJVH
            ),
            DAFIKJ: GeckoBoolStructAccessor(
                self.struct, DAFIKJ, AFIKJP, EFJTAC, QBMJVH
            ),
            FIKJPU: GeckoBoolStructAccessor(
                self.struct, FIKJPU, AFIKJP, WMNZMJ, QBMJVH
            ),
            IKJPUN: GeckoEnumStructAccessor(
                self.struct, IKJPUN, AFIKJP, UTYEKC, PUNRJZ, None, UTYEKC, QBMJVH
            ),
            UNRJZT: GeckoEnumStructAccessor(
                self.struct, UNRJZT, AFIKJP, IRYXBQ, PUNRJZ, None, UTYEKC, QBMJVH
            ),
            NRJZTA: GeckoEnumStructAccessor(
                self.struct, NRJZTA, AFIKJP, WSKWIV, XNQTMF, None, NQTMFZ, QBMJVH
            ),
            QTMFZD: GeckoEnumStructAccessor(
                self.struct, QTMFZD, AFIKJP, WDAFIK, FZDGKE, None, UTYEKC, QBMJVH
            ),
            ZMKQTD: GeckoBoolStructAccessor(
                self.struct, ZMKQTD, MKQTDK, EFJTAC, QBMJVH
            ),
            KQTDKH: GeckoEnumStructAccessor(
                self.struct, KQTDKH, MKQTDK, UTYEKC, DKHTZB, None, WSKWIV, QBMJVH
            ),
            KHTZBB: GeckoByteStructAccessor(self.struct, KHTZBB, HTZBBE, QBMJVH),
            TZBBEK: GeckoBoolStructAccessor(
                self.struct, TZBBEK, JUTYEK, EFJTAC, QBMJVH
            ),
            ZBBEKB: GeckoByteStructAccessor(self.struct, ZBBEKB, BBEKBD, QBMJVH),
            BEKBDF: GeckoEnumStructAccessor(
                self.struct, BEKBDF, EKBDFS, EFJTAC, BDFSRO, None, UTYEKC, None
            ),
            DFSROG: GeckoEnumStructAccessor(
                self.struct, DFSROG, EKBDFS, WMNZMJ, ROGMDD, None, UTYEKC, None
            ),
            OGMDDP: GeckoEnumStructAccessor(
                self.struct, OGMDDP, GMDDPM, EFJTAC, BDFSRO, None, UTYEKC, None
            ),
            MDDPMX: GeckoEnumStructAccessor(
                self.struct, MDDPMX, GMDDPM, WMNZMJ, ROGMDD, None, UTYEKC, None
            ),
            DDPMXF: GeckoEnumStructAccessor(
                self.struct, DDPMXF, DPMXFU, EFJTAC, BDFSRO, None, UTYEKC, None
            ),
            PMXFUB: GeckoEnumStructAccessor(
                self.struct, PMXFUB, DPMXFU, WMNZMJ, ROGMDD, None, UTYEKC, None
            ),
            MXFUBJ: GeckoEnumStructAccessor(
                self.struct, MXFUBJ, XFUBJL, EFJTAC, BDFSRO, None, UTYEKC, None
            ),
            FUBJLO: GeckoEnumStructAccessor(
                self.struct, FUBJLO, XFUBJL, WMNZMJ, ROGMDD, None, UTYEKC, None
            ),
            UBJLOI: GeckoEnumStructAccessor(
                self.struct, UBJLOI, BJLOIN, EFJTAC, NELWUE, None, NQTMFZ, None
            ),
            ELWUEU: GeckoBoolStructAccessor(self.struct, ELWUEU, BJLOIN, WDAFIK, None),
            LWUEUH: GeckoBoolStructAccessor(self.struct, LWUEUH, EKBDFS, WSKWIV, None),
            WUEUHN: GeckoBoolStructAccessor(self.struct, WUEUHN, EKBDFS, KWIVDN, None),
            UEUHNN: GeckoBoolStructAccessor(self.struct, UEUHNN, EKBDFS, CHWDAF, None),
            EUHNNX: GeckoBoolStructAccessor(self.struct, EUHNNX, EKBDFS, WDAFIK, None),
            UHNNXW: GeckoBoolStructAccessor(self.struct, UHNNXW, GMDDPM, WSKWIV, None),
            HNNXWE: GeckoBoolStructAccessor(self.struct, HNNXWE, GMDDPM, KWIVDN, None),
            NNXWEE: GeckoBoolStructAccessor(self.struct, NNXWEE, GMDDPM, CHWDAF, None),
            NXWEEZ: GeckoBoolStructAccessor(self.struct, NXWEEZ, GMDDPM, WDAFIK, None),
            XWEEZF: GeckoBoolStructAccessor(self.struct, XWEEZF, DPMXFU, WSKWIV, None),
            WEEZFE: GeckoBoolStructAccessor(self.struct, WEEZFE, DPMXFU, KWIVDN, None),
            EEZFET: GeckoBoolStructAccessor(self.struct, EEZFET, DPMXFU, CHWDAF, None),
            EZFETD: GeckoBoolStructAccessor(self.struct, EZFETD, DPMXFU, WDAFIK, None),
            ZFETDR: GeckoBoolStructAccessor(self.struct, ZFETDR, XFUBJL, WSKWIV, None),
            FETDRX: GeckoBoolStructAccessor(self.struct, FETDRX, XFUBJL, KWIVDN, None),
            ETDRXA: GeckoBoolStructAccessor(self.struct, ETDRXA, XFUBJL, CHWDAF, None),
            TDRXAI: GeckoBoolStructAccessor(self.struct, TDRXAI, XFUBJL, WDAFIK, None),
        }

#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v62'
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
ACCPQI = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
ACMCVD = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
ACQFFT = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
AHEOCT = 37
AIIDNI = "".join(chr(c) for c in [76, 105, 110, 101, 51])
AIVEMV = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
AJVDQL = "".join(chr(c) for c in [70, 51])
AKQXPI = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
AKSTSE = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
AMJMAO = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
AONPYY = 80
ASSAKQ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
ATDZXN = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
AWBSIR = 31
AZMKQT = "".join(chr(c) for c in [74, 97, 122, 122, 105])
BBEKBD = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
BDFSRO = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
BDJQRJ = 100
BEKBDF = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
BFEGZU = 43
BHZVOA = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
BIAMJM = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
BJEUTO = 109
BJLOIN = "".join(
    chr(c) for c in [83, 105, 110, 103, 108, 101, 80, 117, 109, 112, 75, 101, 121]
)
BLKXSJ = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
BQNRXC = 128
BQSNQL = "".join(chr(c) for c in [85, 76, 95, 67, 69])
BSIRYX = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
BSKSOK = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
BSSUHB = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
BVWVUB = 95
BWJYKL = 78
BXIBHZ = 111
BXTIAC = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
BYGDSB = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
CBFEGZ = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
CCPQIP = 120
CGETIX = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
CHWDAF = "".join(chr(c) for c in [83, 105, 108, 101, 110, 116, 77, 111, 100, 101])
CMCVDS = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
CPQIPO = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
CQBMJV = 0
CQFFTT = 88
CRTFMN = 105
CTHBSK = 39
CVDSSR = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CXQIEF = 14
CZOLSI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
DAFIKJ = "".join(chr(c) for c in [83, 76, 69, 69, 80])
DDPMXF = "".join(
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
DFSROG = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
DGKEAK = "".join(
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
DJQRJJ = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
DKHTZB = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
DMPSCT = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
DNIBXT = 84
DNQGVU = 72
DPMXFU = 112
DQLAII = "".join(chr(c) for c in [70, 50, 51])
DRXAIV = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
DSBDJQ = 99
DSSRUR = "".join(chr(c) for c in [67, 111, 97, 115, 116])
DUBSSU = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
DZXNQT = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
EAKSTS = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EEZFET = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
EFXQGL = 16
EGZUQE = 44
EJNIBX = "".join(chr(c) for c in [65, 85, 84, 79, 95, 87, 95, 66, 79, 79, 83, 84])
EKBDFS = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
EKCWAO = 79
EKVKZI = 122
ELHBQN = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
ELWUEU = "".join(
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
EMCGET = "".join(chr(c) for c in [82, 69, 68])
EMVCYW = "".join(chr(c) for c in [50])
EOCTHB = 38
ETDRXA = 125
ETIXQV = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
EUHNNX = 123
EUTOPH = 3
EXLSXU = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EZFETD = 124
FCRTFM = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
FEFJTA = "".join(chr(c) for c in [79, 119, 110])
FEGZUQ = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
FETDRX = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
FFTTID = 89
FIKJPU = "".join(
    chr(c) for c in [83, 105, 108, 101, 110, 116, 68, 117, 114, 97, 116, 105, 111, 110]
)
FJBIAM = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
FJTACC = 0
FMNHTB = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
FSROGM = "".join(chr(c) for c in [73, 100, 111, 108])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 30
FTTIDU = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
FWRKIN = 77
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
FYLJUI = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
FZCZOL = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
FZDGKE = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
GDSBDJ = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
GETIXQ = "".join(chr(c) for c in [66, 76, 85, 69])
GKEAKS = 110
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
GMDDPM = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
GQPLSP = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
GSELHB = "".join(chr(c) for c in [83, 108, 97, 118, 101])
GTYIYW = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
GVUNXN = "".join(
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
GYOUSP = 60
GZUQEX = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
HBQNRX = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
HBSKSO = 40
HBVWVU = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
HBXIBH = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 22
HTBJEU = 108
HTZBBE = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
HUGTYI = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
HUOJRJ = 19
HWDAFI = 157
HXEKVK = 53
HZVOAC = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
IACQFF = 87
IAMJMA = 1
IBHZVO = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
IBXTIA = 85
IBXYBQ = "".join(chr(c) for c in [66, 79, 84, 72, 95, 72, 69, 65, 84])
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 51])
IDNIBX = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
IDUBSS = 91
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 53])
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
IJUGSE = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
IKJPUN = 158
ILXWAJ = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
INEJNI = "".join(chr(c) for c in [72, 69, 65, 84, 95, 87, 95, 66, 79, 79, 83, 84])
INELWU = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
IPIVLA = "".join(chr(c) for c in [79, 51])
IPMDMP = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
IPOUYN = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
IUSOOQ = "".join(chr(c) for c in [79, 117, 116, 49, 50])
IUXFEF = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
IVDNQG = 82
IVEMVC = 127
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(chr(c) for c in [87, 72, 73, 84, 69])
IYWSKW = 10
JBIAMJ = 63
JEUTOP = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
JHIUSO = "".join(chr(c) for c in [79, 117, 116, 49, 49])
JIGYOU = 59
JJJVYF = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
JJVYFC = 103
JLOINE = "".join(chr(c) for c in [70, 111, 114, 83, 112, 101, 101, 100, 115])
JMAOAW = "".join(chr(c) for c in [70])
JMCBFE = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
JNIBXY = "".join(chr(c) for c in [65, 85, 84, 79, 95, 83, 65, 86, 69, 82])
JPUNRJ = 34
JQRJJJ = 101
JRJHIU = "".join(chr(c) for c in [79, 117, 116, 49, 48])
JTACCP = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
JUGSEL = 73
JUIKFW = 70
JUTYEK = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 65, 115, 67, 80]
)
JVDQLA = "".join(chr(c) for c in [70, 50, 49])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
JYMOUN = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
JZTATD = 64
KBDFSR = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
KCWAON = "".join(chr(c) for c in [76, 73])
KEAKST = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
KFWRKI = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
KHTZBB = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
KINEJN = "".join(chr(c) for c in [67, 72, 73, 76, 76])
KJPUNR = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
KLGQPL = 28
KMLOIJ = 76
KPHUOJ = 18
KQTDKH = "".join(chr(c) for c in [77, 65, 65, 88])
KQXPIC = "".join(chr(c) for c in [65, 85, 88])
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 54])
KSTSEM = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
KVKZIL = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
KXSJWM = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
KZILXW = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
LAIIDN = "".join(chr(c) for c in [76, 105, 110, 101, 50])
LASSAK = "".join(chr(c) for c in [70, 97, 110])
LGQPLS = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
LHBQNR = 75
LIUXFE = 56
LJUIKF = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
LNMHXE = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
LOIJUG = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
LOINEL = "".join(chr(c) for c in [70, 111, 114, 90, 111, 110, 101, 115])
LRAHEO = 36
LSIPMD = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
LSPFTS = 29
LSXUJU = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
LWUEUH = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
LXWAJV = 83
MAOAWB = "".join(chr(c) for c in [67])
MCBFEG = 42
MCGETI = "".join(chr(c) for c in [71, 82, 69, 69, 78])
MCVDSS = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
MDMPSC = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
MFZDGK = 6
MHXEKV = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
MJIGYO = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
MJMAOA = 33
MJVHFT = 12
MKQTDK = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
MLOIJU = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
MNHTBJ = 107
MNZMJI = 1
MOUNBL = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
MPSCTT = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
MVCYWO = "".join(chr(c) for c in [51])
MXFUBJ = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
NBLKXS = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
NEJNIB = "".join(chr(c) for c in [72, 69, 65, 84, 95, 83, 65, 86, 69, 82])
NELWUE = 113
NFZCZO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
NHTBJE = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
NIBXTI = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
NIBXYB = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76, 95, 72, 69, 65, 84])
NKMLOI = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
NMHXEK = 52
NNXWEE = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
NPYYLI = 54
NQGVUN = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
NQJYMO = 27
NQLNMH = "".join(chr(c) for c in [67, 69])
NQTMFZ = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
NRSJMC = 25
NRXCHW = 130
NXNKML = "".join(
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
NXWEEZ = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
NZMJIG = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
OACMCV = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
OAWBSI = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
OGMDDP = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
OIHBXI = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
OJRJHI = 20
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 55])
OLSIPM = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
ONFZCZ = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
ONPYYL = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
OOQNRS = 24
OPHUGT = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
OUNBLK = 57
OUSPBW = 61
OUYNQJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
PBWJYK = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
PFTSIF = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
PHUGTY = 6
PHUOJR = "".join(chr(c) for c in [79, 117, 116, 56])
PICXQI = 13
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
PMDMPS = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
PMXFUB = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
POUYNQ = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
PQIPOU = 32
PSCTTG = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
PUNRJZ = "".join(chr(c) for c in [65, 109, 80, 109])
PYYLIU = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 46
QFFTTI = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
QFYLJU = 66
QGVUNX = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
QIEFXQ = 15
QIPOUY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
QJYMOU = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
QLAIID = "".join(chr(c) for c in [76, 105, 110, 101, 49])
QNRSJM = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
QNRXCH = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
QRJJJV = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
QSNQLN = 51
QTDKHT = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
QVXOIH = 8
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
RAZMKQ = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
RJHIUS = 21
RJJJVY = 102
RJZTAT = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
RKINEJ = 115
ROGMDD = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
RSJMCB = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
RTFMNH = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
RURAZM = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
RXAIVE = 126
RXCHWD = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
RYXBQF = 3
SAKQXP = "".join(chr(c) for c in [72, 84, 82, 50])
SBDJQR = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
SEMCGE = "".join(
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
SIFJBI = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
SIPMDM = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
SIRYXB = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
SJMCBF = 41
SJWMNZ = "".join(chr(c) for c in [72, 105])
SKSOKP = 50
SKWIVD = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
SNQLNM = "".join(chr(c) for c in [85, 76])
SOKPHU = 17
SOOQNR = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
SPBWJY = 62
SROGMD = "".join(chr(c) for c in [65, 115, 112, 101, 110])
SRURAZ = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
SSAKQX = "".join(chr(c) for c in [79, 78, 90, 69, 78])
SSRURA = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
SSUHBV = 93
SUHBVW = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
SXUJUT = 48
TACCPQ = 118
TATDZX = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
TBJEUT = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
TDKHTZ = "".join(chr(c) for c in [80, 68, 67])
TDRXAI = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
TFMNHT = 106
TGCRHY = 62
THBSKS = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
TIDUBS = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
TIXQVX = "".join(chr(c) for c in [67, 89, 65, 78])
TMFZDG = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
TOPHUG = 4
TSEMCG = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
TSIFJB = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
TTIDUB = 90
TYEKCW = 2
TYIYWS = 8
TZBBEK = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
UBJLOI = "".join(
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
UBSSUH = 92
UBYGDS = 97
UEUHNN = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
UGSELH = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
UGTYIY = 116
UHBVWV = 94
UHNNXW = "".join(chr(c) for c in [82, 71, 66])
UIKFWR = "".join(chr(c) for c in [78, 105, 103, 104, 116])
UJUTYE = 49
UNBLKX = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
UNRJZT = "".join(chr(c) for c in [50, 52, 104])
UNXNKM = 4
UOJRJH = "".join(chr(c) for c in [79, 117, 116, 57])
UQEXLS = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
URAZMK = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
USOOQN = 23
USPBWJ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
UTOPHU = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
UTYEKC = 119
UXFEFJ = 81
VCYWON = "".join(chr(c) for c in [52])
VDNQGV = "".join(
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
VDQLAI = "".join(chr(c) for c in [70, 50, 50])
VDSSRU = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
VEMVCY = "".join(chr(c) for c in [49])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 74
VLASSA = "".join(chr(c) for c in [])
VOACMC = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
VUBYGD = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
VUNXNK = "".join(
    chr(c) for c in [65, 117, 120, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
VWVUBY = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
VXOIHB = "".join(
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
VYFCRT = 104
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [70, 50])
WAONPY = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
WBSIRY = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
WDAFIK = "".join(chr(c) for c in [79, 70, 70])
WIVDNQ = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
WJYKLG = "".join(chr(c) for c in [80, 49])
WMNZMJ = "".join(
    chr(c) for c in [65, 117, 120, 65, 115, 66, 117, 98, 98, 108, 101, 71, 101, 110]
)
WONFZC = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
WRKINE = "".join(
    chr(c) for c in [67, 111, 111, 108, 90, 111, 110, 101, 77, 111, 100, 101]
)
WSKWIV = 71
WUEUHN = 121
WVUBYG = 96
XAIVEM = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
XBQFYL = 35
XCHWDA = 132
XEKVKZ = "".join(
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
XFEFJT = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
XFUBJL = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
XIBHZV = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
XLSXUJ = 47
XNKMLO = 5
XNQTMF = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
XOIHBX = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 50])
XQGLRA = 26
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 52])
XSJWMN = "".join(chr(c) for c in [76, 111])
XTIACQ = 86
XUJUTY = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
XWAJVD = "".join(chr(c) for c in [70, 49])
XWEEZF = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
XYBQSN = "".join(
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
YBQSNQ = 114
YEKCWA = "".join(chr(c) for c in [79, 117, 116, 76, 105])
YGDSBD = 98
YIYWSK = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
YKLGQP = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
YLIUXF = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
YLJUIK = 68
YNQJYM = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
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
YWONFZ = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
YWSKWI = "".join(
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
YXBQFY = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
YYLIUX = 55
YYPIPI = "".join(chr(c) for c in [80, 53])
ZBBEKB = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZCZOLS = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
ZDGKEA = 7
ZFETDR = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
ZMJIGY = 58
ZMKQTD = "".join(chr(c) for c in [76, 65])
ZOLSIP = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
ZTATDZ = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
ZUQEXL = 45
ZVOACM = "".join(chr(c) for c in [65, 108, 112, 115])
ZXNQTM = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
AFIKJP = [JVHFTH, WDAFIK, VLASSA, DAFIKJ]
AOAWBS = [JMAOAW, MAOAWB]
BXYBQS = [KINEJN, INEJNI, NEJNIB, EJNIBX, JNIBXY, NIBXYB, IBXYBQ]
CTTGCR = [KCWAON]
CWAONP = [
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
    KCWAON,
]
CYWONF = [VLASSA, VEMVCY, EMVCYW, MVCYWO, VCYWON]
EFJTAC = [XFEFJT, FEFJTA]
FUBJLO = [MXFUBJ, XFUBJL, VLASSA, VLASSA]
HNNXWE = [UHNNXW, IXQVXO]
IFJBIA = [TSIFJB, SIFJBI]
IHBXIB = [XOIHBX, OIHBXI]
IIDNIB = [XWAJVD, WAJVDQ, AJVDQL, JVDQLA, VDQLAI, DQLAII, QLAIID, LAIIDN, AIIDNI]
IKFWRK = [TSIFJB, UIKFWR]
IRYXBQ = [BSIRYX, SIRYXB]
JWMNZM = [XSJWMN, SJWMNZ]
JYKLGQ = [JVHFTH, WJYKLG, PIPIVL]
KWIVDN = [JVHFTH, QJYMOU, SKWIVD]
LKXSJW = [UNBLKX, NBLKXS, BLKXSJ]
MDDPMX = [
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
    AZMKQT,
    ZMKQTD,
    MKQTDK,
    KQTDKH,
    QTDKHT,
    TDKHTZ,
    DKHTZB,
    KHTZBB,
    HTZBBE,
    TZBBEK,
    ZBBEKB,
    BBEKBD,
    BEKBDF,
    EKBDFS,
    KBDFSR,
    BDFSRO,
    DFSROG,
    FSROGM,
    SROGMD,
    ROGMDD,
    OGMDDP,
    GMDDPM,
]
NRJZTA = [JVHFTH, PUNRJZ, UNRJZT]
OIJUGS = [MLOIJU, LOIJUG]
OINELW = [JVHFTH, JLOINE, LOINEL, VLASSA]
OQNRSJ = [
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
QGLRAH = [
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
    SAKQXP,
]
QLNMHX = [SNQLNM, NQLNMH]
QPLSPF = [LGQPLS, GQPLSP]
QTMFZD = [XNQTMF, NQTMFZ]
QXPICX = [
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
    SSAKQX,
    VLASSA,
    SAKQXP,
    AKQXPI,
    KQXPIC,
]
SCTTGC = [
    BMJVHF,
    XPICXQ,
    ICXQIE,
    XQIEFX,
    IEFXQG,
    FXQGLR,
    KSOKPH,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    JRJHIU,
    JHIUSO,
    IUSOOQ,
    SOOQNR,
    QNRSJM,
    YEKCWA,
]
SELHBQ = [VLASSA, UGSELH, GSELHB]
SPFTSI = [PIPIVL, WJYKLG]
STSEMC = [AKSTSE, KSTSEM]
TDZXNQ = [TATDZX, ATDZXN]
TTGCRH = []
UYNQJY = [QIPOUY, IPOUYN, POUYNQ, OUYNQJ]
WEEZFE = [NXWEEZ, XWEEZF]
XQVXOI = [WDAFIK, EMCGET, MCGETI, CGETIX, GETIXQ, ETIXQV, TIXQVX, IXQVXO]
YFCRTF = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, QLAIID, LAIIDN, AIIDNI]
YMOUNB = [QJYMOU, JYMOUN]
ZILXWA = [TSIFJB, KZILXW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return TGCRHY

    @property
    def output_keys(self):
        return SCTTGC

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, QXPICX, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, QXPICX, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, QXPICX, None, None, QBMJVH
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, QIEFXQ, None, QXPICX, None, None, QBMJVH
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, None, QXPICX, None, None, QBMJVH
            ),
            FXQGLR: GeckoEnumStructAccessor(
                self.struct, FXQGLR, XQGLRA, None, QGLRAH, None, None, QBMJVH
            ),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoByteStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, QBMJVH),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, QBMJVH),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, QBMJVH),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, QXPICX, None, None, QBMJVH
            ),
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, QXPICX, None, None, QBMJVH
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, None, QXPICX, None, None, QBMJVH
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, QXPICX, None, None, QBMJVH
            ),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, RJHIUS, None, QXPICX, None, None, QBMJVH
            ),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, HIUSOO, None, QXPICX, None, None, QBMJVH
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, None, QXPICX, None, None, QBMJVH
            ),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, None, OQNRSJ, None, None, QBMJVH
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, NRSJMC, None, OQNRSJ, None, None, QBMJVH
            ),
            RSJMCB: GeckoByteStructAccessor(self.struct, RSJMCB, SJMCBF, QBMJVH),
            JMCBFE: GeckoByteStructAccessor(self.struct, JMCBFE, MCBFEG, QBMJVH),
            CBFEGZ: GeckoByteStructAccessor(self.struct, CBFEGZ, BFEGZU, QBMJVH),
            FEGZUQ: GeckoByteStructAccessor(self.struct, FEGZUQ, EGZUQE, QBMJVH),
            GZUQEX: GeckoByteStructAccessor(self.struct, GZUQEX, ZUQEXL, QBMJVH),
            UQEXLS: GeckoByteStructAccessor(self.struct, UQEXLS, QEXLSX, QBMJVH),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, QBMJVH),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoByteStructAccessor(self.struct, XUJUTY, UJUTYE, QBMJVH),
            JUTYEK: GeckoBoolStructAccessor(
                self.struct, JUTYEK, UTYEKC, TYEKCW, QBMJVH
            ),
            YEKCWA: GeckoEnumStructAccessor(
                self.struct, YEKCWA, EKCWAO, None, CWAONP, None, None, None
            ),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, None),
            ONPYYL: GeckoByteStructAccessor(self.struct, ONPYYL, NPYYLI, QBMJVH),
            PYYLIU: GeckoByteStructAccessor(self.struct, PYYLIU, YYLIUX, QBMJVH),
            YLIUXF: GeckoByteStructAccessor(self.struct, YLIUXF, LIUXFE, QBMJVH),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, UXFEFJ, FJTACC, EFJTAC, None, TYEKCW, QBMJVH
            ),
            JTACCP: GeckoByteStructAccessor(self.struct, JTACCP, TACCPQ, QBMJVH),
            ACCPQI: GeckoByteStructAccessor(self.struct, ACCPQI, CCPQIP, QBMJVH),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, PQIPOU, None, UYNQJY, None, None, QBMJVH
            ),
            YNQJYM: GeckoEnumStructAccessor(
                self.struct, YNQJYM, NQJYMO, None, YMOUNB, None, None, QBMJVH
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, LKXSJW, None, None, QBMJVH
            ),
            KXSJWM: GeckoEnumStructAccessor(
                self.struct, KXSJWM, UXFEFJ, TYEKCW, JWMNZM, None, TYEKCW, QBMJVH
            ),
            WMNZMJ: GeckoBoolStructAccessor(
                self.struct, WMNZMJ, UTYEKC, MNZMJI, QBMJVH
            ),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoByteStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoByteStructAccessor(self.struct, IGYOUS, GYOUSP, QBMJVH),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoByteStructAccessor(self.struct, USPBWJ, SPBWJY, QBMJVH),
            PBWJYK: GeckoEnumStructAccessor(
                self.struct, PBWJYK, BWJYKL, None, JYKLGQ, None, None, QBMJVH
            ),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, QPLSPF, None, None, QBMJVH
            ),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, IFJBIA, None, None, QBMJVH
            ),
            FJBIAM: GeckoByteStructAccessor(self.struct, FJBIAM, JBIAMJ, QBMJVH),
            BIAMJM: GeckoTempStructAccessor(self.struct, BIAMJM, IAMJMA, QBMJVH),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, MJMAOA, None, AOAWBS, None, None, QBMJVH
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, SPFTSI, None, None, QBMJVH
            ),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, UXFEFJ, RYXBQF, IRYXBQ, None, TYEKCW, QBMJVH
            ),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoTempStructAccessor(self.struct, BQFYLJ, QFYLJU, QBMJVH),
            FYLJUI: GeckoTempStructAccessor(self.struct, FYLJUI, YLJUIK, QBMJVH),
            LJUIKF: GeckoEnumStructAccessor(
                self.struct, LJUIKF, JUIKFW, None, IKFWRK, None, None, QBMJVH
            ),
            KFWRKI: GeckoByteStructAccessor(self.struct, KFWRKI, FWRKIN, QBMJVH),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, RKINEJ, None, BXYBQS, None, None, QBMJVH
            ),
            XYBQSN: GeckoByteStructAccessor(self.struct, XYBQSN, YBQSNQ, QBMJVH),
            BQSNQL: GeckoEnumStructAccessor(
                self.struct, BQSNQL, QSNQLN, None, QLNMHX, None, None, QBMJVH
            ),
            LNMHXE: GeckoByteStructAccessor(self.struct, LNMHXE, NMHXEK, QBMJVH),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoByteStructAccessor(self.struct, XEKVKZ, EKVKZI, QBMJVH),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, VKZILX, None, ZILXWA, None, None, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, LXWAJV, None, IIDNIB, None, None, QBMJVH
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, DNIBXT, None, IIDNIB, None, None, QBMJVH
            ),
            NIBXTI: GeckoEnumStructAccessor(
                self.struct, NIBXTI, IBXTIA, None, IIDNIB, None, None, QBMJVH
            ),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, XTIACQ, None, IIDNIB, None, None, QBMJVH
            ),
            TIACQF: GeckoEnumStructAccessor(
                self.struct, TIACQF, IACQFF, None, IIDNIB, None, None, QBMJVH
            ),
            ACQFFT: GeckoEnumStructAccessor(
                self.struct, ACQFFT, CQFFTT, None, IIDNIB, None, None, QBMJVH
            ),
            QFFTTI: GeckoEnumStructAccessor(
                self.struct, QFFTTI, FFTTID, None, IIDNIB, None, None, QBMJVH
            ),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, TTIDUB, None, IIDNIB, None, None, QBMJVH
            ),
            TIDUBS: GeckoEnumStructAccessor(
                self.struct, TIDUBS, IDUBSS, None, IIDNIB, None, None, QBMJVH
            ),
            DUBSSU: GeckoEnumStructAccessor(
                self.struct, DUBSSU, UBSSUH, None, IIDNIB, None, None, QBMJVH
            ),
            BSSUHB: GeckoEnumStructAccessor(
                self.struct, BSSUHB, SSUHBV, None, IIDNIB, None, None, QBMJVH
            ),
            SUHBVW: GeckoEnumStructAccessor(
                self.struct, SUHBVW, UHBVWV, None, IIDNIB, None, None, QBMJVH
            ),
            HBVWVU: GeckoEnumStructAccessor(
                self.struct, HBVWVU, BVWVUB, None, IIDNIB, None, None, QBMJVH
            ),
            VWVUBY: GeckoEnumStructAccessor(
                self.struct, VWVUBY, WVUBYG, None, IIDNIB, None, None, QBMJVH
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, IIDNIB, None, None, QBMJVH
            ),
            BYGDSB: GeckoByteStructAccessor(self.struct, BYGDSB, YGDSBD, QBMJVH),
            GDSBDJ: GeckoByteStructAccessor(self.struct, GDSBDJ, DSBDJQ, QBMJVH),
            SBDJQR: GeckoByteStructAccessor(self.struct, SBDJQR, BDJQRJ, QBMJVH),
            DJQRJJ: GeckoByteStructAccessor(self.struct, DJQRJJ, JQRJJJ, QBMJVH),
            QRJJJV: GeckoByteStructAccessor(self.struct, QRJJJV, RJJJVY, QBMJVH),
            JJJVYF: GeckoByteStructAccessor(self.struct, JJJVYF, JJVYFC, QBMJVH),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, VYFCRT, None, YFCRTF, None, None, QBMJVH
            ),
            FCRTFM: GeckoEnumStructAccessor(
                self.struct, FCRTFM, CRTFMN, None, YFCRTF, None, None, QBMJVH
            ),
            RTFMNH: GeckoEnumStructAccessor(
                self.struct, RTFMNH, TFMNHT, None, YFCRTF, None, None, QBMJVH
            ),
            FMNHTB: GeckoEnumStructAccessor(
                self.struct, FMNHTB, MNHTBJ, None, YFCRTF, None, None, QBMJVH
            ),
            NHTBJE: GeckoEnumStructAccessor(
                self.struct, NHTBJE, HTBJEU, None, YFCRTF, None, None, QBMJVH
            ),
            TBJEUT: GeckoEnumStructAccessor(
                self.struct, TBJEUT, BJEUTO, None, YFCRTF, None, None, QBMJVH
            ),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, QBMJVH),
            UTOPHU: GeckoTimeStructAccessor(self.struct, UTOPHU, TOPHUG, QBMJVH),
            OPHUGT: GeckoTimeStructAccessor(self.struct, OPHUGT, PHUGTY, QBMJVH),
            HUGTYI: GeckoTimeStructAccessor(self.struct, HUGTYI, UGTYIY, QBMJVH),
            GTYIYW: GeckoTimeStructAccessor(self.struct, GTYIYW, TYIYWS, QBMJVH),
            YIYWSK: GeckoTimeStructAccessor(self.struct, YIYWSK, IYWSKW, QBMJVH),
            YWSKWI: GeckoEnumStructAccessor(
                self.struct, YWSKWI, WSKWIV, None, KWIVDN, None, None, QBMJVH
            ),
            WIVDNQ: GeckoBoolStructAccessor(
                self.struct, WIVDNQ, IVDNQG, FJTACC, QBMJVH
            ),
            VDNQGV: GeckoBoolStructAccessor(
                self.struct, VDNQGV, DNQGVU, TYEKCW, QBMJVH
            ),
            NQGVUN: GeckoBoolStructAccessor(
                self.struct, NQGVUN, DNQGVU, FJTACC, QBMJVH
            ),
            QGVUNX: GeckoBoolStructAccessor(
                self.struct, QGVUNX, DNQGVU, MNZMJI, QBMJVH
            ),
            GVUNXN: GeckoBoolStructAccessor(
                self.struct, GVUNXN, DNQGVU, RYXBQF, QBMJVH
            ),
            VUNXNK: GeckoBoolStructAccessor(
                self.struct, VUNXNK, DNQGVU, UNXNKM, QBMJVH
            ),
            NXNKML: GeckoBoolStructAccessor(
                self.struct, NXNKML, DNQGVU, XNKMLO, QBMJVH
            ),
            NKMLOI: GeckoEnumStructAccessor(
                self.struct, NKMLOI, KMLOIJ, None, OIJUGS, None, None, QBMJVH
            ),
            IJUGSE: GeckoEnumStructAccessor(
                self.struct, IJUGSE, JUGSEL, None, SELHBQ, None, None, QBMJVH
            ),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, QBMJVH),
            HBQNRX: GeckoTimeStructAccessor(self.struct, HBQNRX, BQNRXC, QBMJVH),
            QNRXCH: GeckoTimeStructAccessor(self.struct, QNRXCH, NRXCHW, QBMJVH),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, QBMJVH),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, HWDAFI, None, AFIKJP, None, None, QBMJVH
            ),
            FIKJPU: GeckoTimeStructAccessor(self.struct, FIKJPU, IKJPUN, QBMJVH),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, JPUNRJ, None, NRJZTA, None, None, QBMJVH
            ),
            RJZTAT: GeckoWordStructAccessor(self.struct, RJZTAT, JZTATD, QBMJVH),
            ZTATDZ: GeckoEnumStructAccessor(
                self.struct, ZTATDZ, UXFEFJ, MNZMJI, TDZXNQ, None, TYEKCW, QBMJVH
            ),
            DZXNQT: GeckoBoolStructAccessor(
                self.struct, DZXNQT, UXFEFJ, UNXNKM, QBMJVH
            ),
            ZXNQTM: GeckoEnumStructAccessor(
                self.struct, ZXNQTM, UXFEFJ, XNKMLO, QTMFZD, None, TYEKCW, QBMJVH
            ),
            TMFZDG: GeckoBoolStructAccessor(
                self.struct, TMFZDG, UXFEFJ, MFZDGK, QBMJVH
            ),
            FZDGKE: GeckoBoolStructAccessor(
                self.struct, FZDGKE, UXFEFJ, ZDGKEA, QBMJVH
            ),
            DGKEAK: GeckoBoolStructAccessor(
                self.struct, DGKEAK, GKEAKS, FJTACC, QBMJVH
            ),
            KEAKST: GeckoBoolStructAccessor(
                self.struct, KEAKST, GKEAKS, MNZMJI, QBMJVH
            ),
            EAKSTS: GeckoEnumStructAccessor(
                self.struct, EAKSTS, GKEAKS, TYEKCW, STSEMC, None, TYEKCW, QBMJVH
            ),
            TSEMCG: GeckoEnumStructAccessor(
                self.struct, TSEMCG, GKEAKS, RYXBQF, STSEMC, None, TYEKCW, QBMJVH
            ),
            SEMCGE: GeckoEnumStructAccessor(
                self.struct, SEMCGE, GKEAKS, UNXNKM, XQVXOI, None, QVXOIH, QBMJVH
            ),
            VXOIHB: GeckoEnumStructAccessor(
                self.struct, VXOIHB, GKEAKS, ZDGKEA, IHBXIB, None, TYEKCW, QBMJVH
            ),
            DDPMXF: GeckoBoolStructAccessor(
                self.struct, DDPMXF, DPMXFU, MNZMJI, QBMJVH
            ),
            PMXFUB: GeckoEnumStructAccessor(
                self.struct, PMXFUB, DPMXFU, TYEKCW, FUBJLO, None, UNXNKM, QBMJVH
            ),
            UBJLOI: GeckoBoolStructAccessor(
                self.struct, UBJLOI, DPMXFU, UNXNKM, QBMJVH
            ),
            BJLOIN: GeckoEnumStructAccessor(
                self.struct, BJLOIN, DPMXFU, MFZDGK, OINELW, None, UNXNKM, QBMJVH
            ),
            INELWU: GeckoByteStructAccessor(self.struct, INELWU, NELWUE, QBMJVH),
            ELWUEU: GeckoBoolStructAccessor(
                self.struct, ELWUEU, UTYEKC, FJTACC, QBMJVH
            ),
            LWUEUH: GeckoByteStructAccessor(self.struct, LWUEUH, WUEUHN, QBMJVH),
            UEUHNN: GeckoEnumStructAccessor(
                self.struct, UEUHNN, EUHNNX, FJTACC, HNNXWE, None, TYEKCW, None
            ),
            NNXWEE: GeckoEnumStructAccessor(
                self.struct, NNXWEE, EUHNNX, MNZMJI, WEEZFE, None, TYEKCW, None
            ),
            EEZFET: GeckoEnumStructAccessor(
                self.struct, EEZFET, EZFETD, FJTACC, HNNXWE, None, TYEKCW, None
            ),
            ZFETDR: GeckoEnumStructAccessor(
                self.struct, ZFETDR, EZFETD, MNZMJI, WEEZFE, None, TYEKCW, None
            ),
            FETDRX: GeckoEnumStructAccessor(
                self.struct, FETDRX, ETDRXA, FJTACC, HNNXWE, None, TYEKCW, None
            ),
            TDRXAI: GeckoEnumStructAccessor(
                self.struct, TDRXAI, ETDRXA, MNZMJI, WEEZFE, None, TYEKCW, None
            ),
            DRXAIV: GeckoEnumStructAccessor(
                self.struct, DRXAIV, RXAIVE, FJTACC, HNNXWE, None, TYEKCW, None
            ),
            XAIVEM: GeckoEnumStructAccessor(
                self.struct, XAIVEM, RXAIVE, MNZMJI, WEEZFE, None, TYEKCW, None
            ),
            AIVEMV: GeckoEnumStructAccessor(
                self.struct, AIVEMV, IVEMVC, FJTACC, CYWONF, None, QVXOIH, None
            ),
            YWONFZ: GeckoBoolStructAccessor(self.struct, YWONFZ, IVEMVC, ZDGKEA, None),
            WONFZC: GeckoBoolStructAccessor(self.struct, WONFZC, EUHNNX, UNXNKM, None),
            ONFZCZ: GeckoBoolStructAccessor(self.struct, ONFZCZ, EUHNNX, XNKMLO, None),
            NFZCZO: GeckoBoolStructAccessor(self.struct, NFZCZO, EUHNNX, MFZDGK, None),
            FZCZOL: GeckoBoolStructAccessor(self.struct, FZCZOL, EUHNNX, ZDGKEA, None),
            ZCZOLS: GeckoBoolStructAccessor(self.struct, ZCZOLS, EZFETD, UNXNKM, None),
            CZOLSI: GeckoBoolStructAccessor(self.struct, CZOLSI, EZFETD, XNKMLO, None),
            ZOLSIP: GeckoBoolStructAccessor(self.struct, ZOLSIP, EZFETD, MFZDGK, None),
            OLSIPM: GeckoBoolStructAccessor(self.struct, OLSIPM, EZFETD, ZDGKEA, None),
            LSIPMD: GeckoBoolStructAccessor(self.struct, LSIPMD, ETDRXA, UNXNKM, None),
            SIPMDM: GeckoBoolStructAccessor(self.struct, SIPMDM, ETDRXA, XNKMLO, None),
            IPMDMP: GeckoBoolStructAccessor(self.struct, IPMDMP, ETDRXA, MFZDGK, None),
            PMDMPS: GeckoBoolStructAccessor(self.struct, PMDMPS, ETDRXA, ZDGKEA, None),
            MDMPSC: GeckoBoolStructAccessor(self.struct, MDMPSC, RXAIVE, UNXNKM, None),
            DMPSCT: GeckoBoolStructAccessor(self.struct, DMPSCT, RXAIVE, XNKMLO, None),
            MPSCTT: GeckoBoolStructAccessor(self.struct, MPSCTT, RXAIVE, MFZDGK, None),
            PSCTTG: GeckoBoolStructAccessor(self.struct, PSCTTG, RXAIVE, ZDGKEA, None),
        }

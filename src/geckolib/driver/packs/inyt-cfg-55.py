#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v55'
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
ACCPQI = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
ACQFFT = 96
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AIIDNI = 91
AJVDQL = 88
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
AOAWBS = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
AONPYY = 56
AWBSIR = 3
BDJQRJ = 108
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
BIAMJM = "".join(chr(c) for c in [105, 110, 70, 108, 111])
BJEUTO = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
BLKXSJ = 59
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 70
BQNRXC = 7
BQSNQL = "".join(chr(c) for c in [70, 49])
BSIRYX = 35
BSKSOK = 18
BSSUHB = 101
BVWVUB = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
BWJYKL = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
BXTIAC = 94
BYGDSB = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
CBFEGZ = 45
CCPQIP = 27
CHWDAF = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
CPQIPO = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
CRTFMN = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 54])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 55
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
DAFIKJ = 113
DJQRJJ = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
DNIBXT = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
DNQGVU = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
DQLAII = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
DSBDJQ = 107
DUBSSU = 100
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EJNIBX = 53
EKCWAO = 118
EKVKZI = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
ELHBQN = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EUTOPH = "".join(
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
EXLSXU = 49
FCRTFM = 116
FEFJTA = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
FEGZUQ = 46
FFTTID = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
FJBIAM = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
FJTACC = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FMNHTB = 10
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [67])
FTTIDU = 98
FWRKIN = "".join(chr(c) for c in [85, 76])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
GDSBDJ = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
GLRAHE = 38
GQPLSP = 63
GTYIYW = 76
GVUNXN = "".join(chr(c) for c in [50, 52, 104])
GYOUSP = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
GZUQEX = 47
HBQNRX = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 55])
HBVWVU = 103
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HTBJEU = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
HUGTYI = "".join(
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
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 49, 49])
HWDAFI = 112
HXEKVK = "".join(chr(c) for c in [76, 105, 110, 101, 51])
IACQFF = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
IAMJMA = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
IBXTIA = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
IBXYBQ = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
ICXQIE = 16
IDNIBX = 92
IDUBSS = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = 31
IGYOUS = 28
IIDNIB = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
IJUGSE = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
IKFWRK = "".join(chr(c) for c in [85, 76, 95, 67, 69])
ILXWAJ = 86
INEJNI = 52
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
IRYXBQ = 66
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
IUXFEF = 2
IVDNQG = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = 115
JEUTOP = 82
JHIUSO = 24
JIGYOU = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
JJJVYF = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
JJVYFC = 4
JMAOAW = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
JMCBFE = 44
JNIBXY = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
JQRJJJ = 109
JRJHIU = 23
JTACCP = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
JUGSEL = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
JUIKFW = "".join(
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
JUTYEK = 80
JVDQLA = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
JWMNZM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
JYKLGQ = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
JYMOUN = "".join(chr(c) for c in [76, 111])
KCWAON = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
KFWRKI = 51
KINEJN = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
KJPUNR = 55
KMLOIJ = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 49, 48])
KQXPIC = 14
KSOKPH = 19
KVKZIL = 84
KWIVDN = "".join(chr(c) for c in [83, 108, 97, 118, 101])
KXSJWM = 60
KZILXW = 85
LAIIDN = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
LHBQNR = 6
LIUXFE = 0
LJUIKF = 77
LKXSJW = "".join(
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
LNMHXE = "".join(chr(c) for c in [70, 50, 51])
LOIJUG = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
LSXUJU = 79
LXWAJV = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
MAOAWB = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
MHXEKV = "".join(chr(c) for c in [76, 105, 110, 101, 50])
MJVHFT = 12
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
MNZMJI = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
NBLKXS = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
NEJNIB = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
NHTBJE = 71
NIBXTI = 93
NIBXYB = 74
NKMLOI = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
NMHXEK = "".join(chr(c) for c in [76, 105, 110, 101, 49])
NPYYLI = 81
NQGVUN = 34
NQLNMH = "".join(chr(c) for c in [70, 50, 49])
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
NRXCHW = 110
NXNKML = 64
NZMJIG = 78
OCTHBS = 50
OIJUGS = 4
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 50])
OKPHUO = 20
ONPYYL = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
OOQNRS = 41
OPHUGT = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
OUNBLK = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
OUYNQJ = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
PFTSIF = "".join(chr(c) for c in [70])
PHUGTY = 1
PHUOJR = 21
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 1
POUYNQ = 57
PQIPOU = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
PYYLIU = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QFFTTI = 97
QFYLJU = "".join(chr(c) for c in [78, 105, 103, 104, 116])
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QGVUNX = "".join(chr(c) for c in [65, 109, 80, 109])
QJYMOU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
QLAIID = 90
QLNMHX = "".join(chr(c) for c in [70, 50, 50])
QNRSJM = 42
QNRXCH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
QPLSPF = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
QRJJJV = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
QSNQLN = "".join(chr(c) for c in [70, 50])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RJJJVY = 3
RSJMCB = 43
RTFMNH = 8
RXCHWD = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
RYXBQF = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SAKQXP = 13
SBDJQR = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
SELHBQ = 5
SIFJBI = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
SIRYXB = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
SJWMNZ = 61
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 56])
SKWIVD = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
SNQLNM = "".join(chr(c) for c in [70, 51])
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 57])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
SPBWJY = 29
SPFTSI = 33
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SSUHBV = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
SUHBVW = 102
SXUJUT = "".join(chr(c) for c in [76, 73])
TFMNHT = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 95
TIDUBS = 99
TOPHUG = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
TTIDUB = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
TYEKCW = 54
TYIYWS = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
UBSSUH = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
UBYGDS = 105
UGSELH = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
UGTYIY = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
UHBVWV = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
UIKFWR = 114
UJUTYE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UNBLKX = 58
UNXNKM = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
UOJRJH = 22
UQEXLS = 48
USOOQN = 25
USPBWJ = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
UTOPHU = 72
UTYEKC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UXFEFJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
UYNQJY = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
VDNQGV = 75
VDQLAI = 89
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
VWVUBY = 104
VYFCRT = 6
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
WAONPY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
WBSIRY = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
WDAFIK = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
WJYKLG = 30
WMNZMJ = 62
WRKINE = "".join(chr(c) for c in [67, 69])
WSKWIV = 73
XBQFYL = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
XCHWDA = 111
XFEFJT = 32
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XNKMLO = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
XPICXQ = 15
XQGLRA = 37
XQIEFX = 26
XSJWMN = "".join(
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
XTIACQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
XWAJVD = 87
XYBQSN = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
YBQSNQ = 83
YEKCWA = "".join(chr(c) for c in [80, 49, 76, 84, 105, 109, 101, 79, 117, 116])
YFCRTF = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
YGDSBD = 106
YIYWSK = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
YKLGQP = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
YLJUIK = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
YMOUNB = "".join(chr(c) for c in [72, 105])
YNQJYM = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
YOUSPB = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
YXBQFY = 68
YYLIUX = "".join(chr(c) for c in [79, 119, 110])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
ZMJIGY = "".join(chr(c) for c in [80, 49])
ZUQEXL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
AFIKJP = [
    BMJVHF,
    SSAKQX,
    AKQXPI,
    QXPICX,
    PICXQI,
    CXQIEF,
    CTHBSK,
    HBSKSO,
    SKSOKP,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RJHIUS,
    IUSOOQ,
    XLSXUJ,
]
ASSAKQ = [
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
]
BXYBQS = [JYKLGQ, IBXYBQ]
FIKJPU = [SXUJUT]
FYLJUI = [JYKLGQ, QFYLJU]
GSELHB = [JUGSEL, UGSELH]
HIUSOO = [
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
IKJPUN = []
IYWSKW = [TYIYWS, YIYWSK]
KLGQPL = [JYKLGQ, YKLGQP]
MJIGYO = [JVHFTH, ZMJIGY, PIPIVL]
MJMAOA = [BIAMJM, IAMJMA, AMJMAO]
MLOIJU = [NKMLOI, KMLOIJ]
MOUNBL = [JYMOUN, YMOUNB]
NQJYMO = [OUYNQJ, UYNQJY, YNQJYM]
OAWBSI = [MAOAWB, AOAWBS]
OUSPBW = [GYOUSP, YOUSPB]
PBWJYK = [PIPIVL, ZMJIGY]
QIEFXQ = [
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
QIPOUY = [CPQIPO, PQIPOU]
RKINEJ = [FWRKIN, WRKINE]
TACCPQ = [FEFJTA, EFJTAC, FJTACC, JTACCP]
TBJEUT = [JVHFTH, CPQIPO, HTBJEU]
TSIFJB = [PFTSIF, FTSIFJ]
VUNXNK = [JVHFTH, QGVUNX, GVUNXN]
WIVDNQ = [VLASSA, SKWIVD, KWIVDN]
WVUBYG = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, NMHXEK, MHXEKV, HXEKVK]
XEKVKZ = [BQSNQL, QSNQLN, SNQLNM, NQLNMH, QLNMHX, LNMHXE, NMHXEK, MHXEKV, HXEKVK]
XUJUTY = [
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
    SXUJUT,
]
YLIUXF = [PYYLIU, YYLIUX]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return KJPUNR

    @property
    def output_keys(self):
        return AFIKJP

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, ASSAKQ, None, None, QBMJVH
            ),
            SSAKQX: GeckoEnumStructAccessor(
                self.struct, SSAKQX, SAKQXP, None, ASSAKQ, None, None, QBMJVH
            ),
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, None, ASSAKQ, None, None, QBMJVH
            ),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, None, ASSAKQ, None, None, QBMJVH
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, ASSAKQ, None, None, QBMJVH
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, QIEFXQ, None, None, QBMJVH
            ),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, THBSKS, None, ASSAKQ, None, None, QBMJVH
            ),
            HBSKSO: GeckoEnumStructAccessor(
                self.struct, HBSKSO, BSKSOK, None, ASSAKQ, None, None, QBMJVH
            ),
            SKSOKP: GeckoEnumStructAccessor(
                self.struct, SKSOKP, KSOKPH, None, ASSAKQ, None, None, QBMJVH
            ),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, OKPHUO, None, ASSAKQ, None, None, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, ASSAKQ, None, None, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, ASSAKQ, None, None, QBMJVH
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, ASSAKQ, None, None, QBMJVH
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, HIUSOO, None, None, QBMJVH
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, None, HIUSOO, None, None, QBMJVH
            ),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoByteStructAccessor(self.struct, SJMCBF, JMCBFE, QBMJVH),
            MCBFEG: GeckoByteStructAccessor(self.struct, MCBFEG, CBFEGZ, QBMJVH),
            BFEGZU: GeckoByteStructAccessor(self.struct, BFEGZU, FEGZUQ, QBMJVH),
            EGZUQE: GeckoByteStructAccessor(self.struct, EGZUQE, GZUQEX, QBMJVH),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QBMJVH),
            QEXLSX: GeckoByteStructAccessor(self.struct, QEXLSX, EXLSXU, QBMJVH),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, XUJUTY, None, None, None
            ),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, None),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, QBMJVH),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, NPYYLI, LIUXFE, YLIUXF, None, IUXFEF, QBMJVH
            ),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, None, TACCPQ, None, None, QBMJVH
            ),
            ACCPQI: GeckoEnumStructAccessor(
                self.struct, ACCPQI, CCPQIP, None, QIPOUY, None, None, QBMJVH
            ),
            IPOUYN: GeckoEnumStructAccessor(
                self.struct, IPOUYN, POUYNQ, None, NQJYMO, None, None, QBMJVH
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, NPYYLI, IUXFEF, MOUNBL, None, IUXFEF, QBMJVH
            ),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, QBMJVH),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, MJIGYO, None, None, QBMJVH
            ),
            JIGYOU: GeckoEnumStructAccessor(
                self.struct, JIGYOU, IGYOUS, None, OUSPBW, None, None, QBMJVH
            ),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, SPBWJY, None, PBWJYK, None, None, QBMJVH
            ),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, KLGQPL, None, None, QBMJVH
            ),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoTempStructAccessor(self.struct, QPLSPF, PLSPFT, QBMJVH),
            LSPFTS: GeckoEnumStructAccessor(
                self.struct, LSPFTS, SPFTSI, None, TSIFJB, None, None, QBMJVH
            ),
            SIFJBI: GeckoEnumStructAccessor(
                self.struct, SIFJBI, IFJBIA, None, PBWJYK, None, None, QBMJVH
            ),
            FJBIAM: GeckoEnumStructAccessor(
                self.struct, FJBIAM, JBIAMJ, None, MJMAOA, None, None, QBMJVH
            ),
            JMAOAW: GeckoEnumStructAccessor(
                self.struct, JMAOAW, NPYYLI, AWBSIR, OAWBSI, None, IUXFEF, QBMJVH
            ),
            WBSIRY: GeckoByteStructAccessor(self.struct, WBSIRY, BSIRYX, QBMJVH),
            SIRYXB: GeckoTempStructAccessor(self.struct, SIRYXB, IRYXBQ, QBMJVH),
            RYXBQF: GeckoTempStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, FYLJUI, None, None, QBMJVH
            ),
            YLJUIK: GeckoByteStructAccessor(self.struct, YLJUIK, LJUIKF, QBMJVH),
            JUIKFW: GeckoByteStructAccessor(self.struct, JUIKFW, UIKFWR, QBMJVH),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, None, RKINEJ, None, None, QBMJVH
            ),
            KINEJN: GeckoByteStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoByteStructAccessor(self.struct, NEJNIB, EJNIBX, QBMJVH),
            JNIBXY: GeckoEnumStructAccessor(
                self.struct, JNIBXY, NIBXYB, None, BXYBQS, None, None, QBMJVH
            ),
            XYBQSN: GeckoEnumStructAccessor(
                self.struct, XYBQSN, YBQSNQ, None, XEKVKZ, None, None, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, XEKVKZ, None, None, QBMJVH
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, KZILXW, None, XEKVKZ, None, None, QBMJVH
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, ILXWAJ, None, XEKVKZ, None, None, QBMJVH
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XWAJVD, None, XEKVKZ, None, None, QBMJVH
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, AJVDQL, None, XEKVKZ, None, None, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, VDQLAI, None, XEKVKZ, None, None, QBMJVH
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, QLAIID, None, XEKVKZ, None, None, QBMJVH
            ),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AIIDNI, None, XEKVKZ, None, None, QBMJVH
            ),
            IIDNIB: GeckoEnumStructAccessor(
                self.struct, IIDNIB, IDNIBX, None, XEKVKZ, None, None, QBMJVH
            ),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, NIBXTI, None, XEKVKZ, None, None, QBMJVH
            ),
            IBXTIA: GeckoEnumStructAccessor(
                self.struct, IBXTIA, BXTIAC, None, XEKVKZ, None, None, QBMJVH
            ),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, TIACQF, None, XEKVKZ, None, None, QBMJVH
            ),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, ACQFFT, None, XEKVKZ, None, None, QBMJVH
            ),
            CQFFTT: GeckoEnumStructAccessor(
                self.struct, CQFFTT, QFFTTI, None, XEKVKZ, None, None, QBMJVH
            ),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, QBMJVH),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, QBMJVH),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, QBMJVH),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, QBMJVH),
            BVWVUB: GeckoEnumStructAccessor(
                self.struct, BVWVUB, VWVUBY, None, WVUBYG, None, None, QBMJVH
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, WVUBYG, None, None, QBMJVH
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, YGDSBD, None, WVUBYG, None, None, QBMJVH
            ),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, None, WVUBYG, None, None, QBMJVH
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, None, WVUBYG, None, None, QBMJVH
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, None, WVUBYG, None, None, QBMJVH
            ),
            QRJJJV: GeckoByteStructAccessor(self.struct, QRJJJV, RJJJVY, QBMJVH),
            JJJVYF: GeckoTimeStructAccessor(self.struct, JJJVYF, JJVYFC, QBMJVH),
            JVYFCR: GeckoTimeStructAccessor(self.struct, JVYFCR, VYFCRT, QBMJVH),
            YFCRTF: GeckoTimeStructAccessor(self.struct, YFCRTF, FCRTFM, QBMJVH),
            CRTFMN: GeckoTimeStructAccessor(self.struct, CRTFMN, RTFMNH, QBMJVH),
            TFMNHT: GeckoTimeStructAccessor(self.struct, TFMNHT, FMNHTB, QBMJVH),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, NHTBJE, None, TBJEUT, None, None, QBMJVH
            ),
            BJEUTO: GeckoBoolStructAccessor(
                self.struct, BJEUTO, JEUTOP, LIUXFE, QBMJVH
            ),
            EUTOPH: GeckoBoolStructAccessor(
                self.struct, EUTOPH, UTOPHU, IUXFEF, QBMJVH
            ),
            TOPHUG: GeckoBoolStructAccessor(
                self.struct, TOPHUG, UTOPHU, LIUXFE, QBMJVH
            ),
            OPHUGT: GeckoBoolStructAccessor(
                self.struct, OPHUGT, UTOPHU, PHUGTY, QBMJVH
            ),
            HUGTYI: GeckoBoolStructAccessor(
                self.struct, HUGTYI, UTOPHU, AWBSIR, QBMJVH
            ),
            UGTYIY: GeckoEnumStructAccessor(
                self.struct, UGTYIY, GTYIYW, None, IYWSKW, None, None, QBMJVH
            ),
            YWSKWI: GeckoEnumStructAccessor(
                self.struct, YWSKWI, WSKWIV, None, WIVDNQ, None, None, QBMJVH
            ),
            IVDNQG: GeckoByteStructAccessor(self.struct, IVDNQG, VDNQGV, QBMJVH),
            DNQGVU: GeckoEnumStructAccessor(
                self.struct, DNQGVU, NQGVUN, None, VUNXNK, None, None, QBMJVH
            ),
            UNXNKM: GeckoWordStructAccessor(self.struct, UNXNKM, NXNKML, QBMJVH),
            XNKMLO: GeckoEnumStructAccessor(
                self.struct, XNKMLO, NPYYLI, PHUGTY, MLOIJU, None, IUXFEF, QBMJVH
            ),
            LOIJUG: GeckoBoolStructAccessor(
                self.struct, LOIJUG, NPYYLI, OIJUGS, QBMJVH
            ),
            IJUGSE: GeckoEnumStructAccessor(
                self.struct, IJUGSE, NPYYLI, SELHBQ, GSELHB, None, IUXFEF, QBMJVH
            ),
            ELHBQN: GeckoBoolStructAccessor(
                self.struct, ELHBQN, NPYYLI, LHBQNR, QBMJVH
            ),
            HBQNRX: GeckoBoolStructAccessor(
                self.struct, HBQNRX, NPYYLI, BQNRXC, QBMJVH
            ),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, QBMJVH),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, QBMJVH),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, QBMJVH),
            WDAFIK: GeckoByteStructAccessor(self.struct, WDAFIK, DAFIKJ, QBMJVH),
        }

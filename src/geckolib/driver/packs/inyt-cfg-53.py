#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v53'
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
ACCPQI = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
ACQFFT = 104
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AIIDNI = 99
AJVDQL = 96
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = 70
AOAWBS = 77
AONPYY = 81
AWBSIR = 51
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
BIAMJM = 68
BLKXSJ = "".join(
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
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
BQSNQL = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
BSIRYX = "".join(chr(c) for c in [67, 69])
BSKSOK = 18
BSSUHB = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
BVWVUB = 4
BWJYKL = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
BXTIAC = 102
BXYBQS = 85
BYGDSB = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
CBFEGZ = 45
CPQIPO = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
CQBMJV = 0
CRTFMN = 76
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 54])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 56
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
DJQRJJ = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
DNIBXT = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
DNQGVU = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
DQLAII = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
DSBDJQ = 71
DUBSSU = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EKCWAO = 55
EKVKZI = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EUTOPH = 75
EXLSXU = 49
FCRTFM = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
FEFJTA = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FEGZUQ = 46
FFTTID = 105
FJBIAM = 66
FJTACC = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 31
FTTIDU = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
FWRKIN = "".join(chr(c) for c in [70, 50, 49])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
GDSBDJ = "".join(
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
GLRAHE = 38
GQPLSP = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
GSELHB = 53
GTYIYW = 64
GYOUSP = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
GZUQEX = 47
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 55])
HBVWVU = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HTBJEU = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 49, 49])
HXEKVK = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
IACQFF = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
IAMJMA = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
IBXTIA = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
IBXYBQ = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
ICXQIE = 16
IDNIBX = 100
IDUBSS = 107
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IIDNIB = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
IKFWRK = "".join(chr(c) for c in [70, 50])
ILXWAJ = 94
INEJNI = "".join(chr(c) for c in [76, 105, 110, 101, 50])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
IRYXBQ = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
IUXFEF = 32
IVDNQG = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
JBIAMJ = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
JEUTOP = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
JHIUSO = 24
JIGYOU = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
JJJVYF = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
JJVYFC = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
JMCBFE = 44
JNIBXY = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
JQRJJJ = 82
JRJHIU = 23
JTACCP = 27
JUIKFW = 83
JUTYEK = 80
JVDQLA = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = 1
JWMNZM = 78
JYKLGQ = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
JYMOUN = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
KCWAON = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
KFWRKI = "".join(chr(c) for c in [70, 51])
KINEJN = "".join(chr(c) for c in [76, 105, 110, 101, 49])
KLGQPL = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
KMLOIJ = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 49, 48])
KQXPIC = 14
KSOKPH = 19
KVKZIL = 92
KWIVDN = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
KXSJWM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
KZILXW = 93
LAIIDN = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = 1
LIUXFE = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
LJUIKF = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
LKXSJW = 61
LNMHXE = 89
LOIJUG = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [67])
LSXUJU = 79
LXWAJV = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
MAOAWB = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
MHXEKV = 90
MJIGYO = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
MJMAOA = "".join(chr(c) for c in [78, 105, 103, 104, 116])
MJVHFT = 12
MLOIJU = 112
MNHTBJ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
MOUNBL = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
NBLKXS = 60
NEJNIB = "".join(chr(c) for c in [76, 105, 110, 101, 51])
NHTBJE = 73
NIBXTI = 101
NIBXYB = 84
NKMLOI = 111
NMHXEK = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
NPYYLI = "".join(chr(c) for c in [79, 119, 110])
NQGVUN = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
NQJYMO = "".join(chr(c) for c in [72, 105])
NQLNMH = 88
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
NXNKML = 110
NZMJIG = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
OAWBSI = "".join(chr(c) for c in [85, 76, 95, 67, 69])
OCTHBS = 50
OIJUGS = 113
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 50])
OKPHUO = 20
ONPYYL = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OOQNRS = 41
OPHUGT = "".join(chr(c) for c in [65, 109, 80, 109])
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
OUNBLK = 59
PBWJYK = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
PFTSIF = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
PHUGTY = "".join(chr(c) for c in [50, 52, 104])
PHUOJR = 21
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [70])
POUYNQ = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
PQIPOU = 57
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QFFTTI = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
QFYLJU = 74
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QGVUNX = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
QIPOUY = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
QLAIID = 98
QLNMHX = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
QNRSJM = 42
QPLSPF = 33
QRJJJV = "".join(
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
QSNQLN = 87
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RJJJVY = 72
RKINEJ = "".join(chr(c) for c in [70, 50, 51])
RSJMCB = 43
RTFMNH = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
RYXBQF = 52
SAKQXP = 13
SBDJQR = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
SIFJBI = 35
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
SJWMNZ = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 56])
SKWIVD = "".join(chr(c) for c in [105, 110, 70, 108, 111])
SNQLNM = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 57])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
SPBWJY = 30
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SSUHBV = 109
SUHBVW = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
SXUJUT = "".join(chr(c) for c in [76, 73])
TACCPQ = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
TBJEUT = "".join(chr(c) for c in [83, 108, 97, 118, 101])
TFMNHT = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 103
TIDUBS = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
TOPHUG = 34
TSIFJB = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
TTIDUB = 106
TYEKCW = 54
TYIYWS = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
UBSSUH = 108
UBYGDS = 8
UGTYIY = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
UHBVWV = 3
UIKFWR = "".join(chr(c) for c in [70, 49])
UJUTYE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UNBLKX = "".join(
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
UNXNKM = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
UOJRJH = 22
UQEXLS = 48
USOOQN = 25
USPBWJ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
UTOPHU = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
UTYEKC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UXFEFJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
UYNQJY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
VDNQGV = 4
VDQLAI = 97
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
VUNXNK = 5
VWVUBY = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
VYFCRT = "".join(
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
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
WAONPY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
WBSIRY = "".join(chr(c) for c in [85, 76])
WMNZMJ = "".join(chr(c) for c in [80, 49])
WRKINE = "".join(chr(c) for c in [70, 50, 50])
WSKWIV = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
WVUBYG = 6
XBQFYL = 53
XEKVKZ = 91
XFEFJT = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XNKMLO = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
XPICXQ = 15
XQGLRA = 37
XQIEFX = 26
XSJWMN = 62
XTIACQ = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
XWAJVD = 95
XYBQSN = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
YBQSNQ = 86
YEKCWA = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
YFCRTF = 3
YGDSBD = 10
YIYWSK = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
YKLGQP = 63
YLIUXF = 2
YMOUNB = 58
YNQJYM = "".join(chr(c) for c in [76, 111])
YOUSPB = 29
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
YYLIUX = 0
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
ZMJIGY = 28
ZUQEXL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
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
BDJQRJ = [JVHFTH, SBDJQR]
BJEUTO = [VLASSA, HTBJEU, TBJEUT]
CCPQIP = [TACCPQ, ACCPQI]
CQFFTT = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, KINEJN, INEJNI, NEJNIB]
EFJTAC = [UXFEFJ, XFEFJT, FEFJTA]
EJNIBX = [UIKFWR, IKFWRK, KFWRKI, FWRKIN, WRKINE, RKINEJ, KINEJN, INEJNI, NEJNIB]
FMNHTB = [RTFMNH, TFMNHT]
GVUNXN = [NQGVUN, QGVUNX]
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
HUGTYI = [JVHFTH, OPHUGT, PHUGTY]
IGYOUS = [MJIGYO, JIGYOU]
IJUGSE = [
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
JMAOAW = [PBWJYK, MJMAOA]
JUGSEL = [SXUJUT]
MNZMJI = [JVHFTH, WMNZMJ, PIPIVL]
OUSPBW = [PIPIVL, WMNZMJ]
OUYNQJ = [QIPOUY, IPOUYN, POUYNQ]
PYYLIU = [ONPYYL, NPYYLI]
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
QJYMOU = [YNQJYM, NQJYMO]
SIRYXB = [WBSIRY, BSIRYX]
SPFTSI = [PLSPFT, LSPFTS]
UGSELH = []
WIVDNQ = [SKWIVD, KWIVDN]
WJYKLG = [PBWJYK, BWJYKL]
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
YLJUIK = [PBWJYK, FYLJUI]
YWSKWI = [YIYWSK, IYWSKW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return GSELHB

    @property
    def output_keys(self):
        return IJUGSE

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
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, YYLIUX, PYYLIU, None, YLIUXF, QBMJVH
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, EFJTAC, None, None, QBMJVH
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, CCPQIP, None, None, QBMJVH
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, PQIPOU, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, AONPYY, YLIUXF, QJYMOU, None, YLIUXF, QBMJVH
            ),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoByteStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoByteStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, MNZMJI, None, None, QBMJVH
            ),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, ZMJIGY, None, IGYOUS, None, None, QBMJVH
            ),
            GYOUSP: GeckoEnumStructAccessor(
                self.struct, GYOUSP, YOUSPB, None, OUSPBW, None, None, QBMJVH
            ),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, SPBWJY, None, WJYKLG, None, None, QBMJVH
            ),
            JYKLGQ: GeckoByteStructAccessor(self.struct, JYKLGQ, YKLGQP, QBMJVH),
            KLGQPL: GeckoTempStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, QPLSPF, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, OUSPBW, None, None, QBMJVH
            ),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoTempStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoTempStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, AMJMAO, None, JMAOAW, None, None, QBMJVH
            ),
            MAOAWB: GeckoByteStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, SIRYXB, None, None, QBMJVH
            ),
            IRYXBQ: GeckoByteStructAccessor(self.struct, IRYXBQ, RYXBQF, QBMJVH),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, YLJUIK, None, None, QBMJVH
            ),
            LJUIKF: GeckoEnumStructAccessor(
                self.struct, LJUIKF, JUIKFW, None, EJNIBX, None, None, QBMJVH
            ),
            JNIBXY: GeckoEnumStructAccessor(
                self.struct, JNIBXY, NIBXYB, None, EJNIBX, None, None, QBMJVH
            ),
            IBXYBQ: GeckoEnumStructAccessor(
                self.struct, IBXYBQ, BXYBQS, None, EJNIBX, None, None, QBMJVH
            ),
            XYBQSN: GeckoEnumStructAccessor(
                self.struct, XYBQSN, YBQSNQ, None, EJNIBX, None, None, QBMJVH
            ),
            BQSNQL: GeckoEnumStructAccessor(
                self.struct, BQSNQL, QSNQLN, None, EJNIBX, None, None, QBMJVH
            ),
            SNQLNM: GeckoEnumStructAccessor(
                self.struct, SNQLNM, NQLNMH, None, EJNIBX, None, None, QBMJVH
            ),
            QLNMHX: GeckoEnumStructAccessor(
                self.struct, QLNMHX, LNMHXE, None, EJNIBX, None, None, QBMJVH
            ),
            NMHXEK: GeckoEnumStructAccessor(
                self.struct, NMHXEK, MHXEKV, None, EJNIBX, None, None, QBMJVH
            ),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, XEKVKZ, None, EJNIBX, None, None, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, EJNIBX, None, None, QBMJVH
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, KZILXW, None, EJNIBX, None, None, QBMJVH
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, ILXWAJ, None, EJNIBX, None, None, QBMJVH
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XWAJVD, None, EJNIBX, None, None, QBMJVH
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, AJVDQL, None, EJNIBX, None, None, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, VDQLAI, None, EJNIBX, None, None, QBMJVH
            ),
            DQLAII: GeckoByteStructAccessor(self.struct, DQLAII, QLAIID, QBMJVH),
            LAIIDN: GeckoByteStructAccessor(self.struct, LAIIDN, AIIDNI, QBMJVH),
            IIDNIB: GeckoByteStructAccessor(self.struct, IIDNIB, IDNIBX, QBMJVH),
            DNIBXT: GeckoByteStructAccessor(self.struct, DNIBXT, NIBXTI, QBMJVH),
            IBXTIA: GeckoByteStructAccessor(self.struct, IBXTIA, BXTIAC, QBMJVH),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, QBMJVH),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, ACQFFT, None, CQFFTT, None, None, QBMJVH
            ),
            QFFTTI: GeckoEnumStructAccessor(
                self.struct, QFFTTI, FFTTID, None, CQFFTT, None, None, QBMJVH
            ),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, TTIDUB, None, CQFFTT, None, None, QBMJVH
            ),
            TIDUBS: GeckoEnumStructAccessor(
                self.struct, TIDUBS, IDUBSS, None, CQFFTT, None, None, QBMJVH
            ),
            DUBSSU: GeckoEnumStructAccessor(
                self.struct, DUBSSU, UBSSUH, None, CQFFTT, None, None, QBMJVH
            ),
            BSSUHB: GeckoEnumStructAccessor(
                self.struct, BSSUHB, SSUHBV, None, CQFFTT, None, None, QBMJVH
            ),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, QBMJVH),
            HBVWVU: GeckoTimeStructAccessor(self.struct, HBVWVU, BVWVUB, QBMJVH),
            VWVUBY: GeckoTimeStructAccessor(self.struct, VWVUBY, WVUBYG, QBMJVH),
            VUBYGD: GeckoTimeStructAccessor(self.struct, VUBYGD, UBYGDS, QBMJVH),
            BYGDSB: GeckoTimeStructAccessor(self.struct, BYGDSB, YGDSBD, QBMJVH),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, None, BDJQRJ, None, None, QBMJVH
            ),
            DJQRJJ: GeckoBoolStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, YYLIUX, QBMJVH
            ),
            QRJJJV: GeckoBoolStructAccessor(
                self.struct, QRJJJV, RJJJVY, YLIUXF, QBMJVH
            ),
            JJJVYF: GeckoBoolStructAccessor(
                self.struct, JJJVYF, RJJJVY, YYLIUX, QBMJVH
            ),
            JJVYFC: GeckoBoolStructAccessor(
                self.struct, JJVYFC, RJJJVY, JVYFCR, QBMJVH
            ),
            VYFCRT: GeckoBoolStructAccessor(
                self.struct, VYFCRT, RJJJVY, YFCRTF, QBMJVH
            ),
            FCRTFM: GeckoEnumStructAccessor(
                self.struct, FCRTFM, CRTFMN, None, FMNHTB, None, None, QBMJVH
            ),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, NHTBJE, None, BJEUTO, None, None, QBMJVH
            ),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, QBMJVH),
            UTOPHU: GeckoEnumStructAccessor(
                self.struct, UTOPHU, TOPHUG, None, HUGTYI, None, None, QBMJVH
            ),
            UGTYIY: GeckoWordStructAccessor(self.struct, UGTYIY, GTYIYW, QBMJVH),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, AONPYY, JVYFCR, YWSKWI, None, YLIUXF, QBMJVH
            ),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, AONPYY, YFCRTF, WIVDNQ, None, YLIUXF, QBMJVH
            ),
            IVDNQG: GeckoBoolStructAccessor(
                self.struct, IVDNQG, AONPYY, VDNQGV, QBMJVH
            ),
            DNQGVU: GeckoEnumStructAccessor(
                self.struct, DNQGVU, AONPYY, VUNXNK, GVUNXN, None, YLIUXF, QBMJVH
            ),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, QBMJVH),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, QBMJVH),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, QBMJVH),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, QBMJVH),
        }

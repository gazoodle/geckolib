#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v54'
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
ACCPQI = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
ACQFFT = 97
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AIIDNI = 92
AJVDQL = 89
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
AOAWBS = 3
AONPYY = 81
AWBSIR = 35
BDJQRJ = 109
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
BIAMJM = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
BJEUTO = "".join(
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
BLKXSJ = 60
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQNRXC = 110
BQSNQL = "".join(chr(c) for c in [70, 51])
BSIRYX = 66
BSKSOK = 18
BSSUHB = 102
BWJYKL = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
BXTIAC = 95
BXYBQS = 83
BYGDSB = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
CBFEGZ = 45
CCPQIP = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
CHWDAF = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
CRTFMN = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 54])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 56
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
DJQRJJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
DNIBXT = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
DNQGVU = "".join(chr(c) for c in [65, 109, 80, 109])
DQLAII = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
DSBDJQ = 108
DUBSSU = 101
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EJNIBX = 74
EKCWAO = 55
EKVKZI = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
ELHBQN = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EUTOPH = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
EXLSXU = 49
FCRTFM = 8
FEFJTA = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FEGZUQ = 46
FFTTID = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
FIKJPU = 54
FJBIAM = "".join(chr(c) for c in [105, 110, 70, 108, 111])
FMNHTB = 71
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
FTTIDU = 99
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = 77
GDSBDJ = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
GLRAHE = 38
GQPLSP = 1
GSELHB = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
GTYIYW = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
GVUNXN = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
GZUQEX = 47
HBQNRX = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 49]
)
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 55])
HBVWVU = 104
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HTBJEU = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
HUGTYI = 76
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 49, 49])
HWDAFI = 113
HXEKVK = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
IACQFF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
IBXTIA = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
IBXYBQ = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
ICXQIE = 16
IDNIBX = 93
IDUBSS = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = 115
IGYOUS = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
IIDNIB = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
IJUGSE = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
IKFWRK = "".join(chr(c) for c in [85, 76])
ILXWAJ = 87
INEJNI = 53
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
IRYXBQ = 68
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
IUXFEF = 32
IVDNQG = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = 73
JBIAMJ = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
JEUTOP = 72
JHIUSO = 24
JIGYOU = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
JJJVYF = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
JJVYFC = 6
JMAOAW = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
JMCBFE = 44
JNIBXY = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
JQRJJJ = 3
JRJHIU = 23
JTACCP = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
JUIKFW = "".join(chr(c) for c in [85, 76, 95, 67, 69])
JUTYEK = 80
JVDQLA = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
JWMNZM = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
KCWAON = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
KFWRKI = "".join(chr(c) for c in [67, 69])
KINEJN = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
KLGQPL = 63
KMLOIJ = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 49, 48])
KQXPIC = 14
KSOKPH = 19
KVKZIL = 85
KWIVDN = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
KXSJWM = 61
KZILXW = 86
LAIIDN = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
LHBQNR = 7
LIUXFE = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
LJUIKF = 114
LKXSJW = "".join(
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
LNMHXE = "".join(chr(c) for c in [76, 105, 110, 101, 50])
LOIJUG = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [70])
LSXUJU = 79
LXWAJV = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
MJIGYO = 28
MJMAOA = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
MJVHFT = 12
MLOIJU = 4
MNHTBJ = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
MNZMJI = "".join(chr(c) for c in [80, 49])
MOUNBL = 58
NBLKXS = "".join(
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
NEJNIB = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
NIBXTI = 94
NMHXEK = "".join(chr(c) for c in [76, 105, 110, 101, 51])
NPYYLI = "".join(chr(c) for c in [79, 119, 110])
NQGVUN = "".join(chr(c) for c in [50, 52, 104])
NQJYMO = "".join(chr(c) for c in [76, 111])
NQLNMH = "".join(chr(c) for c in [70, 50, 51])
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
NRXCHW = 111
NXNKML = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
OAWBSI = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
OCTHBS = 50
OIJUGS = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 50])
OKPHUO = 20
ONPYYL = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OOQNRS = 41
OPHUGT = "".join(
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
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
OUNBLK = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
OUSPBW = 29
OUYNQJ = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
PBWJYK = 30
PHUGTY = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
PHUOJR = 21
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 33
POUYNQ = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
PQIPOU = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QFFTTI = 98
QFYLJU = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = 57
QJYMOU = "".join(chr(c) for c in [72, 105])
QLAIID = 91
QLNMHX = "".join(chr(c) for c in [76, 105, 110, 101, 49])
QNRSJM = 42
QNRXCH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
QPLSPF = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
QRJJJV = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
QSNQLN = "".join(chr(c) for c in [70, 50, 49])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RJJJVY = 4
RKINEJ = 52
RSJMCB = 43
RTFMNH = 10
RXCHWD = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
RYXBQF = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
SAKQXP = 13
SBDJQR = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
SELHBQ = 6
SIFJBI = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
SIRYXB = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
SJWMNZ = 62
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 56])
SNQLNM = "".join(chr(c) for c in [70, 50, 50])
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 57])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
SPBWJY = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
SPFTSI = "".join(chr(c) for c in [67])
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SSUHBV = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
SUHBVW = 103
SXUJUT = "".join(chr(c) for c in [76, 73])
TACCPQ = 27
TBJEUT = 82
TFMNHT = "".join(
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
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 96
TIDUBS = 100
TOPHUG = 1
TSIFJB = 31
TTIDUB = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
TYEKCW = 54
UBSSUH = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
UBYGDS = 106
UGSELH = 5
UGTYIY = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
UHBVWV = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
UIKFWR = 51
UJUTYE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UNBLKX = 59
UNXNKM = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
UOJRJH = 22
UQEXLS = 48
USOOQN = 25
UTOPHU = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
UTYEKC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UXFEFJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
VDNQGV = 34
VDQLAI = 90
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
VUNXNK = 64
VWVUBY = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
VYFCRT = 116
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
WAONPY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
WBSIRY = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
WIVDNQ = 75
WJYKLG = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
WMNZMJ = 78
WRKINE = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
WSKWIV = "".join(chr(c) for c in [83, 108, 97, 118, 101])
WVUBYG = 105
XBQFYL = "".join(chr(c) for c in [78, 105, 103, 104, 116])
XCHWDA = 112
XEKVKZ = 84
XFEFJT = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XNKMLO = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
XPICXQ = 15
XQGLRA = 37
XQIEFX = 26
XSJWMN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
XTIACQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
XWAJVD = 88
XYBQSN = "".join(chr(c) for c in [70, 49])
YBQSNQ = "".join(chr(c) for c in [70, 50])
YEKCWA = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
YFCRTF = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
YGDSBD = 107
YIYWSK = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
YKLGQP = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
YLIUXF = 2
YLJUIK = "".join(
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
YMOUNB = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
YNQJYM = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
YOUSPB = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
YXBQFY = 70
YYLIUX = 0
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
ZMJIGY = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
ZUQEXL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
AFIKJP = []
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
BQFYLJ = [BWJYKL, XBQFYL]
BVWVUB = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, QLNMHX, LNMHXE, NMHXEK]
CPQIPO = [ACCPQI, CCPQIP]
DAFIKJ = [SXUJUT]
FJTACC = [UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
FWRKIN = [IKFWRK, KFWRKI]
GYOUSP = [JIGYOU, IGYOUS]
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
IAMJMA = [FJBIAM, JBIAMJ, BIAMJM]
JUGSEL = [OIJUGS, IJUGSE]
JYKLGQ = [BWJYKL, WJYKLG]
JYMOUN = [NQJYMO, QJYMOU]
MAOAWB = [MJMAOA, JMAOAW]
MHXEKV = [XYBQSN, YBQSNQ, BQSNQL, QSNQLN, SNQLNM, NQLNMH, QLNMHX, LNMHXE, NMHXEK]
NHTBJE = [JVHFTH, ACCPQI, MNHTBJ]
NIBXYB = [BWJYKL, JNIBXY]
NKMLOI = [NXNKML, XNKMLO]
NZMJIG = [JVHFTH, MNZMJI, PIPIVL]
PFTSIF = [LSPFTS, SPFTSI]
PYYLIU = [ONPYYL, NPYYLI]
QGVUNX = [JVHFTH, DNQGVU, NQGVUN]
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
SKWIVD = [VLASSA, YWSKWI, WSKWIV]
TYIYWS = [UGTYIY, GTYIYW]
USPBWJ = [PIPIVL, MNZMJI]
UYNQJY = [IPOUYN, POUYNQ, OUYNQJ]
WDAFIK = [
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


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return FIKJPU

    @property
    def output_keys(self):
        return WDAFIK

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
                self.struct, LIUXFE, IUXFEF, None, FJTACC, None, None, QBMJVH
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, UYNQJY, None, None, QBMJVH
            ),
            YNQJYM: GeckoEnumStructAccessor(
                self.struct, YNQJYM, AONPYY, YLIUXF, JYMOUN, None, YLIUXF, QBMJVH
            ),
            YMOUNB: GeckoByteStructAccessor(self.struct, YMOUNB, MOUNBL, QBMJVH),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, QBMJVH),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoEnumStructAccessor(
                self.struct, JWMNZM, WMNZMJ, None, NZMJIG, None, None, QBMJVH
            ),
            ZMJIGY: GeckoEnumStructAccessor(
                self.struct, ZMJIGY, MJIGYO, None, GYOUSP, None, None, QBMJVH
            ),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, JYKLGQ, None, None, QBMJVH
            ),
            YKLGQP: GeckoByteStructAccessor(self.struct, YKLGQP, KLGQPL, QBMJVH),
            LGQPLS: GeckoTempStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoEnumStructAccessor(
                self.struct, QPLSPF, PLSPFT, None, PFTSIF, None, None, QBMJVH
            ),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, TSIFJB, None, USPBWJ, None, None, QBMJVH
            ),
            SIFJBI: GeckoEnumStructAccessor(
                self.struct, SIFJBI, IFJBIA, None, IAMJMA, None, None, QBMJVH
            ),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, AONPYY, AOAWBS, MAOAWB, None, YLIUXF, QBMJVH
            ),
            OAWBSI: GeckoByteStructAccessor(self.struct, OAWBSI, AWBSIR, QBMJVH),
            WBSIRY: GeckoTempStructAccessor(self.struct, WBSIRY, BSIRYX, QBMJVH),
            SIRYXB: GeckoTempStructAccessor(self.struct, SIRYXB, IRYXBQ, QBMJVH),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, YXBQFY, None, BQFYLJ, None, None, QBMJVH
            ),
            QFYLJU: GeckoByteStructAccessor(self.struct, QFYLJU, FYLJUI, QBMJVH),
            YLJUIK: GeckoByteStructAccessor(self.struct, YLJUIK, LJUIKF, QBMJVH),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, UIKFWR, None, FWRKIN, None, None, QBMJVH
            ),
            WRKINE: GeckoByteStructAccessor(self.struct, WRKINE, RKINEJ, QBMJVH),
            KINEJN: GeckoByteStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, EJNIBX, None, NIBXYB, None, None, QBMJVH
            ),
            IBXYBQ: GeckoEnumStructAccessor(
                self.struct, IBXYBQ, BXYBQS, None, MHXEKV, None, None, QBMJVH
            ),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, XEKVKZ, None, MHXEKV, None, None, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, MHXEKV, None, None, QBMJVH
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, KZILXW, None, MHXEKV, None, None, QBMJVH
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, ILXWAJ, None, MHXEKV, None, None, QBMJVH
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XWAJVD, None, MHXEKV, None, None, QBMJVH
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, AJVDQL, None, MHXEKV, None, None, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, VDQLAI, None, MHXEKV, None, None, QBMJVH
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, QLAIID, None, MHXEKV, None, None, QBMJVH
            ),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AIIDNI, None, MHXEKV, None, None, QBMJVH
            ),
            IIDNIB: GeckoEnumStructAccessor(
                self.struct, IIDNIB, IDNIBX, None, MHXEKV, None, None, QBMJVH
            ),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, NIBXTI, None, MHXEKV, None, None, QBMJVH
            ),
            IBXTIA: GeckoEnumStructAccessor(
                self.struct, IBXTIA, BXTIAC, None, MHXEKV, None, None, QBMJVH
            ),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, TIACQF, None, MHXEKV, None, None, QBMJVH
            ),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, ACQFFT, None, MHXEKV, None, None, QBMJVH
            ),
            CQFFTT: GeckoByteStructAccessor(self.struct, CQFFTT, QFFTTI, QBMJVH),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, QBMJVH),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, QBMJVH),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, QBMJVH),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoEnumStructAccessor(
                self.struct, UHBVWV, HBVWVU, None, BVWVUB, None, None, QBMJVH
            ),
            VWVUBY: GeckoEnumStructAccessor(
                self.struct, VWVUBY, WVUBYG, None, BVWVUB, None, None, QBMJVH
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, BVWVUB, None, None, QBMJVH
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, YGDSBD, None, BVWVUB, None, None, QBMJVH
            ),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, None, BVWVUB, None, None, QBMJVH
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, None, BVWVUB, None, None, QBMJVH
            ),
            DJQRJJ: GeckoByteStructAccessor(self.struct, DJQRJJ, JQRJJJ, QBMJVH),
            QRJJJV: GeckoTimeStructAccessor(self.struct, QRJJJV, RJJJVY, QBMJVH),
            JJJVYF: GeckoTimeStructAccessor(self.struct, JJJVYF, JJVYFC, QBMJVH),
            JVYFCR: GeckoTimeStructAccessor(self.struct, JVYFCR, VYFCRT, QBMJVH),
            YFCRTF: GeckoTimeStructAccessor(self.struct, YFCRTF, FCRTFM, QBMJVH),
            CRTFMN: GeckoTimeStructAccessor(self.struct, CRTFMN, RTFMNH, QBMJVH),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, FMNHTB, None, NHTBJE, None, None, QBMJVH
            ),
            HTBJEU: GeckoBoolStructAccessor(
                self.struct, HTBJEU, TBJEUT, YYLIUX, QBMJVH
            ),
            BJEUTO: GeckoBoolStructAccessor(
                self.struct, BJEUTO, JEUTOP, YLIUXF, QBMJVH
            ),
            EUTOPH: GeckoBoolStructAccessor(
                self.struct, EUTOPH, JEUTOP, YYLIUX, QBMJVH
            ),
            UTOPHU: GeckoBoolStructAccessor(
                self.struct, UTOPHU, JEUTOP, TOPHUG, QBMJVH
            ),
            OPHUGT: GeckoBoolStructAccessor(
                self.struct, OPHUGT, JEUTOP, AOAWBS, QBMJVH
            ),
            PHUGTY: GeckoEnumStructAccessor(
                self.struct, PHUGTY, HUGTYI, None, TYIYWS, None, None, QBMJVH
            ),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, SKWIVD, None, None, QBMJVH
            ),
            KWIVDN: GeckoByteStructAccessor(self.struct, KWIVDN, WIVDNQ, QBMJVH),
            IVDNQG: GeckoEnumStructAccessor(
                self.struct, IVDNQG, VDNQGV, None, QGVUNX, None, None, QBMJVH
            ),
            GVUNXN: GeckoWordStructAccessor(self.struct, GVUNXN, VUNXNK, QBMJVH),
            UNXNKM: GeckoEnumStructAccessor(
                self.struct, UNXNKM, AONPYY, TOPHUG, NKMLOI, None, YLIUXF, QBMJVH
            ),
            KMLOIJ: GeckoBoolStructAccessor(
                self.struct, KMLOIJ, AONPYY, MLOIJU, QBMJVH
            ),
            LOIJUG: GeckoEnumStructAccessor(
                self.struct, LOIJUG, AONPYY, UGSELH, JUGSEL, None, YLIUXF, QBMJVH
            ),
            GSELHB: GeckoBoolStructAccessor(
                self.struct, GSELHB, AONPYY, SELHBQ, QBMJVH
            ),
            ELHBQN: GeckoBoolStructAccessor(
                self.struct, ELHBQN, AONPYY, LHBQNR, QBMJVH
            ),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, QBMJVH),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, QBMJVH),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, QBMJVH),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, QBMJVH),
        }

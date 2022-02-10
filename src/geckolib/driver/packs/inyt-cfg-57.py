#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v57'
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
ACCPQI = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
ACQFFT = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
AFIKJP = 112
AHEOCT = 38
AIIDNI = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
AJVDQL = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
AMJMAO = 115
AONPYY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
ASSAKQ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
AWBSIR = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
BDJQRJ = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
BFEGZU = 44
BIAMJM = 31
BJEUTO = 71
BLKXSJ = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
BQNRXC = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
BSKSOK = "".join(chr(c) for c in [79, 117, 116, 54])
BSSUHB = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
BVWVUB = 102
BWJYKL = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
BXTIAC = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
BXYBQS = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
CBFEGZ = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
CCPQIP = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
CHWDAF = 110
CQBMJV = 0
CQFFTT = 95
CRTFMN = 6
CTHBSK = 40
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
CXQIEF = 15
DAFIKJ = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 51]
)
DJQRJJ = 107
DNIBXT = 91
DQLAII = 88
DSBDJQ = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
DUBSSU = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
EFXQGL = 26
EGZUQE = 45
EJNIBX = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
EKCWAO = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
EKVKZI = "".join(chr(c) for c in [76, 105, 110, 101, 50])
ELHBQN = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
EOCTHB = 39
EXLSXU = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
FCRTFM = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
FEFJTA = 118
FEGZUQ = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
FFTTID = 96
FIKJPU = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
FJTACC = 32
FMNHTB = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
FTTIDU = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
FWRKIN = 114
FYLJUI = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
GDSBDJ = 105
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
GQPLSP = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
GSELHB = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
GTYIYW = 1
GVUNXN = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
GZUQEX = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
HBQNRX = 5
HBSKSO = 50
HBVWVU = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 23
HTBJEU = 10
HUGTYI = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
HUOJRJ = 20
HWDAFI = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 50]
)
HXEKVK = "".join(chr(c) for c in [70, 50, 51])
IACQFF = 94
IAMJMA = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
IBXTIA = 92
IBXYBQ = 53
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 52])
IDNIBX = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
IDUBSS = 98
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IFJBIA = "".join(chr(c) for c in [67])
IGYOUS = "".join(chr(c) for c in [80, 49])
IIDNIB = 90
IKFWRK = 77
IKJPUN = 113
ILXWAJ = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
INEJNI = "".join(chr(c) for c in [67, 69])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
IRYXBQ = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
IUXFEF = 0
IVDNQG = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = 76
JBIAMJ = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
JEUTOP = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
JHIUSO = "".join(chr(c) for c in [79, 117, 116, 49, 50])
JIGYOU = 78
JJJVYF = 109
JJVYFC = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
JMAOAW = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
JMCBFE = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
JNIBXY = 52
JPUNRJ = 119
JQRJJJ = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
JRJHIU = "".join(chr(c) for c in [79, 117, 116, 49, 49])
JTACCP = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
JUGSEL = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
JUTYEK = "".join(chr(c) for c in [76, 73])
JVDQLA = 87
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = 3
JWMNZM = 60
JYMOUN = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
KCWAON = 54
KFWRKI = "".join(
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
KINEJN = "".join(chr(c) for c in [85, 76])
KJPUNR = "".join(
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
KLGQPL = 30
KMLOIJ = 64
KPHUOJ = 19
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 50])
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 55])
KVKZIL = "".join(chr(c) for c in [76, 105, 110, 101, 51])
KWIVDN = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
KXSJWM = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
KZILXW = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
LAIIDN = 89
LASSAK = "".join(chr(c) for c in [70, 97, 110])
LGQPLS = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
LJUIKF = "".join(chr(c) for c in [78, 105, 103, 104, 116])
LKXSJW = 58
LNMHXE = "".join(chr(c) for c in [70, 51])
LOIJUG = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
LRAHEO = 37
LSPFTS = 63
LSXUJU = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
LXWAJV = 85
MAOAWB = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
MCBFEG = 43
MHXEKV = "".join(chr(c) for c in [70, 50, 50])
MJIGYO = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
MJMAOA = "".join(chr(c) for c in [105, 110, 70, 108, 111])
MJVHFT = 12
MLOIJU = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
MNHTBJ = 8
MNZMJI = 61
MOUNBL = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
NHTBJE = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
NIBXTI = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
NIBXYB = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
NKMLOI = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
NMHXEK = "".join(chr(c) for c in [70, 50, 49])
NPYYLI = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
NQGVUN = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
NQJYMO = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
NQLNMH = "".join(chr(c) for c in [70, 49])
NRSJMC = 41
NRXCHW = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
NXNKML = "".join(chr(c) for c in [50, 52, 104])
NZMJIG = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
OAWBSI = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
OIJUGS = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
OJRJHI = 21
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 56])
ONPYYL = 56
OOQNRS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
OPHUGT = "".join(
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
OQNRSJ = 25
OUNBLK = "".join(chr(c) for c in [76, 111])
OUSPBW = 28
PFTSIF = 1
PHUGTY = 72
PHUOJR = "".join(chr(c) for c in [79, 117, 116, 57])
PICXQI = 14
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
POUYNQ = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
PQIPOU = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
PYYLIU = 81
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 47
QFFTTI = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
QFYLJU = 68
QGLRAH = 36
QGVUNX = 75
QIEFXQ = 16
QIPOUY = 27
QJYMOU = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
QLAIID = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
QLNMHX = "".join(chr(c) for c in [70, 50])
QNRSJM = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
QNRXCH = 6
QRJJJV = 108
QSNQLN = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
QXPICX = 13
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
RJHIUS = 22
RJJJVY = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
RJZTAT = 57
RKINEJ = 51
RSJMCB = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
RTFMNH = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
RXCHWD = 7
RYXBQF = 35
SAKQXP = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
SBDJQR = 106
SELHBQ = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
SIFJBI = "".join(chr(c) for c in [70])
SIRYXB = 3
SJMCBF = 42
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
SKSOKP = 17
SNQLNM = 83
SOKPHU = 18
SPBWJY = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
SPFTSI = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
SSAKQX = "".join(chr(c) for c in [72, 84, 82, 50])
SSUHBV = 100
SUHBVW = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
SXUJUT = 49
TACCPQ = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
TBJEUT = "".join(
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
TFMNHT = 116
THBSKS = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
TIDUBS = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
TOPHUG = 82
TSIFJB = 33
TTIDUB = 97
TYEKCW = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
TYIYWS = "".join(
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
UBSSUH = 99
UBYGDS = 104
UGSELH = 4
UGTYIY = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
UHBVWV = 101
UIKFWR = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
UJUTYE = 79
UNBLKX = "".join(chr(c) for c in [72, 105])
UNXNKM = "".join(chr(c) for c in [65, 109, 80, 109])
UOJRJH = "".join(chr(c) for c in [79, 117, 116, 49, 48])
UQEXLS = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
USOOQN = 24
USPBWJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
UTOPHU = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
UXFEFJ = 2
UYNQJY = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
VDNQGV = "".join(chr(c) for c in [83, 108, 97, 118, 101])
VDQLAI = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
VUNXNK = 34
VWVUBY = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
VYFCRT = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 86
WAONPY = 55
WBSIRY = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
WDAFIK = 111
WIVDNQ = 73
WJYKLG = 29
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
WRKINE = "".join(chr(c) for c in [85, 76, 95, 67, 69])
WSKWIV = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
WVUBYG = 103
XBQFYL = 66
XCHWDA = "".join(
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
XEKVKZ = "".join(chr(c) for c in [76, 105, 110, 101, 49])
XFEFJT = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
XLSXUJ = 48
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 51])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 53])
XSJWMN = 59
XTIACQ = 93
XUJUTY = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XWAJVD = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
XYBQSN = 74
YBQSNQ = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
YEKCWA = 80
YFCRTF = 4
YGDSBD = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
YIYWSK = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
YKLGQP = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
YLIUXF = "".join(chr(c) for c in [79, 119, 110])
YLJUIK = 70
YNQJYM = 57
YOUSPB = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
YXBQFY = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
YYLIUX = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 84
ZMJIGY = 62
ZUQEXL = 46
AKQXPI = [
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
]
AOAWBS = [MJMAOA, JMAOAW, MAOAWB]
BQSNQL = [LGQPLS, YBQSNQ]
BSIRYX = [AWBSIR, WBSIRY]
BYGDSB = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, XEKVKZ, EKVKZI, KVKZIL]
CPQIPO = [JTACCP, TACCPQ, ACCPQI, CCPQIP]
DNQGVU = [VLASSA, IVDNQG, VDNQGV]
EUTOPH = [JVHFTH, IPOUYN, JEUTOP]
FJBIAM = [SIFJBI, IFJBIA]
FXQGLR = [
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
GYOUSP = [JVHFTH, IGYOUS, PIPIVL]
IJUGSE = [LOIJUG, OIJUGS]
JUIKFW = [LGQPLS, LJUIKF]
JYKLGQ = [PIPIVL, IGYOUS]
LHBQNR = [SELHBQ, ELHBQN]
LIUXFE = [YYLIUX, YLIUXF]
NBLKXS = [OUNBLK, UNBLKX]
NEJNIB = [KINEJN, INEJNI]
NRJZTA = []
OUYNQJ = [IPOUYN, POUYNQ]
PBWJYK = [USPBWJ, SPBWJY]
PUNRJZ = [
    BMJVHF,
    KQXPIC,
    XPICXQ,
    ICXQIE,
    XQIEFX,
    IEFXQG,
    BSKSOK,
    KSOKPH,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    JRJHIU,
    JHIUSO,
    IUSOOQ,
    OOQNRS,
    XUJUTY,
]
QPLSPF = [LGQPLS, GQPLSP]
SKWIVD = [YWSKWI, WSKWIV]
SOOQNR = [
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
UNRJZT = [JUTYEK]
UTYEKC = [
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
    JUTYEK,
]
VKZILX = [NQLNMH, QLNMHX, LNMHXE, NMHXEK, MHXEKV, HXEKVK, XEKVKZ, EKVKZI, KVKZIL]
XNKMLO = [JVHFTH, UNXNKM, NXNKML]
YMOUNB = [NQJYMO, QJYMOU, JYMOUN]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return RJZTAT

    @property
    def output_keys(self):
        return PUNRJZ

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, AKQXPI, None, None, QBMJVH
            ),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, AKQXPI, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, AKQXPI, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, AKQXPI, None, None, QBMJVH
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, QIEFXQ, None, AKQXPI, None, None, QBMJVH
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, None, FXQGLR, None, None, QBMJVH
            ),
            XQGLRA: GeckoByteStructAccessor(self.struct, XQGLRA, QGLRAH, QBMJVH),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoByteStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, QBMJVH),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, QBMJVH),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, SKSOKP, None, AKQXPI, None, None, QBMJVH
            ),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, AKQXPI, None, None, QBMJVH
            ),
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, AKQXPI, None, None, QBMJVH
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, None, AKQXPI, None, None, QBMJVH
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, AKQXPI, None, None, QBMJVH
            ),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, RJHIUS, None, AKQXPI, None, None, QBMJVH
            ),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, HIUSOO, None, AKQXPI, None, None, QBMJVH
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, None, SOOQNR, None, None, QBMJVH
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, OQNRSJ, None, SOOQNR, None, None, QBMJVH
            ),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, QBMJVH),
            RSJMCB: GeckoByteStructAccessor(self.struct, RSJMCB, SJMCBF, QBMJVH),
            JMCBFE: GeckoByteStructAccessor(self.struct, JMCBFE, MCBFEG, QBMJVH),
            CBFEGZ: GeckoByteStructAccessor(self.struct, CBFEGZ, BFEGZU, QBMJVH),
            FEGZUQ: GeckoByteStructAccessor(self.struct, FEGZUQ, EGZUQE, QBMJVH),
            GZUQEX: GeckoByteStructAccessor(self.struct, GZUQEX, ZUQEXL, QBMJVH),
            UQEXLS: GeckoByteStructAccessor(self.struct, UQEXLS, QEXLSX, QBMJVH),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, QBMJVH),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UJUTYE, None, UTYEKC, None, None, None
            ),
            TYEKCW: GeckoByteStructAccessor(self.struct, TYEKCW, YEKCWA, None),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, IUXFEF, LIUXFE, None, UXFEFJ, QBMJVH
            ),
            XFEFJT: GeckoByteStructAccessor(self.struct, XFEFJT, FEFJTA, QBMJVH),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, YMOUNB, None, None, QBMJVH
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, PYYLIU, UXFEFJ, NBLKXS, None, UXFEFJ, QBMJVH
            ),
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
            SPFTSI: GeckoTempStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, TSIFJB, None, FJBIAM, None, None, QBMJVH
            ),
            JBIAMJ: GeckoEnumStructAccessor(
                self.struct, JBIAMJ, BIAMJM, None, JYKLGQ, None, None, QBMJVH
            ),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, AMJMAO, None, AOAWBS, None, None, QBMJVH
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, PYYLIU, SIRYXB, BSIRYX, None, UXFEFJ, QBMJVH
            ),
            IRYXBQ: GeckoByteStructAccessor(self.struct, IRYXBQ, RYXBQF, QBMJVH),
            YXBQFY: GeckoTempStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoTempStructAccessor(self.struct, BQFYLJ, QFYLJU, QBMJVH),
            FYLJUI: GeckoEnumStructAccessor(
                self.struct, FYLJUI, YLJUIK, None, JUIKFW, None, None, QBMJVH
            ),
            UIKFWR: GeckoByteStructAccessor(self.struct, UIKFWR, IKFWRK, QBMJVH),
            KFWRKI: GeckoByteStructAccessor(self.struct, KFWRKI, FWRKIN, QBMJVH),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, RKINEJ, None, NEJNIB, None, None, QBMJVH
            ),
            EJNIBX: GeckoByteStructAccessor(self.struct, EJNIBX, JNIBXY, QBMJVH),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, None, BQSNQL, None, None, QBMJVH
            ),
            QSNQLN: GeckoEnumStructAccessor(
                self.struct, QSNQLN, SNQLNM, None, VKZILX, None, None, QBMJVH
            ),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, ZILXWA, None, VKZILX, None, None, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, LXWAJV, None, VKZILX, None, None, QBMJVH
            ),
            XWAJVD: GeckoEnumStructAccessor(
                self.struct, XWAJVD, WAJVDQ, None, VKZILX, None, None, QBMJVH
            ),
            AJVDQL: GeckoEnumStructAccessor(
                self.struct, AJVDQL, JVDQLA, None, VKZILX, None, None, QBMJVH
            ),
            VDQLAI: GeckoEnumStructAccessor(
                self.struct, VDQLAI, DQLAII, None, VKZILX, None, None, QBMJVH
            ),
            QLAIID: GeckoEnumStructAccessor(
                self.struct, QLAIID, LAIIDN, None, VKZILX, None, None, QBMJVH
            ),
            AIIDNI: GeckoEnumStructAccessor(
                self.struct, AIIDNI, IIDNIB, None, VKZILX, None, None, QBMJVH
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, DNIBXT, None, VKZILX, None, None, QBMJVH
            ),
            NIBXTI: GeckoEnumStructAccessor(
                self.struct, NIBXTI, IBXTIA, None, VKZILX, None, None, QBMJVH
            ),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, XTIACQ, None, VKZILX, None, None, QBMJVH
            ),
            TIACQF: GeckoEnumStructAccessor(
                self.struct, TIACQF, IACQFF, None, VKZILX, None, None, QBMJVH
            ),
            ACQFFT: GeckoEnumStructAccessor(
                self.struct, ACQFFT, CQFFTT, None, VKZILX, None, None, QBMJVH
            ),
            QFFTTI: GeckoEnumStructAccessor(
                self.struct, QFFTTI, FFTTID, None, VKZILX, None, None, QBMJVH
            ),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, TTIDUB, None, VKZILX, None, None, QBMJVH
            ),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, QBMJVH),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, QBMJVH),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, QBMJVH),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, QBMJVH),
            VWVUBY: GeckoByteStructAccessor(self.struct, VWVUBY, WVUBYG, QBMJVH),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, BYGDSB, None, None, QBMJVH
            ),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, GDSBDJ, None, BYGDSB, None, None, QBMJVH
            ),
            DSBDJQ: GeckoEnumStructAccessor(
                self.struct, DSBDJQ, SBDJQR, None, BYGDSB, None, None, QBMJVH
            ),
            BDJQRJ: GeckoEnumStructAccessor(
                self.struct, BDJQRJ, DJQRJJ, None, BYGDSB, None, None, QBMJVH
            ),
            JQRJJJ: GeckoEnumStructAccessor(
                self.struct, JQRJJJ, QRJJJV, None, BYGDSB, None, None, QBMJVH
            ),
            RJJJVY: GeckoEnumStructAccessor(
                self.struct, RJJJVY, JJJVYF, None, BYGDSB, None, None, QBMJVH
            ),
            JJVYFC: GeckoByteStructAccessor(self.struct, JJVYFC, JVYFCR, QBMJVH),
            VYFCRT: GeckoTimeStructAccessor(self.struct, VYFCRT, YFCRTF, QBMJVH),
            FCRTFM: GeckoTimeStructAccessor(self.struct, FCRTFM, CRTFMN, QBMJVH),
            RTFMNH: GeckoTimeStructAccessor(self.struct, RTFMNH, TFMNHT, QBMJVH),
            FMNHTB: GeckoTimeStructAccessor(self.struct, FMNHTB, MNHTBJ, QBMJVH),
            NHTBJE: GeckoTimeStructAccessor(self.struct, NHTBJE, HTBJEU, QBMJVH),
            TBJEUT: GeckoEnumStructAccessor(
                self.struct, TBJEUT, BJEUTO, None, EUTOPH, None, None, QBMJVH
            ),
            UTOPHU: GeckoBoolStructAccessor(
                self.struct, UTOPHU, TOPHUG, IUXFEF, QBMJVH
            ),
            OPHUGT: GeckoBoolStructAccessor(
                self.struct, OPHUGT, PHUGTY, UXFEFJ, QBMJVH
            ),
            HUGTYI: GeckoBoolStructAccessor(
                self.struct, HUGTYI, PHUGTY, IUXFEF, QBMJVH
            ),
            UGTYIY: GeckoBoolStructAccessor(
                self.struct, UGTYIY, PHUGTY, GTYIYW, QBMJVH
            ),
            TYIYWS: GeckoBoolStructAccessor(
                self.struct, TYIYWS, PHUGTY, SIRYXB, QBMJVH
            ),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, SKWIVD, None, None, QBMJVH
            ),
            KWIVDN: GeckoEnumStructAccessor(
                self.struct, KWIVDN, WIVDNQ, None, DNQGVU, None, None, QBMJVH
            ),
            NQGVUN: GeckoByteStructAccessor(self.struct, NQGVUN, QGVUNX, QBMJVH),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, XNKMLO, None, None, QBMJVH
            ),
            NKMLOI: GeckoWordStructAccessor(self.struct, NKMLOI, KMLOIJ, QBMJVH),
            MLOIJU: GeckoEnumStructAccessor(
                self.struct, MLOIJU, PYYLIU, GTYIYW, IJUGSE, None, UXFEFJ, QBMJVH
            ),
            JUGSEL: GeckoBoolStructAccessor(
                self.struct, JUGSEL, PYYLIU, UGSELH, QBMJVH
            ),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, PYYLIU, HBQNRX, LHBQNR, None, UXFEFJ, QBMJVH
            ),
            BQNRXC: GeckoBoolStructAccessor(
                self.struct, BQNRXC, PYYLIU, QNRXCH, QBMJVH
            ),
            NRXCHW: GeckoBoolStructAccessor(
                self.struct, NRXCHW, PYYLIU, RXCHWD, QBMJVH
            ),
            XCHWDA: GeckoBoolStructAccessor(
                self.struct, XCHWDA, CHWDAF, IUXFEF, QBMJVH
            ),
            HWDAFI: GeckoByteStructAccessor(self.struct, HWDAFI, WDAFIK, QBMJVH),
            DAFIKJ: GeckoByteStructAccessor(self.struct, DAFIKJ, AFIKJP, QBMJVH),
            FIKJPU: GeckoByteStructAccessor(self.struct, FIKJPU, IKJPUN, QBMJVH),
            KJPUNR: GeckoBoolStructAccessor(
                self.struct, KJPUNR, JPUNRJ, IUXFEF, QBMJVH
            ),
        }

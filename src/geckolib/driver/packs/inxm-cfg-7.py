#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v7'
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
ACCPQI = 4
ACQFFT = "".join(
    chr(c)
    for c in [70, 97, 110, 83, 101, 116, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
AFIKJP = "".join(chr(c) for c in [65, 109, 80, 109])
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114])
AIIDNI = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
AKQXPI = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
AMJMAO = 44
AOAWBS = 15
AONPYY = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
ASSAKQ = "".join(chr(c) for c in [70, 98, 76, 105])
AWBSIR = 13
BDJQRJ = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 51]
)
BFEGZU = "".join(chr(c) for c in [76, 73])
BIAMJM = 57
BJEUTO = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
BLKXSJ = 46
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = "".join(chr(c) for c in [78, 111])
BQNRXC = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
BQSNQL = 86
BSIRYX = "".join(chr(c) for c in [70])
BSKSOK = 109
BSSUHB = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        70,
        111,
        114,
        99,
        101,
        79,
        102,
        102,
        73,
        110,
        104,
        105,
        98,
        105,
        116,
        68,
        101,
        108,
        97,
        121,
    ]
)
BVWVUB = "".join(
    chr(c)
    for c in [86, 83, 80, 67, 104, 101, 99, 107, 102, 108, 111, 83, 112, 101, 101, 100]
)
BWJYKL = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
BXTIAC = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        70,
        111,
        114,
        99,
        101,
        79,
        70,
        70,
        79,
        112,
        116,
        105,
        111,
        110,
    ]
)
BXYBQS = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
BYGDSB = 8
CBFEGZ = 103
CCPQIP = "".join(chr(c) for c in [67, 112, 79, 116, 79, 112, 116, 105, 111, 110])
CHWDAF = 81
CPQIPO = 23
CQBMJV = 0
CQFFTT = 17
CRTFMN = 38
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c) for c in [70, 105, 98, 101, 114, 84, 105, 109, 101, 79, 117, 116]
)
CXQIEF = 94
DAFIKJ = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
DJQRJJ = 11
DNQGVU = 68
DQLAII = "".join(chr(c) for c in [80, 97, 117, 115, 101])
DSBDJQ = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 50]
)
DUBSSU = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        67,
        108,
        114,
        70,
        111,
        114,
        99,
        101,
        79,
        102,
        102,
        84,
        101,
        109,
        112,
        65,
        100,
        99,
    ]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
EFXQGL = 96
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
EJNIBX = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
EKVKZI = 91
ELHBQN = 77
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114])
EUTOPH = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
EXLSXU = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
FCRTFM = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
FEFJTA = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
FFTTID = 18
FIKJPU = "".join(chr(c) for c in [50, 52, 104])
FJBIAM = 56
FMNHTB = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTTIDU = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        99,
        116,
        105,
        118,
        101,
        68,
        101,
        108,
        97,
        121,
        65,
        102,
        116,
        101,
        114,
        80,
        117,
        109,
        112,
        82,
        117,
        110,
    ]
)
FWRKIN = 62
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 51, 65])
GDSBDJ = 9
GLRAHE = 102
GQPLSP = 54
GSELHB = 76
GTYIYW = "".join(chr(c) for c in [75, 54, 48, 48, 70, 111, 114, 77, 97, 121])
GVUNXN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52])
GYOUSP = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
GZUQEX = 104
HBQNRX = 78
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114])
HBVWVU = "".join(chr(c) for c in [80, 117, 109, 112, 51, 65, 115, 86, 83, 80])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 106
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HTBJEU = 65
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 54, 65])
HWDAFI = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
HXEKVK = 90
IACQFF = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        115,
        67,
        111,
        111,
        108,
        105,
        110,
        103,
        68,
        101,
        118,
        105,
        99,
        101,
    ]
)
IAMJMA = "".join(chr(c) for c in [83, 97, 110, 105, 76, 101, 118, 101, 108])
IBXTIA = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        99,
        116,
        105,
        118,
        101,
        79,
        110,
        80,
        117,
        109,
        112,
        82,
        117,
        110,
    ]
)
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 49, 66])
IDNIBX = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
IDUBSS = 20
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 50, 66])
IFJBIA = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
IGYOUS = 48
IIDNIB = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
IJUGSE = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
IKFWRK = 5
ILXWAJ = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
IRYXBQ = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
IUSOOQ = "".join(chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114])
IVLASS = "".join(chr(c) for c in [])
IYWSKW = "".join(chr(c) for c in [67, 108, 101, 97, 110, 70, 105, 108, 116, 101, 114])
JBIAMJ = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
JHIUSO = 116
JIGYOU = "".join(
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
JJJVYF = 28
JJVYFC = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
JMAOAW = 45
JMCBFE = 115
JNIBXY = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
JQRJJJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
JRJHIU = 101
JTACCP = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
JUGSEL = 75
JUIKFW = 14
JUTYEK = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
JVDQLA = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = 30
JWMNZM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
JYKLGQ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
JYMOUN = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
KCWAON = 2
KFWRKI = "".join(
    chr(c)
    for c in [
        69,
        99,
        111,
        110,
        66,
        101,
        108,
        111,
        119,
        83,
        101,
        116,
        112,
        111,
        105,
        110,
        116,
    ]
)
KINEJN = "".join(chr(c) for c in [53, 48, 72, 90])
KJPUNR = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 69, 110, 97, 98, 108, 101]
)
KMLOIJ = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55])
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 53, 65])
KQXPIC = "".join(chr(c) for c in [83, 65, 78, 73])
KSOKPH = 110
KVKZIL = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
KWIVDN = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 111, 118, 101, 114])
KXSJWM = 47
KZILXW = "".join(
    chr(c) for c in [67, 69, 95, 50, 120, 50, 48, 65, 108, 108, 111, 119, 101, 100]
)
LAIIDN = "".join(
    chr(c)
    for c in [
        81,
        117,
        105,
        101,
        116,
        65,
        99,
        116,
        105,
        111,
        110,
        79,
        110,
        72,
        101,
        97,
        116,
        101,
        114,
    ]
)
LASSAK = "".join(chr(c) for c in [70, 98, 77, 116, 114])
LGQPLS = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
LHBQNR = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
LIUXFE = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
LJUIKF = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
LKXSJW = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
LNMHXE = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
LOIJUG = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56])
LRAHEO = "".join(chr(c) for c in [72, 84, 82])
LSPFTS = 59
LSXUJU = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
LXWAJV = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
MAOAWB = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 76, 105])
MHXEKV = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
MJIGYO = 52
MJMAOA = "".join(chr(c) for c in [83, 97, 110, 105, 79, 110, 84, 105, 109, 101])
MJVHFT = 93
MLOIJU = 73
MNHTBJ = 63
MNZMJI = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
MOUNBL = "".join(chr(c) for c in [72, 105])
NBLKXS = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
NEJNIB = 1
NHTBJE = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
NIBXTI = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        65,
        99,
        116,
        105,
        118,
        101,
        79,
        110,
        65,
        109,
        98,
        105,
        97,
        110,
        116,
        79,
        84,
    ]
)
NIBXYB = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
NKMLOI = 72
NMHXEK = 89
NPYYLI = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
NQGVUN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51])
NQLNMH = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114])
NRXCHW = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
NXNKML = 71
NZMJIG = 51
OAWBSI = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
OCTHBS = 107
OIJUGS = 74
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 55, 65])
OKPHUO = 98
ONPYYL = 61
OOQNRS = 112
OPHUGT = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114])
OUSPBW = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
OUYNQJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
PFTSIF = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
PHUGTY = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
PHUOJR = 99
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
PQIPOU = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
PYYLIU = 26
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 105
QFFTTI = "".join(
    chr(c)
    for c in [70, 97, 110, 67, 108, 114, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
QFYLJU = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
QGVUNX = 69
QIEFXQ = 95
QIPOUY = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
QJYMOU = 6
QLNMHX = 88
QNRSJM = 113
QNRXCH = 79
QRJJJV = 27
QSNQLN = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
QXPICX = "".join(chr(c) for c in [79, 78, 90, 69, 78])
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RJJJVY = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
RKINEJ = "".join(chr(c) for c in [54, 48, 72, 90])
RSJMCB = 114
RTFMNH = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
RXCHWD = 80
RYXBQF = 12
SAKQXP = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
SBDJQR = 10
SELHBQ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
SIFJBI = 58
SJMCBF = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
SJWMNZ = 49
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114])
SKWIVD = "".join(chr(c) for c in [67, 104, 97, 110, 103, 101, 87, 97, 116, 101, 114])
SNQLNM = 87
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 52, 65])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114])
SPBWJY = "".join(chr(c) for c in [80, 49])
SPFTSI = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
SSAKQX = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SSUHBV = 22
SUHBVW = "".join(chr(c) for c in [80, 117, 109, 112, 49, 65, 115, 86, 83, 80])
SXUJUT = 4
TACCPQ = 25
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
TFMNHT = 40
THBSKS = 108
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
TIDUBS = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        83,
        101,
        116,
        70,
        111,
        114,
        99,
        101,
        79,
        102,
        102,
        84,
        101,
        109,
        112,
        65,
        100,
        99,
    ]
)
TOPHUG = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
TSIFJB = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
TTIDUB = 19
TYEKCW = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
TYIYWS = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49])
UBSSUH = 21
UBYGDS = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 48]
)
UGSELH = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
UGTYIY = "".join(
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
UHBVWV = 5
UIKFWR = "".join(
    chr(c)
    for c in [
        79,
        118,
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
        69,
        110,
        97,
        98,
        108,
        101,
    ]
)
UJUTYE = 2
UNBLKX = 0
UNXNKM = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53])
UOJRJH = 100
UQEXLS = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
USOOQN = 111
USPBWJ = 117
UTOPHU = "".join(
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
UTYEKC = 1
UXFEFJ = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
UYNQJY = "".join(chr(c) for c in [65, 110, 121, 85, 68])
VDNQGV = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50])
VDQLAI = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 92
VLASSA = "".join(chr(c) for c in [70, 65, 78])
VUBYGD = 7
VUNXNK = 70
VWVUBY = 6
VYFCRT = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(
    chr(c) for c in [67, 97, 110, 99, 101, 108, 79, 116, 104, 101, 114, 85, 68]
)
WAONPY = 3
WBSIRY = "".join(chr(c) for c in [67])
WDAFIK = 82
WIVDNQ = "".join(
    chr(c) for c in [82, 101, 112, 108, 97, 99, 101, 70, 105, 108, 116, 101, 114]
)
WJYKLG = 55
WMNZMJ = 50
WRKINE = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
WSKWIV = "".join(chr(c) for c in [67, 104, 101, 99, 107, 71, 70, 67, 73])
WVUBYG = "".join(
    chr(c) for c in [86, 83, 80, 70, 105, 108, 116, 101, 114, 83, 112, 101, 101, 100]
)
XBQFYL = 83
XCHWDA = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
XEKVKZ = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
XFEFJT = 24
XLSXUJ = 84
XNKMLO = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54])
XPICXQ = "".join(chr(c) for c in [86, 65, 76, 86, 69])
XQGLRA = 97
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 50, 65])
XSJWMN = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
XTIACQ = 7
XUJUTY = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
XWAJVD = "".join(
    chr(c) for c in [82, 101, 115, 116, 111, 114, 101, 65, 108, 108, 85, 68]
)
XYBQSN = 85
YBQSNQ = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
YEKCWA = "".join(chr(c) for c in [79, 119, 110])
YFCRTF = 36
YGDSBD = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 49]
)
YIYWSK = 67
YKLGQP = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
YLIUXF = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
YLJUIK = 3
YMOUNB = "".join(chr(c) for c in [76, 111])
YNQJYM = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
YOUSPB = 53
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [80, 72])
YXBQFY = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
YYLIUX = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 60
ZMJIGY = "".join(
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
AJVDQL = [LXWAJV, XWAJVD, JVHFTH, WAJVDQ]
DNIBXT = [AIIDNI, IIDNIB, IDNIBX, IVLASS]
EKCWAO = [TYEKCW, YEKCWA]
FEGZUQ = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    BFEGZU,
]
FJTACC = [FEFJTA, EFJTAC]
FTSIFJ = [SPFTSI, PFTSIF]
FYLJUI = [BQFYLJ, QFYLJU]
HIUSOO = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    PIPIVL,
]
HUGTYI = [OPHUGT, PHUGTY]
IBXYBQ = [JNIBXY, NIBXYB]
IKJPUN = [AFIKJP, FIKJPU]
INEJNI = [RKINEJ, KINEJN]
IUXFEF = [YYLIUX, YLIUXF, LIUXFE]
IVDNQG = [IYWSKW, YWSKWI, WSKWIV, SKWIVD, KWIVDN, WIVDNQ]
JEUTOP = [JVHFTH, BJEUTO]
JPUNRJ = [
    BMJVHF,
    ICXQIE,
    XQIEFX,
    IEFXQG,
    FXQGLR,
    QGLRAH,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RJHIUS,
    MCBFEG,
    EGZUQE,
    UQEXLS,
]
KLGQPL = [JYKLGQ, YKLGQP]
NQJYMO = [UYNQJY, YNQJYM]
OUNBLK = [YMOUNB, MOUNBL]
PBWJYK = [JVHFTH, SPBWJY, PIPIVL]
PICXQI = [
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
    IVLASS,
    VLASSA,
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
    KQXPIC,
    QXPICX,
    XPICXQ,
]
POUYNQ = [PQIPOU, QIPOUY, IPOUYN]
PUNRJZ = [BFEGZU]
QLAIID = [VDQLAI, DQLAII]
QPLSPF = [PIPIVL, SPBWJY]
RAHEOC = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    LRAHEO,
]
SIRYXB = [WBSIRY, BSIRYX]
UNRJZT = []
ZUQEXL = [
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
    BFEGZU,
    VLASSA,
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
    KQXPIC,
    QXPICX,
    XPICXQ,
]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return XTIACQ

    @property
    def output_keys(self):
        return JPUNRJ

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, PICXQI, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, PICXQI, None, None, QBMJVH
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, QIEFXQ, None, PICXQI, None, None, QBMJVH
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, None, PICXQI, None, None, QBMJVH
            ),
            FXQGLR: GeckoEnumStructAccessor(
                self.struct, FXQGLR, XQGLRA, None, PICXQI, None, None, QBMJVH
            ),
            QGLRAH: GeckoEnumStructAccessor(
                self.struct, QGLRAH, GLRAHE, None, RAHEOC, None, None, QBMJVH
            ),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoByteStructAccessor(self.struct, CTHBSK, THBSKS, QBMJVH),
            HBSKSO: GeckoByteStructAccessor(self.struct, HBSKSO, BSKSOK, QBMJVH),
            SKSOKP: GeckoByteStructAccessor(self.struct, SKSOKP, KSOKPH, QBMJVH),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, OKPHUO, None, PICXQI, None, None, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, PICXQI, None, None, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, PICXQI, None, None, QBMJVH
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, PICXQI, None, None, QBMJVH
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, HIUSOO, None, None, QBMJVH
            ),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoByteStructAccessor(self.struct, SJMCBF, JMCBFE, QBMJVH),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, FEGZUQ, None, None, QBMJVH
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, GZUQEX, None, ZUQEXL, None, None, QBMJVH
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, None, ZUQEXL, None, None, QBMJVH
            ),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, QBMJVH),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoByteStructAccessor(self.struct, XUJUTY, UJUTYE, QBMJVH),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, UTYEKC, KCWAON, EKCWAO, None, KCWAON, QBMJVH
            ),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, IUXFEF, None, None, QBMJVH
            ),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, None, FJTACC, None, None, QBMJVH
            ),
            JTACCP: GeckoBoolStructAccessor(
                self.struct, JTACCP, TACCPQ, ACCPQI, QBMJVH
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, POUYNQ, None, None, QBMJVH
            ),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, TACCPQ, QJYMOU, NQJYMO, None, KCWAON, QBMJVH
            ),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, TACCPQ, UNBLKX, OUNBLK, None, KCWAON, QBMJVH
            ),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, USPBWJ, None, PBWJYK, None, None, QBMJVH
            ),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, KLGQPL, None, None, QBMJVH
            ),
            LGQPLS: GeckoEnumStructAccessor(
                self.struct, LGQPLS, GQPLSP, None, QPLSPF, None, None, QBMJVH
            ),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, FTSIFJ, None, None, QBMJVH
            ),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoEnumStructAccessor(
                self.struct, IFJBIA, FJBIAM, None, NQJYMO, None, None, QBMJVH
            ),
            JBIAMJ: GeckoByteStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoByteStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoByteStructAccessor(self.struct, MJMAOA, JMAOAW, QBMJVH),
            MAOAWB: GeckoTempStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, KCWAON, SIRYXB, None, KCWAON, QBMJVH
            ),
            IRYXBQ: GeckoEnumStructAccessor(
                self.struct, IRYXBQ, RYXBQF, None, QPLSPF, None, None, QBMJVH
            ),
            YXBQFY: GeckoEnumStructAccessor(
                self.struct, YXBQFY, XBQFYL, YLJUIK, FYLJUI, None, KCWAON, QBMJVH
            ),
            LJUIKF: GeckoBoolStructAccessor(
                self.struct, LJUIKF, JUIKFW, ACCPQI, QBMJVH
            ),
            UIKFWR: GeckoBoolStructAccessor(
                self.struct, UIKFWR, JUIKFW, IKFWRK, QBMJVH
            ),
            KFWRKI: GeckoByteStructAccessor(self.struct, KFWRKI, FWRKIN, QBMJVH),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, XBQFYL, NEJNIB, INEJNI, None, KCWAON, QBMJVH
            ),
            EJNIBX: GeckoEnumStructAccessor(
                self.struct, EJNIBX, XBQFYL, KCWAON, IBXYBQ, None, KCWAON, QBMJVH
            ),
            BXYBQS: GeckoByteStructAccessor(self.struct, BXYBQS, XYBQSN, None),
            YBQSNQ: GeckoByteStructAccessor(self.struct, YBQSNQ, BQSNQL, None),
            QSNQLN: GeckoByteStructAccessor(self.struct, QSNQLN, SNQLNM, None),
            NQLNMH: GeckoByteStructAccessor(self.struct, NQLNMH, QLNMHX, QBMJVH),
            LNMHXE: GeckoByteStructAccessor(self.struct, LNMHXE, NMHXEK, QBMJVH),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoByteStructAccessor(self.struct, XEKVKZ, EKVKZI, QBMJVH),
            KVKZIL: GeckoByteStructAccessor(self.struct, KVKZIL, VKZILX, QBMJVH),
            KZILXW: GeckoBoolStructAccessor(
                self.struct, KZILXW, ZILXWA, QJYMOU, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, ZILXWA, NEJNIB, AJVDQL, None, ACCPQI, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, ZILXWA, UNBLKX, QLAIID, None, KCWAON, QBMJVH
            ),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AWBSIR, YLJUIK, DNIBXT, None, ACCPQI, QBMJVH
            ),
            NIBXTI: GeckoBoolStructAccessor(
                self.struct, NIBXTI, AWBSIR, IKFWRK, QBMJVH
            ),
            IBXTIA: GeckoBoolStructAccessor(
                self.struct, IBXTIA, AWBSIR, QJYMOU, QBMJVH
            ),
            BXTIAC: GeckoBoolStructAccessor(
                self.struct, BXTIAC, AWBSIR, XTIACQ, QBMJVH
            ),
            TIACQF: GeckoEnumStructAccessor(
                self.struct, TIACQF, JUIKFW, NEJNIB, PBWJYK, None, ACCPQI, QBMJVH
            ),
            IACQFF: GeckoBoolStructAccessor(
                self.struct, IACQFF, JUIKFW, YLJUIK, QBMJVH
            ),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, QBMJVH),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, QBMJVH),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, QBMJVH),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, QBMJVH),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, QBMJVH),
            SUHBVW: GeckoBoolStructAccessor(
                self.struct, SUHBVW, UHBVWV, UNBLKX, QBMJVH
            ),
            HBVWVU: GeckoBoolStructAccessor(
                self.struct, HBVWVU, UHBVWV, KCWAON, QBMJVH
            ),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, QBMJVH),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, QBMJVH),
            UBYGDS: GeckoByteStructAccessor(self.struct, UBYGDS, BYGDSB, QBMJVH),
            YGDSBD: GeckoByteStructAccessor(self.struct, YGDSBD, GDSBDJ, QBMJVH),
            DSBDJQ: GeckoByteStructAccessor(self.struct, DSBDJQ, SBDJQR, QBMJVH),
            BDJQRJ: GeckoByteStructAccessor(self.struct, BDJQRJ, DJQRJJ, QBMJVH),
            JQRJJJ: GeckoByteStructAccessor(self.struct, JQRJJJ, QRJJJV, QBMJVH),
            RJJJVY: GeckoTimeStructAccessor(self.struct, RJJJVY, JJJVYF, QBMJVH),
            JJVYFC: GeckoTimeStructAccessor(self.struct, JJVYFC, JVYFCR, QBMJVH),
            VYFCRT: GeckoTimeStructAccessor(self.struct, VYFCRT, YFCRTF, QBMJVH),
            FCRTFM: GeckoTimeStructAccessor(self.struct, FCRTFM, CRTFMN, QBMJVH),
            RTFMNH: GeckoByteStructAccessor(self.struct, RTFMNH, TFMNHT, QBMJVH),
            FMNHTB: GeckoTimeStructAccessor(self.struct, FMNHTB, MNHTBJ, QBMJVH),
            NHTBJE: GeckoTimeStructAccessor(self.struct, NHTBJE, HTBJEU, QBMJVH),
            TBJEUT: GeckoEnumStructAccessor(
                self.struct, TBJEUT, ZILXWA, ACCPQI, JEUTOP, None, KCWAON, QBMJVH
            ),
            EUTOPH: GeckoBoolStructAccessor(
                self.struct, EUTOPH, ZILXWA, IKFWRK, QBMJVH
            ),
            UTOPHU: GeckoBoolStructAccessor(
                self.struct, UTOPHU, ZILXWA, YLJUIK, QBMJVH
            ),
            TOPHUG: GeckoEnumStructAccessor(
                self.struct, TOPHUG, UTYEKC, UNBLKX, HUGTYI, None, KCWAON, QBMJVH
            ),
            UGTYIY: GeckoBoolStructAccessor(
                self.struct, UGTYIY, UTYEKC, NEJNIB, QBMJVH
            ),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, XBQFYL, UNBLKX, IKJPUN, None, KCWAON, QBMJVH
            ),
            KJPUNR: GeckoBoolStructAccessor(
                self.struct, KJPUNR, JUIKFW, UNBLKX, QBMJVH
            ),
        }

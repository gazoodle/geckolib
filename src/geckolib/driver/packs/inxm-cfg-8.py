#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v8'
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
ACCPQI = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
ACQFFT = "".join(
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
AFIKJP = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114])
AIIDNI = "".join(
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
AKQXPI = "".join(chr(c) for c in [79, 78, 90, 69, 78])
AMJMAO = 15
AOAWBS = "".join(chr(c) for c in [70])
AONPYY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
ASSAKQ = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
AWBSIR = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
BDJQRJ = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
BIAMJM = 45
BJEUTO = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
BLKXSJ = 49
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
BQNRXC = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
BQSNQL = 88
BSIRYX = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
BSKSOK = 110
BSSUHB = "".join(chr(c) for c in [80, 117, 109, 112, 51, 65, 115, 86, 83, 80])
BVWVUB = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 48]
)
BXTIAC = "".join(
    chr(c)
    for c in [70, 97, 110, 83, 101, 116, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
BXYBQS = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
BYGDSB = 10
CCPQIP = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
CHWDAF = "".join(chr(c) for c in [65, 109, 80, 109])
CQBMJV = 0
CQFFTT = 19
CRTFMN = 63
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
CXQIEF = 95
DAFIKJ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 69, 110, 97, 98, 108, 101]
)
DJQRJJ = 28
DNIBXT = 7
DNQGVU = 70
DQLAII = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
DSBDJQ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
DUBSSU = "".join(chr(c) for c in [80, 117, 109, 112, 49, 65, 115, 86, 83, 80])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 4
EFXQGL = 97
EJNIBX = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
EKCWAO = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
EKVKZI = 60
ELHBQN = 79
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114])
EUTOPH = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
EXLSXU = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
FCRTFM = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
FEFJTA = 25
FEGZUQ = 104
FFTTID = 20
FJBIAM = 44
FJTACC = "".join(chr(c) for c in [67, 112, 79, 116, 79, 112, 116, 105, 111, 110])
FMNHTB = "".join(
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
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 56
FTTIDU = "".join(
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
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
FYLJUI = "".join(
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
GDSBDJ = 11
GQPLSP = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
GSELHB = 78
GTYIYW = "".join(chr(c) for c in [80, 72])
GVUNXN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54])
GYOUSP = "".join(chr(c) for c in [80, 49])
GZUQEX = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
HBQNRX = 80
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114])
HBVWVU = 7
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 107
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 111
HTBJEU = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
HUGTYI = 67
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 55, 65])
HWDAFI = "".join(chr(c) for c in [50, 52, 104])
HXEKVK = 92
IACQFF = 18
IAMJMA = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
IBXTIA = "".join(
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
IBXYBQ = 86
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 50, 65])
IDNIBX = "".join(
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
IDUBSS = 22
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 51, 65])
IFJBIA = "".join(chr(c) for c in [83, 97, 110, 105, 76, 101, 118, 101, 108])
IGYOUS = 117
IIDNIB = "".join(
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
IJUGSE = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
IKFWRK = "".join(chr(c) for c in [54, 48, 72, 90])
INEJNI = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
IRYXBQ = "".join(chr(c) for c in [78, 111])
IUSOOQ = "".join(chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114])
IUXFEF = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
IVDNQG = 69
IVLASS = "".join(chr(c) for c in [])
IYWSKW = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 111, 118, 101, 114])
JBIAMJ = "".join(chr(c) for c in [83, 97, 110, 105, 79, 110, 84, 105, 109, 101])
JEUTOP = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
JHIUSO = "".join(chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114])
JIGYOU = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
JJJVYF = 36
JJVYFC = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
JMAOAW = 13
JMCBFE = 103
JNIBXY = 85
JPUNRJ = 8
JQRJJJ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
JRJHIU = 116
JTACCP = 23
JUGSEL = 77
JUIKFW = 62
JUTYEK = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
JVDQLA = "".join(
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
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = 38
JWMNZM = "".join(
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
JYKLGQ = 54
JYMOUN = 0
KCWAON = 61
KFWRKI = "".join(chr(c) for c in [53, 48, 72, 90])
KINEJN = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
KLGQPL = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
KMLOIJ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 54, 65])
KQXPIC = "".join(chr(c) for c in [86, 65, 76, 86, 69])
KSOKPH = 98
KVKZIL = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
KWIVDN = 68
KXSJWM = 50
KZILXW = "".join(
    chr(c) for c in [82, 101, 115, 116, 111, 114, 101, 65, 108, 108, 85, 68]
)
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = 59
LHBQNR = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
LIUXFE = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
LJUIKF = "".join(
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
LKXSJW = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
LNMHXE = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
LOIJUG = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114])
LSPFTS = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
LSXUJU = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
LXWAJV = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
MAOAWB = "".join(chr(c) for c in [67])
MCBFEG = "".join(chr(c) for c in [76, 73])
MHXEKV = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
MJIGYO = 53
MJMAOA = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
MJVHFT = 93
MLOIJU = 75
MNHTBJ = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
MNZMJI = "".join(
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
MOUNBL = 46
NBLKXS = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
NIBXTI = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
NIBXYB = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
NKMLOI = 74
NMHXEK = 91
NPYYLI = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
NQGVUN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53])
NQJYMO = "".join(chr(c) for c in [72, 105])
NQLNMH = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
NRSJMC = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
NRXCHW = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
NXNKML = 73
NZMJIG = 48
OCTHBS = 108
OIJUGS = 76
OJRJHI = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
OKPHUO = 99
ONPYYL = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
OOQNRS = 113
OPHUGT = "".join(chr(c) for c in [75, 54, 48, 48, 70, 111, 114, 77, 97, 121])
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114])
OUNBLK = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
OUSPBW = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
OUYNQJ = 6
PBWJYK = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
PFTSIF = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
PHUGTY = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49])
PHUOJR = 100
PICXQI = 94
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PQIPOU = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 84
QFFTTI = "".join(
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
QFYLJU = 14
QGLRAH = "".join(chr(c) for c in [72, 84, 82])
QGVUNX = 71
QIEFXQ = 96
QIPOUY = "".join(chr(c) for c in [65, 110, 121, 85, 68])
QLAIID = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
QLNMHX = 90
QNRSJM = 114
QNRXCH = 81
QPLSPF = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
QRJJJV = 30
QSNQLN = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
RAHEOC = 106
RJJJVY = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
RKINEJ = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
RSJMCB = 115
RTFMNH = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
RXCHWD = 82
RYXBQF = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
SAKQXP = "".join(chr(c) for c in [83, 65, 78, 73])
SBDJQR = 27
SELHBQ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
SIFJBI = 57
SIRYXB = 83
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 76, 105])
SJWMNZ = 51
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 52, 65])
SKWIVD = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50])
SNQLNM = 89
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 53, 65])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114])
SPBWJY = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
SPFTSI = 58
SSAKQX = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
SSUHBV = "".join(
    chr(c)
    for c in [86, 83, 80, 67, 104, 101, 99, 107, 102, 108, 111, 83, 112, 101, 101, 100]
)
SUHBVW = 6
SXUJUT = 2
TACCPQ = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
TBJEUT = "".join(
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
TFMNHT = 65
THBSKS = 109
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(
    chr(c)
    for c in [70, 97, 110, 67, 108, 114, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
TIDUBS = "".join(
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
TOPHUG = "".join(
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
TSIFJB = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
TTIDUB = 21
TYIYWS = "".join(chr(c) for c in [67, 104, 101, 99, 107, 71, 70, 67, 73])
UBSSUH = 5
UBYGDS = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 50]
)
UGSELH = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
UGTYIY = "".join(chr(c) for c in [67, 108, 101, 97, 110, 70, 105, 108, 116, 101, 114])
UHBVWV = "".join(
    chr(c) for c in [86, 83, 80, 70, 105, 108, 116, 101, 114, 83, 112, 101, 101, 100]
)
UIKFWR = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
UJUTYE = 1
UNBLKX = 47
UNXNKM = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55])
UOJRJH = 101
UQEXLS = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
USOOQN = 112
USPBWJ = 55
UTYEKC = "".join(chr(c) for c in [79, 119, 110])
UYNQJY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
VDNQGV = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52])
VDQLAI = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
VLASSA = "".join(chr(c) for c in [70, 65, 78])
VUBYGD = 9
VUNXNK = 72
VWVUBY = 8
VYFCRT = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [80, 97, 117, 115, 101])
WAONPY = 26
WBSIRY = 12
WIVDNQ = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51])
WJYKLG = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
WMNZMJ = 52
WRKINE = 1
WVUBYG = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 49]
)
XBQFYL = 3
XCHWDA = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
XEKVKZ = "".join(
    chr(c) for c in [67, 69, 95, 50, 120, 50, 48, 65, 108, 108, 111, 119, 101, 100]
)
XFEFJT = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
XLSXUJ = 4
XNKMLO = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 49, 66])
XQGLRA = 102
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 50, 66])
XSJWMN = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
XTIACQ = 17
XUJUTY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
XWAJVD = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
XYBQSN = 87
YBQSNQ = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
YEKCWA = 2
YFCRTF = 40
YGDSBD = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 51]
)
YIYWSK = "".join(chr(c) for c in [67, 104, 97, 110, 103, 101, 87, 97, 116, 101, 114])
YLIUXF = 24
YLJUIK = 5
YMOUNB = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
YNQJYM = "".join(chr(c) for c in [76, 111])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
    chr(c) for c in [82, 101, 112, 108, 97, 99, 101, 70, 105, 108, 116, 101, 114]
)
YYLIUX = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(
    chr(c) for c in [67, 97, 110, 99, 101, 108, 79, 116, 104, 101, 114, 85, 68]
)
ZMJIGY = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
ZUQEXL = 105
AJVDQL = [XWAJVD, WAJVDQ]
BWJYKL = [SPBWJY, PBWJYK]
CBFEGZ = [
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
    MCBFEG,
]
CPQIPO = [TACCPQ, ACCPQI, CCPQIP]
EGZUQE = [
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
    MCBFEG,
    VLASSA,
    IVLASS,
    IVLASS,
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
    KQXPIC,
]
FIKJPU = [
    BMJVHF,
    XPICXQ,
    ICXQIE,
    XQIEFX,
    IEFXQG,
    FXQGLR,
    SKSOKP,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    SJMCBF,
    BFEGZU,
    GZUQEX,
]
FWRKIN = [IKFWRK, KFWRKI]
GLRAHE = [
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
    QGLRAH,
]
IKJPUN = [MCBFEG]
ILXWAJ = [VKZILX, KZILXW, JVHFTH, ZILXWA]
KJPUNR = []
LAIIDN = [VDQLAI, DQLAII, QLAIID, IVLASS]
NEJNIB = [KINEJN, INEJNI]
NHTBJE = [JVHFTH, MNHTBJ]
OAWBSI = [MAOAWB, AOAWBS]
PLSPFT = [GQPLSP, QPLSPF]
POUYNQ = [QIPOUY, IPOUYN]
PYYLIU = [AONPYY, ONPYYL, NPYYLI]
QJYMOU = [YNQJYM, NQJYMO]
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
    IVLASS,
    VLASSA,
    IVLASS,
    IVLASS,
    LASSAK,
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
    KQXPIC,
]
RJHIUS = [
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
TYEKCW = [JUTYEK, UTYEKC]
UTOPHU = [JEUTOP, EUTOPH]
UXFEFJ = [LIUXFE, IUXFEF]
WDAFIK = [CHWDAF, HWDAFI]
WSKWIV = [UGTYIY, GTYIYW, TYIYWS, YIYWSK, IYWSKW, YWSKWI]
YKLGQP = [PIPIVL, GYOUSP]
YOUSPB = [JVHFTH, GYOUSP, PIPIVL]
YXBQFY = [IRYXBQ, RYXBQF]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return JPUNRJ

    @property
    def output_keys(self):
        return FIKJPU

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
                self.struct, FXQGLR, XQGLRA, None, GLRAHE, None, None, QBMJVH
            ),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoByteStructAccessor(self.struct, CTHBSK, THBSKS, QBMJVH),
            HBSKSO: GeckoByteStructAccessor(self.struct, HBSKSO, BSKSOK, QBMJVH),
            SKSOKP: GeckoEnumStructAccessor(
                self.struct, SKSOKP, KSOKPH, None, QXPICX, None, None, QBMJVH
            ),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, OKPHUO, None, QXPICX, None, None, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, QXPICX, None, None, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, QXPICX, None, None, QBMJVH
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, RJHIUS, None, None, QBMJVH
            ),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, QBMJVH),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, None, CBFEGZ, None, None, QBMJVH
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, FEGZUQ, None, EGZUQE, None, None, QBMJVH
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, EGZUQE, None, None, QBMJVH
            ),
            UQEXLS: GeckoByteStructAccessor(self.struct, UQEXLS, QEXLSX, QBMJVH),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, QBMJVH),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UJUTYE, YEKCWA, TYEKCW, None, YEKCWA, QBMJVH
            ),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoEnumStructAccessor(
                self.struct, CWAONP, WAONPY, None, PYYLIU, None, None, QBMJVH
            ),
            YYLIUX: GeckoEnumStructAccessor(
                self.struct, YYLIUX, YLIUXF, None, UXFEFJ, None, None, QBMJVH
            ),
            XFEFJT: GeckoBoolStructAccessor(
                self.struct, XFEFJT, FEFJTA, EFJTAC, QBMJVH
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, FEFJTA, OUYNQJ, POUYNQ, None, YEKCWA, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, FEFJTA, JYMOUN, QJYMOU, None, YEKCWA, QBMJVH
            ),
            YMOUNB: GeckoByteStructAccessor(self.struct, YMOUNB, MOUNBL, QBMJVH),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, QBMJVH),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, QBMJVH),
            JIGYOU: GeckoEnumStructAccessor(
                self.struct, JIGYOU, IGYOUS, None, YOUSPB, None, None, QBMJVH
            ),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, USPBWJ, None, BWJYKL, None, None, QBMJVH
            ),
            WJYKLG: GeckoEnumStructAccessor(
                self.struct, WJYKLG, JYKLGQ, None, YKLGQP, None, None, QBMJVH
            ),
            KLGQPL: GeckoEnumStructAccessor(
                self.struct, KLGQPL, LGQPLS, None, PLSPFT, None, None, QBMJVH
            ),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, QBMJVH),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, POUYNQ, None, None, QBMJVH
            ),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoByteStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoByteStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoTempStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoEnumStructAccessor(
                self.struct, MJMAOA, JMAOAW, YEKCWA, OAWBSI, None, YEKCWA, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, YKLGQP, None, None, QBMJVH
            ),
            BSIRYX: GeckoEnumStructAccessor(
                self.struct, BSIRYX, SIRYXB, XBQFYL, YXBQFY, None, YEKCWA, QBMJVH
            ),
            BQFYLJ: GeckoBoolStructAccessor(
                self.struct, BQFYLJ, QFYLJU, EFJTAC, QBMJVH
            ),
            FYLJUI: GeckoBoolStructAccessor(
                self.struct, FYLJUI, QFYLJU, YLJUIK, QBMJVH
            ),
            LJUIKF: GeckoByteStructAccessor(self.struct, LJUIKF, JUIKFW, QBMJVH),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, SIRYXB, WRKINE, FWRKIN, None, YEKCWA, QBMJVH
            ),
            RKINEJ: GeckoEnumStructAccessor(
                self.struct, RKINEJ, SIRYXB, YEKCWA, NEJNIB, None, YEKCWA, QBMJVH
            ),
            EJNIBX: GeckoByteStructAccessor(self.struct, EJNIBX, JNIBXY, None),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, None),
            BXYBQS: GeckoByteStructAccessor(self.struct, BXYBQS, XYBQSN, None),
            YBQSNQ: GeckoByteStructAccessor(self.struct, YBQSNQ, BQSNQL, QBMJVH),
            QSNQLN: GeckoByteStructAccessor(self.struct, QSNQLN, SNQLNM, QBMJVH),
            NQLNMH: GeckoByteStructAccessor(self.struct, NQLNMH, QLNMHX, QBMJVH),
            LNMHXE: GeckoByteStructAccessor(self.struct, LNMHXE, NMHXEK, QBMJVH),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoBoolStructAccessor(
                self.struct, XEKVKZ, EKVKZI, OUYNQJ, QBMJVH
            ),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, EKVKZI, WRKINE, ILXWAJ, None, EFJTAC, QBMJVH
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, EKVKZI, JYMOUN, AJVDQL, None, YEKCWA, QBMJVH
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, JMAOAW, XBQFYL, LAIIDN, None, EFJTAC, QBMJVH
            ),
            AIIDNI: GeckoBoolStructAccessor(
                self.struct, AIIDNI, JMAOAW, YLJUIK, QBMJVH
            ),
            IIDNIB: GeckoBoolStructAccessor(
                self.struct, IIDNIB, JMAOAW, OUYNQJ, QBMJVH
            ),
            IDNIBX: GeckoBoolStructAccessor(
                self.struct, IDNIBX, JMAOAW, DNIBXT, QBMJVH
            ),
            NIBXTI: GeckoEnumStructAccessor(
                self.struct, NIBXTI, QFYLJU, WRKINE, YOUSPB, None, EFJTAC, QBMJVH
            ),
            IBXTIA: GeckoBoolStructAccessor(
                self.struct, IBXTIA, QFYLJU, XBQFYL, QBMJVH
            ),
            BXTIAC: GeckoByteStructAccessor(self.struct, BXTIAC, XTIACQ, QBMJVH),
            TIACQF: GeckoByteStructAccessor(self.struct, TIACQF, IACQFF, QBMJVH),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, QBMJVH),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, QBMJVH),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, QBMJVH),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoBoolStructAccessor(
                self.struct, DUBSSU, UBSSUH, JYMOUN, QBMJVH
            ),
            BSSUHB: GeckoBoolStructAccessor(
                self.struct, BSSUHB, UBSSUH, YEKCWA, QBMJVH
            ),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, QBMJVH),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, QBMJVH),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, QBMJVH),
            UBYGDS: GeckoByteStructAccessor(self.struct, UBYGDS, BYGDSB, QBMJVH),
            YGDSBD: GeckoByteStructAccessor(self.struct, YGDSBD, GDSBDJ, QBMJVH),
            DSBDJQ: GeckoByteStructAccessor(self.struct, DSBDJQ, SBDJQR, QBMJVH),
            BDJQRJ: GeckoTimeStructAccessor(self.struct, BDJQRJ, DJQRJJ, QBMJVH),
            JQRJJJ: GeckoTimeStructAccessor(self.struct, JQRJJJ, QRJJJV, QBMJVH),
            RJJJVY: GeckoTimeStructAccessor(self.struct, RJJJVY, JJJVYF, QBMJVH),
            JJVYFC: GeckoTimeStructAccessor(self.struct, JJVYFC, JVYFCR, QBMJVH),
            VYFCRT: GeckoByteStructAccessor(self.struct, VYFCRT, YFCRTF, QBMJVH),
            FCRTFM: GeckoTimeStructAccessor(self.struct, FCRTFM, CRTFMN, QBMJVH),
            RTFMNH: GeckoTimeStructAccessor(self.struct, RTFMNH, TFMNHT, QBMJVH),
            FMNHTB: GeckoEnumStructAccessor(
                self.struct, FMNHTB, EKVKZI, EFJTAC, NHTBJE, None, YEKCWA, QBMJVH
            ),
            HTBJEU: GeckoBoolStructAccessor(
                self.struct, HTBJEU, EKVKZI, YLJUIK, QBMJVH
            ),
            TBJEUT: GeckoBoolStructAccessor(
                self.struct, TBJEUT, EKVKZI, XBQFYL, QBMJVH
            ),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, UJUTYE, JYMOUN, UTOPHU, None, YEKCWA, QBMJVH
            ),
            TOPHUG: GeckoBoolStructAccessor(
                self.struct, TOPHUG, UJUTYE, WRKINE, QBMJVH
            ),
            XCHWDA: GeckoEnumStructAccessor(
                self.struct, XCHWDA, SIRYXB, JYMOUN, WDAFIK, None, YEKCWA, QBMJVH
            ),
            DAFIKJ: GeckoBoolStructAccessor(
                self.struct, DAFIKJ, QFYLJU, JYMOUN, QBMJVH
            ),
            AFIKJP: GeckoBoolStructAccessor(
                self.struct, AFIKJP, FEFJTA, WRKINE, QBMJVH
            ),
        }

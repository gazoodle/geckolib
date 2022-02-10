#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v1'
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
ACCPQI = "".join(chr(c) for c in [70, 105, 108, 116, 77, 105, 110, 68, 117, 114])
ACQFFT = "".join(
    chr(c) for c in [70, 97, 110, 84, 101, 109, 112, 79, 112, 116, 105, 111, 110]
)
AIIDNI = "".join(
    chr(c)
    for c in [
        69,
        120,
        105,
        116,
        81,
        117,
        105,
        101,
        116,
        65,
        110,
        100,
        67,
        97,
        110,
        99,
        101,
        108,
        79,
        116,
        104,
        101,
        114,
        85,
        68,
    ]
)
AJVDQL = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
AKQXPI = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
AMJMAO = 78
AOAWBS = 80
AONPYY = "".join(chr(c) for c in [65, 110, 121, 85, 68])
ASSAKQ = "".join(chr(c) for c in [70, 98, 77, 116, 114])
AWBSIR = 81
BDJQRJ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
BFEGZU = "".join(
    chr(c)
    for c in [
        80,
        117,
        109,
        112,
        82,
        101,
        115,
        101,
        116,
        84,
        105,
        109,
        101,
        79,
        117,
        116,
    ]
)
BIAMJM = 7
BLKXSJ = "".join(chr(c) for c in [78, 79, 78, 69])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = 85
BSIRYX = 82
BSKSOK = "".join(chr(c) for c in [79, 117, 116, 52, 65])
BSSUHB = 31
BVWVUB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
BWJYKL = 40
BXTIAC = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
BXYBQS = "".join(
    chr(c)
    for c in [
        67,
        69,
        95,
        74,
        109,
        112,
        49,
        95,
        52,
        95,
        73,
        110,
        115,
        116,
        97,
        108,
        108,
        101,
        100,
    ]
)
CBFEGZ = 1
CCPQIP = 60
CPQIPO = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
CQBMJV = 1
CQFFTT = "".join(
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
CTHBSK = "".join(chr(c) for c in [68, 101, 115, 99, 101, 110, 100, 97, 110, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 79, 112, 116, 105, 111, 110]
)
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 49, 66])
DJQRJJ = 24
DNIBXT = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
DQLAII = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
DSBDJQ = "".join(chr(c) for c in [70])
DUBSSU = 30
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        68,
        101,
        102,
        80,
        117,
        114,
        103,
        101,
        84,
        105,
        109,
        101,
    ]
)
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 50, 66])
EGZUQE = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116, 83, 104, 97, 114, 101]
)
EKCWAO = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
EKVKZI = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
EOCTHB = 18
EXLSXU = 38
FCRTFM = "".join(
    chr(c)
    for c in [
        75,
        105,
        110,
        101,
        116,
        105,
        99,
        80,
        114,
        111,
        116,
        101,
        99,
        116,
        105,
        111,
        110,
    ]
)
FEGZUQ = 3
FFTTID = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        83,
        101,
        116,
        65,
        79,
        84,
        84,
        101,
        109,
        112,
        65,
        100,
        99,
        49,
        54,
    ]
)
FJTACC = 56
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
FTTIDU = 26
FWRKIN = "".join(chr(c) for c in [54, 48, 72, 90])
FXQGLR = 203
FYLJUI = 70
GDSBDJ = "".join(chr(c) for c in [67])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 72, 101, 97, 116, 101, 114])
GQPLSP = 76
GYOUSP = 68
GZUQEX = 4
HBSKSO = 2
HBVWVU = 35
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(
    chr(c)
    for c in [
        80,
        117,
        109,
        112,
        65,
        99,
        116,
        105,
        118,
        97,
        116,
        105,
        111,
        110,
        79,
        114,
        100,
        101,
        114,
    ]
)
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(
    chr(c)
    for c in [
        76,
        105,
        103,
        104,
        116,
        65,
        99,
        116,
        105,
        118,
        97,
        116,
        105,
        111,
        110,
        79,
        114,
        100,
        101,
        114,
    ]
)
HUOJRJ = 208
HXEKVK = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
IAMJMA = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
IBXYBQ = "".join(
    chr(c)
    for c in [
        67,
        69,
        95,
        74,
        109,
        112,
        49,
        95,
        51,
        95,
        73,
        110,
        115,
        116,
        97,
        108,
        108,
        101,
        100,
    ]
)
IDNIBX = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
IDUBSS = "".join(
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
IEFXQG = 202
IFJBIA = "".join(chr(c) for c in [65, 110, 121, 70, 114, 101, 101, 80, 117, 109, 112])
IGYOUS = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
IKFWRK = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
ILXWAJ = 94
INEJNI = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 59
IRYXBQ = 83
IUSOOQ = 0
IUXFEF = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(
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
JHIUSO = 87
JIGYOU = 67
JJJVYF = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
JJVYFC = "".join(chr(c) for c in [65, 109, 80, 109])
JMAOAW = 79
JMCBFE = "".join(chr(c) for c in [79, 110, 67, 104, 97, 110, 103, 101])
JNIBXY = "".join(chr(c) for c in [70, 117, 115, 101, 77, 97, 112, 112, 105, 110, 103])
JQRJJJ = "".join(
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
JTACCP = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        68,
        101,
        102,
        80,
        49,
        80,
        117,
        114,
        103,
        101,
        84,
        105,
        109,
        101,
    ]
)
JUTYEK = "".join(chr(c) for c in [67, 108, 101, 97, 110, 80, 49])
JVDQLA = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [50, 52, 104])
JWMNZM = "".join(chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 105, 110, 103])
JYKLGQ = 42
JYMOUN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 77, 105, 110, 79, 110, 84, 105, 109, 101]
)
KCWAON = 37
KFWRKI = 86
KINEJN = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
KLGQPL = 74
KPHUOJ = 207
KQXPIC = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 53, 65])
KVKZIL = 92
KZILXW = 93
LAIIDN = "".join(
    chr(c)
    for c in [
        69,
        120,
        105,
        116,
        81,
        117,
        105,
        101,
        116,
        65,
        110,
        100,
        82,
        101,
        115,
        116,
        111,
        114,
        101,
        65,
        108,
        108,
        85,
        68,
    ]
)
LASSAK = "".join(chr(c) for c in [70, 65, 78])
LGQPLS = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
LJUIKF = "".join(chr(c) for c in [72, 105, 103, 104])
LKXSJW = "".join(chr(c) for c in [80, 49])
LNMHXE = 89
LRAHEO = 209
LSPFTS = "".join(
    chr(c) for c in [69, 99, 111, 110, 80, 114, 111, 103, 69, 110, 97, 98, 108, 101]
)
LSXUJU = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 49])
LXWAJV = "".join(
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
MAOAWB = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
MHXEKV = 90
MJIGYO = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
MJMAOA = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
MJVHFT = 200
MNZMJI = 5
MOUNBL = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 77, 97, 120, 68, 117, 114]
)
NBLKXS = 66
NEJNIB = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
NIBXTI = "".join(chr(c) for c in [80, 97, 117, 115, 101])
NIBXYB = "".join(chr(c) for c in [85, 76])
NMHXEK = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
NQJYMO = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
NQLNMH = 88
NRSJMC = 21
NZMJIG = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
OAWBSI = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
OCTHBS = "".join(chr(c) for c in [65, 115, 99, 101, 110, 100, 97, 110, 116])
OJRJHI = 210
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 54, 65])
ONPYYL = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
OOQNRS = "".join(
    chr(c) for c in [70, 105, 98, 101, 114, 84, 105, 109, 101, 79, 117, 116]
)
OQNRSJ = 20
OUNBLK = 64
OUSPBW = 69
OUYNQJ = 65
PBWJYK = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
PFTSIF = "".join(
    chr(c) for c in [69, 99, 111, 110, 80, 114, 111, 103, 77, 111, 100, 101]
)
PHUOJR = "".join(chr(c) for c in [79, 117, 116, 55, 65])
PICXQI = "".join(chr(c) for c in [86, 65, 76, 86, 69])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 71
POUYNQ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
PQIPOU = 58
PYYLIU = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        67,
        80,
        79,
        84,
        76,
        105,
        109,
        105,
        116,
        79,
        112,
        116,
        105,
        111,
        110,
    ]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
QFFTTI = "".join(
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
QFYLJU = "".join(
    chr(c) for c in [83, 87, 77, 80, 117, 114, 103, 101, 83, 112, 101, 101, 100]
)
QGLRAH = 204
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 65])
QIPOUY = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
QJYMOU = 62
QLAIID = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
QLNMHX = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
QNRSJM = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
QPLSPF = "".join(
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
QRJJJV = 73
QSNQLN = 8
QXPICX = "".join(chr(c) for c in [83, 65, 78, 73])
RAHEOC = "".join(chr(c) for c in [])
RJHIUS = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
RJJJVY = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 84, 69, 110, 97, 98, 108, 101]
)
RSJMCB = "".join(
    chr(c)
    for c in [
        76,
        105,
        103,
        104,
        116,
        82,
        101,
        115,
        101,
        116,
        84,
        105,
        109,
        101,
        79,
        117,
        116,
    ]
)
RYXBQF = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
SAKQXP = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SIFJBI = "".join(
    chr(c)
    for c in [78, 101, 120, 116, 70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121]
)
SIRYXB = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
SJMCBF = "".join(chr(c) for c in [79, 110, 83, 116, 97, 114, 116])
SJWMNZ = "".join(
    chr(c) for c in [79, 51, 68, 117, 114, 105, 110, 103, 70, 105, 108, 116]
)
SKSOKP = 205
SNQLNM = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
SOKPHU = 206
SOOQNR = 19
SPBWJY = 39
SPFTSI = "".join(
    chr(c) for c in [69, 99, 111, 110, 85, 115, 101, 114, 68, 101, 109, 97, 110, 100]
)
SSAKQX = "".join(chr(c) for c in [70, 98, 76, 105])
SSUHBV = "".join(
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
        49,
        54,
    ]
)
SUHBVW = 33
SXUJUT = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 50])
TACCPQ = 57
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(chr(c) for c in [78, 111, 110, 101])
TIDUBS = 28
TSIFJB = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
TTIDUB = "".join(
    chr(c)
    for c in [
        70,
        97,
        110,
        67,
        108,
        114,
        65,
        79,
        84,
        84,
        101,
        109,
        112,
        65,
        100,
        99,
        49,
        54,
    ]
)
TYEKCW = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 80])
UBSSUH = "".join(
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
        49,
        54,
    ]
)
UBYGDS = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
UHBVWV = "".join(
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
UIKFWR = "".join(
    chr(c) for c in [83, 87, 77, 80, 117, 114, 103, 101, 66, 108, 111, 119, 101, 114]
)
UNBLKX = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
UOJRJH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
UQEXLS = 72
USOOQN = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
USPBWJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
UTYEKC = 36
UXFEFJ = "".join(chr(c) for c in [76, 111])
UYNQJY = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
VLASSA = "".join(chr(c) for c in [76, 73])
VUBYGD = "".join(chr(c) for c in [78, 111])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
WAONPY = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
WBSIRY = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
WJYKLG = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
WMNZMJ = "".join(
    chr(c) for c in [79, 51, 85, 115, 101, 114, 68, 101, 109, 97, 110, 100]
)
WRKINE = "".join(chr(c) for c in [53, 48, 72, 90])
WVUBYG = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
XBQFYL = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
XEKVKZ = 91
XFEFJT = "".join(chr(c) for c in [72, 105])
XLSXUJ = "".join(chr(c) for c in [83, 116, 97, 114, 116, 68, 117, 114, 70, 114, 101])
XPICXQ = "".join(chr(c) for c in [79, 78, 90, 69, 78])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 51, 65])
XQIEFX = 201
XSJWMN = "".join(chr(c) for c in [79, 51, 65, 108, 119, 97, 121, 115, 79, 78])
XTIACQ = 23
XUJUTY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
XWAJVD = 22
XYBQSN = "".join(
    chr(c)
    for c in [
        67,
        69,
        95,
        74,
        109,
        112,
        50,
        95,
        51,
        95,
        73,
        110,
        115,
        116,
        97,
        108,
        108,
        101,
        100,
    ]
)
YBQSNQ = "".join(
    chr(c)
    for c in [
        67,
        69,
        95,
        74,
        109,
        112,
        50,
        95,
        52,
        95,
        73,
        110,
        115,
        116,
        97,
        108,
        108,
        101,
        100,
    ]
)
YEKCWA = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
YFCRTF = "".join(
    chr(c)
    for c in [
        73,
        110,
        83,
        116,
        97,
        116,
        101,
        85,
        115,
        101,
        114,
        68,
        101,
        109,
        97,
        110,
        100,
    ]
)
YGDSBD = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
YKLGQP = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
YLIUXF = "".join(
    chr(c)
    for c in [
        76,
        105,
        109,
        105,
        116,
        101,
        100,
        73,
        102,
        83,
        80,
        66,
        101,
        108,
        111,
        119,
        57,
        53,
        70,
    ]
)
YLJUIK = "".join(chr(c) for c in [76, 111, 119])
YMOUNB = 63
YNQJYM = 61
YOUSPB = "".join(
    chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 101, 80, 101, 114, 105, 111, 100]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = 84
YYLIUX = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
ZMJIGY = 6
ZUQEXL = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
AHEOCT = [
    JVHFTH,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    IVLASS,
]
BQSNQL = [NIBXYB, IBXYBQ, BXYBQS, XYBQSN, YBQSNQ, RAHEOC, RAHEOC, RAHEOC]
BYGDSB = [VUBYGD, UBYGDS]
CRTFMN = [
    BMJVHF,
    CXQIEF,
    QIEFXQ,
    EFXQGL,
    XQGLRA,
    GLRAHE,
    HEOCTH,
    BSKSOK,
    KSOKPH,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    HIUSOO,
]
EJNIBX = [INEJNI, NEJNIB]
FEFJTA = [UXFEFJ, XFEFJT]
FJBIAM = [TSIFJB, SIFJBI, IFJBIA]
IACQFF = [TIACQF, LKXSJW, PIPIVL]
IBXTIA = [DNIBXT, NIBXTI]
ICXQIE = [
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
    ASSAKQ,
    SSAKQX,
    SAKQXP,
    AKQXPI,
    KQXPIC,
    QXPICX,
    XPICXQ,
    PICXQI,
]
IIDNIB = [QLAIID, LAIIDN, JVHFTH, AIIDNI]
JRJHIU = [
    JVHFTH,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    RAHEOC,
    VLASSA,
]
JUIKFW = [YLJUIK, LJUIKF]
KXSJWM = [BLKXSJ, LKXSJW, PIPIVL, RAHEOC]
LIUXFE = [YYLIUX, YLIUXF]
MCBFEG = [SJMCBF, JMCBFE]
NPYYLI = [AONPYY, ONPYYL]
RKINEJ = [FWRKIN, WRKINE]
RTFMNH = [VLASSA]
SBDJQR = [GDSBDJ, DSBDJQ]
TFMNHT = []
THBSKS = [OCTHBS, CTHBSK]
UJUTYE = [XLSXUJ, LSXUJU, SXUJUT, XUJUTY]
VDQLAI = [WAJVDQ, AJVDQL, JVDQLA, RAHEOC]
VWVUBY = [RAHEOC, PIPIVL, LKXSJW]
VYFCRT = [JJVYFC, JVYFCR]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return CBFEGZ

    @property
    def output_keys(self):
        return CRTFMN

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, ICXQIE, None, None, QBMJVH
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, ICXQIE, None, None, QBMJVH
            ),
            QIEFXQ: GeckoEnumStructAccessor(
                self.struct, QIEFXQ, IEFXQG, None, ICXQIE, None, None, QBMJVH
            ),
            EFXQGL: GeckoEnumStructAccessor(
                self.struct, EFXQGL, FXQGLR, None, ICXQIE, None, None, QBMJVH
            ),
            XQGLRA: GeckoEnumStructAccessor(
                self.struct, XQGLRA, QGLRAH, None, ICXQIE, None, None, QBMJVH
            ),
            GLRAHE: GeckoEnumStructAccessor(
                self.struct, GLRAHE, LRAHEO, None, AHEOCT, None, None, QBMJVH
            ),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, EOCTHB, HBSKSO, THBSKS, None, HBSKSO, QBMJVH
            ),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, SKSOKP, None, ICXQIE, None, None, QBMJVH
            ),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, ICXQIE, None, None, QBMJVH
            ),
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, ICXQIE, None, None, QBMJVH
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, None, ICXQIE, None, None, QBMJVH
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, JRJHIU, None, None, QBMJVH
            ),
            RJHIUS: GeckoByteStructAccessor(self.struct, RJHIUS, JHIUSO, QBMJVH),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, EOCTHB, IUSOOQ, THBSKS, None, HBSKSO, QBMJVH
            ),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, QBMJVH),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, EOCTHB, CBFEGZ, MCBFEG, None, HBSKSO, QBMJVH
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, EOCTHB, FEGZUQ, MCBFEG, None, HBSKSO, QBMJVH
            ),
            EGZUQE: GeckoBoolStructAccessor(
                self.struct, EGZUQE, EOCTHB, GZUQEX, QBMJVH
            ),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QBMJVH),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, EXLSXU, None, UJUTYE, None, None, QBMJVH
            ),
            JUTYEK: GeckoBoolStructAccessor(
                self.struct, JUTYEK, UTYEKC, CBFEGZ, QBMJVH
            ),
            TYEKCW: GeckoBoolStructAccessor(
                self.struct, TYEKCW, UTYEKC, HBSKSO, QBMJVH
            ),
            YEKCWA: GeckoBoolStructAccessor(
                self.struct, YEKCWA, UTYEKC, FEGZUQ, QBMJVH
            ),
            EKCWAO: GeckoBoolStructAccessor(
                self.struct, EKCWAO, KCWAON, IUSOOQ, QBMJVH
            ),
            CWAONP: GeckoBoolStructAccessor(
                self.struct, CWAONP, KCWAON, CBFEGZ, QBMJVH
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, KCWAON, HBSKSO, NPYYLI, None, HBSKSO, QBMJVH
            ),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, KCWAON, FEGZUQ, LIUXFE, None, HBSKSO, QBMJVH
            ),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, UTYEKC, IUSOOQ, FEFJTA, None, HBSKSO, QBMJVH
            ),
            EFJTAC: GeckoByteStructAccessor(self.struct, EFJTAC, FJTACC, QBMJVH),
            JTACCP: GeckoByteStructAccessor(self.struct, JTACCP, TACCPQ, QBMJVH),
            ACCPQI: GeckoByteStructAccessor(self.struct, ACCPQI, CCPQIP, QBMJVH),
            CPQIPO: GeckoByteStructAccessor(self.struct, CPQIPO, PQIPOU, QBMJVH),
            QIPOUY: GeckoByteStructAccessor(self.struct, QIPOUY, IPOUYN, QBMJVH),
            POUYNQ: GeckoByteStructAccessor(self.struct, POUYNQ, OUYNQJ, QBMJVH),
            UYNQJY: GeckoByteStructAccessor(self.struct, UYNQJY, YNQJYM, QBMJVH),
            NQJYMO: GeckoByteStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoByteStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, NBLKXS, IUSOOQ, KXSJWM, None, GZUQEX, QBMJVH
            ),
            XSJWMN: GeckoBoolStructAccessor(
                self.struct, XSJWMN, NBLKXS, HBSKSO, QBMJVH
            ),
            SJWMNZ: GeckoBoolStructAccessor(
                self.struct, SJWMNZ, NBLKXS, FEGZUQ, QBMJVH
            ),
            JWMNZM: GeckoBoolStructAccessor(
                self.struct, JWMNZM, NBLKXS, GZUQEX, QBMJVH
            ),
            WMNZMJ: GeckoBoolStructAccessor(
                self.struct, WMNZMJ, NBLKXS, MNZMJI, QBMJVH
            ),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, NBLKXS, ZMJIGY, NPYYLI, None, None, QBMJVH
            ),
            MJIGYO: GeckoByteStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoByteStructAccessor(self.struct, IGYOUS, GYOUSP, QBMJVH),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoByteStructAccessor(self.struct, USPBWJ, SPBWJY, QBMJVH),
            PBWJYK: GeckoTimeStructAccessor(self.struct, PBWJYK, BWJYKL, QBMJVH),
            WJYKLG: GeckoTimeStructAccessor(self.struct, WJYKLG, JYKLGQ, QBMJVH),
            YKLGQP: GeckoTimeStructAccessor(self.struct, YKLGQP, KLGQPL, QBMJVH),
            LGQPLS: GeckoTimeStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoBoolStructAccessor(
                self.struct, QPLSPF, PLSPFT, FEGZUQ, QBMJVH
            ),
            LSPFTS: GeckoBoolStructAccessor(
                self.struct, LSPFTS, PLSPFT, GZUQEX, QBMJVH
            ),
            SPFTSI: GeckoBoolStructAccessor(
                self.struct, SPFTSI, PLSPFT, MNZMJI, QBMJVH
            ),
            PFTSIF: GeckoBoolStructAccessor(
                self.struct, PFTSIF, PLSPFT, ZMJIGY, QBMJVH
            ),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, EOCTHB, MNZMJI, FJBIAM, None, GZUQEX, QBMJVH
            ),
            JBIAMJ: GeckoBoolStructAccessor(
                self.struct, JBIAMJ, EOCTHB, BIAMJM, QBMJVH
            ),
            QFYLJU: GeckoEnumStructAccessor(
                self.struct, QFYLJU, FYLJUI, IUSOOQ, JUIKFW, None, HBSKSO, QBMJVH
            ),
            UIKFWR: GeckoBoolStructAccessor(
                self.struct, UIKFWR, FYLJUI, CBFEGZ, QBMJVH
            ),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, GZUQEX, RKINEJ, None, HBSKSO, QBMJVH
            ),
            KINEJN: GeckoEnumStructAccessor(
                self.struct, KINEJN, KFWRKI, MNZMJI, EJNIBX, None, HBSKSO, QBMJVH
            ),
            JNIBXY: GeckoEnumStructAccessor(
                self.struct, JNIBXY, KFWRKI, CBFEGZ, BQSNQL, None, QSNQLN, QBMJVH
            ),
            SNQLNM: GeckoByteStructAccessor(self.struct, SNQLNM, NQLNMH, None),
            QLNMHX: GeckoByteStructAccessor(self.struct, QLNMHX, LNMHXE, None),
            NMHXEK: GeckoByteStructAccessor(self.struct, NMHXEK, MHXEKV, QBMJVH),
            HXEKVK: GeckoByteStructAccessor(self.struct, HXEKVK, XEKVKZ, QBMJVH),
            EKVKZI: GeckoByteStructAccessor(self.struct, EKVKZI, KVKZIL, QBMJVH),
            VKZILX: GeckoByteStructAccessor(self.struct, VKZILX, KZILXW, QBMJVH),
            ZILXWA: GeckoByteStructAccessor(self.struct, ZILXWA, ILXWAJ, QBMJVH),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XWAJVD, GZUQEX, VDQLAI, None, GZUQEX, QBMJVH
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, PLSPFT, CBFEGZ, IIDNIB, None, GZUQEX, QBMJVH
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, PLSPFT, IUSOOQ, IBXTIA, None, HBSKSO, QBMJVH
            ),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, XTIACQ, FEGZUQ, IACQFF, None, GZUQEX, QBMJVH
            ),
            ACQFFT: GeckoBoolStructAccessor(
                self.struct, ACQFFT, XWAJVD, ZMJIGY, QBMJVH
            ),
            CQFFTT: GeckoBoolStructAccessor(
                self.struct, CQFFTT, XWAJVD, BIAMJM, QBMJVH
            ),
            QFFTTI: GeckoBoolStructAccessor(
                self.struct, QFFTTI, XTIACQ, IUSOOQ, QBMJVH
            ),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, QBMJVH),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, QBMJVH),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, QBMJVH),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, QBMJVH),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, QBMJVH),
            BVWVUB: GeckoEnumStructAccessor(
                self.struct, BVWVUB, XWAJVD, None, VWVUBY, None, GZUQEX, QBMJVH
            ),
            WVUBYG: GeckoEnumStructAccessor(
                self.struct, WVUBYG, KFWRKI, ZMJIGY, BYGDSB, None, HBSKSO, QBMJVH
            ),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, XWAJVD, HBSKSO, SBDJQR, None, HBSKSO, QBMJVH
            ),
            BDJQRJ: GeckoTempStructAccessor(self.struct, BDJQRJ, DJQRJJ, QBMJVH),
            JQRJJJ: GeckoByteStructAccessor(self.struct, JQRJJJ, QRJJJV, QBMJVH),
            RJJJVY: GeckoBoolStructAccessor(
                self.struct, RJJJVY, XTIACQ, CBFEGZ, QBMJVH
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, KFWRKI, IUSOOQ, VYFCRT, None, HBSKSO, QBMJVH
            ),
            YFCRTF: GeckoBoolStructAccessor(
                self.struct, YFCRTF, XWAJVD, FEGZUQ, QBMJVH
            ),
            FCRTFM: GeckoBoolStructAccessor(
                self.struct, FCRTFM, XTIACQ, HBSKSO, QBMJVH
            ),
        }

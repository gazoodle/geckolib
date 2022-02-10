#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v3'
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
ACCPQI = 5
ACQFFT = 99
AFIKJP = "".join(chr(c) for c in [65, 109, 80, 109])
AJVDQL = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
AKQXPI = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
AMJMAO = 55
AOAWBS = 77
AONPYY = 41
ASSAKQ = "".join(chr(c) for c in [70, 98, 77, 116, 114])
AWBSIR = 72
BDJQRJ = 30
BFEGZU = 211
BIAMJM = 53
BJEUTO = "".join(
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
BLKXSJ = 62
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
BQSNQL = 84
BSIRYX = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
BSKSOK = "".join(
    chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114, 114, 101, 110, 116]
)
BSSUHB = 104
BVWVUB = "".join(
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
BWJYKL = 68
BXTIAC = 97
BXYBQS = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53])
BYGDSB = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 77, 101, 110, 117])
CBFEGZ = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
CCPQIP = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
CHWDAF = "".join(chr(c) for c in [67, 80, 80, 87, 77, 68, 101, 102, 97, 117, 108, 116])
CPQIPO = "".join(chr(c) for c in [65, 110, 121, 85, 68])
CQBMJV = 1
CQFFTT = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
CRTFMN = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
CTHBSK = 221
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 73
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 49, 66])
DAFIKJ = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
DJQRJJ = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
DNIBXT = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
DNQGVU = "".join(
    chr(c) for c in [86, 83, 80, 70, 105, 108, 116, 101, 114, 83, 112, 101, 101, 100]
)
DQLAII = 95
DUBSSU = 103
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 4
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 50, 66])
EGZUQE = 212
EJNIBX = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51])
EKCWAO = 2
EKVKZI = 89
ELHBQN = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
EOCTHB = 220
EUTOPH = "".join(
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
EXLSXU = "".join(
    chr(c) for c in [70, 105, 98, 101, 114, 84, 105, 109, 101, 79, 117, 116]
)
FCRTFM = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
FEFJTA = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
FEGZUQ = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
FFTTID = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
FIKJPU = "".join(chr(c) for c in [50, 52, 104])
FJBIAM = 51
FJTACC = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
FMNHTB = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 43
FTTIDU = 101
FWRKIN = "".join(chr(c) for c in [67, 104, 97, 110, 103, 101, 87, 97, 116, 101, 114])
FXQGLR = 203
GDSBDJ = "".join(
    chr(c) for c in [78, 111, 116, 65, 118, 97, 105, 108, 97, 98, 108, 101]
)
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 72, 101, 97, 116, 101, 114])
GQPLSP = 59
GSELHB = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
GTYIYW = "".join(
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
GVUNXN = 26
GZUQEX = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
HBQNRX = "".join(chr(c) for c in [70])
HBSKSO = 222
HBVWVU = "".join(
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
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(
    chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114, 114, 101, 110, 116]
)
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 225
HUGTYI = "".join(
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
HUOJRJ = 206
HWDAFI = 22
HXEKVK = 88
IACQFF = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
IAMJMA = "".join(chr(c) for c in [79, 110, 122, 101, 110, 70, 114, 101, 113])
IBXTIA = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
IBXYBQ = 82
IDNIBX = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
IDUBSS = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
IEFXQG = 202
IFJBIA = "".join(chr(c) for c in [79, 110, 122, 101, 110, 83, 116, 97, 114, 116])
IGYOUS = "".join(chr(c) for c in [80, 49])
IIDNIB = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
IJUGSE = "".join(chr(c) for c in [78, 111])
IKFWRK = "".join(chr(c) for c in [80, 72])
ILXWAJ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
INEJNI = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
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
IRYXBQ = "".join(chr(c) for c in [65, 99, 116, 105, 118, 101])
IUSOOQ = "".join(
    chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114, 114, 101, 110, 116]
)
IUXFEF = 40
IVDNQG = "".join(
    chr(c)
    for c in [86, 83, 80, 67, 104, 101, 99, 107, 102, 108, 111, 83, 112, 101, 101, 100]
)
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = 38
JBIAMJ = "".join(chr(c) for c in [79, 110, 122, 101, 110, 68, 117, 114])
JEUTOP = "".join(
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
JHIUSO = "".join(
    chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114, 114, 101, 110, 116]
)
JIGYOU = "".join(chr(c) for c in [78, 79, 78, 69])
JJJVYF = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
JJVYFC = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
JMAOAW = 75
JMCBFE = 210
JNIBXY = 81
JPUNRJ = "".join(
    chr(c)
    for c in [
        65,
        117,
        120,
        50,
        65,
        115,
        83,
        112,
        101,
        97,
        107,
        101,
        114,
        76,
        105,
        102,
        116,
        101,
        114,
    ]
)
JQRJJJ = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
JRJHIU = "".join(chr(c) for c in [79, 117, 116, 55, 65])
JTACCP = 3
JUGSEL = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
JUIKFW = 79
JUTYEK = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
JVDQLA = 94
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(
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
JWMNZM = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 77, 97, 120, 68, 117, 114]
)
JYKLGQ = 69
JYMOUN = "".join(chr(c) for c in [72, 105])
JZTATD = "".join(chr(c) for c in [79, 110, 80, 51])
KCWAON = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
KFWRKI = "".join(chr(c) for c in [67, 104, 101, 99, 107, 71, 70, 67, 73])
KJPUNR = "".join(
    chr(c) for c in [65, 117, 120, 49, 65, 115, 84, 86, 76, 105, 102, 116, 101, 114]
)
KLGQPL = 70
KMLOIJ = 29
KPHUOJ = 205
KQXPIC = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
KSOKPH = "".join(
    chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114, 114, 101, 110, 116]
)
KVKZIL = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
KWIVDN = 23
KXSJWM = 63
KZILXW = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
LAIIDN = "".join(chr(c) for c in [53, 48, 72, 90])
LASSAK = "".join(chr(c) for c in [70, 65, 78])
LGQPLS = "".join(chr(c) for c in [83, 97, 110, 105, 76, 101, 118, 101, 108])
LHBQNR = "".join(chr(c) for c in [67])
LIUXFE = "".join(chr(c) for c in [67, 108, 101, 97, 110, 80, 49])
LJUIKF = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49])
LKXSJW = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
LNMHXE = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
LRAHEO = 209
LSPFTS = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
LSXUJU = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
LXWAJV = 92
MAOAWB = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
MHXEKV = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
MJIGYO = 67
MJMAOA = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
MJVHFT = 200
MLOIJU = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
MNHTBJ = 31
MNZMJI = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
MOUNBL = 0
NBLKXS = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
NEJNIB = 80
NHTBJE = "".join(chr(c) for c in [78, 111, 110, 101])
NIBXYB = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52])
NKMLOI = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 51]
)
NMHXEK = 87
NPYYLI = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 49])
NQGVUN = 25
NQJYMO = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
NQLNMH = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56])
NRJZTA = "".join(chr(c) for c in [79, 110, 80, 49])
NRSJMC = "".join(
    chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114, 114, 101, 110, 116]
)
NRXCHW = 32
NXNKML = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 50]
)
NZMJIG = 66
OAWBSI = "".join(
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
OCTHBS = "".join(
    chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114, 114, 101, 110, 116]
)
OIJUGS = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
OJRJHI = 207
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 52, 65])
ONPYYL = "".join(chr(c) for c in [83, 116, 97, 114, 116, 68, 117, 114, 70, 114, 101])
OOQNRS = 227
OPHUGT = "".join(
    chr(c)
    for c in [70, 97, 110, 67, 108, 114, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
OQNRSJ = "".join(
    chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114, 114, 101, 110, 116]
)
OUNBLK = "".join(chr(c) for c in [70, 105, 108, 116, 77, 105, 110, 68, 117, 114])
OUSPBW = "".join(
    chr(c) for c in [79, 51, 68, 117, 114, 105, 110, 103, 70, 105, 108, 116]
)
OUYNQJ = "".join(
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
PBWJYK = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
PFTSIF = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
PHUGTY = 35
PHUOJR = "".join(chr(c) for c in [79, 117, 116, 53, 65])
PICXQI = "".join(chr(c) for c in [86, 65, 76, 86, 69])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 60
POUYNQ = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
PQIPOU = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
PUNRJZ = "".join(chr(c) for c in [65, 117, 120, 50, 65, 115, 79, 110, 122, 101, 110])
PYYLIU = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 50])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 18
QFFTTI = 100
QFYLJU = "".join(
    chr(c)
    for c in [78, 101, 120, 116, 70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121]
)
QGLRAH = 204
QGVUNX = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 48]
)
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 65])
QJYMOU = "".join(chr(c) for c in [76, 111])
QLAIID = "".join(chr(c) for c in [54, 48, 72, 90])
QLNMHX = 86
QNRSJM = 228
QNRXCH = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
QPLSPF = "".join(chr(c) for c in [83, 97, 110, 105, 79, 110, 84, 105, 109, 101])
QRJJJV = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
QSNQLN = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55])
QXPICX = "".join(chr(c) for c in [83, 65, 78, 73])
RAHEOC = "".join(chr(c) for c in [])
RJHIUS = 208
RJZTAT = "".join(chr(c) for c in [79, 110, 80, 50])
RKINEJ = "".join(
    chr(c) for c in [82, 101, 112, 108, 97, 99, 101, 70, 105, 108, 116, 101, 114]
)
RSJMCB = 123
RTFMNH = "".join(chr(c) for c in [80, 97, 117, 115, 101])
RXCHWD = "".join(
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
SAKQXP = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SBDJQR = "".join(
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
SELHBQ = "".join(
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
SIFJBI = 45
SIRYXB = "".join(chr(c) for c in [78, 111, 116, 65, 99, 116, 105, 118, 101])
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 76, 105])
SJWMNZ = 64
SKSOKP = 223
SKWIVD = "".join(chr(c) for c in [80, 117, 109, 112, 49, 65, 115, 86, 83, 80])
SNQLNM = 85
SOKPHU = 224
SOOQNR = "".join(
    chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114, 114, 101, 110, 116]
)
SPBWJY = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
SPFTSI = 42
SSAKQX = "".join(chr(c) for c in [70, 98, 76, 105])
SSUHBV = "".join(
    chr(c) for c in [67, 69, 95, 50, 120, 50, 48, 65, 108, 108, 111, 119, 101, 100]
)
SUHBVW = "".join(chr(c) for c in [70, 117, 115, 101, 77, 97, 112, 112, 105, 110, 103])
SXUJUT = 20
TACCPQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 79, 112, 116, 105, 111, 110]
)
TATDZX = "".join(chr(c) for c in [68, 74, 83, 95, 78, 111, 50])
TBJEUT = "".join(
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
THBSKS = "".join(
    chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114, 114, 101, 110, 116]
)
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 98
TIDUBS = 102
TOPHUG = 34
TSIFJB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
TTIDUB = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
TYIYWS = 37
UBSSUH = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
UBYGDS = 8
UGTYIY = 36
UHBVWV = "".join(chr(c) for c in [85, 76])
UIKFWR = "".join(chr(c) for c in [67, 108, 101, 97, 110, 70, 105, 108, 116, 101, 114])
UJUTYE = 21
UNBLKX = 61
UNRJZT = "".join(chr(c) for c in [68, 74, 83, 95, 78, 111, 49])
UNXNKM = 27
UOJRJH = "".join(chr(c) for c in [79, 117, 116, 54, 65])
UQEXLS = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
USOOQN = 226
USPBWJ = "".join(chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 105, 110, 103])
UTOPHU = "".join(
    chr(c)
    for c in [70, 97, 110, 83, 101, 116, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
UTYEKC = "".join(chr(c) for c in [79, 119, 110])
UXFEFJ = 1
VDNQGV = 24
VDQLAI = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 90
VLASSA = "".join(chr(c) for c in [76, 73])
VUNXNK = "".join(
    chr(c) for c in [86, 83, 80, 83, 112, 101, 101, 100, 76, 101, 118, 101, 108, 49]
)
VWVUBY = "".join(
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
VYFCRT = "".join(
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
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 93
WAONPY = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
WBSIRY = "".join(
    chr(c) for c in [69, 99, 111, 110, 80, 114, 111, 103, 83, 116, 97, 116, 117, 115]
)
WDAFIK = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 84, 69, 110, 97, 98, 108, 101]
)
WIVDNQ = "".join(chr(c) for c in [80, 117, 109, 112, 51, 65, 115, 86, 83, 80])
WJYKLG = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
WMNZMJ = 65
WRKINE = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 111, 118, 101, 114])
WSKWIV = 39
WVUBYG = "".join(
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
XBQFYL = 17
XCHWDA = 74
XEKVKZ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
XFEFJT = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 80])
XLSXUJ = 19
XNKMLO = 28
XPICXQ = "".join(chr(c) for c in [79, 78, 90, 69, 78])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 51, 65])
XQIEFX = 201
XSJWMN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 77, 105, 110, 79, 110, 84, 105, 109, 101]
)
XTIACQ = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
XUJUTY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
XWAJVD = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
XYBQSN = 83
YBQSNQ = "".join(chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54])
YEKCWA = 6
YGDSBD = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
YIYWSK = "".join(
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
YKLGQP = "".join(
    chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 101, 80, 101, 114, 105, 111, 100]
)
YLJUIK = "".join(
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
YNQJYM = 7
YOUSPB = "".join(
    chr(c) for c in [79, 51, 70, 111, 108, 108, 111, 119, 80, 117, 109, 112]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
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
YXBQFY = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
YYLIUX = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 91
ZMJIGY = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
ZUQEXL = 96
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
AIIDNI = [QLAIID, LAIIDN]
ATDZXN = [
    BMJVHF,
    CXQIEF,
    QIEFXQ,
    EFXQGL,
    XQGLRA,
    GLRAHE,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    JRJHIU,
    SJMCBF,
    CBFEGZ,
    FEGZUQ,
]
BQNRXC = [LHBQNR, HBQNRX]
DSBDJQ = [YGDSBD, GDSBDJ]
DZXNQT = []
FYLJUI = [BQFYLJ, QFYLJU]
GYOUSP = [JIGYOU, IGYOUS, PIPIVL, RAHEOC]
HTBJEU = [NHTBJE, IGYOUS, PIPIVL]
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
IKJPUN = [AFIKJP, FIKJPU]
KINEJN = [UIKFWR, IKFWRK, KFWRKI, FWRKIN, WRKINE, RKINEJ]
LOIJUG = [RAHEOC, PIPIVL, IGYOUS]
MCBFEG = [
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
NIBXTI = [IDNIBX, DNIBXT]
QIPOUY = [CPQIPO, PQIPOU]
RJJJVY = [DJQRJJ, JQRJJJ, QRJJJV, RAHEOC]
RYXBQF = [BSIRYX, SIRYXB, JVHFTH, IRYXBQ]
TDZXNQ = [VLASSA]
TFMNHT = [CRTFMN, RTFMNH]
TYEKCW = [JUTYEK, UTYEKC]
UGSELH = [IJUGSE, JUGSEL]
UYNQJY = [POUYNQ, OUYNQJ]
VUBYGD = [UHBVWV, HBVWVU, BVWVUB, VWVUBY, WVUBYG, RAHEOC, RAHEOC, RAHEOC]
YFCRTF = [JJVYFC, JVYFCR, JVHFTH, VYFCRT]
YLIUXF = [ONPYYL, NPYYLI, PYYLIU, YYLIUX]
YMOUNB = [QJYMOU, JYMOUN]
ZTATDZ = [JVHFTH, NRJZTA, RJZTAT, JZTATD]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return JTACCP

    @property
    def output_keys(self):
        return ATDZXN

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
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, QBMJVH),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, QBMJVH),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, QBMJVH),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, QBMJVH),
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, ICXQIE, None, None, QBMJVH
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, None, ICXQIE, None, None, QBMJVH
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, ICXQIE, None, None, QBMJVH
            ),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, RJHIUS, None, ICXQIE, None, None, QBMJVH
            ),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, QBMJVH),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, QBMJVH),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, None, MCBFEG, None, None, QBMJVH
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, None, ICXQIE, None, None, QBMJVH
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, EGZUQE, None, ICXQIE, None, None, QBMJVH
            ),
            GZUQEX: GeckoByteStructAccessor(self.struct, GZUQEX, ZUQEXL, QBMJVH),
            UQEXLS: GeckoByteStructAccessor(self.struct, UQEXLS, QEXLSX, QBMJVH),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, QBMJVH),
            LSXUJU: GeckoByteStructAccessor(self.struct, LSXUJU, SXUJUT, QBMJVH),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UJUTYE, YEKCWA, TYEKCW, None, EKCWAO, QBMJVH
            ),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, YLIUXF, None, None, QBMJVH
            ),
            LIUXFE: GeckoBoolStructAccessor(
                self.struct, LIUXFE, IUXFEF, UXFEFJ, QBMJVH
            ),
            XFEFJT: GeckoBoolStructAccessor(
                self.struct, XFEFJT, IUXFEF, EKCWAO, QBMJVH
            ),
            FEFJTA: GeckoBoolStructAccessor(
                self.struct, FEFJTA, IUXFEF, EFJTAC, QBMJVH
            ),
            FJTACC: GeckoBoolStructAccessor(
                self.struct, FJTACC, IUXFEF, JTACCP, QBMJVH
            ),
            TACCPQ: GeckoBoolStructAccessor(
                self.struct, TACCPQ, IUXFEF, ACCPQI, QBMJVH
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, IUXFEF, YEKCWA, QIPOUY, None, EKCWAO, QBMJVH
            ),
            IPOUYN: GeckoEnumStructAccessor(
                self.struct, IPOUYN, IUXFEF, YNQJYM, UYNQJY, None, EKCWAO, QBMJVH
            ),
            NQJYMO: GeckoEnumStructAccessor(
                self.struct, NQJYMO, IUXFEF, MOUNBL, YMOUNB, None, EKCWAO, QBMJVH
            ),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, QBMJVH),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, QBMJVH),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, QBMJVH),
            ZMJIGY: GeckoEnumStructAccessor(
                self.struct, ZMJIGY, MJIGYO, MOUNBL, GYOUSP, None, EFJTAC, QBMJVH
            ),
            YOUSPB: GeckoBoolStructAccessor(
                self.struct, YOUSPB, MJIGYO, EKCWAO, QBMJVH
            ),
            OUSPBW: GeckoBoolStructAccessor(
                self.struct, OUSPBW, MJIGYO, JTACCP, QBMJVH
            ),
            USPBWJ: GeckoBoolStructAccessor(
                self.struct, USPBWJ, MJIGYO, EFJTAC, QBMJVH
            ),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, MJIGYO, YEKCWA, QIPOUY, None, None, QBMJVH
            ),
            PBWJYK: GeckoByteStructAccessor(self.struct, PBWJYK, BWJYKL, QBMJVH),
            WJYKLG: GeckoByteStructAccessor(self.struct, WJYKLG, JYKLGQ, QBMJVH),
            YKLGQP: GeckoByteStructAccessor(self.struct, YKLGQP, KLGQPL, QBMJVH),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoByteStructAccessor(self.struct, QPLSPF, PLSPFT, QBMJVH),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, QBMJVH),
            PFTSIF: GeckoTimeStructAccessor(self.struct, PFTSIF, FTSIFJ, QBMJVH),
            TSIFJB: GeckoTimeStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoTimeStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoTimeStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoByteStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoTimeStructAccessor(self.struct, MJMAOA, JMAOAW, QBMJVH),
            MAOAWB: GeckoTimeStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoBoolStructAccessor(
                self.struct, OAWBSI, AWBSIR, JTACCP, QBMJVH
            ),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, AWBSIR, EFJTAC, RYXBQF, None, EFJTAC, QBMJVH
            ),
            YXBQFY: GeckoEnumStructAccessor(
                self.struct, YXBQFY, XBQFYL, MOUNBL, FYLJUI, None, EKCWAO, QBMJVH
            ),
            YLJUIK: GeckoBoolStructAccessor(
                self.struct, YLJUIK, XBQFYL, UXFEFJ, QBMJVH
            ),
            VDQLAI: GeckoEnumStructAccessor(
                self.struct, VDQLAI, DQLAII, EFJTAC, AIIDNI, None, EKCWAO, QBMJVH
            ),
            IIDNIB: GeckoEnumStructAccessor(
                self.struct, IIDNIB, DQLAII, ACCPQI, NIBXTI, None, EKCWAO, QBMJVH
            ),
            IBXTIA: GeckoByteStructAccessor(self.struct, IBXTIA, BXTIAC, None),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, None),
            IACQFF: GeckoByteStructAccessor(self.struct, IACQFF, ACQFFT, None),
            CQFFTT: GeckoByteStructAccessor(self.struct, CQFFTT, QFFTTI, QBMJVH),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, QBMJVH),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, QBMJVH),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, QBMJVH),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, QBMJVH),
            SSUHBV: GeckoBoolStructAccessor(
                self.struct, SSUHBV, AWBSIR, YEKCWA, QBMJVH
            ),
            SUHBVW: GeckoEnumStructAccessor(
                self.struct, SUHBVW, DQLAII, UXFEFJ, VUBYGD, None, UBYGDS, QBMJVH
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, DQLAII, YNQJYM, DSBDJQ, None, EKCWAO, QBMJVH
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, JTACCP, RJJJVY, None, EFJTAC, QBMJVH
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, AWBSIR, UXFEFJ, YFCRTF, None, EFJTAC, QBMJVH
            ),
            FCRTFM: GeckoEnumStructAccessor(
                self.struct, FCRTFM, AWBSIR, MOUNBL, TFMNHT, None, EKCWAO, QBMJVH
            ),
            FMNHTB: GeckoEnumStructAccessor(
                self.struct, FMNHTB, MNHTBJ, UXFEFJ, HTBJEU, None, EFJTAC, QBMJVH
            ),
            TBJEUT: GeckoBoolStructAccessor(
                self.struct, TBJEUT, MNHTBJ, JTACCP, QBMJVH
            ),
            BJEUTO: GeckoBoolStructAccessor(
                self.struct, BJEUTO, BDJQRJ, ACCPQI, QBMJVH
            ),
            JEUTOP: GeckoBoolStructAccessor(
                self.struct, JEUTOP, BDJQRJ, YEKCWA, QBMJVH
            ),
            EUTOPH: GeckoBoolStructAccessor(
                self.struct, EUTOPH, BDJQRJ, YNQJYM, QBMJVH
            ),
            UTOPHU: GeckoByteStructAccessor(self.struct, UTOPHU, TOPHUG, QBMJVH),
            OPHUGT: GeckoByteStructAccessor(self.struct, OPHUGT, PHUGTY, QBMJVH),
            HUGTYI: GeckoByteStructAccessor(self.struct, HUGTYI, UGTYIY, QBMJVH),
            GTYIYW: GeckoByteStructAccessor(self.struct, GTYIYW, TYIYWS, QBMJVH),
            YIYWSK: GeckoByteStructAccessor(self.struct, YIYWSK, IYWSKW, QBMJVH),
            YWSKWI: GeckoByteStructAccessor(self.struct, YWSKWI, WSKWIV, QBMJVH),
            SKWIVD: GeckoBoolStructAccessor(
                self.struct, SKWIVD, KWIVDN, MOUNBL, QBMJVH
            ),
            WIVDNQ: GeckoBoolStructAccessor(
                self.struct, WIVDNQ, KWIVDN, EKCWAO, QBMJVH
            ),
            IVDNQG: GeckoByteStructAccessor(self.struct, IVDNQG, VDNQGV, QBMJVH),
            DNQGVU: GeckoByteStructAccessor(self.struct, DNQGVU, NQGVUN, QBMJVH),
            QGVUNX: GeckoByteStructAccessor(self.struct, QGVUNX, GVUNXN, QBMJVH),
            VUNXNK: GeckoByteStructAccessor(self.struct, VUNXNK, UNXNKM, QBMJVH),
            NXNKML: GeckoByteStructAccessor(self.struct, NXNKML, XNKMLO, QBMJVH),
            NKMLOI: GeckoByteStructAccessor(self.struct, NKMLOI, KMLOIJ, QBMJVH),
            MLOIJU: GeckoEnumStructAccessor(
                self.struct, MLOIJU, BDJQRJ, None, LOIJUG, None, EFJTAC, QBMJVH
            ),
            OIJUGS: GeckoEnumStructAccessor(
                self.struct, OIJUGS, DQLAII, YEKCWA, UGSELH, None, EKCWAO, QBMJVH
            ),
            GSELHB: GeckoBoolStructAccessor(
                self.struct, GSELHB, MNHTBJ, EFJTAC, QBMJVH
            ),
            SELHBQ: GeckoBoolStructAccessor(
                self.struct, SELHBQ, MNHTBJ, ACCPQI, QBMJVH
            ),
            ELHBQN: GeckoEnumStructAccessor(
                self.struct, ELHBQN, BDJQRJ, EKCWAO, BQNRXC, None, EKCWAO, QBMJVH
            ),
            QNRXCH: GeckoTempStructAccessor(self.struct, QNRXCH, NRXCHW, QBMJVH),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, QBMJVH),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, QBMJVH),
            WDAFIK: GeckoBoolStructAccessor(
                self.struct, WDAFIK, MNHTBJ, MOUNBL, QBMJVH
            ),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, DQLAII, MOUNBL, IKJPUN, None, EKCWAO, QBMJVH
            ),
            KJPUNR: GeckoBoolStructAccessor(
                self.struct, KJPUNR, UJUTYE, MOUNBL, QBMJVH
            ),
            JPUNRJ: GeckoBoolStructAccessor(
                self.struct, JPUNRJ, UJUTYE, UXFEFJ, QBMJVH
            ),
            PUNRJZ: GeckoBoolStructAccessor(
                self.struct, PUNRJZ, UJUTYE, YEKCWA, QBMJVH
            ),
            UNRJZT: GeckoEnumStructAccessor(
                self.struct, UNRJZT, UJUTYE, EKCWAO, ZTATDZ, None, EFJTAC, QBMJVH
            ),
            TATDZX: GeckoEnumStructAccessor(
                self.struct, TATDZX, UJUTYE, EFJTAC, ZTATDZ, None, EFJTAC, QBMJVH
            ),
        }

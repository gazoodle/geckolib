#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXM v2'
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
ACCPQI = 33
ACQFFT = "".join(chr(c) for c in [85, 76])
AIIDNI = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 52])
AJVDQL = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 49])
AKQXPI = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
AMJMAO = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
AOAWBS = "".join(
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
AONPYY = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
ASSAKQ = "".join(chr(c) for c in [70, 98, 77, 116, 114])
AWBSIR = "".join(
    chr(c) for c in [69, 99, 111, 110, 80, 114, 111, 103, 83, 116, 97, 116, 117, 115]
)
BFEGZU = 211
BIAMJM = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
BJEUTO = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 82, 101, 115, 116, 114, 105, 99, 116, 105, 111, 110]
)
BLKXSJ = "".join(chr(c) for c in [70, 105, 108, 116, 77, 105, 110, 68, 117, 114])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49, 65])
BQFYLJ = "".join(chr(c) for c in [65, 110, 121, 70, 114, 101, 101, 80, 117, 109, 112])
BQSNQL = "".join(chr(c) for c in [72, 105, 103, 104])
BSIRYX = "".join(chr(c) for c in [78, 111, 116, 65, 99, 116, 105, 118, 101])
BSKSOK = "".join(
    chr(c) for c in [79, 117, 116, 50, 66, 67, 117, 114, 114, 101, 110, 116]
)
BSSUHB = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 77, 97, 120, 80, 111, 119, 101, 114]
)
BVWVUB = "".join(
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
BWJYKL = "".join(chr(c) for c in [80, 49])
BXTIAC = "".join(
    chr(c) for c in [78, 111, 116, 65, 118, 97, 105, 108, 97, 98, 108, 101]
)
BXYBQS = "".join(
    chr(c) for c in [83, 87, 77, 80, 117, 114, 103, 101, 83, 112, 101, 101, 100]
)
BYGDSB = "".join(chr(c) for c in [80, 97, 117, 115, 101])
CBFEGZ = "".join(chr(c) for c in [79, 117, 116, 73, 79, 50])
CCPQIP = "".join(chr(c) for c in [67, 108, 101, 97, 110, 67, 80])
CPQIPO = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 79, 112, 116, 105, 111, 110]
)
CQBMJV = 1
CQFFTT = "".join(
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
CRTFMN = "".join(
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
CTHBSK = 221
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 49, 66])
DJQRJJ = "".join(
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
DNIBXT = 92
DNQGVU = "".join(
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
DQLAII = 89
DSBDJQ = 24
DUBSSU = 23
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 50])
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 50, 66])
EGZUQE = 212
EJNIBX = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 55, 78, 98, 87, 101, 101, 107]
)
EKCWAO = "".join(chr(c) for c in [79, 110, 83, 116, 97, 114, 116])
EKVKZI = "".join(chr(c) for c in [50, 51, 48, 86, 65, 67])
EOCTHB = 220
EUTOPH = "".join(
    chr(c) for c in [70, 117, 108, 108, 80, 111, 119, 101, 114, 79, 110, 108, 121]
)
EXLSXU = "".join(chr(c) for c in [65, 115, 99, 101, 110, 100, 97, 110, 116])
FCRTFM = 29
FEFJTA = "".join(chr(c) for c in [78, 111, 116, 85, 115, 101, 100, 49])
FEGZUQ = "".join(chr(c) for c in [79, 117, 116, 73, 79, 52])
FFTTID = "".join(
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
FJBIAM = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
FJTACC = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
FMNHTB = 31
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(
    chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 101, 80, 101, 114, 105, 111, 100]
)
FTTIDU = "".join(
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
FWRKIN = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 52, 78, 98, 87, 101, 101, 107]
)
FXQGLR = 203
FYLJUI = "".join(
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
GDSBDJ = "".join(chr(c) for c in [70, 97, 110, 80, 117, 109, 112])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 72, 101, 97, 116, 101, 114])
GQPLSP = "".join(chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 66, 121])
GTYIYW = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
GVUNXN = "".join(chr(c) for c in [79, 110, 80, 50])
GYOUSP = 60
GZUQEX = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
HBSKSO = 222
HBVWVU = "".join(chr(c) for c in [73, 103, 110, 111, 114, 101, 85, 68])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(
    chr(c) for c in [79, 117, 116, 49, 65, 67, 117, 114, 114, 101, 110, 116]
)
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 225
HTBJEU = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
HUGTYI = "".join(chr(c) for c in [70])
HUOJRJ = 206
HXEKVK = "".join(chr(c) for c in [76, 105, 110, 101, 86, 111, 108, 116, 97, 103, 101])
IACQFF = "".join(chr(c) for c in [70, 117, 115, 101, 77, 97, 112, 112, 105, 110, 103])
IAMJMA = 39
IBXTIA = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
IBXYBQ = 82
IDNIBX = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 53])
IDUBSS = "".join(
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
IEFXQG = 202
IFJBIA = 36
IGYOUS = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 77, 105, 110, 79, 110, 84, 105, 109, 101]
)
IIDNIB = 91
IKFWRK = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 51, 78, 98, 87, 101, 101, 107]
)
ILXWAJ = "".join(
    chr(c) for c in [66, 114, 78, 98, 83, 101, 116, 116, 105, 110, 103, 115]
)
INEJNI = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 54, 78, 98, 87, 101, 101, 107]
)
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 79, 112, 116, 105, 111, 110]
)
IUSOOQ = "".join(
    chr(c) for c in [79, 117, 116, 53, 65, 67, 117, 114, 114, 101, 110, 116]
)
IUXFEF = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
IVDNQG = "".join(
    chr(c) for c in [65, 117, 120, 49, 65, 115, 84, 86, 76, 105, 102, 116, 101, 114]
)
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = 70
JBIAMJ = 37
JEUTOP = "".join(chr(c) for c in [78, 111])
JHIUSO = "".join(
    chr(c) for c in [79, 117, 116, 52, 65, 67, 117, 114, 114, 101, 110, 116]
)
JIGYOU = 59
JJJVYF = "".join(
    chr(c)
    for c in [70, 97, 110, 83, 101, 116, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
JJVYFC = 27
JMAOAW = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 111, 112])
JMCBFE = 210
JNIBXY = 81
JQRJJJ = "".join(
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
JRJHIU = "".join(chr(c) for c in [79, 117, 116, 55, 65])
JUIKFW = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 50, 78, 98, 87, 101, 101, 107]
)
JUTYEK = 18
JVDQLA = 88
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(
    chr(c)
    for c in [70, 97, 110, 67, 108, 114, 65, 79, 84, 84, 101, 109, 112, 65, 100, 99]
)
JWMNZM = 56
JYKLGQ = 4
JYMOUN = "".join(
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
KCWAON = "".join(chr(c) for c in [79, 110, 67, 104, 97, 110, 103, 101])
KFWRKI = 77
KINEJN = 79
KLGQPL = "".join(
    chr(c) for c in [79, 51, 68, 117, 114, 105, 110, 103, 70, 105, 108, 116]
)
KPHUOJ = 205
KQXPIC = "".join(chr(c) for c in [83, 112, 76, 105, 102, 116])
KSOKPH = "".join(
    chr(c) for c in [79, 117, 116, 51, 65, 67, 117, 114, 114, 101, 110, 116]
)
KWIVDN = "".join(chr(c) for c in [50, 52, 104])
KXSJWM = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
KZILXW = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
LAIIDN = 90
LASSAK = "".join(chr(c) for c in [70, 65, 78])
LGQPLS = "".join(chr(c) for c in [79, 51, 84, 111, 103, 103, 108, 105, 110, 103])
LIUXFE = 69
LJUIKF = 75
LKXSJW = 57
LNMHXE = "".join(chr(c) for c in [54, 48, 72, 90])
LRAHEO = 209
LSPFTS = 64
LXWAJV = 86
MAOAWB = 73
MJIGYO = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 67, 80, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
MJMAOA = 71
MJVHFT = 200
MNHTBJ = "".join(
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
MNZMJI = 62
MOUNBL = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
NEJNIB = 80
NHTBJE = 32
NIBXTI = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 77, 101, 110, 117])
NIBXYB = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 56, 78, 98, 87, 101, 101, 107]
)
NMHXEK = "".join(chr(c) for c in [53, 48, 72, 90])
NPYYLI = "".join(
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
NQGVUN = "".join(chr(c) for c in [68, 74, 83, 95, 78, 111, 49])
NQJYMO = "".join(
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
NQLNMH = "".join(
    chr(c) for c in [76, 105, 110, 101, 70, 114, 101, 113, 117, 101, 110, 99, 121]
)
NRSJMC = "".join(
    chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114, 114, 101, 110, 116]
)
NXNKML = "".join(chr(c) for c in [68, 74, 83, 95, 78, 111, 50])
NZMJIG = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 65, 99, 116, 84, 101, 109, 112]
)
OAWBSI = 68
OCTHBS = "".join(
    chr(c) for c in [79, 117, 116, 49, 66, 67, 117, 114, 114, 101, 110, 116]
)
OJRJHI = 207
OKPHUO = "".join(chr(c) for c in [79, 117, 116, 52, 65])
ONPYYL = 20
OOQNRS = 227
OPHUGT = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
OQNRSJ = "".join(
    chr(c) for c in [79, 117, 116, 55, 65, 67, 117, 114, 114, 101, 110, 116]
)
OUNBLK = "".join(chr(c) for c in [76, 111])
OUSPBW = 61
OUYNQJ = "".join(chr(c) for c in [65, 110, 121, 85, 68])
PBWJYK = "".join(chr(c) for c in [78, 79, 78, 69])
PFTSIF = 65
PHUGTY = "".join(chr(c) for c in [67])
PHUOJR = "".join(chr(c) for c in [79, 117, 116, 53, 65])
PICXQI = "".join(chr(c) for c in [86, 65, 76, 86, 69])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(
    chr(c) for c in [79, 51, 70, 105, 108, 116, 101, 114, 68, 101, 108, 97, 121]
)
POUYNQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121]
)
PQIPOU = 34
PYYLIU = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116, 83, 104, 97, 114, 101]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = 17
QFFTTI = "".join(
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
QGLRAH = 204
QGVUNX = "".join(chr(c) for c in [79, 110, 80, 49])
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 65])
QIPOUY = "".join(chr(c) for c in [67, 80, 65, 108, 119, 97, 121, 115, 79, 78])
QJYMOU = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
QLAIID = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 51])
QLNMHX = 83
QNRSJM = 228
QPLSPF = 6
QRJJJV = "".join(
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
QXPICX = "".join(chr(c) for c in [83, 65, 78, 73])
RAHEOC = "".join(chr(c) for c in [])
RJHIUS = 208
RJJJVY = "".join(
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
RKINEJ = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 53, 78, 98, 87, 101, 101, 107]
)
RSJMCB = 123
RTFMNH = 30
RYXBQF = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
SAKQXP = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SBDJQR = "".join(chr(c) for c in [78, 111, 110, 101])
SIFJBI = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
SIRYXB = "".join(chr(c) for c in [65, 99, 116, 105, 118, 101])
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 76, 105])
SJWMNZ = "".join(
    chr(c) for c in [70, 105, 108, 116, 79, 84, 68, 101, 97, 100, 98, 97, 110, 100]
)
SKSOKP = 223
SKWIVD = "".join(chr(c) for c in [65, 109, 80, 109])
SNQLNM = "".join(
    chr(c) for c in [83, 87, 77, 80, 117, 114, 103, 101, 66, 108, 111, 119, 101, 114]
)
SOKPHU = 224
SOOQNR = "".join(
    chr(c) for c in [79, 117, 116, 54, 65, 67, 117, 114, 114, 101, 110, 116]
)
SPBWJY = 63
SPFTSI = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
SSAKQX = "".join(chr(c) for c in [70, 98, 76, 105])
SSUHBV = "".join(chr(c) for c in [75, 101, 101, 112, 79, 102, 102])
SXUJUT = 0
TACCPQ = "".join(chr(c) for c in [67, 108, 101, 97, 110, 80, 49])
TFMNHT = "".join(
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
THBSKS = "".join(
    chr(c) for c in [79, 117, 116, 50, 65, 67, 117, 114, 114, 101, 110, 116]
)
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 7
TIDUBS = 8
TOPHUG = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 69, 110, 97, 98, 108, 101]
)
TSIFJB = 66
TYEKCW = 19
TYIYWS = 25
UBSSUH = "".join(chr(c) for c in [78, 111, 65, 99, 116, 105, 111, 110])
UBYGDS = "".join(chr(c) for c in [67, 97, 110, 99, 101, 108])
UHBVWV = "".join(
    chr(c)
    for c in [85, 68, 65, 99, 116, 105, 111, 110, 79, 110, 81, 117, 105, 101, 116]
)
UIKFWR = 76
UJUTYE = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
UNBLKX = "".join(chr(c) for c in [72, 105])
UOJRJH = "".join(chr(c) for c in [79, 117, 116, 54, 65])
UQEXLS = "".join(
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
USOOQN = 226
USPBWJ = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
UTYEKC = "".join(
    chr(c) for c in [70, 105, 98, 101, 114, 84, 105, 109, 101, 79, 117, 116]
)
UXFEFJ = 35
UYNQJY = "".join(chr(c) for c in [80, 117, 109, 112, 85, 68])
VDNQGV = 21
VDQLAI = "".join(chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 116, 50])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 5
VLASSA = "".join(chr(c) for c in [76, 73])
VUBYGD = "".join(
    chr(c)
    for c in [81, 117, 105, 101, 116, 65, 99, 116, 105, 111, 110, 79, 110, 85, 68]
)
VUNXNK = "".join(chr(c) for c in [79, 110, 80, 51])
VWVUBY = "".join(
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
VYFCRT = 28
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 87
WAONPY = 1
WBSIRY = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
WMNZMJ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
WRKINE = 78
WSKWIV = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
XBQFYL = "".join(
    chr(c)
    for c in [78, 101, 120, 116, 70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121]
)
XEKVKZ = "".join(chr(c) for c in [50, 52, 48, 86, 97, 99])
XFEFJT = "".join(chr(c) for c in [83, 116, 97, 114, 116, 68, 117, 114, 70, 114, 101])
XLSXUJ = "".join(chr(c) for c in [68, 101, 115, 99, 101, 110, 100, 97, 110, 116])
XPICXQ = "".join(chr(c) for c in [79, 78, 90, 69, 78])
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 51, 65])
XQIEFX = 201
XSJWMN = 55
XUJUTY = 2
XWAJVD = "".join(chr(c) for c in [66, 114, 83, 101, 116, 73, 110, 100, 101, 120])
XYBQSN = 67
YBQSNQ = "".join(chr(c) for c in [76, 111, 119])
YEKCWA = "".join(
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
YFCRTF = "".join(
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
YIYWSK = "".join(
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
YKLGQP = "".join(
    chr(c) for c in [79, 51, 70, 111, 108, 108, 111, 119, 80, 117, 109, 112]
)
YLIUXF = "".join(
    chr(c) for c in [81, 117, 105, 101, 116, 84, 105, 109, 101, 79, 117, 116]
)
YLJUIK = "".join(
    chr(c) for c in [75, 54, 48, 48, 77, 115, 103, 49, 78, 98, 87, 101, 101, 107]
)
YOUSPB = "".join(
    chr(c) for c in [70, 105, 108, 116, 67, 80, 79, 84, 77, 97, 120, 68, 117, 114]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 84, 69, 110, 97, 98, 108, 101]
)
YXBQFY = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
YYLIUX = 3
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 85
ZMJIGY = 58
ZUQEXL = 84
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
BDJQRJ = [SBDJQR, BWJYKL, PIPIVL]
CWAONP = [EKCWAO, KCWAON]
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
IRYXBQ = [WBSIRY, BSIRYX, JVHFTH, SIRYXB]
JTACCP = [XFEFJT, FEFJTA, EFJTAC, FJTACC]
KMLOIJ = []
KVKZIL = [XEKVKZ, EKVKZI]
LSXUJU = [EXLSXU, XLSXUJ]
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
MHXEKV = [LNMHXE, NMHXEK]
NBLKXS = [OUNBLK, UNBLKX]
NKMLOI = [VLASSA]
QFYLJU = [YXBQFY, XBQFYL, BQFYLJ]
QSNQLN = [YBQSNQ, BQSNQL]
SUHBVW = [UBSSUH, BSSUHB, SSUHBV, RAHEOC]
TBJEUT = [RAHEOC, PIPIVL, BWJYKL]
TTIDUB = [ACQFFT, CQFFTT, QFFTTI, FFTTID, FTTIDU, RAHEOC, RAHEOC, RAHEOC]
UGTYIY = [PHUGTY, HUGTYI]
UNXNKM = [JVHFTH, QGVUNX, GVUNXN, VUNXNK]
UTOPHU = [JEUTOP, EUTOPH]
WIVDNQ = [SKWIVD, KWIVDN]
WJYKLG = [PBWJYK, BWJYKL, PIPIVL, RAHEOC]
WVUBYG = [HBVWVU, BVWVUB, JVHFTH, VWVUBY]
XNKMLO = [
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
    UQEXLS,
]
XTIACQ = [IBXTIA, BXTIAC]
YGDSBD = [UBYGDS, BYGDSB]
YMOUNB = [QJYMOU, JYMOUN]
YNQJYM = [OUYNQJ, UYNQJY]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return XUJUTY

    @property
    def output_keys(self):
        return XNKMLO

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
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, SXUJUT, LSXUJU, None, XUJUTY, QBMJVH
            ),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, QBMJVH),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoEnumStructAccessor(
                self.struct, YEKCWA, QEXLSX, WAONPY, CWAONP, None, XUJUTY, QBMJVH
            ),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, QEXLSX, XUJUTY, CWAONP, None, XUJUTY, QBMJVH
            ),
            PYYLIU: GeckoBoolStructAccessor(
                self.struct, PYYLIU, QEXLSX, YYLIUX, QBMJVH
            ),
            YLIUXF: GeckoByteStructAccessor(self.struct, YLIUXF, LIUXFE, QBMJVH),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, UXFEFJ, None, JTACCP, None, None, QBMJVH
            ),
            TACCPQ: GeckoBoolStructAccessor(
                self.struct, TACCPQ, ACCPQI, WAONPY, QBMJVH
            ),
            CCPQIP: GeckoBoolStructAccessor(
                self.struct, CCPQIP, ACCPQI, XUJUTY, QBMJVH
            ),
            CPQIPO: GeckoBoolStructAccessor(
                self.struct, CPQIPO, PQIPOU, SXUJUT, QBMJVH
            ),
            QIPOUY: GeckoBoolStructAccessor(
                self.struct, QIPOUY, ACCPQI, YYLIUX, QBMJVH
            ),
            IPOUYN: GeckoBoolStructAccessor(
                self.struct, IPOUYN, PQIPOU, WAONPY, QBMJVH
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, PQIPOU, XUJUTY, YNQJYM, None, XUJUTY, QBMJVH
            ),
            NQJYMO: GeckoEnumStructAccessor(
                self.struct, NQJYMO, PQIPOU, YYLIUX, YMOUNB, None, XUJUTY, QBMJVH
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, ACCPQI, SXUJUT, NBLKXS, None, XUJUTY, QBMJVH
            ),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, QBMJVH),
            WMNZMJ: GeckoByteStructAccessor(self.struct, WMNZMJ, MNZMJI, QBMJVH),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoByteStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoByteStructAccessor(self.struct, IGYOUS, GYOUSP, QBMJVH),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, SPBWJY, SXUJUT, WJYKLG, None, JYKLGQ, QBMJVH
            ),
            YKLGQP: GeckoBoolStructAccessor(
                self.struct, YKLGQP, SPBWJY, XUJUTY, QBMJVH
            ),
            KLGQPL: GeckoBoolStructAccessor(
                self.struct, KLGQPL, SPBWJY, YYLIUX, QBMJVH
            ),
            LGQPLS: GeckoBoolStructAccessor(
                self.struct, LGQPLS, SPBWJY, JYKLGQ, QBMJVH
            ),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, SPBWJY, QPLSPF, YNQJYM, None, None, QBMJVH
            ),
            PLSPFT: GeckoByteStructAccessor(self.struct, PLSPFT, LSPFTS, QBMJVH),
            SPFTSI: GeckoByteStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoByteStructAccessor(self.struct, FTSIFJ, TSIFJB, QBMJVH),
            SIFJBI: GeckoByteStructAccessor(self.struct, SIFJBI, IFJBIA, QBMJVH),
            FJBIAM: GeckoTimeStructAccessor(self.struct, FJBIAM, JBIAMJ, QBMJVH),
            BIAMJM: GeckoTimeStructAccessor(self.struct, BIAMJM, IAMJMA, QBMJVH),
            AMJMAO: GeckoTimeStructAccessor(self.struct, AMJMAO, MJMAOA, QBMJVH),
            JMAOAW: GeckoTimeStructAccessor(self.struct, JMAOAW, MAOAWB, QBMJVH),
            AOAWBS: GeckoBoolStructAccessor(
                self.struct, AOAWBS, OAWBSI, YYLIUX, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, OAWBSI, JYKLGQ, IRYXBQ, None, JYKLGQ, QBMJVH
            ),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, QEXLSX, JYKLGQ, QFYLJU, None, JYKLGQ, QBMJVH
            ),
            FYLJUI: GeckoBoolStructAccessor(
                self.struct, FYLJUI, QEXLSX, QPLSPF, QBMJVH
            ),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, SXUJUT, QSNQLN, None, XUJUTY, QBMJVH
            ),
            SNQLNM: GeckoBoolStructAccessor(
                self.struct, SNQLNM, XYBQSN, WAONPY, QBMJVH
            ),
            NQLNMH: GeckoEnumStructAccessor(
                self.struct, NQLNMH, QLNMHX, JYKLGQ, MHXEKV, None, XUJUTY, QBMJVH
            ),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, QLNMHX, VKZILX, KVKZIL, None, XUJUTY, QBMJVH
            ),
            KZILXW: GeckoByteStructAccessor(self.struct, KZILXW, ZILXWA, None),
            ILXWAJ: GeckoByteStructAccessor(self.struct, ILXWAJ, LXWAJV, None),
            XWAJVD: GeckoByteStructAccessor(self.struct, XWAJVD, WAJVDQ, None),
            AJVDQL: GeckoByteStructAccessor(self.struct, AJVDQL, JVDQLA, QBMJVH),
            VDQLAI: GeckoByteStructAccessor(self.struct, VDQLAI, DQLAII, QBMJVH),
            QLAIID: GeckoByteStructAccessor(self.struct, QLAIID, LAIIDN, QBMJVH),
            AIIDNI: GeckoByteStructAccessor(self.struct, AIIDNI, IIDNIB, QBMJVH),
            IDNIBX: GeckoByteStructAccessor(self.struct, IDNIBX, DNIBXT, QBMJVH),
            NIBXTI: GeckoEnumStructAccessor(
                self.struct, NIBXTI, QLNMHX, TIACQF, XTIACQ, None, XUJUTY, QBMJVH
            ),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, QLNMHX, WAONPY, TTIDUB, None, TIDUBS, QBMJVH
            ),
            IDUBSS: GeckoEnumStructAccessor(
                self.struct, IDUBSS, DUBSSU, YYLIUX, SUHBVW, None, JYKLGQ, QBMJVH
            ),
            UHBVWV: GeckoEnumStructAccessor(
                self.struct, UHBVWV, OAWBSI, WAONPY, WVUBYG, None, JYKLGQ, QBMJVH
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, OAWBSI, SXUJUT, YGDSBD, None, XUJUTY, QBMJVH
            ),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, WAONPY, BDJQRJ, None, JYKLGQ, QBMJVH
            ),
            DJQRJJ: GeckoBoolStructAccessor(
                self.struct, DJQRJJ, DSBDJQ, YYLIUX, QBMJVH
            ),
            JQRJJJ: GeckoBoolStructAccessor(
                self.struct, JQRJJJ, DUBSSU, VKZILX, QBMJVH
            ),
            QRJJJV: GeckoBoolStructAccessor(
                self.struct, QRJJJV, DUBSSU, QPLSPF, QBMJVH
            ),
            RJJJVY: GeckoBoolStructAccessor(
                self.struct, RJJJVY, DUBSSU, TIACQF, QBMJVH
            ),
            JJJVYF: GeckoByteStructAccessor(self.struct, JJJVYF, JJVYFC, QBMJVH),
            JVYFCR: GeckoByteStructAccessor(self.struct, JVYFCR, VYFCRT, QBMJVH),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, QBMJVH),
            CRTFMN: GeckoByteStructAccessor(self.struct, CRTFMN, RTFMNH, QBMJVH),
            TFMNHT: GeckoByteStructAccessor(self.struct, TFMNHT, FMNHTB, QBMJVH),
            MNHTBJ: GeckoByteStructAccessor(self.struct, MNHTBJ, NHTBJE, QBMJVH),
            HTBJEU: GeckoEnumStructAccessor(
                self.struct, HTBJEU, DUBSSU, None, TBJEUT, None, JYKLGQ, QBMJVH
            ),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, QLNMHX, QPLSPF, UTOPHU, None, XUJUTY, QBMJVH
            ),
            TOPHUG: GeckoBoolStructAccessor(
                self.struct, TOPHUG, DSBDJQ, JYKLGQ, QBMJVH
            ),
            OPHUGT: GeckoEnumStructAccessor(
                self.struct, OPHUGT, DUBSSU, XUJUTY, UGTYIY, None, XUJUTY, QBMJVH
            ),
            GTYIYW: GeckoTempStructAccessor(self.struct, GTYIYW, TYIYWS, QBMJVH),
            YIYWSK: GeckoByteStructAccessor(self.struct, YIYWSK, IYWSKW, QBMJVH),
            YWSKWI: GeckoBoolStructAccessor(
                self.struct, YWSKWI, DSBDJQ, SXUJUT, QBMJVH
            ),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, QLNMHX, SXUJUT, WIVDNQ, None, XUJUTY, QBMJVH
            ),
            IVDNQG: GeckoBoolStructAccessor(
                self.struct, IVDNQG, VDNQGV, SXUJUT, QBMJVH
            ),
            DNQGVU: GeckoBoolStructAccessor(
                self.struct, DNQGVU, VDNQGV, WAONPY, QBMJVH
            ),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, VDNQGV, XUJUTY, UNXNKM, None, JYKLGQ, QBMJVH
            ),
            NXNKML: GeckoEnumStructAccessor(
                self.struct, NXNKML, VDNQGV, JYKLGQ, UNXNKM, None, JYKLGQ, QBMJVH
            ),
        }

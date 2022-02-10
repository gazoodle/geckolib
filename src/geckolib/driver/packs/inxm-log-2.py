#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v2'
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
ACCPQI = 313
AHEOCT = 11
AKQXPI = 296
AMJMAO = "".join(chr(c) for c in [82, 72, 95, 82, 101, 103, 83, 108, 111, 112, 101])
AOAWBS = "".join(
    chr(c) for c in [82, 72, 95, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
AONPYY = 307
ASSAKQ = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        54,
        65,
    ]
)
AWBSIR = "".join(
    chr(c) for c in [82, 72, 95, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
BFEGZU = "".join(chr(c) for c in [80, 50])
BIAMJM = 257
BLKXSJ = "".join(
    chr(c) for c in [83, 87, 77, 80, 117, 114, 103, 101, 95, 83, 117, 115, 112]
)
BMJVHF = "".join(chr(c) for c in [66, 114, 77, 101, 110, 117])
BQFYLJ = "".join(chr(c) for c in [82, 72, 95, 83, 87, 84, 114, 105, 97, 99, 79, 72])
BSIRYX = "".join(chr(c) for c in [82, 72, 95, 72, 87, 95, 72, 76])
BSKSOK = "".join(chr(c) for c in [79, 78])
BWJYKL = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
CCPQIP = "".join(chr(c) for c in [70, 105, 108, 116, 80, 117, 114, 103, 101])
CPQIPO = 269
CQBMJV = 256
CTHBSK = "".join(chr(c) for c in [85, 68, 95, 80, 53])
CVYYPI = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        50,
        65,
    ]
)
CWAONP = 303
CXQIEF = "".join(chr(c) for c in [76, 79, 87])
ECVYYP = 282
EFJTAC = 310
EFXQGL = 2
EGZUQE = "".join(chr(c) for c in [80, 52])
EJNIBX = 256
EKCWAO = 306
EOCTHB = "".join(chr(c) for c in [85, 68, 95, 80, 52])
EXLSXU = "".join(chr(c) for c in [79, 90, 79, 78, 69])
FEFJTA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
FEGZUQ = "".join(chr(c) for c in [80, 51])
FJBIAM = 263
FJTACC = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        79,
        110,
        122,
        101,
        110,
        65,
        99,
        116,
        105,
        111,
        110,
    ]
)
FTHECV = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        49,
        65,
    ]
)
FTSIFJ = "".join(chr(c) for c in [79, 72, 67, 111, 110, 100, 105, 116, 105, 111, 110])
FWRKIN = "".join(chr(c) for c in [82, 72, 95, 70, 108, 111, 119, 67, 104, 101, 99, 107])
FXQGLR = 4
FYLJUI = "".join(chr(c) for c in [82, 72, 95, 72, 114, 75, 105, 110])
GLRAHE = "".join(chr(c) for c in [71, 101, 99, 107, 111])
GQPLSP = "".join(
    chr(c)
    for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116, 70, 108, 97, 103]
)
GYOUSP = 301
GZUQEX = "".join(chr(c) for c in [80, 53])
HBSKSO = "".join(chr(c) for c in [85, 68, 95, 66, 76, 79, 87, 69, 82])
HECVYY = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        49,
        66,
    ]
)
HEOCTH = "".join(chr(c) for c in [82, 68])
HFTHEC = 300
HIUSOO = "".join(chr(c) for c in [32])
HUOJRJ = "".join(chr(c) for c in [70, 73, 88, 67, 79, 76, 79, 82])
IAMJMA = "".join(
    chr(c)
    for c in [82, 72, 95, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
ICXQIE = "".join(chr(c) for c in [79, 70, 70])
IEFXQG = 14
IFJBIA = "".join(chr(c) for c in [82, 72, 95, 84, 114, 105, 97, 99, 84, 101, 109, 112])
IGYOUS = "".join(
    chr(c) for c in [69, 120, 116, 80, 114, 111, 98, 101, 65, 99, 116, 105, 118, 101]
)
IKFWRK = 260
INEJNI = "".join(chr(c) for c in [76, 73])
IPIVLA = 288
IPOUYN = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        80,
        117,
        114,
        103,
        101,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        85,
        68,
    ]
)
IRYXBQ = "".join(
    chr(c) for c in [82, 72, 95, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
IUSOOQ = "".join(chr(c) for c in [81, 85, 73, 69, 84])
IUXFEF = "".join(chr(c) for c in [78, 69, 87])
IVLASS = 290
JBIAMJ = "".join(chr(c) for c in [82, 72, 95, 67, 111, 109, 109, 69, 114, 114])
JHIUSO = "".join(
    chr(c) for c in [85, 68, 95, 81, 85, 73, 69, 84, 95, 80, 65, 85, 83, 69]
)
JIGYOU = "".join(
    chr(c)
    for c in [
        80,
        114,
        111,
        103,
        69,
        99,
        111,
        110,
        111,
        109,
        121,
        65,
        99,
        116,
        105,
        118,
        101,
    ]
)
JMAOAW = "".join(
    chr(c) for c in [82, 72, 95, 68, 117, 116, 121, 67, 121, 99, 108, 101, 69, 114, 114]
)
JMCBFE = "".join(chr(c) for c in [80, 49])
JNIBXY = 511
JRJHIU = "".join(chr(c) for c in [85, 68, 95, 76, 73, 71, 72, 84, 49, 50, 48])
JTACCP = 312
JUIKFW = "".join(chr(c) for c in [82, 72, 95, 72, 87, 75, 105, 110, 101, 116, 105, 99])
JUTYEK = 274
JVHFTH = 6
JWMNZM = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
JYKLGQ = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
JYMOUN = 268
KCWAON = "".join(
    chr(c)
    for c in [
        86,
        83,
        80,
        51,
        95,
        65,
        118,
        97,
        110,
        116,
        80,
        108,
        97,
        110,
        83,
        112,
        101,
        101,
        100,
    ]
)
KFWRKI = "".join(
    chr(c)
    for c in [82, 72, 95, 70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 101, 100]
)
KLGQPL = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
KPHUOJ = "".join(chr(c) for c in [85, 68, 95, 65, 85, 88, 50])
KQXPIC = "".join(
    chr(c) for c in [67, 117, 114, 114, 101, 110, 116, 72, 101, 97, 116, 101, 114]
)
KSOKPH = 8
KXSJWM = 265
LASSAK = 292
LGQPLS = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
LIUXFE = "".join(chr(c) for c in [83, 84, 65, 82, 84])
LJUIKF = "".join(chr(c) for c in [82, 72, 95, 83, 119, 75, 105, 110, 84, 101, 109, 112])
LKXSJW = "".join(
    chr(c)
    for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 95, 71]
)
LRAHEO = "".join(chr(c) for c in [85, 68, 95, 80, 51])
LSPFTS = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
LSXUJU = "".join(chr(c) for c in [76, 49, 50, 48])
MAOAWB = 258
MCBFEG = 316
MJIGYO = 271
MJMAOA = "".join(chr(c) for c in [82, 72, 95, 76, 111, 119, 70, 108, 111])
MJVHFT = 279
MNZMJI = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
MOUNBL = "".join(chr(c) for c in [77, 69, 68, 73, 85, 77])
NBLKXS = "".join(chr(c) for c in [83, 87, 77, 80, 117, 114, 103, 101])
NPYYLI = 309
NQJYMO = 267
NRSJMC = 305
NZMJIG = "".join(
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
        117,
        114,
        103,
        101,
        65,
        99,
        116,
        105,
        118,
        101,
    ]
)
OAWBSI = "".join(chr(c) for c in [82, 72, 95, 78, 111, 70, 108, 111, 84, 101, 109, 112])
OCTHBS = 10
OKPHUO = 5
ONPYYL = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        70,
        105,
        108,
        116,
        65,
        99,
        116,
        105,
        111,
        110,
    ]
)
OOQNRS = "".join(chr(c) for c in [86, 83, 80, 49, 95, 85, 68, 83, 112, 101, 101, 100])
OQNRSJ = 304
OUNBLK = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
OUSPBW = 277
OUYNQJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114, 79, 84])
PBWJYK = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        68,
        101,
        116,
        101,
        99,
        116,
        105,
        111,
        110,
        69,
        114,
        114,
    ]
)
PFTSIF = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
PHUOJR = "".join(chr(c) for c in [85, 68, 95, 70, 66, 95, 76, 84])
PICXQI = 275
PIPIVL = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        51,
        65,
    ]
)
PIVLAS = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        52,
        65,
    ]
)
PLSPFT = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
POUYNQ = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        67,
        108,
        101,
        97,
        110,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        85,
        68,
    ]
)
PQIPOU = "".join(chr(c) for c in [70, 105, 108, 116, 67, 108, 101, 97, 110])
PYYLIU = "".join(chr(c) for c in [85, 83, 69, 95, 73, 78, 84, 69, 82, 78, 65, 76])
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [67, 80])
QFYLJU = "".join(chr(c) for c in [82, 72, 95, 72, 119, 84, 114, 105, 97, 99, 79, 72])
QGLRAH = 12
QIPOUY = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        67,
        108,
        101,
        97,
        110,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        101,
        100,
    ]
)
QJYMOU = "".join(chr(c) for c in [83, 87, 77, 95, 82, 105, 115, 107])
QNRSJM = "".join(chr(c) for c in [86, 83, 80, 51, 95, 85, 68, 83, 112, 101, 101, 100])
QPLSPF = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
QXPICX = 298
RJHIUS = 1
RKINEJ = "".join(
    chr(c)
    for c in [82, 72, 95, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
RSJMCB = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 101, 110, 115, 105, 116, 121]
)
RYXBQF = "".join(chr(c) for c in [82, 72, 95, 72, 114, 84, 114, 105, 97, 99, 80, 114])
SAKQXP = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        55,
        65,
    ]
)
SIFJBI = 261
SIRYXB = "".join(
    chr(c) for c in [82, 72, 95, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
SJMCBF = 308
SJWMNZ = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111, 119])
SOKPHU = "".join(chr(c) for c in [85, 68, 95, 65, 85, 88, 49])
SOOQNR = 0
SPBWJY = "".join(
    chr(c)
    for c in [
        78,
        111,
        72,
        101,
        97,
        116,
        101,
        114,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        69,
        114,
        114,
    ]
)
SPFTSI = "".join(chr(c) for c in [114, 72, 73, 100])
SSAKQX = 294
SXUJUT = "".join(chr(c) for c in [70, 65, 78])
TACCPQ = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
THBSKS = 9
THECVY = 280
TSIFJB = "".join(chr(c) for c in [82, 72, 95, 87, 97, 116, 101, 114, 84, 101, 109, 112])
TYEKCW = 302
UIKFWR = "".join(
    chr(c)
    for c in [82, 72, 95, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101]
)
UJUTYE = "".join(chr(c) for c in [82, 72, 95, 68, 117, 116, 121, 67, 121, 99, 108, 101])
UOJRJH = "".join(chr(c) for c in [83, 67, 65, 78])
UQEXLS = "".join(chr(c) for c in [66, 76, 79, 87, 69, 82])
USPBWJ = "".join(
    chr(c)
    for c in [
        67,
        111,
        110,
        116,
        97,
        99,
        116,
        111,
        114,
        67,
        111,
        105,
        108,
        70,
        97,
        105,
        108,
        69,
        114,
        114,
    ]
)
UTYEKC = "".join(
    chr(c)
    for c in [
        86,
        83,
        80,
        49,
        95,
        65,
        118,
        97,
        110,
        116,
        80,
        108,
        97,
        110,
        83,
        112,
        101,
        101,
        100,
    ]
)
UXFEFJ = "".join(chr(c) for c in [70, 73, 76, 84, 69, 82])
UYNQJY = "".join(chr(c) for c in [67, 80, 79, 84])
VHFTHE = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101])
VLASSA = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        53,
        65,
    ]
)
VYYPIP = 284
WAONPY = "".join(
    chr(c)
    for c in [
        86,
        83,
        80,
        51,
        95,
        77,
        105,
        110,
        105,
        109,
        117,
        109,
        83,
        112,
        101,
        101,
        100,
    ]
)
WBSIRY = "".join(chr(c) for c in [82, 72, 95, 72, 82, 95, 72, 76])
WJYKLG = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
WMNZMJ = 270
WRKINE = "".join(
    chr(c)
    for c in [
        82,
        72,
        95,
        72,
        101,
        97,
        116,
        101,
        114,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        101,
        100,
    ]
)
XBQFYL = "".join(chr(c) for c in [82, 72, 95, 72, 114, 84, 114, 105, 97, 99, 79, 72])
XLSXUJ = 3
XPICXQ = "".join(chr(c) for c in [85, 68, 95, 80, 49])
XQGLRA = "".join(chr(c) for c in [85, 68, 95, 80, 50])
XQIEFX = "".join(chr(c) for c in [72, 73, 71, 72])
XSJWMN = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
XUJUTY = 7
YEKCWA = "".join(
    chr(c)
    for c in [
        86,
        83,
        80,
        49,
        95,
        77,
        105,
        110,
        105,
        109,
        117,
        109,
        83,
        112,
        101,
        101,
        100,
    ]
)
YKLGQP = 278
YLIUXF = "".join(chr(c) for c in [83, 84, 79, 80])
YLJUIK = "".join(
    chr(c) for c in [82, 72, 95, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
YMOUNB = "".join(chr(c) for c in [78, 79])
YNQJYM = "".join(chr(c) for c in [83, 87, 77, 95, 65, 99, 116, 105, 118, 101])
YOUSPB = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
YPIPIV = 286
YXBQFY = 259
YYLIUX = "".join(chr(c) for c in [73, 68, 76, 69])
YYPIPI = "".join(
    chr(c)
    for c in [
        76,
        101,
        97,
        114,
        110,
        105,
        110,
        103,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        79,
        85,
        84,
        50,
        66,
    ]
)
ZCQBMJ = "".join(chr(c) for c in [72, 111, 117, 114, 115])
ZMJIGY = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 116, 105, 118, 101]
)
ZUQEXL = 315
CBFEGZ = [ICXQIE, XQIEFX, CXQIEF]
KINEJN = []
NEJNIB = [
    JMCBFE,
    BFEGZU,
    FEGZUQ,
    EGZUQE,
    GZUQEX,
    UQEXLS,
    QEXLSX,
    EXLSXU,
    LSXUJU,
    SXUJUT,
    UJUTYE,
    UTYEKC,
    YEKCWA,
    KCWAON,
    WAONPY,
    INEJNI,
]
OJRJHI = [ICXQIE, HUOJRJ, UOJRJH]
QIEFXQ = [ICXQIE, CXQIEF, XQIEFX]
RAHEOC = [ICXQIE, XQIEFX]
SKSOKP = [ICXQIE, BSKSOK]
UNBLKX = [YMOUNB, CXQIEF, MOUNBL, XQIEFX, OUNBLK]
USOOQN = [HIUSOO, IUSOOQ]
XFEFJT = [PYYLIU, YYLIUX, YLIUXF, LIUXFE, IUXFEF, UXFEFJ]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return EFXQGL

    @property
    def begin(self):
        return EJNIBX

    @property
    def end(self):
        return JNIBXY

    @property
    def all_device_keys(self):
        return NEJNIB

    @property
    def user_demand_keys(self):
        return KINEJN

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoBoolStructAccessor(self.struct, BMJVHF, MJVHFT, JVHFTH, None),
            VHFTHE: GeckoByteStructAccessor(self.struct, VHFTHE, HFTHEC, None),
            FTHECV: GeckoWordStructAccessor(self.struct, FTHECV, THECVY, None),
            HECVYY: GeckoWordStructAccessor(self.struct, HECVYY, ECVYYP, None),
            CVYYPI: GeckoWordStructAccessor(self.struct, CVYYPI, VYYPIP, None),
            YYPIPI: GeckoWordStructAccessor(self.struct, YYPIPI, YPIPIV, None),
            PIPIVL: GeckoWordStructAccessor(self.struct, PIPIVL, IPIVLA, None),
            PIVLAS: GeckoWordStructAccessor(self.struct, PIVLAS, IVLASS, None),
            VLASSA: GeckoWordStructAccessor(self.struct, VLASSA, LASSAK, None),
            ASSAKQ: GeckoWordStructAccessor(self.struct, ASSAKQ, SSAKQX, None),
            SAKQXP: GeckoWordStructAccessor(self.struct, SAKQXP, AKQXPI, None),
            KQXPIC: GeckoWordStructAccessor(self.struct, KQXPIC, QXPICX, QBMJVH),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, IEFXQG, QIEFXQ, EFXQGL, FXQGLR, QBMJVH
            ),
            XQGLRA: GeckoEnumStructAccessor(
                self.struct, XQGLRA, PICXQI, QGLRAH, QIEFXQ, EFXQGL, FXQGLR, GLRAHE
            ),
            LRAHEO: GeckoEnumStructAccessor(
                self.struct, LRAHEO, PICXQI, AHEOCT, RAHEOC, EFXQGL, EFXQGL, HEOCTH
            ),
            EOCTHB: GeckoEnumStructAccessor(
                self.struct, EOCTHB, PICXQI, OCTHBS, RAHEOC, EFXQGL, EFXQGL, QBMJVH
            ),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, PICXQI, THBSKS, RAHEOC, EFXQGL, EFXQGL, QBMJVH
            ),
            HBSKSO: GeckoEnumStructAccessor(
                self.struct, HBSKSO, PICXQI, KSOKPH, SKSOKP, EFXQGL, EFXQGL, QBMJVH
            ),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, PICXQI, OKPHUO, SKSOKP, EFXQGL, EFXQGL, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PICXQI, FXQGLR, SKSOKP, EFXQGL, EFXQGL, QBMJVH
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, PICXQI, EFXQGL, OJRJHI, EFXQGL, FXQGLR, QBMJVH
            ),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, PICXQI, RJHIUS, SKSOKP, EFXQGL, EFXQGL, QBMJVH
            ),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, PICXQI, SOOQNR, USOOQN, EFXQGL, EFXQGL, QBMJVH
            ),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, QBMJVH),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, QBMJVH),
            RSJMCB: GeckoByteStructAccessor(self.struct, RSJMCB, SJMCBF, QBMJVH),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, MCBFEG, SOOQNR, CBFEGZ, None, FXQGLR, None
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, MCBFEG, EFXQGL, CBFEGZ, None, FXQGLR, None
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, MCBFEG, FXQGLR, CBFEGZ, None, FXQGLR, None
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, MCBFEG, JVHFTH, CBFEGZ, None, FXQGLR, None
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, SOOQNR, RAHEOC, None, EFXQGL, None
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, ZUQEXL, RJHIUS, RAHEOC, None, EFXQGL, None
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, ZUQEXL, EFXQGL, SKSOKP, None, EFXQGL, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, ZUQEXL, XLSXUJ, SKSOKP, None, EFXQGL, None
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, ZUQEXL, FXQGLR, SKSOKP, None, EFXQGL, None
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, ZUQEXL, XUJUTY, SKSOKP, None, EFXQGL, None
            ),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, None),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, None),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, None),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, None),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, None),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, NPYYLI, None, XFEFJT, None, JVHFTH, QBMJVH
            ),
            FEFJTA: GeckoTimeStructAccessor(self.struct, FEFJTA, EFJTAC, QBMJVH),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, XFEFJT, None, JVHFTH, QBMJVH
            ),
            TACCPQ: GeckoTimeStructAccessor(self.struct, TACCPQ, ACCPQI, QBMJVH),
            CCPQIP: GeckoBoolStructAccessor(self.struct, CCPQIP, CPQIPO, XUJUTY, None),
            PQIPOU: GeckoBoolStructAccessor(self.struct, PQIPOU, CPQIPO, OKPHUO, None),
            QIPOUY: GeckoBoolStructAccessor(self.struct, QIPOUY, CPQIPO, FXQGLR, None),
            IPOUYN: GeckoBoolStructAccessor(self.struct, IPOUYN, MJVHFT, EFXQGL, None),
            POUYNQ: GeckoBoolStructAccessor(self.struct, POUYNQ, MJVHFT, XLSXUJ, None),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, MJVHFT, SOOQNR, None),
            UYNQJY: GeckoBoolStructAccessor(self.struct, UYNQJY, MJVHFT, RJHIUS, None),
            YNQJYM: GeckoByteStructAccessor(self.struct, YNQJYM, NQJYMO, None),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, UNBLKX, None, KSOKPH, None
            ),
            NBLKXS: GeckoBoolStructAccessor(self.struct, NBLKXS, CPQIPO, XLSXUJ, None),
            BLKXSJ: GeckoBoolStructAccessor(self.struct, BLKXSJ, CPQIPO, EFXQGL, None),
            LKXSJW: GeckoTempStructAccessor(self.struct, LKXSJW, KXSJWM, None),
            XSJWMN: GeckoBoolStructAccessor(self.struct, XSJWMN, CPQIPO, RJHIUS, None),
            SJWMNZ: GeckoBoolStructAccessor(self.struct, SJWMNZ, CPQIPO, SOOQNR, None),
            JWMNZM: GeckoBoolStructAccessor(self.struct, JWMNZM, WMNZMJ, XUJUTY, None),
            MNZMJI: GeckoBoolStructAccessor(self.struct, MNZMJI, WMNZMJ, JVHFTH, None),
            NZMJIG: GeckoBoolStructAccessor(self.struct, NZMJIG, WMNZMJ, OKPHUO, None),
            ZMJIGY: GeckoBoolStructAccessor(self.struct, ZMJIGY, MJIGYO, SOOQNR, None),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, MJIGYO, EFXQGL, None),
            IGYOUS: GeckoBoolStructAccessor(self.struct, IGYOUS, GYOUSP, SOOQNR, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, OUSPBW, OKPHUO, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, OUSPBW, FXQGLR, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, OUSPBW, XLSXUJ, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, OUSPBW, EFXQGL, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, OUSPBW, RJHIUS, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, OUSPBW, SOOQNR, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, YKLGQP, XUJUTY, None),
            KLGQPL: GeckoBoolStructAccessor(self.struct, KLGQPL, YKLGQP, JVHFTH, None),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, YKLGQP, OKPHUO, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, YKLGQP, FXQGLR, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, YKLGQP, XLSXUJ, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, YKLGQP, EFXQGL, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, YKLGQP, RJHIUS, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, YKLGQP, SOOQNR, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, MJVHFT, FXQGLR, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, MJVHFT, OKPHUO, None),
            TSIFJB: GeckoTempStructAccessor(self.struct, TSIFJB, SIFJBI, None),
            IFJBIA: GeckoTempStructAccessor(self.struct, IFJBIA, FJBIAM, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, BIAMJM, XUJUTY, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, BIAMJM, XLSXUJ, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, BIAMJM, EFXQGL, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, BIAMJM, SOOQNR, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MAOAWB, XUJUTY, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, MAOAWB, JVHFTH, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, MAOAWB, OKPHUO, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, MAOAWB, FXQGLR, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, MAOAWB, XLSXUJ, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, MAOAWB, EFXQGL, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, MAOAWB, RJHIUS, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, MAOAWB, SOOQNR, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, YXBQFY, XUJUTY, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, YXBQFY, JVHFTH, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, YXBQFY, OKPHUO, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, YXBQFY, FXQGLR, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, YXBQFY, XLSXUJ, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, YXBQFY, EFXQGL, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, YXBQFY, RJHIUS, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, YXBQFY, SOOQNR, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, IKFWRK, FXQGLR, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, IKFWRK, XLSXUJ, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, IKFWRK, EFXQGL, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, IKFWRK, RJHIUS, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, IKFWRK, SOOQNR, None),
        }

#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v63'
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
ACCPQI = "".join(chr(c) for c in [73, 68, 76, 69])
ACMCVD = 342
ACQFFT = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
AFIKJP = "".join(chr(c) for c in [80, 49, 76])
AHEOCT = "".join(chr(c) for c in [85, 100, 80, 51])
AIIDNI = 354
AIVEMV = "".join(chr(c) for c in [67, 70, 71, 50, 55])
AJVDQL = 351
AKQXPI = "".join(chr(c) for c in [65, 76, 76])
AKSTSE = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
AMJMAO = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
AOAWBS = 281
AONPYY = "".join(chr(c) for c in [70, 85, 76, 76])
ATDZXN = 321
AWBSIR = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
AXNCUG = 479
AZMKQT = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
BBEKBD = 452
BDFSRO = 454
BDJQRJ = "".join(chr(c) for c in [75, 54, 48, 48])
BEKBDF = "".join(chr(c) for c in [67, 70, 71, 53])
BHZVOA = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
BIAMJM = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
BJEUTO = 293
BJLOIN = "".join(chr(c) for c in [67, 70, 71, 49, 52])
BLKXSJ = 271
BMJVHF = 256
BQFYLJ = "".join(
    chr(c)
    for c in [
        72,
        80,
        67,
        82,
        101,
        115,
        72,
        101,
        97,
        116,
        101,
        114,
        82,
        101,
        113,
        117,
        101,
        115,
        116,
    ]
)
BQNRXC = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
BQSNQL = 350
BSIRYX = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
BVWVUB = 288
BWJYKL = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
BXIBHZ = 332
BXTIAC = 309
BXYBQS = 284
BYGDSB = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
CBFEGZ = "".join(chr(c) for c in [76, 79, 87])
CCPQIP = "".join(chr(c) for c in [83, 84, 79, 80])
CGETIX = 333
CHWDAF = "".join(chr(c) for c in [83, 79, 117, 116, 49])
CMCVDS = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
CPQIPO = "".join(chr(c) for c in [83, 84, 65, 82, 84])
CQBMJV = 317
CQFFTT = 311
CRHYUA = "".join(chr(c) for c in [76, 73])
CTTGCR = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
CVDSSR = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
CXQIEF = "".join(chr(c) for c in [79, 70, 70])
CYWONF = "".join(chr(c) for c in [67, 70, 71, 51, 48])
CZOLSI = "".join(
    chr(c)
    for c in [
        105,
        110,
        70,
        108,
        111,
        82,
        97,
        116,
        105,
        111,
        77,
        105,
        110,
        105,
        109,
        117,
        109,
    ]
)
DAFIKJ = "".join(chr(c) for c in [80, 49, 72])
DDPMXF = 458
DFSROG = "".join(chr(c) for c in [67, 70, 71, 55])
DGKEAK = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
DJQRJJ = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
DKHTZB = "".join(chr(c) for c in [67, 70, 71, 50])
DMPSCT = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
DNIBXT = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
DNQGVU = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
DPMXFU = "".join(chr(c) for c in [67, 70, 71, 49, 49])
DQLAII = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        84,
        104,
        101,
        114,
        109,
        105,
        115,
        116,
        97,
        110,
        99,
        101,
        69,
        114,
        114,
    ]
)
DRXAIV = 473
DSBDJQ = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
DSSRUR = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
DUBSSU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
DZXNQT = 322
EAKSTS = 328
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 470
EFJTAC = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
EFXQGL = "".join(chr(c) for c in [76, 79])
EGZUQE = "".join(chr(c) for c in [80, 51])
EJNIBX = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
EKBDFS = 453
EKCWAO = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
EKVKZI = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
ELHBQN = 360
ELWUEU = "".join(chr(c) for c in [67, 70, 71, 49, 55])
EMCGET = 331
EMVCYW = 476
EOCTHB = "".join(chr(c) for c in [85, 100, 80, 53])
ETDRXA = 472
ETIXQV = 325
EUHNNX = "".join(chr(c) for c in [67, 70, 71, 49, 57])
EUTOPH = 294
EXLSXU = "".join(chr(c) for c in [66, 76])
EZFETD = "".join(chr(c) for c in [67, 70, 71, 50, 51])
FCRTFM = "".join(chr(c) for c in [54, 52, 75])
FEFJTA = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
FEGZUQ = "".join(chr(c) for c in [80, 50])
FETDRX = "".join(chr(c) for c in [67, 70, 71, 50, 52])
FFTTID = 314
FIKJPU = "".join(chr(c) for c in [80, 50, 72])
FJBIAM = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
FMNHTB = "".join(chr(c) for c in [67, 69])
FSROGM = 455
FTHECV = 319
FTSIFJ = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
FTTIDU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
FUBJLO = "".join(chr(c) for c in [67, 70, 71, 49, 51])
FWRKIN = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
FXQGLR = "".join(chr(c) for c in [72, 73])
FYLJUI = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
FZCZOL = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
FZDGKE = "".join(chr(c) for c in [72, 84, 82])
GDSBDJ = "".join(chr(c) for c in [68, 74, 83, 52])
GETIXQ = "".join(chr(c) for c in [83, 79, 117, 116, 54])
GKEAKS = 327
GLRAHE = 4
GMDDPM = 457
GQPLSP = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
GSELHB = 358
GTYIYW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
GVUNXN = "".join(chr(c) for c in [75, 52, 48, 48])
GYOUSP = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        101,
        100,
        66,
        121,
        69,
        114,
        114,
    ]
)
GZUQEX = "".join(chr(c) for c in [80, 52])
HBQNRX = 361
HBSKSO = "".join(chr(c) for c in [79, 78])
HBVWVU = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
HBXIBH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 80, 52])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 304
HNNXWE = "".join(chr(c) for c in [67, 70, 71, 50, 48])
HTBJEU = 291
HTZBBE = "".join(chr(c) for c in [67, 70, 71, 51])
HUGTYI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
HUOJRJ = 363
HWDAFI = 320
HXEKVK = 283
HZVOAC = 340
IACQFF = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
IAMJMA = 279
IBHZVO = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
IBXTIA = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
IBXYBQ = "".join(
    chr(c)
    for c in [
        72,
        116,
        114,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
ICXQIE = "".join(chr(c) for c in [83, 79, 65, 75])
IDNIBX = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
IDUBSS = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
IEFXQG = 259
IFJBIA = 277
IGYOUS = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        101,
        100,
        66,
        121,
        79,
        84,
    ]
)
IHBXIB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
IIDNIB = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
IJUGSE = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
IKFWRK = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
IKJPUN = "".join(chr(c) for c in [80, 50, 76])
ILXWAJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
INEJNI = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
INELWU = "".join(chr(c) for c in [67, 70, 71, 49, 54])
IPIVLA = "".join(
    chr(c)
    for c in [
        69,
        120,
        101,
        114,
        99,
        105,
        115,
        101,
        68,
        101,
        116,
        101,
        99,
        116,
        101,
        100,
        84,
        121,
        112,
        101,
    ]
)
IPMDMP = 374
IRYXBQ = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
IUSOOQ = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
IUXFEF = 367
IVDNQG = "".join(chr(c) for c in [70, 117, 108, 108])
IVEMVC = 475
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 73, 78, 83, 84, 65, 76, 76, 69, 68])
IYWSKW = 300
JEUTOP = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
JHIUSO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
JIGYOU = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
JJJVYF = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
JJVYFC = 290
JLOINE = 462
JMAOAW = 280
JMCBFE = 261
JNIBXY = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
JPUNRJ = "".join(chr(c) for c in [80, 51, 76])
JQRJJJ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
JRJHIU = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
JTACCP = "".join(
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
JUIKFW = "".join(chr(c) for c in [67, 72, 73, 76, 76])
JUTYEK = 5
JVDQLA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [49, 54, 75])
JWMNZM = 380
JYKLGQ = "".join(chr(c) for c in [78, 79])
JYMOUN = 267
JZTATD = "".join(chr(c) for c in [65, 85, 88])
KBDFSR = "".join(chr(c) for c in [67, 70, 71, 54])
KCWAON = 310
KEAKST = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
KFWRKI = 379
KHTZBB = 450
KINEJN = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
KJPUNR = "".join(chr(c) for c in [80, 51, 72])
KLGQPL = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
KMLOIJ = "".join(chr(c) for c in [75, 49, 48, 48])
KPHUOJ = 307
KQTDKH = 448
KQXPIC = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
KSTSEM = 329
KVKZIL = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
KWIVDN = 316
KXSJWM = 272
KZILXW = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
LAIIDN = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
LASSAK = "".join(chr(c) for c in [84, 82, 69, 65, 68, 77, 73, 76, 76])
LHBQNR = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
LIUXFE = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
LJUIKF = "".join(chr(c) for c in [72, 69, 65, 84])
LKXSJW = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        66,
        114,
        101,
        97,
        107,
        101,
        114,
        73,
        110,
        100,
        101,
        120,
    ]
)
LNMHXE = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
LOIJUG = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
LOINEL = "".join(chr(c) for c in [67, 70, 71, 49, 53])
LRAHEO = "".join(chr(c) for c in [85, 100, 80, 50])
LSIPMD = 373
LSPFTS = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
LSXUJU = "".join(chr(c) for c in [79, 51])
LWUEUH = 465
LXWAJV = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
MAOAWB = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
MCBFEG = "".join(chr(c) for c in [72, 73, 71, 72])
MCGETI = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
MCVDSS = 343
MDDPMX = "".join(chr(c) for c in [67, 70, 71, 49, 48])
MDMPSC = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
MFZDGK = 326
MHXEKV = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
MJIGYO = "".join(chr(c) for c in [80, 117, 114, 103, 101])
MJMAOA = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = "".join(chr(c) for c in [67, 70, 71, 48])
MLOIJU = "".join(chr(c) for c in [75, 56, 48, 48])
MNZMJI = 381
MOUNBL = 268
MPSCTT = "".join(
    chr(c)
    for c in [
        77,
        79,
        68,
        69,
        95,
        49,
        95,
        65,
        78,
        68,
        95,
        72,
        69,
        65,
        84,
        73,
        78,
        71,
        95,
        70,
        65,
        73,
        76,
    ]
)
MVCYWO = "".join(chr(c) for c in [67, 70, 71, 50, 57])
MXFUBJ = "".join(chr(c) for c in [67, 70, 71, 49, 50])
NBLKXS = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
NEJNIB = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
NELWUE = 464
NFZCZO = "".join(
    chr(c)
    for c in [
        105,
        110,
        70,
        108,
        111,
        80,
        114,
        101,
        115,
        115,
        117,
        114,
        101,
        83,
        119,
        68,
        101,
        116,
        101,
        99,
        116,
        101,
        100,
    ]
)
NHTBJE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
NIBXTI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
NKMLOI = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
NMHXEK = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
NNXWEE = 468
NPYYLI = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
NQGVUN = 357
NQJYMO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
NQLNMH = 383
NQTMFZ = "".join(chr(c) for c in [83, 79, 117, 116, 53])
NRJZTA = "".join(chr(c) for c in [66, 76, 79])
NRSJMC = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
NRXCHW = "".join(chr(c) for c in [45, 45, 45])
NXNKML = "".join(chr(c) for c in [75, 52])
NXWEEZ = "".join(chr(c) for c in [67, 70, 71, 50, 49])
NZMJIG = "".join(chr(c) for c in [67, 108, 101, 97, 110])
OACMCV = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
OAWBSI = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
OCTHBS = 258
OGMDDP = "".join(chr(c) for c in [67, 70, 71, 57])
OIHBXI = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
OIJUGS = "".join(chr(c) for c in [75, 51, 48, 48])
OINELW = 463
OJRJHI = 370
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 105])
OLSIPM = "".join(
    chr(c)
    for c in [
        105,
        110,
        70,
        108,
        111,
        82,
        97,
        116,
        105,
        111,
        77,
        97,
        120,
        105,
        109,
        117,
        109,
    ]
)
ONFZCZ = 479
OOQNRS = 306
OPHUGT = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
OQNRSJ = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
OUNBLK = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        67,
        111,
        110,
        102,
        105,
        103,
        73,
        110,
        100,
        101,
        120,
    ]
)
OUSPBW = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
OUYNQJ = 264
PBWJYK = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
PFTSIF = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
PHUGTY = 296
PHUOJR = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
PICXQI = "".join(chr(c) for c in [68, 82, 65, 73, 78])
PIVLAS = 385
PLSPFT = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
PMDMPS = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
PMXFUB = 459
POUYNQ = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
PQIPOU = "".join(chr(c) for c in [78, 69, 87])
PSCTTG = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
PUNRJZ = "".join(chr(c) for c in [80, 52, 72])
PYYLIU = 364
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QFFTTI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
QFYLJU = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
QGLRAH = 0
QGVUNX = "".join(chr(c) for c in [75, 50, 48, 48])
QIEFXQ = "".join(chr(c) for c in [85, 100, 80, 49])
QIPOUY = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
QJYMOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
QLAIID = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        65,
        109,
        98,
        105,
        97,
        110,
        116,
        79,
        72,
        76,
        101,
        118,
        101,
        108,
        50,
    ]
)
QLNMHX = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
QNRSJM = 362
QNRXCH = 376
QPLSPF = 353
QRJJJV = "".join(chr(c) for c in [105, 110, 89, 84])
QSNQLN = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        72,
        116,
        114,
        50,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
QTDKHT = "".join(chr(c) for c in [67, 70, 71, 49])
QTMFZD = 324
QVXOIH = "".join(chr(c) for c in [83, 79, 117, 116, 56])
QXPICX = 257
RAHEOC = 2
RAZMKQ = 347
RJHIUS = 303
RJZTAT = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
RKINEJ = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
ROGMDD = 456
RSJMCB = 369
RTFMNH = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
RURAZM = 346
RXAIVE = "".join(chr(c) for c in [67, 70, 71, 50, 54])
RXCHWD = "".join(chr(c) for c in [82, 69, 83, 69, 84])
RYXBQF = 384
SAKQXP = 386
SBDJQR = "".join(chr(c) for c in [105, 110, 88, 77])
SELHBQ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
SEMCGE = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
SIFJBI = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
SIPMDM = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
SIRYXB = 377
SJMCBF = "".join(chr(c) for c in [80, 49])
SJWMNZ = "".join(
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
SKSOKP = 1
SKWIVD = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
SNQLNM = "".join(
    chr(c)
    for c in [
        83,
        105,
        108,
        101,
        110,
        116,
        77,
        111,
        100,
        101,
        65,
        99,
        116,
        105,
        118,
        101,
    ]
)
SOKPHU = 308
SOOQNR = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
SPBWJY = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
SPFTSI = 355
SROGMD = "".join(chr(c) for c in [67, 70, 71, 56])
SRURAZ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
SSAKQX = "".join(
    chr(c)
    for c in [
        69,
        120,
        101,
        114,
        99,
        105,
        115,
        101,
        73,
        110,
        116,
        101,
        110,
        115,
        105,
        116,
        121,
    ]
)
SSRURA = 345
SSUHBV = 285
STSEMC = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
SXUJUT = 3
TACCPQ = 263
TATDZX = "".join(chr(c) for c in [83, 79, 117, 116, 50])
TBJEUT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
TDKHTZ = 449
TDRXAI = "".join(chr(c) for c in [67, 70, 71, 50, 53])
TDZXNQ = "".join(chr(c) for c in [83, 79, 117, 116, 51])
TFMNHT = "".join(chr(c) for c in [85, 76])
TGCRHY = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
THBSKS = "".join(chr(c) for c in [85, 100, 66, 76])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIDUBS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
TIXQVX = "".join(chr(c) for c in [70, 97, 110])
TMFZDG = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
TOPHUG = 295
TSEMCG = 330
TSIFJB = 275
TTGCRH = 375
TTIDUB = 315
TYEKCW = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
TYIYWS = 299
TZBBEK = 451
UAXNCU = 256
UBJLOI = 461
UBSSUH = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
UBYGDS = "".join(chr(c) for c in [105, 110, 88, 69])
UEUHNN = 466
UGSELH = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
UGTYIY = 297
UHBVWV = 287
UHNNXW = 467
UJUTYE = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
UNBLKX = 270
UNRJZT = "".join(chr(c) for c in [80, 52, 76])
UNXNKM = "".join(chr(c) for c in [75, 56])
UOJRJH = "".join(chr(c) for c in [85, 100, 65, 117, 120])
UQEXLS = 260
URAZMK = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
USOOQN = 305
USPBWJ = 282
UTOPHU = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
UTYEKC = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
UXFEFJ = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
UYNQJY = "".join(
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
        68,
        117,
        114,
        80,
        101,
        114,
        68,
        97,
        121,
    ]
)
VCYWON = 477
VDQLAI = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        84,
        104,
        101,
        114,
        109,
        70,
        117,
        115,
        101,
        69,
        114,
        114,
    ]
)
VDSSRU = 344
VEMVCY = "".join(chr(c) for c in [67, 70, 71, 50, 56])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
VLASSA = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
VOACMC = 341
VUBYGD = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
VUNXNK = "".join(chr(c) for c in [75, 56, 53])
VWVUBY = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
VXOIHB = "".join(chr(c) for c in [83, 79, 117, 116, 57])
VYFCRT = "".join(chr(c) for c in [51, 50, 75])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
WAONPY = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
WBSIRY = 352
WDAFIK = "".join(chr(c) for c in [78, 65])
WEEZFE = "".join(chr(c) for c in [67, 70, 71, 50, 50])
WIVDNQ = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
WJYKLG = 313
WMNZMJ = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
WONFZC = "".join(chr(c) for c in [67, 70, 71, 51, 49])
WRKINE = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
WSKWIV = 301
WUEUHN = "".join(chr(c) for c in [67, 70, 71, 49, 56])
WVUBYG = 289
XAIVEM = 474
XBQFYL = 378
XEKVKZ = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
XFEFJT = 262
XFUBJL = 460
XLSXUJ = "".join(chr(c) for c in [67, 80])
XNKMLO = "".join(chr(c) for c in [75, 53])
XNQTMF = 323
XOIHBX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
XPICXQ = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
XQVXOI = "".join(chr(c) for c in [83, 79, 117, 116, 55])
XSJWMN = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
XTIACQ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
XUJUTY = "".join(chr(c) for c in [76, 49, 50, 48])
XWAJVD = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
XWEEZF = 469
XYBQSN = "".join(
    chr(c)
    for c in [
        72,
        116,
        114,
        50,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
YBQSNQ = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        72,
        116,
        114,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
YEKCWA = 7
YFCRTF = "".join(chr(c) for c in [52, 56, 75])
YGDSBD = "".join(chr(c) for c in [77, 73, 65])
YIYWSK = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
YKLGQP = "".join(chr(c) for c in [77, 69, 68])
YLIUXF = 365
YLJUIK = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
YMOUNB = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
YNQJYM = 266
YOUSPB = "".join(chr(c) for c in [67, 80, 79, 84])
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YUAXNC = 63
YWONFZ = 478
YWSKWI = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
YXBQFY = "".join(
    chr(c)
    for c in [
        67,
        111,
        111,
        108,
        90,
        111,
        110,
        101,
        68,
        101,
        116,
        101,
        99,
        116,
        101,
        100,
    ]
)
YYLIUX = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = "".join(chr(c) for c in [67, 70, 71, 52])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = 371
ZFETDR = 471
ZILXWA = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
ZMJIGY = 273
ZMKQTD = 348
ZOLSIP = 372
ZUQEXL = "".join(chr(c) for c in [80, 53])
ZVOACM = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
ZXNQTM = "".join(chr(c) for c in [83, 79, 117, 116, 52])
ASSAKQ = [IVLASS, VLASSA, LASSAK]
BFEGZU = [CXQIEF, MCBFEG, CBFEGZ]
BSKSOK = [CXQIEF, HBSKSO]
CRTFMN = [JVYFCR, VYFCRT, YFCRTF, FCRTFM]
CTHBSK = [CXQIEF, FXQGLR]
FJTACC = [FEFJTA, EFJTAC]
GCRHYU = []
HYUAXN = [
    QIEFXQ,
    LRAHEO,
    AHEOCT,
    HEOCTH,
    EOCTHB,
    THBSKS,
    KSOKPH,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    JRJHIU,
    JHIUSO,
    IUSOOQ,
    SOOQNR,
    OQNRSJ,
    NRSJMC,
]
IPOUYN = [ACCPQI, CCPQIP, CPQIPO, PQIPOU, QIPOUY]
IXQVXO = [
    WDAFIK,
    DAFIKJ,
    AFIKJP,
    FIKJPU,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    ZUQEXL,
    NRJZTA,
    XLSXUJ,
    LSXUJU,
    XUJUTY,
    HECVYY,
    HECVYY,
    TIXQVX,
    HECVYY,
    HECVYY,
    RJZTAT,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    TYEKCW,
    JZTATD,
]
JBIAMJ = [HECVYY, FJBIAM, FJBIAM, FJBIAM]
JUGSEL = [
    QGVUNX,
    GVUNXN,
    VUNXNK,
    UNXNKM,
    NXNKML,
    XNKMLO,
    NKMLOI,
    KMLOIJ,
    MLOIJU,
    HECVYY,
    HECVYY,
    HECVYY,
    LOIJUG,
    OIJUGS,
    IJUGSE,
]
LGQPLS = [JYKLGQ, EFXQGL, YKLGQP, FXQGLR, KLGQPL]
MNHTBJ = [TFMNHT, FMNHTB]
NIBXYB = [
    ACCPQI,
    FWRKIN,
    WRKINE,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    RKINEJ,
    KINEJN,
    INEJNI,
    NEJNIB,
    EJNIBX,
    JNIBXY,
]
ONPYYL = [CWAONP, WAONPY, AONPYY]
PIPIVL = [
    THECVY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    ECVYYP,
    CVYYPI,
    VYYPIP,
    YYPIPI,
    HECVYY,
    YPIPIV,
]
QEXLSX = [CXQIEF, MCBFEG]
RHYUAX = [
    SJMCBF,
    FEGZUQ,
    EGZUQE,
    GZUQEX,
    ZUQEXL,
    EXLSXU,
    XLSXUJ,
    LSXUJU,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    TYEKCW,
    EKCWAO,
    NPYYLI,
    YYLIUX,
    LIUXFE,
    CRHYUA,
]
RJJJVY = [
    VUBYGD,
    UBYGDS,
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
]
SCTTGC = [PMDMPS, MDMPSC, DMPSCT, MPSCTT, PSCTTG]
TIACQF = [HECVYY, XTIACQ, XTIACQ, XTIACQ]
UIKFWR = [LJUIKF, JUIKFW]
VDNQGV = [WIVDNQ, IVDNQG]
XCHWDA = [NRXCHW, RXCHWD]
XIBHZV = [
    WDAFIK,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    XLSXUJ,
]
XQGLRA = [CXQIEF, EFXQGL, FXQGLR]
XQIEFX = [XPICXQ, PICXQI, ICXQIE, CXQIEF]
ZDGKEA = [
    WDAFIK,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    FZDGKE,
]
ZTATDZ = [
    WDAFIK,
    DAFIKJ,
    AFIKJP,
    FIKJPU,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    ZUQEXL,
    NRJZTA,
    XLSXUJ,
    LSXUJU,
    XUJUTY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    RJZTAT,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    TYEKCW,
    JZTATD,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return YUAXNC

    @property
    def begin(self):
        return UAXNCU

    @property
    def end(self):
        return AXNCUG

    @property
    def all_device_keys(self):
        return RHYUAX

    @property
    def user_demand_keys(self):
        return HYUAXN

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoTempStructAccessor(self.struct, ZCQBMJ, CQBMJV, None),
            QBMJVH: GeckoByteStructAccessor(self.struct, QBMJVH, BMJVHF, None),
            MJVHFT: GeckoBoolStructAccessor(self.struct, MJVHFT, JVHFTH, VHFTHE, None),
            HFTHEC: GeckoEnumStructAccessor(
                self.struct, HFTHEC, FTHECV, None, PIPIVL, None, None, None
            ),
            IPIVLA: GeckoEnumStructAccessor(
                self.struct, IPIVLA, PIVLAS, None, ASSAKQ, None, None, None
            ),
            SSAKQX: GeckoByteStructAccessor(self.struct, SSAKQX, SAKQXP, AKQXPI),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, XQIEFX, None, None, AKQXPI
            ),
            QIEFXQ: GeckoEnumStructAccessor(
                self.struct, QIEFXQ, IEFXQG, QGLRAH, XQGLRA, None, GLRAHE, AKQXPI
            ),
            LRAHEO: GeckoEnumStructAccessor(
                self.struct, LRAHEO, IEFXQG, RAHEOC, XQGLRA, None, GLRAHE, AKQXPI
            ),
            AHEOCT: GeckoEnumStructAccessor(
                self.struct, AHEOCT, IEFXQG, GLRAHE, XQGLRA, None, GLRAHE, AKQXPI
            ),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, IEFXQG, VHFTHE, XQGLRA, None, GLRAHE, AKQXPI
            ),
            EOCTHB: GeckoEnumStructAccessor(
                self.struct, EOCTHB, OCTHBS, QGLRAH, CTHBSK, None, RAHEOC, AKQXPI
            ),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, OCTHBS, SKSOKP, BSKSOK, None, RAHEOC, AKQXPI
            ),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, BSKSOK, None, None, AKQXPI
            ),
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, None, CTHBSK, None, None, AKQXPI
            ),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, None, BSKSOK, None, None, AKQXPI
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, None, BSKSOK, None, None, AKQXPI
            ),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, AKQXPI),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, AKQXPI),
            IUSOOQ: GeckoByteStructAccessor(self.struct, IUSOOQ, USOOQN, AKQXPI),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, AKQXPI),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, AKQXPI),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, AKQXPI),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, QGLRAH, BFEGZU, None, GLRAHE, None
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, JMCBFE, RAHEOC, BFEGZU, None, GLRAHE, None
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, JMCBFE, GLRAHE, BFEGZU, None, GLRAHE, None
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, JMCBFE, VHFTHE, BFEGZU, None, GLRAHE, None
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, UQEXLS, QGLRAH, QEXLSX, None, RAHEOC, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, UQEXLS, SKSOKP, BSKSOK, None, RAHEOC, None
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, UQEXLS, RAHEOC, BSKSOK, None, RAHEOC, None
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, UQEXLS, SXUJUT, BSKSOK, None, RAHEOC, None
            ),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UQEXLS, GLRAHE, BSKSOK, None, RAHEOC, None
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, UQEXLS, JUTYEK, BSKSOK, None, RAHEOC, None
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, UQEXLS, VHFTHE, BSKSOK, None, RAHEOC, None
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, UQEXLS, YEKCWA, BSKSOK, None, RAHEOC, None
            ),
            EKCWAO: GeckoEnumStructAccessor(
                self.struct, EKCWAO, KCWAON, None, ONPYYL, None, None, AKQXPI
            ),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, ONPYYL, None, None, None
            ),
            YYLIUX: GeckoWordStructAccessor(self.struct, YYLIUX, YLIUXF, None),
            LIUXFE: GeckoWordStructAccessor(self.struct, LIUXFE, IUXFEF, AKQXPI),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, QGLRAH, FJTACC, None, RAHEOC, AKQXPI
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, None, IPOUYN, None, None, AKQXPI
            ),
            POUYNQ: GeckoTimeStructAccessor(self.struct, POUYNQ, OUYNQJ, AKQXPI),
            UYNQJY: GeckoByteStructAccessor(self.struct, UYNQJY, YNQJYM, AKQXPI),
            NQJYMO: GeckoEnumStructAccessor(
                self.struct, NQJYMO, XFEFJT, RAHEOC, FJTACC, None, RAHEOC, AKQXPI
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, JYMOUN, None, IPOUYN, None, None, AKQXPI
            ),
            YMOUNB: GeckoTimeStructAccessor(self.struct, YMOUNB, MOUNBL, AKQXPI),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, AKQXPI),
            NBLKXS: GeckoByteStructAccessor(self.struct, NBLKXS, BLKXSJ, AKQXPI),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, AKQXPI),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, XFEFJT, SKSOKP, FJTACC, None, RAHEOC, AKQXPI
            ),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, IPOUYN, None, None, AKQXPI
            ),
            WMNZMJ: GeckoTimeStructAccessor(self.struct, WMNZMJ, MNZMJI, AKQXPI),
            NZMJIG: GeckoBoolStructAccessor(self.struct, NZMJIG, ZMJIGY, QGLRAH, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, ZMJIGY, RAHEOC, None),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, ZMJIGY, SXUJUT, None),
            IGYOUS: GeckoBoolStructAccessor(self.struct, IGYOUS, ZMJIGY, GLRAHE, None),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, ZMJIGY, JUTYEK, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, JVHFTH, RAHEOC, None),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, USPBWJ, SXUJUT, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, USPBWJ, JUTYEK, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, USPBWJ, VHFTHE, None),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, LGQPLS, None, None, None
            ),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, QPLSPF, JUTYEK, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, QPLSPF, VHFTHE, None),
            LSPFTS: GeckoWordStructAccessor(self.struct, LSPFTS, SPFTSI, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, JVHFTH, SKSOKP, None),
            FTSIFJ: GeckoTempStructAccessor(self.struct, FTSIFJ, TSIFJB, None),
            SIFJBI: GeckoTempStructAccessor(self.struct, SIFJBI, IFJBIA, None),
            FJBIAM: GeckoEnumStructAccessor(
                self.struct, FJBIAM, UQEXLS, JUTYEK, JBIAMJ, None, GLRAHE, None
            ),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, RAHEOC, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, IAMJMA, VHFTHE, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, RAHEOC, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, AOAWBS, SKSOKP, None),
            OAWBSI: GeckoBoolStructAccessor(
                self.struct, OAWBSI, AOAWBS, RAHEOC, AKQXPI
            ),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, WBSIRY, SKSOKP, None),
            BSIRYX: GeckoByteStructAccessor(self.struct, BSIRYX, SIRYXB, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, RYXBQF, QGLRAH, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, XBQFYL, QGLRAH, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, XBQFYL, GLRAHE, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, XBQFYL, JUTYEK, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, XBQFYL, VHFTHE, None),
            YLJUIK: GeckoEnumStructAccessor(
                self.struct, YLJUIK, XBQFYL, YEKCWA, UIKFWR, None, RAHEOC, AKQXPI
            ),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, None, NIBXYB, None, None, None
            ),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BXYBQS, QGLRAH, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, BXYBQS, SKSOKP, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, BQSNQL, QGLRAH, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, BQSNQL, SKSOKP, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, NQLNMH, QGLRAH, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, JVHFTH, SXUJUT, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, USPBWJ, QGLRAH, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, USPBWJ, SKSOKP, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, HXEKVK, RAHEOC, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, HXEKVK, SXUJUT, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, BXYBQS, SXUJUT, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, BXYBQS, GLRAHE, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, BXYBQS, JUTYEK, None),
            KZILXW: GeckoBoolStructAccessor(self.struct, KZILXW, BXYBQS, VHFTHE, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, BQSNQL, SXUJUT, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, BQSNQL, GLRAHE, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, BQSNQL, JUTYEK, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, BQSNQL, VHFTHE, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, AJVDQL, RAHEOC, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, AJVDQL, SXUJUT, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, WBSIRY, SXUJUT, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, QPLSPF, QGLRAH, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, QPLSPF, SKSOKP, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, AIIDNI, QGLRAH, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, JMAOAW, QGLRAH, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, HXEKVK, QGLRAH, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, HXEKVK, SKSOKP, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, HXEKVK, GLRAHE, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, BXTIAC, QGLRAH, None),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, BXTIAC, SKSOKP, TIACQF, None, GLRAHE, None
            ),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, BXTIAC, SXUJUT, None),
            ACQFFT: GeckoWordStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, FFTTID, QGLRAH, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, TTIDUB, QGLRAH, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, TTIDUB, SKSOKP, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, AJVDQL, QGLRAH, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, AJVDQL, SKSOKP, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, AJVDQL, GLRAHE, None),
            BSSUHB: GeckoWordStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, None),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoEnumStructAccessor(
                self.struct, VWVUBY, WVUBYG, None, RJJJVY, None, None, None
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, JJVYFC, QGLRAH, CRTFMN, None, GLRAHE, None
            ),
            RTFMNH: GeckoEnumStructAccessor(
                self.struct, RTFMNH, JJVYFC, RAHEOC, MNHTBJ, None, RAHEOC, None
            ),
            NHTBJE: GeckoWordStructAccessor(self.struct, NHTBJE, HTBJEU, None),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, None),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, None),
            UTOPHU: GeckoByteStructAccessor(self.struct, UTOPHU, TOPHUG, None),
            OPHUGT: GeckoByteStructAccessor(self.struct, OPHUGT, PHUGTY, None),
            HUGTYI: GeckoWordStructAccessor(self.struct, HUGTYI, UGTYIY, None),
            GTYIYW: GeckoByteStructAccessor(self.struct, GTYIYW, TYIYWS, None),
            YIYWSK: GeckoByteStructAccessor(self.struct, YIYWSK, IYWSKW, None),
            YWSKWI: GeckoWordStructAccessor(self.struct, YWSKWI, WSKWIV, None),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, VDNQGV, None, RAHEOC, AKQXPI
            ),
            DNQGVU: GeckoEnumStructAccessor(
                self.struct, DNQGVU, NQGVUN, None, JUGSEL, None, None, None
            ),
            UGSELH: GeckoWordStructAccessor(self.struct, UGSELH, GSELHB, None),
            SELHBQ: GeckoByteStructAccessor(self.struct, SELHBQ, ELHBQN, None),
            LHBQNR: GeckoByteStructAccessor(self.struct, LHBQNR, HBQNRX, None),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, QNRXCH, None, XCHWDA, None, None, AKQXPI
            ),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, HWDAFI, None, ZTATDZ, None, None, AKQXPI
            ),
            TATDZX: GeckoEnumStructAccessor(
                self.struct, TATDZX, ATDZXN, None, ZTATDZ, None, None, AKQXPI
            ),
            TDZXNQ: GeckoEnumStructAccessor(
                self.struct, TDZXNQ, DZXNQT, None, ZTATDZ, None, None, AKQXPI
            ),
            ZXNQTM: GeckoEnumStructAccessor(
                self.struct, ZXNQTM, XNQTMF, None, ZTATDZ, None, None, AKQXPI
            ),
            NQTMFZ: GeckoEnumStructAccessor(
                self.struct, NQTMFZ, QTMFZD, None, ZTATDZ, None, None, AKQXPI
            ),
            TMFZDG: GeckoEnumStructAccessor(
                self.struct, TMFZDG, MFZDGK, None, ZDGKEA, None, None, AKQXPI
            ),
            DGKEAK: GeckoByteStructAccessor(self.struct, DGKEAK, GKEAKS, AKQXPI),
            KEAKST: GeckoByteStructAccessor(self.struct, KEAKST, EAKSTS, AKQXPI),
            AKSTSE: GeckoByteStructAccessor(self.struct, AKSTSE, KSTSEM, AKQXPI),
            STSEMC: GeckoByteStructAccessor(self.struct, STSEMC, TSEMCG, AKQXPI),
            SEMCGE: GeckoByteStructAccessor(self.struct, SEMCGE, EMCGET, AKQXPI),
            MCGETI: GeckoByteStructAccessor(self.struct, MCGETI, CGETIX, AKQXPI),
            GETIXQ: GeckoEnumStructAccessor(
                self.struct, GETIXQ, ETIXQV, None, IXQVXO, None, None, AKQXPI
            ),
            XQVXOI: GeckoEnumStructAccessor(
                self.struct, XQVXOI, MFZDGK, None, IXQVXO, None, None, AKQXPI
            ),
            QVXOIH: GeckoEnumStructAccessor(
                self.struct, QVXOIH, GKEAKS, None, IXQVXO, None, None, AKQXPI
            ),
            VXOIHB: GeckoEnumStructAccessor(
                self.struct, VXOIHB, EAKSTS, None, IXQVXO, None, None, AKQXPI
            ),
            XOIHBX: GeckoEnumStructAccessor(
                self.struct, XOIHBX, KSTSEM, None, IXQVXO, None, None, AKQXPI
            ),
            OIHBXI: GeckoEnumStructAccessor(
                self.struct, OIHBXI, TSEMCG, None, IXQVXO, None, None, AKQXPI
            ),
            IHBXIB: GeckoEnumStructAccessor(
                self.struct, IHBXIB, EMCGET, None, IXQVXO, None, None, AKQXPI
            ),
            HBXIBH: GeckoEnumStructAccessor(
                self.struct, HBXIBH, BXIBHZ, None, XIBHZV, None, None, AKQXPI
            ),
            IBHZVO: GeckoEnumStructAccessor(
                self.struct, IBHZVO, CGETIX, None, XIBHZV, None, None, AKQXPI
            ),
            BHZVOA: GeckoByteStructAccessor(self.struct, BHZVOA, HZVOAC, AKQXPI),
            ZVOACM: GeckoByteStructAccessor(self.struct, ZVOACM, VOACMC, AKQXPI),
            OACMCV: GeckoByteStructAccessor(self.struct, OACMCV, ACMCVD, AKQXPI),
            CMCVDS: GeckoByteStructAccessor(self.struct, CMCVDS, MCVDSS, AKQXPI),
            CVDSSR: GeckoByteStructAccessor(self.struct, CVDSSR, VDSSRU, AKQXPI),
            DSSRUR: GeckoByteStructAccessor(self.struct, DSSRUR, SSRURA, AKQXPI),
            SRURAZ: GeckoByteStructAccessor(self.struct, SRURAZ, RURAZM, AKQXPI),
            URAZMK: GeckoByteStructAccessor(self.struct, URAZMK, RAZMKQ, AKQXPI),
            AZMKQT: GeckoByteStructAccessor(self.struct, AZMKQT, ZMKQTD, AKQXPI),
            NFZCZO: GeckoBoolStructAccessor(self.struct, NFZCZO, JVHFTH, JUTYEK, None),
            FZCZOL: GeckoByteStructAccessor(self.struct, FZCZOL, ZCZOLS, AKQXPI),
            CZOLSI: GeckoByteStructAccessor(self.struct, CZOLSI, ZOLSIP, AKQXPI),
            OLSIPM: GeckoByteStructAccessor(self.struct, OLSIPM, LSIPMD, AKQXPI),
            SIPMDM: GeckoEnumStructAccessor(
                self.struct, SIPMDM, IPMDMP, None, SCTTGC, None, None, AKQXPI
            ),
            CTTGCR: GeckoBoolStructAccessor(
                self.struct, CTTGCR, TTGCRH, QGLRAH, AKQXPI
            ),
            TGCRHY: GeckoBoolStructAccessor(self.struct, TGCRHY, QNRXCH, QGLRAH, None),
        }

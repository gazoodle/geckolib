#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v64'
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
ACMCVD = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
ACQFFT = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
AFIKJP = 320
AIIDNI = "".join(
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
AIVEMV = 473
AJVDQL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
AKQXPI = "".join(chr(c) for c in [65, 76, 76])
AKSTSE = 327
AOAWBS = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
AONPYY = 310
ATDZXN = "".join(chr(c) for c in [65, 85, 88])
AWBSIR = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
AZMKQT = 346
BBEKBD = "".join(chr(c) for c in [67, 70, 71, 51])
BDFSRO = "".join(chr(c) for c in [67, 70, 71, 53])
BDJQRJ = "".join(chr(c) for c in [68, 74, 83, 52])
BEKBDF = 451
BFEGZU = 261
BHZVOA = 332
BIAMJM = 277
BJEUTO = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
BJLOIN = 460
BLKXSJ = "".join(
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
BMJVHF = 256
BQFYLJ = 384
BQNRXC = 360
BQSNQL = 284
BSIRYX = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
BSKSOK = 258
BSSUHB = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
BVWVUB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
BWJYKL = 282
BXIBHZ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
BXTIAC = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
BXYBQS = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
BYGDSB = 289
CBFEGZ = "".join(chr(c) for c in [80, 49])
CCPQIP = "".join(
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
CGETIX = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
CHWDAF = "".join(chr(c) for c in [45, 45, 45])
CMCVDS = 341
CPQIPO = 263
CQBMJV = 317
CRHYUA = 375
CRTFMN = "".join(chr(c) for c in [51, 50, 75])
CTHBSK = "".join(chr(c) for c in [85, 100, 80, 51])
CTTGCR = "".join(
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
CUGUCY = 479
CVDSSR = 342
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = 7
CXQIEF = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
CYWONF = 476
CZOLSI = "".join(
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
DAFIKJ = "".join(chr(c) for c in [83, 79, 117, 116, 49])
DDPMXF = "".join(chr(c) for c in [67, 70, 71, 57])
DFSROG = 453
DGKEAK = 326
DJQRJJ = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
DKHTZB = 448
DMPSCT = 374
DNIBXT = 354
DNQGVU = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
DPMXFU = 457
DQLAII = 351
DRXAIV = "".join(chr(c) for c in [67, 70, 71, 50, 52])
DSBDJQ = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
DSSRUR = 343
DUBSSU = 315
DZXNQT = "".join(chr(c) for c in [83, 79, 117, 116, 50])
EAKSTS = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = "".join(chr(c) for c in [67, 70, 71, 50, 49])
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
EFXQGL = "".join(chr(c) for c in [83, 79, 65, 75])
EGZUQE = "".join(chr(c) for c in [76, 79, 87])
EJNIBX = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
EKBDFS = "".join(chr(c) for c in [67, 70, 71, 52])
EKCWAO = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
EKVKZI = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
ELHBQN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
ELWUEU = 463
EMCGET = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
EMVCYW = "".join(chr(c) for c in [67, 70, 71, 50, 55])
EOCTHB = "".join(chr(c) for c in [85, 100, 80, 50])
ETDRXA = "".join(chr(c) for c in [67, 70, 71, 50, 51])
ETIXQV = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
EUHNNX = 465
EUTOPH = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
EXLSXU = "".join(chr(c) for c in [80, 53])
EZFETD = 469
FCRTFM = "".join(chr(c) for c in [49, 54, 75])
FEFJTA = 367
FEGZUQ = "".join(chr(c) for c in [72, 73, 71, 72])
FETDRX = 470
FFTTID = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
FIKJPU = "".join(chr(c) for c in [78, 65])
FJBIAM = 275
FJTACC = 262
FSROGM = "".join(chr(c) for c in [67, 70, 71, 54])
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
FTTIDU = 311
FUBJLO = 459
FXQGLR = "".join(chr(c) for c in [79, 70, 70])
FYLJUI = 378
FZCZOL = "".join(chr(c) for c in [67, 70, 71, 51, 49])
FZDGKE = 324
GCRHYU = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
GDSBDJ = "".join(chr(c) for c in [105, 110, 88, 69])
GETIXQ = 331
GKEAKS = "".join(chr(c) for c in [72, 84, 82])
GLRAHE = 259
GMDDPM = "".join(chr(c) for c in [67, 70, 71, 56])
GQPLSP = "".join(chr(c) for c in [77, 69, 68])
GSELHB = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
GTYIYW = 296
GVUNXN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
GYOUSP = "".join(chr(c) for c in [80, 117, 114, 103, 101])
HBQNRX = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
HBSKSO = "".join(chr(c) for c in [85, 100, 80, 53])
HBVWVU = 285
HBXIBH = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = 4
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
HNNXWE = 466
HTBJEU = "".join(chr(c) for c in [67, 69])
HTZBBE = 449
HUGTYI = 295
HUOJRJ = "".join(chr(c) for c in [85, 100, 76, 105])
HWDAFI = "".join(chr(c) for c in [82, 69, 83, 69, 84])
HXEKVK = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
IACQFF = 309
IAMJMA = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
IBHZVO = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
IBXTIA = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
IBXYBQ = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
ICXQIE = 1
IDNIBX = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
IDUBSS = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
IEFXQG = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IFJBIA = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
IGYOUS = 273
IHBXIB = "".join(chr(c) for c in [83, 79, 117, 116, 57])
IIDNIB = "".join(
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
IJUGSE = "".join(chr(c) for c in [75, 56, 48, 48])
IKFWRK = "".join(chr(c) for c in [72, 69, 65, 84])
IKJPUN = "".join(chr(c) for c in [80, 49, 72])
ILXWAJ = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
INEJNI = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
INELWU = 462
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
IPMDMP = "".join(
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
IPOUYN = "".join(chr(c) for c in [83, 84, 65, 82, 84])
IRYXBQ = 352
IUSOOQ = 303
IUXFEF = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
IVDNQG = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
IVEMVC = "".join(chr(c) for c in [67, 70, 71, 50, 54])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 73, 78, 83, 84, 65, 76, 76, 69, 68])
IXQVXO = "".join(chr(c) for c in [83, 79, 117, 116, 54])
IYWSKW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
JBIAMJ = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
JEUTOP = 291
JHIUSO = 370
JIGYOU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
JJJVYF = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
JJVYFC = "".join(chr(c) for c in [105, 110, 89, 84])
JLOINE = "".join(chr(c) for c in [67, 70, 71, 49, 51])
JMAOAW = 279
JMCBFE = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JNIBXY = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
JPUNRJ = "".join(chr(c) for c in [80, 50, 72])
JQRJJJ = "".join(chr(c) for c in [105, 110, 88, 77])
JRJHIU = 363
JTACCP = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JUGSEL = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
JUIKFW = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
JUTYEK = 3
JVDQLA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
JVHFTH = 274
JWMNZM = 272
JYKLGQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYMOUN = 266
JZTATD = "".join(chr(c) for c in [80, 52, 76])
KBDFSR = 452
KCWAON = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
KFWRKI = "".join(chr(c) for c in [67, 72, 73, 76, 76])
KHTZBB = "".join(chr(c) for c in [67, 70, 71, 49])
KINEJN = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
KJPUNR = "".join(chr(c) for c in [80, 49, 76])
KLGQPL = 313
KMLOIJ = "".join(chr(c) for c in [75, 52])
KPHUOJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
KQTDKH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
KQXPIC = "".join(
    chr(c)
    for c in [
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        82,
        101,
        113,
        117,
        101,
        115,
        116,
    ]
)
KSOKPH = "".join(chr(c) for c in [85, 100, 66, 76])
KSTSEM = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
KVKZIL = 283
KWIVDN = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
KXSJWM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
KZILXW = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
LAIIDN = "".join(
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
LASSAK = "".join(chr(c) for c in [84, 82, 69, 65, 68, 77, 73, 76, 76])
LGQPLS = "".join(chr(c) for c in [78, 79])
LHBQNR = 358
LIUXFE = 364
LJUIKF = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
LKXSJW = 270
LNMHXE = "".join(
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
LOIJUG = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
LOINEL = 461
LRAHEO = "".join(chr(c) for c in [76, 79])
LSIPMD = "".join(
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
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
LWUEUH = "".join(chr(c) for c in [67, 70, 71, 49, 54])
LXWAJV = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
MAOAWB = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
MCBFEG = 369
MCGETI = 330
MCVDSS = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
MDDPMX = 456
MDMPSC = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
MFZDGK = "".join(chr(c) for c in [83, 79, 117, 116, 53])
MHXEKV = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
MJIGYO = 381
MJMAOA = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 347
MLOIJU = "".join(chr(c) for c in [75, 53])
MNHTBJ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
MNZMJI = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        65,
        99,
        116,
        105,
        111,
        110,
    ]
)
MOUNBL = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
MPSCTT = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
MVCYWO = 475
MXFUBJ = 458
NBLKXS = 268
NCUGUC = 256
NEJNIB = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
NELWUE = "".join(chr(c) for c in [67, 70, 71, 49, 53])
NFZCZO = 478
NHTBJE = "".join(chr(c) for c in [85, 76])
NIBXTI = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
NIBXYB = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
NKMLOI = "".join(chr(c) for c in [75, 56])
NMHXEK = 383
NNXWEE = "".join(chr(c) for c in [67, 70, 71, 49, 57])
NPYYLI = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
NQGVUN = "".join(chr(c) for c in [70, 117, 108, 108])
NQJYMO = 264
NQLNMH = 350
NQTMFZ = 322
NRJZTA = "".join(chr(c) for c in [80, 51, 76])
NRSJMC = 306
NRXCHW = 361
NXNKML = "".join(chr(c) for c in [75, 52, 48, 48])
NXWEEZ = 467
NZMJIG = 380
OACMCV = 340
OAWBSI = 280
OCTHBS = 2
OGMDDP = 455
OIHBXI = "".join(chr(c) for c in [83, 79, 117, 116, 56])
OIJUGS = "".join(chr(c) for c in [75, 49, 48, 48])
OINELW = "".join(chr(c) for c in [67, 70, 71, 49, 52])
OJRJHI = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
OLSIPM = 371
ONFZCZ = "".join(chr(c) for c in [67, 70, 71, 51, 48])
ONPYYL = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
OOQNRS = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
OPHUGT = 294
OQNRSJ = 305
OUNBLK = 267
OUSPBW = "".join(
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
OUYNQJ = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
PBWJYK = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
PFTSIF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
PHUGTY = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
PHUOJR = 308
PICXQI = "".join(
    chr(c)
    for c in [
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        85,
        115,
        101,
        114,
        79,
        102,
        102,
    ]
)
PIVLAS = 385
PMDMPS = 373
PMXFUB = "".join(chr(c) for c in [67, 70, 71, 49, 48])
POUYNQ = "".join(chr(c) for c in [78, 69, 87])
PQIPOU = "".join(chr(c) for c in [73, 68, 76, 69])
PSCTTG = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
PUNRJZ = "".join(chr(c) for c in [80, 50, 76])
PYYLIU = "".join(chr(c) for c in [70, 85, 76, 76])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [80, 52])
QFFTTI = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
QFYLJU = "".join(
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
QGLRAH = "".join(chr(c) for c in [85, 100, 80, 49])
QIEFXQ = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
QIPOUY = "".join(chr(c) for c in [83, 84, 79, 80])
QJYMOU = "".join(
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
QLAIID = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
QLNMHX = "".join(
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
QNRSJM = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
QNRXCH = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
QPLSPF = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QRJJJV = "".join(chr(c) for c in [75, 54, 48, 48])
QSNQLN = "".join(
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
QTDKHT = 348
QTMFZD = "".join(chr(c) for c in [83, 79, 117, 116, 52])
QVXOIH = "".join(chr(c) for c in [70, 97, 110])
QXPICX = 388
RAHEOC = "".join(chr(c) for c in [72, 73])
RAZMKQ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
RHYUAX = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
RJHIUS = "".join(chr(c) for c in [85, 100, 65, 117, 120])
RJJJVY = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
RJZTAT = "".join(chr(c) for c in [80, 52, 72])
RKINEJ = 379
ROGMDD = "".join(chr(c) for c in [67, 70, 71, 55])
RSJMCB = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
RTFMNH = "".join(chr(c) for c in [52, 56, 75])
RURAZM = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
RXAIVE = 472
RXCHWD = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
RYXBQF = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
SAKQXP = 386
SBDJQR = "".join(chr(c) for c in [77, 73, 65])
SCTTGC = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
SEMCGE = 329
SIFJBI = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SIPMDM = 372
SIRYXB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
SJMCBF = 362
SJWMNZ = "".join(
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
SKWIVD = 300
SNQLNM = "".join(
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
SOKPHU = "".join(chr(c) for c in [79, 78])
SOOQNR = 304
SPBWJY = "".join(chr(c) for c in [67, 80, 79, 84])
SPFTSI = 353
SROGMD = 454
SRURAZ = 344
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
SSRURA = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
SSUHBV = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
STSEMC = 328
SUHBVW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
SXUJUT = "".join(chr(c) for c in [66, 76])
TACCPQ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
TATDZX = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 48])
TDRXAI = 471
TFMNHT = "".join(chr(c) for c in [54, 52, 75])
THBSKS = "".join(chr(c) for c in [85, 100, 80, 52])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
TIDUBS = 314
TIXQVX = 333
TMFZDG = 323
TOPHUG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TSEMCG = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
TSIFJB = 355
TTGCRH = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
TTIDUB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
TYEKCW = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
TYIYWS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
TZBBEK = "".join(chr(c) for c in [67, 70, 71, 50])
UBJLOI = "".join(chr(c) for c in [67, 70, 71, 49, 50])
UBSSUH = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
UBYGDS = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
UEUHNN = "".join(chr(c) for c in [67, 70, 71, 49, 55])
UGSELH = "".join(chr(c) for c in [75, 51, 48, 48])
UGTYIY = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
UHBVWV = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
UHNNXW = "".join(chr(c) for c in [67, 70, 71, 49, 56])
UIKFWR = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
UJUTYE = "".join(chr(c) for c in [79, 51])
UNBLKX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
UNRJZT = "".join(chr(c) for c in [80, 51, 72])
UNXNKM = "".join(chr(c) for c in [75, 50, 48, 48])
UOJRJH = 307
UQEXLS = "".join(chr(c) for c in [80, 51])
URAZMK = 345
USOOQN = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
USPBWJ = "".join(
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
UTOPHU = 293
UTYEKC = "".join(chr(c) for c in [76, 49, 50, 48])
UXFEFJ = 365
VCYWON = "".join(chr(c) for c in [67, 70, 71, 50, 56])
VDNQGV = 316
VDQLAI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
VDSSRU = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
VEMVCY = 474
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
VLASSA = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
VOACMC = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
VUBYGD = 288
VUNXNK = 357
VWVUBY = 287
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
WAONPY = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
WBSIRY = 281
WEEZFE = 468
WIVDNQ = 301
WJYKLG = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
WMNZMJ = "".join(
    chr(c)
    for c in [80, 114, 111, 103, 79, 117, 116, 112, 117, 116, 65, 99, 99, 101, 115, 115]
)
WONFZC = 477
WRKINE = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
WSKWIV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
WUEUHN = 464
WVUBYG = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
XAIVEM = "".join(chr(c) for c in [67, 70, 71, 50, 53])
XBQFYL = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
XCHWDA = 376
XEKVKZ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
XFEFJT = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
XFUBJL = "".join(chr(c) for c in [67, 70, 71, 49, 49])
XIBHZV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
XLSXUJ = 260
XNCUGU = 64
XNKMLO = "".join(chr(c) for c in [75, 56, 53])
XNQTMF = "".join(chr(c) for c in [83, 79, 117, 116, 51])
XOIHBX = "".join(chr(c) for c in [83, 79, 117, 116, 55])
XPICXQ = 0
XQIEFX = 257
XQVXOI = 325
XSJWMN = 271
XTIACQ = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
XUJUTY = "".join(chr(c) for c in [67, 80])
XWAJVD = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
XWEEZF = "".join(chr(c) for c in [67, 70, 71, 50, 48])
YBQSNQ = "".join(
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
YEKCWA = 5
YFCRTF = 290
YGDSBD = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
YIYWSK = 297
YKLGQP = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
YLIUXF = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
YLJUIK = "".join(
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
YMOUNB = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
YNQJYM = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YOUSPB = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YUAXNC = "".join(chr(c) for c in [76, 73])
YWONFZ = "".join(chr(c) for c in [67, 70, 71, 50, 57])
YWSKWI = 299
YXBQFY = 377
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 450
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = 479
ZDGKEA = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
ZFETDR = "".join(chr(c) for c in [67, 70, 71, 50, 50])
ZILXWA = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
ZMJIGY = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        68,
        117,
        114,
    ]
)
ZMKQTD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
ZOLSIP = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
ZTATDZ = "".join(chr(c) for c in [66, 76, 79])
ZUQEXL = "".join(chr(c) for c in [80, 50])
ZVOACM = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
ZXNQTM = 321
ACCPQI = [JTACCP, TACCPQ]
AHEOCT = [FXQGLR, LRAHEO, RAHEOC]
AMJMAO = [HECVYY, IAMJMA, IAMJMA, IAMJMA]
ASSAKQ = [IVLASS, VLASSA, LASSAK]
AXNCUG = [
    QGLRAH,
    EOCTHB,
    CTHBSK,
    THBSKS,
    HBSKSO,
    KSOKPH,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RJHIUS,
    HIUSOO,
    USOOQN,
    OOQNRS,
    QNRSJM,
    RSJMCB,
    JMCBFE,
]
CQFFTT = [HECVYY, ACQFFT, ACQFFT, ACQFFT]
FMNHTB = [FCRTFM, CRTFMN, RTFMNH, TFMNHT]
FWRKIN = [IKFWRK, KFWRKI]
GZUQEX = [FXQGLR, FEGZUQ, EGZUQE]
HYUAXN = []
HZVOAC = [
    FIKJPU,
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
    XUJUTY,
]
JVYFCR = [
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
]
KEAKST = [
    FIKJPU,
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
    GKEAKS,
]
LSXUJU = [FXQGLR, FEGZUQ]
OKPHUO = [FXQGLR, SOKPHU]
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
PLSPFT = [LGQPLS, LRAHEO, GQPLSP, RAHEOC, QPLSPF]
QGVUNX = [DNQGVU, NQGVUN]
SELHBQ = [
    UNXNKM,
    NXNKML,
    XNKMLO,
    NKMLOI,
    KMLOIJ,
    MLOIJU,
    LOIJUG,
    OIJUGS,
    IJUGSE,
    HECVYY,
    HECVYY,
    HECVYY,
    JUGSEL,
    UGSELH,
    GSELHB,
]
SKSOKP = [FXQGLR, RAHEOC]
TBJEUT = [NHTBJE, HTBJEU]
TDZXNQ = [
    FIKJPU,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    NRJZTA,
    RJZTAT,
    JZTATD,
    EXLSXU,
    ZTATDZ,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    TATDZX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    KCWAON,
    ATDZXN,
]
TGCRHY = [MPSCTT, PSCTTG, SCTTGC, CTTGCR, TTGCRH]
UAXNCU = [
    CBFEGZ,
    ZUQEXL,
    UQEXLS,
    QEXLSX,
    EXLSXU,
    SXUJUT,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    TYEKCW,
    EKCWAO,
    KCWAON,
    WAONPY,
    YLIUXF,
    IUXFEF,
    XFEFJT,
    YUAXNC,
]
UYNQJY = [PQIPOU, QIPOUY, IPOUYN, POUYNQ, OUYNQJ]
VXOIHB = [
    FIKJPU,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    NRJZTA,
    RJZTAT,
    JZTATD,
    EXLSXU,
    ZTATDZ,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    HECVYY,
    HECVYY,
    QVXOIH,
    HECVYY,
    HECVYY,
    TATDZX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    KCWAON,
    ATDZXN,
]
WDAFIK = [CHWDAF, HWDAFI]
XQGLRA = [QIEFXQ, IEFXQG, EFXQGL, FXQGLR]
XYBQSN = [
    PQIPOU,
    KINEJN,
    INEJNI,
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
    NEJNIB,
    EJNIBX,
    JNIBXY,
    NIBXYB,
    IBXYBQ,
    BXYBQS,
]
YYLIUX = [ONPYYL, NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return XNCUGU

    @property
    def begin(self):
        return NCUGUC

    @property
    def end(self):
        return CUGUCY

    @property
    def all_device_keys(self):
        return UAXNCU

    @property
    def user_demand_keys(self):
        return AXNCUG

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
            KQXPIC: GeckoBoolStructAccessor(self.struct, KQXPIC, QXPICX, XPICXQ, None),
            PICXQI: GeckoBoolStructAccessor(self.struct, PICXQI, QXPICX, ICXQIE, None),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, XQGLRA, None, None, AKQXPI
            ),
            QGLRAH: GeckoEnumStructAccessor(
                self.struct, QGLRAH, GLRAHE, XPICXQ, AHEOCT, None, HEOCTH, AKQXPI
            ),
            EOCTHB: GeckoEnumStructAccessor(
                self.struct, EOCTHB, GLRAHE, OCTHBS, AHEOCT, None, HEOCTH, AKQXPI
            ),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, GLRAHE, HEOCTH, AHEOCT, None, HEOCTH, AKQXPI
            ),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, GLRAHE, VHFTHE, AHEOCT, None, HEOCTH, AKQXPI
            ),
            HBSKSO: GeckoEnumStructAccessor(
                self.struct, HBSKSO, BSKSOK, XPICXQ, SKSOKP, None, OCTHBS, AKQXPI
            ),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, BSKSOK, ICXQIE, OKPHUO, None, OCTHBS, AKQXPI
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, OKPHUO, None, None, AKQXPI
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, SKSOKP, None, None, AKQXPI
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, OKPHUO, None, None, AKQXPI
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, OKPHUO, None, None, AKQXPI
            ),
            HIUSOO: GeckoByteStructAccessor(self.struct, HIUSOO, IUSOOQ, AKQXPI),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, AKQXPI),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, AKQXPI),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, AKQXPI),
            RSJMCB: GeckoByteStructAccessor(self.struct, RSJMCB, SJMCBF, AKQXPI),
            JMCBFE: GeckoByteStructAccessor(self.struct, JMCBFE, MCBFEG, AKQXPI),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, XPICXQ, GZUQEX, None, HEOCTH, None
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, BFEGZU, OCTHBS, GZUQEX, None, HEOCTH, None
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, BFEGZU, HEOCTH, GZUQEX, None, HEOCTH, None
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, BFEGZU, VHFTHE, GZUQEX, None, HEOCTH, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, XPICXQ, LSXUJU, None, OCTHBS, None
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XLSXUJ, ICXQIE, OKPHUO, None, OCTHBS, None
            ),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, XLSXUJ, OCTHBS, OKPHUO, None, OCTHBS, None
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, XLSXUJ, JUTYEK, OKPHUO, None, OCTHBS, None
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, XLSXUJ, HEOCTH, OKPHUO, None, OCTHBS, None
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, XLSXUJ, YEKCWA, OKPHUO, None, OCTHBS, None
            ),
            EKCWAO: GeckoEnumStructAccessor(
                self.struct, EKCWAO, XLSXUJ, VHFTHE, OKPHUO, None, OCTHBS, None
            ),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, XLSXUJ, CWAONP, OKPHUO, None, OCTHBS, None
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, YYLIUX, None, None, AKQXPI
            ),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, YYLIUX, None, None, None
            ),
            IUXFEF: GeckoWordStructAccessor(self.struct, IUXFEF, UXFEFJ, None),
            XFEFJT: GeckoWordStructAccessor(self.struct, XFEFJT, FEFJTA, AKQXPI),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, XPICXQ, ACCPQI, None, OCTHBS, AKQXPI
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, UYNQJY, None, None, AKQXPI
            ),
            YNQJYM: GeckoTimeStructAccessor(self.struct, YNQJYM, NQJYMO, AKQXPI),
            QJYMOU: GeckoByteStructAccessor(self.struct, QJYMOU, JYMOUN, AKQXPI),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, FJTACC, OCTHBS, ACCPQI, None, OCTHBS, AKQXPI
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, UYNQJY, None, None, AKQXPI
            ),
            UNBLKX: GeckoTimeStructAccessor(self.struct, UNBLKX, NBLKXS, AKQXPI),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, AKQXPI),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, AKQXPI),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, AKQXPI),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, FJTACC, ICXQIE, ACCPQI, None, OCTHBS, AKQXPI
            ),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, UYNQJY, None, None, AKQXPI
            ),
            ZMJIGY: GeckoTimeStructAccessor(self.struct, ZMJIGY, MJIGYO, AKQXPI),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, IGYOUS, XPICXQ, None),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, IGYOUS, OCTHBS, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, IGYOUS, JUTYEK, None),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, IGYOUS, HEOCTH, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, IGYOUS, YEKCWA, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, JVHFTH, OCTHBS, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, BWJYKL, JUTYEK, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, BWJYKL, YEKCWA, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, BWJYKL, VHFTHE, None),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, PLSPFT, None, None, None
            ),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, SPFTSI, YEKCWA, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, SPFTSI, VHFTHE, None),
            FTSIFJ: GeckoWordStructAccessor(self.struct, FTSIFJ, TSIFJB, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, JVHFTH, ICXQIE, None),
            IFJBIA: GeckoTempStructAccessor(self.struct, IFJBIA, FJBIAM, None),
            JBIAMJ: GeckoTempStructAccessor(self.struct, JBIAMJ, BIAMJM, None),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, XLSXUJ, YEKCWA, AMJMAO, None, HEOCTH, None
            ),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, OCTHBS, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, JMAOAW, VHFTHE, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, OCTHBS, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, WBSIRY, ICXQIE, None),
            BSIRYX: GeckoBoolStructAccessor(
                self.struct, BSIRYX, WBSIRY, OCTHBS, AKQXPI
            ),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, IRYXBQ, ICXQIE, None),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, XPICXQ, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, XPICXQ, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FYLJUI, HEOCTH, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, FYLJUI, YEKCWA, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, FYLJUI, VHFTHE, None),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, FYLJUI, CWAONP, FWRKIN, None, OCTHBS, AKQXPI
            ),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, RKINEJ, None, XYBQSN, None, None, None
            ),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, BQSNQL, XPICXQ, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, BQSNQL, ICXQIE, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, NQLNMH, XPICXQ, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, NQLNMH, ICXQIE, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, NMHXEK, XPICXQ, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, JVHFTH, JUTYEK, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, BWJYKL, XPICXQ, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, BWJYKL, ICXQIE, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, KVKZIL, OCTHBS, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, KVKZIL, JUTYEK, None),
            KZILXW: GeckoBoolStructAccessor(self.struct, KZILXW, BQSNQL, JUTYEK, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, BQSNQL, HEOCTH, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, BQSNQL, YEKCWA, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, BQSNQL, VHFTHE, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, NQLNMH, JUTYEK, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, NQLNMH, HEOCTH, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, NQLNMH, YEKCWA, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, NQLNMH, VHFTHE, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, DQLAII, OCTHBS, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, DQLAII, JUTYEK, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, IRYXBQ, JUTYEK, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, SPFTSI, XPICXQ, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, SPFTSI, ICXQIE, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, DNIBXT, XPICXQ, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, OAWBSI, XPICXQ, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, KVKZIL, XPICXQ, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, KVKZIL, ICXQIE, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, KVKZIL, HEOCTH, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, IACQFF, XPICXQ, None),
            ACQFFT: GeckoEnumStructAccessor(
                self.struct, ACQFFT, IACQFF, ICXQIE, CQFFTT, None, HEOCTH, None
            ),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, IACQFF, JUTYEK, None),
            FFTTID: GeckoWordStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, TIDUBS, XPICXQ, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, DUBSSU, XPICXQ, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, DUBSSU, ICXQIE, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, DQLAII, XPICXQ, None),
            SSUHBV: GeckoBoolStructAccessor(self.struct, SSUHBV, DQLAII, ICXQIE, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, DQLAII, HEOCTH, None),
            UHBVWV: GeckoWordStructAccessor(self.struct, UHBVWV, HBVWVU, None),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, None),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, None),
            UBYGDS: GeckoEnumStructAccessor(
                self.struct, UBYGDS, BYGDSB, None, JVYFCR, None, None, None
            ),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, YFCRTF, XPICXQ, FMNHTB, None, HEOCTH, None
            ),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, YFCRTF, OCTHBS, TBJEUT, None, OCTHBS, None
            ),
            BJEUTO: GeckoWordStructAccessor(self.struct, BJEUTO, JEUTOP, None),
            EUTOPH: GeckoByteStructAccessor(self.struct, EUTOPH, UTOPHU, None),
            TOPHUG: GeckoByteStructAccessor(self.struct, TOPHUG, OPHUGT, None),
            PHUGTY: GeckoByteStructAccessor(self.struct, PHUGTY, HUGTYI, None),
            UGTYIY: GeckoByteStructAccessor(self.struct, UGTYIY, GTYIYW, None),
            TYIYWS: GeckoWordStructAccessor(self.struct, TYIYWS, YIYWSK, None),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, None),
            WSKWIV: GeckoByteStructAccessor(self.struct, WSKWIV, SKWIVD, None),
            KWIVDN: GeckoWordStructAccessor(self.struct, KWIVDN, WIVDNQ, None),
            IVDNQG: GeckoEnumStructAccessor(
                self.struct, IVDNQG, VDNQGV, None, QGVUNX, None, OCTHBS, AKQXPI
            ),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, SELHBQ, None, None, None
            ),
            ELHBQN: GeckoWordStructAccessor(self.struct, ELHBQN, LHBQNR, None),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, None),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, None),
            RXCHWD: GeckoEnumStructAccessor(
                self.struct, RXCHWD, XCHWDA, None, WDAFIK, None, None, AKQXPI
            ),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, AFIKJP, None, TDZXNQ, None, None, AKQXPI
            ),
            DZXNQT: GeckoEnumStructAccessor(
                self.struct, DZXNQT, ZXNQTM, None, TDZXNQ, None, None, AKQXPI
            ),
            XNQTMF: GeckoEnumStructAccessor(
                self.struct, XNQTMF, NQTMFZ, None, TDZXNQ, None, None, AKQXPI
            ),
            QTMFZD: GeckoEnumStructAccessor(
                self.struct, QTMFZD, TMFZDG, None, TDZXNQ, None, None, AKQXPI
            ),
            MFZDGK: GeckoEnumStructAccessor(
                self.struct, MFZDGK, FZDGKE, None, TDZXNQ, None, None, AKQXPI
            ),
            ZDGKEA: GeckoEnumStructAccessor(
                self.struct, ZDGKEA, DGKEAK, None, KEAKST, None, None, AKQXPI
            ),
            EAKSTS: GeckoByteStructAccessor(self.struct, EAKSTS, AKSTSE, AKQXPI),
            KSTSEM: GeckoByteStructAccessor(self.struct, KSTSEM, STSEMC, AKQXPI),
            TSEMCG: GeckoByteStructAccessor(self.struct, TSEMCG, SEMCGE, AKQXPI),
            EMCGET: GeckoByteStructAccessor(self.struct, EMCGET, MCGETI, AKQXPI),
            CGETIX: GeckoByteStructAccessor(self.struct, CGETIX, GETIXQ, AKQXPI),
            ETIXQV: GeckoByteStructAccessor(self.struct, ETIXQV, TIXQVX, AKQXPI),
            IXQVXO: GeckoEnumStructAccessor(
                self.struct, IXQVXO, XQVXOI, None, VXOIHB, None, None, AKQXPI
            ),
            XOIHBX: GeckoEnumStructAccessor(
                self.struct, XOIHBX, DGKEAK, None, VXOIHB, None, None, AKQXPI
            ),
            OIHBXI: GeckoEnumStructAccessor(
                self.struct, OIHBXI, AKSTSE, None, VXOIHB, None, None, AKQXPI
            ),
            IHBXIB: GeckoEnumStructAccessor(
                self.struct, IHBXIB, STSEMC, None, VXOIHB, None, None, AKQXPI
            ),
            HBXIBH: GeckoEnumStructAccessor(
                self.struct, HBXIBH, SEMCGE, None, VXOIHB, None, None, AKQXPI
            ),
            BXIBHZ: GeckoEnumStructAccessor(
                self.struct, BXIBHZ, MCGETI, None, VXOIHB, None, None, AKQXPI
            ),
            XIBHZV: GeckoEnumStructAccessor(
                self.struct, XIBHZV, GETIXQ, None, VXOIHB, None, None, AKQXPI
            ),
            IBHZVO: GeckoEnumStructAccessor(
                self.struct, IBHZVO, BHZVOA, None, HZVOAC, None, None, AKQXPI
            ),
            ZVOACM: GeckoEnumStructAccessor(
                self.struct, ZVOACM, TIXQVX, None, HZVOAC, None, None, AKQXPI
            ),
            VOACMC: GeckoByteStructAccessor(self.struct, VOACMC, OACMCV, AKQXPI),
            ACMCVD: GeckoByteStructAccessor(self.struct, ACMCVD, CMCVDS, AKQXPI),
            MCVDSS: GeckoByteStructAccessor(self.struct, MCVDSS, CVDSSR, AKQXPI),
            VDSSRU: GeckoByteStructAccessor(self.struct, VDSSRU, DSSRUR, AKQXPI),
            SSRURA: GeckoByteStructAccessor(self.struct, SSRURA, SRURAZ, AKQXPI),
            RURAZM: GeckoByteStructAccessor(self.struct, RURAZM, URAZMK, AKQXPI),
            RAZMKQ: GeckoByteStructAccessor(self.struct, RAZMKQ, AZMKQT, AKQXPI),
            ZMKQTD: GeckoByteStructAccessor(self.struct, ZMKQTD, MKQTDK, AKQXPI),
            KQTDKH: GeckoByteStructAccessor(self.struct, KQTDKH, QTDKHT, AKQXPI),
            CZOLSI: GeckoBoolStructAccessor(self.struct, CZOLSI, JVHFTH, YEKCWA, None),
            ZOLSIP: GeckoByteStructAccessor(self.struct, ZOLSIP, OLSIPM, AKQXPI),
            LSIPMD: GeckoByteStructAccessor(self.struct, LSIPMD, SIPMDM, AKQXPI),
            IPMDMP: GeckoByteStructAccessor(self.struct, IPMDMP, PMDMPS, AKQXPI),
            MDMPSC: GeckoEnumStructAccessor(
                self.struct, MDMPSC, DMPSCT, None, TGCRHY, None, None, AKQXPI
            ),
            GCRHYU: GeckoBoolStructAccessor(
                self.struct, GCRHYU, CRHYUA, XPICXQ, AKQXPI
            ),
            RHYUAX: GeckoBoolStructAccessor(self.struct, RHYUAX, XCHWDA, XPICXQ, None),
        }

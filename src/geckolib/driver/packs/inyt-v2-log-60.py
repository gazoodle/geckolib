#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v60'
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
ACMCVD = 348
ACQFFT = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
AFIKJP = 321
AHEOCT = 1
AIIDNI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
AIVEMV = 371
AJVDQL = 309
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = "".join(chr(c) for c in [83, 79, 117, 116, 55])
AMJMAO = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
AOAWBS = "".join(
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
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = 327
AWBSIR = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
AZMKQT = "".join(chr(c) for c in [67, 70, 71, 53])
BBEKBD = 458
BDFSRO = 460
BDJQRJ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
BEKBDF = "".join(chr(c) for c in [67, 70, 71, 49, 49])
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
BIAMJM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
BJEUTO = 300
BJLOIN = "".join(chr(c) for c in [67, 70, 71, 50, 48])
BLKXSJ = "".join(chr(c) for c in [67, 108, 101, 97, 110])
BMJVHF = 256
BQFYLJ = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
BQNRXC = "".join(chr(c) for c in [80, 51, 72])
BQSNQL = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
BSIRYX = "".join(chr(c) for c in [72, 69, 65, 84])
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(chr(c) for c in [68, 74, 83, 52])
BVWVUB = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
BWJYKL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
BXIBHZ = 344
BXTIAC = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
BXYBQS = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
BYGDSB = "".join(chr(c) for c in [49, 54, 75])
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = 332
CHWDAF = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 48])
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CQFFTT = 287
CRTFMN = 295
CTHBSK = 307
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 49])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
CYWONF = 374
CZOLSI = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
DAFIKJ = "".join(chr(c) for c in [83, 79, 117, 116, 50])
DDPMXF = 464
DFSROG = "".join(chr(c) for c in [67, 70, 71, 49, 51])
DGKEAK = "".join(chr(c) for c in [83, 79, 117, 116, 54])
DJQRJJ = "".join(chr(c) for c in [85, 76])
DKHTZB = "".join(chr(c) for c in [67, 70, 71, 56])
DMPSCT = 60
DNIBXT = 315
DNQGVU = "".join(chr(c) for c in [75, 51, 48, 48])
DPMXFU = "".join(chr(c) for c in [67, 70, 71, 49, 55])
DQLAII = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
DRXAIV = 479
DSBDJQ = "".join(chr(c) for c in [54, 52, 75])
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 50])
DUBSSU = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
DZXNQT = 328
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 476
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EJNIBX = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
EKBDFS = 459
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = "".join(
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
ELHBQN = "".join(chr(c) for c in [80, 49, 76])
ELWUEU = "".join(chr(c) for c in [67, 70, 71, 50, 51])
EMCGET = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
EMVCYW = "".join(
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
EOCTHB = 308
ETDRXA = 478
ETIXQV = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
EUHNNX = "".join(chr(c) for c in [67, 70, 71, 50, 53])
EUTOPH = 301
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
EZFETD = "".join(chr(c) for c in [67, 70, 71, 50, 57])
FCRTFM = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FETDRX = "".join(chr(c) for c in [67, 70, 71, 51, 48])
FFTTID = 288
FIKJPU = "".join(chr(c) for c in [83, 79, 117, 116, 51])
FJBIAM = 281
FMNHTB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
FSROGM = 461
FTHECV = 319
FTSIFJ = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
FUBJLO = "".join(chr(c) for c in [67, 70, 71, 49, 57])
FWRKIN = 284
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
FZCZOL = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
FZDGKE = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
GDSBDJ = "".join(chr(c) for c in [52, 56, 75])
GKEAKS = 325
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GMDDPM = 463
GQPLSP = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
GSELHB = "".join(chr(c) for c in [78, 65])
GTYIYW = 357
GVUNXN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
GYOUSP = "".join(chr(c) for c in [78, 79])
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [80, 50, 76])
HBSKSO = 363
HBVWVU = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
HBXIBH = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HNNXWE = "".join(chr(c) for c in [67, 70, 71, 50, 54])
HTBJEU = 299
HTZBBE = "".join(chr(c) for c in [67, 70, 71, 57])
HUOJRJ = 305
HWDAFI = "".join(chr(c) for c in [65, 85, 88])
HXEKVK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
HZVOAC = 346
IACQFF = 285
IAMJMA = 352
IBHZVO = 345
IBXTIA = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
IBXYBQ = 283
ICXQIE = 0
IDNIBX = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
IDUBSS = "".join(chr(c) for c in [105, 110, 88, 69])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
IGYOUS = 313
IHBXIB = 343
IIDNIB = 314
IKJPUN = 322
ILXWAJ = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
INEJNI = "".join(
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
INELWU = "".join(chr(c) for c in [67, 70, 71, 50, 50])
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IUSOOQ = "".join(chr(c) for c in [80, 49])
IUXFEF = "".join(chr(c) for c in [73, 68, 76, 69])
IVDNQG = "".join(chr(c) for c in [75, 56, 48, 48])
IVEMVC = "".join(
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
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = 340
IYWSKW = "".join(chr(c) for c in [75, 56, 53])
JBIAMJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
JEUTOP = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JIGYOU = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
JJJVYF = 291
JJVYFC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
JLOINE = 468
JMAOAW = "".join(chr(c) for c in [72, 80, 67, 68, 101, 116, 101, 99, 116, 101, 100])
JMCBFE = 260
JNIBXY = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
JPUNRJ = 323
JQRJJJ = "".join(chr(c) for c in [67, 69])
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 49])
JUIKFW = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVDQLA = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
JVHFTH = 274
JVYFCR = 293
JWMNZM = "".join(
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
JYKLGQ = 355
JYMOUN = 272
JZTATD = "".join(chr(c) for c in [72, 84, 82])
KBDFSR = "".join(chr(c) for c in [67, 70, 71, 49, 50])
KCWAON = 365
KEAKST = "".join(chr(c) for c in [70, 97, 110])
KFWRKI = "".join(
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
KHTZBB = 456
KINEJN = 350
KJPUNR = "".join(chr(c) for c in [83, 79, 117, 116, 52])
KLGQPL = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
KMLOIJ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
KPHUOJ = 304
KQTDKH = 454
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [83, 79, 117, 116, 56])
KVKZIL = "".join(
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
KWIVDN = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
KXSJWM = "".join(chr(c) for c in [80, 117, 114, 103, 101])
KZILXW = 354
LAIIDN = 311
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = 275
LHBQNR = "".join(chr(c) for c in [80, 50, 72])
LIUXFE = 263
LJUIKF = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
LKXSJW = 273
LNMHXE = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
LOIJUG = "".join(chr(c) for c in [45, 45, 45])
LOINEL = "".join(chr(c) for c in [67, 70, 71, 50, 49])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LWUEUH = 471
LXWAJV = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
MAOAWB = 378
MCGETI = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
MCVDSS = 448
MDDPMX = "".join(chr(c) for c in [67, 70, 71, 49, 54])
MFZDGK = 331
MHXEKV = 351
MJIGYO = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
MJMAOA = 377
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = "".join(chr(c) for c in [67, 70, 71, 54])
MLOIJU = 376
MNHTBJ = 297
MNZMJI = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
MOUNBL = "".join(
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
MPSCTT = 256
MVCYWO = 373
MXFUBJ = "".join(chr(c) for c in [67, 70, 71, 49, 56])
NBLKXS = 381
NEJNIB = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
NELWUE = 470
NFZCZO = "".join(
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
NHTBJE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
NIBXTI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
NIBXYB = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
NKMLOI = 361
NMHXEK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
NNXWEE = 474
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
NQJYMO = 271
NQLNMH = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
NQTMFZ = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
NRJZTA = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = "".join(chr(c) for c in [80, 52, 72])
NXNKML = 360
NXWEEZ = "".join(chr(c) for c in [67, 70, 71, 50, 55])
NZMJIG = 282
OACMCV = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
OAWBSI = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = "".join(chr(c) for c in [67, 70, 71, 49, 53])
OIHBXI = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
OIJUGS = "".join(chr(c) for c in [82, 69, 83, 69, 84])
OINELW = 469
OJRJHI = 306
OKPHUO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
OLSIPM = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
ONFZCZ = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
ONPYYL = 262
OOQNRS = "".join(chr(c) for c in [76, 79, 87])
OPHUGT = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
OUNBLK = 380
OUSPBW = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
OUYNQJ = "".join(
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
PBWJYK = 353
PFTSIF = 279
PHUGTY = "".join(chr(c) for c in [70, 117, 108, 108])
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
PMXFUB = 465
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PSCTTG = 479
PUNRJZ = "".join(chr(c) for c in [83, 79, 117, 116, 53])
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
QFYLJU = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
QIEFXQ = 2
QIPOUY = 267
QJYMOU = "".join(
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
QLAIID = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
QLNMHX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = "".join(chr(c) for c in [80, 51, 76])
QPLSPF = 277
QSNQLN = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
QTDKHT = "".join(chr(c) for c in [67, 70, 71, 55])
QTMFZD = 330
QVXOIH = 341
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 452
RJHIUS = 362
RJJJVY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
RJZTAT = 326
RKINEJ = "".join(
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
ROGMDD = 462
RSJMCB = "".join(chr(c) for c in [80, 52])
RTFMNH = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
RURAZM = 451
RXAIVE = "".join(
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
RXCHWD = "".join(chr(c) for c in [80, 52, 76])
RYXBQF = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SELHBQ = "".join(chr(c) for c in [80, 49, 72])
SEMCGE = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
SIFJBI = 280
SIPMDM = "".join(chr(c) for c in [76, 73])
SIRYXB = "".join(chr(c) for c in [67, 72, 73, 76, 76])
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(
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
SKSOKP = 370
SKWIVD = "".join(chr(c) for c in [75, 53])
SNQLNM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
SPFTSI = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
SROGMD = "".join(chr(c) for c in [67, 70, 71, 49, 52])
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 51])
SSRURA = 450
SSUHBV = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
STSEMC = "".join(chr(c) for c in [83, 79, 117, 116, 57])
SUHBVW = "".join(chr(c) for c in [105, 110, 88, 77])
SXUJUT = 310
TACCPQ = 264
TATDZX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
TBJEUT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
TDKHTZ = 455
TDRXAI = "".join(chr(c) for c in [67, 70, 71, 51, 49])
TDZXNQ = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
TFMNHT = 296
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
TIDUBS = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
TIXQVX = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
TMFZDG = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
TOPHUG = 316
TSEMCG = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
TSIFJB = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
TTIDUB = 289
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [75, 50, 48, 48])
TZBBEK = 457
UBJLOI = 467
UBSSUH = "".join(chr(c) for c in [77, 73, 65])
UBYGDS = 290
UEUHNN = 472
UGSELH = 320
UGTYIY = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
UHBVWV = "".join(chr(c) for c in [75, 54, 48, 48])
UHNNXW = 473
UIKFWR = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
UNRJZT = 324
UNXNKM = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = "".join(chr(c) for c in [67, 70, 71, 52])
USOOQN = 261
UTOPHU = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VCYWON = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
VDNQGV = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
VDSSRU = 449
VEMVCY = 372
VHFTHE = 6
VKZILX = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = 347
VUBYGD = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
VUNXNK = 358
VWVUBY = "".join(chr(c) for c in [105, 110, 89, 84])
VXOIHB = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
WAONPY = 367
WBSIRY = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
WEEZFE = "".join(chr(c) for c in [67, 70, 71, 50, 56])
WIVDNQ = "".join(chr(c) for c in [75, 49, 48, 48])
WJYKLG = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
WMNZMJ = "".join(chr(c) for c in [67, 80, 79, 84])
WONFZC = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
WRKINE = "".join(
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
WSKWIV = "".join(chr(c) for c in [75, 52])
WUEUHN = "".join(chr(c) for c in [67, 70, 71, 50, 52])
XAIVEM = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
XBQFYL = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
XCHWDA = "".join(chr(c) for c in [66, 76, 79])
XEKVKZ = "".join(
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
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XFUBJL = 466
XIBHZV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
XLSXUJ = 7
XNKMLO = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
XNQTMF = 329
XOIHBX = 342
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
XSJWMN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
XTIACQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
XWEEZF = 475
XYBQSN = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
YBQSNQ = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
YEKCWA = 364
YFCRTF = 294
YGDSBD = "".join(chr(c) for c in [51, 50, 75])
YIYWSK = "".join(chr(c) for c in [75, 52, 48, 48])
YKLGQP = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
YLIUXF = "".join(
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
YLJUIK = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
YMOUNB = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
YNQJYM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
YOUSPB = "".join(chr(c) for c in [77, 69, 68])
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWONFZ = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
YWSKWI = "".join(chr(c) for c in [75, 56])
YXBQFY = 379
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = "".join(chr(c) for c in [67, 70, 71, 49, 48])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 333
ZFETDR = 477
ZILXWA = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
ZMJIGY = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
ZMKQTD = 453
ZOLSIP = 375
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
ZXNQTM = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
EAKSTS = [
    GSELHB,
    SELHBQ,
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
    QNRXCH,
    NRXCHW,
    RXCHWD,
    SJMCBF,
    XCHWDA,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    KEAKST,
    HECVYY,
    HECVYY,
    CHWDAF,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    HWDAFI,
]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
GETIXQ = [
    GSELHB,
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
    BFEGZU,
]
HUGTYI = [OPHUGT, PHUGTY]
IJUGSE = [LOIJUG, OIJUGS]
IKFWRK = [
    IUXFEF,
    XBQFYL,
    BQFYLJ,
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
    QFYLJU,
    FYLJUI,
    YLJUIK,
    LJUIKF,
    JUIKFW,
    UIKFWR,
]
IPMDMP = [
    IUSOOQ,
    QNRSJM,
    NRSJMC,
    RSJMCB,
    SJMCBF,
    CBFEGZ,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    ZUQEXL,
    QEXLSX,
    EXLSXU,
    LSXUJU,
    TYEKCW,
    EKCWAO,
    CWAONP,
    SIPMDM,
]
IRYXBQ = [BSIRYX, SIRYXB]
LSIPMD = []
LSPFTS = [HECVYY, PLSPFT, PLSPFT, PLSPFT]
MCBFEG = [ASSAKQ, SOOQNR]
MDMPSC = [
    IBXTIA,
    HXEKVK,
    KVKZIL,
    YBQSNQ,
    YKLGQP,
    DQLAII,
    NIBXTI,
    BXTIAC,
    SPFTSI,
    JWMNZM,
    LNMHXE,
    SNQLNM,
    NEJNIB,
    BIAMJM,
    IDNIBX,
    QSNQLN,
    NMHXEK,
    QLNMHX,
    BXYBQS,
    VKZILX,
    NIBXYB,
    EJNIBX,
    XEKVKZ,
    LXWAJV,
    EKVKZI,
    JNIBXY,
    NQLNMH,
    BQSNQL,
    XYBQSN,
]
OQNRSJ = [ASSAKQ, SOOQNR, OOQNRS]
PICXQI = [ASSAKQ, QXPICX, XPICXQ]
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
PMDMPS = [
    AKQXPI,
    XQIEFX,
    IEFXQG,
    EFXQGL,
    FXQGLR,
    GLRAHE,
    HEOCTH,
    OCTHBS,
    THBSKS,
    BSKSOK,
    KSOKPH,
    OKPHUO,
    PHUOJR,
    UOJRJH,
    JRJHIU,
    JHIUSO,
]
QGLRAH = [ASSAKQ, XPICXQ]
QGVUNX = [
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    KWIVDN,
    WIVDNQ,
    IVDNQG,
    HECVYY,
    HECVYY,
    HECVYY,
    VDNQGV,
    DNQGVU,
    NQGVUN,
]
QRJJJV = [DJQRJJ, JQRJJJ]
RAHEOC = [ASSAKQ, LRAHEO]
SBDJQR = [BYGDSB, YGDSBD, GDSBDJ, DSBDJQ]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
USPBWJ = [GYOUSP, QXPICX, YOUSPB, XPICXQ, OUSPBW]
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
VDQLAI = [HECVYY, JVDQLA, JVDQLA, JVDQLA]
WDAFIK = [
    GSELHB,
    SELHBQ,
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
    QNRXCH,
    NRXCHW,
    RXCHWD,
    SJMCBF,
    XCHWDA,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    CHWDAF,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    HWDAFI,
]
WVUBYG = [
    TIDUBS,
    IDUBSS,
    DUBSSU,
    UBSSUH,
    BSSUHB,
    SSUHBV,
    SUHBVW,
    UHBVWV,
    HBVWVU,
    BVWVUB,
    VWVUBY,
]
YYLIUX = [NPYYLI, PYYLIU]
ZCZOLS = [YWONFZ, WONFZC, ONFZCZ, NFZCZO, FZCZOL]
ZTATDZ = [
    GSELHB,
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
    JZTATD,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return DMPSCT

    @property
    def begin(self):
        return MPSCTT

    @property
    def end(self):
        return PSCTTG

    @property
    def all_device_keys(self):
        return IPMDMP

    @property
    def user_demand_keys(self):
        return PMDMPS

    @property
    def error_keys(self):
        return MDMPSC

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
                self.struct, IPIVLA, PIVLAS, None, SSAKQX, None, None, SAKQXP
            ),
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, ICXQIE, PICXQI, None, CXQIEF, SAKQXP
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, KQXPIC, QIEFXQ, PICXQI, None, CXQIEF, SAKQXP
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, KQXPIC, CXQIEF, PICXQI, None, CXQIEF, SAKQXP
            ),
            EFXQGL: GeckoEnumStructAccessor(
                self.struct, EFXQGL, KQXPIC, VHFTHE, PICXQI, None, CXQIEF, SAKQXP
            ),
            FXQGLR: GeckoEnumStructAccessor(
                self.struct, FXQGLR, XQGLRA, ICXQIE, QGLRAH, None, QIEFXQ, SAKQXP
            ),
            GLRAHE: GeckoEnumStructAccessor(
                self.struct, GLRAHE, XQGLRA, AHEOCT, RAHEOC, None, QIEFXQ, SAKQXP
            ),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, EOCTHB, None, RAHEOC, None, None, SAKQXP
            ),
            OCTHBS: GeckoEnumStructAccessor(
                self.struct, OCTHBS, CTHBSK, None, QGLRAH, None, None, SAKQXP
            ),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, HBSKSO, None, RAHEOC, None, None, SAKQXP
            ),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, SKSOKP, None, RAHEOC, None, None, SAKQXP
            ),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, SAKQXP),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, SAKQXP),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, SAKQXP),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, SAKQXP),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, SAKQXP),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, SAKQXP),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, ICXQIE, OQNRSJ, None, CXQIEF, None
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, USOOQN, QIEFXQ, OQNRSJ, None, CXQIEF, None
            ),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, USOOQN, CXQIEF, OQNRSJ, None, CXQIEF, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, USOOQN, VHFTHE, OQNRSJ, None, CXQIEF, None
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, ICXQIE, MCBFEG, None, QIEFXQ, None
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, JMCBFE, AHEOCT, RAHEOC, None, QIEFXQ, None
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, JMCBFE, QIEFXQ, RAHEOC, None, QIEFXQ, None
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, JMCBFE, EGZUQE, RAHEOC, None, QIEFXQ, None
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, JMCBFE, CXQIEF, RAHEOC, None, QIEFXQ, None
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, JMCBFE, UQEXLS, RAHEOC, None, QIEFXQ, None
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, JMCBFE, VHFTHE, RAHEOC, None, QIEFXQ, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, JMCBFE, XLSXUJ, RAHEOC, None, QIEFXQ, None
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, None, UTYEKC, None, None, SAKQXP
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, None, UTYEKC, None, None, None
            ),
            EKCWAO: GeckoWordStructAccessor(self.struct, EKCWAO, KCWAON, None),
            CWAONP: GeckoWordStructAccessor(self.struct, CWAONP, WAONPY, SAKQXP),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, ONPYYL, ICXQIE, YYLIUX, None, QIEFXQ, SAKQXP
            ),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, FJTACC, None, None, SAKQXP
            ),
            JTACCP: GeckoTimeStructAccessor(self.struct, JTACCP, TACCPQ, SAKQXP),
            ACCPQI: GeckoByteStructAccessor(self.struct, ACCPQI, CCPQIP, SAKQXP),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, ONPYYL, QIEFXQ, YYLIUX, None, QIEFXQ, SAKQXP
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, FJTACC, None, None, SAKQXP
            ),
            IPOUYN: GeckoTimeStructAccessor(self.struct, IPOUYN, POUYNQ, SAKQXP),
            OUYNQJ: GeckoByteStructAccessor(self.struct, OUYNQJ, UYNQJY, SAKQXP),
            YNQJYM: GeckoByteStructAccessor(self.struct, YNQJYM, NQJYMO, SAKQXP),
            QJYMOU: GeckoByteStructAccessor(self.struct, QJYMOU, JYMOUN, SAKQXP),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, ONPYYL, AHEOCT, YYLIUX, None, QIEFXQ, SAKQXP
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, FJTACC, None, None, SAKQXP
            ),
            UNBLKX: GeckoTimeStructAccessor(self.struct, UNBLKX, NBLKXS, SAKQXP),
            BLKXSJ: GeckoBoolStructAccessor(self.struct, BLKXSJ, LKXSJW, ICXQIE, None),
            KXSJWM: GeckoBoolStructAccessor(self.struct, KXSJWM, LKXSJW, QIEFXQ, None),
            XSJWMN: GeckoBoolStructAccessor(self.struct, XSJWMN, LKXSJW, EGZUQE, None),
            SJWMNZ: GeckoBoolStructAccessor(self.struct, SJWMNZ, LKXSJW, CXQIEF, None),
            JWMNZM: GeckoBoolStructAccessor(self.struct, JWMNZM, LKXSJW, UQEXLS, None),
            WMNZMJ: GeckoBoolStructAccessor(self.struct, WMNZMJ, JVHFTH, QIEFXQ, None),
            MNZMJI: GeckoBoolStructAccessor(self.struct, MNZMJI, NZMJIG, EGZUQE, None),
            ZMJIGY: GeckoBoolStructAccessor(self.struct, ZMJIGY, NZMJIG, UQEXLS, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, NZMJIG, VHFTHE, None),
            JIGYOU: GeckoEnumStructAccessor(
                self.struct, JIGYOU, IGYOUS, None, USPBWJ, None, None, None
            ),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, PBWJYK, UQEXLS, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, PBWJYK, VHFTHE, None),
            WJYKLG: GeckoWordStructAccessor(self.struct, WJYKLG, JYKLGQ, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, JVHFTH, AHEOCT, None),
            KLGQPL: GeckoTempStructAccessor(self.struct, KLGQPL, LGQPLS, None),
            GQPLSP: GeckoTempStructAccessor(self.struct, GQPLSP, QPLSPF, None),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, JMCBFE, UQEXLS, LSPFTS, None, CXQIEF, None
            ),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, QIEFXQ, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, PFTSIF, VHFTHE, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, SIFJBI, QIEFXQ, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FJBIAM, AHEOCT, None),
            JBIAMJ: GeckoBoolStructAccessor(
                self.struct, JBIAMJ, FJBIAM, QIEFXQ, SAKQXP
            ),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, AHEOCT, None),
            AMJMAO: GeckoByteStructAccessor(self.struct, AMJMAO, MJMAOA, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MAOAWB, ICXQIE, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, MAOAWB, CXQIEF, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, MAOAWB, UQEXLS, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, MAOAWB, VHFTHE, None),
            WBSIRY: GeckoEnumStructAccessor(
                self.struct, WBSIRY, MAOAWB, XLSXUJ, IRYXBQ, None, QIEFXQ, SAKQXP
            ),
            RYXBQF: GeckoEnumStructAccessor(
                self.struct, RYXBQF, YXBQFY, None, IKFWRK, None, None, None
            ),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, FWRKIN, ICXQIE, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, FWRKIN, AHEOCT, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, KINEJN, ICXQIE, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, KINEJN, AHEOCT, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, JVHFTH, EGZUQE, None),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, NZMJIG, ICXQIE, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, NZMJIG, AHEOCT, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, IBXYBQ, QIEFXQ, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, IBXYBQ, EGZUQE, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, FWRKIN, EGZUQE, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, FWRKIN, CXQIEF, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, FWRKIN, UQEXLS, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, FWRKIN, VHFTHE, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, KINEJN, EGZUQE, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, KINEJN, CXQIEF, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, KINEJN, UQEXLS, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, KINEJN, VHFTHE, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, MHXEKV, QIEFXQ, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, MHXEKV, EGZUQE, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, IAMJMA, EGZUQE, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, PBWJYK, ICXQIE, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, PBWJYK, AHEOCT, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, KZILXW, ICXQIE, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, SIFJBI, ICXQIE, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, IBXYBQ, ICXQIE, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, IBXYBQ, AHEOCT, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, IBXYBQ, CXQIEF, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, AJVDQL, ICXQIE, None),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, AJVDQL, AHEOCT, VDQLAI, None, CXQIEF, None
            ),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, AJVDQL, EGZUQE, None),
            QLAIID: GeckoWordStructAccessor(self.struct, QLAIID, LAIIDN, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, IIDNIB, ICXQIE, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, DNIBXT, ICXQIE, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, DNIBXT, AHEOCT, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, MHXEKV, ICXQIE, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, MHXEKV, AHEOCT, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, MHXEKV, CXQIEF, None),
            TIACQF: GeckoWordStructAccessor(self.struct, TIACQF, IACQFF, None),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, None),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, TTIDUB, None, WVUBYG, None, None, None
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, ICXQIE, SBDJQR, None, CXQIEF, None
            ),
            BDJQRJ: GeckoEnumStructAccessor(
                self.struct, BDJQRJ, UBYGDS, QIEFXQ, QRJJJV, None, QIEFXQ, None
            ),
            RJJJVY: GeckoWordStructAccessor(self.struct, RJJJVY, JJJVYF, None),
            JJVYFC: GeckoByteStructAccessor(self.struct, JJVYFC, JVYFCR, None),
            VYFCRT: GeckoByteStructAccessor(self.struct, VYFCRT, YFCRTF, None),
            FCRTFM: GeckoByteStructAccessor(self.struct, FCRTFM, CRTFMN, None),
            RTFMNH: GeckoByteStructAccessor(self.struct, RTFMNH, TFMNHT, None),
            FMNHTB: GeckoWordStructAccessor(self.struct, FMNHTB, MNHTBJ, None),
            NHTBJE: GeckoByteStructAccessor(self.struct, NHTBJE, HTBJEU, None),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, None),
            JEUTOP: GeckoWordStructAccessor(self.struct, JEUTOP, EUTOPH, None),
            UTOPHU: GeckoEnumStructAccessor(
                self.struct, UTOPHU, TOPHUG, None, HUGTYI, None, QIEFXQ, SAKQXP
            ),
            UGTYIY: GeckoEnumStructAccessor(
                self.struct, UGTYIY, GTYIYW, None, QGVUNX, None, None, None
            ),
            GVUNXN: GeckoWordStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoEnumStructAccessor(
                self.struct, KMLOIJ, MLOIJU, None, IJUGSE, None, None, SAKQXP
            ),
            JUGSEL: GeckoEnumStructAccessor(
                self.struct, JUGSEL, UGSELH, None, WDAFIK, None, None, SAKQXP
            ),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, AFIKJP, None, WDAFIK, None, None, SAKQXP
            ),
            FIKJPU: GeckoEnumStructAccessor(
                self.struct, FIKJPU, IKJPUN, None, WDAFIK, None, None, SAKQXP
            ),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, JPUNRJ, None, WDAFIK, None, None, SAKQXP
            ),
            PUNRJZ: GeckoEnumStructAccessor(
                self.struct, PUNRJZ, UNRJZT, None, WDAFIK, None, None, SAKQXP
            ),
            NRJZTA: GeckoEnumStructAccessor(
                self.struct, NRJZTA, RJZTAT, None, ZTATDZ, None, None, SAKQXP
            ),
            TATDZX: GeckoByteStructAccessor(self.struct, TATDZX, ATDZXN, SAKQXP),
            TDZXNQ: GeckoByteStructAccessor(self.struct, TDZXNQ, DZXNQT, SAKQXP),
            ZXNQTM: GeckoByteStructAccessor(self.struct, ZXNQTM, XNQTMF, SAKQXP),
            NQTMFZ: GeckoByteStructAccessor(self.struct, NQTMFZ, QTMFZD, SAKQXP),
            TMFZDG: GeckoByteStructAccessor(self.struct, TMFZDG, MFZDGK, SAKQXP),
            FZDGKE: GeckoByteStructAccessor(self.struct, FZDGKE, ZDGKEA, SAKQXP),
            DGKEAK: GeckoEnumStructAccessor(
                self.struct, DGKEAK, GKEAKS, None, EAKSTS, None, None, SAKQXP
            ),
            AKSTSE: GeckoEnumStructAccessor(
                self.struct, AKSTSE, RJZTAT, None, EAKSTS, None, None, SAKQXP
            ),
            KSTSEM: GeckoEnumStructAccessor(
                self.struct, KSTSEM, ATDZXN, None, EAKSTS, None, None, SAKQXP
            ),
            STSEMC: GeckoEnumStructAccessor(
                self.struct, STSEMC, DZXNQT, None, EAKSTS, None, None, SAKQXP
            ),
            TSEMCG: GeckoEnumStructAccessor(
                self.struct, TSEMCG, XNQTMF, None, EAKSTS, None, None, SAKQXP
            ),
            SEMCGE: GeckoEnumStructAccessor(
                self.struct, SEMCGE, QTMFZD, None, EAKSTS, None, None, SAKQXP
            ),
            EMCGET: GeckoEnumStructAccessor(
                self.struct, EMCGET, MFZDGK, None, EAKSTS, None, None, SAKQXP
            ),
            MCGETI: GeckoEnumStructAccessor(
                self.struct, MCGETI, CGETIX, None, GETIXQ, None, None, SAKQXP
            ),
            ETIXQV: GeckoEnumStructAccessor(
                self.struct, ETIXQV, ZDGKEA, None, GETIXQ, None, None, SAKQXP
            ),
            TIXQVX: GeckoByteStructAccessor(self.struct, TIXQVX, IXQVXO, SAKQXP),
            XQVXOI: GeckoByteStructAccessor(self.struct, XQVXOI, QVXOIH, SAKQXP),
            VXOIHB: GeckoByteStructAccessor(self.struct, VXOIHB, XOIHBX, SAKQXP),
            OIHBXI: GeckoByteStructAccessor(self.struct, OIHBXI, IHBXIB, SAKQXP),
            HBXIBH: GeckoByteStructAccessor(self.struct, HBXIBH, BXIBHZ, SAKQXP),
            XIBHZV: GeckoByteStructAccessor(self.struct, XIBHZV, IBHZVO, SAKQXP),
            BHZVOA: GeckoByteStructAccessor(self.struct, BHZVOA, HZVOAC, SAKQXP),
            ZVOACM: GeckoByteStructAccessor(self.struct, ZVOACM, VOACMC, SAKQXP),
            OACMCV: GeckoByteStructAccessor(self.struct, OACMCV, ACMCVD, SAKQXP),
            RXAIVE: GeckoBoolStructAccessor(self.struct, RXAIVE, JVHFTH, UQEXLS, None),
            XAIVEM: GeckoByteStructAccessor(self.struct, XAIVEM, AIVEMV, SAKQXP),
            IVEMVC: GeckoByteStructAccessor(self.struct, IVEMVC, VEMVCY, SAKQXP),
            EMVCYW: GeckoByteStructAccessor(self.struct, EMVCYW, MVCYWO, SAKQXP),
            VCYWON: GeckoEnumStructAccessor(
                self.struct, VCYWON, CYWONF, None, ZCZOLS, None, None, SAKQXP
            ),
            CZOLSI: GeckoBoolStructAccessor(
                self.struct, CZOLSI, ZOLSIP, ICXQIE, SAKQXP
            ),
            OLSIPM: GeckoBoolStructAccessor(self.struct, OLSIPM, MLOIJU, ICXQIE, None),
        }

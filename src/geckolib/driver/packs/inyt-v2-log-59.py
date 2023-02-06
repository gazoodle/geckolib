#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v59'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 49, 52])
ACQFFT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
AFIKJP = "".join(chr(c) for c in [83, 79, 117, 116, 57])
AHEOCT = 1
AIIDNI = 290
AJVDQL = "".join(chr(c) for c in [75, 54, 48, 48])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = 448
AMJMAO = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
AOAWBS = 284
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
AWBSIR = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
AZMKQT = 467
BBEKBD = "".join(chr(c) for c in [67, 70, 71, 50, 53])
BDFSRO = "".join(chr(c) for c in [67, 70, 71, 50, 55])
BDJQRJ = "".join(chr(c) for c in [75, 50, 48, 48])
BEKBDF = 473
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = 459
BIAMJM = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
BJEUTO = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
BJLOIN = "".join(
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
BLKXSJ = "".join(
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
BMJVHF = 256
BQFYLJ = 351
BQNRXC = 331
BQSNQL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
BSIRYX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
BVWVUB = 300
BWJYKL = 275
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 49, 48])
BXTIAC = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
BXYBQS = 314
BYGDSB = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = "".join(chr(c) for c in [67, 70, 71, 52])
CHWDAF = "".join(chr(c) for c in [70, 97, 110])
CMCVDS = 462
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CQFFTT = 291
CRTFMN = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
CTHBSK = 307
CVDSSR = 463
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
DAFIKJ = "".join(chr(c) for c in [83, 79, 117, 116, 56])
DDPMXF = "".join(chr(c) for c in [67, 70, 71, 51, 49])
DFSROG = 475
DGKEAK = 347
DJQRJJ = "".join(chr(c) for c in [75, 52, 48, 48])
DKHTZB = 470
DNIBXT = "".join(chr(c) for c in [52, 56, 75])
DNQGVU = "".join(chr(c) for c in [83, 79, 117, 116, 50])
DPMXFU = 479
DQLAII = "".join(chr(c) for c in [105, 110, 89, 84])
DSBDJQ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
DSSRUR = 464
DUBSSU = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
DZXNQT = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 48])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EJNIBX = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
EKBDFS = "".join(chr(c) for c in [67, 70, 71, 50, 54])
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
ELWUEU = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
EMCGET = "".join(chr(c) for c in [67, 70, 71, 51])
EOCTHB = 308
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 53])
EUHNNX = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
EUTOPH = "".join(chr(c) for c in [45, 45, 45])
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
EZFETD = 59
FCRTFM = "".join(chr(c) for c in [75, 51, 48, 48])
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FETDRX = 479
FFTTID = 293
FIKJPU = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
FJBIAM = 377
FMNHTB = 358
FSROGM = "".join(chr(c) for c in [67, 70, 71, 50, 56])
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
FUBJLO = "".join(
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
FWRKIN = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = "".join(
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
FZDGKE = 346
GETIXQ = 452
GKEAKS = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GMDDPM = "".join(chr(c) for c in [67, 70, 71, 51, 48])
GQPLSP = 279
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [80, 49, 76])
GVUNXN = 322
GYOUSP = 353
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
HBSKSO = 363
HBVWVU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
HBXIBH = 457
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HNNXWE = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
HTBJEU = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
HTZBBE = 471
HUGTYI = "".join(chr(c) for c in [78, 65])
HUOJRJ = 305
HXEKVK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 49, 50])
IAMJMA = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 49, 49])
IBXYBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [51, 50, 75])
IDUBSS = 295
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
IGYOUS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 57])
IIDNIB = "".join(chr(c) for c in [49, 54, 75])
IJUGSE = 327
IKFWRK = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
IKJPUN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
ILXWAJ = "".join(chr(c) for c in [77, 73, 65])
INEJNI = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
INELWU = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IRYXBQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
IUSOOQ = "".join(chr(c) for c in [80, 49])
IUXFEF = "".join(chr(c) for c in [73, 68, 76, 69])
IVDNQG = "".join(chr(c) for c in [65, 85, 88])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 54])
IYWSKW = "".join(chr(c) for c in [80, 51, 72])
JBIAMJ = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
JEUTOP = 376
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JJJVYF = "".join(chr(c) for c in [75, 53])
JJVYFC = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
JLOINE = 373
JMAOAW = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
JMCBFE = 260
JNIBXY = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
JPUNRJ = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
JQRJJJ = "".join(chr(c) for c in [75, 56, 53])
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
JUIKFW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVDQLA = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [75, 49, 48, 48])
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYKLGQ = 277
JYMOUN = 272
JZTATD = 340
KBDFSR = 474
KCWAON = 365
KEAKST = 348
KFWRKI = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
KHTZBB = "".join(chr(c) for c in [67, 70, 71, 50, 51])
KINEJN = 309
KJPUNR = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
KMLOIJ = 326
KPHUOJ = 304
KQTDKH = "".join(chr(c) for c in [67, 70, 71, 50, 49])
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49])
KVKZIL = 289
KWIVDN = "".join(chr(c) for c in [66, 76, 79])
KXSJWM = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KZILXW = "".join(chr(c) for c in [105, 110, 88, 69])
LAIIDN = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
LHBQNR = 330
LIUXFE = 263
LJUIKF = "".join(
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
LKXSJW = "".join(chr(c) for c in [67, 80, 79, 84])
LNMHXE = 285
LOINEL = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 280
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LWUEUH = "".join(
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
LXWAJV = "".join(chr(c) for c in [68, 74, 83, 52])
MAOAWB = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
MCGETI = 451
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 49, 53])
MDDPMX = 478
MFZDGK = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
MHXEKV = 287
MJIGYO = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
MJMAOA = 283
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 468
MLOIJU = "".join(chr(c) for c in [72, 84, 82])
MNHTBJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
MNZMJI = 313
MOUNBL = 273
MXFUBJ = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
NBLKXS = "".join(
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
NELWUE = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
NHTBJE = 360
NIBXTI = "".join(chr(c) for c in [54, 52, 75])
NIBXYB = 311
NKMLOI = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
NMHXEK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = 321
NQJYMO = 271
NQLNMH = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
NQTMFZ = 344
NRJZTA = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = 333
NXNKML = "".join(chr(c) for c in [83, 79, 117, 116, 53])
NXWEEZ = "".join(chr(c) for c in [76, 73])
NZMJIG = "".join(chr(c) for c in [78, 79])
OACMCV = 461
OAWBSI = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = 477
OIHBXI = 456
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
OINELW = 374
OJRJHI = 306
OKPHUO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
ONPYYL = 262
OOQNRS = "".join(chr(c) for c in [76, 79, 87])
OPHUGT = "".join(chr(c) for c in [83, 79, 117, 116, 49])
OUNBLK = "".join(chr(c) for c in [80, 117, 114, 103, 101])
OUSPBW = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
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
PBWJYK = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
PFTSIF = 281
PHUGTY = 320
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
PMXFUB = "".join(
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
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PUNRJZ = 332
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
QFYLJU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
QGVUNX = "".join(chr(c) for c in [83, 79, 117, 116, 51])
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
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
QPLSPF = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
QRJJJV = "".join(chr(c) for c in [75, 56])
QSNQLN = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
QTDKHT = 469
QTMFZD = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 55])
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 49, 57])
RJHIUS = 362
RJJJVY = "".join(chr(c) for c in [75, 52])
RJZTAT = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
RKINEJ = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
ROGMDD = "".join(chr(c) for c in [67, 70, 71, 50, 57])
RSJMCB = "".join(chr(c) for c in [80, 52])
RURAZM = "".join(chr(c) for c in [67, 70, 71, 49, 56])
RXCHWD = "".join(chr(c) for c in [83, 79, 117, 116, 54])
RYXBQF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = 357
SELHBQ = 329
SEMCGE = 450
SIFJBI = 352
SIRYXB = 350
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
SKSOKP = 370
SKWIVD = "".join(chr(c) for c in [80, 52, 76])
SNQLNM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SPFTSI = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
SROGMD = 476
SRURAZ = 465
SSRURA = "".join(chr(c) for c in [67, 70, 71, 49, 55])
SSUHBV = 297
STSEMC = 449
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
SXUJUT = 310
TACCPQ = 264
TATDZX = 341
TBJEUT = 361
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 50, 50])
TDZXNQ = 342
TFMNHT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [67, 69])
TIDUBS = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
TIXQVX = 453
TMFZDG = 345
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 50])
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
TTIDUB = 294
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [80, 50, 72])
TZBBEK = "".join(chr(c) for c in [67, 70, 71, 50, 52])
UBJLOI = 372
UBSSUH = 296
UBYGDS = 316
UGSELH = 328
UGTYIY = "".join(chr(c) for c in [80, 49, 72])
UHBVWV = 299
UHNNXW = 375
UIKFWR = 354
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
UNXNKM = 323
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = 466
USOOQN = 261
USPBWJ = 355
UTOPHU = "".join(chr(c) for c in [82, 69, 83, 69, 84])
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VDQLAI = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 49, 54])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 49, 51])
VUBYGD = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
VUNXNK = "".join(chr(c) for c in [83, 79, 117, 116, 52])
VWVUBY = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
VXOIHB = 455
VYFCRT = "".join(chr(c) for c in [75, 56, 48, 48])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [105, 110, 88, 77])
WAONPY = 367
WBSIRY = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
WDAFIK = "".join(chr(c) for c in [83, 79, 117, 116, 55])
WIVDNQ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
WJYKLG = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
WMNZMJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
WRKINE = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
WSKWIV = "".join(chr(c) for c in [80, 52, 72])
WUEUHN = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
WVUBYG = 301
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
XCHWDA = 325
XEKVKZ = 288
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XFUBJL = 371
XIBHZV = 458
XLSXUJ = 7
XNKMLO = 324
XNQTMF = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 56])
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = 454
XSJWMN = 282
XTIACQ = "".join(chr(c) for c in [85, 76])
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
XYBQSN = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
YBQSNQ = 315
YEKCWA = 364
YFCRTF = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
YGDSBD = "".join(chr(c) for c in [70, 117, 108, 108])
YIYWSK = "".join(chr(c) for c in [80, 50, 76])
YKLGQP = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
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
YMOUNB = "".join(chr(c) for c in [67, 108, 101, 97, 110])
YNQJYM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
YOUSPB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWSKWI = "".join(chr(c) for c in [80, 51, 76])
YXBQFY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 472
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
ZFETDR = 256
ZILXWA = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
ZMJIGY = "".join(chr(c) for c in [77, 69, 68])
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 50, 48])
ZTATDZ = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = 460
ZXNQTM = 343
EEZFET = [
    QSNQLN,
    QFYLJU,
    LJUIKF,
    OAWBSI,
    SPBWJY,
    EJNIBX,
    BQSNQL,
    SNQLNM,
    LGQPLS,
    BLKXSJ,
    YXBQFY,
    BSIRYX,
    JBIAMJ,
    TSIFJB,
    XYBQSN,
    WBSIRY,
    XBQFYL,
    RYXBQF,
    JMAOAW,
    JUIKFW,
    AMJMAO,
    BIAMJM,
    FYLJUI,
    FWRKIN,
    YLJUIK,
    IAMJMA,
    IRYXBQ,
    AWBSIR,
    MAOAWB,
]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
GDSBDJ = [BYGDSB, YGDSBD]
HWDAFI = [
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    SJMCBF,
    KWIVDN,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    CHWDAF,
    HECVYY,
    HECVYY,
    WIVDNQ,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    IVDNQG,
]
IACQFF = [XTIACQ, TIACQF]
IBXTIA = [IIDNIB, IDNIBX, DNIBXT, NIBXTI]
JIGYOU = [NZMJIG, QXPICX, ZMJIGY, XPICXQ, MJIGYO]
KLGQPL = [HECVYY, YKLGQP, YKLGQP, YKLGQP]
LOIJUG = [
    HUGTYI,
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
    MLOIJU,
]
MCBFEG = [ASSAKQ, SOOQNR]
NEJNIB = [HECVYY, INEJNI, INEJNI, INEJNI]
NNXWEE = []
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
QGLRAH = [ASSAKQ, XPICXQ]
QLAIID = [
    VKZILX,
    KZILXW,
    ZILXWA,
    ILXWAJ,
    LXWAJV,
    XWAJVD,
    WAJVDQ,
    AJVDQL,
    JVDQLA,
    VDQLAI,
    DQLAII,
]
RAHEOC = [ASSAKQ, LRAHEO]
RTFMNH = [
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    HECVYY,
    HECVYY,
    HECVYY,
    YFCRTF,
    FCRTFM,
    CRTFMN,
]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
TOPHUG = [EUTOPH, UTOPHU]
UEUHNN = [INELWU, NELWUE, ELWUEU, LWUEUH, WUEUHN]
UNRJZT = [
    HUGTYI,
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
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
VDNQGV = [
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    SJMCBF,
    KWIVDN,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    WIVDNQ,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    IVDNQG,
]
WEEZFE = [
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
XWEEZF = [
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
    NXWEEZ,
]
YYLIUX = [NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return EZFETD

    @property
    def begin(self):
        return ZFETDR

    @property
    def end(self):
        return FETDRX

    @property
    def all_device_keys(self):
        return XWEEZF

    @property
    def user_demand_keys(self):
        return WEEZFE

    @property
    def error_keys(self):
        return EEZFET

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
            YMOUNB: GeckoBoolStructAccessor(self.struct, YMOUNB, MOUNBL, ICXQIE, None),
            OUNBLK: GeckoBoolStructAccessor(self.struct, OUNBLK, MOUNBL, QIEFXQ, None),
            UNBLKX: GeckoBoolStructAccessor(self.struct, UNBLKX, MOUNBL, EGZUQE, None),
            NBLKXS: GeckoBoolStructAccessor(self.struct, NBLKXS, MOUNBL, CXQIEF, None),
            BLKXSJ: GeckoBoolStructAccessor(self.struct, BLKXSJ, MOUNBL, UQEXLS, None),
            LKXSJW: GeckoBoolStructAccessor(self.struct, LKXSJW, JVHFTH, QIEFXQ, None),
            KXSJWM: GeckoBoolStructAccessor(self.struct, KXSJWM, XSJWMN, EGZUQE, None),
            SJWMNZ: GeckoBoolStructAccessor(self.struct, SJWMNZ, XSJWMN, UQEXLS, None),
            JWMNZM: GeckoBoolStructAccessor(self.struct, JWMNZM, XSJWMN, VHFTHE, None),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, MNZMJI, None, JIGYOU, None, None, None
            ),
            IGYOUS: GeckoBoolStructAccessor(self.struct, IGYOUS, GYOUSP, UQEXLS, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, GYOUSP, VHFTHE, None),
            OUSPBW: GeckoWordStructAccessor(self.struct, OUSPBW, USPBWJ, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, JVHFTH, AHEOCT, None),
            PBWJYK: GeckoTempStructAccessor(self.struct, PBWJYK, BWJYKL, None),
            WJYKLG: GeckoTempStructAccessor(self.struct, WJYKLG, JYKLGQ, None),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, JMCBFE, UQEXLS, KLGQPL, None, CXQIEF, None
            ),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, GQPLSP, QIEFXQ, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, GQPLSP, VHFTHE, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, LSPFTS, QIEFXQ, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, AHEOCT, None),
            FTSIFJ: GeckoBoolStructAccessor(
                self.struct, FTSIFJ, PFTSIF, QIEFXQ, SAKQXP
            ),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, SIFJBI, AHEOCT, None),
            IFJBIA: GeckoByteStructAccessor(self.struct, IFJBIA, FJBIAM, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, JVHFTH, EGZUQE, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, XSJWMN, ICXQIE, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, XSJWMN, AHEOCT, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, MJMAOA, QIEFXQ, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MJMAOA, EGZUQE, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, AOAWBS, EGZUQE, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, AOAWBS, CXQIEF, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, AOAWBS, UQEXLS, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, AOAWBS, VHFTHE, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, SIRYXB, EGZUQE, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, SIRYXB, CXQIEF, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, SIRYXB, UQEXLS, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, SIRYXB, VHFTHE, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, QIEFXQ, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, BQFYLJ, EGZUQE, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, SIFJBI, EGZUQE, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, GYOUSP, ICXQIE, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, GYOUSP, AHEOCT, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, UIKFWR, ICXQIE, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, LSPFTS, ICXQIE, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, MJMAOA, ICXQIE, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, MJMAOA, AHEOCT, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, MJMAOA, CXQIEF, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, KINEJN, ICXQIE, None),
            INEJNI: GeckoEnumStructAccessor(
                self.struct, INEJNI, KINEJN, AHEOCT, NEJNIB, None, CXQIEF, None
            ),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, KINEJN, EGZUQE, None),
            JNIBXY: GeckoWordStructAccessor(self.struct, JNIBXY, NIBXYB, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BXYBQS, ICXQIE, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, YBQSNQ, ICXQIE, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, YBQSNQ, AHEOCT, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, BQFYLJ, ICXQIE, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, BQFYLJ, AHEOCT, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, BQFYLJ, CXQIEF, None),
            QLNMHX: GeckoWordStructAccessor(self.struct, QLNMHX, LNMHXE, None),
            NMHXEK: GeckoByteStructAccessor(self.struct, NMHXEK, MHXEKV, None),
            HXEKVK: GeckoByteStructAccessor(self.struct, HXEKVK, XEKVKZ, None),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, QLAIID, None, None, None
            ),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AIIDNI, ICXQIE, IBXTIA, None, CXQIEF, None
            ),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, AIIDNI, QIEFXQ, IACQFF, None, QIEFXQ, None
            ),
            ACQFFT: GeckoWordStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, None),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, None),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, None),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, None),
            BSSUHB: GeckoWordStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, None),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoWordStructAccessor(self.struct, VWVUBY, WVUBYG, None),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, GDSBDJ, None, QIEFXQ, SAKQXP
            ),
            DSBDJQ: GeckoEnumStructAccessor(
                self.struct, DSBDJQ, SBDJQR, None, RTFMNH, None, None, None
            ),
            TFMNHT: GeckoWordStructAccessor(self.struct, TFMNHT, FMNHTB, None),
            MNHTBJ: GeckoByteStructAccessor(self.struct, MNHTBJ, NHTBJE, None),
            HTBJEU: GeckoByteStructAccessor(self.struct, HTBJEU, TBJEUT, None),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, JEUTOP, None, TOPHUG, None, None, SAKQXP
            ),
            OPHUGT: GeckoEnumStructAccessor(
                self.struct, OPHUGT, PHUGTY, None, VDNQGV, None, None, SAKQXP
            ),
            DNQGVU: GeckoEnumStructAccessor(
                self.struct, DNQGVU, NQGVUN, None, VDNQGV, None, None, SAKQXP
            ),
            QGVUNX: GeckoEnumStructAccessor(
                self.struct, QGVUNX, GVUNXN, None, VDNQGV, None, None, SAKQXP
            ),
            VUNXNK: GeckoEnumStructAccessor(
                self.struct, VUNXNK, UNXNKM, None, VDNQGV, None, None, SAKQXP
            ),
            NXNKML: GeckoEnumStructAccessor(
                self.struct, NXNKML, XNKMLO, None, VDNQGV, None, None, SAKQXP
            ),
            NKMLOI: GeckoEnumStructAccessor(
                self.struct, NKMLOI, KMLOIJ, None, LOIJUG, None, None, SAKQXP
            ),
            OIJUGS: GeckoByteStructAccessor(self.struct, OIJUGS, IJUGSE, SAKQXP),
            JUGSEL: GeckoByteStructAccessor(self.struct, JUGSEL, UGSELH, SAKQXP),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, SAKQXP),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, SAKQXP),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, SAKQXP),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, SAKQXP),
            RXCHWD: GeckoEnumStructAccessor(
                self.struct, RXCHWD, XCHWDA, None, HWDAFI, None, None, SAKQXP
            ),
            WDAFIK: GeckoEnumStructAccessor(
                self.struct, WDAFIK, KMLOIJ, None, HWDAFI, None, None, SAKQXP
            ),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, IJUGSE, None, HWDAFI, None, None, SAKQXP
            ),
            AFIKJP: GeckoEnumStructAccessor(
                self.struct, AFIKJP, UGSELH, None, HWDAFI, None, None, SAKQXP
            ),
            FIKJPU: GeckoEnumStructAccessor(
                self.struct, FIKJPU, SELHBQ, None, HWDAFI, None, None, SAKQXP
            ),
            IKJPUN: GeckoEnumStructAccessor(
                self.struct, IKJPUN, LHBQNR, None, HWDAFI, None, None, SAKQXP
            ),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, BQNRXC, None, HWDAFI, None, None, SAKQXP
            ),
            JPUNRJ: GeckoEnumStructAccessor(
                self.struct, JPUNRJ, PUNRJZ, None, UNRJZT, None, None, SAKQXP
            ),
            NRJZTA: GeckoEnumStructAccessor(
                self.struct, NRJZTA, NRXCHW, None, UNRJZT, None, None, SAKQXP
            ),
            RJZTAT: GeckoByteStructAccessor(self.struct, RJZTAT, JZTATD, SAKQXP),
            ZTATDZ: GeckoByteStructAccessor(self.struct, ZTATDZ, TATDZX, SAKQXP),
            ATDZXN: GeckoByteStructAccessor(self.struct, ATDZXN, TDZXNQ, SAKQXP),
            DZXNQT: GeckoByteStructAccessor(self.struct, DZXNQT, ZXNQTM, SAKQXP),
            XNQTMF: GeckoByteStructAccessor(self.struct, XNQTMF, NQTMFZ, SAKQXP),
            QTMFZD: GeckoByteStructAccessor(self.struct, QTMFZD, TMFZDG, SAKQXP),
            MFZDGK: GeckoByteStructAccessor(self.struct, MFZDGK, FZDGKE, SAKQXP),
            ZDGKEA: GeckoByteStructAccessor(self.struct, ZDGKEA, DGKEAK, SAKQXP),
            GKEAKS: GeckoByteStructAccessor(self.struct, GKEAKS, KEAKST, SAKQXP),
            PMXFUB: GeckoBoolStructAccessor(self.struct, PMXFUB, JVHFTH, UQEXLS, None),
            MXFUBJ: GeckoByteStructAccessor(self.struct, MXFUBJ, XFUBJL, SAKQXP),
            FUBJLO: GeckoByteStructAccessor(self.struct, FUBJLO, UBJLOI, SAKQXP),
            BJLOIN: GeckoByteStructAccessor(self.struct, BJLOIN, JLOINE, SAKQXP),
            LOINEL: GeckoEnumStructAccessor(
                self.struct, LOINEL, OINELW, None, UEUHNN, None, None, SAKQXP
            ),
            EUHNNX: GeckoBoolStructAccessor(
                self.struct, EUHNNX, UHNNXW, ICXQIE, SAKQXP
            ),
            HNNXWE: GeckoBoolStructAccessor(self.struct, HNNXWE, JEUTOP, ICXQIE, None),
        }

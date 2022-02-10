#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v58'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 49, 53])
ACQFFT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
AFIKJP = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [51, 50, 75])
AJVDQL = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = 449
AMJMAO = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
AOAWBS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
AWBSIR = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
AZMKQT = 468
BBEKBD = "".join(chr(c) for c in [67, 70, 71, 50, 54])
BDFSRO = "".join(chr(c) for c in [67, 70, 71, 50, 56])
BDJQRJ = "".join(chr(c) for c in [75, 56, 53])
BEKBDF = 474
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = 460
BIAMJM = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
BJEUTO = "".join(chr(c) for c in [45, 45, 45])
BJLOIN = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
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
BQFYLJ = "".join(
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
BQNRXC = 333
BQSNQL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
BSIRYX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
BVWVUB = 301
BWJYKL = 275
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 49, 49])
BXTIAC = "".join(chr(c) for c in [67, 69])
BXYBQS = 315
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = "".join(chr(c) for c in [67, 70, 71, 53])
CHWDAF = "".join(chr(c) for c in [83, 79, 117, 116, 55])
CMCVDS = 463
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CQFFTT = 293
CRTFMN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
CTHBSK = 307
CVDSSR = 464
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
DAFIKJ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
DDPMXF = "".join(
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
DFSROG = 476
DGKEAK = 348
DJQRJJ = "".join(chr(c) for c in [75, 56])
DKHTZB = 471
DNQGVU = "".join(chr(c) for c in [83, 79, 117, 116, 51])
DPMXFU = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
DQLAII = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
DSBDJQ = "".join(chr(c) for c in [75, 50, 48, 48])
DSSRUR = 465
DUBSSU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
DZXNQT = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 479
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EJNIBX = 311
EKBDFS = "".join(chr(c) for c in [67, 70, 71, 50, 55])
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
ELWUEU = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 52])
EOCTHB = 308
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 54])
EUHNNX = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FFTTID = 294
FIKJPU = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
FJBIAM = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
FMNHTB = 360
FSROGM = "".join(chr(c) for c in [67, 70, 71, 50, 57])
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
FTTIDU = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
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
        97,
        120,
        105,
        109,
        117,
        109,
    ]
)
FWRKIN = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
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
FZDGKE = 347
GDSBDJ = 357
GETIXQ = 453
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 48])
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GMDDPM = "".join(chr(c) for c in [67, 70, 71, 51, 49])
GQPLSP = 279
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [80, 50, 76])
GVUNXN = 323
GYOUSP = 353
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
HBSKSO = 363
HBVWVU = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
HBXIBH = 458
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HNNXWE = "".join(chr(c) for c in [76, 73])
HTBJEU = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
HTZBBE = 472
HUGTYI = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = 305
HWDAFI = "".join(chr(c) for c in [83, 79, 117, 116, 56])
HXEKVK = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 49, 51])
IACQFF = 291
IAMJMA = 283
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 49, 50])
IBXTIA = "".join(chr(c) for c in [85, 76])
IBXYBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [54, 52, 75])
IDUBSS = 296
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
IGYOUS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 49, 48])
IIDNIB = "".join(chr(c) for c in [52, 56, 75])
IJUGSE = 328
IKFWRK = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IKJPUN = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
ILXWAJ = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
INEJNI = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
INELWU = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IRYXBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
IUSOOQ = "".join(chr(c) for c in [80, 49])
IUXFEF = "".join(chr(c) for c in [73, 68, 76, 69])
IVDNQG = "".join(chr(c) for c in [83, 79, 117, 116, 50])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 55])
IYWSKW = "".join(chr(c) for c in [80, 52, 72])
JBIAMJ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
JEUTOP = "".join(chr(c) for c in [82, 69, 83, 69, 84])
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JJJVYF = "".join(chr(c) for c in [75, 49, 48, 48])
JJVYFC = "".join(chr(c) for c in [75, 56, 48, 48])
JLOINE = 374
JMAOAW = 284
JMCBFE = 260
JNIBXY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JQRJJJ = "".join(chr(c) for c in [75, 52])
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
JUIKFW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVDQLA = "".join(chr(c) for c in [105, 110, 89, 84])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYKLGQ = 277
JYMOUN = 272
JZTATD = 341
KBDFSR = 475
KCWAON = 365
KEAKST = 448
KFWRKI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
KHTZBB = "".join(chr(c) for c in [67, 70, 71, 50, 52])
KJPUNR = 332
KPHUOJ = 304
KQTDKH = "".join(chr(c) for c in [67, 70, 71, 50, 50])
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 50])
KVKZIL = "".join(chr(c) for c in [105, 110, 88, 69])
KWIVDN = "".join(chr(c) for c in [65, 85, 88])
KXSJWM = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KZILXW = "".join(chr(c) for c in [77, 73, 65])
LAIIDN = "".join(chr(c) for c in [49, 54, 75])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
LHBQNR = 331
LIUXFE = 263
LJUIKF = 354
LKXSJW = "".join(chr(c) for c in [67, 80, 79, 84])
LNMHXE = 287
LOIJUG = 327
LOINEL = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 280
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LXWAJV = "".join(chr(c) for c in [105, 110, 88, 77])
MAOAWB = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
MCGETI = 452
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 49, 54])
MDDPMX = 479
MFZDGK = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
MHXEKV = 288
MJIGYO = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
MJMAOA = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 469
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
MNHTBJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
MNZMJI = 313
MOUNBL = 273
MXFUBJ = "".join(
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
NEJNIB = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
NELWUE = "".join(
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
NHTBJE = 361
NIBXTI = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
NIBXYB = 314
NKMLOI = "".join(chr(c) for c in [72, 84, 82])
NMHXEK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = 322
NQJYMO = 271
NQLNMH = 285
NQTMFZ = 345
NRJZTA = 340
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = 325
NXNKML = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
NZMJIG = "".join(chr(c) for c in [78, 79])
OACMCV = 462
OAWBSI = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = 478
OIHBXI = 457
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
OINELW = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
OJRJHI = 306
OKPHUO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
ONPYYL = 262
OOQNRS = "".join(chr(c) for c in [76, 79, 87])
OPHUGT = "".join(chr(c) for c in [78, 65])
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
PHUGTY = "".join(chr(c) for c in [80, 49, 72])
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
PMXFUB = 371
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PUNRJZ = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
QFYLJU = "".join(
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
QGVUNX = "".join(chr(c) for c in [83, 79, 117, 116, 52])
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
QLAIID = 290
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 54])
QPLSPF = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
QRJJJV = "".join(chr(c) for c in [75, 53])
QSNQLN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
QTDKHT = 470
QTMFZD = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 56])
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 50, 48])
RJHIUS = 362
RJJJVY = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
RJZTAT = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
RKINEJ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
ROGMDD = "".join(chr(c) for c in [67, 70, 71, 51, 48])
RSJMCB = "".join(chr(c) for c in [80, 52])
RTFMNH = 358
RURAZM = "".join(chr(c) for c in [67, 70, 71, 49, 57])
RXCHWD = "".join(chr(c) for c in [70, 97, 110])
RYXBQF = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [75, 52, 48, 48])
SELHBQ = 330
SEMCGE = 451
SIFJBI = 352
SIRYXB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
SKSOKP = 370
SKWIVD = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SNQLNM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SPFTSI = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
SROGMD = 477
SRURAZ = 466
SSRURA = "".join(chr(c) for c in [67, 70, 71, 49, 56])
SSUHBV = 299
STSEMC = 450
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
SXUJUT = 310
TACCPQ = 264
TATDZX = 342
TBJEUT = 376
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 50, 51])
TDZXNQ = 343
TFMNHT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
TIDUBS = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
TIXQVX = 454
TMFZDG = 346
TOPHUG = 320
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 51])
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
TTIDUB = 295
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [80, 51, 72])
TZBBEK = "".join(chr(c) for c in [67, 70, 71, 50, 53])
UBJLOI = 373
UBSSUH = 297
UBYGDS = "".join(chr(c) for c in [70, 117, 108, 108])
UEUHNN = 375
UGSELH = 329
UGTYIY = "".join(chr(c) for c in [80, 50, 72])
UHBVWV = 300
UIKFWR = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
UNRJZT = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
UNXNKM = 324
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = 467
USOOQN = 261
USPBWJ = 355
UTOPHU = "".join(chr(c) for c in [83, 79, 117, 116, 49])
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VDNQGV = 321
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 49, 55])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 49, 52])
VUBYGD = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
VUNXNK = "".join(chr(c) for c in [83, 79, 117, 116, 53])
VWVUBY = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
VXOIHB = 456
VYFCRT = "".join(chr(c) for c in [75, 51, 48, 48])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
WAONPY = 367
WBSIRY = 350
WDAFIK = "".join(chr(c) for c in [83, 79, 117, 116, 57])
WEEZFE = 256
WJYKLG = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
WMNZMJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
WRKINE = 309
WSKWIV = "".join(chr(c) for c in [66, 76, 79])
WUEUHN = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
WVUBYG = 316
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
XEKVKZ = 289
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XFUBJL = 372
XIBHZV = 459
XLSXUJ = 7
XNKMLO = 326
XNQTMF = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 57])
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = 455
XSJWMN = 282
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [75, 54, 48, 48])
XWEEZF = 58
XYBQSN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
YBQSNQ = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
YEKCWA = 364
YFCRTF = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
YGDSBD = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
YIYWSK = "".join(chr(c) for c in [80, 51, 76])
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
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
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
YWSKWI = "".join(chr(c) for c in [80, 52, 76])
YXBQFY = 351
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 473
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
ZILXWA = "".join(chr(c) for c in [68, 74, 83, 52])
ZMJIGY = "".join(chr(c) for c in [77, 69, 68])
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 50, 49])
ZTATDZ = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = 461
ZXNQTM = 344
BYGDSB = [VUBYGD, UBYGDS]
DNIBXT = [LAIIDN, AIIDNI, IIDNIB, IDNIBX]
EUTOPH = [BJEUTO, JEUTOP]
FCRTFM = [
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
    HECVYY,
    HECVYY,
    HECVYY,
    JVYFCR,
    VYFCRT,
    YFCRTF,
]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
JIGYOU = [NZMJIG, QXPICX, ZMJIGY, XPICXQ, MJIGYO]
JPUNRJ = [
    OPHUGT,
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
KINEJN = [HECVYY, RKINEJ, RKINEJ, RKINEJ]
KLGQPL = [HECVYY, YKLGQP, YKLGQP, YKLGQP]
KMLOIJ = [
    OPHUGT,
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
    NKMLOI,
]
LWUEUH = [LOINEL, OINELW, INELWU, NELWUE, ELWUEU]
MCBFEG = [ASSAKQ, SOOQNR]
NNXWEE = [
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
    HNNXWE,
]
NXWEEZ = [
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
RAHEOC = [ASSAKQ, LRAHEO]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
UHNNXW = []
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
VDQLAI = [
    EKVKZI,
    KVKZIL,
    VKZILX,
    KZILXW,
    ZILXWA,
    ILXWAJ,
    LXWAJV,
    XWAJVD,
    WAJVDQ,
    AJVDQL,
    JVDQLA,
]
WIVDNQ = [
    OPHUGT,
    PHUGTY,
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    SJMCBF,
    WSKWIV,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    SKWIVD,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    KWIVDN,
]
XCHWDA = [
    OPHUGT,
    PHUGTY,
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    SJMCBF,
    WSKWIV,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    RXCHWD,
    HECVYY,
    HECVYY,
    SKWIVD,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    KWIVDN,
]
XTIACQ = [IBXTIA, BXTIAC]
YYLIUX = [NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return XWEEZF

    @property
    def begin(self):
        return WEEZFE

    @property
    def end(self):
        return EEZFET

    @property
    def all_device_keys(self):
        return NNXWEE

    @property
    def user_demand_keys(self):
        return NXWEEZ

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
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, JVHFTH, EGZUQE, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, XSJWMN, ICXQIE, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, XSJWMN, AHEOCT, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, QIEFXQ, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, IAMJMA, EGZUQE, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, EGZUQE, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, JMAOAW, CXQIEF, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, JMAOAW, UQEXLS, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, JMAOAW, VHFTHE, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, WBSIRY, EGZUQE, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, WBSIRY, CXQIEF, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, WBSIRY, UQEXLS, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, WBSIRY, VHFTHE, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, YXBQFY, QIEFXQ, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, YXBQFY, EGZUQE, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, SIFJBI, EGZUQE, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, GYOUSP, ICXQIE, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, GYOUSP, AHEOCT, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, LJUIKF, ICXQIE, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, LSPFTS, ICXQIE, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, IAMJMA, ICXQIE, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, IAMJMA, AHEOCT, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, IAMJMA, CXQIEF, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, WRKINE, ICXQIE, None),
            RKINEJ: GeckoEnumStructAccessor(
                self.struct, RKINEJ, WRKINE, AHEOCT, KINEJN, None, CXQIEF, None
            ),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, WRKINE, EGZUQE, None),
            NEJNIB: GeckoWordStructAccessor(self.struct, NEJNIB, EJNIBX, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, NIBXYB, ICXQIE, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BXYBQS, ICXQIE, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, BXYBQS, AHEOCT, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, YXBQFY, ICXQIE, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, YXBQFY, AHEOCT, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, YXBQFY, CXQIEF, None),
            SNQLNM: GeckoWordStructAccessor(self.struct, SNQLNM, NQLNMH, None),
            QLNMHX: GeckoByteStructAccessor(self.struct, QLNMHX, LNMHXE, None),
            NMHXEK: GeckoByteStructAccessor(self.struct, NMHXEK, MHXEKV, None),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, XEKVKZ, None, VDQLAI, None, None, None
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, QLAIID, ICXQIE, DNIBXT, None, CXQIEF, None
            ),
            NIBXTI: GeckoEnumStructAccessor(
                self.struct, NIBXTI, QLAIID, QIEFXQ, XTIACQ, None, QIEFXQ, None
            ),
            TIACQF: GeckoWordStructAccessor(self.struct, TIACQF, IACQFF, None),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, None),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, None),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, None),
            DUBSSU: GeckoWordStructAccessor(self.struct, DUBSSU, UBSSUH, None),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, None),
            HBVWVU: GeckoWordStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoEnumStructAccessor(
                self.struct, VWVUBY, WVUBYG, None, BYGDSB, None, QIEFXQ, SAKQXP
            ),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, GDSBDJ, None, FCRTFM, None, None, None
            ),
            CRTFMN: GeckoWordStructAccessor(self.struct, CRTFMN, RTFMNH, None),
            TFMNHT: GeckoByteStructAccessor(self.struct, TFMNHT, FMNHTB, None),
            MNHTBJ: GeckoByteStructAccessor(self.struct, MNHTBJ, NHTBJE, None),
            HTBJEU: GeckoEnumStructAccessor(
                self.struct, HTBJEU, TBJEUT, None, EUTOPH, None, None, SAKQXP
            ),
            UTOPHU: GeckoEnumStructAccessor(
                self.struct, UTOPHU, TOPHUG, None, WIVDNQ, None, None, SAKQXP
            ),
            IVDNQG: GeckoEnumStructAccessor(
                self.struct, IVDNQG, VDNQGV, None, WIVDNQ, None, None, SAKQXP
            ),
            DNQGVU: GeckoEnumStructAccessor(
                self.struct, DNQGVU, NQGVUN, None, WIVDNQ, None, None, SAKQXP
            ),
            QGVUNX: GeckoEnumStructAccessor(
                self.struct, QGVUNX, GVUNXN, None, WIVDNQ, None, None, SAKQXP
            ),
            VUNXNK: GeckoEnumStructAccessor(
                self.struct, VUNXNK, UNXNKM, None, WIVDNQ, None, None, SAKQXP
            ),
            NXNKML: GeckoEnumStructAccessor(
                self.struct, NXNKML, XNKMLO, None, KMLOIJ, None, None, SAKQXP
            ),
            MLOIJU: GeckoByteStructAccessor(self.struct, MLOIJU, LOIJUG, SAKQXP),
            OIJUGS: GeckoByteStructAccessor(self.struct, OIJUGS, IJUGSE, SAKQXP),
            JUGSEL: GeckoByteStructAccessor(self.struct, JUGSEL, UGSELH, SAKQXP),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, SAKQXP),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, SAKQXP),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, SAKQXP),
            QNRXCH: GeckoEnumStructAccessor(
                self.struct, QNRXCH, NRXCHW, None, XCHWDA, None, None, SAKQXP
            ),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, XNKMLO, None, XCHWDA, None, None, SAKQXP
            ),
            HWDAFI: GeckoEnumStructAccessor(
                self.struct, HWDAFI, LOIJUG, None, XCHWDA, None, None, SAKQXP
            ),
            WDAFIK: GeckoEnumStructAccessor(
                self.struct, WDAFIK, IJUGSE, None, XCHWDA, None, None, SAKQXP
            ),
            DAFIKJ: GeckoEnumStructAccessor(
                self.struct, DAFIKJ, UGSELH, None, XCHWDA, None, None, SAKQXP
            ),
            AFIKJP: GeckoEnumStructAccessor(
                self.struct, AFIKJP, SELHBQ, None, XCHWDA, None, None, SAKQXP
            ),
            FIKJPU: GeckoEnumStructAccessor(
                self.struct, FIKJPU, LHBQNR, None, XCHWDA, None, None, SAKQXP
            ),
            IKJPUN: GeckoEnumStructAccessor(
                self.struct, IKJPUN, KJPUNR, None, JPUNRJ, None, None, SAKQXP
            ),
            PUNRJZ: GeckoEnumStructAccessor(
                self.struct, PUNRJZ, BQNRXC, None, JPUNRJ, None, None, SAKQXP
            ),
            UNRJZT: GeckoByteStructAccessor(self.struct, UNRJZT, NRJZTA, SAKQXP),
            RJZTAT: GeckoByteStructAccessor(self.struct, RJZTAT, JZTATD, SAKQXP),
            ZTATDZ: GeckoByteStructAccessor(self.struct, ZTATDZ, TATDZX, SAKQXP),
            ATDZXN: GeckoByteStructAccessor(self.struct, ATDZXN, TDZXNQ, SAKQXP),
            DZXNQT: GeckoByteStructAccessor(self.struct, DZXNQT, ZXNQTM, SAKQXP),
            XNQTMF: GeckoByteStructAccessor(self.struct, XNQTMF, NQTMFZ, SAKQXP),
            QTMFZD: GeckoByteStructAccessor(self.struct, QTMFZD, TMFZDG, SAKQXP),
            MFZDGK: GeckoByteStructAccessor(self.struct, MFZDGK, FZDGKE, SAKQXP),
            ZDGKEA: GeckoByteStructAccessor(self.struct, ZDGKEA, DGKEAK, SAKQXP),
            DDPMXF: GeckoBoolStructAccessor(self.struct, DDPMXF, JVHFTH, UQEXLS, None),
            DPMXFU: GeckoByteStructAccessor(self.struct, DPMXFU, PMXFUB, SAKQXP),
            MXFUBJ: GeckoByteStructAccessor(self.struct, MXFUBJ, XFUBJL, SAKQXP),
            FUBJLO: GeckoByteStructAccessor(self.struct, FUBJLO, UBJLOI, SAKQXP),
            BJLOIN: GeckoEnumStructAccessor(
                self.struct, BJLOIN, JLOINE, None, LWUEUH, None, None, SAKQXP
            ),
            WUEUHN: GeckoBoolStructAccessor(
                self.struct, WUEUHN, UEUHNN, ICXQIE, SAKQXP
            ),
            EUHNNX: GeckoBoolStructAccessor(self.struct, EUHNNX, TBJEUT, ICXQIE, None),
        }

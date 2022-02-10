#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYJ-V3 v59'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 51])
ACQFFT = "".join(chr(c) for c in [67, 69])
AFIKJP = 331
AHEOCT = 1
AJVDQL = "".join(chr(c) for c in [75, 54, 48, 48])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = 457
AMJMAO = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
AOAWBS = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 50])
AWBSIR = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
AZMKQT = 476
BBEKBD = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
BDFSRO = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
BDJQRJ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
BEKBDF = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = 468
BIAMJM = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
BJEUTO = "".join(chr(c) for c in [75, 52])
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
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
BQNRXC = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
BQSNQL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
BSIRYX = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
BVWVUB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
BWJYKL = 275
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 49, 57])
BXTIAC = "".join(chr(c) for c in [54, 52, 75])
BXYBQS = 314
BYGDSB = 294
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 51])
CHWDAF = 329
CMCVDS = 471
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CRTFMN = "".join(chr(c) for c in [70, 117, 108, 108])
CTHBSK = 307
CVDSSR = 472
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
DAFIKJ = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
DDPMXF = 59
DGKEAK = 455
DJQRJJ = 297
DKHTZB = 479
DNIBXT = "".join(chr(c) for c in [49, 54, 75])
DNQGVU = "".join(chr(c) for c in [80, 50, 76])
DPMXFU = 256
DQLAII = "".join(chr(c) for c in [105, 110, 89, 84])
DSBDJQ = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
DSSRUR = 473
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 51])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 57])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EKBDFS = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
ELHBQN = 326
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 50])
EOCTHB = 308
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 49, 52])
EUTOPH = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
FCRTFM = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FFTTID = "".join(chr(c) for c in [80, 50, 50])
FIKJPU = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
FJBIAM = "".join(
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
FMNHTB = 357
FSROGM = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
FTHECV = 319
FTSIFJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
FWRKIN = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
FZDGKE = 454
GDSBDJ = 295
GETIXQ = 461
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 56])
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GQPLSP = 279
GSELHB = 324
GTYIYW = 358
GVUNXN = "".join(chr(c) for c in [80, 52, 72])
GYOUSP = 353
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBSKSO = 363
HBXIBH = 466
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HTBJEU = "".join(chr(c) for c in [75, 56, 53])
HTZBBE = 371
HUOJRJ = 305
HWDAFI = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
HXEKVK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 49])
IACQFF = "".join(chr(c) for c in [85, 76])
IAMJMA = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 48])
IBXTIA = "".join(chr(c) for c in [52, 56, 75])
IBXYBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
ICXQIE = 0
IDNIBX = 290
IDUBSS = "".join(chr(c) for c in [51, 79, 80])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = 377
IGYOUS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 49, 56])
IIDNIB = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
IJUGSE = "".join(chr(c) for c in [83, 79, 117, 116, 52])
IKFWRK = 354
IKJPUN = 333
ILXWAJ = "".join(chr(c) for c in [77, 73, 65])
INEJNI = 309
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IRYXBQ = 350
IUSOOQ = "".join(chr(c) for c in [80, 49])
IUXFEF = "".join(chr(c) for c in [73, 68, 76, 69])
IVDNQG = "".join(chr(c) for c in [80, 49, 76])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 49, 53])
IYWSKW = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
JBIAMJ = 383
JEUTOP = "".join(chr(c) for c in [75, 53])
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JJJVYF = 300
JJVYFC = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
JMAOAW = 283
JMCBFE = 260
JNIBXY = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
JPUNRJ = 325
JQRJJJ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = 323
JUIKFW = "".join(
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
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVDQLA = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
JVHFTH = 274
JVYFCR = 301
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYKLGQ = 277
JYMOUN = 272
JZTATD = 448
KBDFSR = "".join(
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
KCWAON = 365
KEAKST = 456
KFWRKI = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
KHTZBB = "".join(
    chr(c)
    for c in [105, 110, 70, 108, 111, 80, 117, 108, 115, 101, 87, 105, 100, 116, 104]
)
KINEJN = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
KJPUNR = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 50])
KPHUOJ = 304
KQTDKH = "".join(chr(c) for c in [67, 70, 71, 51, 48])
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 48])
KVKZIL = 289
KWIVDN = "".join(chr(c) for c in [78, 65])
KXSJWM = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KZILXW = "".join(chr(c) for c in [105, 110, 88, 69])
LAIIDN = "".join(chr(c) for c in [105, 110, 89, 74])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
LHBQNR = "".join(chr(c) for c in [72, 84, 82])
LIUXFE = 263
LJUIKF = "".join(
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
LKXSJW = "".join(chr(c) for c in [67, 80, 79, 84])
LNMHXE = 285
LOIJUG = "".join(chr(c) for c in [83, 79, 117, 116, 51])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LXWAJV = "".join(chr(c) for c in [68, 74, 83, 52])
MAOAWB = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
MCGETI = 460
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 50, 52])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 54])
MHXEKV = 287
MJIGYO = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
MJMAOA = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 477
MLOIJU = 321
MNHTBJ = "".join(chr(c) for c in [75, 50, 48, 48])
MNZMJI = 313
MOUNBL = 273
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
NEJNIB = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
NHTBJE = "".join(chr(c) for c in [75, 52, 48, 48])
NIBXTI = "".join(chr(c) for c in [51, 50, 75])
NIBXYB = 311
NMHXEK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = "".join(chr(c) for c in [80, 51, 72])
NQJYMO = 271
NQLNMH = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
NQTMFZ = 452
NRJZTA = 332
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
NXNKML = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
NZMJIG = "".join(chr(c) for c in [78, 79])
OACMCV = 470
OAWBSI = 284
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = "".join(chr(c) for c in [76, 73])
OIHBXI = 465
OIJUGS = 322
OJRJHI = 306
OKPHUO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
ONPYYL = 262
OOQNRS = "".join(chr(c) for c in [76, 79, 87])
OPHUGT = "".join(chr(c) for c in [75, 51, 48, 48])
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
PFTSIF = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
PHUGTY = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = 280
PMXFUB = 479
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
QFYLJU = 351
QGVUNX = "".join(chr(c) for c in [80, 51, 76])
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
QLAIID = "".join(chr(c) for c in [75, 56, 48, 48])
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = 327
QPLSPF = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
QRJJJV = 299
QSNQLN = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
QTDKHT = 478
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 53])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 49, 54])
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 50, 56])
RJHIUS = 362
RJJJVY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 48])
RKINEJ = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
RSJMCB = "".join(chr(c) for c in [80, 52])
RURAZM = "".join(chr(c) for c in [67, 70, 71, 50, 55])
RXCHWD = 328
RYXBQF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = 296
SELHBQ = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
SEMCGE = 459
SIFJBI = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
SIRYXB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
SKSOKP = 370
SKWIVD = 320
SNQLNM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SPFTSI = 281
SROGMD = 375
SRURAZ = 474
SSRURA = "".join(chr(c) for c in [67, 70, 71, 50, 54])
SSUHBV = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
STSEMC = 458
SUHBVW = "".join(chr(c) for c in [50, 53, 65])
SXUJUT = 310
TACCPQ = 264
TATDZX = 449
TBJEUT = "".join(chr(c) for c in [75, 56])
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 51, 49])
TDZXNQ = 450
TFMNHT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
TIDUBS = "".join(chr(c) for c in [53, 79, 80])
TIXQVX = 462
TMFZDG = 453
TOPHUG = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 49])
TSIFJB = 352
TTIDUB = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
TZBBEK = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
UBSSUH = "".join(
    chr(c)
    for c in [
        80,
        97,
        99,
        107,
        88,
        101,
        67,
        69,
        65,
        99,
        99,
        79,
        110,
        70,
        117,
        115,
        101,
        50,
    ]
)
UBYGDS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
UGSELH = "".join(chr(c) for c in [83, 79, 117, 116, 53])
UGTYIY = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
UHBVWV = "".join(chr(c) for c in [51, 48, 65])
UIKFWR = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
UNRJZT = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
UNXNKM = "".join(chr(c) for c in [66, 76, 79])
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = 475
USOOQN = 261
USPBWJ = 355
UTOPHU = "".join(chr(c) for c in [75, 49, 48, 48])
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VDNQGV = "".join(chr(c) for c in [80, 50, 72])
VDQLAI = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 50, 53])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 50])
VUBYGD = 293
VUNXNK = "".join(chr(c) for c in [80, 52, 76])
VWVUBY = 291
VXOIHB = 464
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [105, 110, 88, 77])
WAONPY = 367
WBSIRY = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
WDAFIK = 330
WIVDNQ = "".join(chr(c) for c in [80, 49, 72])
WJYKLG = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
WMNZMJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
WRKINE = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
WSKWIV = "".join(chr(c) for c in [83, 79, 117, 116, 49])
WVUBYG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
XCHWDA = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
XEKVKZ = 288
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XIBHZV = 467
XLSXUJ = 7
XNKMLO = "".join(chr(c) for c in [65, 85, 88])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 52])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 49, 55])
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = 463
XSJWMN = 282
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
XYBQSN = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
YBQSNQ = 315
YEKCWA = 364
YFCRTF = 316
YGDSBD = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
YIYWSK = 360
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
        70,
        117,
        115,
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
YWSKWI = 361
YXBQFY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 374
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 55])
ZILXWA = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
ZMJIGY = "".join(chr(c) for c in [77, 69, 68])
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 50, 57])
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 49])
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = 469
ZXNQTM = 451
AIIDNI = [
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
    QLAIID,
    LAIIDN,
]
CQFFTT = [IACQFF, ACQFFT]
DFSROG = [BBEKBD, BEKBDF, EKBDFS, KBDFSR, BDFSRO]
DUBSSU = [TIDUBS, IDUBSS]
EJNIBX = [HECVYY, NEJNIB, NEJNIB, NEJNIB]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
FTTIDU = [CBFEGZ, FFTTID]
GMDDPM = [
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
    OGMDDP,
]
HBQNRX = [
    KWIVDN,
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
    LHBQNR,
]
HBVWVU = [SUHBVW, UHBVWV]
HUGTYI = [
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    QLAIID,
    HECVYY,
    HECVYY,
    HECVYY,
    TOPHUG,
    OPHUGT,
    PHUGTY,
]
JIGYOU = [NZMJIG, QXPICX, ZMJIGY, XPICXQ, MJIGYO]
KLGQPL = [HECVYY, YKLGQP, YKLGQP, YKLGQP]
MCBFEG = [ASSAKQ, SOOQNR]
MDDPMX = [
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
NKMLOI = [
    KWIVDN,
    WIVDNQ,
    IVDNQG,
    VDNQGV,
    DNQGVU,
    NQGVUN,
    QGVUNX,
    GVUNXN,
    VUNXNK,
    SJMCBF,
    UNXNKM,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    NXNKML,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    XNKMLO,
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
PUNRJZ = [
    KWIVDN,
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
QGLRAH = [ASSAKQ, XPICXQ]
RAHEOC = [ASSAKQ, LRAHEO]
ROGMDD = []
RTFMNH = [FCRTFM, CRTFMN]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
XTIACQ = [DNIBXT, NIBXTI, IBXTIA, BXTIAC]
YYLIUX = [NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return DDPMXF

    @property
    def begin(self):
        return DPMXFU

    @property
    def end(self):
        return PMXFUB

    @property
    def all_device_keys(self):
        return GMDDPM

    @property
    def user_demand_keys(self):
        return MDDPMX

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
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, PLSPFT, QIEFXQ, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, SPFTSI, AHEOCT, None),
            PFTSIF: GeckoBoolStructAccessor(
                self.struct, PFTSIF, SPFTSI, QIEFXQ, SAKQXP
            ),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, TSIFJB, AHEOCT, None),
            SIFJBI: GeckoByteStructAccessor(self.struct, SIFJBI, IFJBIA, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, JBIAMJ, ICXQIE, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, JVHFTH, EGZUQE, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, XSJWMN, ICXQIE, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, XSJWMN, AHEOCT, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, QIEFXQ, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, JMAOAW, EGZUQE, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, EGZUQE, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, OAWBSI, CXQIEF, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, OAWBSI, UQEXLS, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, OAWBSI, VHFTHE, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, IRYXBQ, EGZUQE, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, IRYXBQ, CXQIEF, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, IRYXBQ, UQEXLS, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, IRYXBQ, VHFTHE, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, QFYLJU, QIEFXQ, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, QFYLJU, EGZUQE, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, TSIFJB, EGZUQE, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, GYOUSP, ICXQIE, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, GYOUSP, AHEOCT, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, IKFWRK, ICXQIE, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, PLSPFT, ICXQIE, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, JMAOAW, ICXQIE, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, JMAOAW, AHEOCT, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, JMAOAW, CXQIEF, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, INEJNI, ICXQIE, None),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, INEJNI, AHEOCT, EJNIBX, None, CXQIEF, None
            ),
            JNIBXY: GeckoWordStructAccessor(self.struct, JNIBXY, NIBXYB, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BXYBQS, ICXQIE, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, YBQSNQ, ICXQIE, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, YBQSNQ, AHEOCT, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, QFYLJU, ICXQIE, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, QFYLJU, AHEOCT, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, QFYLJU, CXQIEF, None),
            QLNMHX: GeckoWordStructAccessor(self.struct, QLNMHX, LNMHXE, None),
            NMHXEK: GeckoByteStructAccessor(self.struct, NMHXEK, MHXEKV, None),
            HXEKVK: GeckoByteStructAccessor(self.struct, HXEKVK, XEKVKZ, None),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, AIIDNI, None, None, None
            ),
            IIDNIB: GeckoEnumStructAccessor(
                self.struct, IIDNIB, IDNIBX, ICXQIE, XTIACQ, None, CXQIEF, None
            ),
            TIACQF: GeckoEnumStructAccessor(
                self.struct, TIACQF, IDNIBX, QIEFXQ, CQFFTT, None, QIEFXQ, None
            ),
            QFFTTI: GeckoEnumStructAccessor(
                self.struct, QFFTTI, IDNIBX, EGZUQE, FTTIDU, None, QIEFXQ, None
            ),
            TTIDUB: GeckoEnumStructAccessor(
                self.struct, TTIDUB, IDNIBX, CXQIEF, DUBSSU, None, QIEFXQ, None
            ),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, IDNIBX, UQEXLS, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, IDNIBX, VHFTHE, None),
            SSUHBV: GeckoEnumStructAccessor(
                self.struct, SSUHBV, IDNIBX, XLSXUJ, HBVWVU, None, QIEFXQ, None
            ),
            BVWVUB: GeckoWordStructAccessor(self.struct, BVWVUB, VWVUBY, None),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, None),
            UBYGDS: GeckoByteStructAccessor(self.struct, UBYGDS, BYGDSB, None),
            YGDSBD: GeckoByteStructAccessor(self.struct, YGDSBD, GDSBDJ, None),
            DSBDJQ: GeckoByteStructAccessor(self.struct, DSBDJQ, SBDJQR, None),
            BDJQRJ: GeckoWordStructAccessor(self.struct, BDJQRJ, DJQRJJ, None),
            JQRJJJ: GeckoByteStructAccessor(self.struct, JQRJJJ, QRJJJV, None),
            RJJJVY: GeckoByteStructAccessor(self.struct, RJJJVY, JJJVYF, None),
            JJVYFC: GeckoWordStructAccessor(self.struct, JJVYFC, JVYFCR, None),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, YFCRTF, None, RTFMNH, None, QIEFXQ, SAKQXP
            ),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, FMNHTB, None, HUGTYI, None, None, None
            ),
            UGTYIY: GeckoWordStructAccessor(self.struct, UGTYIY, GTYIYW, None),
            TYIYWS: GeckoByteStructAccessor(self.struct, TYIYWS, YIYWSK, None),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, None),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, SKWIVD, None, NKMLOI, None, None, SAKQXP
            ),
            KMLOIJ: GeckoEnumStructAccessor(
                self.struct, KMLOIJ, MLOIJU, None, NKMLOI, None, None, SAKQXP
            ),
            LOIJUG: GeckoEnumStructAccessor(
                self.struct, LOIJUG, OIJUGS, None, NKMLOI, None, None, SAKQXP
            ),
            IJUGSE: GeckoEnumStructAccessor(
                self.struct, IJUGSE, JUGSEL, None, NKMLOI, None, None, SAKQXP
            ),
            UGSELH: GeckoEnumStructAccessor(
                self.struct, UGSELH, GSELHB, None, NKMLOI, None, None, SAKQXP
            ),
            SELHBQ: GeckoEnumStructAccessor(
                self.struct, SELHBQ, ELHBQN, None, HBQNRX, None, None, SAKQXP
            ),
            BQNRXC: GeckoByteStructAccessor(self.struct, BQNRXC, QNRXCH, SAKQXP),
            NRXCHW: GeckoByteStructAccessor(self.struct, NRXCHW, RXCHWD, SAKQXP),
            XCHWDA: GeckoByteStructAccessor(self.struct, XCHWDA, CHWDAF, SAKQXP),
            HWDAFI: GeckoByteStructAccessor(self.struct, HWDAFI, WDAFIK, SAKQXP),
            DAFIKJ: GeckoByteStructAccessor(self.struct, DAFIKJ, AFIKJP, SAKQXP),
            FIKJPU: GeckoByteStructAccessor(self.struct, FIKJPU, IKJPUN, SAKQXP),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, JPUNRJ, None, PUNRJZ, None, None, SAKQXP
            ),
            UNRJZT: GeckoByteStructAccessor(self.struct, UNRJZT, NRJZTA, SAKQXP),
            KHTZBB: GeckoByteStructAccessor(self.struct, KHTZBB, HTZBBE, None),
            TZBBEK: GeckoEnumStructAccessor(
                self.struct, TZBBEK, ZBBEKB, None, DFSROG, None, None, SAKQXP
            ),
            FSROGM: GeckoBoolStructAccessor(
                self.struct, FSROGM, SROGMD, ICXQIE, SAKQXP
            ),
        }

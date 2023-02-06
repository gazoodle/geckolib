#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE v60'
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
ACMCVD = 468
AFIKJP = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
AJVDQL = "".join(chr(c) for c in [105, 110, 88, 77])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 55])
AMJMAO = 350
AOAWBS = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = 332
AWBSIR = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
AZMKQT = "".join(chr(c) for c in [67, 70, 71, 50, 54])
BBEKBD = 479
BDFSRO = "".join(
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
BDJQRJ = 297
BEKBDF = "".join(
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
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 49, 56])
BIAMJM = 284
BJEUTO = "".join(chr(c) for c in [75, 53])
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
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
BQNRXC = 324
BQSNQL = 315
BSIRYX = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
BVWVUB = 291
BWJYKL = 275
BXIBHZ = 464
BXYBQS = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
BYGDSB = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = 458
CHWDAF = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 50, 49])
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
CTHBSK = 307
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 50, 50])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
DAFIKJ = 328
DDPMXF = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
DFSROG = 372
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 53])
DJQRJJ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
DKHTZB = "".join(chr(c) for c in [67, 70, 71, 50, 57])
DNIBXT = "".join(chr(c) for c in [51, 50, 75])
DNQGVU = 320
DPMXFU = "".join(
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
DQLAII = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
DSBDJQ = 296
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 50, 51])
DUBSSU = "".join(
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
DZXNQT = 448
EAKSTS = 454
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EJNIBX = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
EKBDFS = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = 288
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 52])
ELWUEU = 256
EMCGET = 457
EOCTHB = 308
ETIXQV = 459
EUTOPH = "".join(chr(c) for c in [75, 49, 48, 48])
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
FCRTFM = "".join(chr(c) for c in [70, 117, 108, 108])
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FIKJPU = 329
FJBIAM = 377
FMNHTB = "".join(chr(c) for c in [75, 50, 48, 48])
FSROGM = "".join(
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
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
FTTIDU = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
FUBJLO = 375
FWRKIN = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = 351
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 52])
GDSBDJ = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 49, 49])
GKEAKS = 453
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GMDDPM = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
GQPLSP = 279
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 51])
GTYIYW = 358
GVUNXN = "".join(chr(c) for c in [80, 49, 76])
GYOUSP = 353
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 53])
HBSKSO = 363
HBVWVU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 49, 54])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HTBJEU = "".join(chr(c) for c in [75, 56])
HTZBBE = "".join(chr(c) for c in [67, 70, 71, 51, 48])
HUOJRJ = 305
HWDAFI = 327
HXEKVK = 287
HZVOAC = 466
IACQFF = "".join(chr(c) for c in [67, 69])
IAMJMA = "".join(
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
IBHZVO = 465
IBXTIA = "".join(chr(c) for c in [54, 52, 75])
IBXYBQ = 311
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [49, 54, 75])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
IGYOUS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
IHBXIB = 463
IIDNIB = 290
IKFWRK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
IKJPUN = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
ILXWAJ = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
INEJNI = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IRYXBQ = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
IUSOOQ = "".join(chr(c) for c in [80, 49])
IUXFEF = "".join(chr(c) for c in [73, 68, 76, 69])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = 460
IYWSKW = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
JBIAMJ = "".join(
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
JEUTOP = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JJJVYF = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
JJVYFC = 301
JLOINE = "".join(chr(c) for c in [76, 73])
JMAOAW = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
JMCBFE = 260
JPUNRJ = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
JQRJJJ = 299
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 50])
JUIKFW = "".join(
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
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVDQLA = "".join(chr(c) for c in [75, 54, 48, 48])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYKLGQ = 277
JYMOUN = 272
JZTATD = 325
KBDFSR = 371
KCWAON = 365
KEAKST = "".join(chr(c) for c in [67, 70, 71, 54])
KFWRKI = 354
KHTZBB = 477
KINEJN = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
KJPUNR = 330
KMLOIJ = "".join(chr(c) for c in [80, 52, 76])
KPHUOJ = 304
KQTDKH = 475
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KSTSEM = 455
KVKZIL = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
KWIVDN = "".join(chr(c) for c in [45, 45, 45])
KXSJWM = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KZILXW = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
LHBQNR = 323
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
        70,
        117,
        115,
        101,
        69,
        114,
        114,
    ]
)
LKXSJW = "".join(chr(c) for c in [67, 80, 79, 84])
LNMHXE = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
LOIJUG = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 280
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LWUEUH = 479
LXWAJV = "".join(chr(c) for c in [77, 73, 65])
MAOAWB = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
MCGETI = "".join(chr(c) for c in [67, 70, 71, 49, 48])
MCVDSS = 469
MDDPMX = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
MFZDGK = 451
MHXEKV = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
MJIGYO = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
MJMAOA = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = "".join(chr(c) for c in [67, 70, 71, 50, 55])
MLOIJU = "".join(chr(c) for c in [66, 76, 79])
MNHTBJ = "".join(chr(c) for c in [75, 52, 48, 48])
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
NEJNIB = 309
NELWUE = 60
NHTBJE = "".join(chr(c) for c in [75, 56, 53])
NIBXTI = "".join(chr(c) for c in [52, 56, 75])
NIBXYB = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
NKMLOI = "".join(chr(c) for c in [80, 52, 72])
NMHXEK = 285
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = "".join(chr(c) for c in [78, 65])
NQJYMO = 271
NQLNMH = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 50])
NRJZTA = 333
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = 326
NXNKML = "".join(chr(c) for c in [80, 51, 72])
NZMJIG = "".join(chr(c) for c in [78, 79])
OACMCV = "".join(chr(c) for c in [67, 70, 71, 50, 48])
OAWBSI = 283
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = 374
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 49, 53])
OIJUGS = "".join(chr(c) for c in [65, 85, 88])
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
PFTSIF = 281
PHUGTY = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
PMXFUB = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PUNRJZ = 331
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [80, 50, 50])
QFYLJU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
QGVUNX = "".join(chr(c) for c in [80, 49, 72])
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
QLAIID = "".join(chr(c) for c in [105, 110, 89, 84])
QLNMHX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
QPLSPF = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
QRJJJV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
QSNQLN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
QTDKHT = "".join(chr(c) for c in [67, 70, 71, 50, 56])
QTMFZD = 450
QVXOIH = 461
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 473
RJHIUS = 362
RJJJVY = 300
RJZTAT = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
RKINEJ = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
ROGMDD = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
RSJMCB = "".join(chr(c) for c in [80, 52])
RTFMNH = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
RURAZM = 472
RXCHWD = "".join(chr(c) for c in [72, 84, 82])
RYXBQF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
SELHBQ = 322
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 57])
SIFJBI = 352
SIRYXB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
SKSOKP = 370
SKWIVD = 376
SNQLNM = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SPFTSI = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
SROGMD = 373
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 50, 52])
SSRURA = 471
SSUHBV = "".join(chr(c) for c in [50, 53, 65])
STSEMC = "".join(chr(c) for c in [67, 70, 71, 56])
SUHBVW = "".join(chr(c) for c in [51, 48, 65])
SXUJUT = 310
TACCPQ = 264
TATDZX = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
TBJEUT = "".join(chr(c) for c in [75, 52])
TDKHTZ = 476
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 48])
TFMNHT = 357
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [85, 76])
TIDUBS = "".join(chr(c) for c in [51, 79, 80])
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 49, 50])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 51])
TOPHUG = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
TSEMCG = 456
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
TTIDUB = "".join(chr(c) for c in [53, 79, 80])
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
TZBBEK = 478
UBJLOI = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
UBSSUH = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
UBYGDS = 294
UGSELH = 321
UGTYIY = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
UIKFWR = "".join(
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
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
UNRJZT = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
UNXNKM = "".join(chr(c) for c in [80, 50, 76])
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = "".join(chr(c) for c in [67, 70, 71, 50, 53])
USOOQN = 261
USPBWJ = 355
UTOPHU = "".join(chr(c) for c in [75, 56, 48, 48])
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 49])
VDQLAI = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
VDSSRU = 470
VHFTHE = 6
VKZILX = 289
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = 467
VUBYGD = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
VUNXNK = "".join(chr(c) for c in [80, 50, 72])
VWVUBY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 49, 52])
VYFCRT = 316
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
WAONPY = 367
WBSIRY = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
WDAFIK = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
WIVDNQ = "".join(chr(c) for c in [82, 69, 83, 69, 84])
WJYKLG = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
WMNZMJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
WRKINE = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
WSKWIV = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
WVUBYG = 293
XBQFYL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
XEKVKZ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XFUBJL = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 49, 55])
XLSXUJ = 7
XNKMLO = "".join(chr(c) for c in [80, 51, 76])
XNQTMF = 449
XOIHBX = 462
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 49, 51])
XSJWMN = 282
XTIACQ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [68, 74, 83, 52])
XYBQSN = 314
YBQSNQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
YEKCWA = 364
YFCRTF = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
YGDSBD = 295
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
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
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
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = "".join(chr(c) for c in [67, 70, 71, 51, 49])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 452
ZILXWA = "".join(chr(c) for c in [105, 110, 88, 69])
ZMJIGY = "".join(chr(c) for c in [77, 69, 68])
ZMKQTD = 474
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 49, 57])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 49])
ACQFFT = [TIACQF, IACQFF]
BJLOIN = []
BXTIAC = [IDNIBX, DNIBXT, NIBXTI, IBXTIA]
CRTFMN = [YFCRTF, FCRTFM]
FFTTID = [CBFEGZ, QFFTTI]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
HUGTYI = [
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    HECVYY,
    HECVYY,
    HECVYY,
    TOPHUG,
    OPHUGT,
    PHUGTY,
]
IDUBSS = [TTIDUB, TIDUBS]
IJUGSE = [
    NQGVUN,
    QGVUNX,
    GVUNXN,
    VUNXNK,
    UNXNKM,
    NXNKML,
    XNKMLO,
    NKMLOI,
    KMLOIJ,
    SJMCBF,
    MLOIJU,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    LOIJUG,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    OIJUGS,
]
INELWU = [
    SNQLNM,
    YLJUIK,
    UIKFWR,
    BSIRYX,
    SPBWJY,
    QSNQLN,
    NQLNMH,
    LGQPLS,
    BLKXSJ,
    BQFYLJ,
    RYXBQF,
    MJMAOA,
    TSIFJB,
    YBQSNQ,
    IRYXBQ,
    QFYLJU,
    XBQFYL,
    AWBSIR,
    IKFWRK,
    AOAWBS,
    JMAOAW,
    LJUIKF,
    RKINEJ,
    JUIKFW,
    MAOAWB,
    YXBQFY,
    SIRYXB,
    WBSIRY,
]
IVDNQG = [KWIVDN, WIVDNQ]
JIGYOU = [NZMJIG, QXPICX, ZMJIGY, XPICXQ, MJIGYO]
JNIBXY = [HECVYY, EJNIBX, EJNIBX, EJNIBX]
KLGQPL = [HECVYY, YKLGQP, YKLGQP, YKLGQP]
LAIIDN = [
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
]
LOINEL = [
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
    JLOINE,
]
MCBFEG = [ASSAKQ, SOOQNR]
MXFUBJ = [GMDDPM, MDDPMX, DDPMXF, DPMXFU, PMXFUB]
OINELW = [
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
UHBVWV = [SSUHBV, SUHBVW]
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
XCHWDA = [
    NQGVUN,
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
    RXCHWD,
]
YYLIUX = [NPYYLI, PYYLIU]
ZTATDZ = [
    NQGVUN,
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


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return NELWUE

    @property
    def begin(self):
        return ELWUEU

    @property
    def end(self):
        return LWUEUH

    @property
    def all_device_keys(self):
        return LOINEL

    @property
    def user_demand_keys(self):
        return OINELW

    @property
    def error_keys(self):
        return INELWU

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
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, BIAMJM, ICXQIE, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, AMJMAO, ICXQIE, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JVHFTH, EGZUQE, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, XSJWMN, ICXQIE, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, XSJWMN, AHEOCT, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, QIEFXQ, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, OAWBSI, EGZUQE, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, BIAMJM, EGZUQE, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, BIAMJM, CXQIEF, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, BIAMJM, UQEXLS, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, BIAMJM, VHFTHE, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, AMJMAO, EGZUQE, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, AMJMAO, CXQIEF, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, AMJMAO, UQEXLS, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, AMJMAO, VHFTHE, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, QIEFXQ, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FYLJUI, EGZUQE, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, SIFJBI, EGZUQE, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, GYOUSP, ICXQIE, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, GYOUSP, AHEOCT, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, KFWRKI, ICXQIE, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, LSPFTS, ICXQIE, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, OAWBSI, ICXQIE, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, OAWBSI, AHEOCT, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, OAWBSI, CXQIEF, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, NEJNIB, ICXQIE, None),
            EJNIBX: GeckoEnumStructAccessor(
                self.struct, EJNIBX, NEJNIB, AHEOCT, JNIBXY, None, CXQIEF, None
            ),
            NIBXYB: GeckoWordStructAccessor(self.struct, NIBXYB, IBXYBQ, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, XYBQSN, ICXQIE, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, BQSNQL, ICXQIE, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, BQSNQL, AHEOCT, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, FYLJUI, ICXQIE, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, FYLJUI, AHEOCT, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, FYLJUI, CXQIEF, None),
            LNMHXE: GeckoWordStructAccessor(self.struct, LNMHXE, NMHXEK, None),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, None),
            XEKVKZ: GeckoByteStructAccessor(self.struct, XEKVKZ, EKVKZI, None),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, VKZILX, None, LAIIDN, None, None, None
            ),
            AIIDNI: GeckoEnumStructAccessor(
                self.struct, AIIDNI, IIDNIB, ICXQIE, BXTIAC, None, CXQIEF, None
            ),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, IIDNIB, QIEFXQ, ACQFFT, None, QIEFXQ, None
            ),
            CQFFTT: GeckoEnumStructAccessor(
                self.struct, CQFFTT, IIDNIB, EGZUQE, FFTTID, None, QIEFXQ, None
            ),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, IIDNIB, CXQIEF, IDUBSS, None, QIEFXQ, None
            ),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, IIDNIB, UQEXLS, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, IIDNIB, VHFTHE, None),
            BSSUHB: GeckoEnumStructAccessor(
                self.struct, BSSUHB, IIDNIB, XLSXUJ, UHBVWV, None, QIEFXQ, None
            ),
            HBVWVU: GeckoWordStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoByteStructAccessor(self.struct, VWVUBY, WVUBYG, None),
            VUBYGD: GeckoByteStructAccessor(self.struct, VUBYGD, UBYGDS, None),
            BYGDSB: GeckoByteStructAccessor(self.struct, BYGDSB, YGDSBD, None),
            GDSBDJ: GeckoByteStructAccessor(self.struct, GDSBDJ, DSBDJQ, None),
            SBDJQR: GeckoWordStructAccessor(self.struct, SBDJQR, BDJQRJ, None),
            DJQRJJ: GeckoByteStructAccessor(self.struct, DJQRJJ, JQRJJJ, None),
            QRJJJV: GeckoByteStructAccessor(self.struct, QRJJJV, RJJJVY, None),
            JJJVYF: GeckoWordStructAccessor(self.struct, JJJVYF, JJVYFC, None),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, VYFCRT, None, CRTFMN, None, QIEFXQ, SAKQXP
            ),
            RTFMNH: GeckoEnumStructAccessor(
                self.struct, RTFMNH, TFMNHT, None, HUGTYI, None, None, None
            ),
            UGTYIY: GeckoWordStructAccessor(self.struct, UGTYIY, GTYIYW, None),
            TYIYWS: GeckoByteStructAccessor(self.struct, TYIYWS, YIYWSK, None),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, None),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, SKWIVD, None, IVDNQG, None, None, SAKQXP
            ),
            VDNQGV: GeckoEnumStructAccessor(
                self.struct, VDNQGV, DNQGVU, None, IJUGSE, None, None, SAKQXP
            ),
            JUGSEL: GeckoEnumStructAccessor(
                self.struct, JUGSEL, UGSELH, None, IJUGSE, None, None, SAKQXP
            ),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, SELHBQ, None, IJUGSE, None, None, SAKQXP
            ),
            ELHBQN: GeckoEnumStructAccessor(
                self.struct, ELHBQN, LHBQNR, None, IJUGSE, None, None, SAKQXP
            ),
            HBQNRX: GeckoEnumStructAccessor(
                self.struct, HBQNRX, BQNRXC, None, IJUGSE, None, None, SAKQXP
            ),
            QNRXCH: GeckoEnumStructAccessor(
                self.struct, QNRXCH, NRXCHW, None, XCHWDA, None, None, SAKQXP
            ),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, SAKQXP),
            WDAFIK: GeckoByteStructAccessor(self.struct, WDAFIK, DAFIKJ, SAKQXP),
            AFIKJP: GeckoByteStructAccessor(self.struct, AFIKJP, FIKJPU, SAKQXP),
            IKJPUN: GeckoByteStructAccessor(self.struct, IKJPUN, KJPUNR, SAKQXP),
            JPUNRJ: GeckoByteStructAccessor(self.struct, JPUNRJ, PUNRJZ, SAKQXP),
            UNRJZT: GeckoByteStructAccessor(self.struct, UNRJZT, NRJZTA, SAKQXP),
            RJZTAT: GeckoEnumStructAccessor(
                self.struct, RJZTAT, JZTATD, None, ZTATDZ, None, None, SAKQXP
            ),
            TATDZX: GeckoByteStructAccessor(self.struct, TATDZX, ATDZXN, SAKQXP),
            BEKBDF: GeckoBoolStructAccessor(self.struct, BEKBDF, JVHFTH, UQEXLS, None),
            EKBDFS: GeckoByteStructAccessor(self.struct, EKBDFS, KBDFSR, SAKQXP),
            BDFSRO: GeckoByteStructAccessor(self.struct, BDFSRO, DFSROG, SAKQXP),
            FSROGM: GeckoByteStructAccessor(self.struct, FSROGM, SROGMD, SAKQXP),
            ROGMDD: GeckoEnumStructAccessor(
                self.struct, ROGMDD, OGMDDP, None, MXFUBJ, None, None, SAKQXP
            ),
            XFUBJL: GeckoBoolStructAccessor(
                self.struct, XFUBJL, FUBJLO, ICXQIE, SAKQXP
            ),
            UBJLOI: GeckoBoolStructAccessor(self.struct, UBJLOI, SKWIVD, ICXQIE, None),
        }

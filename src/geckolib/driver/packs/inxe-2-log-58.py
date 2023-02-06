#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE-2 v58'
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
ACMCVD = 470
ACQFFT = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
AFIKJP = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [52, 56, 75])
AJVDQL = "".join(chr(c) for c in [105, 110, 89, 84])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 57])
AMJMAO = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
AOAWBS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = 449
AWBSIR = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
AZMKQT = "".join(chr(c) for c in [67, 70, 71, 50, 56])
BBEKBD = "".join(
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
BDFSRO = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
BDJQRJ = 300
BEKBDF = 372
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 50, 48])
BIAMJM = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
BJEUTO = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
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
BQSNQL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
BSIRYX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
BVWVUB = 294
BWJYKL = 275
BXIBHZ = 466
BXYBQS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
BYGDSB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = 460
CHWDAF = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 50, 51])
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [53, 79, 80])
CRTFMN = "".join(chr(c) for c in [75, 52, 48, 48])
CTHBSK = 307
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 50, 52])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
DAFIKJ = 330
DDPMXF = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
DFSROG = 374
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 55])
DJQRJJ = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
DKHTZB = "".join(chr(c) for c in [67, 70, 71, 51, 49])
DNIBXT = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
DNQGVU = "".join(chr(c) for c in [80, 50, 72])
DPMXFU = 375
DQLAII = 290
DSBDJQ = 299
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 50, 53])
DUBSSU = "".join(chr(c) for c in [51, 48, 65])
DZXNQT = 450
EAKSTS = 456
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EJNIBX = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
EKBDFS = "".join(
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
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = "".join(chr(c) for c in [105, 110, 88, 69])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
EMCGET = 459
EOCTHB = 308
ETIXQV = 461
EUTOPH = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
FCRTFM = "".join(chr(c) for c in [75, 50, 48, 48])
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FIKJPU = 331
FJBIAM = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
FMNHTB = "".join(chr(c) for c in [75, 52])
FSROGM = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
FTTIDU = "".join(
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
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 54])
GDSBDJ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 49, 51])
GKEAKS = 455
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GMDDPM = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
GQPLSP = 279
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 53])
GTYIYW = 361
GVUNXN = "".join(chr(c) for c in [80, 51, 76])
GYOUSP = 353
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [72, 84, 82])
HBSKSO = 363
HBVWVU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 49, 56])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HTBJEU = "".join(chr(c) for c in [75, 49, 48, 48])
HTZBBE = "".join(
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
HUGTYI = 360
HUOJRJ = 305
HWDAFI = 329
HXEKVK = 289
HZVOAC = 468
IAMJMA = 283
IBHZVO = 467
IBXTIA = "".join(chr(c) for c in [67, 69])
IBXYBQ = 315
ICXQIE = 0
IDUBSS = "".join(chr(c) for c in [50, 53, 65])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
IGYOUS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
IHBXIB = 465
IIDNIB = "".join(chr(c) for c in [54, 52, 75])
IJUGSE = 322
IKFWRK = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IKJPUN = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
ILXWAJ = "".join(chr(c) for c in [105, 110, 88, 77])
INEJNI = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
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
IVDNQG = "".join(chr(c) for c in [80, 49, 72])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = 462
IYWSKW = "".join(chr(c) for c in [45, 45, 45])
JBIAMJ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
JEUTOP = "".join(chr(c) for c in [75, 51, 48, 48])
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JJJVYF = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
JJVYFC = "".join(chr(c) for c in [70, 117, 108, 108])
JLOINE = 58
JMAOAW = 284
JMCBFE = 260
JNIBXY = 314
JPUNRJ = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
JQRJJJ = 301
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 52])
JUIKFW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVHFTH = 274
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYKLGQ = 277
JYMOUN = 272
JZTATD = "".join(chr(c) for c in [67, 70, 71, 48])
KBDFSR = 373
KCWAON = 365
KEAKST = "".join(chr(c) for c in [67, 70, 71, 56])
KFWRKI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
KHTZBB = 479
KJPUNR = 333
KPHUOJ = 304
KQTDKH = 477
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KSTSEM = 457
KVKZIL = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
KWIVDN = 320
KXSJWM = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KZILXW = "".join(chr(c) for c in [68, 74, 83, 52])
LAIIDN = "".join(chr(c) for c in [51, 50, 75])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
LHBQNR = 326
LIUXFE = 263
LJUIKF = 354
LKXSJW = "".join(chr(c) for c in [67, 80, 79, 84])
LNMHXE = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
LOIJUG = 321
LOINEL = 256
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 280
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LXWAJV = "".join(chr(c) for c in [75, 54, 48, 48])
MAOAWB = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
MCGETI = "".join(chr(c) for c in [67, 70, 71, 49, 50])
MCVDSS = 471
MFZDGK = 453
MHXEKV = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
MJIGYO = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
MJMAOA = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = "".join(chr(c) for c in [67, 70, 71, 50, 57])
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 50])
MNHTBJ = "".join(chr(c) for c in [75, 53])
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
NEJNIB = 311
NHTBJE = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
NIBXTI = "".join(chr(c) for c in [85, 76])
NIBXYB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
NKMLOI = "".join(chr(c) for c in [65, 85, 88])
NMHXEK = 288
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = "".join(chr(c) for c in [80, 50, 76])
NQJYMO = 271
NQLNMH = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 52])
NRJZTA = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = 327
NXNKML = "".join(chr(c) for c in [66, 76, 79])
NZMJIG = "".join(chr(c) for c in [78, 79])
OACMCV = "".join(chr(c) for c in [67, 70, 71, 50, 50])
OAWBSI = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = "".join(
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
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 49, 55])
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 51])
OINELW = 479
OJRJHI = 306
OKPHUO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
ONPYYL = 262
OOQNRS = "".join(chr(c) for c in [76, 79, 87])
OPHUGT = 358
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
PHUGTY = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
PMXFUB = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PUNRJZ = 325
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [51, 79, 80])
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
QGVUNX = "".join(chr(c) for c in [80, 51, 72])
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
QLAIID = "".join(chr(c) for c in [49, 54, 75])
QLNMHX = 287
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
QPLSPF = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
QRJJJV = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
QSNQLN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
QTDKHT = "".join(chr(c) for c in [67, 70, 71, 51, 48])
QTMFZD = 452
QVXOIH = 463
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 475
RJHIUS = 362
RJJJVY = 316
RJZTAT = 332
RKINEJ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
ROGMDD = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
RSJMCB = "".join(chr(c) for c in [80, 52])
RTFMNH = "".join(chr(c) for c in [75, 56, 53])
RURAZM = 474
RXCHWD = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
RYXBQF = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
SELHBQ = 324
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 49, 49])
SIFJBI = 352
SIRYXB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
SKSOKP = 370
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 49])
SNQLNM = 285
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SPFTSI = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
SROGMD = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 50, 54])
SSRURA = 473
SSUHBV = 291
STSEMC = "".join(chr(c) for c in [67, 70, 71, 49, 48])
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
SXUJUT = 310
TACCPQ = 264
TATDZX = "".join(chr(c) for c in [67, 70, 71, 49])
TBJEUT = "".join(chr(c) for c in [75, 56, 48, 48])
TDKHTZ = 478
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 50])
TFMNHT = "".join(chr(c) for c in [75, 56])
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [80, 50, 50])
TIDUBS = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 49, 52])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 53])
TOPHUG = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
TSEMCG = 458
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
TTIDUB = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
TZBBEK = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
UBYGDS = 296
UGSELH = 323
UGTYIY = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
UHBVWV = 293
UIKFWR = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
UNXNKM = "".join(chr(c) for c in [80, 52, 76])
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = "".join(chr(c) for c in [67, 70, 71, 50, 55])
USOOQN = 261
USPBWJ = 355
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VDNQGV = "".join(chr(c) for c in [80, 49, 76])
VDQLAI = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
VDSSRU = 472
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [77, 73, 65])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = 469
VUBYGD = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
VUNXNK = "".join(chr(c) for c in [80, 52, 72])
VWVUBY = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 49, 54])
VYFCRT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
WAONPY = 367
WBSIRY = 350
WDAFIK = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
WIVDNQ = "".join(chr(c) for c in [78, 65])
WJYKLG = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
WMNZMJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
WRKINE = 309
WVUBYG = 295
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
XCHWDA = 328
XEKVKZ = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XFUBJL = "".join(chr(c) for c in [76, 73])
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 49, 57])
XLSXUJ = 7
XNKMLO = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
XNQTMF = 451
XOIHBX = 464
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 49, 53])
XSJWMN = 282
XTIACQ = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
XYBQSN = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
YBQSNQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
YEKCWA = 364
YFCRTF = 357
YGDSBD = 297
YIYWSK = 376
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
YWSKWI = "".join(chr(c) for c in [82, 69, 83, 69, 84])
YXBQFY = 351
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 371
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 454
ZILXWA = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
ZMJIGY = "".join(chr(c) for c in [77, 69, 68])
ZMKQTD = 476
ZTATDZ = 448
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 50, 49])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 51])
BJLOIN = [
    XYBQSN,
    XBQFYL,
    FYLJUI,
    MAOAWB,
    SPBWJY,
    BXYBQS,
    YBQSNQ,
    LGQPLS,
    BLKXSJ,
    IRYXBQ,
    AWBSIR,
    IFJBIA,
    TSIFJB,
    NIBXYB,
    OAWBSI,
    RYXBQF,
    SIRYXB,
    AMJMAO,
    YLJUIK,
    BIAMJM,
    FJBIAM,
    BQFYLJ,
    IKFWRK,
    QFYLJU,
    JBIAMJ,
    BSIRYX,
    AOAWBS,
    MJMAOA,
]
BQNRXC = [
    WIVDNQ,
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
    HBQNRX,
]
BXTIAC = [NIBXTI, IBXTIA]
FFTTID = [CQFFTT, QFFTTI]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
FUBJLO = [
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
    XFUBJL,
]
IACQFF = [CBFEGZ, TIACQF]
IDNIBX = [QLAIID, LAIIDN, AIIDNI, IIDNIB]
JIGYOU = [NZMJIG, QXPICX, ZMJIGY, XPICXQ, MJIGYO]
JVDQLA = [
    XEKVKZ,
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
]
JVYFCR = [JJJVYF, JJVYFC]
KINEJN = [HECVYY, RKINEJ, RKINEJ, RKINEJ]
KLGQPL = [HECVYY, YKLGQP, YKLGQP, YKLGQP]
KMLOIJ = [
    WIVDNQ,
    IVDNQG,
    VDNQGV,
    DNQGVU,
    NQGVUN,
    QGVUNX,
    GVUNXN,
    VUNXNK,
    UNXNKM,
    SJMCBF,
    NXNKML,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    XNKMLO,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    NKMLOI,
]
MCBFEG = [ASSAKQ, SOOQNR]
MDDPMX = [FSROGM, SROGMD, ROGMDD, OGMDDP, GMDDPM]
MXFUBJ = []
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
UBJLOI = [
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
UBSSUH = [IDUBSS, DUBSSU]
UNRJZT = [
    WIVDNQ,
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
UTOPHU = [
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    HECVYY,
    HECVYY,
    HECVYY,
    BJEUTO,
    JEUTOP,
    EUTOPH,
]
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
WSKWIV = [IYWSKW, YWSKWI]
YYLIUX = [NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return JLOINE

    @property
    def begin(self):
        return LOINEL

    @property
    def end(self):
        return OINELW

    @property
    def all_device_keys(self):
        return FUBJLO

    @property
    def user_demand_keys(self):
        return UBJLOI

    @property
    def error_keys(self):
        return BJLOIN

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
            INEJNI: GeckoWordStructAccessor(self.struct, INEJNI, NEJNIB, None),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, JNIBXY, ICXQIE, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, IBXYBQ, ICXQIE, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, IBXYBQ, AHEOCT, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, YXBQFY, ICXQIE, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, YXBQFY, AHEOCT, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, YXBQFY, CXQIEF, None),
            QSNQLN: GeckoWordStructAccessor(self.struct, QSNQLN, SNQLNM, None),
            NQLNMH: GeckoByteStructAccessor(self.struct, NQLNMH, QLNMHX, None),
            LNMHXE: GeckoByteStructAccessor(self.struct, LNMHXE, NMHXEK, None),
            MHXEKV: GeckoEnumStructAccessor(
                self.struct, MHXEKV, HXEKVK, None, JVDQLA, None, None, None
            ),
            VDQLAI: GeckoEnumStructAccessor(
                self.struct, VDQLAI, DQLAII, ICXQIE, IDNIBX, None, CXQIEF, None
            ),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, DQLAII, QIEFXQ, BXTIAC, None, QIEFXQ, None
            ),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, DQLAII, EGZUQE, IACQFF, None, QIEFXQ, None
            ),
            ACQFFT: GeckoEnumStructAccessor(
                self.struct, ACQFFT, DQLAII, CXQIEF, FFTTID, None, QIEFXQ, None
            ),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, DQLAII, UQEXLS, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, DQLAII, VHFTHE, None),
            TIDUBS: GeckoEnumStructAccessor(
                self.struct, TIDUBS, DQLAII, XLSXUJ, UBSSUH, None, QIEFXQ, None
            ),
            BSSUHB: GeckoWordStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoByteStructAccessor(self.struct, SUHBVW, UHBVWV, None),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoByteStructAccessor(self.struct, VWVUBY, WVUBYG, None),
            VUBYGD: GeckoByteStructAccessor(self.struct, VUBYGD, UBYGDS, None),
            BYGDSB: GeckoWordStructAccessor(self.struct, BYGDSB, YGDSBD, None),
            GDSBDJ: GeckoByteStructAccessor(self.struct, GDSBDJ, DSBDJQ, None),
            SBDJQR: GeckoByteStructAccessor(self.struct, SBDJQR, BDJQRJ, None),
            DJQRJJ: GeckoWordStructAccessor(self.struct, DJQRJJ, JQRJJJ, None),
            QRJJJV: GeckoEnumStructAccessor(
                self.struct, QRJJJV, RJJJVY, None, JVYFCR, None, QIEFXQ, SAKQXP
            ),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, YFCRTF, None, UTOPHU, None, None, None
            ),
            TOPHUG: GeckoWordStructAccessor(self.struct, TOPHUG, OPHUGT, None),
            PHUGTY: GeckoByteStructAccessor(self.struct, PHUGTY, HUGTYI, None),
            UGTYIY: GeckoByteStructAccessor(self.struct, UGTYIY, GTYIYW, None),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, YIYWSK, None, WSKWIV, None, None, SAKQXP
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, KMLOIJ, None, None, SAKQXP
            ),
            MLOIJU: GeckoEnumStructAccessor(
                self.struct, MLOIJU, LOIJUG, None, KMLOIJ, None, None, SAKQXP
            ),
            OIJUGS: GeckoEnumStructAccessor(
                self.struct, OIJUGS, IJUGSE, None, KMLOIJ, None, None, SAKQXP
            ),
            JUGSEL: GeckoEnumStructAccessor(
                self.struct, JUGSEL, UGSELH, None, KMLOIJ, None, None, SAKQXP
            ),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, SELHBQ, None, KMLOIJ, None, None, SAKQXP
            ),
            ELHBQN: GeckoEnumStructAccessor(
                self.struct, ELHBQN, LHBQNR, None, BQNRXC, None, None, SAKQXP
            ),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, SAKQXP),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, SAKQXP),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, SAKQXP),
            WDAFIK: GeckoByteStructAccessor(self.struct, WDAFIK, DAFIKJ, SAKQXP),
            AFIKJP: GeckoByteStructAccessor(self.struct, AFIKJP, FIKJPU, SAKQXP),
            IKJPUN: GeckoByteStructAccessor(self.struct, IKJPUN, KJPUNR, SAKQXP),
            JPUNRJ: GeckoEnumStructAccessor(
                self.struct, JPUNRJ, PUNRJZ, None, UNRJZT, None, None, SAKQXP
            ),
            NRJZTA: GeckoByteStructAccessor(self.struct, NRJZTA, RJZTAT, SAKQXP),
            HTZBBE: GeckoBoolStructAccessor(self.struct, HTZBBE, JVHFTH, UQEXLS, None),
            TZBBEK: GeckoByteStructAccessor(self.struct, TZBBEK, ZBBEKB, SAKQXP),
            BBEKBD: GeckoByteStructAccessor(self.struct, BBEKBD, BEKBDF, SAKQXP),
            EKBDFS: GeckoByteStructAccessor(self.struct, EKBDFS, KBDFSR, SAKQXP),
            BDFSRO: GeckoEnumStructAccessor(
                self.struct, BDFSRO, DFSROG, None, MDDPMX, None, None, SAKQXP
            ),
            DDPMXF: GeckoBoolStructAccessor(
                self.struct, DDPMXF, DPMXFU, ICXQIE, SAKQXP
            ),
            PMXFUB: GeckoBoolStructAccessor(self.struct, PMXFUB, YIYWSK, ICXQIE, None),
        }

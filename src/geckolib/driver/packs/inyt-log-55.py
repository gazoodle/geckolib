#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v55'
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
ACCPQI = 272
ACMCVD = 468
ACQFFT = 299
AFIKJP = 342
AHEOCT = 308
AIIDNI = 293
AJVDQL = "".join(chr(c) for c in [85, 76])
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 55])
AMJMAO = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
AOAWBS = "".join(
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
ASSAKQ = "".join(chr(c) for c in [85, 100, 80, 49])
ATDZXN = 348
AWBSIR = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
AZMKQT = "".join(chr(c) for c in [67, 70, 71, 50, 54])
BBEKBD = 479
BDJQRJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
BFEGZU = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 49, 56])
BIAMJM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
BJEUTO = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
BMJVHF = 256
BQFYLJ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
BQNRXC = 332
BQSNQL = "".join(chr(c) for c in [105, 110, 88, 69])
BSIRYX = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
BSSUHB = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
BVWVUB = "".join(chr(c) for c in [75, 56])
BWJYKL = 281
BXIBHZ = 464
BXTIAC = 296
BXYBQS = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
BYGDSB = "".join(chr(c) for c in [75, 56, 48, 48])
CBFEGZ = 5
CCPQIP = "".join(chr(c) for c in [67, 108, 101, 97, 110])
CGETIX = 458
CHWDAF = 340
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 50, 49])
CPQIPO = 273
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
CRTFMN = "".join(chr(c) for c in [80, 50, 72])
CTHBSK = 363
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 50, 50])
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = "".join(chr(c) for c in [78, 69, 87])
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 53])
DJQRJJ = 358
DKHTZB = "".join(chr(c) for c in [67, 70, 71, 50, 57])
DNIBXT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
DNQGVU = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
DQLAII = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
DSBDJQ = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68])
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 50, 51])
DUBSSU = "".join(chr(c) for c in [70, 117, 108, 108])
DZXNQT = 448
EAKSTS = 454
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 270
EFXQGL = 258
EGZUQE = 7
EJNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
EKBDFS = "".join(chr(c) for c in [76, 73])
EKCWAO = "".join(chr(c) for c in [83, 84, 79, 80])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
EMCGET = 457
EOCTHB = 307
ETIXQV = 459
EUTOPH = "".join(chr(c) for c in [83, 79, 117, 116, 50])
EXLSXU = "".join(chr(c) for c in [70, 85, 76, 76])
FCRTFM = "".join(chr(c) for c in [80, 49, 76])
FEFJTA = "".join(
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
FEGZUQ = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
FFTTID = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
FIKJPU = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
FJBIAM = 350
FJTACC = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
FMNHTB = "".join(chr(c) for c in [80, 51, 76])
FSROGM = 55
FTHECV = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
FTSIFJ = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
FTTIDU = 301
FWRKIN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
FYLJUI = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 52])
GDSBDJ = "".join(chr(c) for c in [75, 51, 48, 48])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 49, 49])
GKEAKS = 453
GQPLSP = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
GTYIYW = 324
GVUNXN = 339
GYOUSP = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
GZUQEX = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
HBQNRX = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
HBSKSO = 303
HBVWVU = "".join(chr(c) for c in [75, 56, 53])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 49, 54])
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = "".join(chr(c) for c in [80, 50])
HTBJEU = "".join(chr(c) for c in [66, 76, 79])
HTZBBE = "".join(chr(c) for c in [67, 70, 71, 51, 48])
HUGTYI = 323
HUOJRJ = 362
HWDAFI = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
HXEKVK = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
HZVOAC = 466
IACQFF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
IAMJMA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
IBHZVO = 465
IBXTIA = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
IBXYBQ = 288
ICXQIE = 2
IDNIBX = 294
IDUBSS = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
IHBXIB = 463
IIDNIB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
IJUGSE = 328
IKFWRK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
IKJPUN = 343
ILXWAJ = "".join(chr(c) for c in [52, 56, 75])
INEJNI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(
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
IRYXBQ = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IUSOOQ = "".join(chr(c) for c in [80, 51])
IUXFEF = 267
IVDNQG = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = 460
IYWSKW = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
JIGYOU = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
JJJVYF = 361
JJVYFC = "".join(chr(c) for c in [83, 79, 117, 116, 49])
JMAOAW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
JMCBFE = "".join(chr(c) for c in [76, 49, 50, 48])
JNIBXY = 287
JPUNRJ = 344
JQRJJJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
JRJHIU = "".join(chr(c) for c in [72, 73, 71, 72])
JTACCP = 271
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
JUIKFW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JVDQLA = "".join(chr(c) for c in [67, 69])
JVHFTH = 319
JVYFCR = 320
JWMNZM = 355
JYKLGQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
JYMOUN = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JZTATD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
KCWAON = "".join(chr(c) for c in [83, 84, 65, 82, 84])
KEAKST = "".join(chr(c) for c in [67, 70, 71, 54])
KFWRKI = 315
KHTZBB = 477
KINEJN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
KJPUNR = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
KLGQPL = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
KMLOIJ = 326
KPHUOJ = 306
KQTDKH = 475
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
KSTSEM = 455
KVKZIL = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
KWIVDN = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
KXSJWM = 353
KZILXW = "".join(chr(c) for c in [49, 54, 75])
LAIIDN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
LHBQNR = 331
LIUXFE = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
LJUIKF = 311
LKXSJW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
LNMHXE = "".join(chr(c) for c in [105, 110, 88, 77])
LOIJUG = 327
LRAHEO = 1
LSPFTS = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
LSXUJU = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
LXWAJV = "".join(chr(c) for c in [54, 52, 75])
MAOAWB = "".join(
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
MCBFEG = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
MCGETI = "".join(chr(c) for c in [67, 70, 71, 49, 48])
MCVDSS = 469
MFZDGK = 451
MHXEKV = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
MJIGYO = 277
MJMAOA = 351
MJVHFT = "".join(chr(c) for c in [77, 101, 110, 117])
MKQTDK = "".join(chr(c) for c in [67, 70, 71, 50, 55])
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 56])
MNHTBJ = "".join(chr(c) for c in [80, 52, 72])
MNZMJI = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
MOUNBL = 313
NBLKXS = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
NEJNIB = 285
NHTBJE = "".join(chr(c) for c in [80, 52, 76])
NIBXTI = 295
NIBXYB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
NKMLOI = "".join(chr(c) for c in [83, 79, 117, 116, 55])
NMHXEK = "".join(chr(c) for c in [75, 54, 48, 48])
NPYYLI = 264
NQGVUN = 338
NQJYMO = 282
NQLNMH = "".join(chr(c) for c in [68, 74, 83, 52])
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 50])
NRJZTA = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
NRSJMC = "".join(chr(c) for c in [67, 80])
NRXCHW = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
NXNKML = "".join(chr(c) for c in [83, 79, 117, 116, 54])
NZMJIG = 275
OACMCV = "".join(chr(c) for c in [67, 70, 71, 50, 48])
OAWBSI = "".join(
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
OCTHBS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 49, 53])
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 57])
OJRJHI = 261
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ONPYYL = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
OOQNRS = 260
OPHUGT = 322
OUNBLK = "".join(chr(c) for c in [78, 79])
OUSPBW = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
OUYNQJ = "".join(chr(c) for c in [67, 80, 79, 84])
PBWJYK = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
PFTSIF = 284
PHUGTY = "".join(chr(c) for c in [83, 79, 117, 116, 52])
PHUOJR = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = 283
POUYNQ = "".join(
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
PQIPOU = "".join(chr(c) for c in [80, 117, 114, 103, 101])
PUNRJZ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
PYYLIU = "".join(
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
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
QFFTTI = 300
QGLRAH = "".join(chr(c) for c in [79, 78])
QGVUNX = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
QIEFXQ = 6
QIPOUY = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
QJYMOU = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
QLAIID = 291
QLNMHX = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
QNRSJM = "".join(chr(c) for c in [66, 76])
QPLSPF = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
QRJJJV = 360
QSNQLN = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
QTDKHT = "".join(chr(c) for c in [67, 70, 71, 50, 56])
QTMFZD = 450
QVXOIH = 461
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RAZMKQ = 473
RJHIUS = "".join(chr(c) for c in [76, 79, 87])
RJJJVY = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
RJZTAT = 346
RKINEJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
ROGMDD = 479
RSJMCB = "".join(chr(c) for c in [79, 51])
RTFMNH = "".join(chr(c) for c in [80, 50, 76])
RURAZM = 472
RXCHWD = 333
RYXBQF = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
SAKQXP = "".join(chr(c) for c in [76, 79])
SELHBQ = 330
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 57])
SIFJBI = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
SIRYXB = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
SJMCBF = 3
SJWMNZ = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
SKSOKP = 304
SKWIVD = 335
SNQLNM = "".join(chr(c) for c in [77, 73, 65])
SOKPHU = 305
SOOQNR = "".join(chr(c) for c in [80, 53])
SPBWJY = 280
SPFTSI = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
SROGMD = 256
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 50, 52])
SSAKQX = 259
SSRURA = 471
SSUHBV = 357
STSEMC = "".join(chr(c) for c in [67, 70, 71, 56])
SUHBVW = "".join(chr(c) for c in [75, 50, 48, 48])
SXUJUT = 262
TACCPQ = "".join(
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
TATDZX = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
TBJEUT = "".join(chr(c) for c in [70, 97, 110])
TDKHTZ = 476
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 48])
TFMNHT = "".join(chr(c) for c in [80, 51, 72])
THBSKS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = 297
TIDUBS = 316
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 49, 50])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 51])
TOPHUG = "".join(chr(c) for c in [83, 79, 117, 116, 51])
TSEMCG = 456
TSIFJB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
TTIDUB = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
TYEKCW = 263
TYIYWS = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
TZBBEK = 478
UBYGDS = "".join(chr(c) for c in [75, 49, 48, 48])
UGSELH = 329
UGTYIY = "".join(chr(c) for c in [83, 79, 117, 116, 53])
UHBVWV = "".join(chr(c) for c in [75, 52, 48, 48])
UIKFWR = 314
UJUTYE = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
UNBLKX = "".join(chr(c) for c in [77, 69, 68])
UNRJZT = 345
UNXNKM = 349
UOJRJH = "".join(chr(c) for c in [80, 49])
UQEXLS = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
URAZMK = "".join(chr(c) for c in [67, 70, 71, 50, 53])
USOOQN = "".join(chr(c) for c in [80, 52])
USPBWJ = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
UTOPHU = 321
UTYEKC = "".join(
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
UXFEFJ = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
UYNQJY = 274
VDNQGV = 337
VDSSRU = 470
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VKZILX = 290
VOACMC = 467
VUBYGD = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
VUNXNK = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
VWVUBY = "".join(chr(c) for c in [75, 52])
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 49, 52])
VYFCRT = "".join(chr(c) for c in [78, 65])
WAJVDQ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
WAONPY = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
WBSIRY = 354
WDAFIK = 341
WIVDNQ = 336
WJYKLG = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
WMNZMJ = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
WRKINE = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
WSKWIV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
WVUBYG = "".join(chr(c) for c in [75, 53])
XBQFYL = 309
XCHWDA = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
XEKVKZ = "".join(chr(c) for c in [105, 110, 89, 84])
XFEFJT = 268
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 49, 55])
XNKMLO = 325
XNQTMF = 449
XOIHBX = 462
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 49, 51])
XSJWMN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
XTIACQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
XUJUTY = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
XYBQSN = 289
YBQSNQ = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
YEKCWA = "".join(chr(c) for c in [73, 68, 76, 69])
YFCRTF = "".join(chr(c) for c in [80, 49, 72])
YGDSBD = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
YIYWSK = 334
YKLGQP = 352
YLIUXF = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
YLJUIK = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
YMOUNB = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
YNQJYM = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
YOUSPB = 279
YPIPIV = 257
YXBQFY = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
YYLIUX = 266
YYPIPI = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
ZBBEKB = "".join(chr(c) for c in [67, 70, 71, 51, 49])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 452
ZILXWA = "".join(chr(c) for c in [51, 50, 75])
ZMJIGY = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
ZMKQTD = 474
ZTATDZ = 347
ZUQEXL = 310
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 49, 57])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 49])
AONPYY = [YEKCWA, EKCWAO, KCWAON, CWAONP, WAONPY]
BDFSRO = [
    ASSAKQ,
    PICXQI,
    CXQIEF,
    XQIEFX,
    IEFXQG,
    XQGLRA,
    RAHEOC,
    HEOCTH,
    OCTHBS,
    THBSKS,
    BSKSOK,
    KSOKPH,
    OKPHUO,
    PHUOJR,
]
BEKBDF = []
BLKXSJ = [OUNBLK, SAKQXP, UNBLKX, AKQXPI, NBLKXS]
DFSROG = [
    WRKINE,
    JMAOAW,
    OAWBSI,
    FTSIFJ,
    WMNZMJ,
    FYLJUI,
    FWRKIN,
    RKINEJ,
    GYOUSP,
    POUYNQ,
    IAMJMA,
    IFJBIA,
    KLGQPL,
    JYKLGQ,
    IKFWRK,
    SIFJBI,
    AMJMAO,
    BIAMJM,
    LSPFTS,
    AWBSIR,
    QPLSPF,
    LGQPLS,
    MAOAWB,
    IRYXBQ,
    AOAWBS,
    GQPLSP,
    JBIAMJ,
    TSIFJB,
    SPFTSI,
]
EKVKZI = [
    YBQSNQ,
    BQSNQL,
    QSNQLN,
    SNQLNM,
    NQLNMH,
    QLNMHX,
    LNMHXE,
    NMHXEK,
    MHXEKV,
    HXEKVK,
    XEKVKZ,
]
FXQGLR = [IVLASS, AKQXPI]
GLRAHE = [IVLASS, QGLRAH]
IGYOUS = [HFTHEC, JIGYOU, JIGYOU, JIGYOU]
JEUTOP = [
    VYFCRT,
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    SOOQNR,
    HTBJEU,
    NRSJMC,
    RSJMCB,
    JMCBFE,
    HFTHEC,
    HFTHEC,
    TBJEUT,
    HFTHEC,
    HFTHEC,
    BJEUTO,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    FEGZUQ,
]
JHIUSO = [IVLASS, JRJHIU, RJHIUS]
JUTYEK = [XUJUTY, UJUTYE]
KBDFSR = [
    UOJRJH,
    HIUSOO,
    IUSOOQ,
    USOOQN,
    SOOQNR,
    QNRSJM,
    NRSJMC,
    RSJMCB,
    JMCBFE,
    MCBFEG,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    EKBDFS,
]
KQXPIC = [IVLASS, SAKQXP, AKQXPI]
OQNRSJ = [IVLASS, JRJHIU]
QFYLJU = [HFTHEC, BQFYLJ, BQFYLJ, BQFYLJ]
QNRXCH = [
    VYFCRT,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    NRSJMC,
]
SBDJQR = [
    SUHBVW,
    UHBVWV,
    HBVWVU,
    BVWVUB,
    VWVUBY,
    WVUBYG,
    VUBYGD,
    UBYGDS,
    BYGDSB,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
]
UBSSUH = [IDUBSS, DUBSSU]
VDQLAI = [AJVDQL, JVDQLA]
VLASSA = [PIPIVL, IPIVLA, PIVLAS, IVLASS]
VYYPIP = [
    VHFTHE,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    FTHECV,
    THECVY,
    HECVYY,
    ECVYYP,
    HFTHEC,
    CVYYPI,
]
XLSXUJ = [UQEXLS, QEXLSX, EXLSXU]
XWAJVD = [KZILXW, ZILXWA, ILXWAJ, LXWAJV]
YWSKWI = [
    VYFCRT,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    IYWSKW,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return FSROGM

    @property
    def begin(self):
        return SROGMD

    @property
    def end(self):
        return ROGMDD

    @property
    def all_device_keys(self):
        return KBDFSR

    @property
    def user_demand_keys(self):
        return BDFSRO

    @property
    def error_keys(self):
        return DFSROG

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoTempStructAccessor(self.struct, ZCQBMJ, CQBMJV, None),
            QBMJVH: GeckoByteStructAccessor(self.struct, QBMJVH, BMJVHF, None),
            MJVHFT: GeckoEnumStructAccessor(
                self.struct, MJVHFT, JVHFTH, None, VYYPIP, None, None, None
            ),
            YYPIPI: GeckoEnumStructAccessor(
                self.struct, YYPIPI, YPIPIV, None, VLASSA, None, None, LASSAK
            ),
            ASSAKQ: GeckoEnumStructAccessor(
                self.struct, ASSAKQ, SSAKQX, QXPICX, KQXPIC, None, XPICXQ, LASSAK
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, SSAKQX, ICXQIE, KQXPIC, None, XPICXQ, LASSAK
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, SSAKQX, XPICXQ, KQXPIC, None, XPICXQ, LASSAK
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, SSAKQX, QIEFXQ, KQXPIC, None, XPICXQ, LASSAK
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, QXPICX, FXQGLR, None, ICXQIE, LASSAK
            ),
            XQGLRA: GeckoEnumStructAccessor(
                self.struct, XQGLRA, EFXQGL, LRAHEO, GLRAHE, None, ICXQIE, LASSAK
            ),
            RAHEOC: GeckoEnumStructAccessor(
                self.struct, RAHEOC, AHEOCT, None, GLRAHE, None, None, LASSAK
            ),
            HEOCTH: GeckoEnumStructAccessor(
                self.struct, HEOCTH, EOCTHB, None, FXQGLR, None, None, LASSAK
            ),
            OCTHBS: GeckoEnumStructAccessor(
                self.struct, OCTHBS, CTHBSK, None, GLRAHE, None, None, LASSAK
            ),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, LASSAK),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, LASSAK),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, LASSAK),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, LASSAK),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, LASSAK),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, QXPICX, JHIUSO, None, XPICXQ, None
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, OJRJHI, ICXQIE, JHIUSO, None, XPICXQ, None
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, OJRJHI, XPICXQ, JHIUSO, None, XPICXQ, None
            ),
            USOOQN: GeckoEnumStructAccessor(
                self.struct, USOOQN, OJRJHI, QIEFXQ, JHIUSO, None, XPICXQ, None
            ),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, OOQNRS, QXPICX, OQNRSJ, None, ICXQIE, None
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, OOQNRS, LRAHEO, GLRAHE, None, ICXQIE, None
            ),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, OOQNRS, ICXQIE, GLRAHE, None, ICXQIE, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, OOQNRS, SJMCBF, GLRAHE, None, ICXQIE, None
            ),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, OOQNRS, XPICXQ, GLRAHE, None, ICXQIE, None
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, OOQNRS, CBFEGZ, GLRAHE, None, ICXQIE, None
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, OOQNRS, QIEFXQ, GLRAHE, None, ICXQIE, None
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, OOQNRS, EGZUQE, GLRAHE, None, ICXQIE, None
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, XLSXUJ, None, None, LASSAK
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, QXPICX, JUTYEK, None, ICXQIE, LASSAK
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, TYEKCW, None, AONPYY, None, None, LASSAK
            ),
            ONPYYL: GeckoTimeStructAccessor(self.struct, ONPYYL, NPYYLI, LASSAK),
            PYYLIU: GeckoByteStructAccessor(self.struct, PYYLIU, YYLIUX, LASSAK),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, SXUJUT, ICXQIE, JUTYEK, None, ICXQIE, LASSAK
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, AONPYY, None, None, LASSAK
            ),
            UXFEFJ: GeckoTimeStructAccessor(self.struct, UXFEFJ, XFEFJT, LASSAK),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, LASSAK),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, LASSAK),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, LASSAK),
            CCPQIP: GeckoBoolStructAccessor(self.struct, CCPQIP, CPQIPO, QXPICX, None),
            PQIPOU: GeckoBoolStructAccessor(self.struct, PQIPOU, CPQIPO, ICXQIE, None),
            QIPOUY: GeckoBoolStructAccessor(self.struct, QIPOUY, CPQIPO, SJMCBF, None),
            IPOUYN: GeckoBoolStructAccessor(self.struct, IPOUYN, CPQIPO, XPICXQ, None),
            POUYNQ: GeckoBoolStructAccessor(self.struct, POUYNQ, CPQIPO, CBFEGZ, None),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, UYNQJY, ICXQIE, None),
            YNQJYM: GeckoBoolStructAccessor(self.struct, YNQJYM, NQJYMO, SJMCBF, None),
            QJYMOU: GeckoBoolStructAccessor(self.struct, QJYMOU, NQJYMO, CBFEGZ, None),
            JYMOUN: GeckoBoolStructAccessor(self.struct, JYMOUN, NQJYMO, QIEFXQ, None),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, MOUNBL, None, BLKXSJ, None, None, None
            ),
            LKXSJW: GeckoBoolStructAccessor(self.struct, LKXSJW, KXSJWM, CBFEGZ, None),
            XSJWMN: GeckoBoolStructAccessor(self.struct, XSJWMN, KXSJWM, QIEFXQ, None),
            SJWMNZ: GeckoWordStructAccessor(self.struct, SJWMNZ, JWMNZM, None),
            WMNZMJ: GeckoBoolStructAccessor(self.struct, WMNZMJ, UYNQJY, LRAHEO, None),
            MNZMJI: GeckoTempStructAccessor(self.struct, MNZMJI, NZMJIG, None),
            ZMJIGY: GeckoTempStructAccessor(self.struct, ZMJIGY, MJIGYO, None),
            JIGYOU: GeckoEnumStructAccessor(
                self.struct, JIGYOU, OOQNRS, CBFEGZ, IGYOUS, None, XPICXQ, None
            ),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, YOUSPB, ICXQIE, None),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, YOUSPB, QIEFXQ, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, SPBWJY, ICXQIE, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, BWJYKL, LRAHEO, None),
            WJYKLG: GeckoBoolStructAccessor(
                self.struct, WJYKLG, BWJYKL, ICXQIE, LASSAK
            ),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, YKLGQP, LRAHEO, None),
            KLGQPL: GeckoBoolStructAccessor(self.struct, KLGQPL, UYNQJY, SJMCBF, None),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, NQJYMO, QXPICX, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, NQJYMO, LRAHEO, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, PLSPFT, ICXQIE, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, PLSPFT, SJMCBF, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, SJMCBF, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, PFTSIF, XPICXQ, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, PFTSIF, CBFEGZ, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, PFTSIF, QIEFXQ, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FJBIAM, SJMCBF, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, FJBIAM, XPICXQ, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, FJBIAM, CBFEGZ, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, FJBIAM, QIEFXQ, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, MJMAOA, ICXQIE, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MJMAOA, SJMCBF, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, YKLGQP, SJMCBF, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, KXSJWM, QXPICX, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, KXSJWM, LRAHEO, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, WBSIRY, QXPICX, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, SPBWJY, QXPICX, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, PLSPFT, QXPICX, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, PLSPFT, LRAHEO, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, PLSPFT, XPICXQ, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, XBQFYL, QXPICX, None),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, XBQFYL, LRAHEO, QFYLJU, None, XPICXQ, None
            ),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, XBQFYL, SJMCBF, None),
            YLJUIK: GeckoWordStructAccessor(self.struct, YLJUIK, LJUIKF, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, UIKFWR, QXPICX, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, KFWRKI, QXPICX, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, KFWRKI, LRAHEO, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, MJMAOA, QXPICX, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, MJMAOA, LRAHEO, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, MJMAOA, XPICXQ, None),
            INEJNI: GeckoWordStructAccessor(self.struct, INEJNI, NEJNIB, None),
            EJNIBX: GeckoByteStructAccessor(self.struct, EJNIBX, JNIBXY, None),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, None),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, None, EKVKZI, None, None, None
            ),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, VKZILX, QXPICX, XWAJVD, None, XPICXQ, None
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, VKZILX, ICXQIE, VDQLAI, None, ICXQIE, None
            ),
            DQLAII: GeckoWordStructAccessor(self.struct, DQLAII, QLAIID, None),
            LAIIDN: GeckoByteStructAccessor(self.struct, LAIIDN, AIIDNI, None),
            IIDNIB: GeckoByteStructAccessor(self.struct, IIDNIB, IDNIBX, None),
            DNIBXT: GeckoByteStructAccessor(self.struct, DNIBXT, NIBXTI, None),
            IBXTIA: GeckoByteStructAccessor(self.struct, IBXTIA, BXTIAC, None),
            XTIACQ: GeckoWordStructAccessor(self.struct, XTIACQ, TIACQF, None),
            IACQFF: GeckoByteStructAccessor(self.struct, IACQFF, ACQFFT, None),
            CQFFTT: GeckoByteStructAccessor(self.struct, CQFFTT, QFFTTI, None),
            FFTTID: GeckoWordStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoEnumStructAccessor(
                self.struct, TTIDUB, TIDUBS, None, UBSSUH, None, ICXQIE, LASSAK
            ),
            BSSUHB: GeckoEnumStructAccessor(
                self.struct, BSSUHB, SSUHBV, None, SBDJQR, None, None, None
            ),
            BDJQRJ: GeckoWordStructAccessor(self.struct, BDJQRJ, DJQRJJ, None),
            JQRJJJ: GeckoByteStructAccessor(self.struct, JQRJJJ, QRJJJV, None),
            RJJJVY: GeckoByteStructAccessor(self.struct, RJJJVY, JJJVYF, None),
            JJVYFC: GeckoEnumStructAccessor(
                self.struct, JJVYFC, JVYFCR, None, JEUTOP, None, None, LASSAK
            ),
            EUTOPH: GeckoEnumStructAccessor(
                self.struct, EUTOPH, UTOPHU, None, JEUTOP, None, None, LASSAK
            ),
            TOPHUG: GeckoEnumStructAccessor(
                self.struct, TOPHUG, OPHUGT, None, JEUTOP, None, None, LASSAK
            ),
            PHUGTY: GeckoEnumStructAccessor(
                self.struct, PHUGTY, HUGTYI, None, JEUTOP, None, None, LASSAK
            ),
            UGTYIY: GeckoEnumStructAccessor(
                self.struct, UGTYIY, GTYIYW, None, JEUTOP, None, None, LASSAK
            ),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, YIYWSK, None, YWSKWI, None, None, LASSAK
            ),
            WSKWIV: GeckoByteStructAccessor(self.struct, WSKWIV, SKWIVD, LASSAK),
            KWIVDN: GeckoByteStructAccessor(self.struct, KWIVDN, WIVDNQ, LASSAK),
            IVDNQG: GeckoByteStructAccessor(self.struct, IVDNQG, VDNQGV, LASSAK),
            DNQGVU: GeckoByteStructAccessor(self.struct, DNQGVU, NQGVUN, LASSAK),
            QGVUNX: GeckoByteStructAccessor(self.struct, QGVUNX, GVUNXN, LASSAK),
            VUNXNK: GeckoByteStructAccessor(self.struct, VUNXNK, UNXNKM, LASSAK),
            NXNKML: GeckoEnumStructAccessor(
                self.struct, NXNKML, XNKMLO, None, JEUTOP, None, None, LASSAK
            ),
            NKMLOI: GeckoEnumStructAccessor(
                self.struct, NKMLOI, KMLOIJ, None, JEUTOP, None, None, LASSAK
            ),
            MLOIJU: GeckoEnumStructAccessor(
                self.struct, MLOIJU, LOIJUG, None, JEUTOP, None, None, LASSAK
            ),
            OIJUGS: GeckoEnumStructAccessor(
                self.struct, OIJUGS, IJUGSE, None, JEUTOP, None, None, LASSAK
            ),
            JUGSEL: GeckoEnumStructAccessor(
                self.struct, JUGSEL, UGSELH, None, JEUTOP, None, None, LASSAK
            ),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, SELHBQ, None, JEUTOP, None, None, LASSAK
            ),
            ELHBQN: GeckoEnumStructAccessor(
                self.struct, ELHBQN, LHBQNR, None, JEUTOP, None, None, LASSAK
            ),
            HBQNRX: GeckoEnumStructAccessor(
                self.struct, HBQNRX, BQNRXC, None, QNRXCH, None, None, LASSAK
            ),
            NRXCHW: GeckoEnumStructAccessor(
                self.struct, NRXCHW, RXCHWD, None, QNRXCH, None, None, LASSAK
            ),
            XCHWDA: GeckoByteStructAccessor(self.struct, XCHWDA, CHWDAF, LASSAK),
            HWDAFI: GeckoByteStructAccessor(self.struct, HWDAFI, WDAFIK, LASSAK),
            DAFIKJ: GeckoByteStructAccessor(self.struct, DAFIKJ, AFIKJP, LASSAK),
            FIKJPU: GeckoByteStructAccessor(self.struct, FIKJPU, IKJPUN, LASSAK),
            KJPUNR: GeckoByteStructAccessor(self.struct, KJPUNR, JPUNRJ, LASSAK),
            PUNRJZ: GeckoByteStructAccessor(self.struct, PUNRJZ, UNRJZT, LASSAK),
            NRJZTA: GeckoByteStructAccessor(self.struct, NRJZTA, RJZTAT, LASSAK),
            JZTATD: GeckoByteStructAccessor(self.struct, JZTATD, ZTATDZ, LASSAK),
            TATDZX: GeckoByteStructAccessor(self.struct, TATDZX, ATDZXN, LASSAK),
        }

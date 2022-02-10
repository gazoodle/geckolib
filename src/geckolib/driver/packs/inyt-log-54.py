#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v54'
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
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 51])
ACQFFT = 301
AFIKJP = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
AHEOCT = 308
AIIDNI = 295
AJVDQL = 291
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = 457
AMJMAO = "".join(
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
AOAWBS = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
AONPYY = 266
ASSAKQ = "".join(chr(c) for c in [85, 100, 80, 49])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 50])
AWBSIR = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
AZMKQT = 476
BBEKBD = 54
BDJQRJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
BEKBDF = 256
BFEGZU = 310
BHZVOA = 468
BIAMJM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
BJEUTO = 322
BLKXSJ = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
BMJVHF = 256
BQFYLJ = 311
BQNRXC = 340
BQSNQL = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
BSIRYX = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
BSSUHB = "".join(chr(c) for c in [75, 56, 53])
BVWVUB = "".join(chr(c) for c in [75, 49, 48, 48])
BWJYKL = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 49, 57])
BXTIAC = 299
BXYBQS = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
CBFEGZ = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
CCPQIP = "".join(
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
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 51])
CHWDAF = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
CMCVDS = 471
CPQIPO = "".join(
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
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
CRTFMN = "".join(chr(c) for c in [80, 52, 72])
CTHBSK = 303
CVDSSR = 472
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = 264
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = 344
DGKEAK = 455
DJQRJJ = 361
DKHTZB = 479
DNIBXT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
DNQGVU = 349
DQLAII = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
DSBDJQ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
DSSRUR = 473
DUBSSU = "".join(chr(c) for c in [75, 50, 48, 48])
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 51])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 57])
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 272
EFXQGL = 258
EGZUQE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
EJNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
EKBDFS = 479
EKVKZI = "".join(chr(c) for c in [51, 50, 75])
ELHBQN = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 50])
EOCTHB = 307
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 49, 52])
EUTOPH = 323
EXLSXU = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
FCRTFM = "".join(chr(c) for c in [80, 51, 76])
FEFJTA = "".join(
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
FEGZUQ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
FFTTID = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
FIKJPU = 345
FJBIAM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
FJTACC = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FMNHTB = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
FTHECV = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
FTSIFJ = 350
FTTIDU = "".join(chr(c) for c in [70, 117, 108, 108])
FWRKIN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
FYLJUI = 314
FZDGKE = 454
GDSBDJ = 358
GETIXQ = 461
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 56])
GQPLSP = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
GSELHB = 332
GTYIYW = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 55])
GYOUSP = 280
GZUQEX = "".join(chr(c) for c in [70, 85, 76, 76])
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
HBSKSO = 362
HBVWVU = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
HBXIBH = 466
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = "".join(chr(c) for c in [80, 52])
HTBJEU = 321
HTZBBE = "".join(chr(c) for c in [76, 73])
HUGTYI = "".join(chr(c) for c in [72, 84, 82])
HUOJRJ = 261
HWDAFI = 343
HXEKVK = 290
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 49])
IACQFF = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
IAMJMA = "".join(
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
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 48])
IBXTIA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
IBXYBQ = "".join(chr(c) for c in [105, 110, 88, 69])
ICXQIE = 2
IDNIBX = 296
IDUBSS = 357
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
IGYOUS = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 49, 56])
IIDNIB = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
IJUGSE = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
IKFWRK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IKJPUN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
ILXWAJ = "".join(chr(c) for c in [85, 76])
INEJNI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
IRYXBQ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
IUSOOQ = "".join(chr(c) for c in [80, 53])
IUXFEF = 270
IVDNQG = 339
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 49, 53])
IYWSKW = 336
JBIAMJ = 351
JEUTOP = "".join(chr(c) for c in [83, 79, 117, 116, 52])
JHIUSO = "".join(chr(c) for c in [80, 51])
JIGYOU = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
JJJVYF = "".join(chr(c) for c in [80, 49, 72])
JJVYFC = "".join(chr(c) for c in [80, 49, 76])
JMAOAW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
JMCBFE = 5
JNIBXY = 289
JPUNRJ = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
JQRJJJ = "".join(chr(c) for c in [83, 79, 117, 116, 49])
JTACCP = 273
JUGSEL = 331
JUIKFW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
JUTYEK = "".join(chr(c) for c in [83, 84, 79, 80])
JVDQLA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
JVHFTH = 319
JVYFCR = "".join(chr(c) for c in [80, 50, 72])
JWMNZM = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
JYKLGQ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
JYMOUN = "".join(chr(c) for c in [77, 69, 68])
JZTATD = 448
KCWAON = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
KEAKST = 456
KFWRKI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
KINEJN = 287
KJPUNR = 346
KLGQPL = 283
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
KPHUOJ = 306
KQTDKH = "".join(chr(c) for c in [67, 70, 71, 51, 48])
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 48])
KVKZIL = "".join(chr(c) for c in [52, 56, 75])
KWIVDN = 338
KXSJWM = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
LAIIDN = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
LHBQNR = 333
LIUXFE = "".join(
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
LJUIKF = 315
LKXSJW = 355
LNMHXE = "".join(chr(c) for c in [105, 110, 89, 84])
LOIJUG = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
LRAHEO = 1
LSPFTS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
LXWAJV = "".join(chr(c) for c in [67, 69])
MAOAWB = 354
MCBFEG = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
MCGETI = 460
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 50, 52])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 54])
MHXEKV = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
MJIGYO = 279
MJMAOA = "".join(
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
MJVHFT = "".join(chr(c) for c in [77, 101, 110, 117])
MKQTDK = 477
MLOIJU = 329
MNZMJI = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
NBLKXS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
NEJNIB = 288
NHTBJE = "".join(chr(c) for c in [83, 79, 117, 116, 50])
NIBXTI = 297
NIBXYB = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
NKMLOI = 328
NPYYLI = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 54])
NQJYMO = 313
NQLNMH = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
NQTMFZ = 452
NRJZTA = 348
NRSJMC = 3
NRXCHW = 341
NXNKML = 327
OACMCV = 470
OAWBSI = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
OCTHBS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
OIHBXI = 465
OIJUGS = 330
OJRJHI = "".join(chr(c) for c in [76, 79, 87])
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ONPYYL = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
OOQNRS = "".join(chr(c) for c in [66, 76])
OPHUGT = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
OQNRSJ = "".join(chr(c) for c in [67, 80])
OUNBLK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
OUSPBW = 281
OUYNQJ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
PBWJYK = 352
PFTSIF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
PHUGTY = 334
PHUOJR = "".join(chr(c) for c in [80, 49])
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
POUYNQ = 282
PQIPOU = "".join(chr(c) for c in [67, 80, 79, 84])
PUNRJZ = 347
PYYLIU = 267
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 262
QFFTTI = 316
QFYLJU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
QGLRAH = "".join(chr(c) for c in [79, 78])
QGVUNX = 325
QIEFXQ = 6
QIPOUY = 274
QJYMOU = "".join(chr(c) for c in [78, 79])
QLAIID = 294
QLNMHX = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
QNRSJM = "".join(chr(c) for c in [79, 51])
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
QPLSPF = 284
QRJJJV = 320
QSNQLN = "".join(chr(c) for c in [105, 110, 88, 77])
QTDKHT = 478
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 53])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 49, 54])
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 50, 56])
RJHIUS = "".join(chr(c) for c in [80, 50])
RJJJVY = "".join(chr(c) for c in [78, 65])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 48])
RKINEJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
RSJMCB = "".join(chr(c) for c in [76, 49, 50, 48])
RTFMNH = "".join(chr(c) for c in [80, 52, 76])
RURAZM = "".join(chr(c) for c in [67, 70, 71, 50, 55])
RXCHWD = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
SAKQXP = "".join(chr(c) for c in [76, 79])
SBDJQR = 360
SEMCGE = 459
SIFJBI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
SIRYXB = 309
SJMCBF = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = 275
SKSOKP = 304
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
SNQLNM = "".join(chr(c) for c in [75, 54, 48, 48])
SOKPHU = 305
SPBWJY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
SPFTSI = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
SRURAZ = 474
SSAKQX = 259
SSRURA = "".join(chr(c) for c in [67, 70, 71, 50, 54])
SSUHBV = "".join(chr(c) for c in [75, 56])
STSEMC = 458
SUHBVW = "".join(chr(c) for c in [75, 52])
SXUJUT = "".join(
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
TACCPQ = "".join(chr(c) for c in [80, 117, 114, 103, 101])
TATDZX = 449
TBJEUT = "".join(chr(c) for c in [83, 79, 117, 116, 51])
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 51, 49])
TDZXNQ = 450
TFMNHT = "".join(chr(c) for c in [66, 76, 79])
THBSKS = "".join(chr(c) for c in [85, 100, 80, 49, 76, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = 300
TIDUBS = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
TIXQVX = 462
TMFZDG = 453
TOPHUG = 324
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 49])
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
TYEKCW = "".join(chr(c) for c in [78, 69, 87])
TYIYWS = 335
UBSSUH = "".join(chr(c) for c in [75, 52, 48, 48])
UBYGDS = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68])
UGSELH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
UHBVWV = "".join(chr(c) for c in [75, 53])
UIKFWR = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
UJUTYE = "".join(chr(c) for c in [73, 68, 76, 69])
UNBLKX = 353
UNRJZT = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
UNXNKM = "".join(chr(c) for c in [83, 79, 117, 116, 56])
UOJRJH = "".join(chr(c) for c in [72, 73, 71, 72])
UQEXLS = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
URAZMK = 475
USOOQN = 260
USPBWJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
UTOPHU = "".join(chr(c) for c in [83, 79, 117, 116, 53])
UTYEKC = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UXFEFJ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
UYNQJY = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
VDQLAI = 293
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 50, 53])
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VKZILX = "".join(chr(c) for c in [54, 52, 75])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 50])
VUBYGD = "".join(chr(c) for c in [75, 51, 48, 48])
VUNXNK = 326
VWVUBY = "".join(chr(c) for c in [75, 56, 48, 48])
VXOIHB = 464
VYFCRT = "".join(chr(c) for c in [80, 50, 76])
WAJVDQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
WAONPY = "".join(
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
WBSIRY = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
WDAFIK = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
WJYKLG = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
WMNZMJ = 277
WRKINE = 285
WSKWIV = 337
WVUBYG = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
XBQFYL = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
XCHWDA = 342
XEKVKZ = "".join(chr(c) for c in [49, 54, 75])
XFEFJT = 271
XIBHZV = 467
XLSXUJ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
XNKMLO = "".join(chr(c) for c in [83, 79, 117, 116, 57])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 52])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 49, 55])
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = 463
XSJWMN = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
XTIACQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
XUJUTY = 263
XYBQSN = "".join(chr(c) for c in [77, 73, 65])
YBQSNQ = "".join(chr(c) for c in [68, 74, 83, 52])
YEKCWA = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
YFCRTF = "".join(chr(c) for c in [80, 51, 72])
YGDSBD = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
YIYWSK = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
YKLGQP = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
YLIUXF = 268
YLJUIK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
YMOUNB = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
YNQJYM = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
YOUSPB = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
YPIPIV = 257
YWSKWI = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
YXBQFY = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
YYLIUX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
YYPIPI = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 55])
ZILXWA = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
ZMJIGY = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 50, 57])
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 49])
ZVOACM = 469
ZXNQTM = 451
BYGDSB = [
    DUBSSU,
    UBSSUH,
    BSSUHB,
    SSUHBV,
    SUHBVW,
    UHBVWV,
    HBVWVU,
    BVWVUB,
    VWVUBY,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    WVUBYG,
    VUBYGD,
    UBYGDS,
]
EKCWAO = [UJUTYE, JUTYEK, UTYEKC, TYEKCW, YEKCWA]
FXQGLR = [IVLASS, AKQXPI]
GLRAHE = [IVLASS, QGLRAH]
JRJHIU = [IVLASS, UOJRJH, OJRJHI]
KHTZBB = []
KQXPIC = [IVLASS, SAKQXP, AKQXPI]
KZILXW = [XEKVKZ, EKVKZI, KVKZIL, VKZILX]
LSXUJU = [EXLSXU, XLSXUJ]
MNHTBJ = [
    RJJJVY,
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
    IUSOOQ,
    TFMNHT,
    OQNRSJ,
    QNRSJM,
    RSJMCB,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    FMNHTB,
]
MOUNBL = [QJYMOU, SAKQXP, JYMOUN, AKQXPI, YMOUNB]
NMHXEK = [
    NIBXYB,
    IBXYBQ,
    BXYBQS,
    XYBQSN,
    YBQSNQ,
    BQSNQL,
    QSNQLN,
    SNQLNM,
    NQLNMH,
    QLNMHX,
    LNMHXE,
]
NZMJIG = [HFTHEC, MNZMJI, MNZMJI, MNZMJI]
RYXBQF = [HFTHEC, IRYXBQ, IRYXBQ, IRYXBQ]
SELHBQ = [
    RJJJVY,
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
    OQNRSJ,
]
SOOQNR = [IVLASS, UOJRJH]
TTIDUB = [FFTTID, FTTIDU]
TZBBEK = [
    PHUOJR,
    RJHIUS,
    JHIUSO,
    HIUSOO,
    IUSOOQ,
    OOQNRS,
    OQNRSJ,
    QNRSJM,
    RSJMCB,
    SJMCBF,
    MCBFEG,
    CBFEGZ,
    HTZBBE,
]
UGTYIY = [
    RJJJVY,
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
    HUGTYI,
]
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
XWAJVD = [ILXWAJ, LXWAJV]
ZBBEKB = [
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
]
ZUQEXL = [FEGZUQ, EGZUQE, GZUQEX]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return BBEKBD

    @property
    def begin(self):
        return BEKBDF

    @property
    def end(self):
        return EKBDFS

    @property
    def all_device_keys(self):
        return TZBBEK

    @property
    def user_demand_keys(self):
        return ZBBEKB

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
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, LASSAK),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, LASSAK),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, LASSAK),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, LASSAK),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, LASSAK),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, QXPICX, JRJHIU, None, XPICXQ, None
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, HUOJRJ, ICXQIE, JRJHIU, None, XPICXQ, None
            ),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, HUOJRJ, XPICXQ, JRJHIU, None, XPICXQ, None
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, HUOJRJ, QIEFXQ, JRJHIU, None, XPICXQ, None
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, QXPICX, SOOQNR, None, ICXQIE, None
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, USOOQN, LRAHEO, GLRAHE, None, ICXQIE, None
            ),
            OQNRSJ: GeckoEnumStructAccessor(
                self.struct, OQNRSJ, USOOQN, ICXQIE, GLRAHE, None, ICXQIE, None
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, USOOQN, NRSJMC, GLRAHE, None, ICXQIE, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, USOOQN, XPICXQ, GLRAHE, None, ICXQIE, None
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, USOOQN, JMCBFE, GLRAHE, None, ICXQIE, None
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, USOOQN, QIEFXQ, GLRAHE, None, ICXQIE, None
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, None, ZUQEXL, None, None, LASSAK
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, QXPICX, LSXUJU, None, ICXQIE, LASSAK
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XUJUTY, None, EKCWAO, None, None, LASSAK
            ),
            KCWAON: GeckoTimeStructAccessor(self.struct, KCWAON, CWAONP, LASSAK),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, LASSAK),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, QEXLSX, ICXQIE, LSXUJU, None, ICXQIE, LASSAK
            ),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, EKCWAO, None, None, LASSAK
            ),
            YYLIUX: GeckoTimeStructAccessor(self.struct, YYLIUX, YLIUXF, LASSAK),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, LASSAK),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, LASSAK),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, LASSAK),
            FJTACC: GeckoBoolStructAccessor(self.struct, FJTACC, JTACCP, QXPICX, None),
            TACCPQ: GeckoBoolStructAccessor(self.struct, TACCPQ, JTACCP, ICXQIE, None),
            ACCPQI: GeckoBoolStructAccessor(self.struct, ACCPQI, JTACCP, NRSJMC, None),
            CCPQIP: GeckoBoolStructAccessor(self.struct, CCPQIP, JTACCP, XPICXQ, None),
            CPQIPO: GeckoBoolStructAccessor(self.struct, CPQIPO, JTACCP, JMCBFE, None),
            PQIPOU: GeckoBoolStructAccessor(self.struct, PQIPOU, QIPOUY, ICXQIE, None),
            IPOUYN: GeckoBoolStructAccessor(self.struct, IPOUYN, POUYNQ, NRSJMC, None),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, POUYNQ, JMCBFE, None),
            UYNQJY: GeckoBoolStructAccessor(self.struct, UYNQJY, POUYNQ, QIEFXQ, None),
            YNQJYM: GeckoEnumStructAccessor(
                self.struct, YNQJYM, NQJYMO, None, MOUNBL, None, None, None
            ),
            OUNBLK: GeckoBoolStructAccessor(self.struct, OUNBLK, UNBLKX, JMCBFE, None),
            NBLKXS: GeckoBoolStructAccessor(self.struct, NBLKXS, UNBLKX, QIEFXQ, None),
            BLKXSJ: GeckoWordStructAccessor(self.struct, BLKXSJ, LKXSJW, None),
            KXSJWM: GeckoBoolStructAccessor(self.struct, KXSJWM, QIPOUY, LRAHEO, None),
            XSJWMN: GeckoTempStructAccessor(self.struct, XSJWMN, SJWMNZ, None),
            JWMNZM: GeckoTempStructAccessor(self.struct, JWMNZM, WMNZMJ, None),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, USOOQN, JMCBFE, NZMJIG, None, XPICXQ, None
            ),
            ZMJIGY: GeckoBoolStructAccessor(self.struct, ZMJIGY, MJIGYO, ICXQIE, None),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, MJIGYO, QIEFXQ, None),
            IGYOUS: GeckoBoolStructAccessor(self.struct, IGYOUS, GYOUSP, ICXQIE, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, OUSPBW, LRAHEO, None),
            USPBWJ: GeckoBoolStructAccessor(
                self.struct, USPBWJ, OUSPBW, ICXQIE, LASSAK
            ),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, PBWJYK, LRAHEO, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, QIPOUY, NRSJMC, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, POUYNQ, QXPICX, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, POUYNQ, LRAHEO, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, KLGQPL, ICXQIE, None),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, KLGQPL, NRSJMC, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, QPLSPF, NRSJMC, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, QPLSPF, XPICXQ, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, QPLSPF, JMCBFE, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, QPLSPF, QIEFXQ, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, FTSIFJ, NRSJMC, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, FTSIFJ, XPICXQ, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, FTSIFJ, JMCBFE, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FTSIFJ, QIEFXQ, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, JBIAMJ, ICXQIE, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, JBIAMJ, NRSJMC, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, PBWJYK, NRSJMC, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, UNBLKX, QXPICX, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, UNBLKX, LRAHEO, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MAOAWB, QXPICX, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, GYOUSP, QXPICX, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, KLGQPL, QXPICX, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, KLGQPL, LRAHEO, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, KLGQPL, XPICXQ, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, SIRYXB, QXPICX, None),
            IRYXBQ: GeckoEnumStructAccessor(
                self.struct, IRYXBQ, SIRYXB, LRAHEO, RYXBQF, None, XPICXQ, None
            ),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, SIRYXB, NRSJMC, None),
            XBQFYL: GeckoWordStructAccessor(self.struct, XBQFYL, BQFYLJ, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, QXPICX, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, LJUIKF, QXPICX, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, LJUIKF, LRAHEO, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, JBIAMJ, QXPICX, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, JBIAMJ, LRAHEO, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, JBIAMJ, XPICXQ, None),
            FWRKIN: GeckoWordStructAccessor(self.struct, FWRKIN, WRKINE, None),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, None),
            INEJNI: GeckoByteStructAccessor(self.struct, INEJNI, NEJNIB, None),
            EJNIBX: GeckoEnumStructAccessor(
                self.struct, EJNIBX, JNIBXY, None, NMHXEK, None, None, None
            ),
            MHXEKV: GeckoEnumStructAccessor(
                self.struct, MHXEKV, HXEKVK, QXPICX, KZILXW, None, XPICXQ, None
            ),
            ZILXWA: GeckoEnumStructAccessor(
                self.struct, ZILXWA, HXEKVK, ICXQIE, XWAJVD, None, ICXQIE, None
            ),
            WAJVDQ: GeckoWordStructAccessor(self.struct, WAJVDQ, AJVDQL, None),
            JVDQLA: GeckoByteStructAccessor(self.struct, JVDQLA, VDQLAI, None),
            DQLAII: GeckoByteStructAccessor(self.struct, DQLAII, QLAIID, None),
            LAIIDN: GeckoByteStructAccessor(self.struct, LAIIDN, AIIDNI, None),
            IIDNIB: GeckoByteStructAccessor(self.struct, IIDNIB, IDNIBX, None),
            DNIBXT: GeckoWordStructAccessor(self.struct, DNIBXT, NIBXTI, None),
            IBXTIA: GeckoByteStructAccessor(self.struct, IBXTIA, BXTIAC, None),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, None),
            IACQFF: GeckoWordStructAccessor(self.struct, IACQFF, ACQFFT, None),
            CQFFTT: GeckoEnumStructAccessor(
                self.struct, CQFFTT, QFFTTI, None, TTIDUB, None, ICXQIE, LASSAK
            ),
            TIDUBS: GeckoEnumStructAccessor(
                self.struct, TIDUBS, IDUBSS, None, BYGDSB, None, None, None
            ),
            YGDSBD: GeckoWordStructAccessor(self.struct, YGDSBD, GDSBDJ, None),
            DSBDJQ: GeckoByteStructAccessor(self.struct, DSBDJQ, SBDJQR, None),
            BDJQRJ: GeckoByteStructAccessor(self.struct, BDJQRJ, DJQRJJ, None),
            JQRJJJ: GeckoEnumStructAccessor(
                self.struct, JQRJJJ, QRJJJV, None, MNHTBJ, None, None, LASSAK
            ),
            NHTBJE: GeckoEnumStructAccessor(
                self.struct, NHTBJE, HTBJEU, None, MNHTBJ, None, None, LASSAK
            ),
            TBJEUT: GeckoEnumStructAccessor(
                self.struct, TBJEUT, BJEUTO, None, MNHTBJ, None, None, LASSAK
            ),
            JEUTOP: GeckoEnumStructAccessor(
                self.struct, JEUTOP, EUTOPH, None, MNHTBJ, None, None, LASSAK
            ),
            UTOPHU: GeckoEnumStructAccessor(
                self.struct, UTOPHU, TOPHUG, None, MNHTBJ, None, None, LASSAK
            ),
            OPHUGT: GeckoEnumStructAccessor(
                self.struct, OPHUGT, PHUGTY, None, UGTYIY, None, None, LASSAK
            ),
            GTYIYW: GeckoByteStructAccessor(self.struct, GTYIYW, TYIYWS, LASSAK),
            YIYWSK: GeckoByteStructAccessor(self.struct, YIYWSK, IYWSKW, LASSAK),
            YWSKWI: GeckoByteStructAccessor(self.struct, YWSKWI, WSKWIV, LASSAK),
            SKWIVD: GeckoByteStructAccessor(self.struct, SKWIVD, KWIVDN, LASSAK),
            WIVDNQ: GeckoByteStructAccessor(self.struct, WIVDNQ, IVDNQG, LASSAK),
            VDNQGV: GeckoByteStructAccessor(self.struct, VDNQGV, DNQGVU, LASSAK),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, QGVUNX, None, MNHTBJ, None, None, LASSAK
            ),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, MNHTBJ, None, None, LASSAK
            ),
            UNXNKM: GeckoEnumStructAccessor(
                self.struct, UNXNKM, NXNKML, None, MNHTBJ, None, None, LASSAK
            ),
            XNKMLO: GeckoEnumStructAccessor(
                self.struct, XNKMLO, NKMLOI, None, MNHTBJ, None, None, LASSAK
            ),
            KMLOIJ: GeckoEnumStructAccessor(
                self.struct, KMLOIJ, MLOIJU, None, MNHTBJ, None, None, LASSAK
            ),
            LOIJUG: GeckoEnumStructAccessor(
                self.struct, LOIJUG, OIJUGS, None, MNHTBJ, None, None, LASSAK
            ),
            IJUGSE: GeckoEnumStructAccessor(
                self.struct, IJUGSE, JUGSEL, None, MNHTBJ, None, None, LASSAK
            ),
            UGSELH: GeckoEnumStructAccessor(
                self.struct, UGSELH, GSELHB, None, SELHBQ, None, None, LASSAK
            ),
            ELHBQN: GeckoEnumStructAccessor(
                self.struct, ELHBQN, LHBQNR, None, SELHBQ, None, None, LASSAK
            ),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, LASSAK),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, LASSAK),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, LASSAK),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, LASSAK),
            WDAFIK: GeckoByteStructAccessor(self.struct, WDAFIK, DAFIKJ, LASSAK),
            AFIKJP: GeckoByteStructAccessor(self.struct, AFIKJP, FIKJPU, LASSAK),
            IKJPUN: GeckoByteStructAccessor(self.struct, IKJPUN, KJPUNR, LASSAK),
            JPUNRJ: GeckoByteStructAccessor(self.struct, JPUNRJ, PUNRJZ, LASSAK),
            UNRJZT: GeckoByteStructAccessor(self.struct, UNRJZT, NRJZTA, LASSAK),
        }

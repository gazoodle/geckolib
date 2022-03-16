#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYJ v56'
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
ACCPQI = 271
ACMCVD = 477
ACQFFT = "".join(chr(c) for c in [51, 48, 65])
AFIKJP = 450
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [80, 50, 50])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 49, 54])
AMJMAO = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
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
        70,
        117,
        115,
        101,
        69,
        114,
        114,
    ]
)
AONPYY = "".join(chr(c) for c in [78, 69, 87])
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = 456
AWBSIR = "".join(
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
AZMKQT = 479
BFEGZU = 310
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 50, 55])
BIAMJM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
BJEUTO = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
BLKXSJ = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
BMJVHF = 256
BQFYLJ = 309
BQNRXC = 325
BQSNQL = "".join(chr(c) for c in [105, 110, 88, 69])
BSIRYX = 354
BSKSOK = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
BSSUHB = 295
BVWVUB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
BWJYKL = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
BXIBHZ = 473
BXTIAC = "".join(
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
BXYBQS = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
BYGDSB = 301
CBFEGZ = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
CCPQIP = "".join(
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
CGETIX = 467
CHWDAF = 448
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 51, 48])
CPQIPO = 272
CQBMJV = 317
CRTFMN = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
CTHBSK = 307
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 51, 49])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(chr(c) for c in [83, 84, 79, 80])
CXQIEF = 4
DAFIKJ = "".join(chr(c) for c in [67, 70, 71, 50])
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 49, 52])
DJQRJJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
DNIBXT = "".join(chr(c) for c in [53, 79, 80])
DNQGVU = "".join(chr(c) for c in [83, 79, 117, 116, 52])
DQLAII = "".join(chr(c) for c in [67, 69])
DSBDJQ = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
DUBSSU = 294
DZXNQT = 457
EAKSTS = 463
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = 268
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
EJNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
EKCWAO = 263
EKVKZI = "".join(chr(c) for c in [75, 56, 48, 48])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
EMCGET = 466
EOCTHB = 308
ETIXQV = 468
EUTOPH = "".join(chr(c) for c in [83, 79, 117, 116, 49])
EXLSXU = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
FCRTFM = "".join(chr(c) for c in [75, 49, 48, 48])
FEFJTA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
FEGZUQ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
FFTTID = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
FIKJPU = "".join(chr(c) for c in [67, 70, 71, 51])
FJBIAM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
FJTACC = "".join(
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
FTHECV = 319
FTSIFJ = 284
FTTIDU = 291
FWRKIN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 49, 51])
GDSBDJ = 316
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 50, 48])
GKEAKS = 462
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GQPLSP = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [80, 51, 72])
GVUNXN = 324
GZUQEX = "".join(chr(c) for c in [70, 85, 76, 76])
HBQNRX = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
HBSKSO = 303
HBVWVU = 297
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 50, 53])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [80, 52])
HTBJEU = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
HUGTYI = "".join(chr(c) for c in [80, 50, 72])
HUOJRJ = 261
HWDAFI = "".join(chr(c) for c in [67, 70, 71, 49])
HXEKVK = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
HZVOAC = 475
IACQFF = "".join(chr(c) for c in [50, 53, 65])
IAMJMA = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
IBHZVO = 474
IBXYBQ = 288
ICXQIE = 0
IDNIBX = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
IDUBSS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
IGYOUS = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
IHBXIB = 472
IJUGSE = 329
IKFWRK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
IKJPUN = 451
ILXWAJ = "".join(chr(c) for c in [49, 54, 75])
INEJNI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(chr(c) for c in [80, 117, 114, 103, 101])
IRYXBQ = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
IUSOOQ = "".join(chr(c) for c in [80, 53])
IUXFEF = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
IVDNQG = "".join(chr(c) for c in [83, 79, 117, 116, 51])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = 469
IYWSKW = "".join(chr(c) for c in [80, 52, 76])
JBIAMJ = 350
JEUTOP = 361
JHIUSO = "".join(chr(c) for c in [80, 51])
JIGYOU = 277
JJJVYF = "".join(chr(c) for c in [75, 56, 53])
JJVYFC = "".join(chr(c) for c in [75, 56])
JMAOAW = 351
JMCBFE = 5
JNIBXY = 287
JPUNRJ = 452
JQRJJJ = 357
JTACCP = 270
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
JUIKFW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JUTYEK = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JVDQLA = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [75, 52])
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
JYKLGQ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
JYMOUN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
JZTATD = "".join(chr(c) for c in [67, 70, 71, 55])
KCWAON = "".join(chr(c) for c in [73, 68, 76, 69])
KEAKST = "".join(chr(c) for c in [67, 70, 71, 49, 53])
KFWRKI = 315
KINEJN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
KJPUNR = "".join(chr(c) for c in [67, 70, 71, 52])
KLGQPL = 352
KMLOIJ = 327
KPHUOJ = 306
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
KSTSEM = 464
KVKZIL = "".join(chr(c) for c in [105, 110, 89, 74])
KWIVDN = "".join(chr(c) for c in [83, 79, 117, 116, 50])
KXSJWM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
KZILXW = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
LAIIDN = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
LHBQNR = 333
LIUXFE = 266
LJUIKF = 311
LNMHXE = "".join(chr(c) for c in [105, 110, 88, 77])
LOIJUG = 328
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 283
LSXUJU = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
LXWAJV = "".join(chr(c) for c in [51, 50, 75])
MAOAWB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
MCBFEG = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
MCGETI = "".join(chr(c) for c in [67, 70, 71, 49, 57])
MCVDSS = 478
MFZDGK = 460
MHXEKV = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
MJIGYO = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
MJMAOA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
MNHTBJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
MNZMJI = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
MOUNBL = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
NBLKXS = "".join(chr(c) for c in [77, 69, 68])
NEJNIB = 285
NHTBJE = 358
NIBXTI = "".join(chr(c) for c in [51, 79, 80])
NIBXYB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
NKMLOI = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
NMHXEK = "".join(chr(c) for c in [75, 54, 48, 48])
NQGVUN = 323
NQJYMO = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
NQLNMH = "".join(chr(c) for c in [68, 74, 83, 52])
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 49, 49])
NRJZTA = "".join(chr(c) for c in [67, 70, 71, 54])
NRSJMC = 3
NRXCHW = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
NXNKML = "".join(chr(c) for c in [72, 84, 82])
NZMJIG = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
OACMCV = "".join(chr(c) for c in [67, 70, 71, 50, 57])
OAWBSI = "".join(
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
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 50, 52])
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
OJRJHI = "".join(chr(c) for c in [76, 79, 87])
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ONPYYL = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
OOQNRS = "".join(chr(c) for c in [66, 76])
OPHUGT = "".join(chr(c) for c in [80, 49, 72])
OQNRSJ = "".join(chr(c) for c in [67, 80])
OUNBLK = 313
OUSPBW = 279
OUYNQJ = "".join(
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
PBWJYK = 280
PFTSIF = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
PHUGTY = "".join(chr(c) for c in [80, 49, 76])
PHUOJR = "".join(chr(c) for c in [80, 49])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
POUYNQ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
PQIPOU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
PUNRJZ = "".join(chr(c) for c in [67, 70, 71, 53])
PYYLIU = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 364
QFFTTI = 7
QFYLJU = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
QGVUNX = "".join(chr(c) for c in [83, 79, 117, 116, 53])
QIEFXQ = 2
QIPOUY = 273
QJYMOU = 282
QLNMHX = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
QNRSJM = "".join(chr(c) for c in [79, 51])
QPLSPF = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
QRJJJV = "".join(chr(c) for c in [75, 50, 48, 48])
QSNQLN = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
QTMFZD = 459
QVXOIH = 470
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 256
RJHIUS = "".join(chr(c) for c in [80, 50])
RJJJVY = "".join(chr(c) for c in [75, 52, 48, 48])
RJZTAT = 454
RKINEJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
RSJMCB = "".join(chr(c) for c in [76, 49, 50, 48])
RTFMNH = "".join(chr(c) for c in [75, 51, 48, 48])
RXCHWD = 332
RYXBQF = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [70, 117, 108, 108])
SELHBQ = 331
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 49, 56])
SIFJBI = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
SIRYXB = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
SJMCBF = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
SKSOKP = 304
SNQLNM = "".join(chr(c) for c in [77, 73, 65])
SOKPHU = 305
SPBWJY = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
SPFTSI = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
SSRURA = "".join(chr(c) for c in [76, 73])
SSUHBV = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
STSEMC = "".join(chr(c) for c in [67, 70, 71, 49, 55])
SUHBVW = 296
SXUJUT = 367
TACCPQ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
TATDZX = "".join(chr(c) for c in [67, 70, 71, 56])
TBJEUT = 360
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 57])
TFMNHT = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
THBSKS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
TIDUBS = 293
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 50, 49])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 49, 50])
TOPHUG = "".join(chr(c) for c in [78, 65])
TSEMCG = 465
TSIFJB = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
TTIDUB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
TYIYWS = "".join(chr(c) for c in [80, 51, 76])
UBSSUH = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
UBYGDS = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
UGSELH = 330
UGTYIY = "".join(chr(c) for c in [80, 50, 76])
UHBVWV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
UIKFWR = 314
UJUTYE = 262
UNBLKX = "".join(chr(c) for c in [78, 79])
UNRJZT = 453
UNXNKM = 326
UOJRJH = "".join(chr(c) for c in [72, 73, 71, 72])
UQEXLS = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
URAZMK = 56
USOOQN = 260
USPBWJ = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
UTOPHU = 320
UTYEKC = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
UXFEFJ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
UYNQJY = "".join(
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
VDNQGV = 322
VDQLAI = "".join(chr(c) for c in [85, 76])
VDSSRU = 479
VHFTHE = 6
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = 476
VUBYGD = 300
VUNXNK = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
VWVUBY = 299
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 50, 51])
VYFCRT = "".join(chr(c) for c in [75, 53])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [54, 52, 75])
WAONPY = "".join(chr(c) for c in [83, 84, 65, 82, 84])
WBSIRY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
WDAFIK = 449
WIVDNQ = 321
WJYKLG = 281
WMNZMJ = 355
WRKINE = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
WSKWIV = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
WVUBYG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
XBQFYL = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
XCHWDA = "".join(chr(c) for c in [67, 70, 71, 48])
XEKVKZ = "".join(chr(c) for c in [105, 110, 89, 84])
XFEFJT = 267
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 50, 54])
XLSXUJ = 365
XNQTMF = 458
XOIHBX = 471
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 50, 50])
XSJWMN = 353
XTIACQ = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
XUJUTY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
XWAJVD = "".join(chr(c) for c in [52, 56, 75])
XYBQSN = 289
YBQSNQ = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
YEKCWA = "".join(
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
YFCRTF = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
YGDSBD = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
YIYWSK = "".join(chr(c) for c in [80, 52, 72])
YKLGQP = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
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
YLJUIK = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
YMOUNB = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
YNQJYM = "".join(chr(c) for c in [67, 80, 79, 84])
YOUSPB = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWSKWI = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
YYLIUX = 264
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 461
ZILXWA = 290
ZMJIGY = 275
ZTATDZ = 455
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 50, 56])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 49, 48])
AJVDQL = [ILXWAJ, LXWAJV, XWAJVD, WAJVDQ]
BDJQRJ = [DSBDJQ, SBDJQR]
CQFFTT = [IACQFF, ACQFFT]
DSSRUR = []
FMNHTB = [
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    YFCRTF,
    FCRTFM,
    EKVKZI,
    HECVYY,
    HECVYY,
    HECVYY,
    CRTFMN,
    RTFMNH,
    TFMNHT,
]
FYLJUI = [HECVYY, QFYLJU, QFYLJU, QFYLJU]
GYOUSP = [HECVYY, IGYOUS, IGYOUS, IGYOUS]
IBXTIA = [DNIBXT, NIBXTI]
IIDNIB = [OOQNRS, AIIDNI]
JRJHIU = [ASSAKQ, UOJRJH, OJRJHI]
LKXSJW = [UNBLKX, QXPICX, NBLKXS, XPICXQ, BLKXSJ]
NPYYLI = [KCWAON, CWAONP, WAONPY, AONPYY, ONPYYL]
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
QLAIID = [VDQLAI, DQLAII]
QNRXCH = [
    TOPHUG,
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
    OQNRSJ,
]
RAHEOC = [ASSAKQ, LRAHEO]
RURAZM = [
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
]
SKWIVD = [
    TOPHUG,
    OPHUGT,
    PHUGTY,
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    IUSOOQ,
    YWSKWI,
    OQNRSJ,
    QNRSJM,
    RSJMCB,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    WSKWIV,
]
SOOQNR = [ASSAKQ, UOJRJH]
SRURAZ = [
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
    UQEXLS,
    EXLSXU,
    LSXUJU,
    SSRURA,
]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
TYEKCW = [JUTYEK, UTYEKC]
VKZILX = [
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
    EKVKZI,
    KVKZIL,
]
XNKMLO = [
    TOPHUG,
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
    NXNKML,
]
ZUQEXL = [FEGZUQ, EGZUQE, GZUQEX]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return URAZMK

    @property
    def begin(self):
        return RAZMKQ

    @property
    def end(self):
        return AZMKQT

    @property
    def all_device_keys(self):
        return SRURAZ

    @property
    def user_demand_keys(self):
        return RURAZM

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
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, SAKQXP),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, SAKQXP),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, SAKQXP),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, SAKQXP),
            PHUOJR: GeckoEnumStructAccessor(
                self.struct, PHUOJR, HUOJRJ, ICXQIE, JRJHIU, None, CXQIEF, None
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, HUOJRJ, QIEFXQ, JRJHIU, None, CXQIEF, None
            ),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, HUOJRJ, CXQIEF, JRJHIU, None, CXQIEF, None
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, HUOJRJ, VHFTHE, JRJHIU, None, CXQIEF, None
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, ICXQIE, SOOQNR, None, QIEFXQ, None
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, USOOQN, AHEOCT, RAHEOC, None, QIEFXQ, None
            ),
            OQNRSJ: GeckoEnumStructAccessor(
                self.struct, OQNRSJ, USOOQN, QIEFXQ, RAHEOC, None, QIEFXQ, None
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, USOOQN, NRSJMC, RAHEOC, None, QIEFXQ, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, USOOQN, CXQIEF, RAHEOC, None, QIEFXQ, None
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, USOOQN, JMCBFE, RAHEOC, None, QIEFXQ, None
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, USOOQN, VHFTHE, RAHEOC, None, QIEFXQ, None
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, None, ZUQEXL, None, None, SAKQXP
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, None, ZUQEXL, None, None, None
            ),
            EXLSXU: GeckoWordStructAccessor(self.struct, EXLSXU, XLSXUJ, None),
            LSXUJU: GeckoWordStructAccessor(self.struct, LSXUJU, SXUJUT, SAKQXP),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UJUTYE, ICXQIE, TYEKCW, None, QIEFXQ, SAKQXP
            ),
            YEKCWA: GeckoEnumStructAccessor(
                self.struct, YEKCWA, EKCWAO, None, NPYYLI, None, None, SAKQXP
            ),
            PYYLIU: GeckoTimeStructAccessor(self.struct, PYYLIU, YYLIUX, SAKQXP),
            YLIUXF: GeckoByteStructAccessor(self.struct, YLIUXF, LIUXFE, SAKQXP),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, UJUTYE, QIEFXQ, TYEKCW, None, QIEFXQ, SAKQXP
            ),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, XFEFJT, None, NPYYLI, None, None, SAKQXP
            ),
            FEFJTA: GeckoTimeStructAccessor(self.struct, FEFJTA, EFJTAC, SAKQXP),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, SAKQXP),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, SAKQXP),
            CCPQIP: GeckoByteStructAccessor(self.struct, CCPQIP, CPQIPO, SAKQXP),
            PQIPOU: GeckoBoolStructAccessor(self.struct, PQIPOU, QIPOUY, ICXQIE, None),
            IPOUYN: GeckoBoolStructAccessor(self.struct, IPOUYN, QIPOUY, QIEFXQ, None),
            POUYNQ: GeckoBoolStructAccessor(self.struct, POUYNQ, QIPOUY, NRSJMC, None),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, QIPOUY, CXQIEF, None),
            UYNQJY: GeckoBoolStructAccessor(self.struct, UYNQJY, QIPOUY, JMCBFE, None),
            YNQJYM: GeckoBoolStructAccessor(self.struct, YNQJYM, JVHFTH, QIEFXQ, None),
            NQJYMO: GeckoBoolStructAccessor(self.struct, NQJYMO, QJYMOU, NRSJMC, None),
            JYMOUN: GeckoBoolStructAccessor(self.struct, JYMOUN, QJYMOU, JMCBFE, None),
            YMOUNB: GeckoBoolStructAccessor(self.struct, YMOUNB, QJYMOU, VHFTHE, None),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, LKXSJW, None, None, None
            ),
            KXSJWM: GeckoBoolStructAccessor(self.struct, KXSJWM, XSJWMN, JMCBFE, None),
            SJWMNZ: GeckoBoolStructAccessor(self.struct, SJWMNZ, XSJWMN, VHFTHE, None),
            JWMNZM: GeckoWordStructAccessor(self.struct, JWMNZM, WMNZMJ, None),
            MNZMJI: GeckoBoolStructAccessor(self.struct, MNZMJI, JVHFTH, AHEOCT, None),
            NZMJIG: GeckoTempStructAccessor(self.struct, NZMJIG, ZMJIGY, None),
            MJIGYO: GeckoTempStructAccessor(self.struct, MJIGYO, JIGYOU, None),
            IGYOUS: GeckoEnumStructAccessor(
                self.struct, IGYOUS, USOOQN, JMCBFE, GYOUSP, None, CXQIEF, None
            ),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, OUSPBW, QIEFXQ, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, OUSPBW, VHFTHE, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, PBWJYK, QIEFXQ, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, WJYKLG, AHEOCT, None),
            JYKLGQ: GeckoBoolStructAccessor(
                self.struct, JYKLGQ, WJYKLG, QIEFXQ, SAKQXP
            ),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, KLGQPL, AHEOCT, None),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, JVHFTH, NRSJMC, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, QJYMOU, ICXQIE, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, QJYMOU, AHEOCT, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, LSPFTS, QIEFXQ, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, LSPFTS, NRSJMC, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, FTSIFJ, NRSJMC, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, FTSIFJ, CXQIEF, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, FTSIFJ, JMCBFE, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FTSIFJ, VHFTHE, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, JBIAMJ, NRSJMC, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, JBIAMJ, CXQIEF, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, JBIAMJ, JMCBFE, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, JBIAMJ, VHFTHE, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, QIEFXQ, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, JMAOAW, NRSJMC, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, KLGQPL, NRSJMC, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, XSJWMN, ICXQIE, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, XSJWMN, AHEOCT, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, BSIRYX, ICXQIE, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, PBWJYK, ICXQIE, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, LSPFTS, ICXQIE, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, LSPFTS, AHEOCT, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, LSPFTS, CXQIEF, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, ICXQIE, None),
            QFYLJU: GeckoEnumStructAccessor(
                self.struct, QFYLJU, BQFYLJ, AHEOCT, FYLJUI, None, CXQIEF, None
            ),
            YLJUIK: GeckoWordStructAccessor(self.struct, YLJUIK, LJUIKF, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, UIKFWR, ICXQIE, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, KFWRKI, ICXQIE, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, KFWRKI, AHEOCT, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, JMAOAW, ICXQIE, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, JMAOAW, AHEOCT, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, JMAOAW, CXQIEF, None),
            INEJNI: GeckoWordStructAccessor(self.struct, INEJNI, NEJNIB, None),
            EJNIBX: GeckoByteStructAccessor(self.struct, EJNIBX, JNIBXY, None),
            NIBXYB: GeckoByteStructAccessor(self.struct, NIBXYB, IBXYBQ, None),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, None, VKZILX, None, None, None
            ),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, ZILXWA, ICXQIE, AJVDQL, None, CXQIEF, None
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, ZILXWA, QIEFXQ, QLAIID, None, QIEFXQ, None
            ),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, ZILXWA, NRSJMC, IIDNIB, None, QIEFXQ, None
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, ZILXWA, CXQIEF, IBXTIA, None, QIEFXQ, None
            ),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, ZILXWA, JMCBFE, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, ZILXWA, VHFTHE, None),
            TIACQF: GeckoEnumStructAccessor(
                self.struct, TIACQF, ZILXWA, QFFTTI, CQFFTT, None, QIEFXQ, None
            ),
            FFTTID: GeckoWordStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, None),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, None),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, None),
            SSUHBV: GeckoByteStructAccessor(self.struct, SSUHBV, SUHBVW, None),
            UHBVWV: GeckoWordStructAccessor(self.struct, UHBVWV, HBVWVU, None),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, None),
            WVUBYG: GeckoByteStructAccessor(self.struct, WVUBYG, VUBYGD, None),
            UBYGDS: GeckoWordStructAccessor(self.struct, UBYGDS, BYGDSB, None),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, GDSBDJ, None, BDJQRJ, None, QIEFXQ, SAKQXP
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, None, FMNHTB, None, None, None
            ),
            MNHTBJ: GeckoWordStructAccessor(self.struct, MNHTBJ, NHTBJE, None),
            HTBJEU: GeckoByteStructAccessor(self.struct, HTBJEU, TBJEUT, None),
            BJEUTO: GeckoByteStructAccessor(self.struct, BJEUTO, JEUTOP, None),
            EUTOPH: GeckoEnumStructAccessor(
                self.struct, EUTOPH, UTOPHU, None, SKWIVD, None, None, SAKQXP
            ),
            KWIVDN: GeckoEnumStructAccessor(
                self.struct, KWIVDN, WIVDNQ, None, SKWIVD, None, None, SAKQXP
            ),
            IVDNQG: GeckoEnumStructAccessor(
                self.struct, IVDNQG, VDNQGV, None, SKWIVD, None, None, SAKQXP
            ),
            DNQGVU: GeckoEnumStructAccessor(
                self.struct, DNQGVU, NQGVUN, None, SKWIVD, None, None, SAKQXP
            ),
            QGVUNX: GeckoEnumStructAccessor(
                self.struct, QGVUNX, GVUNXN, None, SKWIVD, None, None, SAKQXP
            ),
            VUNXNK: GeckoEnumStructAccessor(
                self.struct, VUNXNK, UNXNKM, None, XNKMLO, None, None, SAKQXP
            ),
            NKMLOI: GeckoByteStructAccessor(self.struct, NKMLOI, KMLOIJ, SAKQXP),
            MLOIJU: GeckoByteStructAccessor(self.struct, MLOIJU, LOIJUG, SAKQXP),
            OIJUGS: GeckoByteStructAccessor(self.struct, OIJUGS, IJUGSE, SAKQXP),
            JUGSEL: GeckoByteStructAccessor(self.struct, JUGSEL, UGSELH, SAKQXP),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, SAKQXP),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, SAKQXP),
            HBQNRX: GeckoEnumStructAccessor(
                self.struct, HBQNRX, BQNRXC, None, QNRXCH, None, None, SAKQXP
            ),
            NRXCHW: GeckoByteStructAccessor(self.struct, NRXCHW, RXCHWD, SAKQXP),
        }

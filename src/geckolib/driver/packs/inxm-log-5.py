#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v5'
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
ACMCVD = "".join(chr(c) for c in [76, 73])
ACQFFT = "".join(chr(c) for c in [82, 104, 83, 87, 84, 114, 105, 97, 99, 79, 72])
AFIKJP = 453
AHEOCT = 294
AIIDNI = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
AJVDQL = 257
AKQXPI = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101, 83, 105, 103, 110]
)
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 49, 57])
AMJMAO = 351
AOAWBS = 269
AONPYY = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ASSAKQ = "".join(chr(c) for c in [75, 54, 48, 48, 85, 112, 108, 111, 97, 100])
ATDZXN = 459
AWBSIR = "".join(
    chr(c) for c in [67, 108, 101, 97, 110, 83, 117, 115, 112, 101, 110, 100, 101, 100]
)
BDJQRJ = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
BFEGZU = "".join(chr(c) for c in [78, 65])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 51, 48])
BIAMJM = 350
BJEUTO = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
BLKXSJ = "".join(chr(c) for c in [79, 110, 122, 101, 110])
BMJVHF = 263
BQFYLJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
BQNRXC = "".join(chr(c) for c in [67, 70, 71, 49])
BQSNQL = "".join(
    chr(c) for c in [70, 114, 101, 113, 68, 101, 116, 101, 99, 69, 114, 114]
)
BSIRYX = 279
BSKSOK = "".join(chr(c) for c in [79, 70, 70])
BSSUHB = "".join(
    chr(c)
    for c in [
        82,
        104,
        72,
        101,
        97,
        116,
        101,
        114,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        101,
        100,
    ]
)
BVWVUB = 319
BWJYKL = "".join(chr(c) for c in [78, 69, 87])
BXIBHZ = 476
BXTIAC = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
BXYBQS = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
BYGDSB = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
CBFEGZ = "".join(chr(c) for c in [70, 73, 88])
CCPQIP = "".join(chr(c) for c in [66, 76])
CGETIX = 470
CHWDAF = 451
CPQIPO = "".join(chr(c) for c in [67, 80])
CQBMJV = 261
CQFFTT = "".join(chr(c) for c in [82, 104, 72, 119, 84, 114, 105, 97, 99, 79, 72])
CRTFMN = "".join(chr(c) for c in [54, 52, 75])
CTHBSK = 298
CVDSSR = 256
CVYYPI = "".join(chr(c) for c in [72, 50])
CWAONP = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
CXQIEF = "".join(chr(c) for c in [79, 85, 84, 50, 65, 82, 101, 97, 100])
DAFIKJ = "".join(chr(c) for c in [67, 70, 71, 53])
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 49, 55])
DJQRJJ = "".join(chr(c) for c in [105, 110, 88, 77])
DNIBXT = "".join(chr(c) for c in [82, 104, 72, 114, 72, 76])
DQLAII = "".join(chr(c) for c in [82, 104, 76, 111, 119, 70, 108, 111])
DSBDJQ = "".join(chr(c) for c in [77, 73, 65])
DUBSSU = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
DZXNQT = 460
EAKSTS = 466
ECVYYP = "".join(chr(c) for c in [72, 49])
EFJTAC = "".join(chr(c) for c in [80, 52])
EFXQGL = "".join(chr(c) for c in [79, 85, 84, 51, 65, 82, 101, 97, 100])
EJNIBX = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
EKCWAO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
EKVKZI = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
ELHBQN = 347
EMCGET = 469
EOCTHB = 296
ETIXQV = 471
EUTOPH = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
EXLSXU = "".join(chr(c) for c in [85, 100, 76, 105])
FCRTFM = "".join(chr(c) for c in [52, 56, 75])
FEFJTA = "".join(chr(c) for c in [80, 51])
FEGZUQ = "".join(chr(c) for c in [83, 67, 65, 78])
FFTTID = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
FIKJPU = "".join(chr(c) for c in [67, 70, 71, 54])
FJBIAM = 314
FJTACC = 6
FMNHTB = "".join(chr(c) for c in [85, 76])
FTHECV = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTSIFJ = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
FTTIDU = "".join(chr(c) for c in [82, 104, 83, 119, 75, 105, 110, 84, 101, 109, 112])
FWRKIN = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
FXQGLR = 288
FYLJUI = "".join(chr(c) for c in [78, 79])
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 49, 54])
GDSBDJ = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 50, 51])
GKEAKS = 465
GLRAHE = "".join(chr(c) for c in [79, 85, 84, 53, 65, 82, 101, 97, 100])
GQPLSP = 316
GSELHB = 346
GTYIYW = 329
GVUNXN = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 118])
GZUQEX = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HBQNRX = 448
HBSKSO = 275
HBVWVU = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 50, 56])
HECVYY = "".join(chr(c) for c in [83, 50])
HEOCTH = "".join(chr(c) for c in [79, 85, 84, 55, 65, 82, 101, 97, 100])
HFTHEC = 353
HIUSOO = "".join(chr(c) for c in [85, 100, 80, 52])
HTBJEU = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
HUGTYI = 328
HUOJRJ = "".join(chr(c) for c in [65, 76, 76])
HWDAFI = "".join(chr(c) for c in [67, 70, 71, 52])
HXEKVK = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
HZVOAC = 478
IACQFF = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 79, 72])
IAMJMA = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
IBHZVO = 477
IBXTIA = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IBXYBQ = "".join(
    chr(c) for c in [75, 105, 110, 80, 117, 114, 103, 101, 65, 99, 116, 105, 118, 101]
)
ICXQIE = 282
IDNIBX = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
IDUBSS = 260
IEFXQG = 286
IFJBIA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IGYOUS = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
IHBXIB = 475
IIDNIB = "".join(chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 84, 101, 109, 112])
IJUGSE = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 118])
IKFWRK = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
IKJPUN = 454
ILXWAJ = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
INEJNI = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
IPIVLA = "".join(chr(c) for c in [76, 101, 97, 114, 110, 105, 110, 103])
IPOUYN = "".join(chr(c) for c in [76, 49, 50, 48])
IRYXBQ = "".join(chr(c) for c in [67, 80, 79, 84])
IUSOOQ = 10
IUXFEF = "".join(chr(c) for c in [76, 79, 87])
IVDNQG = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
IVLASS = "".join(chr(c) for c in [80, 104, 97, 115, 101, 83, 101, 108, 101, 99, 116])
IXQVXO = 472
IYWSKW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
JBIAMJ = "".join(
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
JEUTOP = 324
JHIUSO = 11
JIGYOU = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JJVYFC = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
JMAOAW = 352
JMCBFE = "".join(chr(c) for c in [85, 100, 83, 112, 107, 114, 76, 105, 102, 116])
JNIBXY = 270
JPUNRJ = 455
JQRJJJ = "".join(chr(c) for c in [75, 54, 48, 48])
JRJHIU = "".join(chr(c) for c in [85, 100, 80, 51])
JTACCP = "".join(chr(c) for c in [80, 53])
JUGSEL = 345
JUIKFW = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
JUTYEK = "".join(chr(c) for c in [85, 100, 86, 83, 80, 51])
JVDQLA = "".join(
    chr(c)
    for c in [82, 104, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
JVHFTH = 256
JVYFCR = 322
JWMNZM = "".join(chr(c) for c in [86, 115, 112, 49, 77, 105, 110])
JYMOUN = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
JZTATD = "".join(chr(c) for c in [67, 70, 71, 49, 48])
KCWAON = 359
KEAKST = "".join(chr(c) for c in [67, 70, 71, 49, 56])
KFWRKI = 272
KINEJN = 349
KJPUNR = "".join(chr(c) for c in [67, 70, 71, 55])
KLGQPL = 308
KMLOIJ = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 70, 117, 108, 108]
)
KPHUOJ = 2
KQXPIC = 300
KSOKPH = "".join(chr(c) for c in [72, 73])
KSTSEM = 467
KVKZIL = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
KWIVDN = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
KXSJWM = 274
KZILXW = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
LAIIDN = 258
LASSAK = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
LGQPLS = "".join(
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
LHBQNR = "".join(chr(c) for c in [67, 70, 71, 48])
LIUXFE = "".join(chr(c) for c in [72, 73, 71, 72])
LKXSJW = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121])
LNMHXE = "".join(
    chr(c) for c in [76, 101, 97, 114, 110, 80, 104, 97, 115, 101, 69, 114, 114]
)
LOIJUG = "".join(chr(c) for c in [75, 54, 48, 48, 73, 68])
LRAHEO = 292
LSPFTS = 310
LSXUJU = "".join(chr(c) for c in [77, 69, 68])
LXWAJV = "".join(chr(c) for c in [114, 72, 73, 100])
MAOAWB = "".join(chr(c) for c in [80, 117, 114, 103, 101])
MCBFEG = "".join(chr(c) for c in [85, 100, 70, 98])
MCGETI = "".join(chr(c) for c in [67, 70, 71, 50, 50])
MFZDGK = 463
MHXEKV = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
MJIGYO = 348
MJMAOA = "".join(
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
MJVHFT = "".join(chr(c) for c in [72, 111, 117, 114, 115])
MLOIJU = 341
MNHTBJ = "".join(chr(c) for c in [67, 69])
MNZMJI = "".join(chr(c) for c in [86, 83, 80, 51, 70, 114, 111, 110, 116])
MOUNBL = "".join(chr(c) for c in [85, 80])
NBLKXS = "".join(chr(c) for c in [83, 97, 110, 105])
NEJNIB = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
NIBXTI = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
NIBXYB = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
NKMLOI = 339
NMHXEK = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
NPYYLI = "".join(chr(c) for c in [85, 100, 68, 114, 97, 105, 110])
NQGVUN = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 73, 68])
NQLNMH = "".join(
    chr(c)
    for c in [
        67,
        111,
        110,
        116,
        97,
        99,
        116,
        111,
        114,
        67,
        111,
        105,
        108,
        70,
        97,
        105,
        108,
        69,
        114,
        114,
    ]
)
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 49, 52])
NRJZTA = "".join(chr(c) for c in [67, 70, 71, 57])
NRSJMC = 8
NRXCHW = "".join(chr(c) for c in [67, 70, 71, 50])
NXNKML = 338
NZMJIG = 302
OAWBSI = "".join(chr(c) for c in [67, 108, 101, 97, 110])
OCTHBS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 82, 101, 97, 100])
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 50, 55])
OIJUGS = 343
OJRJHI = 12
OKPHUO = 14
ONPYYL = 361
OOQNRS = "".join(chr(c) for c in [85, 100, 66, 76])
OPHUGT = 327
OQNRSJ = "".join(chr(c) for c in [79, 78])
OUSPBW = 307
OUYNQJ = 7
PBWJYK = "".join(chr(c) for c in [83, 84, 65, 82, 84])
PFTSIF = 311
PHUGTY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
PHUOJR = 4
PICXQI = "".join(chr(c) for c in [79, 85, 84, 49, 66, 82, 101, 97, 100])
PIPIVL = "".join(chr(c) for c in [76, 101, 97, 114, 110, 70, 97, 105, 108])
PIVLAS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 108, 101, 99, 116]
)
PLSPFT = "".join(
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
POUYNQ = "".join(chr(c) for c in [70, 65, 78])
PQIPOU = "".join(chr(c) for c in [79, 51])
PUNRJZ = "".join(chr(c) for c in [67, 70, 71, 56])
PYYLIU = 362
QBMJVH = "".join(chr(c) for c in [82, 104, 84, 114, 105, 97, 99, 84, 101, 109, 112])
QEXLSX = 0
QFFTTI = "".join(chr(c) for c in [82, 104, 72, 114, 75, 105, 110])
QFYLJU = 268
QGLRAH = 290
QGVUNX = 335
QIEFXQ = "".join(chr(c) for c in [79, 85, 84, 50, 66, 82, 101, 97, 100])
QIPOUY = 3
QJYMOU = "".join(chr(c) for c in [65, 108, 119, 97, 121, 79, 110])
QLAIID = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121, 69, 114, 114])
QLNMHX = "".join(
    chr(c)
    for c in [
        78,
        111,
        72,
        101,
        97,
        116,
        101,
        114,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
        69,
        114,
        114,
    ]
)
QNRXCH = 449
QPLSPF = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
QRJJJV = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
QSNQLN = 277
QTMFZD = 462
QVXOIH = 473
QXPICX = "".join(chr(c) for c in [79, 85, 84, 49, 65, 82, 101, 97, 100])
RAHEOC = "".join(chr(c) for c in [79, 85, 84, 54, 65, 82, 101, 97, 100])
RJJJVY = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
RJZTAT = 457
RKINEJ = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
RSJMCB = "".join(chr(c) for c in [85, 100, 84, 118, 76, 105, 102, 116])
RXCHWD = 450
RYXBQF = "".join(chr(c) for c in [68, 114, 97, 105, 110, 110, 105, 110, 103])
SBDJQR = "".join(chr(c) for c in [68, 74, 83, 52])
SELHBQ = "".join(chr(c) for c in [75, 54, 48, 48, 80, 114, 111, 116, 111, 99, 111, 108])
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 50, 49])
SIFJBI = 313
SIRYXB = "".join(chr(c) for c in [70, 105, 108, 116, 79, 84])
SJMCBF = 5
SJWMNZ = 301
SKSOKP = "".join(chr(c) for c in [76, 79])
SKWIVD = 333
SNQLNM = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
SOOQNR = 9
SPBWJY = "".join(chr(c) for c in [83, 84, 79, 80])
SPFTSI = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
SSAKQX = "".join(chr(c) for c in [80, 111, 119, 101, 114, 117, 112])
SSUHBV = "".join(
    chr(c)
    for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
STSEMC = "".join(chr(c) for c in [67, 70, 71, 50, 48])
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
TACCPQ = 355
TATDZX = "".join(chr(c) for c in [67, 70, 71, 49, 49])
TBJEUT = 323
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 49, 50])
TFMNHT = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
THBSKS = "".join(chr(c) for c in [85, 100, 80, 49])
THECVY = "".join(chr(c) for c in [83, 49])
TIACQF = 259
TIDUBS = "".join(
    chr(c)
    for c in [82, 104, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101, 100]
)
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 50, 52])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 49, 53])
TOPHUG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
TSEMCG = 468
TSIFJB = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
TTIDUB = "".join(chr(c) for c in [82, 104, 72, 87, 75, 105, 110])
TYEKCW = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
TYIYWS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
UBSSUH = "".join(chr(c) for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107])
UBYGDS = 321
UGSELH = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 108])
UGTYIY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
UHBVWV = 317
UIKFWR = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
UJUTYE = 303
UNBLKX = "".join(chr(c) for c in [83, 112, 107, 114, 76, 105, 102, 116])
UNRJZT = 456
UNXNKM = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 108])
UOJRJH = "".join(chr(c) for c in [85, 100, 80, 50])
UQEXLS = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116])
USOOQN = "".join(chr(c) for c in [85, 100, 80, 53])
USPBWJ = "".join(chr(c) for c in [73, 68, 76, 69])
UTOPHU = 325
UTYEKC = 304
UYNQJY = "".join(chr(c) for c in [70, 98])
VDNQGV = "".join(chr(c) for c in [70, 117, 108, 108])
VDQLAI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
VDSSRU = 479
VHFTHE = "".join(chr(c) for c in [77, 101, 110, 117])
VKZILX = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
VLASSA = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
VOACMC = 479
VUBYGD = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
VUNXNK = 337
VWVUBY = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 50, 54])
VYFCRT = "".join(chr(c) for c in [49, 54, 75])
VYYPIP = "".join(chr(c) for c in [72, 51])
WAJVDQ = "".join(chr(c) for c in [82, 104, 67, 111, 109, 109, 69, 114, 114])
WAONPY = 360
WBSIRY = "".join(
    chr(c) for c in [67, 108, 101, 97, 110, 83, 117, 115, 112, 101, 110, 100, 85, 68]
)
WDAFIK = 452
WIVDNQ = 357
WJYKLG = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
WMNZMJ = 305
WRKINE = 265
WSKWIV = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
WVUBYG = 320
XBQFYL = 267
XCHWDA = "".join(chr(c) for c in [67, 70, 71, 51])
XEKVKZ = 278
XFEFJT = "".join(chr(c) for c in [80, 50])
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 50, 57])
XLSXUJ = 306
XNKMLO = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 49, 75, 87]
)
XNQTMF = 461
XOIHBX = 474
XPICXQ = 280
XQGLRA = "".join(chr(c) for c in [79, 85, 84, 52, 65, 82, 101, 97, 100])
XQIEFX = 284
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 50, 53])
XSJWMN = "".join(chr(c) for c in [86, 115, 112, 49, 70, 114, 111, 110, 116])
XTIACQ = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 80, 114])
XUJUTY = "".join(chr(c) for c in [85, 100, 86, 83, 80, 49])
XWAJVD = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
XYBQSN = 271
YBQSNQ = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
YEKCWA = 358
YFCRTF = "".join(chr(c) for c in [51, 50, 75])
YGDSBD = "".join(chr(c) for c in [105, 110, 88, 69])
YIYWSK = 331
YKLGQP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YLIUXF = 356
YLJUIK = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
YMOUNB = "".join(chr(c) for c in [68, 79, 87, 78])
YNQJYM = 354
YOUSPB = "".join(
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
YPIPIV = "".join(chr(c) for c in [70, 114])
YWSKWI = 332
YXBQFY = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
YYLIUX = "".join(chr(c) for c in [80, 49])
YYPIPI = "".join(chr(c) for c in [72, 52])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 464
ZILXWA = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
ZMJIGY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ZTATDZ = 458
ZUQEXL = 1
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 51, 49])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 49, 51])
ACCPQI = [BSKSOK, LIUXFE]
CMCVDS = [
    YYLIUX,
    XFEFJT,
    FEFJTA,
    EFJTAC,
    JTACCP,
    CCPQIP,
    CPQIPO,
    PQIPOU,
    IPOUYN,
    POUYNQ,
    UYNQJY,
    QJYMOU,
    JYMOUN,
    UNBLKX,
    NBLKXS,
    BLKXSJ,
    LKXSJW,
    XSJWMN,
    JWMNZM,
    MNZMJI,
    ACMCVD,
]
DNQGVU = [IVDNQG, VDNQGV]
EGZUQE = [BSKSOK, CBFEGZ, BFEGZU, FEGZUQ]
GYOUSP = [JIGYOU, IGYOUS]
JJJVYF = [
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
]
JYKLGQ = [USPBWJ, SPBWJY, PBWJYK, BWJYKL, WJYKLG]
LJUIKF = [FYLJUI, SKSOKP, LSXUJU, KSOKPH, YLJUIK]
MCVDSS = [
    THBSKS,
    UOJRJH,
    JRJHIU,
    HIUSOO,
    USOOQN,
    OOQNRS,
    RSJMCB,
    JMCBFE,
    MCBFEG,
    GZUQEX,
    UQEXLS,
    EXLSXU,
    XUJUTY,
    JUTYEK,
    TYEKCW,
    EKCWAO,
    CWAONP,
    AONPYY,
    NPYYLI,
]
NHTBJE = [FMNHTB, MNHTBJ]
NQJYMO = [BSKSOK, BSKSOK, CBFEGZ, FEGZUQ]
OACMCV = []
OUNBLK = [YMOUNB, MOUNBL]
QNRSJM = [BSKSOK, OQNRSJ]
RJHIUS = [BSKSOK, KSOKPH]
RTFMNH = [VYFCRT, YFCRTF, FCRTFM, CRTFMN]
SAKQXP = [
    FTHECV,
    THECVY,
    HECVYY,
    ECVYYP,
    CVYYPI,
    VYYPIP,
    YYPIPI,
    YPIPIV,
    PIPIVL,
    IPIVLA,
    PIVLAS,
    IVLASS,
    VLASSA,
    LASSAK,
    ASSAKQ,
    SSAKQX,
]
SOKPHU = [BSKSOK, SKSOKP, KSOKPH]
SXUJUT = [BSKSOK, SKSOKP, LSXUJU, KSOKPH]
UXFEFJ = [BSKSOK, LIUXFE, IUXFEF]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return SJMCBF

    @property
    def begin(self):
        return CVDSSR

    @property
    def end(self):
        return VDSSRU

    @property
    def all_device_keys(self):
        return CMCVDS

    @property
    def user_demand_keys(self):
        return MCVDSS

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoTempStructAccessor(self.struct, ZCQBMJ, CQBMJV, None),
            QBMJVH: GeckoTempStructAccessor(self.struct, QBMJVH, BMJVHF, None),
            MJVHFT: GeckoByteStructAccessor(self.struct, MJVHFT, JVHFTH, None),
            VHFTHE: GeckoEnumStructAccessor(
                self.struct, VHFTHE, HFTHEC, None, SAKQXP, None, None, None
            ),
            AKQXPI: GeckoByteStructAccessor(self.struct, AKQXPI, KQXPIC, None),
            QXPICX: GeckoWordStructAccessor(self.struct, QXPICX, XPICXQ, None),
            PICXQI: GeckoWordStructAccessor(self.struct, PICXQI, ICXQIE, None),
            CXQIEF: GeckoWordStructAccessor(self.struct, CXQIEF, XQIEFX, None),
            QIEFXQ: GeckoWordStructAccessor(self.struct, QIEFXQ, IEFXQG, None),
            EFXQGL: GeckoWordStructAccessor(self.struct, EFXQGL, FXQGLR, None),
            XQGLRA: GeckoWordStructAccessor(self.struct, XQGLRA, QGLRAH, None),
            GLRAHE: GeckoWordStructAccessor(self.struct, GLRAHE, LRAHEO, None),
            RAHEOC: GeckoWordStructAccessor(self.struct, RAHEOC, AHEOCT, None),
            HEOCTH: GeckoWordStructAccessor(self.struct, HEOCTH, EOCTHB, None),
            OCTHBS: GeckoWordStructAccessor(self.struct, OCTHBS, CTHBSK, None),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, HBSKSO, OKPHUO, SOKPHU, KPHUOJ, PHUOJR, HUOJRJ
            ),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, HBSKSO, OJRJHI, SOKPHU, KPHUOJ, PHUOJR, HUOJRJ
            ),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, HBSKSO, JHIUSO, RJHIUS, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, HBSKSO, IUSOOQ, RJHIUS, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            USOOQN: GeckoEnumStructAccessor(
                self.struct, USOOQN, HBSKSO, SOOQNR, RJHIUS, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, HBSKSO, NRSJMC, QNRSJM, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, HBSKSO, SJMCBF, QNRSJM, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, HBSKSO, PHUOJR, QNRSJM, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, HBSKSO, KPHUOJ, EGZUQE, KPHUOJ, PHUOJR, HUOJRJ
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, HBSKSO, ZUQEXL, QNRSJM, KPHUOJ, KPHUOJ, HUOJRJ
            ),
            UQEXLS: GeckoBoolStructAccessor(
                self.struct, UQEXLS, HBSKSO, QEXLSX, HUOJRJ
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, QEXLSX, SXUJUT, None, PHUOJR, HUOJRJ
            ),
            XUJUTY: GeckoByteStructAccessor(self.struct, XUJUTY, UJUTYE, HUOJRJ),
            JUTYEK: GeckoByteStructAccessor(self.struct, JUTYEK, UTYEKC, HUOJRJ),
            TYEKCW: GeckoByteStructAccessor(self.struct, TYEKCW, YEKCWA, HUOJRJ),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, HUOJRJ),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, HUOJRJ),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, HUOJRJ),
            NPYYLI: GeckoBoolStructAccessor(self.struct, NPYYLI, PYYLIU, None, HUOJRJ),
            YYLIUX: GeckoEnumStructAccessor(
                self.struct, YYLIUX, YLIUXF, QEXLSX, UXFEFJ, None, PHUOJR, None
            ),
            XFEFJT: GeckoEnumStructAccessor(
                self.struct, XFEFJT, YLIUXF, KPHUOJ, UXFEFJ, None, PHUOJR, None
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, YLIUXF, PHUOJR, UXFEFJ, None, PHUOJR, None
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, YLIUXF, FJTACC, UXFEFJ, None, PHUOJR, None
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, QEXLSX, ACCPQI, None, KPHUOJ, None
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, TACCPQ, ZUQEXL, QNRSJM, None, KPHUOJ, None
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, TACCPQ, KPHUOJ, QNRSJM, None, KPHUOJ, None
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, TACCPQ, QIPOUY, QNRSJM, None, KPHUOJ, None
            ),
            IPOUYN: GeckoEnumStructAccessor(
                self.struct, IPOUYN, TACCPQ, PHUOJR, QNRSJM, None, KPHUOJ, None
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, TACCPQ, OUYNQJ, QNRSJM, None, KPHUOJ, None
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, QEXLSX, NQJYMO, None, PHUOJR, None
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, YNQJYM, KPHUOJ, QNRSJM, None, KPHUOJ, None
            ),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, YNQJYM, QIPOUY, OUNBLK, None, KPHUOJ, None
            ),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, YNQJYM, PHUOJR, OUNBLK, None, KPHUOJ, None
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, YNQJYM, SJMCBF, QNRSJM, None, KPHUOJ, None
            ),
            BLKXSJ: GeckoEnumStructAccessor(
                self.struct, BLKXSJ, YNQJYM, FJTACC, QNRSJM, None, KPHUOJ, None
            ),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, None),
            XSJWMN: GeckoByteStructAccessor(self.struct, XSJWMN, SJWMNZ, None),
            JWMNZM: GeckoByteStructAccessor(self.struct, JWMNZM, WMNZMJ, None),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, None),
            ZMJIGY: GeckoEnumStructAccessor(
                self.struct, ZMJIGY, MJIGYO, QEXLSX, GYOUSP, None, KPHUOJ, HUOJRJ
            ),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, None, JYKLGQ, None, None, HUOJRJ
            ),
            YKLGQP: GeckoTimeStructAccessor(self.struct, YKLGQP, KLGQPL, HUOJRJ),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, HUOJRJ),
            QPLSPF: GeckoEnumStructAccessor(
                self.struct, QPLSPF, MJIGYO, ZUQEXL, GYOUSP, None, KPHUOJ, HUOJRJ
            ),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, JYKLGQ, None, None, HUOJRJ
            ),
            SPFTSI: GeckoTimeStructAccessor(self.struct, SPFTSI, PFTSIF, HUOJRJ),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, MJIGYO, KPHUOJ, GYOUSP, None, KPHUOJ, HUOJRJ
            ),
            TSIFJB: GeckoEnumStructAccessor(
                self.struct, TSIFJB, SIFJBI, None, JYKLGQ, None, None, HUOJRJ
            ),
            IFJBIA: GeckoTimeStructAccessor(self.struct, IFJBIA, FJBIAM, HUOJRJ),
            JBIAMJ: GeckoByteStructAccessor(self.struct, JBIAMJ, BIAMJM, HUOJRJ),
            IAMJMA: GeckoByteStructAccessor(self.struct, IAMJMA, AMJMAO, HUOJRJ),
            MJMAOA: GeckoByteStructAccessor(self.struct, MJMAOA, JMAOAW, HUOJRJ),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, AOAWBS, OUYNQJ, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, AOAWBS, SJMCBF, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, AOAWBS, PHUOJR, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, BSIRYX, QIPOUY, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, BSIRYX, QEXLSX, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, BSIRYX, ZUQEXL, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, BSIRYX, OUYNQJ, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, XBQFYL, None, None),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, LJUIKF, None, None, None
            ),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, AOAWBS, QIPOUY, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, AOAWBS, KPHUOJ, None),
            IKFWRK: GeckoTempStructAccessor(self.struct, IKFWRK, KFWRKI, None),
            FWRKIN: GeckoTempStructAccessor(self.struct, FWRKIN, WRKINE, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, KINEJN, ZUQEXL, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, AOAWBS, ZUQEXL, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, AOAWBS, QEXLSX, None),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, JNIBXY, OUYNQJ, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, JNIBXY, FJTACC, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, JNIBXY, SJMCBF, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, XYBQSN, QEXLSX, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, XYBQSN, KPHUOJ, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, QSNQLN, FJTACC, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, QSNQLN, SJMCBF, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, QSNQLN, PHUOJR, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, QSNQLN, QIPOUY, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, QSNQLN, KPHUOJ, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, QSNQLN, ZUQEXL, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, QSNQLN, QEXLSX, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, XEKVKZ, OUYNQJ, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, XEKVKZ, FJTACC, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, XEKVKZ, SJMCBF, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, XEKVKZ, PHUOJR, None),
            KZILXW: GeckoBoolStructAccessor(self.struct, KZILXW, XEKVKZ, QIPOUY, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, XEKVKZ, KPHUOJ, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, XEKVKZ, ZUQEXL, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, XEKVKZ, QEXLSX, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, BSIRYX, PHUOJR, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, AJVDQL, OUYNQJ, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, AJVDQL, QIPOUY, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, AJVDQL, KPHUOJ, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, AJVDQL, QEXLSX, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, LAIIDN, OUYNQJ, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, LAIIDN, FJTACC, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, LAIIDN, SJMCBF, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, LAIIDN, PHUOJR, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, LAIIDN, QIPOUY, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, LAIIDN, KPHUOJ, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, LAIIDN, ZUQEXL, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, LAIIDN, QEXLSX, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, TIACQF, OUYNQJ, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, TIACQF, FJTACC, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, TIACQF, SJMCBF, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, TIACQF, PHUOJR, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, TIACQF, QIPOUY, None),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, TIACQF, KPHUOJ, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, TIACQF, ZUQEXL, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, TIACQF, QEXLSX, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, IDUBSS, PHUOJR, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, IDUBSS, QIPOUY, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, IDUBSS, KPHUOJ, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, IDUBSS, ZUQEXL, None),
            SSUHBV: GeckoBoolStructAccessor(self.struct, SSUHBV, IDUBSS, QEXLSX, None),
            SUHBVW: GeckoWordStructAccessor(self.struct, SUHBVW, UHBVWV, None),
            HBVWVU: GeckoByteStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoByteStructAccessor(self.struct, VWVUBY, WVUBYG, None),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, JJJVYF, None, None, None
            ),
            JJVYFC: GeckoEnumStructAccessor(
                self.struct, JJVYFC, JVYFCR, QEXLSX, RTFMNH, None, PHUOJR, None
            ),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, JVYFCR, KPHUOJ, NHTBJE, None, KPHUOJ, None
            ),
            HTBJEU: GeckoByteStructAccessor(self.struct, HTBJEU, TBJEUT, None),
            BJEUTO: GeckoByteStructAccessor(self.struct, BJEUTO, JEUTOP, None),
            EUTOPH: GeckoWordStructAccessor(self.struct, EUTOPH, UTOPHU, None),
            TOPHUG: GeckoByteStructAccessor(self.struct, TOPHUG, OPHUGT, None),
            PHUGTY: GeckoByteStructAccessor(self.struct, PHUGTY, HUGTYI, None),
            UGTYIY: GeckoWordStructAccessor(self.struct, UGTYIY, GTYIYW, None),
            TYIYWS: GeckoByteStructAccessor(self.struct, TYIYWS, YIYWSK, None),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, None),
            WSKWIV: GeckoWordStructAccessor(self.struct, WSKWIV, SKWIVD, None),
            KWIVDN: GeckoEnumStructAccessor(
                self.struct, KWIVDN, WIVDNQ, None, DNQGVU, None, KPHUOJ, HUOJRJ
            ),
            NQGVUN: GeckoWordStructAccessor(self.struct, NQGVUN, QGVUNX, None),
            GVUNXN: GeckoByteStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoWordStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoWordStructAccessor(self.struct, KMLOIJ, MLOIJU, None),
        }

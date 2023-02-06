#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v52'
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
ACMCVD = 52
ACQFFT = 316
AFIKJP = 455
AHEOCT = 308
AIIDNI = 296
AJVDQL = 293
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 50, 49])
AMJMAO = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
AOAWBS = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
AONPYY = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
ASSAKQ = "".join(chr(c) for c in [85, 100, 80, 49])
ATDZXN = 461
AWBSIR = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
BDJQRJ = 324
BFEGZU = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
BIAMJM = "".join(
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
BJEUTO = "".join(chr(c) for c in [83, 79, 117, 116, 55])
BLKXSJ = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
BMJVHF = 256
BQFYLJ = 314
BQNRXC = "".join(chr(c) for c in [67, 70, 71, 51])
BQSNQL = "".join(chr(c) for c in [75, 54, 48, 48])
BSIRYX = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
BSSUHB = "".join(chr(c) for c in [80, 50, 76])
BVWVUB = "".join(chr(c) for c in [66, 76, 79])
BWJYKL = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
BXIBHZ = 478
BXTIAC = 300
BXYBQS = "".join(chr(c) for c in [68, 74, 83, 52])
BYGDSB = "".join(chr(c) for c in [83, 79, 117, 116, 51])
CBFEGZ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
CCPQIP = "".join(chr(c) for c in [67, 80, 79, 84])
CGETIX = 472
CHWDAF = 453
CMCVDS = 256
CPQIPO = 274
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
CRTFMN = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
CTHBSK = 303
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = 266
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = "".join(chr(c) for c in [67, 70, 71, 55])
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 49, 57])
DJQRJJ = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
DNIBXT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
DNQGVU = 341
DQLAII = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
DSBDJQ = 323
DUBSSU = "".join(chr(c) for c in [80, 49, 76])
DZXNQT = 462
EAKSTS = 468
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 273
EFXQGL = 258
EJNIBX = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
EKCWAO = 264
EKVKZI = "".join(chr(c) for c in [54, 52, 75])
ELHBQN = 449
EMCGET = 471
EOCTHB = 307
ETIXQV = 473
EUTOPH = "".join(chr(c) for c in [83, 79, 117, 116, 56])
FCRTFM = 337
FEFJTA = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FEGZUQ = "".join(chr(c) for c in [70, 85, 76, 76])
FIKJPU = "".join(chr(c) for c in [67, 70, 71, 56])
FJBIAM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
FJTACC = "".join(chr(c) for c in [80, 117, 114, 103, 101])
FMNHTB = 339
FTHECV = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
FTSIFJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
FTTIDU = "".join(chr(c) for c in [83, 79, 117, 116, 49])
FWRKIN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
FYLJUI = 315
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 49, 56])
GDSBDJ = "".join(chr(c) for c in [83, 79, 117, 116, 52])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 50, 53])
GKEAKS = 467
GQPLSP = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
GSELHB = 448
GTYIYW = 330
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
GYOUSP = 281
GZUQEX = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
HBQNRX = 450
HBSKSO = 304
HBVWVU = "".join(chr(c) for c in [80, 52, 76])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 51, 48])
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = 260
HTBJEU = "".join(chr(c) for c in [83, 79, 117, 116, 54])
HUGTYI = 329
HUOJRJ = "".join(chr(c) for c in [76, 79, 87])
HWDAFI = "".join(chr(c) for c in [67, 70, 71, 54])
HXEKVK = "".join(chr(c) for c in [51, 50, 75])
HZVOAC = "".join(chr(c) for c in [76, 73])
IACQFF = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
IAMJMA = "".join(
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
IBHZVO = 479
IBXTIA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
IBXYBQ = "".join(chr(c) for c in [77, 73, 65])
ICXQIE = 2
IDNIBX = 297
IDUBSS = "".join(chr(c) for c in [80, 49, 72])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = 351
IGYOUS = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
IHBXIB = 477
IIDNIB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
IJUGSE = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
IKFWRK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
IKJPUN = 456
INEJNI = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
IRYXBQ = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
IUXFEF = 271
IVDNQG = 340
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = 474
IYWSKW = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
JBIAMJ = "".join(
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
JEUTOP = 326
JHIUSO = "".join(chr(c) for c in [80, 53])
JIGYOU = 280
JJJVYF = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
JJVYFC = 335
JMAOAW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JMCBFE = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
JNIBXY = "".join(chr(c) for c in [105, 110, 88, 69])
JPUNRJ = 457
JQRJJJ = 334
JRJHIU = "".join(chr(c) for c in [80, 51])
JTACCP = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
JUGSEL = 348
JUIKFW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
JUTYEK = "".join(chr(c) for c in [78, 69, 87])
JVDQLA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
JVHFTH = 319
JVYFCR = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
JWMNZM = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
JYKLGQ = 283
JZTATD = "".join(chr(c) for c in [67, 70, 71, 49, 50])
KCWAON = "".join(
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
KEAKST = "".join(chr(c) for c in [67, 70, 71, 50, 48])
KFWRKI = 285
KINEJN = 288
KJPUNR = "".join(chr(c) for c in [67, 70, 71, 57])
KLGQPL = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
KPHUOJ = 261
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
KSTSEM = 469
KWIVDN = 333
KXSJWM = 275
KZILXW = "".join(chr(c) for c in [85, 76])
LAIIDN = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = 284
LHBQNR = "".join(chr(c) for c in [67, 70, 71, 50])
LIUXFE = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
LJUIKF = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
LKXSJW = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
LNMHXE = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
LOIJUG = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
LRAHEO = 1
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
LSXUJU = 263
LXWAJV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
MAOAWB = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
MCBFEG = 310
MCGETI = "".join(chr(c) for c in [67, 70, 71, 50, 52])
MCVDSS = 479
MFZDGK = 465
MHXEKV = "".join(chr(c) for c in [49, 54, 75])
MJIGYO = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
MJMAOA = 354
MJVHFT = "".join(chr(c) for c in [77, 101, 110, 117])
MLOIJU = 346
MNHTBJ = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
MNZMJI = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
MOUNBL = 353
NBLKXS = 355
NEJNIB = 289
NHTBJE = 349
NIBXTI = 299
NIBXYB = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
NKMLOI = 345
NMHXEK = 290
NPYYLI = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
NQJYMO = "".join(chr(c) for c in [77, 69, 68])
NQLNMH = "".join(chr(c) for c in [105, 110, 89, 84])
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 49, 54])
NRJZTA = "".join(chr(c) for c in [67, 70, 71, 49, 49])
NRSJMC = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
NRXCHW = "".join(chr(c) for c in [67, 70, 71, 52])
NXNKML = 344
NZMJIG = 279
OAWBSI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
OCTHBS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 50, 57])
OIJUGS = 347
OJRJHI = "".join(chr(c) for c in [80, 50])
OKPHUO = "".join(chr(c) for c in [80, 49])
ONPYYL = 267
OOQNRS = "".join(chr(c) for c in [79, 51])
OPHUGT = 328
OQNRSJ = 3
OUNBLK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
OUSPBW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
OUYNQJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
PBWJYK = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
PFTSIF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
PHUGTY = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
PHUOJR = "".join(chr(c) for c in [72, 73, 71, 72])
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
POUYNQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
PQIPOU = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
PUNRJZ = "".join(chr(c) for c in [67, 70, 71, 49, 48])
PYYLIU = 268
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QFFTTI = "".join(chr(c) for c in [70, 117, 108, 108])
QFYLJU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
QGLRAH = "".join(chr(c) for c in [79, 78])
QGVUNX = 342
QIEFXQ = 6
QIPOUY = 282
QJYMOU = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QLAIID = 295
QNRSJM = "".join(chr(c) for c in [76, 49, 50, 48])
QNRXCH = 451
QPLSPF = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
QRJJJV = "".join(chr(c) for c in [72, 84, 82])
QSNQLN = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
QTMFZD = 464
QVXOIH = 475
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RJHIUS = "".join(chr(c) for c in [80, 52])
RJZTAT = 459
RKINEJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
RSJMCB = 5
RTFMNH = 338
RXCHWD = 452
RYXBQF = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
SAKQXP = "".join(chr(c) for c in [76, 79])
SBDJQR = "".join(chr(c) for c in [83, 79, 117, 116, 53])
SELHBQ = "".join(chr(c) for c in [67, 70, 71, 49])
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 50, 51])
SIFJBI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
SJMCBF = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = 277
SKSOKP = 305
SKWIVD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
SNQLNM = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
SOKPHU = 306
SOOQNR = "".join(chr(c) for c in [67, 80])
SPBWJY = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
SPFTSI = 350
SSAKQX = 259
SSUHBV = "".join(chr(c) for c in [80, 51, 72])
STSEMC = "".join(chr(c) for c in [67, 70, 71, 50, 50])
SUHBVW = "".join(chr(c) for c in [80, 51, 76])
SXUJUT = "".join(chr(c) for c in [73, 68, 76, 69])
TACCPQ = "".join(
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
TATDZX = "".join(chr(c) for c in [67, 70, 71, 49, 51])
TBJEUT = 325
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 49, 52])
TFMNHT = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
THBSKS = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = 301
TIDUBS = "".join(chr(c) for c in [78, 65])
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 50, 54])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 49, 55])
TOPHUG = "".join(chr(c) for c in [83, 79, 117, 116, 57])
TSEMCG = 470
TSIFJB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
TTIDUB = 320
TYIYWS = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
UBSSUH = "".join(chr(c) for c in [80, 50, 72])
UBYGDS = 321
UGSELH = "".join(chr(c) for c in [67, 70, 71, 48])
UGTYIY = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
UHBVWV = "".join(chr(c) for c in [80, 52, 72])
UIKFWR = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
UJUTYE = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UNBLKX = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
UNRJZT = 458
UNXNKM = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
UQEXLS = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
USOOQN = "".join(chr(c) for c in [66, 76])
USPBWJ = 352
UTOPHU = 327
UTYEKC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
UXFEFJ = "".join(
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
UYNQJY = 313
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
VDQLAI = 294
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VKZILX = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
VUBYGD = "".join(chr(c) for c in [83, 79, 117, 116, 50])
VUNXNK = 343
VWVUBY = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 50, 56])
VYFCRT = 336
WAJVDQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
WAONPY = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
WBSIRY = 309
WDAFIK = 454
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
WJYKLG = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
WRKINE = 287
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
XCHWDA = "".join(chr(c) for c in [67, 70, 71, 53])
XEKVKZ = "".join(chr(c) for c in [52, 56, 75])
XFEFJT = 272
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 51, 49])
XLSXUJ = "".join(
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
XNKMLO = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
XNQTMF = 463
XOIHBX = 476
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 50, 55])
XSJWMN = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
XTIACQ = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
XUJUTY = "".join(chr(c) for c in [83, 84, 79, 80])
XWAJVD = 291
XYBQSN = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
YBQSNQ = "".join(chr(c) for c in [105, 110, 88, 77])
YEKCWA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YFCRTF = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
YGDSBD = 322
YIYWSK = 331
YKLGQP = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
YLIUXF = 270
YLJUIK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
YMOUNB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
YNQJYM = "".join(chr(c) for c in [78, 79])
YOUSPB = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
YPIPIV = 257
YWSKWI = 332
YXBQFY = 311
YYLIUX = "".join(
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
YYPIPI = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 466
ZILXWA = "".join(chr(c) for c in [67, 69])
ZMJIGY = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
ZTATDZ = 460
ZUQEXL = 262
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 49, 53])
BHZVOA = []
EGZUQE = [CBFEGZ, BFEGZU, FEGZUQ]
EXLSXU = [UQEXLS, QEXLSX]
FFTTID = [CQFFTT, QFFTTI]
FXQGLR = [IVLASS, AKQXPI]
GLRAHE = [IVLASS, QGLRAH]
ILXWAJ = [KZILXW, ZILXWA]
IUSOOQ = [IVLASS, PHUOJR]
JYMOUN = [YNQJYM, SAKQXP, NQJYMO, AKQXPI, QJYMOU]
KQXPIC = [IVLASS, SAKQXP, AKQXPI]
KVKZIL = [MHXEKV, HXEKVK, XEKVKZ, EKVKZI]
OACMCV = [
    LJUIKF,
    FJBIAM,
    IAMJMA,
    GQPLSP,
    BLKXSJ,
    IRYXBQ,
    YLJUIK,
    JUIKFW,
    MNZMJI,
    ACCPQI,
    TSIFJB,
    LSPFTS,
    SPBWJY,
    OUSPBW,
    QFYLJU,
    PLSPFT,
    SIFJBI,
    FTSIFJ,
    YKLGQP,
    AMJMAO,
    WJYKLG,
    PBWJYK,
    JBIAMJ,
    AOAWBS,
    BIAMJM,
    BWJYKL,
    PFTSIF,
    QPLSPF,
    KLGQPL,
]
QLNMHX = [
    EJNIBX,
    JNIBXY,
    NIBXYB,
    IBXYBQ,
    BXYBQS,
    XYBQSN,
    YBQSNQ,
    BQSNQL,
    QSNQLN,
    SNQLNM,
    NQLNMH,
]
RJJJVY = [
    TIDUBS,
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
    QRJJJV,
]
SIRYXB = [HFTHEC, BSIRYX, BSIRYX, BSIRYX]
TYEKCW = [SXUJUT, XUJUTY, UJUTYE, JUTYEK, UTYEKC]
UOJRJH = [IVLASS, PHUOJR, HUOJRJ]
VLASSA = [PIPIVL, IPIVLA, PIVLAS, IVLASS]
VOACMC = [
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
]
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
WMNZMJ = [HFTHEC, JWMNZM, JWMNZM, JWMNZM]
WSKWIV = [
    TIDUBS,
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
    SOOQNR,
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
    JHIUSO,
    BVWVUB,
    SOOQNR,
    OOQNRS,
    QNRSJM,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    VWVUBY,
]
ZVOACM = [
    OKPHUO,
    OJRJHI,
    JRJHIU,
    RJHIUS,
    JHIUSO,
    USOOQN,
    SOOQNR,
    OOQNRS,
    QNRSJM,
    NRSJMC,
    SJMCBF,
    JMCBFE,
    HZVOAC,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return ACMCVD

    @property
    def begin(self):
        return CMCVDS

    @property
    def end(self):
        return MCVDSS

    @property
    def all_device_keys(self):
        return ZVOACM

    @property
    def user_demand_keys(self):
        return VOACMC

    @property
    def error_keys(self):
        return OACMCV

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
            OKPHUO: GeckoEnumStructAccessor(
                self.struct, OKPHUO, KPHUOJ, QXPICX, UOJRJH, None, XPICXQ, None
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, KPHUOJ, ICXQIE, UOJRJH, None, XPICXQ, None
            ),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, KPHUOJ, XPICXQ, UOJRJH, None, XPICXQ, None
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, KPHUOJ, QIEFXQ, UOJRJH, None, XPICXQ, None
            ),
            JHIUSO: GeckoEnumStructAccessor(
                self.struct, JHIUSO, HIUSOO, QXPICX, IUSOOQ, None, ICXQIE, None
            ),
            USOOQN: GeckoEnumStructAccessor(
                self.struct, USOOQN, HIUSOO, LRAHEO, GLRAHE, None, ICXQIE, None
            ),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, HIUSOO, ICXQIE, GLRAHE, None, ICXQIE, None
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, HIUSOO, OQNRSJ, GLRAHE, None, ICXQIE, None
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, HIUSOO, XPICXQ, GLRAHE, None, ICXQIE, None
            ),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, HIUSOO, RSJMCB, GLRAHE, None, ICXQIE, None
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, HIUSOO, QIEFXQ, GLRAHE, None, ICXQIE, None
            ),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, MCBFEG, None, EGZUQE, None, None, LASSAK
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, QXPICX, EXLSXU, None, ICXQIE, LASSAK
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, TYEKCW, None, None, LASSAK
            ),
            YEKCWA: GeckoTimeStructAccessor(self.struct, YEKCWA, EKCWAO, LASSAK),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, LASSAK),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, ZUQEXL, ICXQIE, EXLSXU, None, ICXQIE, LASSAK
            ),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, ONPYYL, None, TYEKCW, None, None, LASSAK
            ),
            NPYYLI: GeckoTimeStructAccessor(self.struct, NPYYLI, PYYLIU, LASSAK),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, LASSAK),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, LASSAK),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, LASSAK),
            FEFJTA: GeckoBoolStructAccessor(self.struct, FEFJTA, EFJTAC, QXPICX, None),
            FJTACC: GeckoBoolStructAccessor(self.struct, FJTACC, EFJTAC, ICXQIE, None),
            JTACCP: GeckoBoolStructAccessor(self.struct, JTACCP, EFJTAC, OQNRSJ, None),
            TACCPQ: GeckoBoolStructAccessor(self.struct, TACCPQ, EFJTAC, XPICXQ, None),
            ACCPQI: GeckoBoolStructAccessor(self.struct, ACCPQI, EFJTAC, RSJMCB, None),
            CCPQIP: GeckoBoolStructAccessor(self.struct, CCPQIP, CPQIPO, ICXQIE, None),
            PQIPOU: GeckoBoolStructAccessor(self.struct, PQIPOU, QIPOUY, OQNRSJ, None),
            IPOUYN: GeckoBoolStructAccessor(self.struct, IPOUYN, QIPOUY, RSJMCB, None),
            POUYNQ: GeckoBoolStructAccessor(self.struct, POUYNQ, QIPOUY, QIEFXQ, None),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, UYNQJY, None, JYMOUN, None, None, None
            ),
            YMOUNB: GeckoBoolStructAccessor(self.struct, YMOUNB, MOUNBL, RSJMCB, None),
            OUNBLK: GeckoBoolStructAccessor(self.struct, OUNBLK, MOUNBL, QIEFXQ, None),
            UNBLKX: GeckoWordStructAccessor(self.struct, UNBLKX, NBLKXS, None),
            BLKXSJ: GeckoBoolStructAccessor(self.struct, BLKXSJ, CPQIPO, LRAHEO, None),
            LKXSJW: GeckoTempStructAccessor(self.struct, LKXSJW, KXSJWM, None),
            XSJWMN: GeckoTempStructAccessor(self.struct, XSJWMN, SJWMNZ, None),
            JWMNZM: GeckoEnumStructAccessor(
                self.struct, JWMNZM, HIUSOO, RSJMCB, WMNZMJ, None, XPICXQ, None
            ),
            MNZMJI: GeckoBoolStructAccessor(self.struct, MNZMJI, NZMJIG, ICXQIE, None),
            ZMJIGY: GeckoBoolStructAccessor(self.struct, ZMJIGY, NZMJIG, QIEFXQ, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, JIGYOU, ICXQIE, None),
            IGYOUS: GeckoBoolStructAccessor(self.struct, IGYOUS, GYOUSP, LRAHEO, None),
            YOUSPB: GeckoBoolStructAccessor(
                self.struct, YOUSPB, GYOUSP, ICXQIE, LASSAK
            ),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, USPBWJ, LRAHEO, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, CPQIPO, OQNRSJ, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, QIPOUY, QXPICX, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, QIPOUY, LRAHEO, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, JYKLGQ, ICXQIE, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, JYKLGQ, OQNRSJ, None),
            KLGQPL: GeckoBoolStructAccessor(self.struct, KLGQPL, LGQPLS, OQNRSJ, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, LGQPLS, XPICXQ, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, LGQPLS, RSJMCB, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, LGQPLS, QIEFXQ, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, SPFTSI, OQNRSJ, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, SPFTSI, XPICXQ, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, SPFTSI, RSJMCB, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, SPFTSI, QIEFXQ, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, IFJBIA, ICXQIE, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, IFJBIA, OQNRSJ, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, USPBWJ, OQNRSJ, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, MOUNBL, QXPICX, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, MOUNBL, LRAHEO, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, MJMAOA, QXPICX, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, JIGYOU, QXPICX, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, JYKLGQ, QXPICX, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, JYKLGQ, LRAHEO, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, JYKLGQ, XPICXQ, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, WBSIRY, QXPICX, None),
            BSIRYX: GeckoEnumStructAccessor(
                self.struct, BSIRYX, WBSIRY, LRAHEO, SIRYXB, None, XPICXQ, None
            ),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, WBSIRY, OQNRSJ, None),
            RYXBQF: GeckoWordStructAccessor(self.struct, RYXBQF, YXBQFY, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, QXPICX, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, QXPICX, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FYLJUI, LRAHEO, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, IFJBIA, QXPICX, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, IFJBIA, LRAHEO, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, IFJBIA, XPICXQ, None),
            IKFWRK: GeckoWordStructAccessor(self.struct, IKFWRK, KFWRKI, None),
            FWRKIN: GeckoByteStructAccessor(self.struct, FWRKIN, WRKINE, None),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, None),
            INEJNI: GeckoEnumStructAccessor(
                self.struct, INEJNI, NEJNIB, None, QLNMHX, None, None, None
            ),
            LNMHXE: GeckoEnumStructAccessor(
                self.struct, LNMHXE, NMHXEK, QXPICX, KVKZIL, None, XPICXQ, None
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, NMHXEK, ICXQIE, ILXWAJ, None, ICXQIE, None
            ),
            LXWAJV: GeckoWordStructAccessor(self.struct, LXWAJV, XWAJVD, None),
            WAJVDQ: GeckoByteStructAccessor(self.struct, WAJVDQ, AJVDQL, None),
            JVDQLA: GeckoByteStructAccessor(self.struct, JVDQLA, VDQLAI, None),
            DQLAII: GeckoByteStructAccessor(self.struct, DQLAII, QLAIID, None),
            LAIIDN: GeckoByteStructAccessor(self.struct, LAIIDN, AIIDNI, None),
            IIDNIB: GeckoWordStructAccessor(self.struct, IIDNIB, IDNIBX, None),
            DNIBXT: GeckoByteStructAccessor(self.struct, DNIBXT, NIBXTI, None),
            IBXTIA: GeckoByteStructAccessor(self.struct, IBXTIA, BXTIAC, None),
            XTIACQ: GeckoWordStructAccessor(self.struct, XTIACQ, TIACQF, None),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, ACQFFT, None, FFTTID, None, ICXQIE, LASSAK
            ),
            FTTIDU: GeckoEnumStructAccessor(
                self.struct, FTTIDU, TTIDUB, None, WVUBYG, None, None, LASSAK
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, WVUBYG, None, None, LASSAK
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, YGDSBD, None, WVUBYG, None, None, LASSAK
            ),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, None, WVUBYG, None, None, LASSAK
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, None, WVUBYG, None, None, LASSAK
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, None, RJJJVY, None, None, LASSAK
            ),
            JJJVYF: GeckoByteStructAccessor(self.struct, JJJVYF, JJVYFC, LASSAK),
            JVYFCR: GeckoByteStructAccessor(self.struct, JVYFCR, VYFCRT, LASSAK),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, LASSAK),
            CRTFMN: GeckoByteStructAccessor(self.struct, CRTFMN, RTFMNH, LASSAK),
            TFMNHT: GeckoByteStructAccessor(self.struct, TFMNHT, FMNHTB, LASSAK),
            MNHTBJ: GeckoByteStructAccessor(self.struct, MNHTBJ, NHTBJE, LASSAK),
            HTBJEU: GeckoEnumStructAccessor(
                self.struct, HTBJEU, TBJEUT, None, WVUBYG, None, None, LASSAK
            ),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, JEUTOP, None, WVUBYG, None, None, LASSAK
            ),
            EUTOPH: GeckoEnumStructAccessor(
                self.struct, EUTOPH, UTOPHU, None, WVUBYG, None, None, LASSAK
            ),
            TOPHUG: GeckoEnumStructAccessor(
                self.struct, TOPHUG, OPHUGT, None, WVUBYG, None, None, LASSAK
            ),
            PHUGTY: GeckoEnumStructAccessor(
                self.struct, PHUGTY, HUGTYI, None, WVUBYG, None, None, LASSAK
            ),
            UGTYIY: GeckoEnumStructAccessor(
                self.struct, UGTYIY, GTYIYW, None, WVUBYG, None, None, LASSAK
            ),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, YIYWSK, None, WVUBYG, None, None, LASSAK
            ),
            IYWSKW: GeckoEnumStructAccessor(
                self.struct, IYWSKW, YWSKWI, None, WSKWIV, None, None, LASSAK
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, WSKWIV, None, None, LASSAK
            ),
            WIVDNQ: GeckoByteStructAccessor(self.struct, WIVDNQ, IVDNQG, LASSAK),
            VDNQGV: GeckoByteStructAccessor(self.struct, VDNQGV, DNQGVU, LASSAK),
            NQGVUN: GeckoByteStructAccessor(self.struct, NQGVUN, QGVUNX, LASSAK),
            GVUNXN: GeckoByteStructAccessor(self.struct, GVUNXN, VUNXNK, LASSAK),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, LASSAK),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, LASSAK),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, LASSAK),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, LASSAK),
            IJUGSE: GeckoByteStructAccessor(self.struct, IJUGSE, JUGSEL, LASSAK),
        }

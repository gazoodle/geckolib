#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYJ v54'
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
ACQFFT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 53])
AHEOCT = 308
AJVDQL = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = 466
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
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 49, 49])
AWBSIR = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
BDJQRJ = "".join(chr(c) for c in [75, 56, 53])
BFEGZU = 310
BHZVOA = 477
BIAMJM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
BJEUTO = "".join(chr(c) for c in [80, 49, 72])
BLKXSJ = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
BMJVHF = 256
BQFYLJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
BQNRXC = 448
BQSNQL = "".join(chr(c) for c in [105, 110, 88, 77])
BSIRYX = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
BVWVUB = 301
BWJYKL = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 56])
BXYBQS = "".join(chr(c) for c in [77, 73, 65])
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
CGETIX = "".join(chr(c) for c in [67, 70, 71, 50, 50])
CHWDAF = "".join(chr(c) for c in [67, 70, 71, 51])
CMCVDS = "".join(chr(c) for c in [76, 73])
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
CQFFTT = 293
CRTFMN = 358
CTHBSK = 303
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = 264
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = 452
DGKEAK = 464
DJQRJJ = "".join(chr(c) for c in [75, 56])
DNIBXT = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
DNQGVU = 326
DQLAII = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
DSBDJQ = "".join(chr(c) for c in [75, 50, 48, 48])
DSSRUR = 256
DUBSSU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 49, 50])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 56])
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 272
EFXQGL = 258
EGZUQE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
EJNIBX = 289
EKVKZI = "".join(chr(c) for c in [49, 54, 75])
ELHBQN = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 50, 49])
EOCTHB = 307
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 50, 51])
EUTOPH = "".join(chr(c) for c in [80, 50, 72])
EXLSXU = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
FCRTFM = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
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
FFTTID = 294
FIKJPU = 453
FJBIAM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
FJTACC = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FMNHTB = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
FTHECV = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
FTSIFJ = 350
FTTIDU = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
FWRKIN = 285
FYLJUI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
FZDGKE = 463
GDSBDJ = 357
GETIXQ = 470
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 55])
GQPLSP = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
GSELHB = 325
GTYIYW = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
GYOUSP = 280
GZUQEX = "".join(chr(c) for c in [70, 85, 76, 76])
HBQNRX = "".join(chr(c) for c in [67, 70, 71, 48])
HBSKSO = 362
HBVWVU = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
HBXIBH = 475
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = "".join(chr(c) for c in [80, 52])
HTBJEU = 320
HUGTYI = "".join(chr(c) for c in [80, 52, 76])
HUOJRJ = 261
HWDAFI = 451
HXEKVK = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 51, 48])
IACQFF = 291
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
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 57])
IBXTIA = "".join(chr(c) for c in [51, 48, 65])
IBXYBQ = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
ICXQIE = 2
IDNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
IDUBSS = 296
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
IGYOUS = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 55])
IIDNIB = "".join(
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
IJUGSE = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
IKFWRK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 54])
ILXWAJ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
INEJNI = 288
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
IRYXBQ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
IUSOOQ = "".join(chr(c) for c in [80, 53])
IUXFEF = 270
IVDNQG = 324
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 50, 52])
IYWSKW = 321
JBIAMJ = 351
JEUTOP = "".join(chr(c) for c in [80, 49, 76])
JHIUSO = "".join(chr(c) for c in [80, 51])
JIGYOU = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
JJJVYF = "".join(chr(c) for c in [75, 49, 48, 48])
JJVYFC = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
JMAOAW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
JMCBFE = 5
JNIBXY = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 55])
JQRJJJ = "".join(chr(c) for c in [75, 52])
JTACCP = 273
JUGSEL = 333
JUIKFW = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
JUTYEK = "".join(chr(c) for c in [83, 84, 79, 80])
JVDQLA = "".join(chr(c) for c in [80, 50, 50])
JVHFTH = 319
JVYFCR = "".join(chr(c) for c in [75, 51, 48, 48])
JWMNZM = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
JYKLGQ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
JYMOUN = "".join(chr(c) for c in [77, 69, 68])
JZTATD = 457
KCWAON = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
KEAKST = 465
KFWRKI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
KINEJN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
KJPUNR = 454
KLGQPL = 283
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
KPHUOJ = 306
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 57])
KVKZIL = "".join(chr(c) for c in [51, 50, 75])
KWIVDN = 323
KXSJWM = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
KZILXW = "".join(chr(c) for c in [54, 52, 75])
LAIIDN = "".join(chr(c) for c in [51, 79, 80])
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
LHBQNR = 332
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
LJUIKF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
LKXSJW = 355
LNMHXE = "".join(chr(c) for c in [75, 56, 48, 48])
LOIJUG = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
LRAHEO = 1
LSPFTS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
LXWAJV = "".join(chr(c) for c in [85, 76])
MAOAWB = 354
MCBFEG = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
MCGETI = 469
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 49, 53])
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
MLOIJU = 330
MNHTBJ = 361
MNZMJI = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
NBLKXS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
NEJNIB = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
NHTBJE = "".join(chr(c) for c in [83, 79, 117, 116, 49])
NIBXTI = "".join(chr(c) for c in [50, 53, 65])
NIBXYB = "".join(chr(c) for c in [105, 110, 88, 69])
NKMLOI = 329
NMHXEK = "".join(chr(c) for c in [105, 110, 89, 74])
NPYYLI = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
NQGVUN = "".join(chr(c) for c in [72, 84, 82])
NQJYMO = 313
NQLNMH = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
NQTMFZ = 461
NRJZTA = 456
NRSJMC = 3
NRXCHW = 449
NXNKML = 328
OACMCV = 479
OAWBSI = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
OCTHBS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
OIHBXI = 474
OIJUGS = 331
OJRJHI = "".join(chr(c) for c in [76, 79, 87])
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ONPYYL = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
OOQNRS = "".join(chr(c) for c in [66, 76])
OPHUGT = "".join(chr(c) for c in [80, 51, 76])
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
PHUGTY = "".join(chr(c) for c in [80, 52, 72])
PHUOJR = "".join(chr(c) for c in [80, 49])
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
POUYNQ = 282
PQIPOU = "".join(chr(c) for c in [67, 80, 79, 84])
PUNRJZ = 455
PYYLIU = 267
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 262
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
QFYLJU = 314
QGLRAH = "".join(chr(c) for c in [79, 78])
QIEFXQ = 6
QIPOUY = 274
QJYMOU = "".join(chr(c) for c in [78, 79])
QLAIID = "".join(chr(c) for c in [53, 79, 80])
QLNMHX = "".join(chr(c) for c in [105, 110, 89, 84])
QNRSJM = "".join(chr(c) for c in [79, 51])
QNRXCH = "".join(chr(c) for c in [67, 70, 71, 49])
QPLSPF = 284
QRJJJV = "".join(chr(c) for c in [75, 53])
QSNQLN = "".join(chr(c) for c in [75, 54, 48, 48])
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 49, 52])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 50, 53])
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RJHIUS = "".join(chr(c) for c in [80, 50])
RJJJVY = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 57])
RKINEJ = 287
RSJMCB = "".join(chr(c) for c in [76, 49, 50, 48])
RTFMNH = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
RXCHWD = "".join(chr(c) for c in [67, 70, 71, 50])
SAKQXP = "".join(chr(c) for c in [76, 79])
SBDJQR = "".join(chr(c) for c in [75, 52, 48, 48])
SEMCGE = 468
SIFJBI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
SIRYXB = 309
SJMCBF = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = 275
SKSOKP = 304
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 52])
SNQLNM = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
SOKPHU = 305
SPBWJY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
SPFTSI = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
SSAKQX = 259
SSRURA = 479
SSUHBV = 299
STSEMC = 467
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
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
TATDZX = 458
TBJEUT = "".join(chr(c) for c in [78, 65])
TDZXNQ = 459
TFMNHT = 360
THBSKS = "".join(chr(c) for c in [85, 100, 80, 49, 76, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
TIDUBS = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
TIXQVX = 471
TMFZDG = 462
TOPHUG = "".join(chr(c) for c in [80, 51, 72])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 50, 48])
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
TTIDUB = 295
TYEKCW = "".join(chr(c) for c in [78, 69, 87])
UBSSUH = 297
UBYGDS = "".join(chr(c) for c in [70, 117, 108, 108])
UGSELH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
UGTYIY = "".join(chr(c) for c in [66, 76, 79])
UHBVWV = 300
UIKFWR = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
UJUTYE = "".join(chr(c) for c in [73, 68, 76, 69])
UNBLKX = 353
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 56])
UNXNKM = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
UOJRJH = "".join(chr(c) for c in [72, 73, 71, 72])
UQEXLS = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
USOOQN = 260
USPBWJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
UTOPHU = "".join(chr(c) for c in [80, 50, 76])
UTYEKC = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UXFEFJ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
UYNQJY = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
VDSSRU = 54
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VKZILX = "".join(chr(c) for c in [52, 56, 75])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 51, 49])
VUBYGD = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
VUNXNK = 327
VWVUBY = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
VXOIHB = 473
VYFCRT = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
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
WDAFIK = "".join(chr(c) for c in [67, 70, 71, 52])
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 53])
WJYKLG = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
WMNZMJ = 277
WRKINE = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
WSKWIV = 322
WVUBYG = 316
XBQFYL = 311
XCHWDA = 450
XEKVKZ = 290
XFEFJT = 271
XIBHZV = 476
XLSXUJ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
XNKMLO = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 49, 51])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 50, 54])
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = 472
XSJWMN = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
XTIACQ = 7
XUJUTY = 263
XWAJVD = "".join(chr(c) for c in [67, 69])
XYBQSN = "".join(chr(c) for c in [68, 74, 83, 52])
YBQSNQ = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
YEKCWA = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
YGDSBD = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
YIYWSK = "".join(chr(c) for c in [83, 79, 117, 116, 50])
YKLGQP = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
YLIUXF = 268
YLJUIK = 315
YMOUNB = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
YNQJYM = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
YOUSPB = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
YPIPIV = 257
YWSKWI = "".join(chr(c) for c in [83, 79, 117, 116, 51])
YXBQFY = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
YYLIUX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
YYPIPI = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49, 54])
ZMJIGY = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 49, 48])
ZVOACM = 478
ZXNQTM = 460
ACMCVD = []
AIIDNI = [QLAIID, LAIIDN]
BXTIAC = [NIBXTI, IBXTIA]
BYGDSB = [VUBYGD, UBYGDS]
CVDSSR = [
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
EKCWAO = [UJUTYE, JUTYEK, UTYEKC, TYEKCW, YEKCWA]
FXQGLR = [IVLASS, AKQXPI]
GLRAHE = [IVLASS, QGLRAH]
JRJHIU = [IVLASS, UOJRJH, OJRJHI]
KQXPIC = [IVLASS, SAKQXP, AKQXPI]
LSXUJU = [EXLSXU, XLSXUJ]
MCVDSS = [
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
    CMCVDS,
]
MHXEKV = [
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
    QLNMHX,
    LNMHXE,
    NMHXEK,
]
MOUNBL = [QJYMOU, SAKQXP, JYMOUN, AKQXPI, YMOUNB]
NZMJIG = [HFTHEC, MNZMJI, MNZMJI, MNZMJI]
QGVUNX = [
    TBJEUT,
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
    NQGVUN,
]
RYXBQF = [HFTHEC, IRYXBQ, IRYXBQ, IRYXBQ]
SELHBQ = [
    TBJEUT,
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
TYIYWS = [
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    TOPHUG,
    OPHUGT,
    PHUGTY,
    HUGTYI,
    IUSOOQ,
    UGTYIY,
    OQNRSJ,
    QNRSJM,
    RSJMCB,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    GTYIYW,
]
VDQLAI = [OOQNRS, JVDQLA]
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
WAJVDQ = [LXWAJV, XWAJVD]
YFCRTF = [
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    LNMHXE,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    JJVYFC,
    JVYFCR,
    VYFCRT,
]
ZILXWA = [EKVKZI, KVKZIL, VKZILX, KZILXW]
ZUQEXL = [FEGZUQ, EGZUQE, GZUQEX]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return VDSSRU

    @property
    def begin(self):
        return DSSRUR

    @property
    def end(self):
        return SSRURA

    @property
    def all_device_keys(self):
        return MCVDSS

    @property
    def user_demand_keys(self):
        return CVDSSR

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
            YXBQFY: GeckoWordStructAccessor(self.struct, YXBQFY, XBQFYL, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, QFYLJU, QXPICX, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, YLJUIK, QXPICX, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, YLJUIK, LRAHEO, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, JBIAMJ, QXPICX, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, JBIAMJ, LRAHEO, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, JBIAMJ, XPICXQ, None),
            KFWRKI: GeckoWordStructAccessor(self.struct, KFWRKI, FWRKIN, None),
            WRKINE: GeckoByteStructAccessor(self.struct, WRKINE, RKINEJ, None),
            KINEJN: GeckoByteStructAccessor(self.struct, KINEJN, INEJNI, None),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, EJNIBX, None, MHXEKV, None, None, None
            ),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, XEKVKZ, QXPICX, ZILXWA, None, XPICXQ, None
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, XEKVKZ, ICXQIE, WAJVDQ, None, ICXQIE, None
            ),
            AJVDQL: GeckoEnumStructAccessor(
                self.struct, AJVDQL, XEKVKZ, NRSJMC, VDQLAI, None, ICXQIE, None
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, XEKVKZ, XPICXQ, AIIDNI, None, ICXQIE, None
            ),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, XEKVKZ, JMCBFE, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, XEKVKZ, QIEFXQ, None),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, XEKVKZ, XTIACQ, BXTIAC, None, ICXQIE, None
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
                self.struct, VWVUBY, WVUBYG, None, BYGDSB, None, ICXQIE, LASSAK
            ),
            YGDSBD: GeckoEnumStructAccessor(
                self.struct, YGDSBD, GDSBDJ, None, YFCRTF, None, None, None
            ),
            FCRTFM: GeckoWordStructAccessor(self.struct, FCRTFM, CRTFMN, None),
            RTFMNH: GeckoByteStructAccessor(self.struct, RTFMNH, TFMNHT, None),
            FMNHTB: GeckoByteStructAccessor(self.struct, FMNHTB, MNHTBJ, None),
            NHTBJE: GeckoEnumStructAccessor(
                self.struct, NHTBJE, HTBJEU, None, TYIYWS, None, None, LASSAK
            ),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, TYIYWS, None, None, LASSAK
            ),
            YWSKWI: GeckoEnumStructAccessor(
                self.struct, YWSKWI, WSKWIV, None, TYIYWS, None, None, LASSAK
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, TYIYWS, None, None, LASSAK
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, TYIYWS, None, None, LASSAK
            ),
            VDNQGV: GeckoEnumStructAccessor(
                self.struct, VDNQGV, DNQGVU, None, QGVUNX, None, None, LASSAK
            ),
            GVUNXN: GeckoByteStructAccessor(self.struct, GVUNXN, VUNXNK, LASSAK),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, LASSAK),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, LASSAK),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, LASSAK),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, LASSAK),
            IJUGSE: GeckoByteStructAccessor(self.struct, IJUGSE, JUGSEL, LASSAK),
            UGSELH: GeckoEnumStructAccessor(
                self.struct, UGSELH, GSELHB, None, SELHBQ, None, None, LASSAK
            ),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, LASSAK),
        }

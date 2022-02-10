#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE-64K v56'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 51, 48])
ACQFFT = 7
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 51])
AHEOCT = 1
AIIDNI = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
AJVDQL = "".join(chr(c) for c in [85, 76])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = 464
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
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 57])
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
BDJQRJ = 357
BFEGZU = 310
BHZVOA = 475
BIAMJM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
BJEUTO = 361
BLKXSJ = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
BMJVHF = 256
BQFYLJ = 309
BQSNQL = "".join(chr(c) for c in [105, 110, 88, 69])
BSIRYX = 354
BSKSOK = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
BSSUHB = 296
BVWVUB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
BWJYKL = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 54])
BXTIAC = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
BXYBQS = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
BYGDSB = 316
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
CGETIX = "".join(chr(c) for c in [67, 70, 71, 50, 48])
CHWDAF = "".join(chr(c) for c in [67, 70, 71, 49])
CMCVDS = 478
CPQIPO = 272
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
CRTFMN = "".join(chr(c) for c in [75, 51, 48, 48])
CTHBSK = 307
CVDSSR = 479
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(chr(c) for c in [83, 84, 79, 80])
CXQIEF = 4
DAFIKJ = 450
DGKEAK = 462
DJQRJJ = "".join(chr(c) for c in [75, 50, 48, 48])
DNQGVU = 323
DQLAII = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
DSSRUR = "".join(chr(c) for c in [76, 73])
DUBSSU = 295
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 49, 48])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 54])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = 268
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
EJNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
EKCWAO = 263
ELHBQN = 333
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 57])
EOCTHB = 308
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 50, 49])
EUTOPH = 320
EXLSXU = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
FCRTFM = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
FEFJTA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
FEGZUQ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
FFTTID = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
FIKJPU = 451
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
FMNHTB = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
FTHECV = 319
FTSIFJ = 284
FTTIDU = 293
FWRKIN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FZDGKE = 461
GDSBDJ = "".join(chr(c) for c in [70, 117, 108, 108])
GETIXQ = 468
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 53])
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GQPLSP = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
GSELHB = 331
GTYIYW = "".join(chr(c) for c in [80, 51, 76])
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
GZUQEX = "".join(chr(c) for c in [70, 85, 76, 76])
HBQNRX = 325
HBSKSO = 303
HBVWVU = 299
HBXIBH = 473
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [80, 52])
HTBJEU = 360
HUGTYI = "".join(chr(c) for c in [80, 50, 76])
HUOJRJ = 261
HWDAFI = 449
HXEKVK = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 56])
IAMJMA = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 55])
IBXTIA = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
IBXYBQ = 288
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [51, 79, 80])
IDUBSS = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
IGYOUS = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 53])
IIDNIB = "".join(chr(c) for c in [53, 79, 80])
IJUGSE = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
IKFWRK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 52])
ILXWAJ = "".join(chr(c) for c in [52, 56, 75])
INEJNI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(chr(c) for c in [80, 117, 114, 103, 101])
IRYXBQ = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
IUSOOQ = "".join(chr(c) for c in [80, 53])
IUXFEF = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
IVDNQG = 322
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 50, 50])
IYWSKW = "".join(chr(c) for c in [66, 76, 79])
JBIAMJ = 350
JEUTOP = "".join(chr(c) for c in [83, 79, 117, 116, 49])
JHIUSO = "".join(chr(c) for c in [80, 51])
JIGYOU = 277
JJJVYF = "".join(chr(c) for c in [75, 52])
JJVYFC = "".join(chr(c) for c in [75, 53])
JMAOAW = 351
JMCBFE = 5
JNIBXY = 287
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 53])
JQRJJJ = "".join(chr(c) for c in [75, 52, 48, 48])
JTACCP = 270
JUGSEL = 330
JUIKFW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JUTYEK = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JVDQLA = "".join(chr(c) for c in [67, 69])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
JWMNZM = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
JYKLGQ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
JYMOUN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
JZTATD = 455
KCWAON = "".join(chr(c) for c in [73, 68, 76, 69])
KEAKST = 463
KFWRKI = 315
KINEJN = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
KJPUNR = 452
KLGQPL = 352
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
KPHUOJ = 306
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 55])
KVKZIL = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
KWIVDN = 321
KXSJWM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
KZILXW = "".join(chr(c) for c in [49, 54, 75])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
LHBQNR = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
LIUXFE = 266
LJUIKF = 311
LNMHXE = "".join(chr(c) for c in [105, 110, 88, 77])
LOIJUG = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 283
LSXUJU = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
LXWAJV = "".join(chr(c) for c in [54, 52, 75])
MAOAWB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
MCBFEG = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
MCGETI = 467
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 51, 49])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 49, 51])
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
MLOIJU = 328
MNHTBJ = 358
MNZMJI = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
MOUNBL = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
NBLKXS = "".join(chr(c) for c in [77, 69, 68])
NEJNIB = 285
NHTBJE = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
NIBXTI = "".join(
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
NIBXYB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
NKMLOI = 327
NMHXEK = "".join(chr(c) for c in [75, 54, 48, 48])
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 53])
NQJYMO = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
NQLNMH = "".join(chr(c) for c in [68, 74, 83, 52])
NQTMFZ = 459
NRJZTA = 454
NRSJMC = 3
NRXCHW = 332
NZMJIG = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
OACMCV = 477
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
OIHBXI = 472
OIJUGS = 329
OJRJHI = "".join(chr(c) for c in [76, 79, 87])
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ONPYYL = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
OOQNRS = "".join(chr(c) for c in [66, 76])
OPHUGT = "".join(chr(c) for c in [80, 49, 76])
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
PHUGTY = "".join(chr(c) for c in [80, 50, 72])
PHUOJR = "".join(chr(c) for c in [80, 49])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
POUYNQ = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
PQIPOU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
PUNRJZ = 453
PYYLIU = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 364
QFFTTI = 291
QFYLJU = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
QGVUNX = 324
QIEFXQ = 2
QIPOUY = 273
QJYMOU = 282
QLAIID = "".join(chr(c) for c in [80, 50, 50])
QLNMHX = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
QNRSJM = "".join(chr(c) for c in [79, 51])
QNRXCH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
QPLSPF = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
QRJJJV = "".join(chr(c) for c in [75, 56, 53])
QSNQLN = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 49, 50])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 50, 51])
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 479
RJHIUS = "".join(chr(c) for c in [80, 50])
RJJJVY = "".join(chr(c) for c in [75, 56])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 55])
RKINEJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
RSJMCB = "".join(chr(c) for c in [76, 49, 50, 48])
RTFMNH = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
RURAZM = 56
RXCHWD = "".join(chr(c) for c in [67, 70, 71, 48])
RYXBQF = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
SELHBQ = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
SEMCGE = 466
SIFJBI = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
SIRYXB = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
SJMCBF = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
SKSOKP = 304
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 50])
SNQLNM = "".join(chr(c) for c in [77, 73, 65])
SOKPHU = 305
SPBWJY = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
SPFTSI = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
SSUHBV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
STSEMC = 465
SUHBVW = 297
SXUJUT = 367
TACCPQ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
TATDZX = 456
TBJEUT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
TDZXNQ = 457
THBSKS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [51, 48, 65])
TIDUBS = 294
TIXQVX = 469
TMFZDG = 460
TOPHUG = "".join(chr(c) for c in [80, 49, 72])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 56])
TSIFJB = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
TTIDUB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TYIYWS = "".join(chr(c) for c in [80, 52, 72])
UBSSUH = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
UBYGDS = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
UGSELH = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
UGTYIY = "".join(chr(c) for c in [80, 51, 72])
UHBVWV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
UIKFWR = 314
UJUTYE = 262
UNBLKX = "".join(chr(c) for c in [78, 79])
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 54])
UNXNKM = "".join(chr(c) for c in [72, 84, 82])
UOJRJH = "".join(chr(c) for c in [72, 73, 71, 72])
UQEXLS = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
URAZMK = 256
USOOQN = 260
USPBWJ = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
UTOPHU = "".join(chr(c) for c in [78, 65])
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
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 52])
VHFTHE = 6
VKZILX = 290
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 57])
VUBYGD = 301
VUNXNK = 326
VWVUBY = 300
VXOIHB = 471
VYFCRT = "".join(chr(c) for c in [75, 49, 48, 48])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
WAONPY = "".join(chr(c) for c in [83, 84, 65, 82, 84])
WBSIRY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
WDAFIK = "".join(chr(c) for c in [67, 70, 71, 50])
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 51])
WJYKLG = 281
WMNZMJ = 355
WRKINE = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
WVUBYG = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
XBQFYL = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
XCHWDA = 448
XEKVKZ = "".join(chr(c) for c in [105, 110, 89, 84])
XFEFJT = 267
XIBHZV = 474
XLSXUJ = 365
XNKMLO = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 49, 49])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 50, 52])
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = 470
XSJWMN = 353
XTIACQ = "".join(chr(c) for c in [50, 53, 65])
XUJUTY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
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
YFCRTF = "".join(chr(c) for c in [75, 56, 48, 48])
YGDSBD = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
YIYWSK = "".join(chr(c) for c in [80, 52, 76])
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
YWSKWI = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
YXBQFY = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
YYLIUX = 264
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49, 52])
ZILXWA = "".join(chr(c) for c in [51, 50, 75])
ZMJIGY = 275
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 56])
ZVOACM = 476
ZXNQTM = 458
BQNRXC = [
    UTOPHU,
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
DNIBXT = [IIDNIB, IDNIBX]
DSBDJQ = [YGDSBD, GDSBDJ]
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
FYLJUI = [HECVYY, QFYLJU, QFYLJU, QFYLJU]
GYOUSP = [HECVYY, IGYOUS, IGYOUS, IGYOUS]
IACQFF = [XTIACQ, TIACQF]
JRJHIU = [ASSAKQ, UOJRJH, OJRJHI]
LAIIDN = [OOQNRS, QLAIID]
LKXSJW = [UNBLKX, QXPICX, NBLKXS, XPICXQ, BLKXSJ]
NPYYLI = [KCWAON, CWAONP, WAONPY, AONPYY, ONPYYL]
NXNKML = [
    UTOPHU,
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
    UNXNKM,
]
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
SOOQNR = [ASSAKQ, UOJRJH]
SRURAZ = [
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
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
SSRURA = [
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
    DSSRUR,
]
TFMNHT = [
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    YFCRTF,
    HECVYY,
    HECVYY,
    HECVYY,
    FCRTFM,
    CRTFMN,
    RTFMNH,
]
TYEKCW = [JUTYEK, UTYEKC]
VDQLAI = [AJVDQL, JVDQLA]
VDSSRU = []
WSKWIV = [
    UTOPHU,
    TOPHUG,
    OPHUGT,
    PHUGTY,
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IUSOOQ,
    IYWSKW,
    OQNRSJ,
    QNRSJM,
    RSJMCB,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    YWSKWI,
]
XWAJVD = [KZILXW, ZILXWA, ILXWAJ, LXWAJV]
ZUQEXL = [FEGZUQ, EGZUQE, GZUQEX]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return RURAZM

    @property
    def begin(self):
        return URAZMK

    @property
    def end(self):
        return RAZMKQ

    @property
    def all_device_keys(self):
        return SSRURA

    @property
    def user_demand_keys(self):
        return SRURAZ

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
                self.struct, BXYBQS, XYBQSN, None, EKVKZI, None, None, None
            ),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, VKZILX, ICXQIE, XWAJVD, None, CXQIEF, None
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, VKZILX, QIEFXQ, VDQLAI, None, QIEFXQ, None
            ),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, VKZILX, NRSJMC, LAIIDN, None, QIEFXQ, None
            ),
            AIIDNI: GeckoEnumStructAccessor(
                self.struct, AIIDNI, VKZILX, CXQIEF, DNIBXT, None, QIEFXQ, None
            ),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, VKZILX, JMCBFE, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, VKZILX, VHFTHE, None),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, VKZILX, ACQFFT, IACQFF, None, QIEFXQ, None
            ),
            CQFFTT: GeckoWordStructAccessor(self.struct, CQFFTT, QFFTTI, None),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, None),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, None),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, None),
            SSUHBV: GeckoWordStructAccessor(self.struct, SSUHBV, SUHBVW, None),
            UHBVWV: GeckoByteStructAccessor(self.struct, UHBVWV, HBVWVU, None),
            BVWVUB: GeckoByteStructAccessor(self.struct, BVWVUB, VWVUBY, None),
            WVUBYG: GeckoWordStructAccessor(self.struct, WVUBYG, VUBYGD, None),
            UBYGDS: GeckoEnumStructAccessor(
                self.struct, UBYGDS, BYGDSB, None, DSBDJQ, None, QIEFXQ, SAKQXP
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, None, TFMNHT, None, None, None
            ),
            FMNHTB: GeckoWordStructAccessor(self.struct, FMNHTB, MNHTBJ, None),
            NHTBJE: GeckoByteStructAccessor(self.struct, NHTBJE, HTBJEU, None),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, None),
            JEUTOP: GeckoEnumStructAccessor(
                self.struct, JEUTOP, EUTOPH, None, WSKWIV, None, None, SAKQXP
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, WSKWIV, None, None, SAKQXP
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, WSKWIV, None, None, SAKQXP
            ),
            VDNQGV: GeckoEnumStructAccessor(
                self.struct, VDNQGV, DNQGVU, None, WSKWIV, None, None, SAKQXP
            ),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, QGVUNX, None, WSKWIV, None, None, SAKQXP
            ),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, NXNKML, None, None, SAKQXP
            ),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, SAKQXP),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, SAKQXP),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, SAKQXP),
            IJUGSE: GeckoByteStructAccessor(self.struct, IJUGSE, JUGSEL, SAKQXP),
            UGSELH: GeckoByteStructAccessor(self.struct, UGSELH, GSELHB, SAKQXP),
            SELHBQ: GeckoByteStructAccessor(self.struct, SELHBQ, ELHBQN, SAKQXP),
            LHBQNR: GeckoEnumStructAccessor(
                self.struct, LHBQNR, HBQNRX, None, BQNRXC, None, None, SAKQXP
            ),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, SAKQXP),
        }

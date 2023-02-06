#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYJ v58'
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
ACCPQI = 268
ACMCVD = 473
ACQFFT = "".join(chr(c) for c in [53, 79, 80])
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [54, 52, 75])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 49, 50])
AMJMAO = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
AOAWBS = 350
AONPYY = 263
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = 452
AWBSIR = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
AZMKQT = "".join(chr(c) for c in [67, 70, 71, 51, 49])
BDJQRJ = 300
BFEGZU = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 50, 51])
BIAMJM = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
BJEUTO = "".join(chr(c) for c in [75, 51, 48, 48])
BLKXSJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
BMJVHF = 256
BQFYLJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
BQNRXC = 329
BQSNQL = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
BSIRYX = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
BVWVUB = 294
BWJYKL = 279
BXIBHZ = 469
BXTIAC = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
BXYBQS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
BYGDSB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
CBFEGZ = "".join(chr(c) for c in [76, 49, 50, 48])
CCPQIP = "".join(
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
CGETIX = 463
CHWDAF = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 50, 54])
CPQIPO = 270
CQBMJV = 317
CQFFTT = "".join(chr(c) for c in [51, 79, 80])
CRTFMN = "".join(chr(c) for c in [75, 52, 48, 48])
CTHBSK = 307
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 50, 55])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CXQIEF = 4
DAFIKJ = 325
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 49, 48])
DJQRJJ = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
DNIBXT = "".join(chr(c) for c in [85, 76])
DNQGVU = "".join(chr(c) for c in [66, 76, 79])
DQLAII = "".join(chr(c) for c in [49, 54, 75])
DSBDJQ = 299
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 50, 56])
DZXNQT = 453
EAKSTS = 459
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
EJNIBX = 315
EKCWAO = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
EKVKZI = "".join(chr(c) for c in [68, 74, 83, 52])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
EMCGET = 462
EOCTHB = 308
ETIXQV = 464
EXLSXU = "".join(chr(c) for c in [70, 85, 76, 76])
FCRTFM = "".join(chr(c) for c in [75, 50, 48, 48])
FEFJTA = 266
FEGZUQ = 5
FFTTID = "".join(
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
FIKJPU = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
FJBIAM = 283
FJTACC = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
FMNHTB = "".join(chr(c) for c in [75, 52])
FTHECV = 319
FTSIFJ = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 57])
GDSBDJ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 49, 54])
GKEAKS = 458
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GQPLSP = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [83, 79, 117, 116, 49])
GYOUSP = 275
GZUQEX = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
HBSKSO = 370
HBVWVU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 50, 49])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [76, 79, 87])
HTBJEU = "".join(chr(c) for c in [75, 49, 48, 48])
HTZBBE = 256
HUGTYI = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
HUOJRJ = 306
HWDAFI = 333
HXEKVK = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
HZVOAC = 471
IACQFF = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
IAMJMA = 284
IBHZVO = 470
IBXYBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
IDUBSS = "".join(chr(c) for c in [51, 48, 65])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
IGYOUS = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
IHBXIB = 468
IJUGSE = 326
IKFWRK = 309
IKJPUN = 332
ILXWAJ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
INEJNI = 314
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
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
IRYXBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
IUXFEF = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
IVDNQG = "".join(chr(c) for c in [80, 52, 72])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = 465
IYWSKW = "".join(chr(c) for c in [80, 49, 72])
JBIAMJ = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
JEUTOP = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
JHIUSO = "".join(chr(c) for c in [72, 73, 71, 72])
JIGYOU = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
JJJVYF = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
JJVYFC = "".join(chr(c) for c in [70, 117, 108, 108])
JMAOAW = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
JMCBFE = "".join(chr(c) for c in [79, 51])
JNIBXY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
JPUNRJ = 448
JQRJJJ = 301
JRJHIU = "".join(chr(c) for c in [80, 49])
JTACCP = 267
JUGSEL = "".join(chr(c) for c in [72, 84, 82])
JUIKFW = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
JUTYEK = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
JVDQLA = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
JVHFTH = 274
JYKLGQ = 280
JYMOUN = "".join(
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
JZTATD = "".join(chr(c) for c in [67, 70, 71, 51])
KCWAON = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
KEAKST = "".join(chr(c) for c in [67, 70, 71, 49, 49])
KFWRKI = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
KHTZBB = 58
KINEJN = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
KJPUNR = "".join(chr(c) for c in [67, 70, 71, 48])
KLGQPL = 281
KMLOIJ = 323
KPHUOJ = 305
KQTDKH = "".join(chr(c) for c in [76, 73])
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
KSTSEM = 460
KVKZIL = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
KWIVDN = "".join(chr(c) for c in [80, 51, 72])
KXSJWM = "".join(chr(c) for c in [78, 79])
KZILXW = "".join(chr(c) for c in [75, 54, 48, 48])
LAIIDN = "".join(chr(c) for c in [52, 56, 75])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
LHBQNR = 328
LJUIKF = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
LKXSJW = 313
LNMHXE = 289
LOIJUG = 324
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = 377
LSXUJU = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
LXWAJV = "".join(chr(c) for c in [105, 110, 89, 84])
MAOAWB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
MCBFEG = 3
MCGETI = "".join(chr(c) for c in [67, 70, 71, 49, 53])
MCVDSS = 474
MFZDGK = 456
MHXEKV = "".join(chr(c) for c in [105, 110, 88, 69])
MJIGYO = 355
MJMAOA = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 53])
MNHTBJ = "".join(chr(c) for c in [75, 53])
MNZMJI = 353
MOUNBL = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
NBLKXS = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
NEJNIB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
NHTBJE = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
NIBXTI = "".join(chr(c) for c in [67, 69])
NIBXYB = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
NKMLOI = "".join(chr(c) for c in [83, 79, 117, 116, 52])
NMHXEK = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
NPYYLI = "".join(chr(c) for c in [83, 84, 79, 80])
NQGVUN = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
NQJYMO = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
NQLNMH = 288
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 55])
NRJZTA = "".join(chr(c) for c in [67, 70, 71, 50])
NRXCHW = 330
NXNKML = "".join(chr(c) for c in [83, 79, 117, 116, 51])
NZMJIG = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
OACMCV = "".join(chr(c) for c in [67, 70, 71, 50, 53])
OAWBSI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 50, 48])
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
OJRJHI = 369
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
ONPYYL = "".join(chr(c) for c in [73, 68, 76, 69])
OOQNRS = "".join(chr(c) for c in [80, 52])
OPHUGT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
OQNRSJ = "".join(chr(c) for c in [80, 53])
OUNBLK = 282
OUSPBW = 277
OUYNQJ = "".join(chr(c) for c in [67, 108, 101, 97, 110])
PBWJYK = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
PFTSIF = 383
PHUGTY = 360
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
POUYNQ = 272
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
PUNRJZ = "".join(chr(c) for c in [67, 70, 71, 49])
PYYLIU = "".join(chr(c) for c in [83, 84, 65, 82, 84])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
QFYLJU = 354
QGVUNX = "".join(chr(c) for c in [65, 85, 88])
QIEFXQ = 2
QIPOUY = 271
QJYMOU = "".join(
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
QLAIID = "".join(chr(c) for c in [51, 50, 75])
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
QNRSJM = 260
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
QPLSPF = 352
QRJJJV = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
QSNQLN = 287
QTMFZD = 455
QVXOIH = 466
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 478
RJHIUS = 261
RJJJVY = 316
RJZTAT = 450
RKINEJ = 311
RSJMCB = "".join(chr(c) for c in [66, 76])
RTFMNH = "".join(chr(c) for c in [75, 56, 53])
RURAZM = 477
RXCHWD = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
RYXBQF = "".join(
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
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
SELHBQ = 327
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 49, 52])
SIFJBI = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
SIRYXB = 351
SJMCBF = "".join(chr(c) for c in [67, 80])
SJWMNZ = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
SKSOKP = 303
SKWIVD = "".join(chr(c) for c in [80, 50, 76])
SNQLNM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
SOKPHU = 304
SOOQNR = "".join(chr(c) for c in [80, 51])
SPFTSI = "".join(
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
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 50, 57])
SSRURA = 476
SSUHBV = 291
STSEMC = "".join(chr(c) for c in [67, 70, 71, 49, 51])
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
SXUJUT = 364
TACCPQ = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
TATDZX = "".join(chr(c) for c in [67, 70, 71, 52])
TBJEUT = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 53])
TFMNHT = "".join(chr(c) for c in [75, 56])
THBSKS = "".join(chr(c) for c in [85, 100, 65, 117, 120])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIDUBS = "".join(chr(c) for c in [50, 53, 65])
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 49, 55])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 56])
TOPHUG = 358
TSEMCG = 461
TSIFJB = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
TTIDUB = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
TYEKCW = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
TYIYWS = 320
TZBBEK = 479
UBSSUH = 7
UBYGDS = 296
UGTYIY = 361
UHBVWV = 293
UIKFWR = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
UJUTYE = 365
UNBLKX = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
UNRJZT = 449
UNXNKM = 321
UOJRJH = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
UQEXLS = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
URAZMK = "".join(chr(c) for c in [67, 70, 71, 51, 48])
USOOQN = "".join(chr(c) for c in [80, 50])
USPBWJ = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
UTOPHU = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
UTYEKC = 367
UXFEFJ = 264
UYNQJY = 273
VDNQGV = "".join(chr(c) for c in [80, 52, 76])
VDQLAI = 290
VDSSRU = 475
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [105, 110, 88, 77])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = 472
VUBYGD = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
VUNXNK = "".join(chr(c) for c in [83, 79, 117, 116, 50])
VWVUBY = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 49, 57])
VYFCRT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [105, 110, 89, 74])
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
        65,
        99,
        116,
        105,
        111,
        110,
    ]
)
WBSIRY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
WDAFIK = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
WIVDNQ = "".join(chr(c) for c in [80, 51, 76])
WJYKLG = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
WMNZMJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
WRKINE = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
WSKWIV = "".join(chr(c) for c in [80, 50, 72])
WVUBYG = 295
XBQFYL = "".join(
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
XCHWDA = 331
XEKVKZ = "".join(chr(c) for c in [77, 73, 65])
XFEFJT = "".join(
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
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 50, 50])
XNKMLO = 322
XNQTMF = 454
XOIHBX = 467
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 49, 56])
XSJWMN = "".join(chr(c) for c in [77, 69, 68])
XTIACQ = "".join(chr(c) for c in [80, 50, 50])
XUJUTY = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
XWAJVD = "".join(chr(c) for c in [75, 56, 48, 48])
XYBQSN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
YBQSNQ = 285
YEKCWA = 262
YFCRTF = 357
YGDSBD = 297
YIYWSK = "".join(chr(c) for c in [78, 65])
YKLGQP = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
YLIUXF = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
YLJUIK = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
YMOUNB = "".join(chr(c) for c in [67, 80, 79, 84])
YNQJYM = "".join(chr(c) for c in [80, 117, 114, 103, 101])
YOUSPB = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWSKWI = "".join(chr(c) for c in [80, 49, 76])
YXBQFY = "".join(
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
YYLIUX = "".join(chr(c) for c in [78, 69, 87])
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 457
ZILXWA = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
ZMJIGY = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
ZMKQTD = 479
ZTATDZ = 451
ZUQEXL = 310
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 50, 52])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 54])
AFIKJP = [
    YIYWSK,
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
    SJMCBF,
]
AJVDQL = [
    NMHXEK,
    MHXEKV,
    HXEKVK,
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
]
CWAONP = [EKCWAO, KCWAON]
DKHTZB = [
    NIBXYB,
    IRYXBQ,
    XBQFYL,
    AMJMAO,
    JIGYOU,
    JNIBXY,
    IBXYBQ,
    PBWJYK,
    JYMOUN,
    WBSIRY,
    MAOAWB,
    FTSIFJ,
    GQPLSP,
    NEJNIB,
    JMAOAW,
    BSIRYX,
    AWBSIR,
    JBIAMJ,
    BQFYLJ,
    IFJBIA,
    TSIFJB,
    RYXBQF,
    LJUIKF,
    YXBQFY,
    SIFJBI,
    OAWBSI,
    MJMAOA,
    BIAMJM,
]
DUBSSU = [TIDUBS, IDUBSS]
EUTOPH = [
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    XWAJVD,
    HECVYY,
    HECVYY,
    HECVYY,
    TBJEUT,
    BJEUTO,
    JEUTOP,
]
FWRKIN = [HECVYY, KFWRKI, KFWRKI, KFWRKI]
GVUNXN = [
    YIYWSK,
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    KWIVDN,
    WIVDNQ,
    IVDNQG,
    VDNQGV,
    OQNRSJ,
    DNQGVU,
    SJMCBF,
    JMCBFE,
    CBFEGZ,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    NQGVUN,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    QGVUNX,
]
IBXTIA = [DNIBXT, NIBXTI]
IIDNIB = [DQLAII, QLAIID, LAIIDN, AIIDNI]
IUSOOQ = [ASSAKQ, JHIUSO, HIUSOO]
JVYFCR = [JJJVYF, JJVYFC]
JWMNZM = [KXSJWM, QXPICX, XSJWMN, XPICXQ, SJWMNZ]
LIUXFE = [ONPYYL, NPYYLI, PYYLIU, YYLIUX, YLIUXF]
MKQTDK = []
NRSJMC = [ASSAKQ, JHIUSO]
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
QFFTTI = [ACQFFT, CQFFTT]
QGLRAH = [ASSAKQ, XPICXQ]
QTDKHT = [
    JRJHIU,
    USOOQN,
    SOOQNR,
    OOQNRS,
    OQNRSJ,
    RSJMCB,
    SJMCBF,
    JMCBFE,
    CBFEGZ,
    BFEGZU,
    EGZUQE,
    GZUQEX,
    LSXUJU,
    XUJUTY,
    JUTYEK,
    KQTDKH,
]
RAHEOC = [ASSAKQ, LRAHEO]
SPBWJY = [HECVYY, USPBWJ, USPBWJ, USPBWJ]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
TDKHTZ = [
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
]
TIACQF = [RSJMCB, XTIACQ]
UGSELH = [
    YIYWSK,
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
    JUGSEL,
]
XLSXUJ = [UQEXLS, QEXLSX, EXLSXU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return KHTZBB

    @property
    def begin(self):
        return HTZBBE

    @property
    def end(self):
        return TZBBEK

    @property
    def all_device_keys(self):
        return QTDKHT

    @property
    def user_demand_keys(self):
        return TDKHTZ

    @property
    def error_keys(self):
        return DKHTZB

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
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, SAKQXP),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, SAKQXP),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, SAKQXP),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, SAKQXP),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, SAKQXP),
            JRJHIU: GeckoEnumStructAccessor(
                self.struct, JRJHIU, RJHIUS, ICXQIE, IUSOOQ, None, CXQIEF, None
            ),
            USOOQN: GeckoEnumStructAccessor(
                self.struct, USOOQN, RJHIUS, QIEFXQ, IUSOOQ, None, CXQIEF, None
            ),
            SOOQNR: GeckoEnumStructAccessor(
                self.struct, SOOQNR, RJHIUS, CXQIEF, IUSOOQ, None, CXQIEF, None
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, RJHIUS, VHFTHE, IUSOOQ, None, CXQIEF, None
            ),
            OQNRSJ: GeckoEnumStructAccessor(
                self.struct, OQNRSJ, QNRSJM, ICXQIE, NRSJMC, None, QIEFXQ, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, QNRSJM, AHEOCT, RAHEOC, None, QIEFXQ, None
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, QNRSJM, QIEFXQ, RAHEOC, None, QIEFXQ, None
            ),
            JMCBFE: GeckoEnumStructAccessor(
                self.struct, JMCBFE, QNRSJM, MCBFEG, RAHEOC, None, QIEFXQ, None
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, QNRSJM, CXQIEF, RAHEOC, None, QIEFXQ, None
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, QNRSJM, FEGZUQ, RAHEOC, None, QIEFXQ, None
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, QNRSJM, VHFTHE, RAHEOC, None, QIEFXQ, None
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, XLSXUJ, None, None, SAKQXP
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, None, XLSXUJ, None, None, None
            ),
            XUJUTY: GeckoWordStructAccessor(self.struct, XUJUTY, UJUTYE, None),
            JUTYEK: GeckoWordStructAccessor(self.struct, JUTYEK, UTYEKC, SAKQXP),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, ICXQIE, CWAONP, None, QIEFXQ, SAKQXP
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, LIUXFE, None, None, SAKQXP
            ),
            IUXFEF: GeckoTimeStructAccessor(self.struct, IUXFEF, UXFEFJ, SAKQXP),
            XFEFJT: GeckoByteStructAccessor(self.struct, XFEFJT, FEFJTA, SAKQXP),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, YEKCWA, QIEFXQ, CWAONP, None, QIEFXQ, SAKQXP
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, LIUXFE, None, None, SAKQXP
            ),
            TACCPQ: GeckoTimeStructAccessor(self.struct, TACCPQ, ACCPQI, SAKQXP),
            CCPQIP: GeckoByteStructAccessor(self.struct, CCPQIP, CPQIPO, SAKQXP),
            PQIPOU: GeckoByteStructAccessor(self.struct, PQIPOU, QIPOUY, SAKQXP),
            IPOUYN: GeckoByteStructAccessor(self.struct, IPOUYN, POUYNQ, SAKQXP),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, UYNQJY, ICXQIE, None),
            YNQJYM: GeckoBoolStructAccessor(self.struct, YNQJYM, UYNQJY, QIEFXQ, None),
            NQJYMO: GeckoBoolStructAccessor(self.struct, NQJYMO, UYNQJY, MCBFEG, None),
            QJYMOU: GeckoBoolStructAccessor(self.struct, QJYMOU, UYNQJY, CXQIEF, None),
            JYMOUN: GeckoBoolStructAccessor(self.struct, JYMOUN, UYNQJY, FEGZUQ, None),
            YMOUNB: GeckoBoolStructAccessor(self.struct, YMOUNB, JVHFTH, QIEFXQ, None),
            MOUNBL: GeckoBoolStructAccessor(self.struct, MOUNBL, OUNBLK, MCBFEG, None),
            UNBLKX: GeckoBoolStructAccessor(self.struct, UNBLKX, OUNBLK, FEGZUQ, None),
            NBLKXS: GeckoBoolStructAccessor(self.struct, NBLKXS, OUNBLK, VHFTHE, None),
            BLKXSJ: GeckoEnumStructAccessor(
                self.struct, BLKXSJ, LKXSJW, None, JWMNZM, None, None, None
            ),
            WMNZMJ: GeckoBoolStructAccessor(self.struct, WMNZMJ, MNZMJI, FEGZUQ, None),
            NZMJIG: GeckoBoolStructAccessor(self.struct, NZMJIG, MNZMJI, VHFTHE, None),
            ZMJIGY: GeckoWordStructAccessor(self.struct, ZMJIGY, MJIGYO, None),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, JVHFTH, AHEOCT, None),
            IGYOUS: GeckoTempStructAccessor(self.struct, IGYOUS, GYOUSP, None),
            YOUSPB: GeckoTempStructAccessor(self.struct, YOUSPB, OUSPBW, None),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, QNRSJM, FEGZUQ, SPBWJY, None, CXQIEF, None
            ),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, BWJYKL, QIEFXQ, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, JYKLGQ, QIEFXQ, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, KLGQPL, AHEOCT, None),
            LGQPLS: GeckoBoolStructAccessor(
                self.struct, LGQPLS, KLGQPL, QIEFXQ, SAKQXP
            ),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, QPLSPF, AHEOCT, None),
            PLSPFT: GeckoByteStructAccessor(self.struct, PLSPFT, LSPFTS, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, ICXQIE, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, JVHFTH, MCBFEG, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, OUNBLK, ICXQIE, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, OUNBLK, AHEOCT, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FJBIAM, QIEFXQ, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, FJBIAM, MCBFEG, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, MCBFEG, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, IAMJMA, CXQIEF, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, IAMJMA, FEGZUQ, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, IAMJMA, VHFTHE, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, AOAWBS, MCBFEG, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, AOAWBS, CXQIEF, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, AOAWBS, FEGZUQ, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, AOAWBS, VHFTHE, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, SIRYXB, QIEFXQ, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, SIRYXB, MCBFEG, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, QPLSPF, MCBFEG, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, MNZMJI, ICXQIE, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, MNZMJI, AHEOCT, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, QFYLJU, ICXQIE, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, JYKLGQ, ICXQIE, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FJBIAM, ICXQIE, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, FJBIAM, AHEOCT, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, FJBIAM, CXQIEF, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, IKFWRK, ICXQIE, None),
            KFWRKI: GeckoEnumStructAccessor(
                self.struct, KFWRKI, IKFWRK, AHEOCT, FWRKIN, None, CXQIEF, None
            ),
            WRKINE: GeckoWordStructAccessor(self.struct, WRKINE, RKINEJ, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, INEJNI, ICXQIE, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, EJNIBX, ICXQIE, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, EJNIBX, AHEOCT, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, SIRYXB, ICXQIE, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, SIRYXB, AHEOCT, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, SIRYXB, CXQIEF, None),
            XYBQSN: GeckoWordStructAccessor(self.struct, XYBQSN, YBQSNQ, None),
            BQSNQL: GeckoByteStructAccessor(self.struct, BQSNQL, QSNQLN, None),
            SNQLNM: GeckoByteStructAccessor(self.struct, SNQLNM, NQLNMH, None),
            QLNMHX: GeckoEnumStructAccessor(
                self.struct, QLNMHX, LNMHXE, None, AJVDQL, None, None, None
            ),
            JVDQLA: GeckoEnumStructAccessor(
                self.struct, JVDQLA, VDQLAI, ICXQIE, IIDNIB, None, CXQIEF, None
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, VDQLAI, QIEFXQ, IBXTIA, None, QIEFXQ, None
            ),
            BXTIAC: GeckoEnumStructAccessor(
                self.struct, BXTIAC, VDQLAI, MCBFEG, TIACQF, None, QIEFXQ, None
            ),
            IACQFF: GeckoEnumStructAccessor(
                self.struct, IACQFF, VDQLAI, CXQIEF, QFFTTI, None, QIEFXQ, None
            ),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, VDQLAI, FEGZUQ, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, VDQLAI, VHFTHE, None),
            TTIDUB: GeckoEnumStructAccessor(
                self.struct, TTIDUB, VDQLAI, UBSSUH, DUBSSU, None, QIEFXQ, None
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
                self.struct, VYFCRT, YFCRTF, None, EUTOPH, None, None, None
            ),
            UTOPHU: GeckoWordStructAccessor(self.struct, UTOPHU, TOPHUG, None),
            OPHUGT: GeckoByteStructAccessor(self.struct, OPHUGT, PHUGTY, None),
            HUGTYI: GeckoByteStructAccessor(self.struct, HUGTYI, UGTYIY, None),
            GTYIYW: GeckoEnumStructAccessor(
                self.struct, GTYIYW, TYIYWS, None, GVUNXN, None, None, SAKQXP
            ),
            VUNXNK: GeckoEnumStructAccessor(
                self.struct, VUNXNK, UNXNKM, None, GVUNXN, None, None, SAKQXP
            ),
            NXNKML: GeckoEnumStructAccessor(
                self.struct, NXNKML, XNKMLO, None, GVUNXN, None, None, SAKQXP
            ),
            NKMLOI: GeckoEnumStructAccessor(
                self.struct, NKMLOI, KMLOIJ, None, GVUNXN, None, None, SAKQXP
            ),
            MLOIJU: GeckoEnumStructAccessor(
                self.struct, MLOIJU, LOIJUG, None, GVUNXN, None, None, SAKQXP
            ),
            OIJUGS: GeckoEnumStructAccessor(
                self.struct, OIJUGS, IJUGSE, None, UGSELH, None, None, SAKQXP
            ),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, SAKQXP),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, SAKQXP),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, SAKQXP),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, SAKQXP),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, SAKQXP),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, SAKQXP),
            WDAFIK: GeckoEnumStructAccessor(
                self.struct, WDAFIK, DAFIKJ, None, AFIKJP, None, None, SAKQXP
            ),
            FIKJPU: GeckoByteStructAccessor(self.struct, FIKJPU, IKJPUN, SAKQXP),
        }

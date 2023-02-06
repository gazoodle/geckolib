#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE v57'
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
ACQFFT = 294
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 54])
AHEOCT = 1
AIIDNI = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
AJVDQL = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = 467
AMJMAO = "".join(
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
AOAWBS = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
AONPYY = 266
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 49, 50])
AWBSIR = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
BDJQRJ = "".join(chr(c) for c in [75, 53])
BFEGZU = 310
BHZVOA = 478
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
        70,
        117,
        115,
        101,
        69,
        114,
        114,
    ]
)
BJEUTO = "".join(chr(c) for c in [80, 50, 72])
BLKXSJ = 355
BMJVHF = 256
BQFYLJ = 314
BQNRXC = 449
BQSNQL = "".join(chr(c) for c in [75, 54, 48, 48])
BSIRYX = 309
BSKSOK = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
BSSUHB = 300
BVWVUB = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
BWJYKL = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 57])
BXTIAC = 291
BXYBQS = "".join(chr(c) for c in [68, 74, 83, 52])
BYGDSB = "".join(chr(c) for c in [75, 50, 48, 48])
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
CGETIX = "".join(chr(c) for c in [67, 70, 71, 50, 51])
CHWDAF = "".join(chr(c) for c in [67, 70, 71, 52])
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
CQFFTT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
CRTFMN = 360
CTHBSK = 307
CVDSSR = 57
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = 264
CXQIEF = 4
DAFIKJ = 453
DGKEAK = 465
DJQRJJ = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
DSBDJQ = "".join(chr(c) for c in [75, 56])
DSSRUR = 479
DUBSSU = 299
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 49, 51])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 57])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = 272
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
EJNIBX = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
EKVKZI = "".join(chr(c) for c in [54, 52, 75])
ELHBQN = "".join(chr(c) for c in [67, 70, 71, 48])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 50, 50])
EOCTHB = 308
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 50, 52])
EUTOPH = "".join(chr(c) for c in [80, 51, 72])
EXLSXU = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
FCRTFM = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
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
FFTTID = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
FIKJPU = 454
FJBIAM = 351
FJTACC = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FMNHTB = "".join(chr(c) for c in [83, 79, 117, 116, 49])
FTHECV = 319
FTSIFJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
FTTIDU = 296
FWRKIN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = 315
FZDGKE = 464
GDSBDJ = "".join(chr(c) for c in [75, 56, 53])
GETIXQ = 471
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 56])
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GQPLSP = 284
GSELHB = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [83, 79, 117, 116, 50])
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
GYOUSP = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
GZUQEX = "".join(chr(c) for c in [70, 85, 76, 76])
HBQNRX = "".join(chr(c) for c in [67, 70, 71, 49])
HBSKSO = 303
HBVWVU = 316
HBXIBH = 476
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [80, 52])
HTBJEU = "".join(chr(c) for c in [80, 49, 72])
HUGTYI = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
HUOJRJ = 261
HWDAFI = 452
HXEKVK = "".join(chr(c) for c in [51, 50, 75])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 51, 49])
IACQFF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
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
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 51, 48])
IBXTIA = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
IBXYBQ = "".join(chr(c) for c in [77, 73, 65])
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [51, 48, 65])
IDUBSS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
IGYOUS = 280
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 56])
IIDNIB = "".join(chr(c) for c in [50, 53, 65])
IJUGSE = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
IKFWRK = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 55])
INEJNI = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = 282
IUSOOQ = "".join(chr(c) for c in [80, 53])
IUXFEF = 270
IVDNQG = 326
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 50, 53])
IYWSKW = 322
JBIAMJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
JEUTOP = "".join(chr(c) for c in [80, 50, 76])
JHIUSO = "".join(chr(c) for c in [80, 51])
JIGYOU = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
JJJVYF = "".join(chr(c) for c in [75, 51, 48, 48])
JJVYFC = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
JMAOAW = 354
JMCBFE = 5
JNIBXY = "".join(chr(c) for c in [105, 110, 88, 69])
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 56])
JQRJJJ = "".join(chr(c) for c in [75, 49, 48, 48])
JTACCP = 273
JUGSEL = 325
JUIKFW = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
JUTYEK = "".join(chr(c) for c in [83, 84, 79, 80])
JVDQLA = "".join(chr(c) for c in [53, 79, 80])
JVHFTH = 274
JWMNZM = 277
JYKLGQ = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
JYMOUN = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
JZTATD = 458
KCWAON = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
KEAKST = 466
KFWRKI = 285
KINEJN = 288
KJPUNR = 455
KLGQPL = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
KPHUOJ = 306
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 50, 48])
KWIVDN = 324
KXSJWM = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
KZILXW = "".join(chr(c) for c in [85, 76])
LAIIDN = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
LHBQNR = 448
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
LJUIKF = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
LKXSJW = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
LNMHXE = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
LOIJUG = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
LXWAJV = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
MAOAWB = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
MCBFEG = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
MCGETI = 470
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 49, 54])
MHXEKV = "".join(chr(c) for c in [49, 54, 75])
MJIGYO = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
MJMAOA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MLOIJU = 331
MNHTBJ = 320
MOUNBL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
NBLKXS = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
NEJNIB = 289
NHTBJE = "".join(chr(c) for c in [78, 65])
NIBXTI = 7
NIBXYB = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
NKMLOI = 330
NMHXEK = 290
NPYYLI = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
NQJYMO = "".join(chr(c) for c in [78, 79])
NQLNMH = "".join(chr(c) for c in [105, 110, 89, 84])
NQTMFZ = 462
NRJZTA = 457
NRSJMC = 3
NRXCHW = 450
NXNKML = 329
NZMJIG = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
OACMCV = "".join(chr(c) for c in [76, 73])
OAWBSI = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OIHBXI = 475
OIJUGS = 333
OJRJHI = "".join(chr(c) for c in [76, 79, 87])
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
ONPYYL = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
OOQNRS = "".join(chr(c) for c in [66, 76])
OPHUGT = "".join(chr(c) for c in [80, 52, 76])
OQNRSJ = "".join(chr(c) for c in [67, 80])
OUNBLK = 353
OUSPBW = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
OUYNQJ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
PBWJYK = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
PFTSIF = 350
PHUGTY = "".join(chr(c) for c in [66, 76, 79])
PHUOJR = "".join(chr(c) for c in [80, 49])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
POUYNQ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
PQIPOU = "".join(chr(c) for c in [67, 80, 79, 84])
PUNRJZ = 456
PYYLIU = 267
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 262
QFFTTI = 295
QFYLJU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
QGVUNX = 327
QIEFXQ = 2
QIPOUY = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
QJYMOU = "".join(chr(c) for c in [77, 69, 68])
QLAIID = "".join(
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
QNRSJM = "".join(chr(c) for c in [79, 51])
QNRXCH = "".join(chr(c) for c in [67, 70, 71, 50])
QPLSPF = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
QRJJJV = "".join(chr(c) for c in [75, 56, 48, 48])
QSNQLN = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 49, 53])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 50, 54])
QXPICX = "".join(chr(c) for c in [76, 79])
RJHIUS = "".join(chr(c) for c in [80, 50])
RJJJVY = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 49, 48])
RKINEJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
RSJMCB = "".join(chr(c) for c in [76, 49, 50, 48])
RTFMNH = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
RXCHWD = "".join(chr(c) for c in [67, 70, 71, 51])
RYXBQF = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [75, 52])
SELHBQ = 332
SEMCGE = 469
SIFJBI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
SIRYXB = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
SJMCBF = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
SKSOKP = 304
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 53])
SNQLNM = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
SOKPHU = 305
SPBWJY = 352
SPFTSI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
SSUHBV = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
STSEMC = 468
SUHBVW = 301
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
TATDZX = 459
TBJEUT = "".join(chr(c) for c in [80, 49, 76])
TDZXNQ = 460
TFMNHT = 361
THBSKS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = 293
TIDUBS = 297
TIXQVX = 472
TMFZDG = 463
TOPHUG = "".join(chr(c) for c in [80, 52, 72])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 50, 49])
TSIFJB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
TTIDUB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
TYEKCW = "".join(chr(c) for c in [78, 69, 87])
TYIYWS = 321
UBSSUH = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
UBYGDS = 357
UHBVWV = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
UIKFWR = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
UJUTYE = "".join(chr(c) for c in [73, 68, 76, 69])
UNBLKX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 57])
UNXNKM = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
UOJRJH = "".join(chr(c) for c in [72, 73, 71, 72])
UQEXLS = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
USOOQN = 260
USPBWJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
UTOPHU = "".join(chr(c) for c in [80, 51, 76])
UTYEKC = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UXFEFJ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
UYNQJY = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
VDNQGV = "".join(chr(c) for c in [72, 84, 82])
VDQLAI = "".join(chr(c) for c in [51, 79, 80])
VDSSRU = 256
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VUBYGD = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
VUNXNK = 328
VWVUBY = "".join(chr(c) for c in [70, 117, 108, 108])
VXOIHB = 474
VYFCRT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
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
WBSIRY = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
WDAFIK = "".join(chr(c) for c in [67, 70, 71, 53])
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
WJYKLG = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
WMNZMJ = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
WRKINE = 287
WSKWIV = 323
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
XCHWDA = 451
XEKVKZ = "".join(chr(c) for c in [52, 56, 75])
XFEFJT = 271
XIBHZV = 477
XLSXUJ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
XNKMLO = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 49, 52])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 50, 55])
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = 473
XSJWMN = 275
XTIACQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
XUJUTY = 263
XWAJVD = "".join(chr(c) for c in [80, 50, 50])
XYBQSN = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
YBQSNQ = "".join(chr(c) for c in [105, 110, 88, 77])
YEKCWA = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
YFCRTF = 358
YGDSBD = "".join(chr(c) for c in [75, 52, 48, 48])
YIYWSK = "".join(chr(c) for c in [83, 79, 117, 116, 51])
YKLGQP = 283
YLIUXF = 268
YLJUIK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
YNQJYM = 313
YOUSPB = 281
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWSKWI = "".join(chr(c) for c in [83, 79, 117, 116, 52])
YXBQFY = 311
YYLIUX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49, 55])
ZILXWA = "".join(chr(c) for c in [67, 69])
ZMJIGY = 279
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 49, 49])
ZVOACM = 479
ZXNQTM = 461
ACMCVD = [
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
    OACMCV,
]
CMCVDS = [
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
DNIBXT = [IIDNIB, IDNIBX]
DNQGVU = [
    NHTBJE,
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
    VDNQGV,
]
DQLAII = [JVDQLA, VDQLAI]
EKCWAO = [UJUTYE, JUTYEK, UTYEKC, TYEKCW, YEKCWA]
ILXWAJ = [KZILXW, ZILXWA]
IRYXBQ = [HECVYY, SIRYXB, SIRYXB, SIRYXB]
JRJHIU = [ASSAKQ, UOJRJH, OJRJHI]
JVYFCR = [
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    HECVYY,
    HECVYY,
    HECVYY,
    RJJJVY,
    JJJVYF,
    JJVYFC,
]
KVKZIL = [MHXEKV, HXEKVK, XEKVKZ, EKVKZI]
LSXUJU = [EXLSXU, XLSXUJ]
MCVDSS = [
    LJUIKF,
    JBIAMJ,
    AMJMAO,
    QPLSPF,
    LKXSJW,
    YLJUIK,
    JUIKFW,
    NZMJIG,
    CPQIPO,
    SIFJBI,
    SPFTSI,
    PBWJYK,
    USPBWJ,
    QFYLJU,
    LSPFTS,
    IFJBIA,
    TSIFJB,
    KLGQPL,
    MJMAOA,
    JYKLGQ,
    BWJYKL,
    BIAMJM,
    OAWBSI,
    IAMJMA,
    WJYKLG,
    FTSIFJ,
    PLSPFT,
    LGQPLS,
]
MNZMJI = [HECVYY, WMNZMJ, WMNZMJ, WMNZMJ]
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
RAHEOC = [ASSAKQ, LRAHEO]
SOOQNR = [ASSAKQ, UOJRJH]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
UGSELH = [
    NHTBJE,
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
UGTYIY = [
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    TOPHUG,
    OPHUGT,
    IUSOOQ,
    PHUGTY,
    OQNRSJ,
    QNRSJM,
    RSJMCB,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HUGTYI,
]
VOACMC = []
WAJVDQ = [OOQNRS, XWAJVD]
WVUBYG = [BVWVUB, VWVUBY]
YMOUNB = [NQJYMO, QXPICX, QJYMOU, XPICXQ, JYMOUN]
ZUQEXL = [FEGZUQ, EGZUQE, GZUQEX]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return CVDSSR

    @property
    def begin(self):
        return VDSSRU

    @property
    def end(self):
        return DSSRUR

    @property
    def all_device_keys(self):
        return ACMCVD

    @property
    def user_demand_keys(self):
        return CMCVDS

    @property
    def error_keys(self):
        return MCVDSS

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
                self.struct, UQEXLS, QEXLSX, ICXQIE, LSXUJU, None, QIEFXQ, SAKQXP
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XUJUTY, None, EKCWAO, None, None, SAKQXP
            ),
            KCWAON: GeckoTimeStructAccessor(self.struct, KCWAON, CWAONP, SAKQXP),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, SAKQXP),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, QEXLSX, QIEFXQ, LSXUJU, None, QIEFXQ, SAKQXP
            ),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, EKCWAO, None, None, SAKQXP
            ),
            YYLIUX: GeckoTimeStructAccessor(self.struct, YYLIUX, YLIUXF, SAKQXP),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, SAKQXP),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, SAKQXP),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, SAKQXP),
            FJTACC: GeckoBoolStructAccessor(self.struct, FJTACC, JTACCP, ICXQIE, None),
            TACCPQ: GeckoBoolStructAccessor(self.struct, TACCPQ, JTACCP, QIEFXQ, None),
            ACCPQI: GeckoBoolStructAccessor(self.struct, ACCPQI, JTACCP, NRSJMC, None),
            CCPQIP: GeckoBoolStructAccessor(self.struct, CCPQIP, JTACCP, CXQIEF, None),
            CPQIPO: GeckoBoolStructAccessor(self.struct, CPQIPO, JTACCP, JMCBFE, None),
            PQIPOU: GeckoBoolStructAccessor(self.struct, PQIPOU, JVHFTH, QIEFXQ, None),
            QIPOUY: GeckoBoolStructAccessor(self.struct, QIPOUY, IPOUYN, NRSJMC, None),
            POUYNQ: GeckoBoolStructAccessor(self.struct, POUYNQ, IPOUYN, JMCBFE, None),
            OUYNQJ: GeckoBoolStructAccessor(self.struct, OUYNQJ, IPOUYN, VHFTHE, None),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, YMOUNB, None, None, None
            ),
            MOUNBL: GeckoBoolStructAccessor(self.struct, MOUNBL, OUNBLK, JMCBFE, None),
            UNBLKX: GeckoBoolStructAccessor(self.struct, UNBLKX, OUNBLK, VHFTHE, None),
            NBLKXS: GeckoWordStructAccessor(self.struct, NBLKXS, BLKXSJ, None),
            LKXSJW: GeckoBoolStructAccessor(self.struct, LKXSJW, JVHFTH, AHEOCT, None),
            KXSJWM: GeckoTempStructAccessor(self.struct, KXSJWM, XSJWMN, None),
            SJWMNZ: GeckoTempStructAccessor(self.struct, SJWMNZ, JWMNZM, None),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, USOOQN, JMCBFE, MNZMJI, None, CXQIEF, None
            ),
            NZMJIG: GeckoBoolStructAccessor(self.struct, NZMJIG, ZMJIGY, QIEFXQ, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, ZMJIGY, VHFTHE, None),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, IGYOUS, QIEFXQ, None),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, YOUSPB, AHEOCT, None),
            OUSPBW: GeckoBoolStructAccessor(
                self.struct, OUSPBW, YOUSPB, QIEFXQ, SAKQXP
            ),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, SPBWJY, AHEOCT, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, JVHFTH, NRSJMC, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, IPOUYN, ICXQIE, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, IPOUYN, AHEOCT, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, YKLGQP, QIEFXQ, None),
            KLGQPL: GeckoBoolStructAccessor(self.struct, KLGQPL, YKLGQP, NRSJMC, None),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, GQPLSP, NRSJMC, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, GQPLSP, CXQIEF, None),
            PLSPFT: GeckoBoolStructAccessor(self.struct, PLSPFT, GQPLSP, JMCBFE, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, GQPLSP, VHFTHE, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, NRSJMC, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, PFTSIF, CXQIEF, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, PFTSIF, JMCBFE, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, PFTSIF, VHFTHE, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FJBIAM, QIEFXQ, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, FJBIAM, NRSJMC, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, SPBWJY, NRSJMC, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, OUNBLK, ICXQIE, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, OUNBLK, AHEOCT, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, ICXQIE, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, IGYOUS, ICXQIE, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, YKLGQP, ICXQIE, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, YKLGQP, AHEOCT, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, YKLGQP, CXQIEF, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, BSIRYX, ICXQIE, None),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, BSIRYX, AHEOCT, IRYXBQ, None, CXQIEF, None
            ),
            RYXBQF: GeckoWordStructAccessor(self.struct, RYXBQF, YXBQFY, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, ICXQIE, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, ICXQIE, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FYLJUI, AHEOCT, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, FJBIAM, ICXQIE, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, FJBIAM, AHEOCT, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, FJBIAM, CXQIEF, None),
            IKFWRK: GeckoWordStructAccessor(self.struct, IKFWRK, KFWRKI, None),
            FWRKIN: GeckoByteStructAccessor(self.struct, FWRKIN, WRKINE, None),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, None),
            INEJNI: GeckoEnumStructAccessor(
                self.struct, INEJNI, NEJNIB, None, QLNMHX, None, None, None
            ),
            LNMHXE: GeckoEnumStructAccessor(
                self.struct, LNMHXE, NMHXEK, ICXQIE, KVKZIL, None, CXQIEF, None
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, NMHXEK, QIEFXQ, ILXWAJ, None, QIEFXQ, None
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, NMHXEK, NRSJMC, WAJVDQ, None, QIEFXQ, None
            ),
            AJVDQL: GeckoEnumStructAccessor(
                self.struct, AJVDQL, NMHXEK, CXQIEF, DQLAII, None, QIEFXQ, None
            ),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, NMHXEK, JMCBFE, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, NMHXEK, VHFTHE, None),
            AIIDNI: GeckoEnumStructAccessor(
                self.struct, AIIDNI, NMHXEK, NIBXTI, DNIBXT, None, QIEFXQ, None
            ),
            IBXTIA: GeckoWordStructAccessor(self.struct, IBXTIA, BXTIAC, None),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, None),
            IACQFF: GeckoByteStructAccessor(self.struct, IACQFF, ACQFFT, None),
            CQFFTT: GeckoByteStructAccessor(self.struct, CQFFTT, QFFTTI, None),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoWordStructAccessor(self.struct, TTIDUB, TIDUBS, None),
            IDUBSS: GeckoByteStructAccessor(self.struct, IDUBSS, DUBSSU, None),
            UBSSUH: GeckoByteStructAccessor(self.struct, UBSSUH, BSSUHB, None),
            SSUHBV: GeckoWordStructAccessor(self.struct, SSUHBV, SUHBVW, None),
            UHBVWV: GeckoEnumStructAccessor(
                self.struct, UHBVWV, HBVWVU, None, WVUBYG, None, QIEFXQ, SAKQXP
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, JVYFCR, None, None, None
            ),
            VYFCRT: GeckoWordStructAccessor(self.struct, VYFCRT, YFCRTF, None),
            FCRTFM: GeckoByteStructAccessor(self.struct, FCRTFM, CRTFMN, None),
            RTFMNH: GeckoByteStructAccessor(self.struct, RTFMNH, TFMNHT, None),
            FMNHTB: GeckoEnumStructAccessor(
                self.struct, FMNHTB, MNHTBJ, None, UGTYIY, None, None, SAKQXP
            ),
            GTYIYW: GeckoEnumStructAccessor(
                self.struct, GTYIYW, TYIYWS, None, UGTYIY, None, None, SAKQXP
            ),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, UGTYIY, None, None, SAKQXP
            ),
            YWSKWI: GeckoEnumStructAccessor(
                self.struct, YWSKWI, WSKWIV, None, UGTYIY, None, None, SAKQXP
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, UGTYIY, None, None, SAKQXP
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, DNQGVU, None, None, SAKQXP
            ),
            NQGVUN: GeckoByteStructAccessor(self.struct, NQGVUN, QGVUNX, SAKQXP),
            GVUNXN: GeckoByteStructAccessor(self.struct, GVUNXN, VUNXNK, SAKQXP),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, SAKQXP),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, SAKQXP),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, SAKQXP),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, SAKQXP),
            IJUGSE: GeckoEnumStructAccessor(
                self.struct, IJUGSE, JUGSEL, None, UGSELH, None, None, SAKQXP
            ),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, SAKQXP),
        }

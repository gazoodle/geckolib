#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE v51'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 57])
ACQFFT = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 50])
AHEOCT = 308
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = 463
AMJMAO = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
AOAWBS = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
AONPYY = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
ASSAKQ = "".join(chr(c) for c in [85, 100, 80, 49])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 56])
AWBSIR = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
AZMKQT = 256
BDJQRJ = "".join(chr(c) for c in [80, 52, 76])
BFEGZU = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
BHZVOA = 474
BIAMJM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
BJEUTO = 336
BLKXSJ = 275
BMJVHF = 256
BQFYLJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
BQNRXC = 346
BQSNQL = "".join(chr(c) for c in [105, 110, 89, 84])
BSIRYX = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
BSKSOK = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
BVWVUB = "".join(chr(c) for c in [83, 79, 117, 116, 49])
BWJYKL = 283
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 53])
BXTIAC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
BXYBQS = "".join(chr(c) for c in [75, 54, 48, 48])
BYGDSB = "".join(chr(c) for c in [80, 50, 72])
CBFEGZ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
CCPQIP = "".join(chr(c) for c in [67, 80, 79, 84])
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 57])
CHWDAF = "".join(chr(c) for c in [67, 70, 71, 48])
CMCVDS = 477
CPQIPO = 274
CQBMJV = 317
CQFFTT = 296
CRTFMN = 324
CTHBSK = 303
CVDSSR = 478
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = 266
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = 449
DGKEAK = 461
DJQRJJ = "".join(chr(c) for c in [66, 76, 79])
DNIBXT = 291
DNQGVU = 330
DQLAII = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
DSBDJQ = "".join(chr(c) for c in [80, 51, 76])
DSSRUR = 479
DUBSSU = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 57])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 53])
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 273
EFXQGL = 258
EJNIBX = "".join(chr(c) for c in [77, 73, 65])
EKCWAO = 264
EKVKZI = "".join(chr(c) for c in [85, 76])
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 56])
EOCTHB = 307
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 50, 48])
EUTOPH = 337
FCRTFM = "".join(chr(c) for c in [83, 79, 117, 116, 53])
FEFJTA = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FEGZUQ = "".join(chr(c) for c in [70, 85, 76, 76])
FFTTID = 297
FIKJPU = 450
FJBIAM = "".join(
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
FJTACC = "".join(chr(c) for c in [80, 117, 114, 103, 101])
FMNHTB = "".join(chr(c) for c in [72, 84, 82])
FTHECV = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
FTSIFJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
FWRKIN = 288
FYLJUI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
FZDGKE = 460
GDSBDJ = "".join(chr(c) for c in [80, 51, 72])
GETIXQ = 467
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 52])
GQPLSP = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [83, 79, 117, 116, 54])
GVUNXN = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
GYOUSP = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
GZUQEX = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
HBSKSO = 304
HBXIBH = 472
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = 260
HTBJEU = 335
HUGTYI = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
HUOJRJ = "".join(chr(c) for c in [76, 79, 87])
HWDAFI = 448
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 55])
IACQFF = 295
IAMJMA = 354
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 54])
IBXTIA = 293
IBXYBQ = "".join(chr(c) for c in [105, 110, 88, 77])
ICXQIE = 2
IDNIBX = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
IDUBSS = 300
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = "".join(
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
IGYOUS = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 52])
IIDNIB = 7
IJUGSE = 342
IKFWRK = 287
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 51])
INEJNI = "".join(chr(c) for c in [105, 110, 88, 69])
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
IRYXBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
IUXFEF = 271
IVDNQG = 329
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 50, 49])
IYWSKW = 326
JBIAMJ = "".join(
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
JEUTOP = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
JHIUSO = "".join(chr(c) for c in [80, 53])
JIGYOU = 281
JJJVYF = 321
JJVYFC = "".join(chr(c) for c in [83, 79, 117, 116, 51])
JMAOAW = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
JMCBFE = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
JNIBXY = "".join(chr(c) for c in [68, 74, 83, 52])
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 52])
JQRJJJ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
JRJHIU = "".join(chr(c) for c in [80, 51])
JTACCP = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
JUIKFW = 285
JUTYEK = "".join(chr(c) for c in [78, 69, 87])
JVDQLA = "".join(
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
JVHFTH = 319
JVYFCR = 322
JWMNZM = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
JYKLGQ = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
JZTATD = 454
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
KEAKST = 462
KFWRKI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
KINEJN = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
KJPUNR = 451
KLGQPL = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
KMLOIJ = 340
KPHUOJ = 261
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 54])
KVKZIL = "".join(chr(c) for c in [67, 69])
KWIVDN = 328
KXSJWM = 277
KZILXW = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
LAIIDN = "".join(chr(c) for c in [51, 48, 65])
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
LHBQNR = 345
LIUXFE = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
LJUIKF = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
LKXSJW = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
LNMHXE = "".join(chr(c) for c in [51, 50, 75])
LOIJUG = 341
LRAHEO = 1
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
LSXUJU = 263
LXWAJV = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
MAOAWB = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
MCBFEG = 310
MCGETI = 466
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 51, 48])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 49, 50])
MHXEKV = "".join(chr(c) for c in [54, 52, 75])
MJIGYO = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
MJMAOA = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
MJVHFT = "".join(chr(c) for c in [77, 101, 110, 117])
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
MNZMJI = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
MOUNBL = 353
NBLKXS = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
NEJNIB = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
NHTBJE = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
NIBXTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
NIBXYB = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
NKMLOI = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
NMHXEK = "".join(chr(c) for c in [52, 56, 75])
NPYYLI = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
NQJYMO = "".join(chr(c) for c in [77, 69, 68])
NQLNMH = 290
NQTMFZ = 458
NRJZTA = 453
NRSJMC = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
NRXCHW = 347
NXNKML = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
NZMJIG = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
OACMCV = 476
OAWBSI = 309
OCTHBS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
OIHBXI = 471
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
OJRJHI = "".join(chr(c) for c in [80, 50])
OKPHUO = "".join(chr(c) for c in [80, 49])
ONPYYL = 267
OOQNRS = "".join(chr(c) for c in [79, 51])
OPHUGT = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
OQNRSJ = 3
OUNBLK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
OUSPBW = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
OUYNQJ = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
PBWJYK = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
PFTSIF = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
PHUGTY = 339
PHUOJR = "".join(chr(c) for c in [72, 73, 71, 72])
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = 350
POUYNQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
PQIPOU = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
PUNRJZ = 452
PYYLIU = 268
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
QFYLJU = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
QGLRAH = "".join(chr(c) for c in [79, 78])
QGVUNX = 331
QIEFXQ = 6
QIPOUY = 282
QJYMOU = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QLAIID = "".join(chr(c) for c in [50, 53, 65])
QLNMHX = "".join(chr(c) for c in [49, 54, 75])
QNRSJM = "".join(chr(c) for c in [76, 49, 50, 48])
QNRXCH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
QPLSPF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 49, 49])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 50, 50])
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RAZMKQ = 51
RJHIUS = "".join(chr(c) for c in [80, 52])
RJJJVY = "".join(chr(c) for c in [83, 79, 117, 116, 50])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 54])
RKINEJ = 289
RSJMCB = 5
RTFMNH = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
RXCHWD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
RYXBQF = 314
SAKQXP = "".join(chr(c) for c in [76, 79])
SBDJQR = "".join(chr(c) for c in [80, 52, 72])
SELHBQ = 344
SEMCGE = 465
SIFJBI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
SIRYXB = 311
SJMCBF = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
SKSOKP = 305
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 57])
SNQLNM = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
SOKPHU = 306
SOOQNR = "".join(chr(c) for c in [67, 80])
SPBWJY = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
SPFTSI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
SRURAZ = "".join(chr(c) for c in [76, 73])
SSAKQX = 259
SSUHBV = 316
STSEMC = 464
SUHBVW = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
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
TATDZX = 455
TBJEUT = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
TDZXNQ = 456
TFMNHT = 334
THBSKS = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
TIDUBS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
TIXQVX = 468
TMFZDG = 459
TOPHUG = 338
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 55])
TSIFJB = 351
TTIDUB = 299
TYIYWS = 325
UBSSUH = 301
UBYGDS = "".join(chr(c) for c in [80, 49, 76])
UGSELH = 343
UGTYIY = 349
UHBVWV = "".join(chr(c) for c in [70, 117, 108, 108])
UIKFWR = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
UJUTYE = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UNBLKX = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 53])
UQEXLS = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
USOOQN = "".join(chr(c) for c in [66, 76])
USPBWJ = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
UTOPHU = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
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
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
VDQLAI = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 51, 49])
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 56])
VUBYGD = "".join(chr(c) for c in [80, 49, 72])
VUNXNK = 332
VWVUBY = 320
VXOIHB = 470
VYFCRT = "".join(chr(c) for c in [83, 79, 117, 116, 52])
WAJVDQ = "".join(chr(c) for c in [51, 79, 80])
WAONPY = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
WDAFIK = "".join(chr(c) for c in [67, 70, 71, 49])
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
WJYKLG = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
WMNZMJ = 279
WRKINE = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
WSKWIV = 327
WVUBYG = "".join(chr(c) for c in [78, 65])
XBQFYL = 315
XCHWDA = 348
XEKVKZ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
XFEFJT = 272
XIBHZV = 473
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
XNKMLO = 333
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 49, 48])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 50, 51])
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = 469
XSJWMN = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
XTIACQ = 294
XUJUTY = "".join(chr(c) for c in [83, 84, 79, 80])
XWAJVD = "".join(chr(c) for c in [53, 79, 80])
XYBQSN = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
YBQSNQ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
YEKCWA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YFCRTF = 323
YGDSBD = "".join(chr(c) for c in [80, 50, 76])
YIYWSK = "".join(chr(c) for c in [83, 79, 117, 116, 55])
YKLGQP = 284
YLIUXF = 270
YLJUIK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
YMOUNB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
YNQJYM = "".join(chr(c) for c in [78, 79])
YOUSPB = 352
YPIPIV = 257
YWSKWI = "".join(chr(c) for c in [83, 79, 117, 116, 56])
YXBQFY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
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
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49, 51])
ZILXWA = "".join(chr(c) for c in [80, 50, 50])
ZMJIGY = 280
ZMKQTD = 479
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 55])
ZUQEXL = 262
ZVOACM = 475
ZXNQTM = 457
AIIDNI = [QLAIID, LAIIDN]
AJVDQL = [XWAJVD, WAJVDQ]
EGZUQE = [CBFEGZ, BFEGZU, FEGZUQ]
EXLSXU = [UQEXLS, QEXLSX]
FXQGLR = [IVLASS, AKQXPI]
GLRAHE = [IVLASS, QGLRAH]
HBVWVU = [SUHBVW, UHBVWV]
HXEKVK = [QLNMHX, LNMHXE, NMHXEK, MHXEKV]
ILXWAJ = [USOOQN, ZILXWA]
IUSOOQ = [IVLASS, PHUOJR]
JYMOUN = [YNQJYM, SAKQXP, NQJYMO, AKQXPI, QJYMOU]
KQXPIC = [IVLASS, SAKQXP, AKQXPI]
MNHTBJ = [
    WVUBYG,
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
    FMNHTB,
]
QRJJJV = [
    WVUBYG,
    VUBYGD,
    UBYGDS,
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    JHIUSO,
    DJQRJJ,
    SOOQNR,
    OOQNRS,
    QNRSJM,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    JQRJJJ,
]
QSNQLN = [
    KINEJN,
    INEJNI,
    NEJNIB,
    EJNIBX,
    JNIBXY,
    NIBXYB,
    IBXYBQ,
    BXYBQS,
    XYBQSN,
    YBQSNQ,
    BQSNQL,
]
RURAZM = [
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
    SRURAZ,
]
SJWMNZ = [HFTHEC, XSJWMN, XSJWMN, XSJWMN]
SSRURA = []
TYEKCW = [SXUJUT, XUJUTY, UJUTYE, JUTYEK, UTYEKC]
UNXNKM = [
    WVUBYG,
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
UOJRJH = [IVLASS, PHUOJR, HUOJRJ]
URAZMK = [
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
VKZILX = [EKVKZI, KVKZIL]
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
WBSIRY = [HFTHEC, AWBSIR, AWBSIR, AWBSIR]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return RAZMKQ

    @property
    def begin(self):
        return AZMKQT

    @property
    def end(self):
        return ZMKQTD

    @property
    def all_device_keys(self):
        return RURAZM

    @property
    def user_demand_keys(self):
        return URAZMK

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
            UNBLKX: GeckoBoolStructAccessor(self.struct, UNBLKX, CPQIPO, LRAHEO, None),
            NBLKXS: GeckoTempStructAccessor(self.struct, NBLKXS, BLKXSJ, None),
            LKXSJW: GeckoTempStructAccessor(self.struct, LKXSJW, KXSJWM, None),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, HIUSOO, RSJMCB, SJWMNZ, None, XPICXQ, None
            ),
            JWMNZM: GeckoBoolStructAccessor(self.struct, JWMNZM, WMNZMJ, ICXQIE, None),
            MNZMJI: GeckoBoolStructAccessor(self.struct, MNZMJI, WMNZMJ, QIEFXQ, None),
            NZMJIG: GeckoBoolStructAccessor(self.struct, NZMJIG, ZMJIGY, ICXQIE, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, JIGYOU, LRAHEO, None),
            IGYOUS: GeckoBoolStructAccessor(
                self.struct, IGYOUS, JIGYOU, ICXQIE, LASSAK
            ),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, YOUSPB, LRAHEO, None),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, CPQIPO, OQNRSJ, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, QIPOUY, QXPICX, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, QIPOUY, LRAHEO, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, BWJYKL, ICXQIE, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, BWJYKL, OQNRSJ, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, YKLGQP, OQNRSJ, None),
            KLGQPL: GeckoBoolStructAccessor(self.struct, KLGQPL, YKLGQP, XPICXQ, None),
            LGQPLS: GeckoBoolStructAccessor(self.struct, LGQPLS, YKLGQP, RSJMCB, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, YKLGQP, QIEFXQ, None),
            QPLSPF: GeckoBoolStructAccessor(self.struct, QPLSPF, PLSPFT, OQNRSJ, None),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, PLSPFT, XPICXQ, None),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PLSPFT, RSJMCB, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, PLSPFT, QIEFXQ, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, TSIFJB, ICXQIE, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, TSIFJB, OQNRSJ, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, YOUSPB, OQNRSJ, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, MOUNBL, QXPICX, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, MOUNBL, LRAHEO, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, QXPICX, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, ZMJIGY, QXPICX, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, BWJYKL, QXPICX, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, BWJYKL, LRAHEO, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, BWJYKL, XPICXQ, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, QXPICX, None),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, OAWBSI, LRAHEO, WBSIRY, None, XPICXQ, None
            ),
            BSIRYX: GeckoWordStructAccessor(self.struct, BSIRYX, SIRYXB, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, RYXBQF, QXPICX, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, XBQFYL, QXPICX, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, XBQFYL, LRAHEO, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, TSIFJB, QXPICX, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, TSIFJB, LRAHEO, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, TSIFJB, XPICXQ, None),
            LJUIKF: GeckoWordStructAccessor(self.struct, LJUIKF, JUIKFW, None),
            UIKFWR: GeckoByteStructAccessor(self.struct, UIKFWR, IKFWRK, None),
            KFWRKI: GeckoByteStructAccessor(self.struct, KFWRKI, FWRKIN, None),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, RKINEJ, None, QSNQLN, None, None, None
            ),
            SNQLNM: GeckoEnumStructAccessor(
                self.struct, SNQLNM, NQLNMH, QXPICX, HXEKVK, None, XPICXQ, None
            ),
            XEKVKZ: GeckoEnumStructAccessor(
                self.struct, XEKVKZ, NQLNMH, ICXQIE, VKZILX, None, ICXQIE, None
            ),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, NQLNMH, OQNRSJ, ILXWAJ, None, ICXQIE, None
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, NQLNMH, XPICXQ, AJVDQL, None, ICXQIE, None
            ),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, NQLNMH, RSJMCB, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, NQLNMH, QIEFXQ, None),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, NQLNMH, IIDNIB, AIIDNI, None, ICXQIE, None
            ),
            IDNIBX: GeckoWordStructAccessor(self.struct, IDNIBX, DNIBXT, None),
            NIBXTI: GeckoByteStructAccessor(self.struct, NIBXTI, IBXTIA, None),
            BXTIAC: GeckoByteStructAccessor(self.struct, BXTIAC, XTIACQ, None),
            TIACQF: GeckoByteStructAccessor(self.struct, TIACQF, IACQFF, None),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoWordStructAccessor(self.struct, QFFTTI, FFTTID, None),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, None),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, None),
            DUBSSU: GeckoWordStructAccessor(self.struct, DUBSSU, UBSSUH, None),
            BSSUHB: GeckoEnumStructAccessor(
                self.struct, BSSUHB, SSUHBV, None, HBVWVU, None, ICXQIE, LASSAK
            ),
            BVWVUB: GeckoEnumStructAccessor(
                self.struct, BVWVUB, VWVUBY, None, QRJJJV, None, None, LASSAK
            ),
            RJJJVY: GeckoEnumStructAccessor(
                self.struct, RJJJVY, JJJVYF, None, QRJJJV, None, None, LASSAK
            ),
            JJVYFC: GeckoEnumStructAccessor(
                self.struct, JJVYFC, JVYFCR, None, QRJJJV, None, None, LASSAK
            ),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, YFCRTF, None, QRJJJV, None, None, LASSAK
            ),
            FCRTFM: GeckoEnumStructAccessor(
                self.struct, FCRTFM, CRTFMN, None, QRJJJV, None, None, LASSAK
            ),
            RTFMNH: GeckoEnumStructAccessor(
                self.struct, RTFMNH, TFMNHT, None, MNHTBJ, None, None, LASSAK
            ),
            NHTBJE: GeckoByteStructAccessor(self.struct, NHTBJE, HTBJEU, LASSAK),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, LASSAK),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, LASSAK),
            UTOPHU: GeckoByteStructAccessor(self.struct, UTOPHU, TOPHUG, LASSAK),
            OPHUGT: GeckoByteStructAccessor(self.struct, OPHUGT, PHUGTY, LASSAK),
            HUGTYI: GeckoByteStructAccessor(self.struct, HUGTYI, UGTYIY, LASSAK),
            GTYIYW: GeckoEnumStructAccessor(
                self.struct, GTYIYW, TYIYWS, None, QRJJJV, None, None, LASSAK
            ),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, QRJJJV, None, None, LASSAK
            ),
            YWSKWI: GeckoEnumStructAccessor(
                self.struct, YWSKWI, WSKWIV, None, QRJJJV, None, None, LASSAK
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, QRJJJV, None, None, LASSAK
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, QRJJJV, None, None, LASSAK
            ),
            VDNQGV: GeckoEnumStructAccessor(
                self.struct, VDNQGV, DNQGVU, None, QRJJJV, None, None, LASSAK
            ),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, QGVUNX, None, QRJJJV, None, None, LASSAK
            ),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, UNXNKM, None, None, LASSAK
            ),
            NXNKML: GeckoEnumStructAccessor(
                self.struct, NXNKML, XNKMLO, None, UNXNKM, None, None, LASSAK
            ),
            NKMLOI: GeckoByteStructAccessor(self.struct, NKMLOI, KMLOIJ, LASSAK),
            MLOIJU: GeckoByteStructAccessor(self.struct, MLOIJU, LOIJUG, LASSAK),
            OIJUGS: GeckoByteStructAccessor(self.struct, OIJUGS, IJUGSE, LASSAK),
            JUGSEL: GeckoByteStructAccessor(self.struct, JUGSEL, UGSELH, LASSAK),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, LASSAK),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, LASSAK),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, LASSAK),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, LASSAK),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, LASSAK),
        }

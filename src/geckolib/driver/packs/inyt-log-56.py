#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v56'
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
ACCPQI = 267
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 49, 55])
ACQFFT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
AFIKJP = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
AJVDQL = 290
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = 451
AMJMAO = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
AOAWBS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
ATDZXN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
AWBSIR = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
AZMKQT = 470
BBEKBD = "".join(chr(c) for c in [67, 70, 71, 50, 56])
BDFSRO = "".join(chr(c) for c in [67, 70, 71, 51, 48])
BDJQRJ = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
BEKBDF = 476
BFEGZU = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
BHZVOA = 462
BIAMJM = 284
BJEUTO = "".join(chr(c) for c in [80, 50, 76])
BLKXSJ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
BMJVHF = 256
BQFYLJ = 354
BQNRXC = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
BQSNQL = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
BSIRYX = 351
BSKSOK = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
BSSUHB = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
BVWVUB = "".join(chr(c) for c in [70, 117, 108, 108])
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 49, 51])
BXTIAC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
BXYBQS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
BYGDSB = "".join(chr(c) for c in [75, 52, 48, 48])
CBFEGZ = "".join(chr(c) for c in [76, 49, 50, 48])
CCPQIP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
CGETIX = "".join(chr(c) for c in [67, 70, 71, 55])
CHWDAF = 331
CMCVDS = 465
CPQIPO = 268
CQBMJV = 317
CQFFTT = 295
CRTFMN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
CTHBSK = 307
CVDSSR = 466
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
CXQIEF = 4
DDPMXF = 56
DFSROG = 478
DGKEAK = 449
DJQRJJ = "".join(chr(c) for c in [75, 49, 48, 48])
DKHTZB = 473
DPMXFU = 256
DQLAII = "".join(chr(c) for c in [52, 56, 75])
DSBDJQ = "".join(chr(c) for c in [75, 52])
DSSRUR = 467
DUBSSU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
DZXNQT = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 51])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EFJTAC = "".join(
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
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
EJNIBX = 315
EKBDFS = "".join(chr(c) for c in [67, 70, 71, 50, 57])
EKCWAO = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
EKVKZI = "".join(chr(c) for c in [68, 74, 83, 52])
ELHBQN = 327
EMCGET = "".join(chr(c) for c in [67, 70, 71, 54])
EOCTHB = 308
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 56])
EUTOPH = "".join(chr(c) for c in [80, 51, 76])
EXLSXU = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
FCRTFM = 360
FEFJTA = 264
FEGZUQ = 5
FFTTID = 296
FIKJPU = 333
FJBIAM = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
FJTACC = 266
FMNHTB = 320
FSROGM = "".join(chr(c) for c in [67, 70, 71, 51, 49])
FTHECV = 319
FTSIFJ = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
FWRKIN = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
FZDGKE = 448
GDSBDJ = "".join(chr(c) for c in [75, 56])
GETIXQ = 455
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 50])
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GQPLSP = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
GSELHB = 326
GTYIYW = "".join(chr(c) for c in [83, 79, 117, 116, 50])
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
GYOUSP = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
GZUQEX = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
HBQNRX = 328
HBSKSO = 363
HBVWVU = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
HBXIBH = 460
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [76, 79, 87])
HTBJEU = "".join(chr(c) for c in [80, 49, 76])
HTZBBE = 474
HUGTYI = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
HUOJRJ = 306
HWDAFI = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
HXEKVK = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 49, 53])
IACQFF = 294
IAMJMA = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 49, 52])
IBXTIA = 291
IBXYBQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
ICXQIE = 0
IDNIBX = "".join(chr(c) for c in [67, 69])
IDUBSS = 299
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = 283
IGYOUS = 355
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 49, 50])
IIDNIB = "".join(chr(c) for c in [85, 76])
IJUGSE = "".join(chr(c) for c in [83, 79, 117, 116, 54])
IKFWRK = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
IKJPUN = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
ILXWAJ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
INEJNI = 314
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
IRYXBQ = "".join(
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
IUXFEF = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
IVDNQG = 334
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 57])
IYWSKW = 322
JBIAMJ = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
JEUTOP = "".join(chr(c) for c in [80, 51, 72])
JHIUSO = "".join(chr(c) for c in [72, 73, 71, 72])
JIGYOU = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
JJJVYF = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68])
JMAOAW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
JMCBFE = "".join(chr(c) for c in [79, 51])
JNIBXY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
JPUNRJ = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
JQRJJJ = "".join(chr(c) for c in [75, 56, 48, 48])
JRJHIU = "".join(chr(c) for c in [80, 49])
JTACCP = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
JUGSEL = 325
JUIKFW = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
JUTYEK = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
JVDQLA = "".join(chr(c) for c in [49, 54, 75])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
JWMNZM = "".join(chr(c) for c in [77, 69, 68])
JYKLGQ = 279
JYMOUN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
JZTATD = 343
KBDFSR = 477
KCWAON = 262
KEAKST = 450
KHTZBB = "".join(chr(c) for c in [67, 70, 71, 50, 54])
KINEJN = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
KJPUNR = 340
KLGQPL = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
KMLOIJ = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
KPHUOJ = 305
KQTDKH = "".join(chr(c) for c in [67, 70, 71, 50, 52])
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 52])
KVKZIL = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
KWIVDN = 324
KXSJWM = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
KZILXW = "".join(chr(c) for c in [75, 54, 48, 48])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = 280
LHBQNR = "".join(chr(c) for c in [83, 79, 117, 116, 57])
LIUXFE = "".join(chr(c) for c in [78, 69, 87])
LJUIKF = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
LKXSJW = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
LNMHXE = 289
LOIJUG = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
LSXUJU = "".join(chr(c) for c in [70, 85, 76, 76])
LXWAJV = "".join(chr(c) for c in [105, 110, 89, 84])
MAOAWB = 350
MCBFEG = 3
MCGETI = 454
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 49, 56])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 48])
MHXEKV = "".join(chr(c) for c in [105, 110, 88, 69])
MJIGYO = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
MJMAOA = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 471
MLOIJU = 339
MNHTBJ = "".join(chr(c) for c in [78, 65])
MOUNBL = "".join(
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
NBLKXS = 282
NEJNIB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
NHTBJE = "".join(chr(c) for c in [80, 49, 72])
NIBXTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
NIBXYB = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
NKMLOI = 338
NMHXEK = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
NPYYLI = 263
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
NQJYMO = 273
NQLNMH = 288
NQTMFZ = 347
NRJZTA = 342
NRXCHW = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
NXNKML = 337
NZMJIG = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
OACMCV = 464
OAWBSI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = "".join(chr(c) for c in [76, 73])
OIHBXI = 459
OIJUGS = 349
OJRJHI = 362
OKPHUO = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
ONPYYL = "".join(
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
OOQNRS = "".join(chr(c) for c in [80, 52])
OPHUGT = "".join(chr(c) for c in [66, 76, 79])
OQNRSJ = "".join(chr(c) for c in [80, 53])
OUNBLK = "".join(chr(c) for c in [67, 80, 79, 84])
OUSPBW = 275
OUYNQJ = "".join(
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
PBWJYK = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
PFTSIF = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
PHUGTY = "".join(chr(c) for c in [70, 97, 110])
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
PMXFUB = 479
POUYNQ = 271
PQIPOU = "".join(
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
PUNRJZ = 341
PYYLIU = "".join(chr(c) for c in [73, 68, 76, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 310
QFFTTI = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
QFYLJU = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
QGVUNX = 335
QIEFXQ = 2
QIPOUY = 270
QJYMOU = "".join(chr(c) for c in [80, 117, 114, 103, 101])
QLAIID = "".join(chr(c) for c in [54, 52, 75])
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
QNRSJM = 260
QNRXCH = 329
QPLSPF = 281
QRJJJV = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
QSNQLN = 287
QTDKHT = 472
QTMFZD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 49, 48])
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 50, 50])
RJHIUS = 261
RJJJVY = "".join(chr(c) for c in [75, 51, 48, 48])
RJZTAT = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
RKINEJ = 311
RSJMCB = "".join(chr(c) for c in [66, 76])
RTFMNH = 361
RURAZM = "".join(chr(c) for c in [67, 70, 71, 50, 49])
RXCHWD = 330
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
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [75, 53])
SELHBQ = "".join(chr(c) for c in [83, 79, 117, 116, 56])
SEMCGE = 453
SIFJBI = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
SIRYXB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
SJMCBF = "".join(chr(c) for c in [67, 80])
SJWMNZ = "".join(chr(c) for c in [78, 79])
SKSOKP = 303
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 53])
SNQLNM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
SOKPHU = 304
SOOQNR = "".join(chr(c) for c in [80, 51])
SPBWJY = 277
SPFTSI = 352
SROGMD = 479
SRURAZ = 468
SSRURA = "".join(chr(c) for c in [67, 70, 71, 50, 48])
SSUHBV = 301
STSEMC = 452
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
TACCPQ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
TATDZX = 344
TBJEUT = "".join(chr(c) for c in [80, 50, 72])
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 50, 53])
TDZXNQ = 345
TFMNHT = "".join(chr(c) for c in [83, 79, 117, 116, 49])
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TIDUBS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
TIXQVX = 456
TMFZDG = 348
TOPHUG = "".join(chr(c) for c in [80, 52, 76])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 53])
TSIFJB = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
TTIDUB = 297
TYEKCW = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
TYIYWS = 321
TZBBEK = "".join(chr(c) for c in [67, 70, 71, 50, 55])
UBSSUH = 300
UBYGDS = "".join(chr(c) for c in [75, 50, 48, 48])
UGSELH = "".join(chr(c) for c in [83, 79, 117, 116, 55])
UHBVWV = 316
UIKFWR = 309
UJUTYE = 364
UNBLKX = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
UNRJZT = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
UNXNKM = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
UOJRJH = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
UQEXLS = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
URAZMK = 469
USOOQN = "".join(chr(c) for c in [80, 50])
USPBWJ = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
UTOPHU = "".join(chr(c) for c in [80, 52, 72])
UTYEKC = 365
UYNQJY = 272
VDNQGV = "".join(chr(c) for c in [72, 84, 82])
VDQLAI = "".join(chr(c) for c in [51, 50, 75])
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 49, 57])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [105, 110, 88, 77])
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 49, 54])
VUBYGD = 357
VUNXNK = 336
VXOIHB = 458
VYFCRT = 358
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
WAONPY = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
WBSIRY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
WDAFIK = 332
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
WJYKLG = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
WMNZMJ = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
WRKINE = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
WSKWIV = 323
WVUBYG = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
XBQFYL = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
XCHWDA = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
XEKVKZ = "".join(chr(c) for c in [77, 73, 65])
XFEFJT = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
XIBHZV = 461
XLSXUJ = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
XNKMLO = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
XNQTMF = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 49, 49])
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = 457
XSJWMN = 313
XTIACQ = 293
XUJUTY = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
XYBQSN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
YBQSNQ = 285
YEKCWA = 367
YFCRTF = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
YGDSBD = "".join(chr(c) for c in [75, 56, 53])
YIYWSK = "".join(chr(c) for c in [83, 79, 117, 116, 51])
YKLGQP = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
YLIUXF = "".join(chr(c) for c in [83, 84, 65, 82, 84])
YLJUIK = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
YMOUNB = "".join(
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
YNQJYM = "".join(chr(c) for c in [67, 108, 101, 97, 110])
YOUSPB = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWSKWI = "".join(chr(c) for c in [83, 79, 117, 116, 52])
YXBQFY = "".join(
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
YYLIUX = "".join(chr(c) for c in [83, 84, 79, 80])
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 475
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49])
ZILXWA = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
ZMJIGY = 353
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 50, 51])
ZTATDZ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
ZUQEXL = 7
ZVOACM = 463
ZXNQTM = 346
AONPYY = [CWAONP, WAONPY]
BWJYKL = [HECVYY, PBWJYK, PBWJYK, PBWJYK]
DAFIKJ = [
    MNHTBJ,
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
DNIBXT = [IIDNIB, IDNIBX]
DNQGVU = [
    MNHTBJ,
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
GMDDPM = [
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
    UQEXLS,
    XUJUTY,
    JUTYEK,
    TYEKCW,
    OGMDDP,
]
IUSOOQ = [ASSAKQ, JHIUSO, HIUSOO]
JJVYFC = [
    UBYGDS,
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    HECVYY,
    HECVYY,
    HECVYY,
    QRJJJV,
    RJJJVY,
    JJJVYF,
]
KFWRKI = [HECVYY, IKFWRK, IKFWRK, IKFWRK]
LAIIDN = [JVDQLA, VDQLAI, DQLAII, QLAIID]
MDDPMX = [
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
MNZMJI = [SJWMNZ, QXPICX, JWMNZM, XPICXQ, WMNZMJ]
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
QGLRAH = [ASSAKQ, XPICXQ]
RAHEOC = [ASSAKQ, LRAHEO]
ROGMDD = []
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
SXUJUT = [EXLSXU, XLSXUJ, LSXUJU]
UGTYIY = [
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    TOPHUG,
    OQNRSJ,
    OPHUGT,
    SJMCBF,
    JMCBFE,
    CBFEGZ,
    HECVYY,
    HECVYY,
    PHUGTY,
    HECVYY,
    HECVYY,
    HUGTYI,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    GZUQEX,
]
UXFEFJ = [PYYLIU, YYLIUX, YLIUXF, LIUXFE, IUXFEF]
VWVUBY = [HBVWVU, BVWVUB]
XWAJVD = [
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
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return DDPMXF

    @property
    def begin(self):
        return DPMXFU

    @property
    def end(self):
        return PMXFUB

    @property
    def all_device_keys(self):
        return GMDDPM

    @property
    def user_demand_keys(self):
        return MDDPMX

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
                self.struct, GZUQEX, QNRSJM, ZUQEXL, RAHEOC, None, QIEFXQ, None
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, QEXLSX, None, SXUJUT, None, None, SAKQXP
            ),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UJUTYE, None, SXUJUT, None, None, None
            ),
            JUTYEK: GeckoWordStructAccessor(self.struct, JUTYEK, UTYEKC, None),
            TYEKCW: GeckoWordStructAccessor(self.struct, TYEKCW, YEKCWA, SAKQXP),
            EKCWAO: GeckoEnumStructAccessor(
                self.struct, EKCWAO, KCWAON, ICXQIE, AONPYY, None, QIEFXQ, SAKQXP
            ),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, NPYYLI, None, UXFEFJ, None, None, SAKQXP
            ),
            XFEFJT: GeckoTimeStructAccessor(self.struct, XFEFJT, FEFJTA, SAKQXP),
            EFJTAC: GeckoByteStructAccessor(self.struct, EFJTAC, FJTACC, SAKQXP),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, KCWAON, QIEFXQ, AONPYY, None, QIEFXQ, SAKQXP
            ),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, None, UXFEFJ, None, None, SAKQXP
            ),
            CCPQIP: GeckoTimeStructAccessor(self.struct, CCPQIP, CPQIPO, SAKQXP),
            PQIPOU: GeckoByteStructAccessor(self.struct, PQIPOU, QIPOUY, SAKQXP),
            IPOUYN: GeckoByteStructAccessor(self.struct, IPOUYN, POUYNQ, SAKQXP),
            OUYNQJ: GeckoByteStructAccessor(self.struct, OUYNQJ, UYNQJY, SAKQXP),
            YNQJYM: GeckoBoolStructAccessor(self.struct, YNQJYM, NQJYMO, ICXQIE, None),
            QJYMOU: GeckoBoolStructAccessor(self.struct, QJYMOU, NQJYMO, QIEFXQ, None),
            JYMOUN: GeckoBoolStructAccessor(self.struct, JYMOUN, NQJYMO, MCBFEG, None),
            YMOUNB: GeckoBoolStructAccessor(self.struct, YMOUNB, NQJYMO, CXQIEF, None),
            MOUNBL: GeckoBoolStructAccessor(self.struct, MOUNBL, NQJYMO, FEGZUQ, None),
            OUNBLK: GeckoBoolStructAccessor(self.struct, OUNBLK, JVHFTH, QIEFXQ, None),
            UNBLKX: GeckoBoolStructAccessor(self.struct, UNBLKX, NBLKXS, MCBFEG, None),
            BLKXSJ: GeckoBoolStructAccessor(self.struct, BLKXSJ, NBLKXS, FEGZUQ, None),
            LKXSJW: GeckoBoolStructAccessor(self.struct, LKXSJW, NBLKXS, VHFTHE, None),
            KXSJWM: GeckoEnumStructAccessor(
                self.struct, KXSJWM, XSJWMN, None, MNZMJI, None, None, None
            ),
            NZMJIG: GeckoBoolStructAccessor(self.struct, NZMJIG, ZMJIGY, FEGZUQ, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, ZMJIGY, VHFTHE, None),
            JIGYOU: GeckoWordStructAccessor(self.struct, JIGYOU, IGYOUS, None),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, JVHFTH, AHEOCT, None),
            YOUSPB: GeckoTempStructAccessor(self.struct, YOUSPB, OUSPBW, None),
            USPBWJ: GeckoTempStructAccessor(self.struct, USPBWJ, SPBWJY, None),
            PBWJYK: GeckoEnumStructAccessor(
                self.struct, PBWJYK, QNRSJM, FEGZUQ, BWJYKL, None, CXQIEF, None
            ),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, JYKLGQ, QIEFXQ, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, JYKLGQ, VHFTHE, None),
            KLGQPL: GeckoBoolStructAccessor(self.struct, KLGQPL, LGQPLS, QIEFXQ, None),
            GQPLSP: GeckoBoolStructAccessor(self.struct, GQPLSP, QPLSPF, AHEOCT, None),
            PLSPFT: GeckoBoolStructAccessor(
                self.struct, PLSPFT, QPLSPF, QIEFXQ, SAKQXP
            ),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, SPFTSI, AHEOCT, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, JVHFTH, MCBFEG, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, NBLKXS, ICXQIE, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, NBLKXS, AHEOCT, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, IFJBIA, QIEFXQ, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, IFJBIA, MCBFEG, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, BIAMJM, MCBFEG, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, BIAMJM, CXQIEF, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, BIAMJM, FEGZUQ, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, BIAMJM, VHFTHE, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MAOAWB, MCBFEG, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, MAOAWB, CXQIEF, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, MAOAWB, FEGZUQ, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, MAOAWB, VHFTHE, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, BSIRYX, QIEFXQ, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, BSIRYX, MCBFEG, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, SPFTSI, MCBFEG, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, ZMJIGY, ICXQIE, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, ZMJIGY, AHEOCT, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, ICXQIE, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, LGQPLS, ICXQIE, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, IFJBIA, ICXQIE, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, IFJBIA, AHEOCT, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, IFJBIA, CXQIEF, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, UIKFWR, ICXQIE, None),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, UIKFWR, AHEOCT, KFWRKI, None, CXQIEF, None
            ),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, UIKFWR, MCBFEG, None),
            WRKINE: GeckoWordStructAccessor(self.struct, WRKINE, RKINEJ, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, INEJNI, ICXQIE, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, EJNIBX, ICXQIE, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, EJNIBX, AHEOCT, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, BSIRYX, ICXQIE, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BSIRYX, AHEOCT, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, BSIRYX, CXQIEF, None),
            XYBQSN: GeckoWordStructAccessor(self.struct, XYBQSN, YBQSNQ, None),
            BQSNQL: GeckoByteStructAccessor(self.struct, BQSNQL, QSNQLN, None),
            SNQLNM: GeckoByteStructAccessor(self.struct, SNQLNM, NQLNMH, None),
            QLNMHX: GeckoEnumStructAccessor(
                self.struct, QLNMHX, LNMHXE, None, XWAJVD, None, None, None
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, AJVDQL, ICXQIE, LAIIDN, None, CXQIEF, None
            ),
            AIIDNI: GeckoEnumStructAccessor(
                self.struct, AIIDNI, AJVDQL, QIEFXQ, DNIBXT, None, QIEFXQ, None
            ),
            NIBXTI: GeckoWordStructAccessor(self.struct, NIBXTI, IBXTIA, None),
            BXTIAC: GeckoByteStructAccessor(self.struct, BXTIAC, XTIACQ, None),
            TIACQF: GeckoByteStructAccessor(self.struct, TIACQF, IACQFF, None),
            ACQFFT: GeckoByteStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, None),
            FTTIDU: GeckoWordStructAccessor(self.struct, FTTIDU, TTIDUB, None),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, None),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, None),
            BSSUHB: GeckoWordStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoEnumStructAccessor(
                self.struct, SUHBVW, UHBVWV, None, VWVUBY, None, QIEFXQ, SAKQXP
            ),
            WVUBYG: GeckoEnumStructAccessor(
                self.struct, WVUBYG, VUBYGD, None, JJVYFC, None, None, None
            ),
            JVYFCR: GeckoWordStructAccessor(self.struct, JVYFCR, VYFCRT, None),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, None),
            CRTFMN: GeckoByteStructAccessor(self.struct, CRTFMN, RTFMNH, None),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, FMNHTB, None, UGTYIY, None, None, SAKQXP
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
                self.struct, IJUGSE, JUGSEL, None, UGTYIY, None, None, SAKQXP
            ),
            UGSELH: GeckoEnumStructAccessor(
                self.struct, UGSELH, GSELHB, None, UGTYIY, None, None, SAKQXP
            ),
            SELHBQ: GeckoEnumStructAccessor(
                self.struct, SELHBQ, ELHBQN, None, UGTYIY, None, None, SAKQXP
            ),
            LHBQNR: GeckoEnumStructAccessor(
                self.struct, LHBQNR, HBQNRX, None, UGTYIY, None, None, SAKQXP
            ),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, QNRXCH, None, UGTYIY, None, None, SAKQXP
            ),
            NRXCHW: GeckoEnumStructAccessor(
                self.struct, NRXCHW, RXCHWD, None, UGTYIY, None, None, SAKQXP
            ),
            XCHWDA: GeckoEnumStructAccessor(
                self.struct, XCHWDA, CHWDAF, None, UGTYIY, None, None, SAKQXP
            ),
            HWDAFI: GeckoEnumStructAccessor(
                self.struct, HWDAFI, WDAFIK, None, DAFIKJ, None, None, SAKQXP
            ),
            AFIKJP: GeckoEnumStructAccessor(
                self.struct, AFIKJP, FIKJPU, None, DAFIKJ, None, None, SAKQXP
            ),
            IKJPUN: GeckoByteStructAccessor(self.struct, IKJPUN, KJPUNR, SAKQXP),
            JPUNRJ: GeckoByteStructAccessor(self.struct, JPUNRJ, PUNRJZ, SAKQXP),
            UNRJZT: GeckoByteStructAccessor(self.struct, UNRJZT, NRJZTA, SAKQXP),
            RJZTAT: GeckoByteStructAccessor(self.struct, RJZTAT, JZTATD, SAKQXP),
            ZTATDZ: GeckoByteStructAccessor(self.struct, ZTATDZ, TATDZX, SAKQXP),
            ATDZXN: GeckoByteStructAccessor(self.struct, ATDZXN, TDZXNQ, SAKQXP),
            DZXNQT: GeckoByteStructAccessor(self.struct, DZXNQT, ZXNQTM, SAKQXP),
            XNQTMF: GeckoByteStructAccessor(self.struct, XNQTMF, NQTMFZ, SAKQXP),
            QTMFZD: GeckoByteStructAccessor(self.struct, QTMFZD, TMFZDG, SAKQXP),
        }

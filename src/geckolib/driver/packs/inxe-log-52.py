#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE v52'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 56])
ACQFFT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 49])
AHEOCT = 308
AIIDNI = "".join(chr(c) for c in [50, 53, 65])
AJVDQL = "".join(chr(c) for c in [53, 79, 80])
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = 462
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
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 55])
AWBSIR = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
BDJQRJ = "".join(chr(c) for c in [80, 51, 76])
BFEGZU = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
BHZVOA = 473
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
BJEUTO = 335
BLKXSJ = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
BMJVHF = 256
BQFYLJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
BQNRXC = 345
BQSNQL = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
BSIRYX = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
BSSUHB = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
BVWVUB = "".join(chr(c) for c in [70, 117, 108, 108])
BWJYKL = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 52])
BXTIAC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
BXYBQS = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
BYGDSB = "".join(chr(c) for c in [80, 49, 72])
CBFEGZ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
CCPQIP = "".join(chr(c) for c in [67, 80, 79, 84])
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 56])
CHWDAF = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
CMCVDS = 476
CPQIPO = 274
CQBMJV = 317
CQFFTT = 295
CRTFMN = 323
CTHBSK = 303
CVDSSR = 477
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = 266
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = 448
DGKEAK = 460
DJQRJJ = "".join(chr(c) for c in [80, 52, 72])
DNIBXT = 7
DNQGVU = 329
DQLAII = "".join(
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
DSBDJQ = "".join(chr(c) for c in [80, 50, 76])
DSSRUR = 478
DUBSSU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 56])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 52])
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 273
EFXQGL = 258
EJNIBX = "".join(chr(c) for c in [105, 110, 88, 69])
EKCWAO = 264
ELHBQN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 55])
EOCTHB = 307
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 49, 57])
EUTOPH = 336
FCRTFM = "".join(chr(c) for c in [83, 79, 117, 116, 52])
FEFJTA = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FEGZUQ = "".join(chr(c) for c in [70, 85, 76, 76])
FFTTID = 296
FIKJPU = 449
FJBIAM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
FJTACC = "".join(chr(c) for c in [80, 117, 114, 103, 101])
FMNHTB = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
FTHECV = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
FTSIFJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
FWRKIN = 287
FYLJUI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
FZDGKE = 459
GDSBDJ = "".join(chr(c) for c in [80, 50, 72])
GETIXQ = 466
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 51])
GQPLSP = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
GTYIYW = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
GVUNXN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
GYOUSP = 281
GZUQEX = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
HBQNRX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
HBSKSO = 304
HBVWVU = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
HBXIBH = 471
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = 260
HUGTYI = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
HUOJRJ = "".join(chr(c) for c in [76, 79, 87])
HWDAFI = 348
HXEKVK = "".join(chr(c) for c in [52, 56, 75])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 54])
IACQFF = 294
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
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 53])
IBXTIA = 291
IBXYBQ = "".join(chr(c) for c in [68, 74, 83, 52])
ICXQIE = 2
IDUBSS = 299
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = 351
IGYOUS = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 51])
IIDNIB = "".join(chr(c) for c in [51, 48, 65])
IJUGSE = 341
IKFWRK = 285
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 50])
ILXWAJ = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
INEJNI = 289
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
IRYXBQ = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
IUXFEF = 271
IVDNQG = 328
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 50, 48])
IYWSKW = 325
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
JEUTOP = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
JHIUSO = "".join(chr(c) for c in [80, 53])
JIGYOU = 280
JJVYFC = "".join(chr(c) for c in [83, 79, 117, 116, 50])
JMAOAW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JMCBFE = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
JNIBXY = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 51])
JQRJJJ = "".join(chr(c) for c in [80, 52, 76])
JRJHIU = "".join(chr(c) for c in [80, 51])
JTACCP = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
JUGSEL = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
JUIKFW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
JUTYEK = "".join(chr(c) for c in [78, 69, 87])
JVDQLA = "".join(chr(c) for c in [51, 79, 80])
JVHFTH = 319
JVYFCR = 321
JWMNZM = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
JYKLGQ = 283
JZTATD = 453
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
KEAKST = 461
KFWRKI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
KINEJN = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
KJPUNR = 450
KLGQPL = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
KMLOIJ = 333
KPHUOJ = 261
KQTDKH = 479
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 53])
KVKZIL = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
KWIVDN = 327
KXSJWM = 275
KZILXW = "".join(chr(c) for c in [67, 69])
LAIIDN = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = 284
LHBQNR = 344
LIUXFE = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
LJUIKF = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
LKXSJW = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
LNMHXE = 290
LOIJUG = 340
LRAHEO = 1
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
LSXUJU = 263
LXWAJV = "".join(chr(c) for c in [80, 50, 50])
MAOAWB = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
MCBFEG = 310
MCGETI = 465
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 50, 57])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 49, 49])
MHXEKV = "".join(chr(c) for c in [51, 50, 75])
MJIGYO = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
MJMAOA = 354
MJVHFT = "".join(chr(c) for c in [77, 101, 110, 117])
MKQTDK = 256
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
MNHTBJ = 334
MNZMJI = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
MOUNBL = 353
NBLKXS = 355
NEJNIB = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
NHTBJE = "".join(chr(c) for c in [72, 84, 82])
NIBXTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
NIBXYB = "".join(chr(c) for c in [77, 73, 65])
NKMLOI = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
NMHXEK = "".join(chr(c) for c in [49, 54, 75])
NPYYLI = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
NQGVUN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
NQJYMO = "".join(chr(c) for c in [77, 69, 68])
NQTMFZ = 457
NRJZTA = 452
NRSJMC = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
NRXCHW = 346
NXNKML = 332
NZMJIG = 279
OACMCV = 475
OAWBSI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
OCTHBS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
OIHBXI = 470
OIJUGS = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
OJRJHI = "".join(chr(c) for c in [80, 50])
OKPHUO = "".join(chr(c) for c in [80, 49])
ONPYYL = 267
OOQNRS = "".join(chr(c) for c in [79, 51])
OPHUGT = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
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
PHUGTY = 338
PHUOJR = "".join(chr(c) for c in [72, 73, 71, 72])
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
POUYNQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
PQIPOU = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
PUNRJZ = 451
PYYLIU = 268
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QFFTTI = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
QFYLJU = 315
QGLRAH = "".join(chr(c) for c in [79, 78])
QGVUNX = 330
QIEFXQ = 6
QIPOUY = 282
QJYMOU = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QLAIID = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
QNRSJM = "".join(chr(c) for c in [76, 49, 50, 48])
QNRXCH = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
QPLSPF = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
QRJJJV = "".join(chr(c) for c in [66, 76, 79])
QSNQLN = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 49, 48])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 50, 49])
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RJHIUS = "".join(chr(c) for c in [80, 52])
RJJJVY = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 53])
RKINEJ = 288
RSJMCB = 5
RTFMNH = "".join(chr(c) for c in [83, 79, 117, 116, 53])
RXCHWD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
RYXBQF = 311
SAKQXP = "".join(chr(c) for c in [76, 79])
SBDJQR = "".join(chr(c) for c in [80, 51, 72])
SELHBQ = 343
SEMCGE = 464
SIFJBI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
SJMCBF = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = 277
SKSOKP = 305
SKWIVD = "".join(chr(c) for c in [83, 79, 117, 116, 56])
SNQLNM = "".join(chr(c) for c in [105, 110, 89, 84])
SOKPHU = 306
SOOQNR = "".join(chr(c) for c in [67, 80])
SPBWJY = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
SPFTSI = 350
SRURAZ = 479
SSAKQX = 259
SSRURA = "".join(chr(c) for c in [67, 70, 71, 51, 49])
SSUHBV = 301
STSEMC = 463
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
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
TATDZX = 454
TBJEUT = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
TDZXNQ = 455
TFMNHT = 324
THBSKS = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TIDUBS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
TIXQVX = 467
TMFZDG = 458
TOPHUG = 337
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 54])
TSIFJB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
TTIDUB = 297
TYIYWS = 349
UBSSUH = 300
UBYGDS = "".join(chr(c) for c in [78, 65])
UGSELH = 342
UGTYIY = 339
UHBVWV = 316
UIKFWR = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
UJUTYE = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UNBLKX = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 52])
UNXNKM = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
UQEXLS = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
URAZMK = "".join(chr(c) for c in [76, 73])
USOOQN = "".join(chr(c) for c in [66, 76])
USPBWJ = 352
UTOPHU = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
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
VDNQGV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 51, 48])
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VKZILX = "".join(chr(c) for c in [85, 76])
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 55])
VUBYGD = 320
VUNXNK = 331
VXOIHB = 469
VYFCRT = "".join(chr(c) for c in [83, 79, 117, 116, 51])
WAJVDQ = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
WAONPY = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
WBSIRY = 309
WDAFIK = "".join(chr(c) for c in [67, 70, 71, 48])
WIVDNQ = "".join(chr(c) for c in [83, 79, 117, 116, 57])
WJYKLG = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
WRKINE = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
WSKWIV = 326
WVUBYG = "".join(chr(c) for c in [83, 79, 117, 116, 49])
XBQFYL = 314
XCHWDA = 347
XEKVKZ = "".join(chr(c) for c in [54, 52, 75])
XFEFJT = 272
XIBHZV = 472
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
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 57])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 50, 50])
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = 468
XSJWMN = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
XTIACQ = 293
XUJUTY = "".join(chr(c) for c in [83, 84, 79, 80])
XYBQSN = "".join(chr(c) for c in [105, 110, 88, 77])
YBQSNQ = "".join(chr(c) for c in [75, 54, 48, 48])
YEKCWA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YFCRTF = 322
YGDSBD = "".join(chr(c) for c in [80, 49, 76])
YIYWSK = "".join(chr(c) for c in [83, 79, 117, 116, 54])
YKLGQP = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
YLIUXF = 270
YLJUIK = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
YMOUNB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
YNQJYM = "".join(chr(c) for c in [78, 79])
YOUSPB = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
YPIPIV = 257
YWSKWI = "".join(chr(c) for c in [83, 79, 117, 116, 55])
YXBQFY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
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
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49, 50])
ZMJIGY = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
ZMKQTD = 52
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 54])
ZUQEXL = 262
ZVOACM = 474
ZXNQTM = 456
AZMKQT = [
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
EGZUQE = [CBFEGZ, BFEGZU, FEGZUQ]
EKVKZI = [NMHXEK, MHXEKV, HXEKVK, XEKVKZ]
EXLSXU = [UQEXLS, QEXLSX]
FXQGLR = [IVLASS, AKQXPI]
GLRAHE = [IVLASS, QGLRAH]
HTBJEU = [
    UBYGDS,
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
    NHTBJE,
]
IDNIBX = [AIIDNI, IIDNIB]
IUSOOQ = [IVLASS, PHUOJR]
JJJVYF = [
    UBYGDS,
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    JHIUSO,
    QRJJJV,
    SOOQNR,
    OOQNRS,
    QNRSJM,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    RJJJVY,
]
JYMOUN = [YNQJYM, SAKQXP, NQJYMO, AKQXPI, QJYMOU]
KQXPIC = [IVLASS, SAKQXP, AKQXPI]
NQLNMH = [
    NEJNIB,
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
]
RAZMKQ = [
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
    URAZMK,
]
RURAZM = []
SIRYXB = [HFTHEC, BSIRYX, BSIRYX, BSIRYX]
TYEKCW = [SXUJUT, XUJUTY, UJUTYE, JUTYEK, UTYEKC]
UOJRJH = [IVLASS, PHUOJR, HUOJRJ]
VDQLAI = [AJVDQL, JVDQLA]
VLASSA = [PIPIVL, IPIVLA, PIVLAS, IVLASS]
VWVUBY = [HBVWVU, BVWVUB]
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
XNKMLO = [
    UBYGDS,
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
XWAJVD = [USOOQN, LXWAJV]
ZILXWA = [VKZILX, KZILXW]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return ZMKQTD

    @property
    def begin(self):
        return MKQTDK

    @property
    def end(self):
        return KQTDKH

    @property
    def all_device_keys(self):
        return RAZMKQ

    @property
    def user_demand_keys(self):
        return AZMKQT

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
            IRYXBQ: GeckoWordStructAccessor(self.struct, IRYXBQ, RYXBQF, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, XBQFYL, QXPICX, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, QFYLJU, QXPICX, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, QFYLJU, LRAHEO, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, IFJBIA, QXPICX, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, IFJBIA, LRAHEO, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, IFJBIA, XPICXQ, None),
            UIKFWR: GeckoWordStructAccessor(self.struct, UIKFWR, IKFWRK, None),
            KFWRKI: GeckoByteStructAccessor(self.struct, KFWRKI, FWRKIN, None),
            WRKINE: GeckoByteStructAccessor(self.struct, WRKINE, RKINEJ, None),
            KINEJN: GeckoEnumStructAccessor(
                self.struct, KINEJN, INEJNI, None, NQLNMH, None, None, None
            ),
            QLNMHX: GeckoEnumStructAccessor(
                self.struct, QLNMHX, LNMHXE, QXPICX, EKVKZI, None, XPICXQ, None
            ),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, LNMHXE, ICXQIE, ZILXWA, None, ICXQIE, None
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, LNMHXE, OQNRSJ, XWAJVD, None, ICXQIE, None
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, LNMHXE, XPICXQ, VDQLAI, None, ICXQIE, None
            ),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, LNMHXE, RSJMCB, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, LNMHXE, QIEFXQ, None),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, LNMHXE, DNIBXT, IDNIBX, None, ICXQIE, None
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
                self.struct, SUHBVW, UHBVWV, None, VWVUBY, None, ICXQIE, LASSAK
            ),
            WVUBYG: GeckoEnumStructAccessor(
                self.struct, WVUBYG, VUBYGD, None, JJJVYF, None, None, LASSAK
            ),
            JJVYFC: GeckoEnumStructAccessor(
                self.struct, JJVYFC, JVYFCR, None, JJJVYF, None, None, LASSAK
            ),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, YFCRTF, None, JJJVYF, None, None, LASSAK
            ),
            FCRTFM: GeckoEnumStructAccessor(
                self.struct, FCRTFM, CRTFMN, None, JJJVYF, None, None, LASSAK
            ),
            RTFMNH: GeckoEnumStructAccessor(
                self.struct, RTFMNH, TFMNHT, None, JJJVYF, None, None, LASSAK
            ),
            FMNHTB: GeckoEnumStructAccessor(
                self.struct, FMNHTB, MNHTBJ, None, HTBJEU, None, None, LASSAK
            ),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, LASSAK),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, LASSAK),
            UTOPHU: GeckoByteStructAccessor(self.struct, UTOPHU, TOPHUG, LASSAK),
            OPHUGT: GeckoByteStructAccessor(self.struct, OPHUGT, PHUGTY, LASSAK),
            HUGTYI: GeckoByteStructAccessor(self.struct, HUGTYI, UGTYIY, LASSAK),
            GTYIYW: GeckoByteStructAccessor(self.struct, GTYIYW, TYIYWS, LASSAK),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, JJJVYF, None, None, LASSAK
            ),
            YWSKWI: GeckoEnumStructAccessor(
                self.struct, YWSKWI, WSKWIV, None, JJJVYF, None, None, LASSAK
            ),
            SKWIVD: GeckoEnumStructAccessor(
                self.struct, SKWIVD, KWIVDN, None, JJJVYF, None, None, LASSAK
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, JJJVYF, None, None, LASSAK
            ),
            VDNQGV: GeckoEnumStructAccessor(
                self.struct, VDNQGV, DNQGVU, None, JJJVYF, None, None, LASSAK
            ),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, QGVUNX, None, JJJVYF, None, None, LASSAK
            ),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, JJJVYF, None, None, LASSAK
            ),
            UNXNKM: GeckoEnumStructAccessor(
                self.struct, UNXNKM, NXNKML, None, XNKMLO, None, None, LASSAK
            ),
            NKMLOI: GeckoEnumStructAccessor(
                self.struct, NKMLOI, KMLOIJ, None, XNKMLO, None, None, LASSAK
            ),
            MLOIJU: GeckoByteStructAccessor(self.struct, MLOIJU, LOIJUG, LASSAK),
            OIJUGS: GeckoByteStructAccessor(self.struct, OIJUGS, IJUGSE, LASSAK),
            JUGSEL: GeckoByteStructAccessor(self.struct, JUGSEL, UGSELH, LASSAK),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, LASSAK),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, LASSAK),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, LASSAK),
            QNRXCH: GeckoByteStructAccessor(self.struct, QNRXCH, NRXCHW, LASSAK),
            RXCHWD: GeckoByteStructAccessor(self.struct, RXCHWD, XCHWDA, LASSAK),
            CHWDAF: GeckoByteStructAccessor(self.struct, CHWDAF, HWDAFI, LASSAK),
        }

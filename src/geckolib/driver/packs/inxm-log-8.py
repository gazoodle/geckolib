#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v8'
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
ACCPQI = 355
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 49])
ACQFFT = "".join(chr(c) for c in [82, 104, 67, 111, 109, 109, 69, 114, 114])
AFIKJP = "".join(chr(c) for c in [75, 52, 48, 48])
AHEOCT = 294
AIIDNI = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
AJVDQL = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
AKQXPI = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101, 83, 105, 103, 110]
)
AKSTSE = 455
AMJMAO = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
AOAWBS = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
AONPYY = 359
ASSAKQ = "".join(chr(c) for c in [75, 54, 48, 48, 85, 112, 108, 111, 97, 100])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 48])
AWBSIR = "".join(
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
AZMKQT = 474
BDFSRO = 256
BDJQRJ = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
BEKBDF = "".join(chr(c) for c in [76, 73])
BHZVOA = 466
BIAMJM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
BJEUTO = "".join(chr(c) for c in [54, 52, 75])
BLKXSJ = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121])
BMJVHF = 263
BQFYLJ = "".join(chr(c) for c in [67, 80, 79, 84])
BQNRXC = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 118])
BQSNQL = 271
BSIRYX = "".join(chr(c) for c in [67, 108, 101, 97, 110])
BSKSOK = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
BSSUHB = "".join(chr(c) for c in [82, 104, 83, 87, 84, 114, 105, 97, 99, 79, 72])
BVWVUB = "".join(
    chr(c)
    for c in [82, 104, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101, 100]
)
BWJYKL = "".join(
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
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 49, 55])
BXTIAC = 259
BXYBQS = 364
BYGDSB = 317
CBFEGZ = "".join(chr(c) for c in [79, 78])
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 49])
CHWDAF = 347
CMCVDS = 469
CPQIPO = "".join(chr(c) for c in [66, 76])
CQBMJV = 261
CQFFTT = "".join(
    chr(c)
    for c in [82, 104, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
CRTFMN = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
CTHBSK = 298
CVDSSR = 470
CVYYPI = "".join(chr(c) for c in [72, 50])
CWAONP = 358
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 50, 65, 82, 101, 97, 100])
DAFIKJ = "".join(chr(c) for c in [75, 50, 48, 48])
DFSROG = 479
DGKEAK = 453
DJQRJJ = 321
DKHTZB = 477
DNIBXT = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
DNQGVU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
DQLAII = "".join(chr(c) for c in [114, 72, 73, 100])
DSBDJQ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
DSSRUR = 471
DUBSSU = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 80, 114])
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 49])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 55])
ECVYYP = "".join(chr(c) for c in [72, 49])
EFJTAC = "".join(chr(c) for c in [80, 51])
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 51, 65, 82, 101, 97, 100])
EGZUQE = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
EJNIBX = 270
EKCWAO = 304
EKVKZI = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
ELHBQN = 341
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 48])
EOCTHB = 296
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 49, 50])
EUTOPH = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
FCRTFM = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
FEFJTA = "".join(chr(c) for c in [80, 50])
FEGZUQ = 8
FFTTID = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121, 69, 114, 114])
FIKJPU = "".join(chr(c) for c in [75, 56, 53])
FJBIAM = 311
FJTACC = "".join(chr(c) for c in [80, 52])
FMNHTB = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
FTHECV = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTSIFJ = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
FTTIDU = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
FXQGLR = 288
FYLJUI = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
FZDGKE = 452
GDSBDJ = 319
GETIXQ = 459
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 54])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 53, 65, 82, 101, 97, 100])
GQPLSP = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
GSELHB = 339
GTYIYW = 327
GVUNXN = 333
GZUQEX = 1
HBQNRX = 343
HBSKSO = 362
HBVWVU = "".join(chr(c) for c in [82, 104, 72, 87, 75, 105, 110])
HBXIBH = 464
HECVYY = "".join(chr(c) for c in [83, 50])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 55, 65, 82, 101, 97, 100])
HFTHEC = 353
HIUSOO = 2
HTBJEU = "".join(chr(c) for c in [51, 50, 75])
HTZBBE = 478
HUGTYI = 325
HUOJRJ = "".join(chr(c) for c in [85, 100, 80, 49])
HWDAFI = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
HXEKVK = 278
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 49, 57])
IACQFF = 365
IAMJMA = 313
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 49, 56])
IBXTIA = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
IBXYBQ = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
ICXQIE = 282
IDNIBX = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IDUBSS = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
IEFXQG = 286
IFJBIA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
IGYOUS = "".join(chr(c) for c in [70, 85, 76, 76])
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 49, 54])
IIDNIB = 258
IJUGSE = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 108])
IKFWRK = "".join(chr(c) for c in [78, 79])
IKJPUN = "".join(chr(c) for c in [75, 56])
ILXWAJ = "".join(
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
INEJNI = 265
IPIVLA = "".join(chr(c) for c in [76, 101, 97, 114, 110, 105, 110, 103])
IPOUYN = 3
IRYXBQ = "".join(chr(c) for c in [80, 117, 114, 103, 101])
IUSOOQ = 4
IUXFEF = "".join(chr(c) for c in [72, 73, 71, 72])
IVDNQG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
IVLASS = "".join(chr(c) for c in [80, 104, 97, 115, 101, 83, 101, 108, 101, 99, 116])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 49, 51])
IYWSKW = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
JBIAMJ = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
JHIUSO = 14
JIGYOU = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
JJJVYF = "".join(chr(c) for c in [77, 73, 65])
JJVYFC = "".join(chr(c) for c in [68, 74, 83, 52])
JMAOAW = "".join(
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
JMCBFE = 9
JNIBXY = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
JPUNRJ = "".join(chr(c) for c in [75, 53])
JQRJJJ = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
JRJHIU = "".join(chr(c) for c in [72, 73])
JTACCP = 6
JUGSEL = 338
JUIKFW = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
JUTYEK = "".join(chr(c) for c in [85, 100, 83, 112, 107, 114, 76, 105, 102, 116])
JVDQLA = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
JVHFTH = 256
JVYFCR = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
JWMNZM = 305
JYKLGQ = "".join(chr(c) for c in [73, 68, 76, 69])
JYMOUN = "".join(chr(c) for c in [85, 80])
JZTATD = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
KCWAON = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KEAKST = 454
KFWRKI = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
KHTZBB = "".join(chr(c) for c in [67, 70, 71, 51, 48])
KINEJN = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
KJPUNR = "".join(chr(c) for c in [75, 52])
KLGQPL = "".join(chr(c) for c in [83, 84, 65, 82, 84])
KMLOIJ = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 73, 68])
KQTDKH = "".join(chr(c) for c in [67, 70, 71, 50, 56])
KQXPIC = 300
KSOKPH = "".join(chr(c) for c in [68, 82, 65, 73, 78])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 56])
KVKZIL = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
KWIVDN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
KXSJWM = "".join(chr(c) for c in [86, 115, 112, 49, 70, 114, 111, 110, 116])
KZILXW = "".join(
    chr(c) for c in [70, 114, 101, 113, 68, 101, 116, 101, 99, 69, 114, 114]
)
LAIIDN = 260
LASSAK = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
LGQPLS = "".join(chr(c) for c in [78, 69, 87])
LHBQNR = "".join(chr(c) for c in [75, 54, 48, 48, 73, 68])
LIUXFE = 356
LJUIKF = 267
LKXSJW = 274
LNMHXE = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
LOIJUG = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 118])
LRAHEO = 292
LSPFTS = 308
LSXUJU = "".join(chr(c) for c in [85, 100, 86, 97, 108, 118, 101])
LXWAJV = "".join(
    chr(c) for c in [76, 101, 97, 114, 110, 80, 104, 97, 115, 101, 69, 114, 114]
)
MAOAWB = 350
MCBFEG = "".join(chr(c) for c in [85, 100, 66, 76])
MCGETI = 458
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 50, 50])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 52])
MHXEKV = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
MJIGYO = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
MJMAOA = 314
MJVHFT = "".join(chr(c) for c in [72, 111, 117, 114, 115])
MKQTDK = 475
MLOIJU = 335
MNHTBJ = 322
MNZMJI = 302
MOUNBL = "".join(chr(c) for c in [83, 112, 107, 114, 76, 105, 102, 116])
NBLKXS = "".join(chr(c) for c in [86, 97, 108, 118, 101])
NEJNIB = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
NHTBJE = "".join(chr(c) for c in [49, 54, 75])
NIBXTI = 257
NIBXYB = 349
NMHXEK = 277
NPYYLI = 360
NQGVUN = 332
NQJYMO = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
NQLNMH = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
NQTMFZ = 450
NRJZTA = "".join(chr(c) for c in [75, 56, 48, 48])
NRSJMC = "".join(chr(c) for c in [85, 100, 80, 52])
NRXCHW = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 108])
NXNKML = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
NZMJIG = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
OACMCV = 468
OAWBSI = 351
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 82, 101, 97, 100])
OIHBXI = 463
OIJUGS = 337
OJRJHI = "".join(chr(c) for c in [76, 79])
OKPHUO = "".join(chr(c) for c in [79, 70, 70])
ONPYYL = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
OOQNRS = "".join(chr(c) for c in [85, 100, 80, 51])
OUNBLK = "".join(chr(c) for c in [83, 97, 110, 105])
OUSPBW = 348
OUYNQJ = "".join(chr(c) for c in [70, 65, 78])
PFTSIF = 316
PHUGTY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
PHUOJR = "".join(chr(c) for c in [65, 76, 76])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 49, 66, 82, 101, 97, 100])
PIPIVL = "".join(chr(c) for c in [76, 101, 97, 114, 110, 70, 97, 105, 108])
PIVLAS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 108, 101, 99, 116]
)
PLSPFT = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
POUYNQ = "".join(chr(c) for c in [76, 49, 50, 48])
PQIPOU = "".join(chr(c) for c in [67, 80])
PUNRJZ = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
PYYLIU = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
QBMJVH = "".join(chr(c) for c in [82, 104, 84, 114, 105, 97, 99, 84, 101, 109, 112])
QEXLSX = "".join(chr(c) for c in [77, 69, 68])
QFFTTI = "".join(chr(c) for c in [82, 104, 76, 111, 119, 70, 108, 111])
QFYLJU = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
QGLRAH = 290
QGVUNX = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 66, 82, 101, 97, 100])
QIPOUY = "".join(chr(c) for c in [79, 51])
QJYMOU = "".join(chr(c) for c in [68, 79, 87, 78])
QLAIID = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
QLNMHX = "".join(
    chr(c) for c in [75, 105, 110, 80, 117, 114, 103, 101, 65, 99, 116, 105, 118, 101]
)
QNRSJM = 11
QNRXCH = 345
QRJJJV = "".join(chr(c) for c in [105, 110, 88, 69])
QSNQLN = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
QTDKHT = 476
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 51])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 49, 52])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 49, 65, 82, 101, 97, 100])
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 54, 65, 82, 101, 97, 100])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 50, 54])
RJJJVY = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
RJZTAT = "".join(chr(c) for c in [])
RKINEJ = 272
RSJMCB = 10
RTFMNH = "".join(chr(c) for c in [105, 110, 89, 84])
RURAZM = "".join(chr(c) for c in [67, 70, 71, 50, 53])
RXCHWD = 346
RYXBQF = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
SBDJQR = 320
SELHBQ = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 70, 117, 108, 108]
)
SEMCGE = 457
SIFJBI = 310
SIRYXB = 269
SJMCBF = "".join(chr(c) for c in [85, 100, 80, 53])
SJWMNZ = "".join(chr(c) for c in [86, 115, 112, 49, 77, 105, 110])
SKSOKP = "".join(chr(c) for c in [81, 85, 73, 69, 84])
SKWIVD = 323
SNQLNM = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
SOKPHU = "".join(chr(c) for c in [83, 79, 65, 75])
SOOQNR = 12
SPBWJY = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
SPFTSI = "".join(
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
SRURAZ = 472
SSAKQX = "".join(chr(c) for c in [80, 111, 119, 101, 114, 117, 112])
SSRURA = "".join(chr(c) for c in [67, 70, 71, 50, 52])
SSUHBV = "".join(chr(c) for c in [82, 104, 72, 119, 84, 114, 105, 97, 99, 79, 72])
STSEMC = 456
SUHBVW = "".join(chr(c) for c in [82, 104, 72, 114, 75, 105, 110])
SXUJUT = 7
TACCPQ = "".join(chr(c) for c in [80, 53])
TBJEUT = "".join(chr(c) for c in [52, 56, 75])
TDKHTZ = "".join(chr(c) for c in [67, 70, 71, 50, 57])
TDZXNQ = 448
THBSKS = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
THECVY = "".join(chr(c) for c in [83, 49])
TIACQF = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
TIDUBS = "".join(chr(c) for c in [82, 104, 72, 114, 72, 76])
TIXQVX = 460
TMFZDG = 451
TOPHUG = "".join(chr(c) for c in [67, 69])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 57])
TSIFJB = "".join(
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
TTIDUB = "".join(chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 84, 101, 109, 112])
TYEKCW = 303
TYIYWS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TZBBEK = "".join(chr(c) for c in [67, 70, 71, 51, 49])
UBSSUH = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 79, 72])
UBYGDS = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
UGSELH = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 49, 75, 87]
)
UGTYIY = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
UHBVWV = "".join(chr(c) for c in [82, 104, 83, 119, 75, 105, 110, 84, 101, 109, 112])
UIKFWR = 268
UJUTYE = 5
UNBLKX = "".join(chr(c) for c in [79, 110, 122, 101, 110])
UNRJZT = "".join(chr(c) for c in [75, 49, 48, 48])
UNXNKM = 357
UOJRJH = 275
UQEXLS = 306
URAZMK = 473
USOOQN = "".join(chr(c) for c in [85, 100, 80, 50])
USPBWJ = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
UTOPHU = "".join(chr(c) for c in [85, 76])
UTYEKC = "".join(chr(c) for c in [85, 100, 86, 83, 80, 49])
UXFEFJ = "".join(chr(c) for c in [76, 79, 87])
UYNQJY = "".join(chr(c) for c in [65, 108, 119, 97, 121, 79, 110])
VDNQGV = 331
VDQLAI = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 50, 51])
VHFTHE = "".join(chr(c) for c in [77, 101, 110, 117])
VKZILX = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
VLASSA = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 48])
VUBYGD = "".join(
    chr(c)
    for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
VUNXNK = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
VWVUBY = "".join(chr(c) for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107])
VXOIHB = 462
VYFCRT = "".join(chr(c) for c in [105, 110, 88, 77])
VYYPIP = "".join(chr(c) for c in [72, 51])
WAJVDQ = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
WAONPY = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
WBSIRY = 352
WDAFIK = 367
WIVDNQ = 329
WJYKLG = 307
WMNZMJ = "".join(chr(c) for c in [86, 83, 80, 51, 70, 114, 111, 110, 116])
WRKINE = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
WSKWIV = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
WVUBYG = "".join(
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
XBQFYL = "".join(
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
XCHWDA = "".join(chr(c) for c in [75, 54, 48, 48, 80, 114, 111, 116, 111, 99, 111, 108])
XEKVKZ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
XIBHZV = 465
XLSXUJ = 0
XNKMLO = "".join(chr(c) for c in [70, 117, 108, 108])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 50])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 49, 53])
XPICXQ = 280
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 52, 65, 82, 101, 97, 100])
XQIEFX = 284
XQVXOI = 461
XSJWMN = 301
XTIACQ = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
XUJUTY = "".join(chr(c) for c in [85, 100, 84, 118, 76, 105, 102, 116])
XWAJVD = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
XYBQSN = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
YBQSNQ = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
YEKCWA = "".join(chr(c) for c in [85, 100, 86, 83, 80, 51])
YFCRTF = "".join(chr(c) for c in [75, 54, 48, 48])
YGDSBD = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
YIYWSK = 328
YKLGQP = "".join(chr(c) for c in [83, 84, 79, 80])
YLIUXF = "".join(chr(c) for c in [80, 49])
YLJUIK = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
YNQJYM = 354
YOUSPB = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
YPIPIV = "".join(chr(c) for c in [70, 114])
YWSKWI = 324
YXBQFY = 279
YYLIUX = 361
YYPIPI = "".join(chr(c) for c in [72, 52])
ZBBEKB = 479
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 53])
ZILXWA = "".join(
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
ZMJIGY = 363
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 50, 55])
ZTATDZ = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
ZUQEXL = "".join(chr(c) for c in [85, 100, 76, 105])
ZVOACM = 467
ZXNQTM = 449
BBEKBD = []
BFEGZU = [OKPHUO, CBFEGZ]
CCPQIP = [OKPHUO, IUXFEF]
EKBDFS = [
    YLIUXF,
    FEFJTA,
    EFJTAC,
    FJTACC,
    TACCPQ,
    CPQIPO,
    PQIPOU,
    QIPOUY,
    POUYNQ,
    OUYNQJ,
    UYNQJY,
    NQJYMO,
    MOUNBL,
    OUNBLK,
    UNBLKX,
    NBLKXS,
    BLKXSJ,
    KXSJWM,
    SJWMNZ,
    WMNZMJ,
    NZMJIG,
    BEKBDF,
]
EXLSXU = [OKPHUO, OJRJHI, QEXLSX, JRJHIU]
FWRKIN = [IKFWRK, OJRJHI, QEXLSX, JRJHIU, KFWRKI]
GYOUSP = [MJIGYO, JIGYOU, IGYOUS]
JEUTOP = [NHTBJE, HTBJEU, TBJEUT, BJEUTO]
KBDFSR = [
    HUOJRJ,
    USOOQN,
    OOQNRS,
    NRSJMC,
    SJMCBF,
    MCBFEG,
    EGZUQE,
    ZUQEXL,
    LSXUJU,
    XUJUTY,
    JUTYEK,
    UTYEKC,
    YEKCWA,
    KCWAON,
    WAONPY,
    ONPYYL,
    PYYLIU,
]
KPHUOJ = [BSKSOK, SKSOKP, KSOKPH, SOKPHU, OKPHUO]
NKMLOI = [NXNKML, XNKMLO]
OPHUGT = [UTOPHU, TOPHUG]
OQNRSJ = [OKPHUO, JRJHIU]
PBWJYK = [USPBWJ, SPBWJY]
QPLSPF = [JYKLGQ, YKLGQP, KLGQPL, LGQPLS, GQPLSP]
RJHIUS = [OKPHUO, OJRJHI, JRJHIU]
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
TATDZX = [
    DAFIKJ,
    AFIKJP,
    FIKJPU,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    NRJZTA,
    RJZTAT,
    RJZTAT,
    RJZTAT,
    JZTATD,
    ZTATDZ,
]
TFMNHT = [
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
]
XFEFJT = [OKPHUO, IUXFEF, UXFEFJ]
YMOUNB = [QJYMOU, JYMOUN]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return FEGZUQ

    @property
    def begin(self):
        return BDFSRO

    @property
    def end(self):
        return DFSROG

    @property
    def all_device_keys(self):
        return EKBDFS

    @property
    def user_demand_keys(self):
        return KBDFSR

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
                self.struct, THBSKS, HBSKSO, None, KPHUOJ, None, None, PHUOJR
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, JHIUSO, RJHIUS, HIUSOO, IUSOOQ, PHUOJR
            ),
            USOOQN: GeckoEnumStructAccessor(
                self.struct, USOOQN, UOJRJH, SOOQNR, RJHIUS, HIUSOO, IUSOOQ, PHUOJR
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, UOJRJH, QNRSJM, OQNRSJ, HIUSOO, HIUSOO, PHUOJR
            ),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, UOJRJH, RSJMCB, OQNRSJ, HIUSOO, HIUSOO, PHUOJR
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, UOJRJH, JMCBFE, OQNRSJ, HIUSOO, HIUSOO, PHUOJR
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, UOJRJH, FEGZUQ, BFEGZU, HIUSOO, HIUSOO, PHUOJR
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, UOJRJH, GZUQEX, BFEGZU, HIUSOO, HIUSOO, PHUOJR
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, UQEXLS, XLSXUJ, EXLSXU, None, IUSOOQ, PHUOJR
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, UOJRJH, SXUJUT, BFEGZU, HIUSOO, HIUSOO, PHUOJR
            ),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, UOJRJH, UJUTYE, BFEGZU, HIUSOO, HIUSOO, PHUOJR
            ),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, UOJRJH, IUSOOQ, BFEGZU, HIUSOO, HIUSOO, PHUOJR
            ),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, PHUOJR),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, PHUOJR),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, PHUOJR),
            WAONPY: GeckoByteStructAccessor(self.struct, WAONPY, AONPYY, PHUOJR),
            ONPYYL: GeckoByteStructAccessor(self.struct, ONPYYL, NPYYLI, PHUOJR),
            PYYLIU: GeckoByteStructAccessor(self.struct, PYYLIU, YYLIUX, PHUOJR),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, XLSXUJ, XFEFJT, None, IUSOOQ, None
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, LIUXFE, HIUSOO, XFEFJT, None, IUSOOQ, None
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, LIUXFE, IUSOOQ, XFEFJT, None, IUSOOQ, None
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, LIUXFE, JTACCP, XFEFJT, None, IUSOOQ, None
            ),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, XLSXUJ, CCPQIP, None, HIUSOO, None
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, ACCPQI, GZUQEX, BFEGZU, None, HIUSOO, None
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, ACCPQI, HIUSOO, BFEGZU, None, HIUSOO, None
            ),
            QIPOUY: GeckoEnumStructAccessor(
                self.struct, QIPOUY, ACCPQI, IPOUYN, BFEGZU, None, HIUSOO, None
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, ACCPQI, IUSOOQ, BFEGZU, None, HIUSOO, None
            ),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, ACCPQI, SXUJUT, BFEGZU, None, HIUSOO, None
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, HIUSOO, BFEGZU, None, HIUSOO, None
            ),
            NQJYMO: GeckoEnumStructAccessor(
                self.struct, NQJYMO, YNQJYM, IPOUYN, YMOUNB, None, HIUSOO, None
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, YNQJYM, IUSOOQ, YMOUNB, None, HIUSOO, None
            ),
            OUNBLK: GeckoEnumStructAccessor(
                self.struct, OUNBLK, YNQJYM, UJUTYE, BFEGZU, None, HIUSOO, None
            ),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, YNQJYM, JTACCP, BFEGZU, None, HIUSOO, None
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, YNQJYM, SXUJUT, BFEGZU, None, HIUSOO, None
            ),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, None),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, None),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, None),
            WMNZMJ: GeckoByteStructAccessor(self.struct, WMNZMJ, MNZMJI, None),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, ZMJIGY, None, GYOUSP, None, None, PHUOJR
            ),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, XLSXUJ, PBWJYK, None, HIUSOO, PHUOJR
            ),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, QPLSPF, None, None, PHUOJR
            ),
            PLSPFT: GeckoTimeStructAccessor(self.struct, PLSPFT, LSPFTS, PHUOJR),
            SPFTSI: GeckoByteStructAccessor(self.struct, SPFTSI, PFTSIF, PHUOJR),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, OUSPBW, GZUQEX, PBWJYK, None, HIUSOO, PHUOJR
            ),
            TSIFJB: GeckoEnumStructAccessor(
                self.struct, TSIFJB, SIFJBI, None, QPLSPF, None, None, PHUOJR
            ),
            IFJBIA: GeckoTimeStructAccessor(self.struct, IFJBIA, FJBIAM, PHUOJR),
            JBIAMJ: GeckoEnumStructAccessor(
                self.struct, JBIAMJ, OUSPBW, HIUSOO, PBWJYK, None, HIUSOO, PHUOJR
            ),
            BIAMJM: GeckoEnumStructAccessor(
                self.struct, BIAMJM, IAMJMA, None, QPLSPF, None, None, PHUOJR
            ),
            AMJMAO: GeckoTimeStructAccessor(self.struct, AMJMAO, MJMAOA, PHUOJR),
            JMAOAW: GeckoByteStructAccessor(self.struct, JMAOAW, MAOAWB, PHUOJR),
            AOAWBS: GeckoByteStructAccessor(self.struct, AOAWBS, OAWBSI, PHUOJR),
            AWBSIR: GeckoByteStructAccessor(self.struct, AWBSIR, WBSIRY, PHUOJR),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, SIRYXB, UJUTYE, None),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, SIRYXB, SXUJUT, None),
            RYXBQF: GeckoBoolStructAccessor(self.struct, RYXBQF, YXBQFY, IPOUYN, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, YXBQFY, XLSXUJ, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, YXBQFY, GZUQEX, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, SIRYXB, HIUSOO, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, SIRYXB, IPOUYN, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, LJUIKF, None, None),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, UIKFWR, None, FWRKIN, None, None, None
            ),
            WRKINE: GeckoTempStructAccessor(self.struct, WRKINE, RKINEJ, None),
            KINEJN: GeckoTempStructAccessor(self.struct, KINEJN, INEJNI, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, EJNIBX, SXUJUT, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, NIBXYB, GZUQEX, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BXYBQS, XLSXUJ, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, SIRYXB, XLSXUJ, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, BQSNQL, HIUSOO, None),
            QSNQLN: GeckoBoolStructAccessor(
                self.struct, QSNQLN, BQSNQL, XLSXUJ, PHUOJR
            ),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, SIRYXB, GZUQEX, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, EJNIBX, JTACCP, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, EJNIBX, UJUTYE, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, NMHXEK, UJUTYE, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, HXEKVK, IPOUYN, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, HXEKVK, HIUSOO, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, YXBQFY, IUSOOQ, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, HXEKVK, IUSOOQ, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, HXEKVK, GZUQEX, None),
            KZILXW: GeckoBoolStructAccessor(self.struct, KZILXW, NMHXEK, JTACCP, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, NMHXEK, IUSOOQ, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, NMHXEK, IPOUYN, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, NMHXEK, HIUSOO, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, NMHXEK, GZUQEX, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, NMHXEK, XLSXUJ, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, HXEKVK, SXUJUT, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, HXEKVK, JTACCP, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, HXEKVK, UJUTYE, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, HXEKVK, XLSXUJ, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, LAIIDN, IPOUYN, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, IIDNIB, HIUSOO, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, IIDNIB, GZUQEX, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, NIBXTI, HIUSOO, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, BXTIAC, HIUSOO, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, IIDNIB, IUSOOQ, None),
            TIACQF: GeckoWordStructAccessor(self.struct, TIACQF, IACQFF, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, NIBXTI, SXUJUT, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, NIBXTI, IPOUYN, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, NIBXTI, XLSXUJ, None),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, IIDNIB, SXUJUT, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, IIDNIB, JTACCP, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, IIDNIB, UJUTYE, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, IIDNIB, IPOUYN, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, IIDNIB, XLSXUJ, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, BXTIAC, SXUJUT, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, BXTIAC, JTACCP, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, BXTIAC, UJUTYE, None),
            SSUHBV: GeckoBoolStructAccessor(self.struct, SSUHBV, BXTIAC, IUSOOQ, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, BXTIAC, IPOUYN, None),
            UHBVWV: GeckoBoolStructAccessor(self.struct, UHBVWV, BXTIAC, GZUQEX, None),
            HBVWVU: GeckoBoolStructAccessor(self.struct, HBVWVU, BXTIAC, XLSXUJ, None),
            BVWVUB: GeckoBoolStructAccessor(self.struct, BVWVUB, LAIIDN, IUSOOQ, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, LAIIDN, HIUSOO, None),
            WVUBYG: GeckoBoolStructAccessor(self.struct, WVUBYG, LAIIDN, GZUQEX, None),
            VUBYGD: GeckoBoolStructAccessor(self.struct, VUBYGD, LAIIDN, XLSXUJ, None),
            UBYGDS: GeckoWordStructAccessor(self.struct, UBYGDS, BYGDSB, None),
            YGDSBD: GeckoByteStructAccessor(self.struct, YGDSBD, GDSBDJ, None),
            DSBDJQ: GeckoByteStructAccessor(self.struct, DSBDJQ, SBDJQR, None),
            BDJQRJ: GeckoEnumStructAccessor(
                self.struct, BDJQRJ, DJQRJJ, None, TFMNHT, None, None, None
            ),
            FMNHTB: GeckoEnumStructAccessor(
                self.struct, FMNHTB, MNHTBJ, XLSXUJ, JEUTOP, None, IUSOOQ, None
            ),
            EUTOPH: GeckoEnumStructAccessor(
                self.struct, EUTOPH, MNHTBJ, HIUSOO, OPHUGT, None, HIUSOO, None
            ),
            PHUGTY: GeckoWordStructAccessor(self.struct, PHUGTY, HUGTYI, None),
            UGTYIY: GeckoByteStructAccessor(self.struct, UGTYIY, GTYIYW, None),
            TYIYWS: GeckoByteStructAccessor(self.struct, TYIYWS, YIYWSK, None),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, None),
            WSKWIV: GeckoByteStructAccessor(self.struct, WSKWIV, SKWIVD, None),
            KWIVDN: GeckoWordStructAccessor(self.struct, KWIVDN, WIVDNQ, None),
            IVDNQG: GeckoByteStructAccessor(self.struct, IVDNQG, VDNQGV, None),
            DNQGVU: GeckoByteStructAccessor(self.struct, DNQGVU, NQGVUN, None),
            QGVUNX: GeckoWordStructAccessor(self.struct, QGVUNX, GVUNXN, None),
            VUNXNK: GeckoEnumStructAccessor(
                self.struct, VUNXNK, UNXNKM, None, NKMLOI, None, HIUSOO, PHUOJR
            ),
            KMLOIJ: GeckoWordStructAccessor(self.struct, KMLOIJ, MLOIJU, None),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, None),
            IJUGSE: GeckoByteStructAccessor(self.struct, IJUGSE, JUGSEL, None),
            UGSELH: GeckoWordStructAccessor(self.struct, UGSELH, GSELHB, None),
            SELHBQ: GeckoWordStructAccessor(self.struct, SELHBQ, ELHBQN, None),
            HWDAFI: GeckoEnumStructAccessor(
                self.struct, HWDAFI, WDAFIK, None, TATDZX, None, None, None
            ),
        }

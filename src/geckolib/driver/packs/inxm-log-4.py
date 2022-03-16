#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v4'
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
ACQFFT = "".join(
    chr(c)
    for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 49, 49])
AHEOCT = 294
AIIDNI = "".join(chr(c) for c in [82, 104, 72, 119, 84, 114, 105, 97, 99, 79, 72])
AJVDQL = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
AKQXPI = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101, 83, 105, 103, 110]
)
AKSTSE = 472
AMJMAO = "".join(chr(c) for c in [67, 80, 79, 84])
AOAWBS = 268
AONPYY = "".join(chr(c) for c in [80, 51])
ASSAKQ = "".join(chr(c) for c in [75, 54, 48, 48, 85, 112, 108, 111, 97, 100])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 49, 55])
AWBSIR = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
BDJQRJ = "".join(chr(c) for c in [54, 52, 75])
BFEGZU = "".join(chr(c) for c in [78, 65])
BIAMJM = 279
BJEUTO = 331
BLKXSJ = 348
BMJVHF = 263
BQFYLJ = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
BQNRXC = 454
BQSNQL = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
BSIRYX = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
BSKSOK = "".join(chr(c) for c in [79, 70, 70])
BSSUHB = "".join(chr(c) for c in [105, 110, 88, 69])
BVWVUB = "".join(chr(c) for c in [105, 110, 88, 77])
BWJYKL = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
BXIBHZ = 256
BXTIAC = 260
BXYBQS = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
BYGDSB = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
CBFEGZ = "".join(chr(c) for c in [70, 73, 88])
CCPQIP = "".join(chr(c) for c in [65, 108, 119, 97, 121, 79, 110])
CGETIX = "".join(chr(c) for c in [67, 70, 71, 50, 56])
CHWDAF = "".join(chr(c) for c in [67, 70, 71, 57])
CPQIPO = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
CQBMJV = 261
CQFFTT = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
CRTFMN = 325
CTHBSK = 298
CVYYPI = "".join(chr(c) for c in [72, 50])
CXQIEF = "".join(chr(c) for c in [79, 85, 84, 50, 65, 82, 101, 97, 100])
DAFIKJ = 458
DGKEAK = 470
DNIBXT = "".join(chr(c) for c in [82, 104, 83, 119, 75, 105, 110, 84, 101, 109, 112])
DNQGVU = "".join(chr(c) for c in [75, 54, 48, 48, 73, 68])
DQLAII = 259
DSBDJQ = "".join(chr(c) for c in [51, 50, 75])
DUBSSU = 321
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 49, 56])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 50, 52])
ECVYYP = "".join(chr(c) for c in [72, 49])
EFJTAC = "".join(chr(c) for c in [70, 65, 78])
EFXQGL = "".join(chr(c) for c in [79, 85, 84, 51, 65, 82, 101, 97, 100])
EJNIBX = "".join(
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
EKCWAO = "".join(chr(c) for c in [72, 73, 71, 72])
EKVKZI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
ELHBQN = "".join(chr(c) for c in [67, 70, 71, 53])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 50, 55])
EOCTHB = 296
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 50, 57])
EUTOPH = 332
EXLSXU = "".join(chr(c) for c in [85, 100, 76, 105])
FCRTFM = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
FEFJTA = "".join(chr(c) for c in [76, 49, 50, 48])
FEGZUQ = "".join(chr(c) for c in [83, 67, 65, 78])
FFTTID = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
FIKJPU = 459
FJBIAM = "".join(
    chr(c) for c in [67, 108, 101, 97, 110, 83, 117, 115, 112, 101, 110, 100, 101, 100]
)
FJTACC = 7
FMNHTB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
FTHECV = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTSIFJ = 352
FTTIDU = 319
FWRKIN = 271
FXQGLR = 288
FYLJUI = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
FZDGKE = 469
GDSBDJ = "".join(chr(c) for c in [49, 54, 75])
GETIXQ = 476
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 50, 51])
GLRAHE = "".join(chr(c) for c in [79, 85, 84, 53, 65, 82, 101, 97, 100])
GQPLSP = 314
GSELHB = "".join(chr(c) for c in [67, 70, 71, 52])
GVUNXN = 345
GYOUSP = 308
GZUQEX = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [67, 70, 71, 54])
HBSKSO = 275
HBVWVU = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
HECVYY = "".join(chr(c) for c in [83, 50])
HEOCTH = "".join(chr(c) for c in [79, 85, 84, 55, 65, 82, 101, 97, 100])
HFTHEC = 353
HIUSOO = "".join(chr(c) for c in [85, 100, 80, 52])
HTBJEU = 329
HUGTYI = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
HUOJRJ = "".join(chr(c) for c in [65, 76, 76])
HWDAFI = 457
HXEKVK = 257
IACQFF = "".join(
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
IAMJMA = "".join(chr(c) for c in [70, 105, 108, 116, 79, 84])
IBXTIA = "".join(
    chr(c)
    for c in [82, 104, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101, 100]
)
IBXYBQ = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
ICXQIE = 282
IDNIBX = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
IDUBSS = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
IEFXQG = 286
IFJBIA = "".join(chr(c) for c in [67, 108, 101, 97, 110])
IGYOUS = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
IIDNIB = "".join(chr(c) for c in [82, 104, 72, 114, 75, 105, 110])
IJUGSE = 450
IKFWRK = "".join(
    chr(c) for c in [75, 105, 110, 80, 117, 114, 103, 101, 65, 99, 116, 105, 118, 101]
)
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 49, 50])
ILXWAJ = "".join(chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 84, 101, 109, 112])
INEJNI = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
IPIVLA = "".join(chr(c) for c in [76, 101, 97, 114, 110, 105, 110, 103])
IRYXBQ = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
IUSOOQ = 10
IUXFEF = "".join(chr(c) for c in [67, 80])
IVDNQG = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 70, 117, 108, 108]
)
IVLASS = "".join(chr(c) for c in [80, 104, 97, 115, 101, 83, 101, 108, 101, 99, 116])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 51, 48])
IYWSKW = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 118])
JBIAMJ = "".join(
    chr(c) for c in [67, 108, 101, 97, 110, 83, 117, 115, 112, 101, 110, 100, 85, 68]
)
JEUTOP = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
JHIUSO = 11
JJVYFC = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
JMAOAW = 267
JMCBFE = "".join(chr(c) for c in [85, 100, 83, 112, 107, 114, 76, 105, 102, 116])
JNIBXY = "".join(
    chr(c) for c in [76, 101, 97, 114, 110, 80, 104, 97, 115, 101, 69, 114, 114]
)
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 49, 51])
JQRJJJ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
JRJHIU = "".join(chr(c) for c in [85, 100, 80, 51])
JTACCP = "".join(chr(c) for c in [70, 98])
JUGSEL = "".join(chr(c) for c in [67, 70, 71, 51])
JUIKFW = 270
JUTYEK = "".join(chr(c) for c in [85, 100, 86, 83, 80, 51])
JVDQLA = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
JVHFTH = 256
JVYFCR = 323
JWMNZM = 307
JYKLGQ = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
JYMOUN = 301
JZTATD = 463
KCWAON = "".join(chr(c) for c in [76, 79, 87])
KEAKST = 471
KFWRKI = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
KINEJN = 277
KJPUNR = 460
KLGQPL = 313
KMLOIJ = 448
KPHUOJ = 2
KQXPIC = 300
KSOKPH = "".join(chr(c) for c in [72, 73])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 50, 53])
KVKZIL = "".join(chr(c) for c in [82, 104, 76, 111, 119, 70, 108, 111])
KWIVDN = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 49, 75, 87]
)
KXSJWM = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
KZILXW = 258
LAIIDN = "".join(chr(c) for c in [82, 104, 83, 87, 84, 114, 105, 97, 99, 79, 72])
LASSAK = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
LGQPLS = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
LHBQNR = 453
LIUXFE = "".join(chr(c) for c in [66, 76])
LJUIKF = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
LKXSJW = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
LNMHXE = "".join(chr(c) for c in [114, 72, 73, 100])
LOIJUG = 449
LRAHEO = 292
LSPFTS = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
LSXUJU = "".join(chr(c) for c in [77, 69, 68])
LXWAJV = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
MAOAWB = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
MCBFEG = "".join(chr(c) for c in [85, 100, 70, 98])
MCGETI = 475
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 50, 49])
MHXEKV = "".join(chr(c) for c in [82, 104, 67, 111, 109, 109, 69, 114, 114])
MJIGYO = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
MJMAOA = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
MJVHFT = "".join(chr(c) for c in [72, 111, 117, 114, 115])
MLOIJU = "".join(chr(c) for c in [67, 70, 71, 49])
MNHTBJ = 328
MNZMJI = "".join(chr(c) for c in [83, 84, 79, 80])
MOUNBL = 305
NBLKXS = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
NEJNIB = "".join(
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
NHTBJE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
NIBXTI = "".join(chr(c) for c in [82, 104, 72, 87, 75, 105, 110])
NIBXYB = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
NKMLOI = "".join(chr(c) for c in [67, 70, 71, 48])
NMHXEK = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
NPYYLI = 6
NQGVUN = 343
NQJYMO = 274
NQLNMH = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
NQTMFZ = 467
NRJZTA = 462
NRSJMC = 8
NRXCHW = 455
NXNKML = "".join(chr(c) for c in [75, 54, 48, 48, 80, 114, 111, 116, 111, 99, 111, 108])
NZMJIG = "".join(chr(c) for c in [83, 84, 65, 82, 84])
OAWBSI = "".join(chr(c) for c in [78, 79])
OCTHBS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 82, 101, 97, 100])
OIHBXI = "".join(chr(c) for c in [76, 73])
OIJUGS = "".join(chr(c) for c in [67, 70, 71, 50])
OJRJHI = 12
OKPHUO = 14
ONPYYL = "".join(chr(c) for c in [80, 52])
OOQNRS = "".join(chr(c) for c in [85, 100, 66, 76])
OPHUGT = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
OQNRSJ = "".join(chr(c) for c in [79, 78])
OUNBLK = "".join(chr(c) for c in [86, 83, 80, 51, 70, 114, 111, 110, 116])
OUSPBW = 316
OUYNQJ = "".join(chr(c) for c in [83, 97, 110, 105])
PBWJYK = 310
PFTSIF = "".join(
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
PHUGTY = 357
PHUOJR = 4
PICXQI = "".join(chr(c) for c in [79, 85, 84, 49, 66, 82, 101, 97, 100])
PIPIVL = "".join(chr(c) for c in [76, 101, 97, 114, 110, 70, 97, 105, 108])
PIVLAS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 108, 101, 99, 116]
)
PLSPFT = 350
POUYNQ = "".join(chr(c) for c in [83, 112, 107, 114, 76, 105, 102, 116])
PQIPOU = "".join(chr(c) for c in [68, 79, 87, 78])
PUNRJZ = 461
PYYLIU = "".join(chr(c) for c in [80, 53])
QBMJVH = "".join(chr(c) for c in [82, 104, 84, 114, 105, 97, 99, 84, 101, 109, 112])
QEXLSX = 0
QFFTTI = 317
QFYLJU = 349
QGLRAH = 290
QGVUNX = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 118])
QIEFXQ = "".join(chr(c) for c in [79, 85, 84, 50, 66, 82, 101, 97, 100])
QIPOUY = "".join(chr(c) for c in [85, 80])
QJYMOU = "".join(chr(c) for c in [86, 115, 112, 49, 70, 114, 111, 110, 116])
QLAIID = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 79, 72])
QLNMHX = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
QNRXCH = "".join(chr(c) for c in [67, 70, 71, 55])
QPLSPF = "".join(
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
QRJJJV = "".join(chr(c) for c in [85, 76])
QSNQLN = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 50, 48])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 51, 49])
QXPICX = "".join(chr(c) for c in [79, 85, 84, 49, 65, 82, 101, 97, 100])
RAHEOC = "".join(chr(c) for c in [79, 85, 84, 54, 65, 82, 101, 97, 100])
RJJJVY = "".join(chr(c) for c in [67, 69])
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 49, 53])
RKINEJ = "".join(
    chr(c) for c in [70, 114, 101, 113, 68, 101, 116, 101, 99, 69, 114, 114]
)
RSJMCB = "".join(chr(c) for c in [85, 100, 84, 118, 76, 105, 102, 116])
RTFMNH = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
RXCHWD = "".join(chr(c) for c in [67, 70, 71, 56])
RYXBQF = 272
SBDJQR = "".join(chr(c) for c in [52, 56, 75])
SELHBQ = 452
SEMCGE = 474
SIFJBI = 269
SIRYXB = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
SJMCBF = 5
SJWMNZ = "".join(
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
SKSOKP = "".join(chr(c) for c in [76, 79])
SKWIVD = 338
SNQLNM = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
SOOQNR = 9
SPBWJY = "".join(
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
SPFTSI = 351
SSAKQX = "".join(chr(c) for c in [80, 111, 119, 101, 114, 117, 112])
SSUHBV = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
STSEMC = 473
SUHBVW = "".join(chr(c) for c in [77, 73, 65])
TACCPQ = 354
TATDZX = 464
TBJEUT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
TDZXNQ = 465
TFMNHT = 327
THBSKS = "".join(chr(c) for c in [85, 100, 80, 49])
THECVY = "".join(chr(c) for c in [83, 49])
TIACQF = "".join(chr(c) for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107])
TIDUBS = 320
TIXQVX = 477
TMFZDG = 468
TOPHUG = 333
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 50, 54])
TSIFJB = "".join(chr(c) for c in [80, 117, 114, 103, 101])
TTIDUB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
TYEKCW = "".join(chr(c) for c in [80, 49])
TYIYWS = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 73, 68])
UBSSUH = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
UGSELH = 451
UGTYIY = "".join(chr(c) for c in [70, 117, 108, 108])
UHBVWV = "".join(chr(c) for c in [68, 74, 83, 52])
UIKFWR = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
UJUTYE = 303
UNBLKX = 302
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 49, 52])
UNXNKM = 346
UOJRJH = "".join(chr(c) for c in [85, 100, 80, 50])
UQEXLS = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116])
USOOQN = "".join(chr(c) for c in [85, 100, 80, 53])
USPBWJ = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
UTOPHU = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
UTYEKC = 304
UXFEFJ = "".join(chr(c) for c in [79, 51])
UYNQJY = "".join(chr(c) for c in [79, 110, 122, 101, 110])
VDNQGV = 341
VDQLAI = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 80, 114])
VHFTHE = "".join(chr(c) for c in [77, 101, 110, 117])
VKZILX = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121, 69, 114, 114])
VLASSA = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
VUBYGD = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
VUNXNK = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 108])
VWVUBY = "".join(chr(c) for c in [75, 54, 48, 48])
VXOIHB = 479
VYFCRT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
VYYPIP = "".join(chr(c) for c in [72, 51])
WAJVDQ = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
WAONPY = "".join(chr(c) for c in [80, 50])
WDAFIK = "".join(chr(c) for c in [67, 70, 71, 49, 48])
WIVDNQ = 339
WJYKLG = 311
WMNZMJ = "".join(chr(c) for c in [73, 68, 76, 69])
WRKINE = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
WSKWIV = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 108])
WVUBYG = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
XBQFYL = 265
XCHWDA = 456
XEKVKZ = "".join(
    chr(c)
    for c in [82, 104, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
XFEFJT = 3
XIBHZV = 479
XLSXUJ = 306
XNKMLO = 347
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 49, 57])
XPICXQ = 280
XQGLRA = "".join(chr(c) for c in [79, 85, 84, 52, 65, 82, 101, 97, 100])
XQIEFX = 284
XQVXOI = 478
XTIACQ = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
XUJUTY = "".join(chr(c) for c in [85, 100, 86, 83, 80, 49])
XWAJVD = "".join(chr(c) for c in [82, 104, 72, 114, 72, 76])
XYBQSN = 278
YBQSNQ = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
YEKCWA = 356
YFCRTF = 324
YGDSBD = 322
YIYWSK = 335
YKLGQP = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
YLJUIK = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
YMOUNB = "".join(chr(c) for c in [86, 115, 112, 49, 77, 105, 110])
YNQJYM = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121])
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
YPIPIV = "".join(chr(c) for c in [70, 114])
YWSKWI = 337
YXBQFY = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
YYLIUX = 355
YYPIPI = "".join(chr(c) for c in [72, 52])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 50, 50])
ZILXWA = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
ZMJIGY = "".join(chr(c) for c in [78, 69, 87])
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 49, 54])
ZUQEXL = 1
ZXNQTM = 466
ACCPQI = [BSKSOK, BSKSOK, CBFEGZ, FEGZUQ]
CWAONP = [BSKSOK, EKCWAO, KCWAON]
DJQRJJ = [GDSBDJ, DSBDJQ, SBDJQR, BDJQRJ]
EGZUQE = [BSKSOK, CBFEGZ, BFEGZU, FEGZUQ]
GTYIYW = [HUGTYI, UGTYIY]
HBXIBH = [
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
]
IHBXIB = [
    TYEKCW,
    WAONPY,
    AONPYY,
    ONPYYL,
    PYYLIU,
    LIUXFE,
    IUXFEF,
    UXFEFJ,
    FEFJTA,
    EFJTAC,
    JTACCP,
    CCPQIP,
    CPQIPO,
    POUYNQ,
    OUYNQJ,
    UYNQJY,
    YNQJYM,
    QJYMOU,
    YMOUNB,
    OUNBLK,
    OIHBXI,
]
IPOUYN = [PQIPOU, QIPOUY]
JIGYOU = [WMNZMJ, MNZMJI, NZMJIG, ZMJIGY, MJIGYO]
JJJVYF = [QRJJJV, RJJJVY]
QNRSJM = [BSKSOK, OQNRSJ]
RJHIUS = [BSKSOK, KSOKPH]
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
UBYGDS = [
    UBSSUH,
    BSSUHB,
    SSUHBV,
    SUHBVW,
    UHBVWV,
    HBVWVU,
    BVWVUB,
    VWVUBY,
    WVUBYG,
    VUBYGD,
]
WBSIRY = [OAWBSI, SKSOKP, LSXUJU, KSOKPH, AWBSIR]
XOIHBX = []
XSJWMN = [LKXSJW, KXSJWM]
YLIUXF = [BSKSOK, EKCWAO]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return PHUOJR

    @property
    def begin(self):
        return BXIBHZ

    @property
    def end(self):
        return XIBHZV

    @property
    def all_device_keys(self):
        return IHBXIB

    @property
    def user_demand_keys(self):
        return HBXIBH

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
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, QEXLSX, CWAONP, None, PHUOJR, None
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, YEKCWA, KPHUOJ, CWAONP, None, PHUOJR, None
            ),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, YEKCWA, PHUOJR, CWAONP, None, PHUOJR, None
            ),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, YEKCWA, NPYYLI, CWAONP, None, PHUOJR, None
            ),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, YYLIUX, QEXLSX, YLIUXF, None, KPHUOJ, None
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, YYLIUX, ZUQEXL, QNRSJM, None, KPHUOJ, None
            ),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, YYLIUX, KPHUOJ, QNRSJM, None, KPHUOJ, None
            ),
            UXFEFJ: GeckoEnumStructAccessor(
                self.struct, UXFEFJ, YYLIUX, XFEFJT, QNRSJM, None, KPHUOJ, None
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, YYLIUX, PHUOJR, QNRSJM, None, KPHUOJ, None
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, YYLIUX, FJTACC, QNRSJM, None, KPHUOJ, None
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, TACCPQ, QEXLSX, ACCPQI, None, PHUOJR, None
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, TACCPQ, KPHUOJ, QNRSJM, None, KPHUOJ, None
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, TACCPQ, XFEFJT, IPOUYN, None, KPHUOJ, None
            ),
            POUYNQ: GeckoEnumStructAccessor(
                self.struct, POUYNQ, TACCPQ, PHUOJR, IPOUYN, None, KPHUOJ, None
            ),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, TACCPQ, SJMCBF, QNRSJM, None, KPHUOJ, None
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, TACCPQ, NPYYLI, QNRSJM, None, KPHUOJ, None
            ),
            YNQJYM: GeckoByteStructAccessor(self.struct, YNQJYM, NQJYMO, None),
            QJYMOU: GeckoByteStructAccessor(self.struct, QJYMOU, JYMOUN, None),
            YMOUNB: GeckoByteStructAccessor(self.struct, YMOUNB, MOUNBL, None),
            OUNBLK: GeckoByteStructAccessor(self.struct, OUNBLK, UNBLKX, None),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, BLKXSJ, QEXLSX, XSJWMN, None, KPHUOJ, HUOJRJ
            ),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, JIGYOU, None, None, HUOJRJ
            ),
            IGYOUS: GeckoTimeStructAccessor(self.struct, IGYOUS, GYOUSP, HUOJRJ),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, HUOJRJ),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, BLKXSJ, ZUQEXL, XSJWMN, None, KPHUOJ, HUOJRJ
            ),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, JIGYOU, None, None, HUOJRJ
            ),
            BWJYKL: GeckoTimeStructAccessor(self.struct, BWJYKL, WJYKLG, HUOJRJ),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, BLKXSJ, KPHUOJ, XSJWMN, None, KPHUOJ, HUOJRJ
            ),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, JIGYOU, None, None, HUOJRJ
            ),
            LGQPLS: GeckoTimeStructAccessor(self.struct, LGQPLS, GQPLSP, HUOJRJ),
            QPLSPF: GeckoByteStructAccessor(self.struct, QPLSPF, PLSPFT, HUOJRJ),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, HUOJRJ),
            PFTSIF: GeckoByteStructAccessor(self.struct, PFTSIF, FTSIFJ, HUOJRJ),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, SIFJBI, FJTACC, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, SIFJBI, SJMCBF, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, SIFJBI, PHUOJR, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, BIAMJM, XFEFJT, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, BIAMJM, QEXLSX, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, BIAMJM, ZUQEXL, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, None, None),
            MAOAWB: GeckoEnumStructAccessor(
                self.struct, MAOAWB, AOAWBS, None, WBSIRY, None, None, None
            ),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, SIFJBI, XFEFJT, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, SIFJBI, KPHUOJ, None),
            IRYXBQ: GeckoTempStructAccessor(self.struct, IRYXBQ, RYXBQF, None),
            YXBQFY: GeckoTempStructAccessor(self.struct, YXBQFY, XBQFYL, None),
            BQFYLJ: GeckoBoolStructAccessor(self.struct, BQFYLJ, QFYLJU, ZUQEXL, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, SIFJBI, ZUQEXL, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, SIFJBI, QEXLSX, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, JUIKFW, FJTACC, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, JUIKFW, NPYYLI, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, JUIKFW, SJMCBF, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, FWRKIN, QEXLSX, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, FWRKIN, KPHUOJ, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, KINEJN, NPYYLI, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, KINEJN, SJMCBF, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, KINEJN, PHUOJR, None),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, KINEJN, XFEFJT, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, KINEJN, KPHUOJ, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, KINEJN, ZUQEXL, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, KINEJN, QEXLSX, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, XYBQSN, FJTACC, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, XYBQSN, NPYYLI, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, XYBQSN, SJMCBF, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, XYBQSN, PHUOJR, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, XYBQSN, XFEFJT, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, XYBQSN, KPHUOJ, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, XYBQSN, ZUQEXL, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, XYBQSN, QEXLSX, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, BIAMJM, PHUOJR, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, HXEKVK, FJTACC, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, HXEKVK, XFEFJT, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, HXEKVK, KPHUOJ, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, HXEKVK, QEXLSX, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, KZILXW, FJTACC, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, KZILXW, NPYYLI, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, KZILXW, SJMCBF, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, KZILXW, PHUOJR, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, KZILXW, XFEFJT, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, KZILXW, KPHUOJ, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, KZILXW, ZUQEXL, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, KZILXW, QEXLSX, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, DQLAII, FJTACC, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, DQLAII, NPYYLI, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, DQLAII, SJMCBF, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, DQLAII, PHUOJR, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, DQLAII, XFEFJT, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, DQLAII, KPHUOJ, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, DQLAII, ZUQEXL, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, DQLAII, QEXLSX, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, BXTIAC, PHUOJR, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, BXTIAC, XFEFJT, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, BXTIAC, KPHUOJ, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, BXTIAC, ZUQEXL, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, BXTIAC, QEXLSX, None),
            CQFFTT: GeckoWordStructAccessor(self.struct, CQFFTT, QFFTTI, None),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoByteStructAccessor(self.struct, TTIDUB, TIDUBS, None),
            IDUBSS: GeckoEnumStructAccessor(
                self.struct, IDUBSS, DUBSSU, None, UBYGDS, None, None, None
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, YGDSBD, QEXLSX, DJQRJJ, None, PHUOJR, None
            ),
            JQRJJJ: GeckoEnumStructAccessor(
                self.struct, JQRJJJ, YGDSBD, KPHUOJ, JJJVYF, None, KPHUOJ, None
            ),
            JJVYFC: GeckoByteStructAccessor(self.struct, JJVYFC, JVYFCR, None),
            VYFCRT: GeckoByteStructAccessor(self.struct, VYFCRT, YFCRTF, None),
            FCRTFM: GeckoWordStructAccessor(self.struct, FCRTFM, CRTFMN, None),
            RTFMNH: GeckoByteStructAccessor(self.struct, RTFMNH, TFMNHT, None),
            FMNHTB: GeckoByteStructAccessor(self.struct, FMNHTB, MNHTBJ, None),
            NHTBJE: GeckoWordStructAccessor(self.struct, NHTBJE, HTBJEU, None),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, None),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, None),
            UTOPHU: GeckoWordStructAccessor(self.struct, UTOPHU, TOPHUG, None),
            OPHUGT: GeckoEnumStructAccessor(
                self.struct, OPHUGT, PHUGTY, None, GTYIYW, None, KPHUOJ, HUOJRJ
            ),
            TYIYWS: GeckoWordStructAccessor(self.struct, TYIYWS, YIYWSK, None),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, None),
            WSKWIV: GeckoByteStructAccessor(self.struct, WSKWIV, SKWIVD, None),
            KWIVDN: GeckoWordStructAccessor(self.struct, KWIVDN, WIVDNQ, None),
            IVDNQG: GeckoWordStructAccessor(self.struct, IVDNQG, VDNQGV, None),
        }

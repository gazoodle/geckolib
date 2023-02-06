#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v6'
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
ACCPQI = "".join(chr(c) for c in [80, 50])
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 55])
ACQFFT = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
AFIKJP = "".join(chr(c) for c in [67, 70, 71, 48])
AHEOCT = 294
AIIDNI = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
AJVDQL = "".join(
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
AKQXPI = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101, 83, 105, 103, 110]
)
AKSTSE = 461
AMJMAO = "".join(
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
AOAWBS = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
AONPYY = "".join(chr(c) for c in [85, 100, 86, 83, 80, 51])
ASSAKQ = "".join(chr(c) for c in [75, 54, 48, 48, 85, 112, 108, 111, 97, 100])
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 54])
AWBSIR = 313
AZMKQT = "".join(chr(c) for c in [76, 73])
BDJQRJ = 319
BHZVOA = 472
BIAMJM = 316
BJEUTO = "".join(chr(c) for c in [49, 54, 75])
BLKXSJ = "".join(chr(c) for c in [68, 79, 87, 78])
BMJVHF = 263
BQFYLJ = 352
BQNRXC = 341
BQSNQL = 270
BSIRYX = 314
BSKSOK = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
BSSUHB = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
BVWVUB = "".join(chr(c) for c in [82, 104, 72, 114, 75, 105, 110])
BWJYKL = "".join(chr(c) for c in [70, 85, 76, 76])
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 51])
BXTIAC = 258
BXYBQS = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
BYGDSB = "".join(
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
CBFEGZ = "".join(chr(c) for c in [79, 78])
CCPQIP = "".join(chr(c) for c in [80, 51])
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 55])
CHWDAF = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 108])
CMCVDS = 475
CPQIPO = "".join(chr(c) for c in [80, 52])
CQBMJV = 261
CQFFTT = 259
CRTFMN = "".join(chr(c) for c in [105, 110, 88, 77])
CTHBSK = 298
CVDSSR = 476
CVYYPI = "".join(chr(c) for c in [72, 50])
CWAONP = "".join(chr(c) for c in [85, 100, 86, 83, 80, 49])
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 50, 65, 82, 101, 97, 100])
DAFIKJ = 347
DGKEAK = 459
DJQRJJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
DNIBXT = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
DNQGVU = 329
DQLAII = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
DSBDJQ = 317
DSSRUR = 477
DUBSSU = "".join(chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 84, 101, 109, 112])
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 55])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 51])
ECVYYP = "".join(chr(c) for c in [72, 49])
EFJTAC = 356
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 51, 65, 82, 101, 97, 100])
EGZUQE = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
EJNIBX = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
EKCWAO = "".join(chr(c) for c in [83, 67, 65, 78])
EKVKZI = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
ELHBQN = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 49, 75, 87]
)
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 54])
EOCTHB = 296
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 49, 56])
EUTOPH = "".join(chr(c) for c in [52, 56, 75])
FCRTFM = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
FEFJTA = "".join(chr(c) for c in [80, 49])
FEGZUQ = 8
FFTTID = "".join(chr(c) for c in [82, 104, 67, 111, 109, 109, 69, 114, 114])
FIKJPU = 448
FJBIAM = 308
FJTACC = "".join(chr(c) for c in [72, 73, 71, 72])
FMNHTB = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
FTHECV = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTSIFJ = "".join(chr(c) for c in [78, 69, 87])
FTTIDU = "".join(
    chr(c)
    for c in [82, 104, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
FWRKIN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
FXQGLR = 288
FYLJUI = 269
FZDGKE = 458
GDSBDJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
GETIXQ = 465
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 50])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 53, 65, 82, 101, 97, 100])
GSELHB = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 108])
GTYIYW = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
GVUNXN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
GYOUSP = "".join(chr(c) for c in [86, 83, 80, 51, 70, 114, 111, 110, 116])
GZUQEX = 1
HBQNRX = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 70, 117, 108, 108]
)
HBSKSO = 362
HBVWVU = "".join(chr(c) for c in [82, 104, 72, 119, 84, 114, 105, 97, 99, 79, 72])
HBXIBH = 470
HECVYY = "".join(chr(c) for c in [83, 50])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 55, 65, 82, 101, 97, 100])
HFTHEC = 353
HIUSOO = 2
HTBJEU = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
HUGTYI = "".join(chr(c) for c in [67, 69])
HUOJRJ = "".join(chr(c) for c in [85, 100, 80, 49])
HWDAFI = 346
HXEKVK = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 53])
IACQFF = 257
IAMJMA = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 52])
IBXTIA = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
IBXYBQ = 272
ICXQIE = 282
IDNIBX = "".join(chr(c) for c in [114, 72, 73, 100])
IDUBSS = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
IEFXQG = 286
IFJBIA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
IGYOUS = 305
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 50])
IIDNIB = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
IJUGSE = 335
IKFWRK = "".join(chr(c) for c in [67, 80, 79, 84])
IKJPUN = "".join(chr(c) for c in [67, 70, 71, 49])
ILXWAJ = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
INEJNI = 268
IPIVLA = "".join(chr(c) for c in [76, 101, 97, 114, 110, 105, 110, 103])
IPOUYN = 355
IRYXBQ = 350
IUSOOQ = 4
IUXFEF = 360
IVDNQG = 323
IVLASS = "".join(chr(c) for c in [80, 104, 97, 115, 101, 83, 101, 108, 101, 99, 116])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 49, 57])
IYWSKW = 327
JBIAMJ = "".join(
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
JEUTOP = "".join(chr(c) for c in [51, 50, 75])
JHIUSO = 14
JIGYOU = "".join(chr(c) for c in [86, 115, 112, 49, 77, 105, 110])
JJJVYF = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
JJVYFC = "".join(chr(c) for c in [105, 110, 88, 69])
JMAOAW = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
JMCBFE = 9
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 50])
JQRJJJ = 320
JRJHIU = "".join(chr(c) for c in [72, 73])
JTACCP = "".join(chr(c) for c in [76, 79, 87])
JUGSEL = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 118])
JUIKFW = 279
JUTYEK = "".join(chr(c) for c in [85, 100, 83, 112, 107, 114, 76, 105, 102, 116])
JVDQLA = "".join(
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
JVHFTH = 256
JVYFCR = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
JWMNZM = "".join(chr(c) for c in [79, 110, 122, 101, 110])
JYKLGQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
JYMOUN = "".join(chr(c) for c in [70, 65, 78])
JZTATD = 452
KEAKST = 460
KFWRKI = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KINEJN = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
KJPUNR = 449
KLGQPL = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
KMLOIJ = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
KQXPIC = 300
KSOKPH = "".join(chr(c) for c in [68, 82, 65, 73, 78])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 52])
KVKZIL = 277
KWIVDN = 324
KZILXW = 278
LAIIDN = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
LASSAK = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
LGQPLS = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
LHBQNR = 339
LIUXFE = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
LJUIKF = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
LKXSJW = "".join(chr(c) for c in [85, 80])
LNMHXE = 271
LRAHEO = 292
LSPFTS = "".join(chr(c) for c in [73, 68, 76, 69])
LSXUJU = "".join(chr(c) for c in [85, 100, 86, 97, 108, 118, 101])
LXWAJV = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
MAOAWB = 311
MCBFEG = "".join(chr(c) for c in [85, 100, 66, 76])
MCGETI = 464
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 50, 56])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 49, 48])
MHXEKV = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
MJIGYO = 301
MJMAOA = 310
MJVHFT = "".join(chr(c) for c in [72, 111, 117, 114, 115])
MLOIJU = "".join(chr(c) for c in [70, 117, 108, 108])
MNHTBJ = "".join(chr(c) for c in [105, 110, 89, 84])
MNZMJI = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121])
MOUNBL = 354
NBLKXS = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
NEJNIB = "".join(chr(c) for c in [78, 79])
NIBXTI = 260
NIBXYB = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
NKMLOI = 357
NMHXEK = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
NPYYLI = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
NQGVUN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
NQJYMO = 3
NQLNMH = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
NQTMFZ = 456
NRJZTA = 451
NRSJMC = "".join(chr(c) for c in [85, 100, 80, 52])
NRXCHW = 343
NXNKML = 333
NZMJIG = 274
OACMCV = 474
OAWBSI = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 82, 101, 97, 100])
OIHBXI = 469
OIJUGS = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 73, 68])
OJRJHI = "".join(chr(c) for c in [76, 79])
OKPHUO = "".join(chr(c) for c in [79, 70, 70])
ONPYYL = 304
OOQNRS = "".join(chr(c) for c in [85, 100, 80, 51])
OPHUGT = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
OUSPBW = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
OUYNQJ = "".join(chr(c) for c in [66, 76])
PBWJYK = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
PFTSIF = "".join(chr(c) for c in [83, 84, 65, 82, 84])
PHUGTY = "".join(chr(c) for c in [85, 76])
PHUOJR = "".join(chr(c) for c in [65, 76, 76])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 49, 66, 82, 101, 97, 100])
PIPIVL = "".join(chr(c) for c in [76, 101, 97, 114, 110, 70, 97, 105, 108])
PIVLAS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 108, 101, 99, 116]
)
PLSPFT = 307
PQIPOU = 6
PUNRJZ = 450
PYYLIU = 358
QBMJVH = "".join(chr(c) for c in [82, 104, 84, 114, 105, 97, 99, 84, 101, 109, 112])
QEXLSX = "".join(chr(c) for c in [77, 69, 68])
QFFTTI = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
QFYLJU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
QGLRAH = 290
QGVUNX = 331
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 66, 82, 101, 97, 100])
QIPOUY = "".join(chr(c) for c in [80, 53])
QJYMOU = "".join(chr(c) for c in [76, 49, 50, 48])
QLAIID = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
QLNMHX = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
QNRSJM = 11
QNRXCH = "".join(chr(c) for c in [75, 54, 48, 48, 73, 68])
QPLSPF = "".join(
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
QRJJJV = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
QSNQLN = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
QTDKHT = 256
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 57])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 50, 48])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 49, 65, 82, 101, 97, 100])
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 54, 65, 82, 101, 97, 100])
RJJJVY = 321
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 52])
RKINEJ = 267
RSJMCB = 10
RTFMNH = "".join(chr(c) for c in [75, 54, 48, 48])
RURAZM = "".join(chr(c) for c in [67, 70, 71, 51, 49])
RXCHWD = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 118])
RYXBQF = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
SBDJQR = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
SELHBQ = 338
SEMCGE = 463
SIRYXB = "".join(
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
SJMCBF = "".join(chr(c) for c in [85, 100, 80, 53])
SJWMNZ = "".join(chr(c) for c in [83, 97, 110, 105])
SKSOKP = "".join(chr(c) for c in [81, 85, 73, 69, 84])
SKWIVD = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
SNQLNM = 349
SOKPHU = "".join(chr(c) for c in [83, 79, 65, 75])
SOOQNR = 12
SPBWJY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
SPFTSI = "".join(chr(c) for c in [83, 84, 79, 80])
SRURAZ = 478
SSAKQX = "".join(chr(c) for c in [80, 111, 119, 101, 114, 117, 112])
SSRURA = "".join(chr(c) for c in [67, 70, 71, 51, 48])
SSUHBV = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 80, 114])
STSEMC = 462
SUHBVW = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 79, 72])
SXUJUT = 7
TATDZX = 453
TBJEUT = 322
TDKHTZ = 479
TDZXNQ = 454
TFMNHT = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
THBSKS = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
THECVY = "".join(chr(c) for c in [83, 49])
TIACQF = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
TIDUBS = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121, 69, 114, 114])
TIXQVX = 466
TMFZDG = 457
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 53])
TSIFJB = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
TTIDUB = "".join(chr(c) for c in [82, 104, 76, 111, 119, 70, 108, 111])
TYEKCW = "".join(chr(c) for c in [70, 73, 88])
TYIYWS = 325
UBSSUH = "".join(chr(c) for c in [82, 104, 72, 114, 72, 76])
UBYGDS = "".join(chr(c) for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107])
UGSELH = 337
UHBVWV = "".join(chr(c) for c in [82, 104, 83, 87, 84, 114, 105, 97, 99, 79, 72])
UIKFWR = "".join(
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
UJUTYE = 5
UNBLKX = "".join(chr(c) for c in [65, 108, 119, 97, 121, 79, 110])
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 51])
UNXNKM = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
UOJRJH = 275
UQEXLS = 306
URAZMK = 479
USOOQN = "".join(chr(c) for c in [85, 100, 80, 50])
USPBWJ = 363
UTOPHU = "".join(chr(c) for c in [54, 52, 75])
UTYEKC = "".join(chr(c) for c in [85, 100, 70, 98])
UXFEFJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UYNQJY = "".join(chr(c) for c in [67, 80])
VDNQGV = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
VDQLAI = "".join(
    chr(c) for c in [76, 101, 97, 114, 110, 80, 104, 97, 115, 101, 69, 114, 114]
)
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 50, 57])
VHFTHE = "".join(chr(c) for c in [77, 101, 110, 117])
VKZILX = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
VLASSA = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 54])
VUBYGD = "".join(
    chr(c)
    for c in [82, 104, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101, 100]
)
VUNXNK = 332
VWVUBY = "".join(chr(c) for c in [82, 104, 83, 119, 75, 105, 110, 84, 101, 109, 112])
VXOIHB = 468
VYFCRT = "".join(chr(c) for c in [77, 73, 65])
VYYPIP = "".join(chr(c) for c in [72, 51])
WAJVDQ = "".join(
    chr(c) for c in [70, 114, 101, 113, 68, 101, 116, 101, 99, 69, 114, 114]
)
WAONPY = 303
WBSIRY = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
WDAFIK = "".join(chr(c) for c in [75, 54, 48, 48, 80, 114, 111, 116, 111, 99, 111, 108])
WIVDNQ = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
WMNZMJ = "".join(chr(c) for c in [86, 97, 108, 118, 101])
WRKINE = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
WSKWIV = 328
WVUBYG = "".join(chr(c) for c in [82, 104, 72, 87, 75, 105, 110])
XBQFYL = "".join(
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
XCHWDA = 345
XEKVKZ = "".join(
    chr(c) for c in [75, 105, 110, 80, 117, 114, 103, 101, 65, 99, 116, 105, 118, 101]
)
XFEFJT = 361
XIBHZV = 471
XLSXUJ = 0
XNKMLO = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 56])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 50, 49])
XPICXQ = 280
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 52, 65, 82, 101, 97, 100])
XQIEFX = 284
XQVXOI = 467
XSJWMN = "".join(chr(c) for c in [83, 112, 107, 114, 76, 105, 102, 116])
XTIACQ = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
XUJUTY = "".join(chr(c) for c in [85, 100, 84, 118, 76, 105, 102, 116])
XWAJVD = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
XYBQSN = 265
YBQSNQ = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
YEKCWA = "".join(chr(c) for c in [78, 65])
YFCRTF = "".join(chr(c) for c in [68, 74, 83, 52])
YGDSBD = "".join(
    chr(c)
    for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
YIYWSK = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
YKLGQP = 348
YLIUXF = 359
YLJUIK = "".join(chr(c) for c in [80, 117, 114, 103, 101])
YMOUNB = "".join(chr(c) for c in [70, 98])
YNQJYM = "".join(chr(c) for c in [79, 51])
YOUSPB = 302
YPIPIV = "".join(chr(c) for c in [70, 114])
YWSKWI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
YXBQFY = 351
YYLIUX = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
YYPIPI = "".join(chr(c) for c in [72, 52])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 49, 49])
ZILXWA = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
ZMJIGY = "".join(chr(c) for c in [86, 115, 112, 49, 70, 114, 111, 110, 116])
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 53])
ZUQEXL = "".join(chr(c) for c in [85, 100, 76, 105])
ZVOACM = 473
ZXNQTM = 455
BFEGZU = [OKPHUO, CBFEGZ]
EXLSXU = [OKPHUO, OJRJHI, QEXLSX, JRJHIU]
GQPLSP = [KLGQPL, LGQPLS]
JNIBXY = [NEJNIB, OJRJHI, QEXLSX, JRJHIU, EJNIBX]
KCWAON = [OKPHUO, TYEKCW, YEKCWA, EKCWAO]
KPHUOJ = [BSKSOK, SKSOKP, KSOKPH, SOKPHU, OKPHUO]
KQTDKH = [
    LAIIDN,
    QLAIID,
    JVDQLA,
    QSNQLN,
    AJVDQL,
    ZILXWA,
    AIIDNI,
    IIDNIB,
    XWAJVD,
    FFTTID,
    TIDUBS,
    VDQLAI,
    DQLAII,
    ILXWAJ,
    EKVKZI,
    XTIACQ,
    VKZILX,
    WAJVDQ,
    IDNIBX,
    LXWAJV,
]
KXSJWM = [BLKXSJ, LKXSJW]
LOIJUG = [KMLOIJ, MLOIJU]
MKQTDK = [
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
    CWAONP,
    AONPYY,
    NPYYLI,
    YYLIUX,
    LIUXFE,
    UXFEFJ,
]
NHTBJE = [
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
    FMNHTB,
    MNHTBJ,
]
OQNRSJ = [OKPHUO, JRJHIU]
OUNBLK = [OKPHUO, OKPHUO, TYEKCW, EKCWAO]
POUYNQ = [OKPHUO, FJTACC]
RAZMKQ = []
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
SIFJBI = [LSPFTS, SPFTSI, PFTSIF, FTSIFJ, TSIFJB]
TACCPQ = [OKPHUO, FJTACC, JTACCP]
TOPHUG = [BJEUTO, JEUTOP, EUTOPH, UTOPHU]
UGTYIY = [PHUGTY, HUGTYI]
WJYKLG = [SPBWJY, PBWJYK, BWJYKL]
ZMKQTD = [
    FEFJTA,
    ACCPQI,
    CCPQIP,
    CPQIPO,
    QIPOUY,
    OUYNQJ,
    UYNQJY,
    YNQJYM,
    QJYMOU,
    JYMOUN,
    YMOUNB,
    UNBLKX,
    NBLKXS,
    XSJWMN,
    SJWMNZ,
    JWMNZM,
    WMNZMJ,
    MNZMJI,
    ZMJIGY,
    JIGYOU,
    GYOUSP,
    OUSPBW,
    AZMKQT,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return PQIPOU

    @property
    def begin(self):
        return QTDKHT

    @property
    def end(self):
        return TDKHTZ

    @property
    def all_device_keys(self):
        return ZMKQTD

    @property
    def user_demand_keys(self):
        return MKQTDK

    @property
    def error_keys(self):
        return KQTDKH

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
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, UOJRJH, HIUSOO, KCWAON, HIUSOO, IUSOOQ, PHUOJR
            ),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, PHUOJR),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, PHUOJR),
            NPYYLI: GeckoByteStructAccessor(self.struct, NPYYLI, PYYLIU, PHUOJR),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, PHUOJR),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, PHUOJR),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, PHUOJR),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, EFJTAC, XLSXUJ, TACCPQ, None, IUSOOQ, None
            ),
            ACCPQI: GeckoEnumStructAccessor(
                self.struct, ACCPQI, EFJTAC, HIUSOO, TACCPQ, None, IUSOOQ, None
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, EFJTAC, IUSOOQ, TACCPQ, None, IUSOOQ, None
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, EFJTAC, PQIPOU, TACCPQ, None, IUSOOQ, None
            ),
            QIPOUY: GeckoEnumStructAccessor(
                self.struct, QIPOUY, IPOUYN, XLSXUJ, POUYNQ, None, HIUSOO, None
            ),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, IPOUYN, GZUQEX, BFEGZU, None, HIUSOO, None
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, IPOUYN, HIUSOO, BFEGZU, None, HIUSOO, None
            ),
            YNQJYM: GeckoEnumStructAccessor(
                self.struct, YNQJYM, IPOUYN, NQJYMO, BFEGZU, None, HIUSOO, None
            ),
            QJYMOU: GeckoEnumStructAccessor(
                self.struct, QJYMOU, IPOUYN, IUSOOQ, BFEGZU, None, HIUSOO, None
            ),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, IPOUYN, SXUJUT, BFEGZU, None, HIUSOO, None
            ),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, MOUNBL, XLSXUJ, OUNBLK, None, IUSOOQ, None
            ),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, MOUNBL, HIUSOO, BFEGZU, None, HIUSOO, None
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, MOUNBL, NQJYMO, KXSJWM, None, HIUSOO, None
            ),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, MOUNBL, IUSOOQ, KXSJWM, None, HIUSOO, None
            ),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, MOUNBL, UJUTYE, BFEGZU, None, HIUSOO, None
            ),
            JWMNZM: GeckoEnumStructAccessor(
                self.struct, JWMNZM, MOUNBL, PQIPOU, BFEGZU, None, HIUSOO, None
            ),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, MOUNBL, SXUJUT, BFEGZU, None, HIUSOO, None
            ),
            MNZMJI: GeckoByteStructAccessor(self.struct, MNZMJI, NZMJIG, None),
            ZMJIGY: GeckoByteStructAccessor(self.struct, ZMJIGY, MJIGYO, None),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, None),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, None),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, USPBWJ, None, WJYKLG, None, None, PHUOJR
            ),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, YKLGQP, XLSXUJ, GQPLSP, None, HIUSOO, PHUOJR
            ),
            QPLSPF: GeckoEnumStructAccessor(
                self.struct, QPLSPF, PLSPFT, None, SIFJBI, None, None, PHUOJR
            ),
            IFJBIA: GeckoTimeStructAccessor(self.struct, IFJBIA, FJBIAM, PHUOJR),
            JBIAMJ: GeckoByteStructAccessor(self.struct, JBIAMJ, BIAMJM, PHUOJR),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, YKLGQP, GZUQEX, GQPLSP, None, HIUSOO, PHUOJR
            ),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, MJMAOA, None, SIFJBI, None, None, PHUOJR
            ),
            JMAOAW: GeckoTimeStructAccessor(self.struct, JMAOAW, MAOAWB, PHUOJR),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, YKLGQP, HIUSOO, GQPLSP, None, HIUSOO, PHUOJR
            ),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, SIFJBI, None, None, PHUOJR
            ),
            WBSIRY: GeckoTimeStructAccessor(self.struct, WBSIRY, BSIRYX, PHUOJR),
            SIRYXB: GeckoByteStructAccessor(self.struct, SIRYXB, IRYXBQ, PHUOJR),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, PHUOJR),
            XBQFYL: GeckoByteStructAccessor(self.struct, XBQFYL, BQFYLJ, PHUOJR),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, UJUTYE, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FYLJUI, SXUJUT, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, JUIKFW, NQJYMO, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, JUIKFW, XLSXUJ, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, JUIKFW, GZUQEX, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, FYLJUI, HIUSOO, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, FYLJUI, NQJYMO, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, RKINEJ, None, None),
            KINEJN: GeckoEnumStructAccessor(
                self.struct, KINEJN, INEJNI, None, JNIBXY, None, None, None
            ),
            NIBXYB: GeckoTempStructAccessor(self.struct, NIBXYB, IBXYBQ, None),
            BXYBQS: GeckoTempStructAccessor(self.struct, BXYBQS, XYBQSN, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, BQSNQL, SXUJUT, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, SNQLNM, GZUQEX, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, FYLJUI, XLSXUJ, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, LNMHXE, HIUSOO, None),
            NMHXEK: GeckoBoolStructAccessor(
                self.struct, NMHXEK, LNMHXE, XLSXUJ, PHUOJR
            ),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, FYLJUI, GZUQEX, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, BQSNQL, PQIPOU, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, BQSNQL, UJUTYE, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, KVKZIL, UJUTYE, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, KZILXW, NQJYMO, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, KZILXW, HIUSOO, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, JUIKFW, IUSOOQ, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, KZILXW, IUSOOQ, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, KZILXW, GZUQEX, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, KVKZIL, PQIPOU, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, KVKZIL, IUSOOQ, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, KVKZIL, NQJYMO, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, KVKZIL, HIUSOO, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, KVKZIL, GZUQEX, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, KVKZIL, XLSXUJ, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, KZILXW, SXUJUT, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, KZILXW, PQIPOU, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, KZILXW, UJUTYE, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, KZILXW, XLSXUJ, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, NIBXTI, NQJYMO, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, BXTIAC, HIUSOO, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, BXTIAC, GZUQEX, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, IACQFF, HIUSOO, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, CQFFTT, HIUSOO, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, BXTIAC, IUSOOQ, None),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, IACQFF, SXUJUT, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, IACQFF, NQJYMO, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, IACQFF, XLSXUJ, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, BXTIAC, SXUJUT, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, BXTIAC, PQIPOU, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, BXTIAC, UJUTYE, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, BXTIAC, NQJYMO, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, BXTIAC, XLSXUJ, None),
            SSUHBV: GeckoBoolStructAccessor(self.struct, SSUHBV, CQFFTT, SXUJUT, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, CQFFTT, PQIPOU, None),
            UHBVWV: GeckoBoolStructAccessor(self.struct, UHBVWV, CQFFTT, UJUTYE, None),
            HBVWVU: GeckoBoolStructAccessor(self.struct, HBVWVU, CQFFTT, IUSOOQ, None),
            BVWVUB: GeckoBoolStructAccessor(self.struct, BVWVUB, CQFFTT, NQJYMO, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, CQFFTT, GZUQEX, None),
            WVUBYG: GeckoBoolStructAccessor(self.struct, WVUBYG, CQFFTT, XLSXUJ, None),
            VUBYGD: GeckoBoolStructAccessor(self.struct, VUBYGD, NIBXTI, IUSOOQ, None),
            UBYGDS: GeckoBoolStructAccessor(self.struct, UBYGDS, NIBXTI, HIUSOO, None),
            BYGDSB: GeckoBoolStructAccessor(self.struct, BYGDSB, NIBXTI, GZUQEX, None),
            YGDSBD: GeckoBoolStructAccessor(self.struct, YGDSBD, NIBXTI, XLSXUJ, None),
            GDSBDJ: GeckoWordStructAccessor(self.struct, GDSBDJ, DSBDJQ, None),
            SBDJQR: GeckoByteStructAccessor(self.struct, SBDJQR, BDJQRJ, None),
            DJQRJJ: GeckoByteStructAccessor(self.struct, DJQRJJ, JQRJJJ, None),
            QRJJJV: GeckoEnumStructAccessor(
                self.struct, QRJJJV, RJJJVY, None, NHTBJE, None, None, None
            ),
            HTBJEU: GeckoEnumStructAccessor(
                self.struct, HTBJEU, TBJEUT, XLSXUJ, TOPHUG, None, IUSOOQ, None
            ),
            OPHUGT: GeckoEnumStructAccessor(
                self.struct, OPHUGT, TBJEUT, HIUSOO, UGTYIY, None, HIUSOO, None
            ),
            GTYIYW: GeckoWordStructAccessor(self.struct, GTYIYW, TYIYWS, None),
            YIYWSK: GeckoByteStructAccessor(self.struct, YIYWSK, IYWSKW, None),
            YWSKWI: GeckoByteStructAccessor(self.struct, YWSKWI, WSKWIV, None),
            SKWIVD: GeckoByteStructAccessor(self.struct, SKWIVD, KWIVDN, None),
            WIVDNQ: GeckoByteStructAccessor(self.struct, WIVDNQ, IVDNQG, None),
            VDNQGV: GeckoWordStructAccessor(self.struct, VDNQGV, DNQGVU, None),
            NQGVUN: GeckoByteStructAccessor(self.struct, NQGVUN, QGVUNX, None),
            GVUNXN: GeckoByteStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoWordStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoEnumStructAccessor(
                self.struct, XNKMLO, NKMLOI, None, LOIJUG, None, HIUSOO, PHUOJR
            ),
            OIJUGS: GeckoWordStructAccessor(self.struct, OIJUGS, IJUGSE, None),
            JUGSEL: GeckoByteStructAccessor(self.struct, JUGSEL, UGSELH, None),
            GSELHB: GeckoByteStructAccessor(self.struct, GSELHB, SELHBQ, None),
            ELHBQN: GeckoWordStructAccessor(self.struct, ELHBQN, LHBQNR, None),
            HBQNRX: GeckoWordStructAccessor(self.struct, HBQNRX, BQNRXC, None),
        }

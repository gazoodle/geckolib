#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v7'
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
ACMCVD = "".join(chr(c) for c in [67, 70, 71, 50, 53])
ACQFFT = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
AFIKJP = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 108])
AHEOCT = 294
AIIDNI = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
AJVDQL = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
AKQXPI = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101, 83, 105, 103, 110]
)
AKSTSE = 459
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
ATDZXN = "".join(chr(c) for c in [67, 70, 71, 52])
AWBSIR = 313
AZMKQT = 478
BDJQRJ = "".join(
    chr(c)
    for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
BHZVOA = 470
BIAMJM = 316
BJEUTO = "".join(chr(c) for c in [105, 110, 89, 84])
BLKXSJ = "".join(chr(c) for c in [68, 79, 87, 78])
BMJVHF = 263
BQFYLJ = 352
BQNRXC = 338
BQSNQL = 270
BSIRYX = 314
BSKSOK = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
BSSUHB = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121, 69, 114, 114])
BVWVUB = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 80, 114])
BWJYKL = "".join(chr(c) for c in [70, 85, 76, 76])
BXIBHZ = "".join(chr(c) for c in [67, 70, 71, 50, 49])
BXTIAC = 260
BXYBQS = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
BYGDSB = "".join(chr(c) for c in [82, 104, 83, 119, 75, 105, 110, 84, 101, 109, 112])
CBFEGZ = "".join(chr(c) for c in [79, 78])
CCPQIP = "".join(chr(c) for c in [80, 51])
CGETIX = "".join(chr(c) for c in [67, 70, 71, 49, 53])
CHWDAF = "".join(chr(c) for c in [75, 54, 48, 48, 73, 68])
CMCVDS = 473
CPQIPO = "".join(chr(c) for c in [80, 52])
CQBMJV = 261
CQFFTT = 257
CRTFMN = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
CTHBSK = 298
CVDSSR = 474
CVYYPI = "".join(chr(c) for c in [72, 50])
CWAONP = "".join(chr(c) for c in [85, 100, 86, 83, 80, 49])
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 50, 65, 82, 101, 97, 100])
DAFIKJ = 345
DGKEAK = 457
DJQRJJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
DNIBXT = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
DNQGVU = 324
DQLAII = "".join(
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
DSBDJQ = "".join(chr(c) for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107])
DSSRUR = 475
DUBSSU = "".join(
    chr(c)
    for c in [82, 104, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
DZXNQT = "".join(chr(c) for c in [67, 70, 71, 53])
EAKSTS = "".join(chr(c) for c in [67, 70, 71, 49, 49])
ECVYYP = "".join(chr(c) for c in [72, 49])
EFJTAC = 356
EFXQGL = "".join(chr(c) for c in [79, 117, 116, 51, 65, 82, 101, 97, 100])
EGZUQE = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
EJNIBX = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
EKCWAO = "".join(chr(c) for c in [83, 67, 65, 78])
EKVKZI = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
ELHBQN = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 118])
EMCGET = "".join(chr(c) for c in [67, 70, 71, 49, 52])
EOCTHB = 296
ETIXQV = "".join(chr(c) for c in [67, 70, 71, 49, 54])
EUTOPH = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
FCRTFM = "".join(chr(c) for c in [105, 110, 88, 69])
FEFJTA = "".join(chr(c) for c in [80, 49])
FEGZUQ = 8
FFTTID = 259
FIKJPU = 346
FJBIAM = 308
FJTACC = "".join(chr(c) for c in [72, 73, 71, 72])
FMNHTB = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
FTHECV = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTSIFJ = "".join(chr(c) for c in [78, 69, 87])
FTTIDU = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
FWRKIN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
FXQGLR = 288
FYLJUI = 269
FZDGKE = 456
GDSBDJ = "".join(
    chr(c)
    for c in [82, 104, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101, 100]
)
GETIXQ = 463
GKEAKS = "".join(chr(c) for c in [67, 70, 71, 49, 48])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 53, 65, 82, 101, 97, 100])
GSELHB = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 73, 68])
GTYIYW = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
GVUNXN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
GYOUSP = "".join(chr(c) for c in [86, 83, 80, 51, 70, 114, 111, 110, 116])
GZUQEX = 1
HBQNRX = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 108])
HBSKSO = 362
HBVWVU = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
HBXIBH = 468
HECVYY = "".join(chr(c) for c in [83, 50])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 55, 65, 82, 101, 97, 100])
HFTHEC = 353
HIUSOO = 2
HTBJEU = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
HTZBBE = 256
HUGTYI = "".join(chr(c) for c in [54, 52, 75])
HUOJRJ = "".join(chr(c) for c in [85, 100, 80, 49])
HWDAFI = 343
HXEKVK = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
HZVOAC = "".join(chr(c) for c in [67, 70, 71, 50, 51])
IACQFF = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IAMJMA = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
IBHZVO = "".join(chr(c) for c in [67, 70, 71, 50, 50])
IBXTIA = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
IBXYBQ = 272
ICXQIE = 282
IDNIBX = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
IDUBSS = "".join(chr(c) for c in [82, 104, 67, 111, 109, 109, 69, 114, 114])
IEFXQG = 286
IFJBIA = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
IGYOUS = 305
IHBXIB = "".join(chr(c) for c in [67, 70, 71, 50, 48])
IIDNIB = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
IJUGSE = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
IKFWRK = "".join(chr(c) for c in [67, 80, 79, 84])
IKJPUN = "".join(chr(c) for c in [75, 54, 48, 48, 80, 114, 111, 116, 111, 99, 111, 108])
ILXWAJ = 278
INEJNI = 268
IPIVLA = "".join(chr(c) for c in [76, 101, 97, 114, 110, 105, 110, 103])
IPOUYN = 355
IRYXBQ = 350
IUSOOQ = 4
IUXFEF = 360
IVDNQG = 328
IVLASS = "".join(chr(c) for c in [80, 104, 97, 115, 101, 83, 101, 108, 101, 99, 116])
IXQVXO = "".join(chr(c) for c in [67, 70, 71, 49, 55])
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
JHIUSO = 14
JIGYOU = "".join(chr(c) for c in [86, 115, 112, 49, 77, 105, 110])
JJJVYF = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
JJVYFC = 320
JMAOAW = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
JMCBFE = 9
JPUNRJ = "".join(chr(c) for c in [67, 70, 71, 48])
JQRJJJ = 317
JRJHIU = "".join(chr(c) for c in [72, 73])
JTACCP = "".join(chr(c) for c in [76, 79, 87])
JUGSEL = "".join(chr(c) for c in [70, 117, 108, 108])
JUIKFW = 279
JUTYEK = "".join(chr(c) for c in [85, 100, 83, 112, 107, 114, 76, 105, 102, 116])
JVDQLA = "".join(
    chr(c) for c in [70, 114, 101, 113, 68, 101, 116, 101, 99, 69, 114, 114]
)
JVHFTH = 256
JVYFCR = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
JWMNZM = "".join(chr(c) for c in [79, 110, 122, 101, 110])
JYKLGQ = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
JYMOUN = "".join(chr(c) for c in [70, 65, 78])
JZTATD = 450
KEAKST = 458
KFWRKI = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
KINEJN = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
KJPUNR = 347
KLGQPL = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
KMLOIJ = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
KQXPIC = 300
KSOKPH = "".join(chr(c) for c in [68, 82, 65, 73, 78])
KSTSEM = "".join(chr(c) for c in [67, 70, 71, 49, 50])
KVKZIL = "".join(
    chr(c) for c in [75, 105, 110, 80, 117, 114, 103, 101, 65, 99, 116, 105, 118, 101]
)
KWIVDN = 327
KZILXW = 277
LAIIDN = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
LASSAK = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
LGQPLS = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
LHBQNR = 337
LIUXFE = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
LJUIKF = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
LKXSJW = "".join(chr(c) for c in [85, 80])
LNMHXE = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
LOIJUG = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
LRAHEO = 292
LSPFTS = "".join(chr(c) for c in [73, 68, 76, 69])
LSXUJU = "".join(chr(c) for c in [85, 100, 86, 97, 108, 118, 101])
LXWAJV = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
MAOAWB = 311
MCBFEG = "".join(chr(c) for c in [85, 100, 66, 76])
MCGETI = 462
MCVDSS = "".join(chr(c) for c in [67, 70, 71, 50, 54])
MFZDGK = "".join(chr(c) for c in [67, 70, 71, 56])
MHXEKV = 271
MJIGYO = 301
MJMAOA = 310
MJVHFT = "".join(chr(c) for c in [72, 111, 117, 114, 115])
MKQTDK = 479
MLOIJU = 333
MNHTBJ = "".join(chr(c) for c in [105, 110, 88, 77])
MNZMJI = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121])
MOUNBL = 354
NBLKXS = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
NEJNIB = "".join(chr(c) for c in [78, 79])
NHTBJE = "".join(chr(c) for c in [75, 54, 48, 48])
NIBXTI = "".join(chr(c) for c in [114, 72, 73, 100])
NIBXYB = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
NKMLOI = 332
NMHXEK = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
NPYYLI = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
NQGVUN = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
NQJYMO = 3
NQLNMH = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
NQTMFZ = 454
NRJZTA = 449
NRSJMC = "".join(chr(c) for c in [85, 100, 80, 52])
NRXCHW = 339
NXNKML = 331
NZMJIG = 274
OACMCV = 472
OAWBSI = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 82, 101, 97, 100])
OIHBXI = 467
OIJUGS = 357
OJRJHI = "".join(chr(c) for c in [76, 79])
OKPHUO = "".join(chr(c) for c in [79, 70, 70])
ONPYYL = 304
OOQNRS = "".join(chr(c) for c in [85, 100, 80, 51])
OPHUGT = "".join(chr(c) for c in [51, 50, 75])
OUSPBW = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
OUYNQJ = "".join(chr(c) for c in [66, 76])
PBWJYK = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
PFTSIF = "".join(chr(c) for c in [83, 84, 65, 82, 84])
PHUGTY = "".join(chr(c) for c in [52, 56, 75])
PHUOJR = "".join(chr(c) for c in [65, 76, 76])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 49, 66, 82, 101, 97, 100])
PIPIVL = "".join(chr(c) for c in [76, 101, 97, 114, 110, 70, 97, 105, 108])
PIVLAS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 108, 101, 99, 116]
)
PLSPFT = 307
PQIPOU = 6
PUNRJZ = 448
PYYLIU = 358
QBMJVH = "".join(chr(c) for c in [82, 104, 84, 114, 105, 97, 99, 84, 101, 109, 112])
QEXLSX = "".join(chr(c) for c in [77, 69, 68])
QFFTTI = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
QFYLJU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
QGLRAH = 290
QGVUNX = 323
QIEFXQ = "".join(chr(c) for c in [79, 117, 116, 50, 66, 82, 101, 97, 100])
QIPOUY = "".join(chr(c) for c in [80, 53])
QJYMOU = "".join(chr(c) for c in [76, 49, 50, 48])
QLAIID = "".join(
    chr(c) for c in [76, 101, 97, 114, 110, 80, 104, 97, 115, 101, 69, 114, 114]
)
QLNMHX = 364
QNRSJM = 11
QNRXCH = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 49, 75, 87]
)
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
QRJJJV = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
QSNQLN = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
QTDKHT = "".join(chr(c) for c in [76, 73])
QTMFZD = "".join(chr(c) for c in [67, 70, 71, 55])
QVXOIH = "".join(chr(c) for c in [67, 70, 71, 49, 56])
QXPICX = "".join(chr(c) for c in [79, 117, 116, 49, 65, 82, 101, 97, 100])
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 54, 65, 82, 101, 97, 100])
RAZMKQ = "".join(chr(c) for c in [67, 70, 71, 51, 48])
RJJJVY = 319
RJZTAT = "".join(chr(c) for c in [67, 70, 71, 50])
RKINEJ = 267
RSJMCB = 10
RTFMNH = "".join(chr(c) for c in [77, 73, 65])
RURAZM = "".join(chr(c) for c in [67, 70, 71, 50, 57])
RXCHWD = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 70, 117, 108, 108]
)
RYXBQF = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
SBDJQR = "".join(
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
SELHBQ = 335
SEMCGE = 461
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
SKWIVD = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
SNQLNM = 349
SOKPHU = "".join(chr(c) for c in [83, 79, 65, 75])
SOOQNR = 12
SPBWJY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
SPFTSI = "".join(chr(c) for c in [83, 84, 79, 80])
SRURAZ = 476
SSAKQX = "".join(chr(c) for c in [80, 111, 119, 101, 114, 117, 112])
SSRURA = "".join(chr(c) for c in [67, 70, 71, 50, 56])
SSUHBV = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
STSEMC = 460
SUHBVW = "".join(chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 84, 101, 109, 112])
SXUJUT = 7
TATDZX = 451
TBJEUT = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
TDZXNQ = 452
TFMNHT = "".join(chr(c) for c in [68, 74, 83, 52])
THBSKS = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
THECVY = "".join(chr(c) for c in [83, 49])
TIACQF = 258
TIDUBS = 365
TIXQVX = 464
TMFZDG = 455
TOPHUG = "".join(chr(c) for c in [49, 54, 75])
TSEMCG = "".join(chr(c) for c in [67, 70, 71, 49, 51])
TSIFJB = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
TTIDUB = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
TYEKCW = "".join(chr(c) for c in [70, 73, 88])
TYIYWS = "".join(chr(c) for c in [85, 76])
TZBBEK = 479
UBSSUH = "".join(chr(c) for c in [82, 104, 76, 111, 119, 70, 108, 111])
UBYGDS = "".join(chr(c) for c in [82, 104, 72, 114, 75, 105, 110])
UHBVWV = "".join(chr(c) for c in [82, 104, 72, 114, 72, 76])
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
UNRJZT = "".join(chr(c) for c in [67, 70, 71, 49])
UNXNKM = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
UOJRJH = 275
UQEXLS = 306
URAZMK = 477
USOOQN = "".join(chr(c) for c in [85, 100, 80, 50])
USPBWJ = 363
UTOPHU = 322
UTYEKC = "".join(chr(c) for c in [85, 100, 70, 98])
UXFEFJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UYNQJY = "".join(chr(c) for c in [67, 80])
VDNQGV = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
VDQLAI = "".join(
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
VDSSRU = "".join(chr(c) for c in [67, 70, 71, 50, 55])
VHFTHE = "".join(chr(c) for c in [77, 101, 110, 117])
VKZILX = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
VLASSA = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
VOACMC = "".join(chr(c) for c in [67, 70, 71, 50, 52])
VUBYGD = "".join(chr(c) for c in [82, 104, 72, 119, 84, 114, 105, 97, 99, 79, 72])
VUNXNK = 329
VWVUBY = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 79, 72])
VXOIHB = 466
VYFCRT = 321
VYYPIP = "".join(chr(c) for c in [72, 51])
WAJVDQ = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
WAONPY = 303
WBSIRY = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
WDAFIK = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 118])
WIVDNQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
WMNZMJ = "".join(chr(c) for c in [86, 97, 108, 118, 101])
WRKINE = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
WSKWIV = 325
WVUBYG = "".join(chr(c) for c in [82, 104, 83, 87, 84, 114, 105, 97, 99, 79, 72])
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
XCHWDA = 341
XEKVKZ = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
XFEFJT = 361
XIBHZV = 469
XLSXUJ = 0
XNKMLO = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
XNQTMF = "".join(chr(c) for c in [67, 70, 71, 54])
XOIHBX = "".join(chr(c) for c in [67, 70, 71, 49, 57])
XPICXQ = 280
XQGLRA = "".join(chr(c) for c in [79, 117, 116, 52, 65, 82, 101, 97, 100])
XQIEFX = 284
XQVXOI = 465
XSJWMN = "".join(chr(c) for c in [83, 112, 107, 114, 76, 105, 102, 116])
XTIACQ = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
XUJUTY = "".join(chr(c) for c in [85, 100, 84, 118, 76, 105, 102, 116])
XWAJVD = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
XYBQSN = 265
YBQSNQ = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
YEKCWA = "".join(chr(c) for c in [78, 65])
YFCRTF = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
YGDSBD = "".join(chr(c) for c in [82, 104, 72, 87, 75, 105, 110])
YIYWSK = "".join(chr(c) for c in [67, 69])
YKLGQP = 348
YLIUXF = 359
YLJUIK = "".join(chr(c) for c in [80, 117, 114, 103, 101])
YMOUNB = "".join(chr(c) for c in [70, 98])
YNQJYM = "".join(chr(c) for c in [79, 51])
YOUSPB = 302
YPIPIV = "".join(chr(c) for c in [70, 114])
YWSKWI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
YXBQFY = 351
YYLIUX = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
YYPIPI = "".join(chr(c) for c in [72, 52])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = "".join(chr(c) for c in [67, 70, 71, 57])
ZILXWA = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
ZMJIGY = "".join(chr(c) for c in [86, 115, 112, 49, 70, 114, 111, 110, 116])
ZMKQTD = "".join(chr(c) for c in [67, 70, 71, 51, 49])
ZTATDZ = "".join(chr(c) for c in [67, 70, 71, 51])
ZUQEXL = "".join(chr(c) for c in [85, 100, 76, 105])
ZVOACM = 471
ZXNQTM = 453
BFEGZU = [OKPHUO, CBFEGZ]
DKHTZB = [
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
EXLSXU = [OKPHUO, OJRJHI, QEXLSX, JRJHIU]
GQPLSP = [KLGQPL, LGQPLS]
IYWSKW = [TYIYWS, YIYWSK]
JEUTOP = [
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
]
JNIBXY = [NEJNIB, OJRJHI, QEXLSX, JRJHIU, EJNIBX]
KCWAON = [OKPHUO, TYEKCW, YEKCWA, EKCWAO]
KHTZBB = [
    IIDNIB,
    AIIDNI,
    DQLAII,
    QSNQLN,
    VDQLAI,
    LXWAJV,
    IDNIBX,
    DNIBXT,
    AJVDQL,
    IDUBSS,
    BSSUHB,
    QLAIID,
    LAIIDN,
    XWAJVD,
    VKZILX,
    IACQFF,
    ZILXWA,
    JVDQLA,
    NIBXTI,
    WAJVDQ,
]
KPHUOJ = [BSKSOK, SKSOKP, KSOKPH, SOKPHU, OKPHUO]
KQTDKH = []
KXSJWM = [BLKXSJ, LKXSJW]
OQNRSJ = [OKPHUO, JRJHIU]
OUNBLK = [OKPHUO, OKPHUO, TYEKCW, EKCWAO]
POUYNQ = [OKPHUO, FJTACC]
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
TDKHTZ = [
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
    QTDKHT,
]
UGSELH = [IJUGSE, JUGSEL]
UGTYIY = [TOPHUG, OPHUGT, PHUGTY, HUGTYI]
WJYKLG = [SPBWJY, PBWJYK, BWJYKL]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return SXUJUT

    @property
    def begin(self):
        return HTZBBE

    @property
    def end(self):
        return TZBBEK

    @property
    def all_device_keys(self):
        return TDKHTZ

    @property
    def user_demand_keys(self):
        return DKHTZB

    @property
    def error_keys(self):
        return KHTZBB

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
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, QLNMHX, XLSXUJ, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, FYLJUI, XLSXUJ, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, MHXEKV, HIUSOO, None),
            HXEKVK: GeckoBoolStructAccessor(
                self.struct, HXEKVK, MHXEKV, XLSXUJ, PHUOJR
            ),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, FYLJUI, GZUQEX, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, BQSNQL, PQIPOU, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, BQSNQL, UJUTYE, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, KZILXW, UJUTYE, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, ILXWAJ, NQJYMO, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, ILXWAJ, HIUSOO, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, JUIKFW, IUSOOQ, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, ILXWAJ, IUSOOQ, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, ILXWAJ, GZUQEX, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, KZILXW, PQIPOU, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, KZILXW, IUSOOQ, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, KZILXW, NQJYMO, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, KZILXW, HIUSOO, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, KZILXW, GZUQEX, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, KZILXW, XLSXUJ, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, ILXWAJ, SXUJUT, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, ILXWAJ, PQIPOU, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, ILXWAJ, UJUTYE, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, ILXWAJ, XLSXUJ, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, BXTIAC, NQJYMO, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, TIACQF, HIUSOO, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, TIACQF, GZUQEX, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, CQFFTT, HIUSOO, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, FFTTID, HIUSOO, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, TIACQF, IUSOOQ, None),
            TTIDUB: GeckoWordStructAccessor(self.struct, TTIDUB, TIDUBS, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, CQFFTT, SXUJUT, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, CQFFTT, NQJYMO, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, CQFFTT, XLSXUJ, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, TIACQF, SXUJUT, None),
            SSUHBV: GeckoBoolStructAccessor(self.struct, SSUHBV, TIACQF, PQIPOU, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, TIACQF, UJUTYE, None),
            UHBVWV: GeckoBoolStructAccessor(self.struct, UHBVWV, TIACQF, NQJYMO, None),
            HBVWVU: GeckoBoolStructAccessor(self.struct, HBVWVU, TIACQF, XLSXUJ, None),
            BVWVUB: GeckoBoolStructAccessor(self.struct, BVWVUB, FFTTID, SXUJUT, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, FFTTID, PQIPOU, None),
            WVUBYG: GeckoBoolStructAccessor(self.struct, WVUBYG, FFTTID, UJUTYE, None),
            VUBYGD: GeckoBoolStructAccessor(self.struct, VUBYGD, FFTTID, IUSOOQ, None),
            UBYGDS: GeckoBoolStructAccessor(self.struct, UBYGDS, FFTTID, NQJYMO, None),
            BYGDSB: GeckoBoolStructAccessor(self.struct, BYGDSB, FFTTID, GZUQEX, None),
            YGDSBD: GeckoBoolStructAccessor(self.struct, YGDSBD, FFTTID, XLSXUJ, None),
            GDSBDJ: GeckoBoolStructAccessor(self.struct, GDSBDJ, BXTIAC, IUSOOQ, None),
            DSBDJQ: GeckoBoolStructAccessor(self.struct, DSBDJQ, BXTIAC, HIUSOO, None),
            SBDJQR: GeckoBoolStructAccessor(self.struct, SBDJQR, BXTIAC, GZUQEX, None),
            BDJQRJ: GeckoBoolStructAccessor(self.struct, BDJQRJ, BXTIAC, XLSXUJ, None),
            DJQRJJ: GeckoWordStructAccessor(self.struct, DJQRJJ, JQRJJJ, None),
            QRJJJV: GeckoByteStructAccessor(self.struct, QRJJJV, RJJJVY, None),
            JJJVYF: GeckoByteStructAccessor(self.struct, JJJVYF, JJVYFC, None),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, VYFCRT, None, JEUTOP, None, None, None
            ),
            EUTOPH: GeckoEnumStructAccessor(
                self.struct, EUTOPH, UTOPHU, XLSXUJ, UGTYIY, None, IUSOOQ, None
            ),
            GTYIYW: GeckoEnumStructAccessor(
                self.struct, GTYIYW, UTOPHU, HIUSOO, IYWSKW, None, HIUSOO, None
            ),
            YWSKWI: GeckoWordStructAccessor(self.struct, YWSKWI, WSKWIV, None),
            SKWIVD: GeckoByteStructAccessor(self.struct, SKWIVD, KWIVDN, None),
            WIVDNQ: GeckoByteStructAccessor(self.struct, WIVDNQ, IVDNQG, None),
            VDNQGV: GeckoByteStructAccessor(self.struct, VDNQGV, DNQGVU, None),
            NQGVUN: GeckoByteStructAccessor(self.struct, NQGVUN, QGVUNX, None),
            GVUNXN: GeckoWordStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoWordStructAccessor(self.struct, KMLOIJ, MLOIJU, None),
            LOIJUG: GeckoEnumStructAccessor(
                self.struct, LOIJUG, OIJUGS, None, UGSELH, None, HIUSOO, PHUOJR
            ),
            GSELHB: GeckoWordStructAccessor(self.struct, GSELHB, SELHBQ, None),
            ELHBQN: GeckoByteStructAccessor(self.struct, ELHBQN, LHBQNR, None),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, None),
            QNRXCH: GeckoWordStructAccessor(self.struct, QNRXCH, NRXCHW, None),
            RXCHWD: GeckoWordStructAccessor(self.struct, RXCHWD, XCHWDA, None),
        }

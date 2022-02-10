#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXM v9'
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
ACCPQI = 274
ACMCVD = 475
ACQFFT = "".join(chr(c) for c in [82, 104, 83, 119, 75, 105, 110, 84, 101, 109, 112])
AFIKJP = 448
AHEOCT = "".join(chr(c) for c in [72, 73])
AIIDNI = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121, 69, 114, 114])
AJVDQL = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
AKQXPI = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 80, 104, 97, 115, 101, 83, 105, 103, 110]
)
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 49, 52])
AMJMAO = "".join(
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
AOAWBS = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
AONPYY = "".join(chr(c) for c in [67, 80])
ASSAKQ = "".join(chr(c) for c in [75, 54, 48, 48, 85, 112, 108, 111, 97, 100])
ATDZXN = 454
AWBSIR = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
BFEGZU = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 50, 53])
BIAMJM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
BJEUTO = 324
BLKXSJ = 371
BMJVHF = 263
BQFYLJ = 265
BQNRXC = "".join(chr(c) for c in [75, 53])
BQSNQL = "".join(
    chr(c) for c in [70, 114, 101, 113, 68, 101, 116, 101, 99, 69, 114, 114]
)
BSIRYX = "".join(chr(c) for c in [78, 79])
BSKSOK = "".join(chr(c) for c in [85, 100, 80, 51])
BSSUHB = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
BVWVUB = "".join(chr(c) for c in [105, 110, 88, 69])
BWJYKL = "".join(
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
BXIBHZ = 471
BXTIAC = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 79, 72])
BXYBQS = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
BYGDSB = "".join(chr(c) for c in [105, 110, 88, 77])
CBFEGZ = 304
CCPQIP = "".join(chr(c) for c in [86, 115, 112, 49, 70, 114, 111, 110, 116])
CGETIX = 465
CHWDAF = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
CMCVDS = "".join(chr(c) for c in [67, 70, 71, 50, 56])
CPQIPO = 301
CQBMJV = 261
CQFFTT = "".join(chr(c) for c in [82, 104, 72, 87, 75, 105, 110])
CTHBSK = 4
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 50, 57])
CVYYPI = "".join(chr(c) for c in [72, 50])
CXQIEF = 362
DAFIKJ = "".join(chr(c) for c in [67, 70, 71, 48])
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 49, 50])
DJQRJJ = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
DNIBXT = "".join(chr(c) for c in [82, 104, 72, 114, 72, 76])
DNQGVU = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 108])
DQLAII = "".join(chr(c) for c in [82, 104, 67, 111, 109, 109, 69, 114, 114])
DSBDJQ = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 51, 48])
DUBSSU = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
DZXNQT = 455
EAKSTS = 461
ECVYYP = "".join(chr(c) for c in [72, 49])
EFJTAC = "".join(chr(c) for c in [83, 97, 110, 105])
EFXQGL = "".join(chr(c) for c in [83, 79, 65, 75])
EGZUQE = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
EJNIBX = 277
EKCWAO = "".join(chr(c) for c in [80, 53])
EKVKZI = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
ELHBQN = "".join(chr(c) for c in [75, 56, 53])
EMCGET = 464
EOCTHB = 14
ETIXQV = 466
EUTOPH = 323
EXLSXU = 361
FCRTFM = "".join(chr(c) for c in [67, 69])
FEFJTA = "".join(chr(c) for c in [83, 112, 107, 114, 76, 105, 102, 116])
FEGZUQ = 358
FFTTID = "".join(chr(c) for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107])
FIKJPU = "".join(chr(c) for c in [67, 70, 71, 49])
FJBIAM = 269
FJTACC = "".join(chr(c) for c in [79, 110, 122, 101, 110])
FMNHTB = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
FTHECV = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
FTSIFJ = 351
FTTIDU = "".join(
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
FWRKIN = 271
FXQGLR = "".join(chr(c) for c in [79, 70, 70])
FYLJUI = 270
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 49, 49])
GDSBDJ = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 49, 56])
GKEAKS = 460
GLRAHE = "".join(chr(c) for c in [85, 100, 80, 49])
GQPLSP = 313
GSELHB = "".join(chr(c) for c in [75, 50, 48, 48])
GTYIYW = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
GVUNXN = 339
GZUQEX = 359
HBQNRX = "".join(chr(c) for c in [75, 52])
HBSKSO = 12
HBVWVU = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 50, 51])
HECVYY = "".join(chr(c) for c in [83, 50])
HFTHEC = 353
HIUSOO = "".join(chr(c) for c in [85, 100, 76, 105])
HTBJEU = 328
HUGTYI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
HUOJRJ = "".join(chr(c) for c in [85, 100, 66, 76])
HWDAFI = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
HXEKVK = "".join(chr(c) for c in [83, 99, 97, 110, 69, 114, 114])
HZVOAC = 473
IACQFF = "".join(chr(c) for c in [82, 104, 72, 114, 75, 105, 110])
IAMJMA = 279
IBHZVO = 472
IBXTIA = "".join(chr(c) for c in [82, 104, 72, 114, 84, 114, 105, 97, 99, 80, 114])
IBXYBQ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 49]
)
ICXQIE = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IDNIBX = "".join(chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 84, 101, 109, 112])
IDUBSS = 317
IEFXQG = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IFJBIA = "".join(chr(c) for c in [67, 108, 101, 97, 110])
IGYOUS = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
IHBXIB = 470
IIDNIB = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 82, 101, 116, 114, 121]
)
IJUGSE = 347
IKFWRK = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
IKJPUN = 449
ILXWAJ = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
INEJNI = "".join(
    chr(c) for c in [75, 105, 110, 80, 117, 114, 103, 101, 65, 99, 116, 105, 118, 101]
)
IPIVLA = "".join(chr(c) for c in [76, 101, 97, 114, 110, 105, 110, 103])
IPOUYN = "".join(chr(c) for c in [86, 83, 80, 51, 70, 114, 111, 110, 116])
IUSOOQ = 306
IUXFEF = "".join(chr(c) for c in [68, 79, 87, 78])
IVDNQG = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 82, 101, 118])
IVLASS = "".join(chr(c) for c in [80, 104, 97, 115, 101, 83, 101, 108, 101, 99, 116])
IXQVXO = 467
IYWSKW = 357
JBIAMJ = "".join(chr(c) for c in [80, 117, 114, 103, 101])
JEUTOP = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
JHIUSO = 1
JIGYOU = "".join(chr(c) for c in [78, 69, 87])
JJJVYF = "".join(chr(c) for c in [52, 56, 75])
JJVYFC = "".join(chr(c) for c in [54, 52, 75])
JMAOAW = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
JMCBFE = 303
JNIBXY = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
JPUNRJ = 450
JQRJJJ = 322
JRJHIU = 8
JTACCP = "".join(chr(c) for c in [86, 97, 108, 118, 101])
JUGSEL = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
JUIKFW = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
JUTYEK = "".join(chr(c) for c in [80, 50])
JVDQLA = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
JVHFTH = 256
JYKLGQ = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
JZTATD = "".join(chr(c) for c in [67, 70, 71, 53])
KCWAON = 355
KEAKST = "".join(chr(c) for c in [67, 70, 71, 49, 51])
KFWRKI = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
KINEJN = "".join(chr(c) for c in [67, 111, 111, 108, 105, 110, 103, 68, 111, 119, 110])
KJPUNR = "".join(chr(c) for c in [67, 70, 71, 50])
KLGQPL = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
KMLOIJ = 345
KPHUOJ = "".join(chr(c) for c in [85, 100, 80, 53])
KQTDKH = 480
KQXPIC = 300
KSOKPH = 11
KSTSEM = 462
KVKZIL = 260
KWIVDN = "".join(chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 73, 68])
KXSJWM = 348
KZILXW = 258
LAIIDN = "".join(chr(c) for c in [82, 104, 76, 111, 119, 70, 108, 111])
LASSAK = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
LGQPLS = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
LHBQNR = "".join(chr(c) for c in [75, 56])
LIUXFE = "".join(chr(c) for c in [84, 118, 76, 105, 102, 116])
LJUIKF = 349
LKXSJW = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
LNMHXE = "".join(chr(c) for c in [70, 117, 115, 101, 50, 69, 114, 114])
LOIJUG = 346
LRAHEO = 275
LSPFTS = "".join(
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
LSXUJU = 356
LXWAJV = 257
MAOAWB = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
MCBFEG = "".join(chr(c) for c in [85, 100, 86, 83, 80, 51])
MCGETI = "".join(chr(c) for c in [67, 70, 71, 49, 55])
MCVDSS = 476
MFZDGK = 458
MHXEKV = "".join(chr(c) for c in [83, 117, 112, 112, 108, 121, 69, 114, 114])
MJIGYO = "".join(chr(c) for c in [83, 84, 65, 82, 84])
MJMAOA = "".join(chr(c) for c in [67, 80, 79, 84])
MJVHFT = "".join(chr(c) for c in [72, 111, 117, 114, 115])
MKQTDK = 256
MLOIJU = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 108])
MNHTBJ = 327
MNZMJI = 307
MOUNBL = 368
NBLKXS = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
NEJNIB = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
NHTBJE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
NIBXTI = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
NIBXYB = 278
NKMLOI = "".join(chr(c) for c in [75, 54, 48, 48, 82, 101, 118])
NMHXEK = "".join(chr(c) for c in [70, 117, 115, 101, 49, 69, 114, 114])
NPYYLI = 3
NQGVUN = 338
NQJYMO = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
NQLNMH = "".join(
    chr(c) for c in [76, 101, 97, 114, 110, 80, 104, 97, 115, 101, 69, 114, 114]
)
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 57])
NRJZTA = "".join(chr(c) for c in [67, 70, 71, 52])
NRSJMC = 5
NRXCHW = "".join(chr(c) for c in [75, 49, 48, 48])
NXNKML = "".join(chr(c) for c in [75, 54, 48, 48, 73, 68])
NZMJIG = "".join(chr(c) for c in [73, 68, 76, 69])
OACMCV = "".join(chr(c) for c in [67, 70, 71, 50, 55])
OAWBSI = 267
OCTHBS = 2
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 50, 50])
OIJUGS = "".join(chr(c) for c in [75, 54, 48, 48, 80, 114, 111, 116, 111, 99, 111, 108])
OKPHUO = 10
ONPYYL = "".join(chr(c) for c in [79, 51])
OOQNRS = "".join(chr(c) for c in [85, 100, 86, 97, 108, 118, 101])
OPHUGT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
OQNRSJ = 7
OUNBLK = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
OUSPBW = 308
OUYNQJ = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
PBWJYK = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
PFTSIF = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
PHUGTY = 331
PHUOJR = 9
PICXQI = 0
PIPIVL = "".join(chr(c) for c in [76, 101, 97, 114, 110, 70, 97, 105, 108])
PIVLAS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 83, 101, 108, 101, 99, 116]
)
PLSPFT = 314
POUYNQ = 302
PQIPOU = "".join(chr(c) for c in [86, 115, 112, 49, 77, 105, 110])
PUNRJZ = "".join(chr(c) for c in [67, 70, 71, 51])
PYYLIU = "".join(chr(c) for c in [76, 49, 50, 48])
QBMJVH = "".join(chr(c) for c in [82, 104, 84, 114, 105, 97, 99, 84, 101, 109, 112])
QEXLSX = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
QFFTTI = "".join(
    chr(c)
    for c in [82, 104, 72, 101, 97, 116, 101, 114, 68, 105, 115, 97, 98, 108, 101, 100]
)
QFYLJU = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
QGLRAH = "".join(chr(c) for c in [65, 76, 76])
QGVUNX = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 49, 75, 87]
)
QIEFXQ = "".join(chr(c) for c in [81, 85, 73, 69, 84])
QIPOUY = 305
QJYMOU = "".join(chr(c) for c in [70, 85, 76, 76])
QLAIID = "".join(
    chr(c)
    for c in [82, 104, 78, 111, 116, 69, 110, 111, 117, 103, 104, 72, 101, 97, 116]
)
QLNMHX = "".join(chr(c) for c in [70, 117, 115, 101, 51, 69, 114, 114])
QNRSJM = "".join(chr(c) for c in [85, 100, 84, 118, 76, 105, 102, 116])
QNRXCH = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
QPLSPF = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
QRJJJV = "".join(chr(c) for c in [49, 54, 75])
QSNQLN = "".join(
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
QTMFZD = 457
QVXOIH = 468
QXPICX = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
RAHEOC = "".join(chr(c) for c in [76, 79])
RAZMKQ = "".join(chr(c) for c in [76, 73])
RJHIUS = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RJJJVY = "".join(chr(c) for c in [51, 50, 75])
RJZTAT = 452
RKINEJ = "".join(chr(c) for c in [80, 117, 109, 112, 82, 117, 110])
RSJMCB = "".join(chr(c) for c in [85, 100, 83, 112, 107, 114, 76, 105, 102, 116])
RTFMNH = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
RURAZM = 479
RXCHWD = "".join(chr(c) for c in [75, 56, 48, 48])
RYXBQF = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
SBDJQR = "".join(chr(c) for c in [105, 110, 89, 84])
SELHBQ = "".join(chr(c) for c in [75, 52, 48, 48])
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 49, 54])
SIFJBI = 352
SIRYXB = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
SJMCBF = "".join(chr(c) for c in [85, 100, 86, 83, 80, 49])
SJWMNZ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
SNQLNM = "".join(
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
SOKPHU = "".join(chr(c) for c in [85, 100, 80, 52])
SPBWJY = 316
SPFTSI = 350
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 51, 49])
SSAKQX = "".join(chr(c) for c in [80, 111, 119, 101, 114, 117, 112])
SSRURA = 478
SSUHBV = 320
STSEMC = "".join(chr(c) for c in [67, 70, 71, 49, 53])
SUHBVW = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
SXUJUT = "".join(chr(c) for c in [72, 73, 71, 72])
TACCPQ = "".join(chr(c) for c in [82, 104, 68, 117, 116, 121])
TATDZX = "".join(chr(c) for c in [67, 70, 71, 54])
TBJEUT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 55])
TFMNHT = 325
THBSKS = "".join(chr(c) for c in [85, 100, 80, 50])
THECVY = "".join(chr(c) for c in [83, 49])
TIACQF = "".join(chr(c) for c in [82, 104, 72, 119, 84, 114, 105, 97, 99, 79, 72])
TIDUBS = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 49, 57])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 49, 48])
TOPHUG = 329
TSEMCG = 463
TSIFJB = "".join(
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
TTIDUB = "".join(
    chr(c)
    for c in [82, 104, 70, 108, 111, 67, 104, 101, 99, 107, 82, 101, 97, 100, 121]
)
TYEKCW = "".join(chr(c) for c in [80, 52])
TYIYWS = 333
UBSSUH = 319
UBYGDS = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
UGSELH = 367
UGTYIY = 332
UHBVWV = 321
UIKFWR = 364
UNBLKX = 369
UNRJZT = 451
UNXNKM = 341
UOJRJH = "".join(chr(c) for c in [79, 78])
UQEXLS = 360
USOOQN = "".join(chr(c) for c in [77, 69, 68])
USPBWJ = "".join(
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
UTOPHU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
UTYEKC = "".join(chr(c) for c in [80, 51])
UXFEFJ = "".join(chr(c) for c in [85, 80])
UYNQJY = 363
VDNQGV = 337
VDQLAI = 365
VDSSRU = 477
VHFTHE = "".join(chr(c) for c in [77, 101, 110, 117])
VKZILX = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
VLASSA = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
VOACMC = 474
VUBYGD = "".join(chr(c) for c in [68, 74, 83, 52])
VUNXNK = "".join(
    chr(c) for c in [105, 110, 84, 104, 101, 114, 109, 67, 117, 114, 70, 117, 108, 108]
)
VWVUBY = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 50, 49])
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
VYYPIP = "".join(chr(c) for c in [72, 51])
WAJVDQ = 259
WAONPY = "".join(chr(c) for c in [66, 76])
WBSIRY = 268
WIVDNQ = 335
WJYKLG = 310
WMNZMJ = "".join(
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
WRKINE = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
WSKWIV = "".join(chr(c) for c in [70, 117, 108, 108])
WVUBYG = "".join(chr(c) for c in [77, 73, 65])
XBQFYL = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
XCHWDA = "".join(chr(c) for c in [])
XEKVKZ = "".join(chr(c) for c in [114, 72, 73, 100])
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 50, 52])
XLSXUJ = "".join(chr(c) for c in [80, 49])
XNKMLO = 343
XNQTMF = 456
XOIHBX = 469
XPICXQ = 373
XQIEFX = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 50, 48])
XSJWMN = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
XTIACQ = "".join(chr(c) for c in [82, 104, 83, 87, 84, 114, 105, 97, 99, 79, 72])
XUJUTY = "".join(chr(c) for c in [76, 79, 87])
XWAJVD = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
XYBQSN = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
YBQSNQ = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
YEKCWA = 6
YFCRTF = "".join(chr(c) for c in [85, 76])
YGDSBD = "".join(chr(c) for c in [75, 54, 48, 48])
YIYWSK = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
YKLGQP = 311
YLIUXF = 354
YLJUIK = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
YMOUNB = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
YNQJYM = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
YOUSPB = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YPIPIV = "".join(chr(c) for c in [70, 114])
YWSKWI = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
YXBQFY = 272
YYLIUX = "".join(chr(c) for c in [65, 108, 119, 97, 121, 79, 110])
YYPIPI = "".join(chr(c) for c in [72, 52])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZDGKEA = 459
ZILXWA = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
ZMJIGY = "".join(chr(c) for c in [83, 84, 79, 80])
ZTATDZ = 453
ZUQEXL = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
ZVOACM = "".join(chr(c) for c in [67, 70, 71, 50, 54])
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 56])
AZMKQT = [
    XLSXUJ,
    JUTYEK,
    UTYEKC,
    TYEKCW,
    EKCWAO,
    WAONPY,
    AONPYY,
    ONPYYL,
    PYYLIU,
    YYLIUX,
    LIUXFE,
    FEFJTA,
    EFJTAC,
    FJTACC,
    JTACCP,
    TACCPQ,
    CCPQIP,
    PQIPOU,
    IPOUYN,
    OUYNQJ,
    YMOUNB,
    OUNBLK,
    NBLKXS,
    RAZMKQ,
]
BDJQRJ = [
    HBVWVU,
    BVWVUB,
    VWVUBY,
    WVUBYG,
    VUBYGD,
    UBYGDS,
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
]
CRTFMN = [YFCRTF, FCRTFM]
CWAONP = [FXQGLR, SXUJUT]
GYOUSP = [NZMJIG, ZMJIGY, MJIGYO, JIGYOU, IGYOUS]
HEOCTH = [FXQGLR, RAHEOC, AHEOCT]
IRYXBQ = [BSIRYX, RAHEOC, USOOQN, AHEOCT, SIRYXB]
JVYFCR = [QRJJJV, RJJJVY, JJJVYF, JJVYFC]
JWMNZM = [XSJWMN, SJWMNZ]
JYMOUN = [YNQJYM, NQJYMO, QJYMOU]
OJRJHI = [FXQGLR, UOJRJH]
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
SKSOKP = [FXQGLR, AHEOCT]
SKWIVD = [YWSKWI, WSKWIV]
SOOQNR = [FXQGLR, RAHEOC, USOOQN, AHEOCT]
UJUTYE = [FXQGLR, SXUJUT, XUJUTY]
URAZMK = []
WDAFIK = [
    GSELHB,
    SELHBQ,
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
    QNRXCH,
    NRXCHW,
    RXCHWD,
    XCHWDA,
    XCHWDA,
    XCHWDA,
    CHWDAF,
    HWDAFI,
]
XFEFJT = [IUXFEF, UXFEFJ]
XQGLRA = [XQIEFX, QIEFXQ, IEFXQG, EFXQGL, FXQGLR]
ZMKQTD = [
    GLRAHE,
    THBSKS,
    BSKSOK,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    RJHIUS,
    HIUSOO,
    OOQNRS,
    QNRSJM,
    RSJMCB,
    SJMCBF,
    MCBFEG,
    BFEGZU,
    EGZUQE,
    ZUQEXL,
    QEXLSX,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return PHUOJR

    @property
    def begin(self):
        return MKQTDK

    @property
    def end(self):
        return KQTDKH

    @property
    def all_device_keys(self):
        return AZMKQT

    @property
    def user_demand_keys(self):
        return ZMKQTD

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
            QXPICX: GeckoBoolStructAccessor(self.struct, QXPICX, XPICXQ, PICXQI, None),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, XQGLRA, None, None, QGLRAH
            ),
            GLRAHE: GeckoEnumStructAccessor(
                self.struct, GLRAHE, LRAHEO, EOCTHB, HEOCTH, OCTHBS, CTHBSK, QGLRAH
            ),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, LRAHEO, HBSKSO, HEOCTH, OCTHBS, CTHBSK, QGLRAH
            ),
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, LRAHEO, KSOKPH, SKSOKP, OCTHBS, OCTHBS, QGLRAH
            ),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, LRAHEO, OKPHUO, SKSOKP, OCTHBS, OCTHBS, QGLRAH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, LRAHEO, PHUOJR, SKSOKP, OCTHBS, OCTHBS, QGLRAH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, LRAHEO, JRJHIU, OJRJHI, OCTHBS, OCTHBS, QGLRAH
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, LRAHEO, JHIUSO, OJRJHI, OCTHBS, OCTHBS, QGLRAH
            ),
            HIUSOO: GeckoEnumStructAccessor(
                self.struct, HIUSOO, IUSOOQ, PICXQI, SOOQNR, None, CTHBSK, QGLRAH
            ),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, LRAHEO, OQNRSJ, OJRJHI, OCTHBS, OCTHBS, QGLRAH
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, LRAHEO, NRSJMC, OJRJHI, OCTHBS, OCTHBS, QGLRAH
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, LRAHEO, CTHBSK, OJRJHI, OCTHBS, OCTHBS, QGLRAH
            ),
            SJMCBF: GeckoByteStructAccessor(self.struct, SJMCBF, JMCBFE, QGLRAH),
            MCBFEG: GeckoByteStructAccessor(self.struct, MCBFEG, CBFEGZ, QGLRAH),
            BFEGZU: GeckoByteStructAccessor(self.struct, BFEGZU, FEGZUQ, QGLRAH),
            EGZUQE: GeckoByteStructAccessor(self.struct, EGZUQE, GZUQEX, QGLRAH),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QGLRAH),
            QEXLSX: GeckoByteStructAccessor(self.struct, QEXLSX, EXLSXU, QGLRAH),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, PICXQI, UJUTYE, None, CTHBSK, None
            ),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, LSXUJU, OCTHBS, UJUTYE, None, CTHBSK, None
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, LSXUJU, CTHBSK, UJUTYE, None, CTHBSK, None
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, LSXUJU, YEKCWA, UJUTYE, None, CTHBSK, None
            ),
            EKCWAO: GeckoEnumStructAccessor(
                self.struct, EKCWAO, KCWAON, PICXQI, CWAONP, None, OCTHBS, None
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, KCWAON, JHIUSO, OJRJHI, None, OCTHBS, None
            ),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, KCWAON, OCTHBS, OJRJHI, None, OCTHBS, None
            ),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, KCWAON, NPYYLI, OJRJHI, None, OCTHBS, None
            ),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, KCWAON, CTHBSK, OJRJHI, None, OCTHBS, None
            ),
            YYLIUX: GeckoEnumStructAccessor(
                self.struct, YYLIUX, YLIUXF, OCTHBS, OJRJHI, None, OCTHBS, None
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, YLIUXF, NPYYLI, XFEFJT, None, OCTHBS, None
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, YLIUXF, CTHBSK, XFEFJT, None, OCTHBS, None
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, YLIUXF, NRSJMC, OJRJHI, None, OCTHBS, None
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, YLIUXF, YEKCWA, OJRJHI, None, OCTHBS, None
            ),
            JTACCP: GeckoEnumStructAccessor(
                self.struct, JTACCP, YLIUXF, OQNRSJ, OJRJHI, None, OCTHBS, None
            ),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, None),
            CCPQIP: GeckoByteStructAccessor(self.struct, CCPQIP, CPQIPO, None),
            PQIPOU: GeckoByteStructAccessor(self.struct, PQIPOU, QIPOUY, None),
            IPOUYN: GeckoByteStructAccessor(self.struct, IPOUYN, POUYNQ, None),
            OUYNQJ: GeckoEnumStructAccessor(
                self.struct, OUYNQJ, UYNQJY, None, JYMOUN, None, None, QGLRAH
            ),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, MOUNBL, None, JYMOUN, None, None, None
            ),
            OUNBLK: GeckoWordStructAccessor(self.struct, OUNBLK, UNBLKX, None),
            NBLKXS: GeckoWordStructAccessor(self.struct, NBLKXS, BLKXSJ, QGLRAH),
            LKXSJW: GeckoEnumStructAccessor(
                self.struct, LKXSJW, KXSJWM, PICXQI, JWMNZM, None, OCTHBS, QGLRAH
            ),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, MNZMJI, None, GYOUSP, None, None, QGLRAH
            ),
            YOUSPB: GeckoTimeStructAccessor(self.struct, YOUSPB, OUSPBW, QGLRAH),
            USPBWJ: GeckoByteStructAccessor(self.struct, USPBWJ, SPBWJY, QGLRAH),
            PBWJYK: GeckoEnumStructAccessor(
                self.struct, PBWJYK, KXSJWM, JHIUSO, JWMNZM, None, OCTHBS, QGLRAH
            ),
            BWJYKL: GeckoEnumStructAccessor(
                self.struct, BWJYKL, WJYKLG, None, GYOUSP, None, None, QGLRAH
            ),
            JYKLGQ: GeckoTimeStructAccessor(self.struct, JYKLGQ, YKLGQP, QGLRAH),
            KLGQPL: GeckoEnumStructAccessor(
                self.struct, KLGQPL, KXSJWM, OCTHBS, JWMNZM, None, OCTHBS, QGLRAH
            ),
            LGQPLS: GeckoEnumStructAccessor(
                self.struct, LGQPLS, GQPLSP, None, GYOUSP, None, None, QGLRAH
            ),
            QPLSPF: GeckoTimeStructAccessor(self.struct, QPLSPF, PLSPFT, QGLRAH),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, QGLRAH),
            PFTSIF: GeckoByteStructAccessor(self.struct, PFTSIF, FTSIFJ, QGLRAH),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QGLRAH),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FJBIAM, NRSJMC, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, FJBIAM, OQNRSJ, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, NPYYLI, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, IAMJMA, PICXQI, None),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, IAMJMA, JHIUSO, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, FJBIAM, OCTHBS, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, FJBIAM, NPYYLI, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, None, None),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, IRYXBQ, None, None, None
            ),
            RYXBQF: GeckoTempStructAccessor(self.struct, RYXBQF, YXBQFY, None),
            XBQFYL: GeckoTempStructAccessor(self.struct, XBQFYL, BQFYLJ, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, OQNRSJ, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, LJUIKF, JHIUSO, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, UIKFWR, PICXQI, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, FJBIAM, PICXQI, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, FWRKIN, OCTHBS, None),
            WRKINE: GeckoBoolStructAccessor(
                self.struct, WRKINE, FWRKIN, PICXQI, QGLRAH
            ),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, FJBIAM, JHIUSO, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, FYLJUI, YEKCWA, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, FYLJUI, NRSJMC, None),
            NEJNIB: GeckoBoolStructAccessor(self.struct, NEJNIB, EJNIBX, NRSJMC, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, NIBXYB, NPYYLI, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, NIBXYB, OCTHBS, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, IAMJMA, CTHBSK, None),
            XYBQSN: GeckoBoolStructAccessor(self.struct, XYBQSN, NIBXYB, CTHBSK, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, NIBXYB, JHIUSO, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, EJNIBX, YEKCWA, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, EJNIBX, CTHBSK, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, EJNIBX, NPYYLI, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, EJNIBX, OCTHBS, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, EJNIBX, JHIUSO, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, EJNIBX, PICXQI, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, NIBXYB, OQNRSJ, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, NIBXYB, YEKCWA, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, NIBXYB, NRSJMC, None),
            XEKVKZ: GeckoBoolStructAccessor(self.struct, XEKVKZ, NIBXYB, PICXQI, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, KVKZIL, NPYYLI, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, KZILXW, OCTHBS, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, KZILXW, JHIUSO, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, LXWAJV, OCTHBS, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, WAJVDQ, OCTHBS, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, KZILXW, CTHBSK, None),
            JVDQLA: GeckoWordStructAccessor(self.struct, JVDQLA, VDQLAI, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, LXWAJV, OQNRSJ, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, LXWAJV, NPYYLI, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, LXWAJV, PICXQI, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, KZILXW, OQNRSJ, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, KZILXW, YEKCWA, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, KZILXW, NRSJMC, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, KZILXW, NPYYLI, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, KZILXW, PICXQI, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, WAJVDQ, OQNRSJ, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, WAJVDQ, YEKCWA, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, WAJVDQ, NRSJMC, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, WAJVDQ, CTHBSK, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, WAJVDQ, NPYYLI, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, WAJVDQ, JHIUSO, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, WAJVDQ, PICXQI, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, KVKZIL, CTHBSK, None),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, KVKZIL, OCTHBS, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, KVKZIL, JHIUSO, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, KVKZIL, PICXQI, None),
            TIDUBS: GeckoWordStructAccessor(self.struct, TIDUBS, IDUBSS, None),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, None),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoEnumStructAccessor(
                self.struct, SUHBVW, UHBVWV, None, BDJQRJ, None, None, None
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, PICXQI, JVYFCR, None, CTHBSK, None
            ),
            VYFCRT: GeckoEnumStructAccessor(
                self.struct, VYFCRT, JQRJJJ, OCTHBS, CRTFMN, None, OCTHBS, None
            ),
            RTFMNH: GeckoWordStructAccessor(self.struct, RTFMNH, TFMNHT, None),
            FMNHTB: GeckoByteStructAccessor(self.struct, FMNHTB, MNHTBJ, None),
            NHTBJE: GeckoByteStructAccessor(self.struct, NHTBJE, HTBJEU, None),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, None),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, None),
            UTOPHU: GeckoWordStructAccessor(self.struct, UTOPHU, TOPHUG, None),
            OPHUGT: GeckoByteStructAccessor(self.struct, OPHUGT, PHUGTY, None),
            HUGTYI: GeckoByteStructAccessor(self.struct, HUGTYI, UGTYIY, None),
            GTYIYW: GeckoWordStructAccessor(self.struct, GTYIYW, TYIYWS, None),
            YIYWSK: GeckoEnumStructAccessor(
                self.struct, YIYWSK, IYWSKW, None, SKWIVD, None, OCTHBS, QGLRAH
            ),
            KWIVDN: GeckoWordStructAccessor(self.struct, KWIVDN, WIVDNQ, None),
            IVDNQG: GeckoByteStructAccessor(self.struct, IVDNQG, VDNQGV, None),
            DNQGVU: GeckoByteStructAccessor(self.struct, DNQGVU, NQGVUN, None),
            QGVUNX: GeckoWordStructAccessor(self.struct, QGVUNX, GVUNXN, None),
            VUNXNK: GeckoWordStructAccessor(self.struct, VUNXNK, UNXNKM, None),
            JUGSEL: GeckoEnumStructAccessor(
                self.struct, JUGSEL, UGSELH, None, WDAFIK, None, None, None
            ),
        }

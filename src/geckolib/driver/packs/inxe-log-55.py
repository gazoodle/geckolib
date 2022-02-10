#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InXE v55'
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
ACQFFT = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
AFIKJP = 454
AHEOCT = 308
AIIDNI = "".join(chr(c) for c in [50, 53, 65])
AJVDQL = "".join(chr(c) for c in [53, 79, 80])
AKQXPI = "".join(chr(c) for c in [72, 73])
AKSTSE = "".join(chr(c) for c in [67, 70, 71, 50, 48])
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
ATDZXN = 460
AWBSIR = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
BDJQRJ = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
BFEGZU = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
BHZVOA = "".join(chr(c) for c in [67, 70, 71, 51, 49])
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
BJEUTO = "".join(chr(c) for c in [80, 50, 76])
BLKXSJ = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
BMJVHF = 256
BQFYLJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
BQNRXC = "".join(chr(c) for c in [67, 70, 71, 50])
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
BXIBHZ = 477
BXTIAC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
BXYBQS = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
BYGDSB = "".join(chr(c) for c in [75, 52, 48, 48])
CBFEGZ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
CCPQIP = "".join(chr(c) for c in [67, 80, 79, 84])
CGETIX = 471
CHWDAF = 452
CMCVDS = 55
CPQIPO = 274
CQBMJV = 317
CQFFTT = 295
CRTFMN = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
CTHBSK = 303
CVDSSR = 479
CVYYPI = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
CWAONP = 266
CXQIEF = "".join(chr(c) for c in [85, 100, 80, 51])
DAFIKJ = "".join(chr(c) for c in [67, 70, 71, 54])
DGKEAK = "".join(chr(c) for c in [67, 70, 71, 49, 56])
DJQRJJ = "".join(chr(c) for c in [75, 49, 48, 48])
DNIBXT = 7
DNQGVU = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
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
DSBDJQ = "".join(chr(c) for c in [75, 52])
DUBSSU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
DZXNQT = 461
EAKSTS = 467
ECVYYP = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
EFJTAC = 273
EFXQGL = 258
EJNIBX = "".join(chr(c) for c in [105, 110, 88, 69])
EKCWAO = 264
ELHBQN = 448
EMCGET = 470
EOCTHB = 307
ETIXQV = 472
EUTOPH = "".join(chr(c) for c in [80, 51, 76])
FCRTFM = 360
FEFJTA = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FEGZUQ = "".join(chr(c) for c in [70, 85, 76, 76])
FFTTID = 296
FIKJPU = "".join(chr(c) for c in [67, 70, 71, 55])
FJBIAM = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
FJTACC = "".join(chr(c) for c in [80, 117, 114, 103, 101])
FMNHTB = 320
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
FZDGKE = "".join(chr(c) for c in [67, 70, 71, 49, 55])
GDSBDJ = "".join(chr(c) for c in [75, 56])
GETIXQ = "".join(chr(c) for c in [67, 70, 71, 50, 52])
GKEAKS = 466
GQPLSP = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
GSELHB = 332
GTYIYW = 321
GVUNXN = 328
GYOUSP = 281
GZUQEX = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
HBQNRX = 449
HBSKSO = 304
HBVWVU = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
HBXIBH = "".join(chr(c) for c in [67, 70, 71, 50, 57])
HECVYY = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 105])
HFTHEC = "".join(chr(c) for c in [])
HIUSOO = 260
HTBJEU = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = "".join(chr(c) for c in [76, 79, 87])
HWDAFI = "".join(chr(c) for c in [67, 70, 71, 53])
HXEKVK = "".join(chr(c) for c in [52, 56, 75])
HZVOAC = 479
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
IBHZVO = 478
IBXTIA = 291
IBXYBQ = "".join(chr(c) for c in [68, 74, 83, 52])
ICXQIE = 2
IDUBSS = 299
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 53])
IFJBIA = 351
IGYOUS = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
IHBXIB = 476
IIDNIB = "".join(chr(c) for c in [51, 48, 65])
IJUGSE = 325
IKFWRK = 285
IKJPUN = 455
ILXWAJ = "".join(chr(c) for c in [80, 97, 99, 107, 88, 101, 80, 50, 50, 66, 76])
INEJNI = 289
IPIVLA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IPOUYN = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
IRYXBQ = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
IUXFEF = 271
IVDNQG = "".join(chr(c) for c in [72, 84, 82])
IVLASS = "".join(chr(c) for c in [79, 70, 70])
IXQVXO = 473
IYWSKW = "".join(chr(c) for c in [83, 79, 117, 116, 52])
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
JEUTOP = "".join(chr(c) for c in [80, 51, 72])
JHIUSO = "".join(chr(c) for c in [80, 53])
JIGYOU = 280
JJJVYF = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
JMAOAW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
JMCBFE = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
JNIBXY = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
JPUNRJ = 456
JQRJJJ = "".join(chr(c) for c in [75, 56, 48, 48])
JRJHIU = "".join(chr(c) for c in [80, 51])
JTACCP = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
JUIKFW = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
JUTYEK = "".join(chr(c) for c in [78, 69, 87])
JVDQLA = "".join(chr(c) for c in [51, 79, 80])
JVHFTH = 319
JVYFCR = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
JWMNZM = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
JYKLGQ = 283
JZTATD = "".join(chr(c) for c in [67, 70, 71, 49, 49])
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
KEAKST = "".join(chr(c) for c in [67, 70, 71, 49, 57])
KFWRKI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
KINEJN = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
KJPUNR = "".join(chr(c) for c in [67, 70, 71, 56])
KLGQPL = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
KMLOIJ = 331
KPHUOJ = 261
KSOKPH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
KSTSEM = 468
KVKZIL = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
KWIVDN = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
KXSJWM = 275
KZILXW = "".join(chr(c) for c in [67, 69])
LAIIDN = "".join(
    chr(c) for c in [80, 97, 99, 107, 70, 117, 115, 101, 49, 82, 97, 116, 105, 110, 103]
)
LASSAK = "".join(chr(c) for c in [65, 76, 76])
LGQPLS = 284
LHBQNR = "".join(chr(c) for c in [67, 70, 71, 49])
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
LOIJUG = 333
LRAHEO = 1
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
LSXUJU = 263
LXWAJV = "".join(chr(c) for c in [80, 50, 50])
MAOAWB = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
MCBFEG = 310
MCGETI = "".join(chr(c) for c in [67, 70, 71, 50, 51])
MCVDSS = 256
MFZDGK = 464
MHXEKV = "".join(chr(c) for c in [51, 50, 75])
MJIGYO = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
MJMAOA = 354
MJVHFT = "".join(chr(c) for c in [77, 101, 110, 117])
MLOIJU = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
MNHTBJ = "".join(chr(c) for c in [78, 65])
MNZMJI = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
MOUNBL = 353
NBLKXS = 355
NEJNIB = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
NHTBJE = "".join(chr(c) for c in [80, 49, 72])
NIBXTI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
NIBXYB = "".join(chr(c) for c in [77, 73, 65])
NKMLOI = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
NMHXEK = "".join(chr(c) for c in [49, 54, 75])
NPYYLI = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
NQGVUN = 327
NQJYMO = "".join(chr(c) for c in [77, 69, 68])
NQTMFZ = "".join(chr(c) for c in [67, 70, 71, 49, 53])
NRJZTA = "".join(chr(c) for c in [67, 70, 71, 49, 48])
NRSJMC = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
NRXCHW = "".join(chr(c) for c in [67, 70, 71, 51])
NXNKML = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
NZMJIG = 279
OAWBSI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
OCTHBS = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
OIHBXI = "".join(chr(c) for c in [67, 70, 71, 50, 56])
OIJUGS = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
OJRJHI = "".join(chr(c) for c in [80, 50])
OKPHUO = "".join(chr(c) for c in [80, 49])
ONPYYL = 267
OOQNRS = "".join(chr(c) for c in [79, 51])
OPHUGT = "".join(chr(c) for c in [66, 76, 79])
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
PHUGTY = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
PHUOJR = "".join(chr(c) for c in [72, 73, 71, 72])
PICXQI = "".join(chr(c) for c in [85, 100, 80, 50])
PIPIVL = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
PIVLAS = "".join(chr(c) for c in [83, 79, 65, 75])
PLSPFT = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
POUYNQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
PQIPOU = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
PUNRJZ = "".join(chr(c) for c in [67, 70, 71, 57])
PYYLIU = 268
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QFFTTI = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
QFYLJU = 315
QGLRAH = "".join(chr(c) for c in [79, 78])
QGVUNX = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
QIEFXQ = 6
QIPOUY = 282
QJYMOU = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QLAIID = "".join(chr(c) for c in [80, 97, 99, 107, 78, 111, 73, 110, 70, 108, 111])
QLNMHX = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
QNRSJM = "".join(chr(c) for c in [76, 49, 50, 48])
QNRXCH = 450
QPLSPF = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
QRJJJV = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
QSNQLN = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
QTMFZD = 463
QVXOIH = 474
QXPICX = 0
RAHEOC = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
RJHIUS = "".join(chr(c) for c in [80, 52])
RJJJVY = "".join(chr(c) for c in [75, 51, 48, 48])
RJZTAT = 458
RKINEJ = 288
RSJMCB = 5
RTFMNH = 361
RXCHWD = 451
RYXBQF = 311
SAKQXP = "".join(chr(c) for c in [76, 79])
SBDJQR = "".join(chr(c) for c in [75, 53])
SELHBQ = "".join(chr(c) for c in [67, 70, 71, 48])
SEMCGE = "".join(chr(c) for c in [67, 70, 71, 50, 50])
SIFJBI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
SJMCBF = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
SJWMNZ = 277
SKSOKP = 305
SKWIVD = 324
SNQLNM = "".join(chr(c) for c in [105, 110, 89, 84])
SOKPHU = 306
SOOQNR = "".join(chr(c) for c in [67, 80])
SPBWJY = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
SPFTSI = 350
SSAKQX = 259
SSUHBV = 301
STSEMC = "".join(chr(c) for c in [67, 70, 71, 50, 49])
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
TATDZX = "".join(chr(c) for c in [67, 70, 71, 49, 50])
TBJEUT = "".join(chr(c) for c in [80, 50, 72])
TDZXNQ = "".join(chr(c) for c in [67, 70, 71, 49, 51])
TFMNHT = "".join(chr(c) for c in [83, 79, 117, 116, 49])
THBSKS = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
THECVY = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
TIACQF = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TIDUBS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
TIXQVX = "".join(chr(c) for c in [67, 70, 71, 50, 53])
TMFZDG = "".join(chr(c) for c in [67, 70, 71, 49, 54])
TOPHUG = "".join(chr(c) for c in [80, 52, 76])
TSEMCG = 469
TSIFJB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
TTIDUB = 297
TYIYWS = "".join(chr(c) for c in [83, 79, 117, 116, 51])
UBSSUH = 300
UBYGDS = "".join(chr(c) for c in [75, 50, 48, 48])
UGSELH = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
UGTYIY = "".join(chr(c) for c in [83, 79, 117, 116, 50])
UHBVWV = 316
UIKFWR = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
UJUTYE = "".join(chr(c) for c in [83, 84, 65, 82, 84])
UNBLKX = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
UNRJZT = 457
UNXNKM = 329
UQEXLS = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
USOOQN = "".join(chr(c) for c in [66, 76])
USPBWJ = 352
UTOPHU = "".join(chr(c) for c in [80, 52, 72])
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
VHFTHE = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
VKZILX = "".join(chr(c) for c in [85, 76])
VOACMC = "".join(chr(c) for c in [76, 73])
VUBYGD = 357
VUNXNK = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
VXOIHB = "".join(chr(c) for c in [67, 70, 71, 50, 55])
VYFCRT = 358
WAJVDQ = "".join(
    chr(c) for c in [80, 97, 99, 107, 88, 101, 79, 117, 116, 112, 117, 116, 115]
)
WAONPY = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
WBSIRY = 309
WDAFIK = 453
WIVDNQ = 326
WJYKLG = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
WRKINE = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
WSKWIV = "".join(chr(c) for c in [83, 79, 117, 116, 53])
WVUBYG = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
XBQFYL = 314
XCHWDA = "".join(chr(c) for c in [67, 70, 71, 52])
XEKVKZ = "".join(chr(c) for c in [54, 52, 75])
XFEFJT = 272
XIBHZV = "".join(chr(c) for c in [67, 70, 71, 51, 48])
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
XNKMLO = 330
XNQTMF = 462
XOIHBX = 475
XPICXQ = 4
XQGLRA = "".join(chr(c) for c in [85, 100, 66, 76])
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 52])
XQVXOI = "".join(chr(c) for c in [67, 70, 71, 50, 54])
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
YFCRTF = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
YGDSBD = "".join(chr(c) for c in [75, 56, 53])
YIYWSK = 322
YKLGQP = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
YLIUXF = 270
YLJUIK = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
YMOUNB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
YNQJYM = "".join(chr(c) for c in [78, 79])
YOUSPB = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
YPIPIV = 257
YWSKWI = 323
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
ZDGKEA = 465
ZMJIGY = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
ZTATDZ = 459
ZUQEXL = 262
ZXNQTM = "".join(chr(c) for c in [67, 70, 71, 49, 52])
ACMCVD = [
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
HUGTYI = [
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    TOPHUG,
    JHIUSO,
    OPHUGT,
    SOOQNR,
    OOQNRS,
    QNRSJM,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    HFTHEC,
    PHUGTY,
]
IDNIBX = [AIIDNI, IIDNIB]
IUSOOQ = [IVLASS, PHUOJR]
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
    HFTHEC,
    HFTHEC,
    HFTHEC,
    QRJJJV,
    RJJJVY,
    JJJVYF,
]
JUGSEL = [
    MNHTBJ,
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
OACMCV = [
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
    VOACMC,
]
SIRYXB = [HFTHEC, BSIRYX, BSIRYX, BSIRYX]
TYEKCW = [SXUJUT, XUJUTY, UJUTYE, JUTYEK, UTYEKC]
UOJRJH = [IVLASS, PHUOJR, HUOJRJ]
VDNQGV = [
    MNHTBJ,
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
    IVDNQG,
]
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
XWAJVD = [USOOQN, LXWAJV]
ZILXWA = [VKZILX, KZILXW]
ZVOACM = []


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return CMCVDS

    @property
    def begin(self):
        return MCVDSS

    @property
    def end(self):
        return CVDSSR

    @property
    def all_device_keys(self):
        return OACMCV

    @property
    def user_demand_keys(self):
        return ACMCVD

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
                self.struct, WVUBYG, VUBYGD, None, JJVYFC, None, None, None
            ),
            JVYFCR: GeckoWordStructAccessor(self.struct, JVYFCR, VYFCRT, None),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, None),
            CRTFMN: GeckoByteStructAccessor(self.struct, CRTFMN, RTFMNH, None),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, FMNHTB, None, HUGTYI, None, None, LASSAK
            ),
            UGTYIY: GeckoEnumStructAccessor(
                self.struct, UGTYIY, GTYIYW, None, HUGTYI, None, None, LASSAK
            ),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, YIYWSK, None, HUGTYI, None, None, LASSAK
            ),
            IYWSKW: GeckoEnumStructAccessor(
                self.struct, IYWSKW, YWSKWI, None, HUGTYI, None, None, LASSAK
            ),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, SKWIVD, None, HUGTYI, None, None, LASSAK
            ),
            KWIVDN: GeckoEnumStructAccessor(
                self.struct, KWIVDN, WIVDNQ, None, VDNQGV, None, None, LASSAK
            ),
            DNQGVU: GeckoByteStructAccessor(self.struct, DNQGVU, NQGVUN, LASSAK),
            QGVUNX: GeckoByteStructAccessor(self.struct, QGVUNX, GVUNXN, LASSAK),
            VUNXNK: GeckoByteStructAccessor(self.struct, VUNXNK, UNXNKM, LASSAK),
            NXNKML: GeckoByteStructAccessor(self.struct, NXNKML, XNKMLO, LASSAK),
            NKMLOI: GeckoByteStructAccessor(self.struct, NKMLOI, KMLOIJ, LASSAK),
            MLOIJU: GeckoByteStructAccessor(self.struct, MLOIJU, LOIJUG, LASSAK),
            OIJUGS: GeckoEnumStructAccessor(
                self.struct, OIJUGS, IJUGSE, None, JUGSEL, None, None, LASSAK
            ),
            UGSELH: GeckoByteStructAccessor(self.struct, UGSELH, GSELHB, LASSAK),
        }

#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v61'
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
ACMCVD = 347
ACQFFT = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
AHEOCT = 1
AIIDNI = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
AIVEMV = "".join(
    chr(c)
    for c in [
        105,
        110,
        70,
        108,
        111,
        80,
        114,
        101,
        115,
        115,
        117,
        114,
        101,
        83,
        119,
        68,
        101,
        116,
        101,
        99,
        116,
        101,
        100,
    ]
)
AJVDQL = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
AKQXPI = "".join(chr(c) for c in [85, 100, 80, 49])
AKSTSE = "".join(chr(c) for c in [70, 97, 110])
AMJMAO = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
AOAWBS = "".join(
    chr(c)
    for c in [
        67,
        111,
        111,
        108,
        90,
        111,
        110,
        101,
        68,
        101,
        116,
        101,
        99,
        116,
        101,
        100,
    ]
)
AONPYY = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
ASSAKQ = "".join(chr(c) for c in [79, 70, 70])
AWBSIR = "".join(
    chr(c)
    for c in [
        72,
        80,
        67,
        82,
        101,
        115,
        72,
        101,
        97,
        116,
        101,
        114,
        82,
        101,
        113,
        117,
        101,
        115,
        116,
    ]
)
AZMKQT = "".join(chr(c) for c in [67, 70, 71, 52])
BBEKBD = 457
BDFSRO = 459
BDJQRJ = "".join(chr(c) for c in [54, 52, 75])
BEKBDF = "".join(chr(c) for c in [67, 70, 71, 49, 48])
BFEGZU = "".join(chr(c) for c in [67, 80])
BHZVOA = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
BIAMJM = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
BJEUTO = 299
BJLOIN = "".join(chr(c) for c in [67, 70, 71, 49, 57])
BLKXSJ = "".join(chr(c) for c in [67, 108, 101, 97, 110])
BMJVHF = 256
BQFYLJ = 379
BQNRXC = "".join(chr(c) for c in [80, 50, 72])
BQSNQL = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
BSIRYX = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
BSKSOK = "".join(chr(c) for c in [85, 100, 65, 117, 120])
BSSUHB = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
BVWVUB = "".join(chr(c) for c in [75, 54, 48, 48])
BWJYKL = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
BXIBHZ = 343
BXTIAC = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
BXYBQS = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
BYGDSB = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
CBFEGZ = "".join(chr(c) for c in [66, 76])
CCPQIP = 266
CGETIX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
CHWDAF = "".join(chr(c) for c in [80, 52, 76])
CMCVDS = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
CPQIPO = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
CQBMJV = 317
CQFFTT = 285
CRTFMN = 294
CTHBSK = 307
CVDSSR = "".join(chr(c) for c in [67, 70, 71, 48])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
CXQIEF = 4
CYWONF = 373
CZOLSI = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
DAFIKJ = "".join(chr(c) for c in [65, 85, 88])
DDPMXF = 463
DFSROG = "".join(chr(c) for c in [67, 70, 71, 49, 50])
DGKEAK = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
DKHTZB = "".join(chr(c) for c in [67, 70, 71, 55])
DNIBXT = 314
DNQGVU = "".join(chr(c) for c in [75, 56, 48, 48])
DPMXFU = "".join(chr(c) for c in [67, 70, 71, 49, 54])
DQLAII = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
DRXAIV = 478
DSBDJQ = "".join(chr(c) for c in [51, 50, 75])
DSSRUR = "".join(chr(c) for c in [67, 70, 71, 49])
DUBSSU = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
DZXNQT = 327
EAKSTS = 325
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 475
EFJTAC = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
EFXQGL = "".join(chr(c) for c in [85, 100, 80, 52])
EGZUQE = 3
EJNIBX = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        72,
        116,
        114,
        50,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
EKBDFS = 458
EKCWAO = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
EKVKZI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
ELHBQN = "".join(chr(c) for c in [78, 65])
ELWUEU = "".join(chr(c) for c in [67, 70, 71, 50, 50])
EMCGET = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
EMVCYW = "".join(
    chr(c)
    for c in [
        105,
        110,
        70,
        108,
        111,
        82,
        97,
        116,
        105,
        111,
        77,
        105,
        110,
        105,
        109,
        117,
        109,
    ]
)
EOCTHB = 308
ETDRXA = 477
ETIXQV = 332
EUHNNX = "".join(chr(c) for c in [67, 70, 71, 50, 52])
EUTOPH = 300
EXLSXU = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
EZFETD = "".join(chr(c) for c in [67, 70, 71, 50, 56])
FCRTFM = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
FEFJTA = "".join(chr(c) for c in [78, 69, 87])
FEGZUQ = "".join(chr(c) for c in [79, 51])
FETDRX = "".join(chr(c) for c in [67, 70, 71, 50, 57])
FFTTID = 287
FIKJPU = "".join(chr(c) for c in [83, 79, 117, 116, 50])
FJBIAM = 281
FMNHTB = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
FSROGM = 460
FTHECV = 319
FTSIFJ = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
FTTIDU = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
FUBJLO = "".join(chr(c) for c in [67, 70, 71, 49, 56])
FXQGLR = "".join(chr(c) for c in [85, 100, 80, 53])
FYLJUI = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
FZCZOL = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
FZDGKE = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
GDSBDJ = "".join(chr(c) for c in [49, 54, 75])
GETIXQ = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
GKEAKS = 333
GLRAHE = "".join(chr(c) for c in [85, 100, 66, 76])
GMDDPM = 462
GQPLSP = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
GSELHB = "".join(chr(c) for c in [83, 79, 117, 116, 49])
GVUNXN = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
GYOUSP = "".join(chr(c) for c in [78, 79])
GZUQEX = "".join(chr(c) for c in [76, 49, 50, 48])
HBQNRX = "".join(chr(c) for c in [80, 49, 76])
HBSKSO = 363
HBVWVU = "".join(chr(c) for c in [105, 110, 88, 77])
HBXIBH = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = 369
HNNXWE = "".join(chr(c) for c in [67, 70, 71, 50, 53])
HTBJEU = 297
HTZBBE = "".join(chr(c) for c in [67, 70, 71, 56])
HUGTYI = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
HUOJRJ = 305
HWDAFI = "".join(chr(c) for c in [66, 76, 79])
HXEKVK = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
HZVOAC = 345
IACQFF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
IAMJMA = 352
IBHZVO = 344
IBXTIA = 315
IBXYBQ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
ICXQIE = 0
IDNIBX = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
IDUBSS = 289
IEFXQG = "".join(chr(c) for c in [85, 100, 80, 51])
IFJBIA = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
IGYOUS = 313
IHBXIB = 342
IIDNIB = 311
IJUGSE = "".join(chr(c) for c in [45, 45, 45])
IKFWRK = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
IKJPUN = 321
ILXWAJ = 354
INEJNI = "".join(
    chr(c)
    for c in [
        83,
        108,
        97,
        118,
        101,
        72,
        116,
        114,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
INELWU = "".join(chr(c) for c in [67, 70, 71, 50, 49])
IPIVLA = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
IPOUYN = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
IRYXBQ = "".join(chr(c) for c in [72, 69, 65, 84])
IUSOOQ = "".join(chr(c) for c in [80, 49])
IUXFEF = "".join(chr(c) for c in [73, 68, 76, 69])
IVDNQG = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
IVEMVC = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
IXQVXO = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
IYWSKW = "".join(chr(c) for c in [75, 50, 48, 48])
JBIAMJ = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
JEUTOP = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
JHIUSO = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JIGYOU = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
JJVYFC = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
JLOINE = 467
JMAOAW = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
JMCBFE = 260
JNIBXY = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
JPUNRJ = 322
JQRJJJ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
JRJHIU = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
JTACCP = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JUGSEL = "".join(chr(c) for c in [82, 69, 83, 69, 84])
JUIKFW = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
JUTYEK = "".join(chr(c) for c in [70, 85, 76, 76])
JVDQLA = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
JVHFTH = 274
JVYFCR = 291
JWMNZM = "".join(
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
JYKLGQ = 355
JYMOUN = 272
JZTATD = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
KBDFSR = "".join(chr(c) for c in [67, 70, 71, 49, 49])
KCWAON = 365
KEAKST = "".join(chr(c) for c in [83, 79, 117, 116, 54])
KFWRKI = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
KHTZBB = 455
KINEJN = "".join(
    chr(c)
    for c in [
        72,
        116,
        114,
        50,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
KJPUNR = "".join(chr(c) for c in [83, 79, 117, 116, 51])
KLGQPL = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
KMLOIJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
KPHUOJ = 304
KQTDKH = 453
KQXPIC = 259
KSOKPH = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
KVKZIL = "".join(
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
KWIVDN = "".join(chr(c) for c in [75, 52])
KXSJWM = "".join(chr(c) for c in [80, 117, 114, 103, 101])
KZILXW = "".join(
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
LAIIDN = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
LASSAK = "".join(chr(c) for c in [83, 79, 65, 75])
LGQPLS = 275
LHBQNR = "".join(chr(c) for c in [80, 49, 72])
LIUXFE = 263
LJUIKF = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
LKXSJW = 273
LNMHXE = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
LOIJUG = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
LOINEL = "".join(chr(c) for c in [67, 70, 71, 50, 48])
LRAHEO = "".join(chr(c) for c in [79, 78])
LSIPMD = 375
LSXUJU = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
LWUEUH = 470
LXWAJV = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
MAOAWB = 384
MCGETI = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
MCVDSS = 348
MDDPMX = "".join(chr(c) for c in [67, 70, 71, 49, 53])
MFZDGK = 330
MHXEKV = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
MJIGYO = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
MJMAOA = 377
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = "".join(chr(c) for c in [67, 70, 71, 53])
MLOIJU = 361
MNHTBJ = 296
MNZMJI = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
MOUNBL = "".join(
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
MPSCTT = 61
MVCYWO = 372
MXFUBJ = "".join(chr(c) for c in [67, 70, 71, 49, 55])
NBLKXS = 381
NEJNIB = 350
NELWUE = 469
NFZCZO = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
NHTBJE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
NIBXTI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
NIBXYB = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
NKMLOI = 360
NMHXEK = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
NNXWEE = 473
NPYYLI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
NQGVUN = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
NQJYMO = 271
NQLNMH = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
NQTMFZ = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
NRJZTA = "".join(chr(c) for c in [83, 79, 117, 116, 53])
NRSJMC = "".join(chr(c) for c in [80, 51])
NRXCHW = "".join(chr(c) for c in [80, 51, 72])
NXNKML = 358
NXWEEZ = "".join(chr(c) for c in [67, 70, 71, 50, 54])
NZMJIG = 282
OACMCV = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
OAWBSI = 378
OCTHBS = "".join(chr(c) for c in [85, 100, 76, 105])
OGMDDP = "".join(chr(c) for c in [67, 70, 71, 49, 52])
OIHBXI = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
OIJUGS = 376
OINELW = 468
OJRJHI = 306
OKPHUO = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
OLSIPM = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
ONFZCZ = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
ONPYYL = 262
OOQNRS = "".join(chr(c) for c in [76, 79, 87])
OPHUGT = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
OUNBLK = 380
OUSPBW = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
OUYNQJ = "".join(
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
PBWJYK = 353
PFTSIF = 279
PHUGTY = 316
PHUOJR = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
PIVLAS = 257
PLSPFT = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
PMDMPS = "".join(chr(c) for c in [76, 73])
PMXFUB = 464
POUYNQ = 268
PQIPOU = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
PSCTTG = 256
PUNRJZ = "".join(chr(c) for c in [83, 79, 117, 116, 52])
PYYLIU = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
QFFTTI = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
QFYLJU = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
QGVUNX = "".join(chr(c) for c in [75, 51, 48, 48])
QIEFXQ = 2
QIPOUY = 267
QJYMOU = "".join(
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
QLNMHX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
QNRSJM = "".join(chr(c) for c in [80, 50])
QNRXCH = "".join(chr(c) for c in [80, 50, 76])
QPLSPF = 277
QRJJJV = "".join(chr(c) for c in [85, 76])
QSNQLN = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
QTDKHT = "".join(chr(c) for c in [67, 70, 71, 54])
QTMFZD = 329
QVXOIH = 340
QXPICX = "".join(chr(c) for c in [76, 79])
RAZMKQ = 451
RJHIUS = 362
RJJJVY = "".join(chr(c) for c in [67, 69])
RJZTAT = 324
RKINEJ = 284
ROGMDD = 461
RSJMCB = "".join(chr(c) for c in [80, 52])
RTFMNH = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
RURAZM = 450
RXAIVE = "".join(chr(c) for c in [67, 70, 71, 51, 49])
RXCHWD = "".join(chr(c) for c in [80, 51, 76])
RYXBQF = "".join(chr(c) for c in [67, 72, 73, 76, 76])
SAKQXP = "".join(chr(c) for c in [65, 76, 76])
SBDJQR = "".join(chr(c) for c in [52, 56, 75])
SCTTGC = 479
SELHBQ = 320
SEMCGE = "".join(chr(c) for c in [83, 79, 117, 116, 57])
SIFJBI = 280
SIPMDM = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
SIRYXB = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
SJMCBF = "".join(chr(c) for c in [80, 53])
SJWMNZ = "".join(
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
SKSOKP = 370
SKWIVD = "".join(chr(c) for c in [75, 56])
SNQLNM = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
SOKPHU = 303
SOOQNR = "".join(chr(c) for c in [72, 73, 71, 72])
SPBWJY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
SPFTSI = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
SROGMD = "".join(chr(c) for c in [67, 70, 71, 49, 51])
SRURAZ = "".join(chr(c) for c in [67, 70, 71, 50])
SSRURA = 449
SSUHBV = "".join(chr(c) for c in [77, 73, 65])
STSEMC = "".join(chr(c) for c in [83, 79, 117, 116, 55])
SUHBVW = "".join(chr(c) for c in [68, 74, 83, 52])
SXUJUT = 310
TACCPQ = 264
TATDZX = "".join(chr(c) for c in [72, 84, 82])
TBJEUT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
TDKHTZ = 454
TDRXAI = "".join(chr(c) for c in [67, 70, 71, 51, 48])
TDZXNQ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
TFMNHT = 295
THBSKS = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
TIDUBS = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
TMFZDG = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
TOPHUG = 301
TSEMCG = "".join(chr(c) for c in [83, 79, 117, 116, 56])
TSIFJB = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
TTIDUB = 288
TYEKCW = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
TYIYWS = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
TZBBEK = 456
UBJLOI = 466
UBSSUH = "".join(chr(c) for c in [105, 110, 88, 69])
UEUHNN = 471
UGTYIY = "".join(chr(c) for c in [70, 117, 108, 108])
UHBVWV = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
UHNNXW = 472
UIKFWR = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
UJUTYE = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
UNBLKX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 79, 110, 122, 101, 110, 68, 117, 114]
)
UNRJZT = 323
UNXNKM = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
UOJRJH = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
UQEXLS = 5
URAZMK = "".join(chr(c) for c in [67, 70, 71, 51])
USOOQN = 261
UTOPHU = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
UXFEFJ = "".join(chr(c) for c in [83, 84, 79, 80])
UYNQJY = 270
VCYWON = "".join(
    chr(c)
    for c in [
        105,
        110,
        70,
        108,
        111,
        82,
        97,
        116,
        105,
        111,
        77,
        97,
        120,
        105,
        109,
        117,
        109,
    ]
)
VDNQGV = "".join(chr(c) for c in [75, 49, 48, 48])
VDQLAI = 309
VDSSRU = 448
VEMVCY = 371
VHFTHE = 6
VKZILX = "".join(
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
VLASSA = "".join(chr(c) for c in [68, 82, 65, 73, 78])
VOACMC = 346
VUBYGD = "".join(chr(c) for c in [105, 110, 89, 84])
VWVUBY = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
VXOIHB = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
WAONPY = 367
WBSIRY = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
WDAFIK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
WEEZFE = "".join(chr(c) for c in [67, 70, 71, 50, 55])
WIVDNQ = "".join(chr(c) for c in [75, 53])
WJYKLG = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
WMNZMJ = "".join(chr(c) for c in [67, 80, 79, 84])
WONFZC = 374
WRKINE = "".join(
    chr(c)
    for c in [
        72,
        116,
        114,
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        66,
        121,
        80,
        119,
        114,
        77,
        110,
        103,
    ]
)
WSKWIV = "".join(chr(c) for c in [75, 56, 53])
WUEUHN = "".join(chr(c) for c in [67, 70, 71, 50, 51])
WVUBYG = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
XAIVEM = 479
XBQFYL = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
XCHWDA = "".join(chr(c) for c in [80, 52, 72])
XEKVKZ = 351
XFEFJT = "".join(chr(c) for c in [83, 84, 65, 82, 84])
XFUBJL = 465
XIBHZV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
XLSXUJ = 7
XNKMLO = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
XNQTMF = 328
XOIHBX = 341
XPICXQ = "".join(chr(c) for c in [72, 73])
XQGLRA = 258
XQIEFX = "".join(chr(c) for c in [85, 100, 80, 50])
XQVXOI = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
XSJWMN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
XTIACQ = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
XUJUTY = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
XWAJVD = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
XWEEZF = 474
XYBQSN = 283
YBQSNQ = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
YEKCWA = 364
YFCRTF = 293
YGDSBD = 290
YIYWSK = 357
YKLGQP = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
YLIUXF = "".join(
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
YLJUIK = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
YMOUNB = "".join(chr(c) for c in [79, 110, 122, 101, 110, 65, 99, 99, 101, 115, 115])
YNQJYM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
YOUSPB = "".join(chr(c) for c in [77, 69, 68])
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YWONFZ = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
YWSKWI = "".join(chr(c) for c in [75, 52, 48, 48])
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = "".join(chr(c) for c in [67, 70, 71, 57])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = "".join(
    chr(c)
    for c in [
        77,
        79,
        68,
        69,
        95,
        49,
        95,
        65,
        78,
        68,
        95,
        72,
        69,
        65,
        84,
        73,
        78,
        71,
        95,
        70,
        65,
        73,
        76,
    ]
)
ZDGKEA = 331
ZFETDR = 476
ZILXWA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
ZMJIGY = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
ZMKQTD = 452
ZTATDZ = 326
ZUQEXL = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
ZVOACM = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
ZXNQTM = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
AFIKJP = [
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
    QNRXCH,
    NRXCHW,
    RXCHWD,
    XCHWDA,
    CHWDAF,
    SJMCBF,
    HWDAFI,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    WDAFIK,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    DAFIKJ,
]
ATDZXN = [
    ELHBQN,
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
    TATDZX,
]
DJQRJJ = [GDSBDJ, DSBDJQ, SBDJQR, BDJQRJ]
DMPSCT = [
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
    JRJHIU,
    JHIUSO,
]
FJTACC = [IUXFEF, UXFEFJ, XFEFJT, FEFJTA, EFJTAC]
FWRKIN = [
    IUXFEF,
    QFYLJU,
    FYLJUI,
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
    YLJUIK,
    LJUIKF,
    JUIKFW,
    UIKFWR,
    IKFWRK,
    KFWRKI,
]
GTYIYW = [HUGTYI, UGTYIY]
IPMDMP = []
JJJVYF = [QRJJJV, RJJJVY]
KSTSEM = [
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
    QNRXCH,
    NRXCHW,
    RXCHWD,
    XCHWDA,
    CHWDAF,
    SJMCBF,
    HWDAFI,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    HECVYY,
    HECVYY,
    AKSTSE,
    HECVYY,
    HECVYY,
    WDAFIK,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    EXLSXU,
    DAFIKJ,
]
LSPFTS = [HECVYY, PLSPFT, PLSPFT, PLSPFT]
MCBFEG = [ASSAKQ, SOOQNR]
MDMPSC = [
    IUSOOQ,
    QNRSJM,
    NRSJMC,
    RSJMCB,
    SJMCBF,
    CBFEGZ,
    BFEGZU,
    FEGZUQ,
    GZUQEX,
    ZUQEXL,
    QEXLSX,
    EXLSXU,
    LSXUJU,
    TYEKCW,
    EKCWAO,
    CWAONP,
    PMDMPS,
]
OQNRSJ = [ASSAKQ, SOOQNR, OOQNRS]
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
QLAIID = [HECVYY, DQLAII, DQLAII, DQLAII]
RAHEOC = [ASSAKQ, LRAHEO]
SSAKQX = [IVLASS, VLASSA, LASSAK, ASSAKQ]
TIXQVX = [
    ELHBQN,
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
    BFEGZU,
]
UBYGDS = [
    DUBSSU,
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
UGSELH = [IJUGSE, JUGSEL]
USPBWJ = [GYOUSP, QXPICX, YOUSPB, XPICXQ, OUSPBW]
UTYEKC = [XUJUTY, UJUTYE, JUTYEK]
VUNXNK = [
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    KWIVDN,
    WIVDNQ,
    IVDNQG,
    VDNQGV,
    DNQGVU,
    HECVYY,
    HECVYY,
    HECVYY,
    NQGVUN,
    QGVUNX,
    GVUNXN,
]
YXBQFY = [IRYXBQ, RYXBQF]
YYLIUX = [NPYYLI, PYYLIU]
ZOLSIP = [ONFZCZ, NFZCZO, FZCZOL, ZCZOLS, CZOLSI]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return MPSCTT

    @property
    def begin(self):
        return PSCTTG

    @property
    def end(self):
        return SCTTGC

    @property
    def all_device_keys(self):
        return MDMPSC

    @property
    def user_demand_keys(self):
        return DMPSCT

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
            BSKSOK: GeckoEnumStructAccessor(
                self.struct, BSKSOK, SKSOKP, None, RAHEOC, None, None, SAKQXP
            ),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, SAKQXP),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, SAKQXP),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, SAKQXP),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, SAKQXP),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, SAKQXP),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, SAKQXP),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, ICXQIE, OQNRSJ, None, CXQIEF, None
            ),
            QNRSJM: GeckoEnumStructAccessor(
                self.struct, QNRSJM, USOOQN, QIEFXQ, OQNRSJ, None, CXQIEF, None
            ),
            NRSJMC: GeckoEnumStructAccessor(
                self.struct, NRSJMC, USOOQN, CXQIEF, OQNRSJ, None, CXQIEF, None
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, USOOQN, VHFTHE, OQNRSJ, None, CXQIEF, None
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, ICXQIE, MCBFEG, None, QIEFXQ, None
            ),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, JMCBFE, AHEOCT, RAHEOC, None, QIEFXQ, None
            ),
            BFEGZU: GeckoEnumStructAccessor(
                self.struct, BFEGZU, JMCBFE, QIEFXQ, RAHEOC, None, QIEFXQ, None
            ),
            FEGZUQ: GeckoEnumStructAccessor(
                self.struct, FEGZUQ, JMCBFE, EGZUQE, RAHEOC, None, QIEFXQ, None
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, JMCBFE, CXQIEF, RAHEOC, None, QIEFXQ, None
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, JMCBFE, UQEXLS, RAHEOC, None, QIEFXQ, None
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, JMCBFE, VHFTHE, RAHEOC, None, QIEFXQ, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, JMCBFE, XLSXUJ, RAHEOC, None, QIEFXQ, None
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, None, UTYEKC, None, None, SAKQXP
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, YEKCWA, None, UTYEKC, None, None, None
            ),
            EKCWAO: GeckoWordStructAccessor(self.struct, EKCWAO, KCWAON, None),
            CWAONP: GeckoWordStructAccessor(self.struct, CWAONP, WAONPY, SAKQXP),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, ONPYYL, ICXQIE, YYLIUX, None, QIEFXQ, SAKQXP
            ),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, FJTACC, None, None, SAKQXP
            ),
            JTACCP: GeckoTimeStructAccessor(self.struct, JTACCP, TACCPQ, SAKQXP),
            ACCPQI: GeckoByteStructAccessor(self.struct, ACCPQI, CCPQIP, SAKQXP),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, ONPYYL, QIEFXQ, YYLIUX, None, QIEFXQ, SAKQXP
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, FJTACC, None, None, SAKQXP
            ),
            IPOUYN: GeckoTimeStructAccessor(self.struct, IPOUYN, POUYNQ, SAKQXP),
            OUYNQJ: GeckoByteStructAccessor(self.struct, OUYNQJ, UYNQJY, SAKQXP),
            YNQJYM: GeckoByteStructAccessor(self.struct, YNQJYM, NQJYMO, SAKQXP),
            QJYMOU: GeckoByteStructAccessor(self.struct, QJYMOU, JYMOUN, SAKQXP),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, ONPYYL, AHEOCT, YYLIUX, None, QIEFXQ, SAKQXP
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, FJTACC, None, None, SAKQXP
            ),
            UNBLKX: GeckoTimeStructAccessor(self.struct, UNBLKX, NBLKXS, SAKQXP),
            BLKXSJ: GeckoBoolStructAccessor(self.struct, BLKXSJ, LKXSJW, ICXQIE, None),
            KXSJWM: GeckoBoolStructAccessor(self.struct, KXSJWM, LKXSJW, QIEFXQ, None),
            XSJWMN: GeckoBoolStructAccessor(self.struct, XSJWMN, LKXSJW, EGZUQE, None),
            SJWMNZ: GeckoBoolStructAccessor(self.struct, SJWMNZ, LKXSJW, CXQIEF, None),
            JWMNZM: GeckoBoolStructAccessor(self.struct, JWMNZM, LKXSJW, UQEXLS, None),
            WMNZMJ: GeckoBoolStructAccessor(self.struct, WMNZMJ, JVHFTH, QIEFXQ, None),
            MNZMJI: GeckoBoolStructAccessor(self.struct, MNZMJI, NZMJIG, EGZUQE, None),
            ZMJIGY: GeckoBoolStructAccessor(self.struct, ZMJIGY, NZMJIG, UQEXLS, None),
            MJIGYO: GeckoBoolStructAccessor(self.struct, MJIGYO, NZMJIG, VHFTHE, None),
            JIGYOU: GeckoEnumStructAccessor(
                self.struct, JIGYOU, IGYOUS, None, USPBWJ, None, None, None
            ),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, PBWJYK, UQEXLS, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, PBWJYK, VHFTHE, None),
            WJYKLG: GeckoWordStructAccessor(self.struct, WJYKLG, JYKLGQ, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, JVHFTH, AHEOCT, None),
            KLGQPL: GeckoTempStructAccessor(self.struct, KLGQPL, LGQPLS, None),
            GQPLSP: GeckoTempStructAccessor(self.struct, GQPLSP, QPLSPF, None),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, JMCBFE, UQEXLS, LSPFTS, None, CXQIEF, None
            ),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, QIEFXQ, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, PFTSIF, VHFTHE, None),
            TSIFJB: GeckoBoolStructAccessor(self.struct, TSIFJB, SIFJBI, QIEFXQ, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, FJBIAM, AHEOCT, None),
            JBIAMJ: GeckoBoolStructAccessor(
                self.struct, JBIAMJ, FJBIAM, QIEFXQ, SAKQXP
            ),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, IAMJMA, AHEOCT, None),
            AMJMAO: GeckoByteStructAccessor(self.struct, AMJMAO, MJMAOA, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MAOAWB, ICXQIE, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, ICXQIE, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, OAWBSI, CXQIEF, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, OAWBSI, UQEXLS, None),
            BSIRYX: GeckoBoolStructAccessor(self.struct, BSIRYX, OAWBSI, VHFTHE, None),
            SIRYXB: GeckoEnumStructAccessor(
                self.struct, SIRYXB, OAWBSI, XLSXUJ, YXBQFY, None, QIEFXQ, SAKQXP
            ),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, FWRKIN, None, None, None
            ),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, RKINEJ, ICXQIE, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, RKINEJ, AHEOCT, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, NEJNIB, ICXQIE, None),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, NEJNIB, AHEOCT, None),
            JNIBXY: GeckoBoolStructAccessor(self.struct, JNIBXY, JVHFTH, EGZUQE, None),
            NIBXYB: GeckoBoolStructAccessor(self.struct, NIBXYB, NZMJIG, ICXQIE, None),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, NZMJIG, AHEOCT, None),
            BXYBQS: GeckoBoolStructAccessor(self.struct, BXYBQS, XYBQSN, QIEFXQ, None),
            YBQSNQ: GeckoBoolStructAccessor(self.struct, YBQSNQ, XYBQSN, EGZUQE, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, RKINEJ, EGZUQE, None),
            QSNQLN: GeckoBoolStructAccessor(self.struct, QSNQLN, RKINEJ, CXQIEF, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, RKINEJ, UQEXLS, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, RKINEJ, VHFTHE, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, NEJNIB, EGZUQE, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, NEJNIB, CXQIEF, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, NEJNIB, UQEXLS, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, NEJNIB, VHFTHE, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, XEKVKZ, QIEFXQ, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, XEKVKZ, EGZUQE, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, IAMJMA, EGZUQE, None),
            VKZILX: GeckoBoolStructAccessor(self.struct, VKZILX, PBWJYK, ICXQIE, None),
            KZILXW: GeckoBoolStructAccessor(self.struct, KZILXW, PBWJYK, AHEOCT, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, ILXWAJ, ICXQIE, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, SIFJBI, ICXQIE, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, XYBQSN, ICXQIE, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, XYBQSN, AHEOCT, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, XYBQSN, CXQIEF, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, VDQLAI, ICXQIE, None),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, VDQLAI, AHEOCT, QLAIID, None, CXQIEF, None
            ),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, VDQLAI, EGZUQE, None),
            AIIDNI: GeckoWordStructAccessor(self.struct, AIIDNI, IIDNIB, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, DNIBXT, ICXQIE, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, IBXTIA, ICXQIE, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, IBXTIA, AHEOCT, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, XEKVKZ, ICXQIE, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, XEKVKZ, AHEOCT, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, XEKVKZ, CXQIEF, None),
            ACQFFT: GeckoWordStructAccessor(self.struct, ACQFFT, CQFFTT, None),
            QFFTTI: GeckoByteStructAccessor(self.struct, QFFTTI, FFTTID, None),
            FTTIDU: GeckoByteStructAccessor(self.struct, FTTIDU, TTIDUB, None),
            TIDUBS: GeckoEnumStructAccessor(
                self.struct, TIDUBS, IDUBSS, None, UBYGDS, None, None, None
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, YGDSBD, ICXQIE, DJQRJJ, None, CXQIEF, None
            ),
            JQRJJJ: GeckoEnumStructAccessor(
                self.struct, JQRJJJ, YGDSBD, QIEFXQ, JJJVYF, None, QIEFXQ, None
            ),
            JJVYFC: GeckoWordStructAccessor(self.struct, JJVYFC, JVYFCR, None),
            VYFCRT: GeckoByteStructAccessor(self.struct, VYFCRT, YFCRTF, None),
            FCRTFM: GeckoByteStructAccessor(self.struct, FCRTFM, CRTFMN, None),
            RTFMNH: GeckoByteStructAccessor(self.struct, RTFMNH, TFMNHT, None),
            FMNHTB: GeckoByteStructAccessor(self.struct, FMNHTB, MNHTBJ, None),
            NHTBJE: GeckoWordStructAccessor(self.struct, NHTBJE, HTBJEU, None),
            TBJEUT: GeckoByteStructAccessor(self.struct, TBJEUT, BJEUTO, None),
            JEUTOP: GeckoByteStructAccessor(self.struct, JEUTOP, EUTOPH, None),
            UTOPHU: GeckoWordStructAccessor(self.struct, UTOPHU, TOPHUG, None),
            OPHUGT: GeckoEnumStructAccessor(
                self.struct, OPHUGT, PHUGTY, None, GTYIYW, None, QIEFXQ, SAKQXP
            ),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, YIYWSK, None, VUNXNK, None, None, None
            ),
            UNXNKM: GeckoWordStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, None),
            LOIJUG: GeckoEnumStructAccessor(
                self.struct, LOIJUG, OIJUGS, None, UGSELH, None, None, SAKQXP
            ),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, SELHBQ, None, AFIKJP, None, None, SAKQXP
            ),
            FIKJPU: GeckoEnumStructAccessor(
                self.struct, FIKJPU, IKJPUN, None, AFIKJP, None, None, SAKQXP
            ),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, JPUNRJ, None, AFIKJP, None, None, SAKQXP
            ),
            PUNRJZ: GeckoEnumStructAccessor(
                self.struct, PUNRJZ, UNRJZT, None, AFIKJP, None, None, SAKQXP
            ),
            NRJZTA: GeckoEnumStructAccessor(
                self.struct, NRJZTA, RJZTAT, None, AFIKJP, None, None, SAKQXP
            ),
            JZTATD: GeckoEnumStructAccessor(
                self.struct, JZTATD, ZTATDZ, None, ATDZXN, None, None, SAKQXP
            ),
            TDZXNQ: GeckoByteStructAccessor(self.struct, TDZXNQ, DZXNQT, SAKQXP),
            ZXNQTM: GeckoByteStructAccessor(self.struct, ZXNQTM, XNQTMF, SAKQXP),
            NQTMFZ: GeckoByteStructAccessor(self.struct, NQTMFZ, QTMFZD, SAKQXP),
            TMFZDG: GeckoByteStructAccessor(self.struct, TMFZDG, MFZDGK, SAKQXP),
            FZDGKE: GeckoByteStructAccessor(self.struct, FZDGKE, ZDGKEA, SAKQXP),
            DGKEAK: GeckoByteStructAccessor(self.struct, DGKEAK, GKEAKS, SAKQXP),
            KEAKST: GeckoEnumStructAccessor(
                self.struct, KEAKST, EAKSTS, None, KSTSEM, None, None, SAKQXP
            ),
            STSEMC: GeckoEnumStructAccessor(
                self.struct, STSEMC, ZTATDZ, None, KSTSEM, None, None, SAKQXP
            ),
            TSEMCG: GeckoEnumStructAccessor(
                self.struct, TSEMCG, DZXNQT, None, KSTSEM, None, None, SAKQXP
            ),
            SEMCGE: GeckoEnumStructAccessor(
                self.struct, SEMCGE, XNQTMF, None, KSTSEM, None, None, SAKQXP
            ),
            EMCGET: GeckoEnumStructAccessor(
                self.struct, EMCGET, QTMFZD, None, KSTSEM, None, None, SAKQXP
            ),
            MCGETI: GeckoEnumStructAccessor(
                self.struct, MCGETI, MFZDGK, None, KSTSEM, None, None, SAKQXP
            ),
            CGETIX: GeckoEnumStructAccessor(
                self.struct, CGETIX, ZDGKEA, None, KSTSEM, None, None, SAKQXP
            ),
            GETIXQ: GeckoEnumStructAccessor(
                self.struct, GETIXQ, ETIXQV, None, TIXQVX, None, None, SAKQXP
            ),
            IXQVXO: GeckoEnumStructAccessor(
                self.struct, IXQVXO, GKEAKS, None, TIXQVX, None, None, SAKQXP
            ),
            XQVXOI: GeckoByteStructAccessor(self.struct, XQVXOI, QVXOIH, SAKQXP),
            VXOIHB: GeckoByteStructAccessor(self.struct, VXOIHB, XOIHBX, SAKQXP),
            OIHBXI: GeckoByteStructAccessor(self.struct, OIHBXI, IHBXIB, SAKQXP),
            HBXIBH: GeckoByteStructAccessor(self.struct, HBXIBH, BXIBHZ, SAKQXP),
            XIBHZV: GeckoByteStructAccessor(self.struct, XIBHZV, IBHZVO, SAKQXP),
            BHZVOA: GeckoByteStructAccessor(self.struct, BHZVOA, HZVOAC, SAKQXP),
            ZVOACM: GeckoByteStructAccessor(self.struct, ZVOACM, VOACMC, SAKQXP),
            OACMCV: GeckoByteStructAccessor(self.struct, OACMCV, ACMCVD, SAKQXP),
            CMCVDS: GeckoByteStructAccessor(self.struct, CMCVDS, MCVDSS, SAKQXP),
            AIVEMV: GeckoBoolStructAccessor(self.struct, AIVEMV, JVHFTH, UQEXLS, None),
            IVEMVC: GeckoByteStructAccessor(self.struct, IVEMVC, VEMVCY, SAKQXP),
            EMVCYW: GeckoByteStructAccessor(self.struct, EMVCYW, MVCYWO, SAKQXP),
            VCYWON: GeckoByteStructAccessor(self.struct, VCYWON, CYWONF, SAKQXP),
            YWONFZ: GeckoEnumStructAccessor(
                self.struct, YWONFZ, WONFZC, None, ZOLSIP, None, None, SAKQXP
            ),
            OLSIPM: GeckoBoolStructAccessor(
                self.struct, OLSIPM, LSIPMD, ICXQIE, SAKQXP
            ),
            SIPMDM: GeckoBoolStructAccessor(self.struct, SIPMDM, OIJUGS, ICXQIE, None),
        }

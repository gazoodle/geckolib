#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v80'
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
ACMCVD = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
ACQFFT = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
AFIKJP = "".join(chr(c) for c in [75, 56, 53])
AIIDNI = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
AIVEMV = "".join(chr(c) for c in [67, 70, 71, 49, 51])
AJVDQL = "".join(
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
AKQXPI = "".join(chr(c) for c in [65, 76, 76])
AKSTSE = "".join(chr(c) for c in [80, 52, 76])
AMJMAO = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
AOAWBS = "".join(chr(c) for c in [72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116])
AOESVZ = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
AONPYY = 310
APUMEA = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
ATDZXN = 358
AWBSIR = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
AXNCUG = "".join(chr(c) for c in [67, 70, 71, 51, 48])
AZMKQT = 328
BBEKBD = 333
BDFSRO = 341
BDJQRJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
BEKBDF = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
BFEGZU = 261
BHZVOA = 337
BIAMJM = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
BJEUTO = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
BJLOIN = "".join(chr(c) for c in [67, 70, 71, 48])
BLKXSJ = "".join(
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
BMJVHF = 256
BQFYLJ = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
BQNRXC = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
BQSNQL = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
BSIRYX = 280
BSKSOK = 258
BSSUHB = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        101,
        97,
        116,
        80,
        117,
        109,
        112,
        69,
        114,
        114,
        111,
        114,
        73,
        68,
    ]
)
BVNAXA = 256
BVWVUB = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
BWJYKL = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
BXIBHZ = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
BXTIAC = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
BXYBQS = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
BYGDSB = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
CBFEGZ = "".join(chr(c) for c in [80, 49])
CCPQIP = "".join(
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
CGETIX = "".join(chr(c) for c in [83, 79, 117, 116, 51])
CHWDAF = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
CMCVDS = 349
CPQIPO = 263
CQBMJV = 317
CQFFTT = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
CRHYUA = 475
CRTFMN = 288
CTHBSK = "".join(chr(c) for c in [85, 100, 80, 51])
CTTGCR = 473
CUGUCY = 479
CVDSSR = 325
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = 7
CXQIEF = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
CYRAPU = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
CYWONF = "".join(chr(c) for c in [67, 70, 71, 49, 54])
CZOLSI = 467
DAFIKJ = "".join(chr(c) for c in [75, 52, 48, 48])
DDPMXF = 345
DFSROG = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
DGKEAK = "".join(chr(c) for c in [80, 50, 76])
DJQRJJ = 315
DKHTZB = 331
DMPSCT = 471
DNIBXT = 283
DPMXFU = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
DQLAII = "".join(
    chr(c)
    for c in [
        83,
        105,
        108,
        101,
        110,
        116,
        77,
        111,
        100,
        101,
        65,
        99,
        116,
        105,
        118,
        101,
    ]
)
DRXAIV = 459
DSBDJQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
DUBSSU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
DZXNQT = 360
EAKSTS = "".join(chr(c) for c in [80, 52, 72])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 456
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
EFXQGL = "".join(chr(c) for c in [83, 79, 65, 75])
EGZUQE = "".join(chr(c) for c in [76, 79, 87])
EJNIBX = 379
EKBDFS = 340
EKCWAO = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
EKVKZI = "".join(chr(c) for c in [71, 69, 78, 69, 82, 73, 67])
ELHBQN = 300
ELWUEU = "".join(chr(c) for c in [67, 70, 71, 51])
EMCGET = "".join(chr(c) for c in [83, 79, 117, 116, 50])
EMVCYW = 462
EOCTHB = "".join(chr(c) for c in [85, 100, 80, 50])
ETDRXA = 458
ETIXQV = "".join(chr(c) for c in [83, 79, 117, 116, 52])
EUHNNX = "".join(chr(c) for c in [67, 70, 71, 53])
EUTOPH = "".join(chr(c) for c in [75, 54, 48, 48])
EXLSXU = "".join(chr(c) for c in [80, 53])
EZFETD = "".join(chr(c) for c in [67, 70, 71, 57])
FCRTFM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
FEFJTA = 367
FEGZUQ = "".join(chr(c) for c in [72, 73, 71, 72])
FETDRX = "".join(chr(c) for c in [67, 70, 71, 49, 48])
FFTTID = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
FIKJPU = "".join(chr(c) for c in [75, 56])
FJBIAM = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
FJTACC = 262
FMNHTB = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
FSROGM = 342
FTHECV = 319
FTSIFJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
FTTIDU = 351
FUBJLO = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
FWRKIN = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
FXQGLR = "".join(chr(c) for c in [79, 70, 70])
FYLJUI = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
FZCZOL = 466
FZDGKE = "".join(chr(c) for c in [80, 49, 76])
GCRHYU = "".join(chr(c) for c in [67, 70, 71, 50, 55])
GDSBDJ = 311
GETIXQ = 322
GKEAKS = "".join(chr(c) for c in [80, 51, 72])
GLRAHE = 259
GMDDPM = 344
GQPLSP = "".join(chr(c) for c in [78, 79])
GSELHB = 299
GTYIYW = "".join(chr(c) for c in [49, 54, 75])
GUCYRA = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
GVUNXN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
GYOUSP = "".join(chr(c) for c in [70, 105, 108, 116, 82, 101, 113, 117, 101, 115, 116])
HBQNRX = 301
HBSKSO = "".join(chr(c) for c in [85, 100, 80, 53])
HBVWVU = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
HBXIBH = 335
HECVYY = "".join(chr(c) for c in [])
HEOCTH = 4
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
HNNXWE = "".join(chr(c) for c in [67, 70, 71, 54])
HTBJEU = "".join(chr(c) for c in [77, 73, 65])
HTZBBE = 332
HUGTYI = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
HUOJRJ = "".join(chr(c) for c in [85, 100, 76, 105])
HWDAFI = 357
HXEKVK = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        101,
        97,
        116,
        80,
        117,
        109,
        112,
        84,
        121,
        112,
        101,
    ]
)
HYUAXN = 476
HZVOAC = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
IACQFF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
IAMJMA = 277
IBHZVO = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
IBXTIA = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
IBXYBQ = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
ICXQIE = 1
IDNIBX = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
IDUBSS = "".join(
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
IEFXQG = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IFJBIA = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
IGYOUS = 273
IHBXIB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
IIDNIB = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
IJUGSE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
IKFWRK = "".join(
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
IKJPUN = "".join(chr(c) for c in [75, 52])
ILXWAJ = 390
INELWU = "".join(chr(c) for c in [67, 70, 71, 50])
IPIVLA = "".join(
    chr(c)
    for c in [
        69,
        120,
        101,
        114,
        99,
        105,
        115,
        101,
        68,
        101,
        116,
        101,
        99,
        116,
        101,
        100,
        84,
        121,
        112,
        101,
    ]
)
IPMDMP = "".join(chr(c) for c in [67, 70, 71, 50, 50])
IPOUYN = "".join(chr(c) for c in [83, 84, 65, 82, 84])
IRYXBQ = 281
IUSOOQ = 303
IUXFEF = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
IVDNQG = "".join(chr(c) for c in [52, 84, 72, 95, 71, 69, 78])
IVEMVC = 461
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 73, 78, 83, 84, 65, 76, 76, 69, 68])
IXQVXO = "".join(chr(c) for c in [83, 79, 117, 116, 53])
IYWSKW = "".join(chr(c) for c in [54, 52, 75])
JBIAMJ = 275
JEUTOP = "".join(chr(c) for c in [105, 110, 88, 77])
JHIUSO = 370
JIGYOU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
JJJVYF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
JJVYFC = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
JLOINE = 448
JMAOAW = "".join(chr(c) for c in [78, 101, 97, 114, 72, 76])
JMCBFE = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JNIBXY = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
JPUNRJ = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
JQRJJJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
JRJHIU = 363
JTACCP = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JUGSEL = 297
JUIKFW = 378
JUTYEK = 3
JVDQLA = 350
JVHFTH = 274
JVYFCR = 285
JWMNZM = 272
JYKLGQ = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
JYMOUN = 266
JZTATD = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
KBDFSR = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
KCWAON = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
KEAKST = "".join(chr(c) for c in [80, 51, 76])
KFWRKI = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
KHTZBB = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
KINEJN = "".join(chr(c) for c in [67, 72, 73, 76, 76])
KJPUNR = "".join(chr(c) for c in [75, 53])
KLGQPL = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
KMLOIJ = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
KPHUOJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
KQTDKH = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
KQXPIC = "".join(
    chr(c)
    for c in [
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        82,
        101,
        113,
        117,
        101,
        115,
        116,
    ]
)
KSOKPH = "".join(chr(c) for c in [85, 100, 66, 76])
KSTSEM = "".join(chr(c) for c in [66, 76, 79])
KVKZIL = "".join(chr(c) for c in [71, 69, 67, 75, 79, 95, 53, 48, 48, 48, 87])
KWIVDN = "".join(chr(c) for c in [50, 78, 68, 95, 71, 69, 78])
KXSJWM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
LAIIDN = "".join(
    chr(c)
    for c in [
        83,
        105,
        108,
        101,
        110,
        116,
        77,
        111,
        100,
        101,
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
LASSAK = "".join(chr(c) for c in [84, 82, 69, 65, 68, 77, 73, 76, 76])
LGQPLS = 313
LHBQNR = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
LIUXFE = 364
LJUIKF = "".join(
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
LKXSJW = 270
LNMHXE = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        80,
        67,
        65,
        109,
        98,
        105,
        101,
        110,
        116,
        80,
        114,
        111,
        116,
        101,
        99,
        116,
        105,
        111,
        110,
    ]
)
LOIJUG = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
LOINEL = "".join(chr(c) for c in [67, 70, 71, 49])
LRAHEO = "".join(chr(c) for c in [76, 79])
LSIPMD = "".join(chr(c) for c in [67, 70, 71, 50, 49])
LWUEUH = 451
LXWAJV = "".join(
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
MAOAWB = 279
MCBFEG = 369
MCGETI = 321
MCVDSS = "".join(chr(c) for c in [83, 79, 117, 116, 54])
MDDPMX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
MDMPSC = "".join(chr(c) for c in [67, 70, 71, 50, 51])
MEAOES = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
MFZDGK = "".join(chr(c) for c in [80, 49, 72])
MHXEKV = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        80,
        67,
        65,
        99,
        116,
        105,
        118,
        101,
        67,
        104,
        101,
        99,
        107,
        70,
        108,
        111,
        119,
    ]
)
MJIGYO = 381
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 329
MLOIJU = 295
MNHTBJ = "".join(chr(c) for c in [105, 110, 88, 69])
MNZMJI = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        65,
        99,
        116,
        105,
        111,
        110,
    ]
)
MOUNBL = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
MPSCTT = "".join(chr(c) for c in [67, 70, 71, 50, 52])
MVCYWO = "".join(chr(c) for c in [67, 70, 71, 49, 53])
MXFUBJ = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
NBLKXS = 268
NCUGUC = "".join(chr(c) for c in [67, 70, 71, 51, 49])
NEJNIB = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
NELWUE = 450
NFZCZO = "".join(chr(c) for c in [67, 70, 71, 49, 56])
NHTBJE = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
NIBXTI = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
NIBXYB = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
NKMLOI = 294
NMHXEK = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        80,
        67,
        82,
        101,
        113,
        117,
        101,
        115,
        116,
        70,
        108,
        111,
        119,
    ]
)
NNXWEE = 454
NPYYLI = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
NQGVUN = 8
NQJYMO = 264
NQLNMH = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        80,
        67,
        79,
        117,
        116,
        108,
        101,
        116,
        80,
        114,
        111,
        116,
        101,
        99,
        116,
        105,
        111,
        110,
    ]
)
NQTMFZ = "".join(chr(c) for c in [83, 79, 117, 116, 49])
NRJZTA = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
NRSJMC = 306
NRXCHW = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
NXNKML = 293
NXWEEZ = "".join(chr(c) for c in [67, 70, 71, 55])
NZMJIG = 380
OACMCV = 339
OAWBSI = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
OCTHBS = 2
OESVZS = 375
OGMDDP = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
OIJUGS = 296
OINELW = 449
OJRJHI = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
OLSIPM = 468
ONFZCZ = 465
ONPYYL = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
OOQNRS = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
OPHUGT = "".join(chr(c) for c in [105, 110, 89, 84])
OQNRSJ = 305
OUNBLK = 267
OUSPBW = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
OUYNQJ = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
PBWJYK = "".join(chr(c) for c in [67, 80, 79, 84])
PFTSIF = 353
PHUOJR = 308
PICXQI = "".join(
    chr(c)
    for c in [
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        85,
        115,
        101,
        114,
        79,
        102,
        102,
    ]
)
PIVLAS = 385
PLSPFT = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
PMDMPS = 470
PMXFUB = 346
POUYNQ = "".join(chr(c) for c in [78, 69, 87])
PQIPOU = "".join(chr(c) for c in [73, 68, 76, 69])
PSCTTG = 472
PUMEAO = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
PUNRJZ = "".join(chr(c) for c in [75, 49, 48, 48])
PYYLIU = "".join(chr(c) for c in [70, 85, 76, 76])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [80, 52])
QFFTTI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
QFYLJU = 377
QGLRAH = "".join(chr(c) for c in [85, 100, 80, 49])
QGVUNX = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 50, 53, 54, 75])
QIEFXQ = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
QIPOUY = "".join(chr(c) for c in [83, 84, 79, 80])
QJYMOU = "".join(
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
QLAIID = 383
QLNMHX = 392
QNRSJM = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
QNRXCH = 316
QPLSPF = "".join(chr(c) for c in [77, 69, 68])
QRJJJV = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
QSNQLN = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
QTDKHT = 330
QTMFZD = 320
QVXOIH = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
QXPICX = 388
RAHEOC = "".join(chr(c) for c in [72, 73])
RAPUME = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
RAZMKQ = "".join(chr(c) for c in [83, 79, 117, 116, 57])
RHYUAX = "".join(chr(c) for c in [67, 70, 71, 50, 56])
RJHIUS = "".join(chr(c) for c in [85, 100, 65, 117, 120])
RJJJVY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
RJZTAT = "".join(chr(c) for c in [75, 51, 48, 48])
RKINEJ = "".join(chr(c) for c in [72, 69, 65, 84])
ROGMDD = 343
RSJMCB = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
RTFMNH = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
RURAZM = "".join(chr(c) for c in [83, 79, 117, 116, 56])
RXAIVE = "".join(chr(c) for c in [67, 70, 71, 49, 50])
RXCHWD = "".join(chr(c) for c in [70, 117, 108, 108])
RYXBQF = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
SAKQXP = 386
SBDJQR = 314
SBVNAX = 80
SCTTGC = "".join(chr(c) for c in [67, 70, 71, 50, 53])
SELHBQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
SIFJBI = 355
SIPMDM = 469
SIRYXB = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
SJMCBF = 362
SJWMNZ = "".join(
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
SKWIVD = "".join(chr(c) for c in [49, 83, 84, 95, 71, 69, 78])
SOKPHU = "".join(chr(c) for c in [79, 78])
SOOQNR = 304
SPBWJY = "".join(
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
SPFTSI = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
SROGMD = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
SRURAZ = 326
SSAKQX = "".join(
    chr(c)
    for c in [
        69,
        120,
        101,
        114,
        99,
        105,
        115,
        101,
        73,
        110,
        116,
        101,
        110,
        115,
        105,
        116,
        121,
    ]
)
SSRURA = "".join(chr(c) for c in [83, 79, 117, 116, 55])
SSUHBV = 387
STSEMC = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SUHBVW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
SVZSSB = "".join(chr(c) for c in [76, 73])
SXUJUT = "".join(chr(c) for c in [66, 76])
TACCPQ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
TATDZX = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
TBJEUT = "".join(chr(c) for c in [68, 74, 83, 52])
TDKHTZ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
TDRXAI = "".join(chr(c) for c in [67, 70, 71, 49, 49])
TDZXNQ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
TFMNHT = 289
TGCRHY = 474
THBSKS = "".join(chr(c) for c in [85, 100, 80, 52])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
TIDUBS = "".join(
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
TIXQVX = 323
TMFZDG = "".join(chr(c) for c in [78, 65])
TOPHUG = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
TSEMCG = "".join(chr(c) for c in [65, 85, 88])
TSIFJB = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
TTGCRH = "".join(chr(c) for c in [67, 70, 71, 50, 54])
TTIDUB = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
TYEKCW = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
TYIYWS = "".join(chr(c) for c in [51, 50, 75])
UAXNCU = 477
UBJLOI = 348
UBSSUH = 354
UCYRAP = 371
UEUHNN = 452
UGSELH = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
UGTYIY = 290
UGUCYR = "".join(
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
UHBVWV = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
UHNNXW = 453
UIKFWR = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        101,
        97,
        116,
        80,
        117,
        109,
        112,
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
UJUTYE = "".join(chr(c) for c in [79, 51])
UMEAOE = "".join(
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
UNBLKX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
UNRJZT = "".join(chr(c) for c in [75, 56, 48, 48])
UNXNKM = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
UOJRJH = 307
UQEXLS = "".join(chr(c) for c in [80, 51])
URAZMK = 327
USOOQN = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
USPBWJ = "".join(
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
UTOPHU = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
UTYEKC = "".join(chr(c) for c in [76, 49, 50, 48])
UXFEFJ = 365
VCYWON = 463
VDNQGV = "".join(chr(c) for c in [53, 84, 72, 95, 71, 69, 78])
VDQLAI = "".join(
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
VDSSRU = "".join(chr(c) for c in [70, 97, 110])
VEMVCY = "".join(chr(c) for c in [67, 70, 71, 49, 52])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [71, 69, 67, 75, 79, 55, 53, 48, 48, 87])
VLASSA = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
VNAXAD = 479
VOACMC = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
VUBYGD = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
VUNXNK = 291
VWVUBY = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
VXOIHB = 334
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(
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
WAONPY = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
WBSIRY = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
WDAFIK = "".join(chr(c) for c in [75, 50, 48, 48])
WEEZFE = "".join(chr(c) for c in [67, 70, 71, 56])
WIVDNQ = "".join(chr(c) for c in [51, 82, 68, 95, 71, 69, 78])
WJYKLG = 282
WMNZMJ = "".join(
    chr(c)
    for c in [80, 114, 111, 103, 79, 117, 116, 112, 117, 116, 65, 99, 99, 101, 115, 115]
)
WONFZC = "".join(chr(c) for c in [67, 70, 71, 49, 55])
WRKINE = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
WSKWIV = "".join(
    chr(c) for c in [80, 97, 99, 107, 71, 101, 110, 101, 114, 97, 116, 105, 111, 110]
)
WUEUHN = "".join(chr(c) for c in [67, 70, 71, 52])
WVUBYG = 309
XAIVEM = 460
XBQFYL = 352
XEKVKZ = 389
XFEFJT = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
XFUBJL = 347
XIBHZV = 336
XLSXUJ = 260
XNCUGU = 478
XNKMLO = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
XNQTMF = 361
XOIHBX = "".join(chr(c) for c in [72, 84, 82])
XPICXQ = 0
XQIEFX = 257
XQVXOI = 324
XSJWMN = 271
XTIACQ = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
XUJUTY = "".join(chr(c) for c in [67, 80])
XWAJVD = 284
XWEEZF = 455
XYBQSN = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
YBQSNQ = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
YEKCWA = 5
YFCRTF = 287
YGDSBD = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
YIYWSK = "".join(chr(c) for c in [52, 56, 75])
YKLGQP = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
YLIUXF = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
YLJUIK = 384
YMOUNB = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
YNQJYM = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YOUSPB = "".join(chr(c) for c in [80, 117, 114, 103, 101])
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YRAPUM = 374
YUAXNC = "".join(chr(c) for c in [67, 70, 71, 50, 57])
YWONFZ = 464
YXBQFY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = "".join(chr(c) for c in [67, 70, 71, 49, 57])
ZDGKEA = "".join(chr(c) for c in [80, 50, 72])
ZFETDR = 457
ZILXWA = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        98,
        117,
        115,
        72,
        101,
        97,
        116,
        80,
        117,
        109,
        112,
        65,
        109,
        98,
        105,
        101,
        110,
        116,
    ]
)
ZMJIGY = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        111,
        116,
        101,
        80,
        114,
        111,
        103,
        79,
        117,
        116,
        112,
        117,
        116,
        68,
        117,
        114,
    ]
)
ZMKQTD = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
ZOLSIP = "".join(chr(c) for c in [67, 70, 71, 50, 48])
ZUQEXL = "".join(chr(c) for c in [80, 50])
ZVOACM = 338
ZXNQTM = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
ACCPQI = [JTACCP, TACCPQ]
AHEOCT = [FXQGLR, LRAHEO, RAHEOC]
ASSAKQ = [IVLASS, VLASSA, LASSAK]
DNQGVU = [SKWIVD, KWIVDN, HECVYY, WIVDNQ, HECVYY, IVDNQG, HECVYY, VDNQGV]
DSSRUR = [
    TMFZDG,
    MFZDGK,
    FZDGKE,
    ZDGKEA,
    DGKEAK,
    GKEAKS,
    KEAKST,
    EAKSTS,
    AKSTSE,
    EXLSXU,
    KSTSEM,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    HECVYY,
    HECVYY,
    VDSSRU,
    HECVYY,
    HECVYY,
    STSEMC,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    KCWAON,
    TSEMCG,
]
EAOESV = [RAPUME, APUMEA, PUMEAO, UMEAOE, MEAOES]
ESVZSS = []
GZUQEX = [FXQGLR, FEGZUQ, EGZUQE]
INEJNI = [RKINEJ, KINEJN]
KZILXW = [EKVKZI, KVKZIL, VKZILX]
LSPFTS = [GQPLSP, LRAHEO, QPLSPF, RAHEOC, PLSPFT]
LSXUJU = [FXQGLR, FEGZUQ]
MJMAOA = [HECVYY, AMJMAO, AMJMAO, AMJMAO]
OIHBXI = [
    TMFZDG,
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
    XOIHBX,
]
OKPHUO = [FXQGLR, SOKPHU]
PHUGTY = [
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
    TBJEUT,
    BJEUTO,
    JEUTOP,
    EUTOPH,
    UTOPHU,
    TOPHUG,
    OPHUGT,
]
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
SEMCGE = [
    TMFZDG,
    MFZDGK,
    FZDGKE,
    ZDGKEA,
    DGKEAK,
    GKEAKS,
    KEAKST,
    EAKSTS,
    AKSTSE,
    EXLSXU,
    KSTSEM,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    STSEMC,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    KCWAON,
    TSEMCG,
]
SKSOKP = [FXQGLR, RAHEOC]
SNQLNM = [
    PQIPOU,
    JNIBXY,
    NIBXYB,
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
    IBXYBQ,
    BXYBQS,
    XYBQSN,
    YBQSNQ,
    BQSNQL,
    QSNQLN,
]
SSBVNA = [
    QRJJJV,
    TTIDUB,
    IDUBSS,
    BXTIAC,
    IFJBIA,
    BYGDSB,
    JQRJJJ,
    RJJJVY,
    OAWBSI,
    SPBWJY,
    QFFTTI,
    IACQFF,
    YXBQFY,
    BDJQRJ,
    TIACQF,
    FFTTID,
    CQFFTT,
    NIBXTI,
    DUBSSU,
    IDNIBX,
    AIIDNI,
    HBVWVU,
    TIDUBS,
    IIDNIB,
    BSSUHB,
    ACQFFT,
    XTIACQ,
    IBXTIA,
]
TZBBEK = [
    TMFZDG,
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
    XUJUTY,
]
UBYGDS = [HECVYY, VUBYGD, VUBYGD, VUBYGD]
UYNQJY = [PQIPOU, QIPOUY, IPOUYN, POUYNQ, OUYNQJ]
VZSSBV = [
    CBFEGZ,
    ZUQEXL,
    UQEXLS,
    QEXLSX,
    EXLSXU,
    SXUJUT,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    TYEKCW,
    EKCWAO,
    KCWAON,
    WAONPY,
    YLIUXF,
    IUXFEF,
    XFEFJT,
    SVZSSB,
]
XCHWDA = [NRXCHW, RXCHWD]
XQGLRA = [QIEFXQ, IEFXQG, EFXQGL, FXQGLR]
YWSKWI = [GTYIYW, TYIYWS, YIYWSK, IYWSKW]
YYLIUX = [ONPYYL, NPYYLI, PYYLIU]
ZSSBVN = [
    QGLRAH,
    EOCTHB,
    CTHBSK,
    THBSKS,
    HBSKSO,
    KSOKPH,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RJHIUS,
    HIUSOO,
    USOOQN,
    OOQNRS,
    QNRSJM,
    RSJMCB,
    JMCBFE,
]
ZTATDZ = [
    WDAFIK,
    DAFIKJ,
    AFIKJP,
    FIKJPU,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
    PUNRJZ,
    UNRJZT,
    HECVYY,
    HECVYY,
    HECVYY,
    NRJZTA,
    RJZTAT,
    JZTATD,
]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return SBVNAX

    @property
    def begin(self):
        return BVNAXA

    @property
    def end(self):
        return VNAXAD

    @property
    def all_device_keys(self):
        return VZSSBV

    @property
    def user_demand_keys(self):
        return ZSSBVN

    @property
    def error_keys(self):
        return SSBVNA

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
                self.struct, IPIVLA, PIVLAS, None, ASSAKQ, None, None, None
            ),
            SSAKQX: GeckoByteStructAccessor(self.struct, SSAKQX, SAKQXP, AKQXPI),
            KQXPIC: GeckoBoolStructAccessor(self.struct, KQXPIC, QXPICX, XPICXQ, None),
            PICXQI: GeckoBoolStructAccessor(self.struct, PICXQI, QXPICX, ICXQIE, None),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, XQGLRA, None, None, AKQXPI
            ),
            QGLRAH: GeckoEnumStructAccessor(
                self.struct, QGLRAH, GLRAHE, XPICXQ, AHEOCT, None, HEOCTH, AKQXPI
            ),
            EOCTHB: GeckoEnumStructAccessor(
                self.struct, EOCTHB, GLRAHE, OCTHBS, AHEOCT, None, HEOCTH, AKQXPI
            ),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, GLRAHE, HEOCTH, AHEOCT, None, HEOCTH, AKQXPI
            ),
            THBSKS: GeckoEnumStructAccessor(
                self.struct, THBSKS, GLRAHE, VHFTHE, AHEOCT, None, HEOCTH, AKQXPI
            ),
            HBSKSO: GeckoEnumStructAccessor(
                self.struct, HBSKSO, BSKSOK, XPICXQ, SKSOKP, None, OCTHBS, AKQXPI
            ),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, BSKSOK, ICXQIE, OKPHUO, None, OCTHBS, AKQXPI
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, OKPHUO, None, None, AKQXPI
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, SKSOKP, None, None, AKQXPI
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, OKPHUO, None, None, AKQXPI
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, OKPHUO, None, None, AKQXPI
            ),
            HIUSOO: GeckoByteStructAccessor(self.struct, HIUSOO, IUSOOQ, AKQXPI),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, AKQXPI),
            OOQNRS: GeckoByteStructAccessor(self.struct, OOQNRS, OQNRSJ, AKQXPI),
            QNRSJM: GeckoByteStructAccessor(self.struct, QNRSJM, NRSJMC, AKQXPI),
            RSJMCB: GeckoByteStructAccessor(self.struct, RSJMCB, SJMCBF, AKQXPI),
            JMCBFE: GeckoByteStructAccessor(self.struct, JMCBFE, MCBFEG, AKQXPI),
            CBFEGZ: GeckoEnumStructAccessor(
                self.struct, CBFEGZ, BFEGZU, XPICXQ, GZUQEX, None, HEOCTH, None
            ),
            ZUQEXL: GeckoEnumStructAccessor(
                self.struct, ZUQEXL, BFEGZU, OCTHBS, GZUQEX, None, HEOCTH, None
            ),
            UQEXLS: GeckoEnumStructAccessor(
                self.struct, UQEXLS, BFEGZU, HEOCTH, GZUQEX, None, HEOCTH, None
            ),
            QEXLSX: GeckoEnumStructAccessor(
                self.struct, QEXLSX, BFEGZU, VHFTHE, GZUQEX, None, HEOCTH, None
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, XPICXQ, LSXUJU, None, OCTHBS, None
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XLSXUJ, ICXQIE, OKPHUO, None, OCTHBS, None
            ),
            XUJUTY: GeckoEnumStructAccessor(
                self.struct, XUJUTY, XLSXUJ, OCTHBS, OKPHUO, None, OCTHBS, None
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, XLSXUJ, JUTYEK, OKPHUO, None, OCTHBS, None
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, XLSXUJ, HEOCTH, OKPHUO, None, OCTHBS, None
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, XLSXUJ, YEKCWA, OKPHUO, None, OCTHBS, None
            ),
            EKCWAO: GeckoEnumStructAccessor(
                self.struct, EKCWAO, XLSXUJ, VHFTHE, OKPHUO, None, OCTHBS, None
            ),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, XLSXUJ, CWAONP, OKPHUO, None, OCTHBS, None
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, YYLIUX, None, None, AKQXPI
            ),
            YLIUXF: GeckoEnumStructAccessor(
                self.struct, YLIUXF, LIUXFE, None, YYLIUX, None, None, None
            ),
            IUXFEF: GeckoWordStructAccessor(self.struct, IUXFEF, UXFEFJ, None),
            XFEFJT: GeckoWordStructAccessor(self.struct, XFEFJT, FEFJTA, AKQXPI),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, XPICXQ, ACCPQI, None, OCTHBS, AKQXPI
            ),
            CCPQIP: GeckoEnumStructAccessor(
                self.struct, CCPQIP, CPQIPO, None, UYNQJY, None, None, AKQXPI
            ),
            YNQJYM: GeckoTimeStructAccessor(self.struct, YNQJYM, NQJYMO, AKQXPI),
            QJYMOU: GeckoByteStructAccessor(self.struct, QJYMOU, JYMOUN, AKQXPI),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, FJTACC, OCTHBS, ACCPQI, None, OCTHBS, AKQXPI
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, UYNQJY, None, None, AKQXPI
            ),
            UNBLKX: GeckoTimeStructAccessor(self.struct, UNBLKX, NBLKXS, AKQXPI),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, AKQXPI),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, AKQXPI),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, AKQXPI),
            WMNZMJ: GeckoEnumStructAccessor(
                self.struct, WMNZMJ, FJTACC, ICXQIE, ACCPQI, None, OCTHBS, AKQXPI
            ),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, UYNQJY, None, None, AKQXPI
            ),
            ZMJIGY: GeckoTimeStructAccessor(self.struct, ZMJIGY, MJIGYO, AKQXPI),
            JIGYOU: GeckoBoolStructAccessor(self.struct, JIGYOU, IGYOUS, XPICXQ, None),
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, IGYOUS, ICXQIE, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, IGYOUS, OCTHBS, None),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, IGYOUS, JUTYEK, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, IGYOUS, HEOCTH, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, IGYOUS, YEKCWA, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, JVHFTH, OCTHBS, None),
            BWJYKL: GeckoBoolStructAccessor(self.struct, BWJYKL, WJYKLG, JUTYEK, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, WJYKLG, YEKCWA, None),
            YKLGQP: GeckoBoolStructAccessor(self.struct, YKLGQP, WJYKLG, VHFTHE, None),
            KLGQPL: GeckoEnumStructAccessor(
                self.struct, KLGQPL, LGQPLS, None, LSPFTS, None, None, None
            ),
            SPFTSI: GeckoBoolStructAccessor(self.struct, SPFTSI, PFTSIF, YEKCWA, None),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, PFTSIF, VHFTHE, None),
            TSIFJB: GeckoWordStructAccessor(self.struct, TSIFJB, SIFJBI, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, JVHFTH, ICXQIE, None),
            FJBIAM: GeckoTempStructAccessor(self.struct, FJBIAM, JBIAMJ, None),
            BIAMJM: GeckoTempStructAccessor(self.struct, BIAMJM, IAMJMA, None),
            AMJMAO: GeckoEnumStructAccessor(
                self.struct, AMJMAO, XLSXUJ, YEKCWA, MJMAOA, None, HEOCTH, None
            ),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MAOAWB, XPICXQ, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, MAOAWB, ICXQIE, None),
            OAWBSI: GeckoBoolStructAccessor(self.struct, OAWBSI, MAOAWB, OCTHBS, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, MAOAWB, VHFTHE, None),
            WBSIRY: GeckoBoolStructAccessor(self.struct, WBSIRY, BSIRYX, OCTHBS, None),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, IRYXBQ, ICXQIE, None),
            RYXBQF: GeckoBoolStructAccessor(
                self.struct, RYXBQF, IRYXBQ, OCTHBS, AKQXPI
            ),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, XBQFYL, ICXQIE, None),
            BQFYLJ: GeckoByteStructAccessor(self.struct, BQFYLJ, QFYLJU, None),
            FYLJUI: GeckoBoolStructAccessor(self.struct, FYLJUI, YLJUIK, XPICXQ, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, JUIKFW, XPICXQ, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, JUIKFW, ICXQIE, None),
            IKFWRK: GeckoBoolStructAccessor(self.struct, IKFWRK, JUIKFW, HEOCTH, None),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, JUIKFW, YEKCWA, None),
            FWRKIN: GeckoBoolStructAccessor(self.struct, FWRKIN, JUIKFW, VHFTHE, None),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, JUIKFW, CWAONP, INEJNI, None, OCTHBS, AKQXPI
            ),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, EJNIBX, None, SNQLNM, None, None, None
            ),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, QLNMHX, XPICXQ, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, QLNMHX, ICXQIE, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, QLNMHX, OCTHBS, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, QLNMHX, JUTYEK, None),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, XEKVKZ, None, KZILXW, None, None, None
            ),
            ZILXWA: GeckoWordStructAccessor(self.struct, ZILXWA, ILXWAJ, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, XWAJVD, XPICXQ, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, XWAJVD, ICXQIE, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, JVDQLA, XPICXQ, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, JVDQLA, ICXQIE, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, QLAIID, XPICXQ, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, QLAIID, ICXQIE, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, WJYKLG, XPICXQ, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, WJYKLG, ICXQIE, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, DNIBXT, OCTHBS, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, DNIBXT, JUTYEK, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, XWAJVD, JUTYEK, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, XWAJVD, HEOCTH, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, XWAJVD, YEKCWA, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, XWAJVD, VHFTHE, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, JVDQLA, JUTYEK, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, JVDQLA, HEOCTH, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, JVDQLA, YEKCWA, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, JVDQLA, VHFTHE, None),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, FTTIDU, OCTHBS, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, FTTIDU, JUTYEK, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, PFTSIF, XPICXQ, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, PFTSIF, ICXQIE, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, UBSSUH, XPICXQ, None),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, BSIRYX, XPICXQ, None),
            UHBVWV: GeckoBoolStructAccessor(self.struct, UHBVWV, DNIBXT, XPICXQ, None),
            HBVWVU: GeckoBoolStructAccessor(self.struct, HBVWVU, DNIBXT, ICXQIE, None),
            BVWVUB: GeckoBoolStructAccessor(self.struct, BVWVUB, DNIBXT, HEOCTH, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, WVUBYG, XPICXQ, None),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, WVUBYG, ICXQIE, UBYGDS, None, HEOCTH, None
            ),
            BYGDSB: GeckoBoolStructAccessor(self.struct, BYGDSB, WVUBYG, JUTYEK, None),
            YGDSBD: GeckoWordStructAccessor(self.struct, YGDSBD, GDSBDJ, None),
            DSBDJQ: GeckoBoolStructAccessor(self.struct, DSBDJQ, SBDJQR, XPICXQ, None),
            BDJQRJ: GeckoBoolStructAccessor(self.struct, BDJQRJ, DJQRJJ, XPICXQ, None),
            JQRJJJ: GeckoBoolStructAccessor(self.struct, JQRJJJ, DJQRJJ, ICXQIE, None),
            QRJJJV: GeckoBoolStructAccessor(self.struct, QRJJJV, FTTIDU, XPICXQ, None),
            RJJJVY: GeckoBoolStructAccessor(self.struct, RJJJVY, FTTIDU, ICXQIE, None),
            JJJVYF: GeckoBoolStructAccessor(self.struct, JJJVYF, FTTIDU, HEOCTH, None),
            JJVYFC: GeckoWordStructAccessor(self.struct, JJVYFC, JVYFCR, None),
            VYFCRT: GeckoByteStructAccessor(self.struct, VYFCRT, YFCRTF, None),
            FCRTFM: GeckoByteStructAccessor(self.struct, FCRTFM, CRTFMN, None),
            RTFMNH: GeckoEnumStructAccessor(
                self.struct, RTFMNH, TFMNHT, None, PHUGTY, None, None, None
            ),
            HUGTYI: GeckoEnumStructAccessor(
                self.struct, HUGTYI, UGTYIY, XPICXQ, YWSKWI, None, HEOCTH, None
            ),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, UGTYIY, JUTYEK, DNQGVU, None, NQGVUN, None
            ),
            QGVUNX: GeckoBoolStructAccessor(self.struct, QGVUNX, UGTYIY, VHFTHE, None),
            GVUNXN: GeckoWordStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoByteStructAccessor(self.struct, KMLOIJ, MLOIJU, None),
            LOIJUG: GeckoByteStructAccessor(self.struct, LOIJUG, OIJUGS, None),
            IJUGSE: GeckoWordStructAccessor(self.struct, IJUGSE, JUGSEL, None),
            UGSELH: GeckoByteStructAccessor(self.struct, UGSELH, GSELHB, None),
            SELHBQ: GeckoByteStructAccessor(self.struct, SELHBQ, ELHBQN, None),
            LHBQNR: GeckoWordStructAccessor(self.struct, LHBQNR, HBQNRX, None),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, QNRXCH, None, XCHWDA, None, OCTHBS, AKQXPI
            ),
            CHWDAF: GeckoEnumStructAccessor(
                self.struct, CHWDAF, HWDAFI, None, ZTATDZ, None, None, None
            ),
            TATDZX: GeckoWordStructAccessor(self.struct, TATDZX, ATDZXN, None),
            TDZXNQ: GeckoByteStructAccessor(self.struct, TDZXNQ, DZXNQT, None),
            ZXNQTM: GeckoByteStructAccessor(self.struct, ZXNQTM, XNQTMF, None),
            NQTMFZ: GeckoEnumStructAccessor(
                self.struct, NQTMFZ, QTMFZD, None, SEMCGE, None, None, AKQXPI
            ),
            EMCGET: GeckoEnumStructAccessor(
                self.struct, EMCGET, MCGETI, None, SEMCGE, None, None, AKQXPI
            ),
            CGETIX: GeckoEnumStructAccessor(
                self.struct, CGETIX, GETIXQ, None, SEMCGE, None, None, AKQXPI
            ),
            ETIXQV: GeckoEnumStructAccessor(
                self.struct, ETIXQV, TIXQVX, None, SEMCGE, None, None, AKQXPI
            ),
            IXQVXO: GeckoEnumStructAccessor(
                self.struct, IXQVXO, XQVXOI, None, SEMCGE, None, None, AKQXPI
            ),
            QVXOIH: GeckoEnumStructAccessor(
                self.struct, QVXOIH, VXOIHB, None, OIHBXI, None, None, AKQXPI
            ),
            IHBXIB: GeckoByteStructAccessor(self.struct, IHBXIB, HBXIBH, AKQXPI),
            BXIBHZ: GeckoByteStructAccessor(self.struct, BXIBHZ, XIBHZV, AKQXPI),
            IBHZVO: GeckoByteStructAccessor(self.struct, IBHZVO, BHZVOA, AKQXPI),
            HZVOAC: GeckoByteStructAccessor(self.struct, HZVOAC, ZVOACM, AKQXPI),
            VOACMC: GeckoByteStructAccessor(self.struct, VOACMC, OACMCV, AKQXPI),
            ACMCVD: GeckoByteStructAccessor(self.struct, ACMCVD, CMCVDS, AKQXPI),
            MCVDSS: GeckoEnumStructAccessor(
                self.struct, MCVDSS, CVDSSR, None, DSSRUR, None, None, AKQXPI
            ),
            SSRURA: GeckoEnumStructAccessor(
                self.struct, SSRURA, SRURAZ, None, DSSRUR, None, None, AKQXPI
            ),
            RURAZM: GeckoEnumStructAccessor(
                self.struct, RURAZM, URAZMK, None, DSSRUR, None, None, AKQXPI
            ),
            RAZMKQ: GeckoEnumStructAccessor(
                self.struct, RAZMKQ, AZMKQT, None, DSSRUR, None, None, AKQXPI
            ),
            ZMKQTD: GeckoEnumStructAccessor(
                self.struct, ZMKQTD, MKQTDK, None, DSSRUR, None, None, AKQXPI
            ),
            KQTDKH: GeckoEnumStructAccessor(
                self.struct, KQTDKH, QTDKHT, None, DSSRUR, None, None, AKQXPI
            ),
            TDKHTZ: GeckoEnumStructAccessor(
                self.struct, TDKHTZ, DKHTZB, None, DSSRUR, None, None, AKQXPI
            ),
            KHTZBB: GeckoEnumStructAccessor(
                self.struct, KHTZBB, HTZBBE, None, TZBBEK, None, None, AKQXPI
            ),
            ZBBEKB: GeckoEnumStructAccessor(
                self.struct, ZBBEKB, BBEKBD, None, TZBBEK, None, None, AKQXPI
            ),
            BEKBDF: GeckoByteStructAccessor(self.struct, BEKBDF, EKBDFS, AKQXPI),
            KBDFSR: GeckoByteStructAccessor(self.struct, KBDFSR, BDFSRO, AKQXPI),
            DFSROG: GeckoByteStructAccessor(self.struct, DFSROG, FSROGM, AKQXPI),
            SROGMD: GeckoByteStructAccessor(self.struct, SROGMD, ROGMDD, AKQXPI),
            OGMDDP: GeckoByteStructAccessor(self.struct, OGMDDP, GMDDPM, AKQXPI),
            MDDPMX: GeckoByteStructAccessor(self.struct, MDDPMX, DDPMXF, AKQXPI),
            DPMXFU: GeckoByteStructAccessor(self.struct, DPMXFU, PMXFUB, AKQXPI),
            MXFUBJ: GeckoByteStructAccessor(self.struct, MXFUBJ, XFUBJL, AKQXPI),
            FUBJLO: GeckoByteStructAccessor(self.struct, FUBJLO, UBJLOI, AKQXPI),
            UGUCYR: GeckoBoolStructAccessor(self.struct, UGUCYR, JVHFTH, YEKCWA, None),
            GUCYRA: GeckoByteStructAccessor(self.struct, GUCYRA, UCYRAP, AKQXPI),
            CYRAPU: GeckoEnumStructAccessor(
                self.struct, CYRAPU, YRAPUM, None, EAOESV, None, None, AKQXPI
            ),
            AOESVZ: GeckoBoolStructAccessor(
                self.struct, AOESVZ, OESVZS, XPICXQ, AKQXPI
            ),
        }

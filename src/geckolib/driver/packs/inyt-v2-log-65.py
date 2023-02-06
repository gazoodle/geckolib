#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT-V2 v65'
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
ACMCVD = "".join(chr(c) for c in [83, 79, 117, 116, 56])
ACQFFT = "".join(
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
AFIKJP = 358
AIIDNI = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
AIVEMV = "".join(chr(c) for c in [67, 70, 71, 50, 48])
AJVDQL = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
AKQXPI = "".join(chr(c) for c in [65, 76, 76])
AKSTSE = "".join(chr(c) for c in [83, 79, 117, 116, 51])
AOAWBS = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
AOESVZ = 479
AONPYY = 310
ATDZXN = "".join(chr(c) for c in [78, 65])
AWBSIR = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
AXNCUG = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
AZMKQT = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
BBEKBD = 346
BDFSRO = 348
BDJQRJ = 285
BEKBDF = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
BFEGZU = 261
BHZVOA = "".join(chr(c) for c in [83, 79, 117, 116, 54])
BIAMJM = 277
BJEUTO = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
BJLOIN = "".join(chr(c) for c in [67, 70, 71, 55])
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
BQFYLJ = 384
BQNRXC = "".join(chr(c) for c in [75, 53])
BQSNQL = "".join(
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
BSIRYX = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
BSKSOK = 258
BSSUHB = 309
BVWVUB = 311
BWJYKL = 282
BXIBHZ = 331
BXTIAC = 351
BXYBQS = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
BYGDSB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
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
CGETIX = 326
CHWDAF = "".join(chr(c) for c in [75, 51, 48, 48])
CMCVDS = "".join(chr(c) for c in [83, 79, 117, 116, 57])
CPQIPO = 263
CQBMJV = 317
CQFFTT = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
CRHYUA = "".join(
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
CRTFMN = "".join(chr(c) for c in [68, 74, 83, 52])
CTHBSK = "".join(chr(c) for c in [85, 100, 80, 51])
CTTGCR = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
CUGUCY = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
CVDSSR = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = 7
CXQIEF = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
CYRAPU = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
CYWONF = "".join(chr(c) for c in [67, 70, 71, 50, 51])
CZOLSI = 474
DAFIKJ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
DDPMXF = 451
DFSROG = "".join(chr(c) for c in [67, 70, 71, 48])
DGKEAK = "".join(chr(c) for c in [65, 85, 88])
DJQRJJ = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
DKHTZB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
DMPSCT = 478
DNIBXT = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
DNQGVU = 296
DPMXFU = "".join(chr(c) for c in [67, 70, 71, 52])
DQLAII = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
DRXAIV = 466
DSBDJQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
DSSRUR = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
DUBSSU = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
DZXNQT = "".join(chr(c) for c in [80, 49, 76])
EAKSTS = 321
EAOESV = 256
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 463
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
EFXQGL = "".join(chr(c) for c in [83, 79, 65, 75])
EGZUQE = "".join(chr(c) for c in [76, 79, 87])
EJNIBX = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
EKBDFS = 347
EKCWAO = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
EKVKZI = "".join(
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
ELHBQN = "".join(chr(c) for c in [75, 56, 53])
ELWUEU = "".join(chr(c) for c in [67, 70, 71, 49, 48])
EMCGET = 324
EMVCYW = 469
EOCTHB = "".join(chr(c) for c in [85, 100, 80, 50])
ETDRXA = 465
EUHNNX = "".join(chr(c) for c in [67, 70, 71, 49, 50])
EUTOPH = "".join(chr(c) for c in [49, 54, 75])
EXLSXU = "".join(chr(c) for c in [80, 53])
EZFETD = "".join(chr(c) for c in [67, 70, 71, 49, 54])
FCRTFM = "".join(chr(c) for c in [77, 73, 65])
FEFJTA = 367
FEGZUQ = "".join(chr(c) for c in [72, 73, 71, 72])
FETDRX = "".join(chr(c) for c in [67, 70, 71, 49, 55])
FFTTID = "".join(
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
FIKJPU = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
FJBIAM = 275
FJTACC = 262
FMNHTB = "".join(chr(c) for c in [75, 54, 48, 48])
FSROGM = 448
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
FTTIDU = 387
FUBJLO = "".join(chr(c) for c in [67, 70, 71, 54])
FWRKIN = "".join(chr(c) for c in [67, 72, 73, 76, 76])
FXQGLR = "".join(chr(c) for c in [79, 70, 70])
FYLJUI = 378
FZCZOL = 473
FZDGKE = "".join(chr(c) for c in [66, 76, 79])
GCRHYU = 372
GDSBDJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
GETIXQ = "".join(chr(c) for c in [72, 84, 82])
GLRAHE = 259
GMDDPM = 450
GQPLSP = "".join(chr(c) for c in [77, 69, 68])
GSELHB = "".join(chr(c) for c in [75, 50, 48, 48])
GTYIYW = "".join(chr(c) for c in [67, 69])
GUCYRA = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
GVUNXN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
GYOUSP = "".join(chr(c) for c in [80, 117, 114, 103, 101])
HBQNRX = "".join(chr(c) for c in [75, 52])
HBSKSO = "".join(chr(c) for c in [85, 100, 80, 53])
HBVWVU = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
HBXIBH = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = 4
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
HNNXWE = "".join(chr(c) for c in [67, 70, 71, 49, 51])
HTBJEU = "".join(chr(c) for c in [105, 110, 89, 84])
HTZBBE = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
HUGTYI = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
HUOJRJ = "".join(chr(c) for c in [85, 100, 76, 105])
HWDAFI = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
HXEKVK = "".join(
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
HYUAXN = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
HZVOAC = 325
IACQFF = "".join(
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
IAMJMA = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
IBHZVO = 333
IBXTIA = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
IBXYBQ = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
ICXQIE = 1
IDNIBX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
IDUBSS = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
IEFXQG = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IFJBIA = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
IGYOUS = 273
IHBXIB = 330
IIDNIB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
IKFWRK = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
IKJPUN = 360
ILXWAJ = 383
INEJNI = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
INELWU = "".join(chr(c) for c in [67, 70, 71, 57])
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
IPMDMP = "".join(chr(c) for c in [67, 70, 71, 50, 57])
IPOUYN = "".join(chr(c) for c in [83, 84, 65, 82, 84])
IRYXBQ = 352
IUSOOQ = 303
IUXFEF = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
IVDNQG = 295
IVEMVC = 468
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 73, 78, 83, 84, 65, 76, 76, 69, 68])
IXQVXO = 327
IYWSKW = 291
JBIAMJ = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
JEUTOP = 290
JHIUSO = 370
JIGYOU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
JJJVYF = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
JJVYFC = 289
JLOINE = 455
JMAOAW = 279
JMCBFE = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JNIBXY = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
JPUNRJ = 361
JQRJJJ = 287
JRJHIU = 363
JTACCP = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JUGSEL = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
JUIKFW = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
JUTYEK = 3
JVDQLA = 283
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
JWMNZM = 272
JYKLGQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYMOUN = 266
KBDFSR = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
KCWAON = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
KEAKST = "".join(chr(c) for c in [83, 79, 117, 116, 50])
KFWRKI = "".join(chr(c) for c in [72, 69, 65, 84])
KHTZBB = 344
KINEJN = 379
KJPUNR = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
KLGQPL = 313
KMLOIJ = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
KPHUOJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
KQTDKH = 342
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
KSTSEM = 322
KVKZIL = "".join(
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
KWIVDN = 294
KXSJWM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
KZILXW = "".join(
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
LAIIDN = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
LASSAK = "".join(chr(c) for c in [84, 82, 69, 65, 68, 77, 73, 76, 76])
LGQPLS = "".join(chr(c) for c in [78, 79])
LHBQNR = "".join(chr(c) for c in [75, 56])
LIUXFE = 364
LJUIKF = "".join(
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
LKXSJW = 270
LOIJUG = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
LOINEL = "".join(chr(c) for c in [67, 70, 71, 56])
LRAHEO = "".join(chr(c) for c in [76, 79])
LSIPMD = "".join(chr(c) for c in [67, 70, 71, 50, 56])
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
LWUEUH = 458
LXWAJV = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
)
MAOAWB = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
MCBFEG = 369
MCGETI = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
MCVDSS = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
MDDPMX = "".join(chr(c) for c in [67, 70, 71, 51])
MDMPSC = "".join(chr(c) for c in [67, 70, 71, 51, 48])
MEAOES = 65
MFZDGK = "".join(chr(c) for c in [80, 52, 76])
MHXEKV = 390
MJIGYO = 381
MJMAOA = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
MLOIJU = 316
MNHTBJ = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
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
MPSCTT = "".join(chr(c) for c in [67, 70, 71, 51, 49])
MVCYWO = "".join(chr(c) for c in [67, 70, 71, 50, 50])
MXFUBJ = "".join(chr(c) for c in [67, 70, 71, 53])
NBLKXS = 268
NCUGUC = "".join(
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
NEJNIB = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
NELWUE = 457
NFZCZO = "".join(chr(c) for c in [67, 70, 71, 50, 53])
NHTBJE = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
NIBXTI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
NIBXYB = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
NKMLOI = 301
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
NNXWEE = 461
NPYYLI = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
NQGVUN = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
NQJYMO = 264
NQLNMH = "".join(chr(c) for c in [71, 69, 67, 75, 79, 95, 53, 48, 48, 48, 87])
NQTMFZ = "".join(chr(c) for c in [80, 51, 72])
NRJZTA = "".join(chr(c) for c in [45, 45, 45])
NRSJMC = 306
NRXCHW = "".join(chr(c) for c in [75, 49, 48, 48])
NXNKML = 300
NXWEEZ = "".join(chr(c) for c in [67, 70, 71, 49, 52])
NZMJIG = 380
OACMCV = "".join(chr(c) for c in [83, 79, 117, 116, 55])
OAWBSI = 280
OCTHBS = 2
OGMDDP = "".join(chr(c) for c in [67, 70, 71, 50])
OIHBXI = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
OIJUGS = "".join(chr(c) for c in [70, 117, 108, 108])
OINELW = 456
OJRJHI = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
OLSIPM = 475
ONFZCZ = 472
ONPYYL = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
OOQNRS = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
OPHUGT = "".join(chr(c) for c in [54, 52, 75])
OQNRSJ = 305
OUNBLK = 267
OUSPBW = "".join(
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
OUYNQJ = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
PBWJYK = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
PFTSIF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
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
PMDMPS = 477
PMXFUB = 452
POUYNQ = "".join(chr(c) for c in [78, 69, 87])
PQIPOU = "".join(chr(c) for c in [73, 68, 76, 69])
PSCTTG = 479
PUNRJZ = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
PYYLIU = "".join(chr(c) for c in [70, 85, 76, 76])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [80, 52])
QFFTTI = 354
QFYLJU = "".join(
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
QGLRAH = "".join(chr(c) for c in [85, 100, 80, 49])
QGVUNX = 297
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
QLAIID = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
QLNMHX = "".join(chr(c) for c in [71, 69, 67, 75, 79, 55, 53, 48, 48, 87])
QNRSJM = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
QNRXCH = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
QPLSPF = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QRJJJV = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
QSNQLN = 389
QTDKHT = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
QTMFZD = "".join(chr(c) for c in [80, 51, 76])
QVXOIH = 328
QXPICX = 388
RAHEOC = "".join(chr(c) for c in [72, 73])
RAPUME = "".join(chr(c) for c in [76, 73])
RAZMKQ = 340
RHYUAX = 373
RJHIUS = "".join(chr(c) for c in [85, 100, 65, 117, 120])
RJJJVY = 288
RJZTAT = "".join(chr(c) for c in [82, 69, 83, 69, 84])
RKINEJ = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
ROGMDD = 449
RSJMCB = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
RTFMNH = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
RURAZM = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
RXAIVE = "".join(chr(c) for c in [67, 70, 71, 49, 57])
RXCHWD = "".join(chr(c) for c in [75, 56, 48, 48])
RYXBQF = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
SAKQXP = 386
SBDJQR = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
SCTTGC = "".join(
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
SELHBQ = "".join(chr(c) for c in [75, 52, 48, 48])
SEMCGE = "".join(chr(c) for c in [83, 79, 117, 116, 53])
SIFJBI = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SIPMDM = 476
SIRYXB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
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
SKWIVD = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
SNQLNM = "".join(chr(c) for c in [71, 69, 78, 69, 82, 73, 67])
SOKPHU = "".join(chr(c) for c in [79, 78])
SOOQNR = 304
SPBWJY = "".join(chr(c) for c in [67, 80, 79, 84])
SPFTSI = 353
SROGMD = "".join(chr(c) for c in [67, 70, 71, 49])
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
SSRURA = 332
SSUHBV = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
STSEMC = "".join(chr(c) for c in [83, 79, 117, 116, 52])
SXUJUT = "".join(chr(c) for c in [66, 76])
TACCPQ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
TATDZX = 320
TDKHTZ = 343
TDRXAI = "".join(chr(c) for c in [67, 70, 71, 49, 56])
TDZXNQ = "".join(chr(c) for c in [80, 49, 72])
TFMNHT = "".join(chr(c) for c in [105, 110, 88, 77])
TGCRHY = "".join(
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
THBSKS = "".join(chr(c) for c in [85, 100, 80, 52])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(
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
TIDUBS = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
TIXQVX = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
TMFZDG = "".join(chr(c) for c in [80, 52, 72])
TOPHUG = "".join(chr(c) for c in [52, 56, 75])
TSEMCG = 323
TSIFJB = 355
TTGCRH = 371
TTIDUB = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
TYEKCW = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
TZBBEK = 345
UAXNCU = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
UBJLOI = 454
UBSSUH = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
UBYGDS = 315
UCYRAP = 375
UEUHNN = 459
UGSELH = 357
UGTYIY = "".join(chr(c) for c in [85, 76])
UHBVWV = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
UHNNXW = 460
UIKFWR = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
UJUTYE = "".join(chr(c) for c in [79, 51])
UNBLKX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
UNRJZT = 376
UNXNKM = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
UOJRJH = 307
UQEXLS = "".join(chr(c) for c in [80, 51])
URAZMK = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
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
        69,
        114,
        114,
    ]
)
UTOPHU = "".join(chr(c) for c in [51, 50, 75])
UTYEKC = "".join(chr(c) for c in [76, 49, 50, 48])
UXFEFJ = 365
VCYWON = 470
VDNQGV = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
VDQLAI = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
VDSSRU = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
VEMVCY = "".join(chr(c) for c in [67, 70, 71, 50, 49])
VHFTHE = 6
VKZILX = 350
VLASSA = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
VUBYGD = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
VUNXNK = 299
VWVUBY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
VXOIHB = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
VYFCRT = "".join(chr(c) for c in [105, 110, 88, 69])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
WAJVDQ = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
WAONPY = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
WBSIRY = 281
WEEZFE = "".join(chr(c) for c in [67, 70, 71, 49, 53])
WIVDNQ = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
WJYKLG = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
WMNZMJ = "".join(
    chr(c)
    for c in [80, 114, 111, 103, 79, 117, 116, 112, 117, 116, 65, 99, 99, 101, 115, 115]
)
WONFZC = "".join(chr(c) for c in [67, 70, 71, 50, 52])
WSKWIV = 293
WUEUHN = "".join(chr(c) for c in [67, 70, 71, 49, 49])
WVUBYG = 314
XAIVEM = 467
XBQFYL = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
XCHWDA = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
XEKVKZ = 284
XFEFJT = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
XFUBJL = 453
XIBHZV = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
XLSXUJ = 260
XNCUGU = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
XNKMLO = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
XNQTMF = "".join(chr(c) for c in [80, 50, 76])
XOIHBX = 329
XPICXQ = 0
XQIEFX = 257
XQVXOI = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
XSJWMN = 271
XTIACQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
XUJUTY = "".join(chr(c) for c in [67, 80])
XWAJVD = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
XWEEZF = 462
XYBQSN = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
YEKCWA = 5
YFCRTF = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
YGDSBD = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
YIYWSK = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
YKLGQP = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
YLIUXF = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
YLJUIK = "".join(
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
YMOUNB = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
YNQJYM = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
YOUSPB = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YUAXNC = 374
YWONFZ = 471
YWSKWI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
YXBQFY = 377
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = "".join(chr(c) for c in [67, 70, 71, 50, 54])
ZDGKEA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
ZFETDR = 464
ZILXWA = "".join(
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
ZMKQTD = 341
ZOLSIP = "".join(chr(c) for c in [67, 70, 71, 50, 55])
ZTATDZ = "".join(chr(c) for c in [83, 79, 117, 116, 49])
ZUQEXL = "".join(chr(c) for c in [80, 50])
ZVOACM = "".join(chr(c) for c in [70, 97, 110])
ZXNQTM = "".join(chr(c) for c in [80, 50, 72])
ACCPQI = [JTACCP, TACCPQ]
AHEOCT = [FXQGLR, LRAHEO, RAHEOC]
AMJMAO = [HECVYY, IAMJMA, IAMJMA, IAMJMA]
APUMEA = [
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
    RAPUME,
]
ASSAKQ = [IVLASS, VLASSA, LASSAK]
ETIXQV = [
    ATDZXN,
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
    GETIXQ,
]
GKEAKS = [
    ATDZXN,
    TDZXNQ,
    DZXNQT,
    ZXNQTM,
    XNQTMF,
    NQTMFZ,
    QTMFZD,
    TMFZDG,
    MFZDGK,
    EXLSXU,
    FZDGKE,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    ZDGKEA,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    KCWAON,
    DGKEAK,
]
GZUQEX = [FXQGLR, FEGZUQ, EGZUQE]
IJUGSE = [LOIJUG, OIJUGS]
JZTATD = [NRJZTA, RJZTAT]
LNMHXE = [SNQLNM, NQLNMH, QLNMHX]
LSXUJU = [FXQGLR, FEGZUQ]
OKPHUO = [FXQGLR, SOKPHU]
PHUGTY = [EUTOPH, UTOPHU, TOPHUG, OPHUGT]
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
PLSPFT = [LGQPLS, LRAHEO, GQPLSP, RAHEOC, QPLSPF]
PUMEAO = [
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
SKSOKP = [FXQGLR, RAHEOC]
SRURAZ = [
    ATDZXN,
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
SUHBVW = [HECVYY, SSUHBV, SSUHBV, SSUHBV]
TBJEUT = [
    JVYFCR,
    VYFCRT,
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
    FMNHTB,
    MNHTBJ,
    NHTBJE,
    HTBJEU,
]
TYIYWS = [UGTYIY, GTYIYW]
UGUCYR = [UAXNCU, AXNCUG, XNCUGU, NCUGUC, CUGUCY]
UMEAOE = [
    YGDSBD,
    XTIACQ,
    ACQFFT,
    QLAIID,
    SIFJBI,
    UHBVWV,
    BYGDSB,
    GDSBDJ,
    MJMAOA,
    USPBWJ,
    NIBXTI,
    IIDNIB,
    LXWAJV,
    SIRYXB,
    VUBYGD,
    AIIDNI,
    IBXTIA,
    DNIBXT,
    VDQLAI,
    CQFFTT,
    AJVDQL,
    XWAJVD,
    TIACQF,
    IDUBSS,
    IACQFF,
    WAJVDQ,
    FFTTID,
    IDNIBX,
    LAIIDN,
    DQLAII,
]
UYNQJY = [PQIPOU, QIPOUY, IPOUYN, POUYNQ, OUYNQJ]
VOACMC = [
    ATDZXN,
    TDZXNQ,
    DZXNQT,
    ZXNQTM,
    XNQTMF,
    NQTMFZ,
    QTMFZD,
    TMFZDG,
    MFZDGK,
    EXLSXU,
    FZDGKE,
    XUJUTY,
    UJUTYE,
    UTYEKC,
    HECVYY,
    HECVYY,
    ZVOACM,
    HECVYY,
    HECVYY,
    ZDGKEA,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    KCWAON,
    DGKEAK,
]
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
    HECVYY,
    HECVYY,
    HECVYY,
    XCHWDA,
    CHWDAF,
    HWDAFI,
]
WRKINE = [KFWRKI, FWRKIN]
XQGLRA = [QIEFXQ, IEFXQG, EFXQGL, FXQGLR]
YBQSNQ = [
    PQIPOU,
    INEJNI,
    NEJNIB,
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
    EJNIBX,
    JNIBXY,
    NIBXYB,
    IBXYBQ,
    BXYBQS,
    XYBQSN,
]
YRAPUM = []
YYLIUX = [ONPYYL, NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return MEAOES

    @property
    def begin(self):
        return EAOESV

    @property
    def end(self):
        return AOESVZ

    @property
    def all_device_keys(self):
        return APUMEA

    @property
    def user_demand_keys(self):
        return PUMEAO

    @property
    def error_keys(self):
        return UMEAOE

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
            GYOUSP: GeckoBoolStructAccessor(self.struct, GYOUSP, IGYOUS, OCTHBS, None),
            YOUSPB: GeckoBoolStructAccessor(self.struct, YOUSPB, IGYOUS, JUTYEK, None),
            OUSPBW: GeckoBoolStructAccessor(self.struct, OUSPBW, IGYOUS, HEOCTH, None),
            USPBWJ: GeckoBoolStructAccessor(self.struct, USPBWJ, IGYOUS, YEKCWA, None),
            SPBWJY: GeckoBoolStructAccessor(self.struct, SPBWJY, JVHFTH, OCTHBS, None),
            PBWJYK: GeckoBoolStructAccessor(self.struct, PBWJYK, BWJYKL, JUTYEK, None),
            WJYKLG: GeckoBoolStructAccessor(self.struct, WJYKLG, BWJYKL, YEKCWA, None),
            JYKLGQ: GeckoBoolStructAccessor(self.struct, JYKLGQ, BWJYKL, VHFTHE, None),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, PLSPFT, None, None, None
            ),
            LSPFTS: GeckoBoolStructAccessor(self.struct, LSPFTS, SPFTSI, YEKCWA, None),
            PFTSIF: GeckoBoolStructAccessor(self.struct, PFTSIF, SPFTSI, VHFTHE, None),
            FTSIFJ: GeckoWordStructAccessor(self.struct, FTSIFJ, TSIFJB, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, JVHFTH, ICXQIE, None),
            IFJBIA: GeckoTempStructAccessor(self.struct, IFJBIA, FJBIAM, None),
            JBIAMJ: GeckoTempStructAccessor(self.struct, JBIAMJ, BIAMJM, None),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, XLSXUJ, YEKCWA, AMJMAO, None, HEOCTH, None
            ),
            MJMAOA: GeckoBoolStructAccessor(self.struct, MJMAOA, JMAOAW, OCTHBS, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, JMAOAW, VHFTHE, None),
            AOAWBS: GeckoBoolStructAccessor(self.struct, AOAWBS, OAWBSI, OCTHBS, None),
            AWBSIR: GeckoBoolStructAccessor(self.struct, AWBSIR, WBSIRY, ICXQIE, None),
            BSIRYX: GeckoBoolStructAccessor(
                self.struct, BSIRYX, WBSIRY, OCTHBS, AKQXPI
            ),
            SIRYXB: GeckoBoolStructAccessor(self.struct, SIRYXB, IRYXBQ, ICXQIE, None),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, None),
            XBQFYL: GeckoBoolStructAccessor(self.struct, XBQFYL, BQFYLJ, XPICXQ, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, FYLJUI, XPICXQ, None),
            YLJUIK: GeckoBoolStructAccessor(self.struct, YLJUIK, FYLJUI, ICXQIE, None),
            LJUIKF: GeckoBoolStructAccessor(self.struct, LJUIKF, FYLJUI, HEOCTH, None),
            JUIKFW: GeckoBoolStructAccessor(self.struct, JUIKFW, FYLJUI, YEKCWA, None),
            UIKFWR: GeckoBoolStructAccessor(self.struct, UIKFWR, FYLJUI, VHFTHE, None),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, FYLJUI, CWAONP, WRKINE, None, OCTHBS, AKQXPI
            ),
            RKINEJ: GeckoEnumStructAccessor(
                self.struct, RKINEJ, KINEJN, None, YBQSNQ, None, None, None
            ),
            BQSNQL: GeckoEnumStructAccessor(
                self.struct, BQSNQL, QSNQLN, None, LNMHXE, None, None, None
            ),
            NMHXEK: GeckoWordStructAccessor(self.struct, NMHXEK, MHXEKV, None),
            HXEKVK: GeckoBoolStructAccessor(self.struct, HXEKVK, XEKVKZ, XPICXQ, None),
            EKVKZI: GeckoBoolStructAccessor(self.struct, EKVKZI, XEKVKZ, ICXQIE, None),
            KVKZIL: GeckoBoolStructAccessor(self.struct, KVKZIL, VKZILX, XPICXQ, None),
            KZILXW: GeckoBoolStructAccessor(self.struct, KZILXW, VKZILX, ICXQIE, None),
            ZILXWA: GeckoBoolStructAccessor(self.struct, ZILXWA, ILXWAJ, XPICXQ, None),
            LXWAJV: GeckoBoolStructAccessor(self.struct, LXWAJV, JVHFTH, JUTYEK, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, BWJYKL, XPICXQ, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, BWJYKL, ICXQIE, None),
            AJVDQL: GeckoBoolStructAccessor(self.struct, AJVDQL, JVDQLA, OCTHBS, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, JVDQLA, JUTYEK, None),
            DQLAII: GeckoBoolStructAccessor(self.struct, DQLAII, XEKVKZ, JUTYEK, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, XEKVKZ, HEOCTH, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, XEKVKZ, YEKCWA, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, XEKVKZ, VHFTHE, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, VKZILX, JUTYEK, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, VKZILX, HEOCTH, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, VKZILX, YEKCWA, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, VKZILX, VHFTHE, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, BXTIAC, OCTHBS, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, BXTIAC, JUTYEK, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, IRYXBQ, JUTYEK, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, SPFTSI, XPICXQ, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, SPFTSI, ICXQIE, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, QFFTTI, XPICXQ, None),
            FFTTID: GeckoByteStructAccessor(self.struct, FFTTID, FTTIDU, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, OAWBSI, XPICXQ, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, JVDQLA, XPICXQ, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, JVDQLA, ICXQIE, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, JVDQLA, HEOCTH, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, BSSUHB, XPICXQ, None),
            SSUHBV: GeckoEnumStructAccessor(
                self.struct, SSUHBV, BSSUHB, ICXQIE, SUHBVW, None, HEOCTH, None
            ),
            UHBVWV: GeckoBoolStructAccessor(self.struct, UHBVWV, BSSUHB, JUTYEK, None),
            HBVWVU: GeckoWordStructAccessor(self.struct, HBVWVU, BVWVUB, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, WVUBYG, XPICXQ, None),
            VUBYGD: GeckoBoolStructAccessor(self.struct, VUBYGD, UBYGDS, XPICXQ, None),
            BYGDSB: GeckoBoolStructAccessor(self.struct, BYGDSB, UBYGDS, ICXQIE, None),
            YGDSBD: GeckoBoolStructAccessor(self.struct, YGDSBD, BXTIAC, XPICXQ, None),
            GDSBDJ: GeckoBoolStructAccessor(self.struct, GDSBDJ, BXTIAC, ICXQIE, None),
            DSBDJQ: GeckoBoolStructAccessor(self.struct, DSBDJQ, BXTIAC, HEOCTH, None),
            SBDJQR: GeckoWordStructAccessor(self.struct, SBDJQR, BDJQRJ, None),
            DJQRJJ: GeckoByteStructAccessor(self.struct, DJQRJJ, JQRJJJ, None),
            QRJJJV: GeckoByteStructAccessor(self.struct, QRJJJV, RJJJVY, None),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, JJVYFC, None, TBJEUT, None, None, None
            ),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, JEUTOP, XPICXQ, PHUGTY, None, HEOCTH, None
            ),
            HUGTYI: GeckoEnumStructAccessor(
                self.struct, HUGTYI, JEUTOP, OCTHBS, TYIYWS, None, OCTHBS, None
            ),
            YIYWSK: GeckoWordStructAccessor(self.struct, YIYWSK, IYWSKW, None),
            YWSKWI: GeckoByteStructAccessor(self.struct, YWSKWI, WSKWIV, None),
            SKWIVD: GeckoByteStructAccessor(self.struct, SKWIVD, KWIVDN, None),
            WIVDNQ: GeckoByteStructAccessor(self.struct, WIVDNQ, IVDNQG, None),
            VDNQGV: GeckoByteStructAccessor(self.struct, VDNQGV, DNQGVU, None),
            NQGVUN: GeckoWordStructAccessor(self.struct, NQGVUN, QGVUNX, None),
            GVUNXN: GeckoByteStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoWordStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoEnumStructAccessor(
                self.struct, KMLOIJ, MLOIJU, None, IJUGSE, None, OCTHBS, AKQXPI
            ),
            JUGSEL: GeckoEnumStructAccessor(
                self.struct, JUGSEL, UGSELH, None, WDAFIK, None, None, None
            ),
            DAFIKJ: GeckoWordStructAccessor(self.struct, DAFIKJ, AFIKJP, None),
            FIKJPU: GeckoByteStructAccessor(self.struct, FIKJPU, IKJPUN, None),
            KJPUNR: GeckoByteStructAccessor(self.struct, KJPUNR, JPUNRJ, None),
            PUNRJZ: GeckoEnumStructAccessor(
                self.struct, PUNRJZ, UNRJZT, None, JZTATD, None, None, AKQXPI
            ),
            ZTATDZ: GeckoEnumStructAccessor(
                self.struct, ZTATDZ, TATDZX, None, GKEAKS, None, None, AKQXPI
            ),
            KEAKST: GeckoEnumStructAccessor(
                self.struct, KEAKST, EAKSTS, None, GKEAKS, None, None, AKQXPI
            ),
            AKSTSE: GeckoEnumStructAccessor(
                self.struct, AKSTSE, KSTSEM, None, GKEAKS, None, None, AKQXPI
            ),
            STSEMC: GeckoEnumStructAccessor(
                self.struct, STSEMC, TSEMCG, None, GKEAKS, None, None, AKQXPI
            ),
            SEMCGE: GeckoEnumStructAccessor(
                self.struct, SEMCGE, EMCGET, None, GKEAKS, None, None, AKQXPI
            ),
            MCGETI: GeckoEnumStructAccessor(
                self.struct, MCGETI, CGETIX, None, ETIXQV, None, None, AKQXPI
            ),
            TIXQVX: GeckoByteStructAccessor(self.struct, TIXQVX, IXQVXO, AKQXPI),
            XQVXOI: GeckoByteStructAccessor(self.struct, XQVXOI, QVXOIH, AKQXPI),
            VXOIHB: GeckoByteStructAccessor(self.struct, VXOIHB, XOIHBX, AKQXPI),
            OIHBXI: GeckoByteStructAccessor(self.struct, OIHBXI, IHBXIB, AKQXPI),
            HBXIBH: GeckoByteStructAccessor(self.struct, HBXIBH, BXIBHZ, AKQXPI),
            XIBHZV: GeckoByteStructAccessor(self.struct, XIBHZV, IBHZVO, AKQXPI),
            BHZVOA: GeckoEnumStructAccessor(
                self.struct, BHZVOA, HZVOAC, None, VOACMC, None, None, AKQXPI
            ),
            OACMCV: GeckoEnumStructAccessor(
                self.struct, OACMCV, CGETIX, None, VOACMC, None, None, AKQXPI
            ),
            ACMCVD: GeckoEnumStructAccessor(
                self.struct, ACMCVD, IXQVXO, None, VOACMC, None, None, AKQXPI
            ),
            CMCVDS: GeckoEnumStructAccessor(
                self.struct, CMCVDS, QVXOIH, None, VOACMC, None, None, AKQXPI
            ),
            MCVDSS: GeckoEnumStructAccessor(
                self.struct, MCVDSS, XOIHBX, None, VOACMC, None, None, AKQXPI
            ),
            CVDSSR: GeckoEnumStructAccessor(
                self.struct, CVDSSR, IHBXIB, None, VOACMC, None, None, AKQXPI
            ),
            VDSSRU: GeckoEnumStructAccessor(
                self.struct, VDSSRU, BXIBHZ, None, VOACMC, None, None, AKQXPI
            ),
            DSSRUR: GeckoEnumStructAccessor(
                self.struct, DSSRUR, SSRURA, None, SRURAZ, None, None, AKQXPI
            ),
            RURAZM: GeckoEnumStructAccessor(
                self.struct, RURAZM, IBHZVO, None, SRURAZ, None, None, AKQXPI
            ),
            URAZMK: GeckoByteStructAccessor(self.struct, URAZMK, RAZMKQ, AKQXPI),
            AZMKQT: GeckoByteStructAccessor(self.struct, AZMKQT, ZMKQTD, AKQXPI),
            MKQTDK: GeckoByteStructAccessor(self.struct, MKQTDK, KQTDKH, AKQXPI),
            QTDKHT: GeckoByteStructAccessor(self.struct, QTDKHT, TDKHTZ, AKQXPI),
            DKHTZB: GeckoByteStructAccessor(self.struct, DKHTZB, KHTZBB, AKQXPI),
            HTZBBE: GeckoByteStructAccessor(self.struct, HTZBBE, TZBBEK, AKQXPI),
            ZBBEKB: GeckoByteStructAccessor(self.struct, ZBBEKB, BBEKBD, AKQXPI),
            BEKBDF: GeckoByteStructAccessor(self.struct, BEKBDF, EKBDFS, AKQXPI),
            KBDFSR: GeckoByteStructAccessor(self.struct, KBDFSR, BDFSRO, AKQXPI),
            SCTTGC: GeckoBoolStructAccessor(self.struct, SCTTGC, JVHFTH, YEKCWA, None),
            CTTGCR: GeckoByteStructAccessor(self.struct, CTTGCR, TTGCRH, AKQXPI),
            TGCRHY: GeckoByteStructAccessor(self.struct, TGCRHY, GCRHYU, AKQXPI),
            CRHYUA: GeckoByteStructAccessor(self.struct, CRHYUA, RHYUAX, AKQXPI),
            HYUAXN: GeckoEnumStructAccessor(
                self.struct, HYUAXN, YUAXNC, None, UGUCYR, None, None, AKQXPI
            ),
            GUCYRA: GeckoBoolStructAccessor(
                self.struct, GUCYRA, UCYRAP, XPICXQ, AKQXPI
            ),
            CYRAPU: GeckoBoolStructAccessor(self.struct, CYRAPU, UNRJZT, XPICXQ, None),
        }

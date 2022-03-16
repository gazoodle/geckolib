#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v81'
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
ACCPQI = "".join(chr(c) for c in [83, 112, 101, 101, 100, 86, 83, 80, 52])
ACMCVD = 320
ACQFFT = 390
ADXLUB = "".join(chr(c) for c in [67, 70, 71, 50, 54])
AFIKJP = "".join(
    chr(c) for c in [80, 97, 99, 107, 71, 101, 110, 101, 114, 97, 116, 105, 111, 110]
)
AIIDNI = "".join(
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
AIVEMV = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
AJVDQL = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
AKQXPI = "".join(chr(c) for c in [65, 76, 76])
AKSTSE = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
AMJMAO = "".join(
    chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101, 83, 117, 115, 112]
)
AOAWBS = "".join(chr(c) for c in [83, 119, 109, 82, 105, 115, 107])
AOESVZ = 467
AONPYY = "".join(chr(c) for c in [67, 80])
APUMEA = "".join(chr(c) for c in [67, 70, 71, 49, 55])
ATDZXN = 293
AWBSIR = "".join(chr(c) for c in [78, 79])
AXADXL = "".join(chr(c) for c in [67, 70, 71, 50, 53])
AXNCUG = "".join(chr(c) for c in [67, 70, 71, 49, 50])
AZMKQT = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
BBEKBD = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
BDFSRO = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
BDJQRJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
BEKBDF = 334
BFEGZU = 304
BGJFJN = 476
BHZVOA = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
BIAMJM = "".join(
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
BJEUTO = "".join(chr(c) for c in [86, 83, 80, 50, 67, 111, 109, 109, 76, 111, 115, 116])
BLKXSJ = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
BMJVHF = 256
BQFYLJ = 355
BQNRXC = "".join(chr(c) for c in [105, 110, 89, 84])
BQSNQL = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
BSIRYX = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
BSKSOK = 258
BSSUHB = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
BVNAXA = 471
BVWVUB = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
BWJYKL = 268
BXTIAC = "".join(chr(c) for c in [71, 69, 67, 75, 79, 95, 53, 48, 48, 48, 87])
BXYBQS = 352
BYGDSB = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
CBFEGZ = "".join(chr(c) for c in [85, 100, 81, 117, 105, 101, 116, 84, 105, 109, 101])
CCPQIP = 401
CGETIX = "".join(chr(c) for c in [75, 50, 48, 48])
CHWDAF = "".join(chr(c) for c in [51, 50, 75])
CMCVDS = "".join(chr(c) for c in [78, 65])
CPQIPO = "".join(chr(c) for c in [83, 112, 101, 101, 100, 86, 83, 80, 53])
CQBMJV = 317
CQFFTT = "".join(
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
CRHYUA = 457
CRTFMN = "".join(chr(c) for c in [86, 83, 80, 51, 69, 114, 114, 111, 114, 73, 68])
CTHBSK = "".join(chr(c) for c in [85, 100, 80, 51])
CTTGCR = 455
CUGUCY = 461
CVDSSR = "".join(chr(c) for c in [80, 49, 76])
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CXQIEF = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
CYRAPU = 463
CYWONF = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
CZOLSI = 449
DDPMXF = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
DFSROG = 335
DGKEAK = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
DJQRJJ = "".join(
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
DKHTZB = 322
DMPSCT = 453
DNIBXT = "".join(
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
DNQGVU = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
DPMXFU = 339
DRXAIV = 342
DSBDJQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
DSSRUR = "".join(chr(c) for c in [80, 50, 76])
DUBSSU = 383
DXLUBG = 474
DZXNQT = 294
EAKSTS = 301
EAOESV = "".join(chr(c) for c in [67, 70, 71, 49, 57])
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = 333
EFJTAC = "".join(chr(c) for c in [83, 112, 101, 101, 100, 86, 83, 80, 50])
EFXQGL = "".join(chr(c) for c in [83, 79, 65, 75])
EGZUQE = 305
EJNIBX = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
EKBDFS = "".join(chr(c) for c in [72, 84, 82])
EKCWAO = "".join(chr(c) for c in [80, 53])
EKVKZI = "".join(chr(c) for c in [67, 72, 73, 76, 76])
ELHBQN = "".join(chr(c) for c in [75, 54, 48, 48])
ELWUEU = 328
EMCGET = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
EMVCYW = 345
EOCTHB = "".join(chr(c) for c in [85, 100, 80, 50])
ESVZSS = 468
ETDRXA = 341
ETIXQV = "".join(chr(c) for c in [75, 56, 53])
EUHNNX = 330
EUTOPH = "".join(chr(c) for c in [86, 83, 80, 52, 67, 111, 109, 109, 76, 111, 115, 116])
EXLSXU = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
EZFETD = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
FCRTFM = 404
FEFJTA = 398
FEGZUQ = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
FETDRX = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
FFTTID = "".join(
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
FIKJPU = "".join(chr(c) for c in [49, 83, 84, 95, 71, 69, 78])
FJBIAM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 66, 121, 85, 68]
)
FJNTTU = "".join(chr(c) for c in [67, 70, 71, 51, 48])
FJTACC = 399
FLSIJU = 374
FMNHTB = 406
FSROGM = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [67, 108, 101, 97, 110])
FTTIDU = "".join(
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
FUBJLO = 325
FWRKIN = 279
FXQGLR = "".join(chr(c) for c in [79, 70, 70])
FYLJUI = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
FZCZOL = 448
FZDGKE = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
GCRHYU = "".join(chr(c) for c in [67, 70, 71, 57])
GDSBDJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
GETIXQ = "".join(chr(c) for c in [75, 52, 48, 48])
GJFJNT = "".join(chr(c) for c in [67, 70, 71, 50, 57])
GKEAKS = 300
GLRAHE = 259
GMDDPM = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
GQPLSP = 272
GSELHB = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
GTYIYW = 309
GUCYRA = 462
GVUNXN = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
GYOUSP = "".join(
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
GZUQEX = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
HBQNRX = "".join(chr(c) for c in [105, 110, 84, 111, 117, 99, 104])
HBSKSO = "".join(chr(c) for c in [85, 100, 80, 53])
HBVWVU = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
HBXIBH = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
HECVYY = "".join(chr(c) for c in [])
HEOCTH = 4
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [85, 100, 83, 112, 101, 101, 100, 86, 83, 80, 49])
HNNXWE = 331
HTBJEU = "".join(chr(c) for c in [86, 83, 80, 49, 67, 111, 109, 109, 76, 111, 115, 116])
HTZBBE = 323
HUGTYI = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
HUOJRJ = "".join(chr(c) for c in [85, 100, 76, 105])
HWDAFI = "".join(chr(c) for c in [52, 56, 75])
HXEKVK = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
HYUAXN = 458
HZVOAC = 360
IACQFF = "".join(
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
IAMJMA = "".join(chr(c) for c in [67, 80, 79, 84])
IBHZVO = 358
IBXTIA = "".join(chr(c) for c in [71, 69, 78, 69, 82, 73, 67])
IBXYBQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 79, 118, 101, 114, 84, 101, 109, 112]
)
ICXQIE = 1
IDNIBX = "".join(
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
IDUBSS = "".join(
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
IEFXQG = "".join(chr(c) for c in [68, 82, 65, 73, 78])
IFJBIA = "".join(chr(c) for c in [80, 117, 114, 103, 101])
IGYOUS = 264
IHBXIB = "".join(chr(c) for c in [75, 51, 48, 48])
IIDNIB = "".join(
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
IJUGSE = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
IJUZMR = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
IKJPUN = "".join(chr(c) for c in [50, 78, 68, 95, 71, 69, 78])
ILXWAJ = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
INEJNI = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
INELWU = 327
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
IPMDMP = "".join(chr(c) for c in [67, 70, 71, 52])
IPOUYN = 310
IRYXBQ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
IUSOOQ = 393
IUXFEF = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
IVDNQG = 315
IVEMVC = 344
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 73, 78, 83, 84, 65, 76, 76, 69, 68])
IXQVXO = "".join(chr(c) for c in [75, 52])
IYWSKW = "".join(chr(c) for c in [70, 76, 67, 69, 114, 114])
JBIAMJ = "".join(
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
JEUTOP = "".join(chr(c) for c in [86, 83, 80, 51, 67, 111, 109, 109, 76, 111, 115, 116])
JFJNTT = 477
JHIUSO = 370
JIGYOU = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 70, 105, 108, 116, 68, 117, 114]
)
JJJVYF = "".join(
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
JJVYFC = 387
JLOINE = "".join(chr(c) for c in [83, 79, 117, 116, 55])
JMAOAW = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
JMCBFE = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
JNIBXY = 281
JNTTUV = 478
JPUNRJ = "".join(chr(c) for c in [52, 84, 72, 95, 71, 69, 78])
JQRJJJ = "".join(
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
JRJHIU = 363
JTACCP = "".join(chr(c) for c in [83, 112, 101, 101, 100, 86, 83, 80, 51])
JUGSEL = "".join(chr(c) for c in [77, 73, 65])
JUIKFW = 277
JUZMRK = "".join(
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
JVDQLA = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
JVHFTH = 274
JVYFCR = "".join(chr(c) for c in [86, 83, 80, 49, 69, 114, 114, 111, 114, 73, 68])
JWMNZM = "".join(chr(c) for c in [73, 68, 76, 69])
JYKLGQ = 270
JYMOUN = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
JZTATD = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
KCWAON = 260
KEAKST = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
KFWRKI = "".join(chr(c) for c in [78, 101, 97, 114, 72, 76])
KHTZBB = "".join(chr(c) for c in [83, 79, 117, 116, 52])
KINEJN = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
KJPUNR = "".join(chr(c) for c in [51, 82, 68, 95, 71, 69, 78])
KLGQPL = 271
KMLOIJ = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
KPHUOJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
KQTDKH = "".join(chr(c) for c in [83, 79, 117, 116, 50])
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
KSTSEM = 316
KWIVDN = 314
KZILXW = 379
LAIIDN = 392
LASSAK = "".join(chr(c) for c in [84, 82, 69, 65, 68, 77, 73, 76, 76])
LGQPLS = "".join(
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
LHBQNR = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
LIUXFE = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
LJUIKF = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
LKXSJW = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
LNMHXE = "".join(
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
LOIJUG = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
LOINEL = 326
LRAHEO = "".join(chr(c) for c in [76, 79])
LSIJUZ = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
LSIPMD = "".join(chr(c) for c in [67, 70, 71, 51])
LSPFTS = 380
LSXUJU = "".join(chr(c) for c in [80, 49])
LUBGJF = 475
LWUEUH = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
LXWAJV = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
MAOAWB = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
MCBFEG = 303
MCGETI = 357
MCVDSS = "".join(chr(c) for c in [80, 49, 72])
MDDPMX = 338
MDMPSC = "".join(chr(c) for c in [67, 70, 71, 53])
MEAOES = 466
MFZDGK = 297
MHXEKV = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
MJMAOA = 282
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MLOIJU = 289
MNHTBJ = "".join(chr(c) for c in [86, 83, 80, 53, 69, 114, 114, 111, 114, 73, 68])
MNZMJI = "".join(chr(c) for c in [83, 84, 65, 82, 84])
MOUNBL = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
MPSCTT = "".join(chr(c) for c in [67, 70, 71, 54])
MRKVFC = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
MVCYWO = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
MXFUBJ = 349
NAXADX = 472
NBLKXS = 262
NCUGUC = "".join(chr(c) for c in [67, 70, 71, 49, 51])
NEJNIB = 280
NELWUE = "".join(chr(c) for c in [83, 79, 117, 116, 57])
NFZCZO = "".join(chr(c) for c in [67, 70, 71, 48])
NHTBJE = 407
NIBXTI = 389
NIBXYB = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
NKMLOI = 288
NMHXEK = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
NNXWEE = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
NPYYLI = 3
NQGVUN = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
NQJYMO = "".join(
    chr(c)
    for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 116, 97, 116, 117, 115]
)
NQLNMH = 378
NQTMFZ = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
NRJZTA = 8
NRSJMC = 396
NRXCHW = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
NTTUVR = "".join(chr(c) for c in [67, 70, 71, 51, 49])
NXNKML = 287
NXWEEZ = 332
NZMJIG = "".join(chr(c) for c in [78, 69, 87])
OACMCV = "".join(chr(c) for c in [83, 79, 117, 116, 49])
OAWBSI = 313
OCTHBS = 2
OESVZS = "".join(chr(c) for c in [67, 70, 71, 50, 48])
OGMDDP = 337
OIHBXI = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
OIJUGS = "".join(chr(c) for c in [105, 110, 88, 69])
OINELW = "".join(chr(c) for c in [83, 79, 117, 116, 56])
OJRJHI = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
OLSIPM = 450
ONFZCZ = 348
ONPYYL = "".join(chr(c) for c in [79, 51])
OOQNRS = "".join(chr(c) for c in [85, 100, 83, 112, 101, 101, 100, 86, 83, 80, 51])
OPHUGT = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
OQNRSJ = 395
OUBMIK = 256
OUNBLK = 367
OUSPBW = "".join(
    chr(c) for c in [69, 99, 111, 110, 111, 109, 121, 65, 99, 99, 101, 115, 115]
)
OUYNQJ = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
PBWJYK = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
PFTSIF = 381
PHUGTY = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
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
PLSPFT = "".join(
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
PMDMPS = 452
PMXFUB = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114, 67, 117, 114])
POUBMI = 81
POUYNQ = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
PQIPOU = 402
PSCTTG = 454
PUMEAO = 465
PUNRJZ = "".join(chr(c) for c in [53, 84, 72, 95, 71, 69, 78])
PYYLIU = "".join(chr(c) for c in [76, 49, 50, 48])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = 362
QFFTTI = 284
QFYLJU = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
QGLRAH = "".join(chr(c) for c in [85, 100, 80, 49])
QGVUNX = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
QIEFXQ = "".join(chr(c) for c in [78, 79, 84, 95, 83, 69, 84])
QIPOUY = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
QJYMOU = 364
QLAIID = "".join(
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
QLNMHX = "".join(
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
QNRSJM = "".join(chr(c) for c in [85, 100, 83, 112, 101, 101, 100, 86, 83, 80, 52])
QPLSPF = "".join(
    chr(c)
    for c in [80, 114, 111, 103, 79, 117, 116, 112, 117, 116, 65, 99, 99, 101, 115, 115]
)
QRJJJV = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
QSNQLN = 384
QTDKHT = 321
QTMFZD = 296
QVXOIH = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
QXPICX = 388
RAHEOC = "".join(chr(c) for c in [72, 73])
RAPUME = 464
RAZMKQ = "".join(chr(c) for c in [66, 76, 79])
RFLSIJ = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
RHYUAX = "".join(chr(c) for c in [67, 70, 71, 49, 48])
RJHIUS = "".join(chr(c) for c in [85, 100, 65, 117, 120])
RJJJVY = 354
RJZTAT = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 50, 53, 54, 75])
RKINEJ = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
RKVFCP = 375
ROGMDD = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
RSJMCB = "".join(chr(c) for c in [85, 100, 83, 112, 101, 101, 100, 86, 83, 80, 53])
RTFMNH = 405
RURAZM = "".join(chr(c) for c in [80, 52, 72])
RXAIVE = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
RXCHWD = 290
RYXBQF = 353
SAKQXP = 386
SBDJQR = 351
SBVNAX = "".join(chr(c) for c in [67, 70, 71, 50, 51])
SCTTGC = "".join(chr(c) for c in [67, 70, 71, 55])
SELHBQ = "".join(chr(c) for c in [105, 110, 88, 77])
SIFJBI = "".join(chr(c) for c in [70, 105, 108, 116, 82, 101, 113, 117, 101, 115, 116])
SIJUZM = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
SIPMDM = 451
SJMCBF = 397
SJWMNZ = 263
SKWIVD = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
SNQLNM = "".join(
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
SOKPHU = "".join(chr(c) for c in [79, 78])
SOOQNR = 394
SPBWJY = 267
SPFTSI = "".join(
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
SROGMD = 336
SRURAZ = "".join(chr(c) for c in [80, 51, 76])
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
SSBVNA = 470
SSRURA = "".join(chr(c) for c in [80, 51, 72])
SSUHBV = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
STSEMC = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
SUHBVW = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
SVZSSB = "".join(chr(c) for c in [67, 70, 71, 50, 49])
SXUJUT = 261
TACCPQ = 400
TATDZX = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
TBJEUT = 408
TDKHTZ = "".join(chr(c) for c in [83, 79, 117, 116, 51])
TDRXAI = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
TDZXNQ = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
TFMNHT = "".join(chr(c) for c in [86, 83, 80, 52, 69, 114, 114, 111, 114, 73, 68])
TGCRHY = 456
THBSKS = "".join(chr(c) for c in [85, 100, 80, 52])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIDUBS = "".join(
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
TIXQVX = "".join(chr(c) for c in [75, 56])
TMFZDG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
TOPHUG = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
TSEMCG = "".join(chr(c) for c in [70, 117, 108, 108])
TSIFJB = 273
TTGCRH = "".join(chr(c) for c in [67, 70, 71, 56])
TTIDUB = 350
TTUVRF = 479
TUVRFL = "".join(
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
TYEKCW = "".join(chr(c) for c in [80, 51])
TYIYWS = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
TZBBEK = "".join(chr(c) for c in [83, 79, 117, 116, 53])
UAXNCU = 459
UBGJFJ = "".join(chr(c) for c in [67, 70, 71, 50, 56])
UBJLOI = "".join(chr(c) for c in [70, 97, 110])
UBMIKG = 479
UBSSUH = "".join(
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
UBYGDS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
UCYRAP = "".join(chr(c) for c in [67, 70, 71, 49, 53])
UEUHNN = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
UGSELH = "".join(chr(c) for c in [68, 74, 83, 52])
UGTYIY = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
UGUCYR = "".join(chr(c) for c in [67, 70, 71, 49, 52])
UHBVWV = 283
UHNNXW = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
UIKFWR = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
UJUTYE = "".join(chr(c) for c in [76, 79, 87])
UMEAOE = "".join(chr(c) for c in [67, 70, 71, 49, 56])
UNBLKX = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
UNXNKM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
UOJRJH = 307
UQEXLS = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
URAZMK = "".join(chr(c) for c in [80, 52, 76])
USOOQN = "".join(chr(c) for c in [85, 100, 83, 112, 101, 101, 100, 86, 83, 80, 50])
USPBWJ = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 65, 99, 116, 105, 111, 110]
)
UTOPHU = "".join(chr(c) for c in [86, 83, 80, 53, 67, 111, 109, 109, 76, 111, 115, 116])
UTYEKC = "".join(chr(c) for c in [80, 50])
UVRFLS = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
UXFEFJ = 7
UYNQJY = "".join(chr(c) for c in [70, 85, 76, 76])
UZMRKV = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
VCYWON = 346
VDNQGV = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
VDQLAI = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
VDSSRU = "".join(chr(c) for c in [80, 50, 72])
VEMVCY = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
VFCPOU = "".join(chr(c) for c in [76, 73])
VHFTHE = 6
VKZILX = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
VLASSA = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
VNAXAD = "".join(chr(c) for c in [67, 70, 71, 50, 52])
VOACMC = 361
VRFLSI = 371
VUBYGD = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
VUNXNK = 285
VWVUBY = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
VXOIHB = "".join(chr(c) for c in [75, 49, 48, 48])
VYFCRT = 403
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
VZSSBV = 469
WAJVDQ = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
WAONPY = "".join(chr(c) for c in [66, 76])
WBSIRY = "".join(chr(c) for c in [77, 69, 68])
WDAFIK = "".join(chr(c) for c in [54, 52, 75])
WEEZFE = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
WIVDNQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
WJYKLG = "".join(
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
WMNZMJ = "".join(chr(c) for c in [83, 84, 79, 80])
WONFZC = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
WRKINE = "".join(chr(c) for c in [72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116])
WSKWIV = 311
WUEUHN = 329
WVUBYG = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
XADXLU = 473
XAIVEM = 343
XBQFYL = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
XCHWDA = "".join(chr(c) for c in [49, 54, 75])
XEKVKZ = "".join(chr(c) for c in [72, 69, 65, 84])
XFEFJT = "".join(chr(c) for c in [83, 112, 101, 101, 100, 86, 83, 80, 49])
XFUBJL = "".join(chr(c) for c in [83, 79, 117, 116, 54])
XIBHZV = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
XLSXUJ = 369
XLUBGJ = "".join(chr(c) for c in [67, 70, 71, 50, 55])
XNCUGU = 460
XNKMLO = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
XNQTMF = 295
XOIHBX = "".join(chr(c) for c in [75, 56, 48, 48])
XPICXQ = 0
XQIEFX = 257
XQVXOI = "".join(chr(c) for c in [75, 53])
XSJWMN = "".join(
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
XTIACQ = "".join(chr(c) for c in [71, 69, 67, 75, 79, 55, 53, 48, 48, 87])
XUJUTY = "".join(chr(c) for c in [72, 73, 71, 72])
XWAJVD = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
XYBQSN = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
YBQSNQ = 377
YEKCWA = "".join(chr(c) for c in [80, 52])
YFCRTF = "".join(chr(c) for c in [86, 83, 80, 50, 69, 114, 114, 111, 114, 73, 68])
YGDSBD = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
YKLGQP = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
YLIUXF = 5
YLJUIK = 275
YMOUNB = 365
YOUSPB = 266
YPIPIV = "".join(chr(c) for c in [83, 116, 105, 99, 107, 66, 97, 110, 107])
YRAPUM = "".join(chr(c) for c in [67, 70, 71, 49, 54])
YUAXNC = "".join(chr(c) for c in [67, 70, 71, 49, 49])
YWONFZ = 347
YWSKWI = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
YXBQFY = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 65, 99, 116, 105, 118, 101]
)
YYLIUX = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 324
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = "".join(chr(c) for c in [67, 70, 71, 49])
ZDGKEA = 299
ZFETDR = 340
ZILXWA = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
ZMJIGY = "".join(chr(c) for c in [65, 67, 84, 73, 86, 69])
ZMKQTD = "".join(chr(c) for c in [65, 85, 88])
ZOLSIP = "".join(chr(c) for c in [67, 70, 71, 50])
ZSSBVN = "".join(chr(c) for c in [67, 70, 71, 50, 50])
ZTATDZ = 291
ZUQEXL = 306
ZVOACM = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
ZXNQTM = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
AHEOCT = [FXQGLR, LRAHEO, RAHEOC]
ASSAKQ = [IVLASS, VLASSA, LASSAK]
BJLOIN = [
    CMCVDS,
    MCVDSS,
    CVDSSR,
    VDSSRU,
    DSSRUR,
    SSRURA,
    SRURAZ,
    RURAZM,
    URAZMK,
    EKCWAO,
    RAZMKQ,
    AONPYY,
    ONPYYL,
    PYYLIU,
    HECVYY,
    HECVYY,
    UBJLOI,
    HECVYY,
    HECVYY,
    AZMKQT,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    IUXFEF,
    ZMKQTD,
]
BXIBHZ = [
    CGETIX,
    GETIXQ,
    ETIXQV,
    TIXQVX,
    IXQVXO,
    XQVXOI,
    QVXOIH,
    VXOIHB,
    XOIHBX,
    HECVYY,
    HECVYY,
    HECVYY,
    OIHBXI,
    IHBXIB,
    HBXIBH,
]
CPOUBM = [
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
    CBFEGZ,
    FEGZUQ,
    GZUQEX,
    UQEXLS,
    EXLSXU,
]
CWAONP = [FXQGLR, XUJUTY]
DAFIKJ = [XCHWDA, CHWDAF, HWDAFI, WDAFIK]
DQLAII = [
    JWMNZM,
    ZILXWA,
    ILXWAJ,
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
    LXWAJV,
    XWAJVD,
    WAJVDQ,
    AJVDQL,
    JVDQLA,
    VDQLAI,
]
FCPOUB = [
    LSXUJU,
    UTYEKC,
    TYEKCW,
    YEKCWA,
    EKCWAO,
    WAONPY,
    AONPYY,
    ONPYYL,
    PYYLIU,
    YYLIUX,
    LIUXFE,
    IUXFEF,
    XFEFJT,
    EFJTAC,
    JTACCP,
    ACCPQI,
    CPQIPO,
    QIPOUY,
    NQJYMO,
    JYMOUN,
    MOUNBL,
    VFCPOU,
]
IKFWRK = [HECVYY, UIKFWR, UIKFWR, UIKFWR]
JUTYEK = [FXQGLR, XUJUTY, UJUTYE]
KBDFSR = [
    CMCVDS,
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
    EKBDFS,
]
KVFCPO = []
KVKZIL = [XEKVKZ, EKVKZI]
KXSJWM = [BLKXSJ, LKXSJW]
MJIGYO = [JWMNZM, WMNZMJ, MNZMJI, NZMJIG, ZMJIGY]
MKQTDK = [
    CMCVDS,
    MCVDSS,
    CVDSSR,
    VDSSRU,
    DSSRUR,
    SSRURA,
    SRURAZ,
    RURAZM,
    URAZMK,
    EKCWAO,
    RAZMKQ,
    AONPYY,
    ONPYYL,
    PYYLIU,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    AZMKQT,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    HECVYY,
    IUXFEF,
    ZMKQTD,
]
OKPHUO = [FXQGLR, SOKPHU]
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
QNRXCH = [
    LOIJUG,
    OIJUGS,
    IJUGSE,
    JUGSEL,
    UGSELH,
    GSELHB,
    SELHBQ,
    ELHBQN,
    LHBQNR,
    HBQNRX,
    BQNRXC,
]
SEMCGE = [STSEMC, TSEMCG]
SIRYXB = [AWBSIR, LRAHEO, WBSIRY, RAHEOC, BSIRYX]
SKSOKP = [FXQGLR, RAHEOC]
TIACQF = [IBXTIA, BXTIAC, XTIACQ]
UNRJZT = [FIKJPU, IKJPUN, HECVYY, KJPUNR, HECVYY, JPUNRJ, HECVYY, PUNRJZ]
XQGLRA = [QIEFXQ, IEFXQG, EFXQGL, FXQGLR]
XWEEZF = [
    CMCVDS,
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
    AONPYY,
]
YIYWSK = [HECVYY, TYIYWS, TYIYWS, TYIYWS]
YNQJYM = [POUYNQ, OUYNQJ, UYNQJY]
ZMRKVF = [LSIJUZ, SIJUZM, IJUZMR, JUZMRK, UZMRKV]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return POUBMI

    @property
    def begin(self):
        return OUBMIK

    @property
    def end(self):
        return UBMIKG

    @property
    def all_device_keys(self):
        return FCPOUB

    @property
    def user_demand_keys(self):
        return CPOUBM

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
            CBFEGZ: GeckoByteStructAccessor(self.struct, CBFEGZ, BFEGZU, AKQXPI),
            FEGZUQ: GeckoByteStructAccessor(self.struct, FEGZUQ, EGZUQE, AKQXPI),
            GZUQEX: GeckoByteStructAccessor(self.struct, GZUQEX, ZUQEXL, AKQXPI),
            UQEXLS: GeckoByteStructAccessor(self.struct, UQEXLS, QEXLSX, AKQXPI),
            EXLSXU: GeckoByteStructAccessor(self.struct, EXLSXU, XLSXUJ, AKQXPI),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, SXUJUT, XPICXQ, JUTYEK, None, HEOCTH, None
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, SXUJUT, OCTHBS, JUTYEK, None, HEOCTH, None
            ),
            TYEKCW: GeckoEnumStructAccessor(
                self.struct, TYEKCW, SXUJUT, HEOCTH, JUTYEK, None, HEOCTH, None
            ),
            YEKCWA: GeckoEnumStructAccessor(
                self.struct, YEKCWA, SXUJUT, VHFTHE, JUTYEK, None, HEOCTH, None
            ),
            EKCWAO: GeckoEnumStructAccessor(
                self.struct, EKCWAO, KCWAON, XPICXQ, CWAONP, None, OCTHBS, None
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, KCWAON, ICXQIE, OKPHUO, None, OCTHBS, None
            ),
            AONPYY: GeckoEnumStructAccessor(
                self.struct, AONPYY, KCWAON, OCTHBS, OKPHUO, None, OCTHBS, None
            ),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, KCWAON, NPYYLI, OKPHUO, None, OCTHBS, None
            ),
            PYYLIU: GeckoEnumStructAccessor(
                self.struct, PYYLIU, KCWAON, HEOCTH, OKPHUO, None, OCTHBS, None
            ),
            YYLIUX: GeckoEnumStructAccessor(
                self.struct, YYLIUX, KCWAON, YLIUXF, OKPHUO, None, OCTHBS, None
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, KCWAON, VHFTHE, OKPHUO, None, OCTHBS, None
            ),
            IUXFEF: GeckoEnumStructAccessor(
                self.struct, IUXFEF, KCWAON, UXFEFJ, OKPHUO, None, OCTHBS, None
            ),
            XFEFJT: GeckoByteStructAccessor(self.struct, XFEFJT, FEFJTA, AKQXPI),
            EFJTAC: GeckoByteStructAccessor(self.struct, EFJTAC, FJTACC, AKQXPI),
            JTACCP: GeckoByteStructAccessor(self.struct, JTACCP, TACCPQ, AKQXPI),
            ACCPQI: GeckoByteStructAccessor(self.struct, ACCPQI, CCPQIP, AKQXPI),
            CPQIPO: GeckoByteStructAccessor(self.struct, CPQIPO, PQIPOU, AKQXPI),
            QIPOUY: GeckoEnumStructAccessor(
                self.struct, QIPOUY, IPOUYN, None, YNQJYM, None, None, AKQXPI
            ),
            NQJYMO: GeckoEnumStructAccessor(
                self.struct, NQJYMO, QJYMOU, None, YNQJYM, None, None, None
            ),
            JYMOUN: GeckoWordStructAccessor(self.struct, JYMOUN, YMOUNB, None),
            MOUNBL: GeckoWordStructAccessor(self.struct, MOUNBL, OUNBLK, AKQXPI),
            UNBLKX: GeckoEnumStructAccessor(
                self.struct, UNBLKX, NBLKXS, XPICXQ, KXSJWM, None, OCTHBS, AKQXPI
            ),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, SJWMNZ, None, MJIGYO, None, None, AKQXPI
            ),
            JIGYOU: GeckoTimeStructAccessor(self.struct, JIGYOU, IGYOUS, AKQXPI),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, AKQXPI),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, NBLKXS, OCTHBS, KXSJWM, None, OCTHBS, AKQXPI
            ),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, SPBWJY, None, MJIGYO, None, None, AKQXPI
            ),
            PBWJYK: GeckoTimeStructAccessor(self.struct, PBWJYK, BWJYKL, AKQXPI),
            WJYKLG: GeckoByteStructAccessor(self.struct, WJYKLG, JYKLGQ, AKQXPI),
            YKLGQP: GeckoByteStructAccessor(self.struct, YKLGQP, KLGQPL, AKQXPI),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, AKQXPI),
            QPLSPF: GeckoEnumStructAccessor(
                self.struct, QPLSPF, NBLKXS, ICXQIE, KXSJWM, None, OCTHBS, AKQXPI
            ),
            PLSPFT: GeckoEnumStructAccessor(
                self.struct, PLSPFT, LSPFTS, None, MJIGYO, None, None, AKQXPI
            ),
            SPFTSI: GeckoTimeStructAccessor(self.struct, SPFTSI, PFTSIF, AKQXPI),
            FTSIFJ: GeckoBoolStructAccessor(self.struct, FTSIFJ, TSIFJB, XPICXQ, None),
            SIFJBI: GeckoBoolStructAccessor(self.struct, SIFJBI, TSIFJB, ICXQIE, None),
            IFJBIA: GeckoBoolStructAccessor(self.struct, IFJBIA, TSIFJB, OCTHBS, None),
            FJBIAM: GeckoBoolStructAccessor(self.struct, FJBIAM, TSIFJB, NPYYLI, None),
            JBIAMJ: GeckoBoolStructAccessor(self.struct, JBIAMJ, TSIFJB, HEOCTH, None),
            BIAMJM: GeckoBoolStructAccessor(self.struct, BIAMJM, TSIFJB, YLIUXF, None),
            IAMJMA: GeckoBoolStructAccessor(self.struct, IAMJMA, JVHFTH, OCTHBS, None),
            AMJMAO: GeckoBoolStructAccessor(self.struct, AMJMAO, MJMAOA, NPYYLI, None),
            JMAOAW: GeckoBoolStructAccessor(self.struct, JMAOAW, MJMAOA, YLIUXF, None),
            MAOAWB: GeckoBoolStructAccessor(self.struct, MAOAWB, MJMAOA, VHFTHE, None),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, None, SIRYXB, None, None, None
            ),
            IRYXBQ: GeckoBoolStructAccessor(self.struct, IRYXBQ, RYXBQF, YLIUXF, None),
            YXBQFY: GeckoBoolStructAccessor(self.struct, YXBQFY, RYXBQF, VHFTHE, None),
            XBQFYL: GeckoWordStructAccessor(self.struct, XBQFYL, BQFYLJ, None),
            QFYLJU: GeckoBoolStructAccessor(self.struct, QFYLJU, JVHFTH, ICXQIE, None),
            FYLJUI: GeckoTempStructAccessor(self.struct, FYLJUI, YLJUIK, None),
            LJUIKF: GeckoTempStructAccessor(self.struct, LJUIKF, JUIKFW, None),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, KCWAON, YLIUXF, IKFWRK, None, HEOCTH, None
            ),
            KFWRKI: GeckoBoolStructAccessor(self.struct, KFWRKI, FWRKIN, XPICXQ, None),
            WRKINE: GeckoBoolStructAccessor(self.struct, WRKINE, FWRKIN, ICXQIE, None),
            RKINEJ: GeckoBoolStructAccessor(self.struct, RKINEJ, FWRKIN, OCTHBS, None),
            KINEJN: GeckoBoolStructAccessor(self.struct, KINEJN, FWRKIN, VHFTHE, None),
            INEJNI: GeckoBoolStructAccessor(self.struct, INEJNI, NEJNIB, OCTHBS, None),
            EJNIBX: GeckoBoolStructAccessor(self.struct, EJNIBX, JNIBXY, ICXQIE, None),
            NIBXYB: GeckoBoolStructAccessor(
                self.struct, NIBXYB, JNIBXY, OCTHBS, AKQXPI
            ),
            IBXYBQ: GeckoBoolStructAccessor(self.struct, IBXYBQ, BXYBQS, ICXQIE, None),
            XYBQSN: GeckoByteStructAccessor(self.struct, XYBQSN, YBQSNQ, None),
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, QSNQLN, XPICXQ, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, NQLNMH, XPICXQ, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, NQLNMH, ICXQIE, None),
            LNMHXE: GeckoBoolStructAccessor(self.struct, LNMHXE, NQLNMH, HEOCTH, None),
            NMHXEK: GeckoBoolStructAccessor(self.struct, NMHXEK, NQLNMH, YLIUXF, None),
            MHXEKV: GeckoBoolStructAccessor(self.struct, MHXEKV, NQLNMH, VHFTHE, None),
            HXEKVK: GeckoEnumStructAccessor(
                self.struct, HXEKVK, NQLNMH, UXFEFJ, KVKZIL, None, OCTHBS, AKQXPI
            ),
            VKZILX: GeckoEnumStructAccessor(
                self.struct, VKZILX, KZILXW, None, DQLAII, None, None, None
            ),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, LAIIDN, XPICXQ, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, LAIIDN, ICXQIE, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, LAIIDN, OCTHBS, None),
            IDNIBX: GeckoBoolStructAccessor(self.struct, IDNIBX, LAIIDN, NPYYLI, None),
            DNIBXT: GeckoEnumStructAccessor(
                self.struct, DNIBXT, NIBXTI, None, TIACQF, None, None, None
            ),
            IACQFF: GeckoWordStructAccessor(self.struct, IACQFF, ACQFFT, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, QFFTTI, XPICXQ, None),
            FFTTID: GeckoBoolStructAccessor(self.struct, FFTTID, QFFTTI, ICXQIE, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, TTIDUB, XPICXQ, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, TTIDUB, ICXQIE, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, DUBSSU, XPICXQ, None),
            UBSSUH: GeckoBoolStructAccessor(self.struct, UBSSUH, DUBSSU, ICXQIE, None),
            BSSUHB: GeckoBoolStructAccessor(self.struct, BSSUHB, MJMAOA, XPICXQ, None),
            SSUHBV: GeckoBoolStructAccessor(self.struct, SSUHBV, MJMAOA, ICXQIE, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, UHBVWV, OCTHBS, None),
            HBVWVU: GeckoBoolStructAccessor(self.struct, HBVWVU, UHBVWV, NPYYLI, None),
            BVWVUB: GeckoBoolStructAccessor(self.struct, BVWVUB, QFFTTI, NPYYLI, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, QFFTTI, HEOCTH, None),
            WVUBYG: GeckoBoolStructAccessor(self.struct, WVUBYG, QFFTTI, YLIUXF, None),
            VUBYGD: GeckoBoolStructAccessor(self.struct, VUBYGD, QFFTTI, VHFTHE, None),
            UBYGDS: GeckoBoolStructAccessor(self.struct, UBYGDS, TTIDUB, NPYYLI, None),
            BYGDSB: GeckoBoolStructAccessor(self.struct, BYGDSB, TTIDUB, HEOCTH, None),
            YGDSBD: GeckoBoolStructAccessor(self.struct, YGDSBD, TTIDUB, YLIUXF, None),
            GDSBDJ: GeckoBoolStructAccessor(self.struct, GDSBDJ, TTIDUB, VHFTHE, None),
            DSBDJQ: GeckoBoolStructAccessor(self.struct, DSBDJQ, SBDJQR, OCTHBS, None),
            BDJQRJ: GeckoBoolStructAccessor(self.struct, BDJQRJ, SBDJQR, NPYYLI, None),
            DJQRJJ: GeckoBoolStructAccessor(self.struct, DJQRJJ, RYXBQF, XPICXQ, None),
            JQRJJJ: GeckoBoolStructAccessor(self.struct, JQRJJJ, RYXBQF, ICXQIE, None),
            QRJJJV: GeckoBoolStructAccessor(self.struct, QRJJJV, RJJJVY, XPICXQ, None),
            JJJVYF: GeckoByteStructAccessor(self.struct, JJJVYF, JJVYFC, None),
            JVYFCR: GeckoByteStructAccessor(self.struct, JVYFCR, VYFCRT, AKQXPI),
            YFCRTF: GeckoByteStructAccessor(self.struct, YFCRTF, FCRTFM, AKQXPI),
            CRTFMN: GeckoByteStructAccessor(self.struct, CRTFMN, RTFMNH, AKQXPI),
            TFMNHT: GeckoByteStructAccessor(self.struct, TFMNHT, FMNHTB, AKQXPI),
            MNHTBJ: GeckoByteStructAccessor(self.struct, MNHTBJ, NHTBJE, AKQXPI),
            HTBJEU: GeckoBoolStructAccessor(self.struct, HTBJEU, TBJEUT, XPICXQ, None),
            BJEUTO: GeckoBoolStructAccessor(self.struct, BJEUTO, TBJEUT, ICXQIE, None),
            JEUTOP: GeckoBoolStructAccessor(self.struct, JEUTOP, TBJEUT, OCTHBS, None),
            EUTOPH: GeckoBoolStructAccessor(self.struct, EUTOPH, TBJEUT, NPYYLI, None),
            UTOPHU: GeckoBoolStructAccessor(self.struct, UTOPHU, TBJEUT, HEOCTH, None),
            TOPHUG: GeckoBoolStructAccessor(self.struct, TOPHUG, NEJNIB, XPICXQ, None),
            OPHUGT: GeckoBoolStructAccessor(self.struct, OPHUGT, UHBVWV, XPICXQ, None),
            PHUGTY: GeckoBoolStructAccessor(self.struct, PHUGTY, UHBVWV, ICXQIE, None),
            HUGTYI: GeckoBoolStructAccessor(self.struct, HUGTYI, UHBVWV, HEOCTH, None),
            UGTYIY: GeckoBoolStructAccessor(self.struct, UGTYIY, GTYIYW, XPICXQ, None),
            TYIYWS: GeckoEnumStructAccessor(
                self.struct, TYIYWS, GTYIYW, ICXQIE, YIYWSK, None, HEOCTH, None
            ),
            IYWSKW: GeckoBoolStructAccessor(self.struct, IYWSKW, GTYIYW, NPYYLI, None),
            YWSKWI: GeckoWordStructAccessor(self.struct, YWSKWI, WSKWIV, None),
            SKWIVD: GeckoBoolStructAccessor(self.struct, SKWIVD, KWIVDN, XPICXQ, None),
            WIVDNQ: GeckoBoolStructAccessor(self.struct, WIVDNQ, IVDNQG, XPICXQ, None),
            VDNQGV: GeckoBoolStructAccessor(self.struct, VDNQGV, IVDNQG, ICXQIE, None),
            DNQGVU: GeckoBoolStructAccessor(self.struct, DNQGVU, SBDJQR, XPICXQ, None),
            NQGVUN: GeckoBoolStructAccessor(self.struct, NQGVUN, SBDJQR, ICXQIE, None),
            QGVUNX: GeckoBoolStructAccessor(self.struct, QGVUNX, SBDJQR, HEOCTH, None),
            GVUNXN: GeckoWordStructAccessor(self.struct, GVUNXN, VUNXNK, None),
            UNXNKM: GeckoByteStructAccessor(self.struct, UNXNKM, NXNKML, None),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, None),
            KMLOIJ: GeckoEnumStructAccessor(
                self.struct, KMLOIJ, MLOIJU, None, QNRXCH, None, None, None
            ),
            NRXCHW: GeckoEnumStructAccessor(
                self.struct, NRXCHW, RXCHWD, XPICXQ, DAFIKJ, None, HEOCTH, None
            ),
            AFIKJP: GeckoEnumStructAccessor(
                self.struct, AFIKJP, RXCHWD, NPYYLI, UNRJZT, None, NRJZTA, None
            ),
            RJZTAT: GeckoBoolStructAccessor(self.struct, RJZTAT, RXCHWD, VHFTHE, None),
            JZTATD: GeckoWordStructAccessor(self.struct, JZTATD, ZTATDZ, None),
            TATDZX: GeckoByteStructAccessor(self.struct, TATDZX, ATDZXN, None),
            TDZXNQ: GeckoByteStructAccessor(self.struct, TDZXNQ, DZXNQT, None),
            ZXNQTM: GeckoByteStructAccessor(self.struct, ZXNQTM, XNQTMF, None),
            NQTMFZ: GeckoByteStructAccessor(self.struct, NQTMFZ, QTMFZD, None),
            TMFZDG: GeckoWordStructAccessor(self.struct, TMFZDG, MFZDGK, None),
            FZDGKE: GeckoByteStructAccessor(self.struct, FZDGKE, ZDGKEA, None),
            DGKEAK: GeckoByteStructAccessor(self.struct, DGKEAK, GKEAKS, None),
            KEAKST: GeckoWordStructAccessor(self.struct, KEAKST, EAKSTS, None),
            AKSTSE: GeckoEnumStructAccessor(
                self.struct, AKSTSE, KSTSEM, None, SEMCGE, None, OCTHBS, AKQXPI
            ),
            EMCGET: GeckoEnumStructAccessor(
                self.struct, EMCGET, MCGETI, None, BXIBHZ, None, None, None
            ),
            XIBHZV: GeckoWordStructAccessor(self.struct, XIBHZV, IBHZVO, None),
            BHZVOA: GeckoByteStructAccessor(self.struct, BHZVOA, HZVOAC, None),
            ZVOACM: GeckoByteStructAccessor(self.struct, ZVOACM, VOACMC, None),
            OACMCV: GeckoEnumStructAccessor(
                self.struct, OACMCV, ACMCVD, None, MKQTDK, None, None, AKQXPI
            ),
            KQTDKH: GeckoEnumStructAccessor(
                self.struct, KQTDKH, QTDKHT, None, MKQTDK, None, None, AKQXPI
            ),
            TDKHTZ: GeckoEnumStructAccessor(
                self.struct, TDKHTZ, DKHTZB, None, MKQTDK, None, None, AKQXPI
            ),
            KHTZBB: GeckoEnumStructAccessor(
                self.struct, KHTZBB, HTZBBE, None, MKQTDK, None, None, AKQXPI
            ),
            TZBBEK: GeckoEnumStructAccessor(
                self.struct, TZBBEK, ZBBEKB, None, MKQTDK, None, None, AKQXPI
            ),
            BBEKBD: GeckoEnumStructAccessor(
                self.struct, BBEKBD, BEKBDF, None, KBDFSR, None, None, AKQXPI
            ),
            BDFSRO: GeckoByteStructAccessor(self.struct, BDFSRO, DFSROG, AKQXPI),
            FSROGM: GeckoByteStructAccessor(self.struct, FSROGM, SROGMD, AKQXPI),
            ROGMDD: GeckoByteStructAccessor(self.struct, ROGMDD, OGMDDP, AKQXPI),
            GMDDPM: GeckoByteStructAccessor(self.struct, GMDDPM, MDDPMX, AKQXPI),
            DDPMXF: GeckoByteStructAccessor(self.struct, DDPMXF, DPMXFU, AKQXPI),
            PMXFUB: GeckoByteStructAccessor(self.struct, PMXFUB, MXFUBJ, AKQXPI),
            XFUBJL: GeckoEnumStructAccessor(
                self.struct, XFUBJL, FUBJLO, None, BJLOIN, None, None, AKQXPI
            ),
            JLOINE: GeckoEnumStructAccessor(
                self.struct, JLOINE, LOINEL, None, BJLOIN, None, None, AKQXPI
            ),
            OINELW: GeckoEnumStructAccessor(
                self.struct, OINELW, INELWU, None, BJLOIN, None, None, AKQXPI
            ),
            NELWUE: GeckoEnumStructAccessor(
                self.struct, NELWUE, ELWUEU, None, BJLOIN, None, None, AKQXPI
            ),
            LWUEUH: GeckoEnumStructAccessor(
                self.struct, LWUEUH, WUEUHN, None, BJLOIN, None, None, AKQXPI
            ),
            UEUHNN: GeckoEnumStructAccessor(
                self.struct, UEUHNN, EUHNNX, None, BJLOIN, None, None, AKQXPI
            ),
            UHNNXW: GeckoEnumStructAccessor(
                self.struct, UHNNXW, HNNXWE, None, BJLOIN, None, None, AKQXPI
            ),
            NNXWEE: GeckoEnumStructAccessor(
                self.struct, NNXWEE, NXWEEZ, None, XWEEZF, None, None, AKQXPI
            ),
            WEEZFE: GeckoEnumStructAccessor(
                self.struct, WEEZFE, EEZFET, None, XWEEZF, None, None, AKQXPI
            ),
            EZFETD: GeckoByteStructAccessor(self.struct, EZFETD, ZFETDR, AKQXPI),
            FETDRX: GeckoByteStructAccessor(self.struct, FETDRX, ETDRXA, AKQXPI),
            TDRXAI: GeckoByteStructAccessor(self.struct, TDRXAI, DRXAIV, AKQXPI),
            RXAIVE: GeckoByteStructAccessor(self.struct, RXAIVE, XAIVEM, AKQXPI),
            AIVEMV: GeckoByteStructAccessor(self.struct, AIVEMV, IVEMVC, AKQXPI),
            VEMVCY: GeckoByteStructAccessor(self.struct, VEMVCY, EMVCYW, AKQXPI),
            MVCYWO: GeckoByteStructAccessor(self.struct, MVCYWO, VCYWON, AKQXPI),
            CYWONF: GeckoByteStructAccessor(self.struct, CYWONF, YWONFZ, AKQXPI),
            WONFZC: GeckoByteStructAccessor(self.struct, WONFZC, ONFZCZ, AKQXPI),
            TUVRFL: GeckoBoolStructAccessor(self.struct, TUVRFL, JVHFTH, YLIUXF, None),
            UVRFLS: GeckoByteStructAccessor(self.struct, UVRFLS, VRFLSI, AKQXPI),
            RFLSIJ: GeckoEnumStructAccessor(
                self.struct, RFLSIJ, FLSIJU, None, ZMRKVF, None, None, AKQXPI
            ),
            MRKVFC: GeckoBoolStructAccessor(
                self.struct, MRKVFC, RKVFCP, XPICXQ, AKQXPI
            ),
        }

#!/usr/bin/python3
"""
    GeckoLogStruct - A class to manage the LogStruct for 'InYT v66'
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
    chr(c) for c in [83, 108, 97, 118, 101, 72, 116, 114, 83, 116, 117, 99, 107]
)
AFIKJP = "".join(chr(c) for c in [75, 49, 48, 48])
AIIDNI = "".join(
    chr(c) for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 76, 101, 118, 101, 108, 50]
)
AIVEMV = 464
AJVDQL = 350
AKQXPI = "".join(chr(c) for c in [65, 76, 76])
AKSTSE = "".join(chr(c) for c in [80, 52, 76])
AOAWBS = "".join(chr(c) for c in [67, 104, 101, 99, 107, 70, 108, 111])
AONPYY = 310
APUMEA = "".join(chr(c) for c in [72, 69, 65, 84, 73, 78, 71, 95, 70, 65, 73, 76])
ATDZXN = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 115, 101, 116])
AWBSIR = "".join(
    chr(c) for c in [80, 114, 111, 103, 69, 99, 111, 110, 65, 99, 116, 105, 118, 101]
)
AXNCUG = "".join(
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
AZMKQT = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50])
BBEKBD = "".join(chr(c) for c in [83, 79, 117, 116, 57, 67, 117, 114])
BDFSRO = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49, 67, 117, 114])
BDJQRJ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 78, 111, 70, 108, 111, 69, 114, 114]
)
BEKBDF = 343
BFEGZU = 261
BHZVOA = 329
BIAMJM = 277
BJEUTO = "".join(chr(c) for c in [105, 110, 67, 108, 101, 97, 114])
BJLOIN = 451
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
BQNRXC = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 84, 121, 112, 101])
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
BSIRYX = "".join(chr(c) for c in [69, 99, 111, 110, 65, 99, 116, 105, 118, 101])
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
BVWVUB = "".join(chr(c) for c in [82, 104, 82, 101, 103, 83, 108, 111, 112, 101])
BWJYKL = 282
BXIBHZ = "".join(chr(c) for c in [83, 79, 117, 116, 50, 67, 117, 114])
BXTIAC = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 116, 117, 99, 107])
BXYBQS = "".join(chr(c) for c in [80, 82, 69, 83, 83, 85, 82, 69, 95, 69, 82, 82])
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
CHWDAF = "".join(chr(c) for c in [75, 56])
CMCVDS = 333
CPQIPO = 263
CQBMJV = 317
CQFFTT = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 108, 97, 121, 83, 116, 117, 99, 107]
)
CRHYUA = "".join(chr(c) for c in [67, 70, 71, 51, 49])
CRTFMN = 288
CTHBSK = "".join(chr(c) for c in [85, 100, 80, 51])
CTTGCR = "".join(chr(c) for c in [67, 70, 71, 50, 57])
CUGUCY = 373
CVDSSR = 325
CVYYPI = "".join(chr(c) for c in [68, 101, 97, 108, 101, 114, 79, 112, 116])
CWAONP = 7
CXQIEF = "".join(chr(c) for c in [81, 117, 105, 101, 116, 83, 116, 97, 116, 101])
CYRAPU = "".join(chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 70, 65, 73, 76])
CYWONF = 467
CZOLSI = "".join(chr(c) for c in [67, 70, 71, 50, 51])
DAFIKJ = "".join(chr(c) for c in [75, 54, 48, 48, 76, 69])
DDPMXF = "".join(chr(c) for c in [67, 70, 71, 48])
DFSROG = 345
DGKEAK = "".join(chr(c) for c in [80, 50, 76])
DJQRJJ = 315
DKHTZB = 340
DMPSCT = "".join(chr(c) for c in [67, 70, 71, 50, 55])
DNIBXT = "".join(chr(c) for c in [82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116])
DNQGVU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 118])
DPMXFU = 448
DQLAII = 383
DRXAIV = "".join(chr(c) for c in [67, 70, 71, 49, 53])
DSBDJQ = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
DUBSSU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 77, 105, 115, 115, 105, 110, 103, 69, 114, 114]
)
DZXNQT = "".join(chr(c) for c in [45, 45, 45])
EAKSTS = "".join(chr(c) for c in [80, 52, 72])
EAOESV = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 74, 117, 115, 116, 82, 101, 115, 101, 116]
)
ECVYYP = "".join(
    chr(c) for c in [73, 110, 115, 116, 97, 108, 108, 101, 114, 79, 112, 116]
)
EEZFET = "".join(chr(c) for c in [67, 70, 71, 49, 50])
EFJTAC = "".join(
    chr(c) for c in [70, 105, 108, 116, 101, 114, 65, 99, 99, 101, 115, 115]
)
EFXQGL = "".join(chr(c) for c in [83, 79, 65, 75])
EGZUQE = "".join(chr(c) for c in [76, 79, 87])
EJNIBX = "".join(
    chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 82, 69, 81, 85, 69, 83, 84]
)
EKBDFS = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48, 67, 117, 114])
EKCWAO = "".join(chr(c) for c in [83, 76, 86, 95, 72, 69, 65, 84, 69, 82])
EKVKZI = "".join(
    chr(c) for c in [71, 69, 67, 75, 79, 95, 53, 48, 48, 48, 87, 95, 85, 76]
)
ELHBQN = "".join(chr(c) for c in [82, 101, 115, 116, 114, 105, 99, 116, 101, 100])
ELWUEU = 454
EMCGET = "".join(chr(c) for c in [83, 79, 117, 116, 50])
EMVCYW = "".join(chr(c) for c in [67, 70, 71, 49, 56])
EOCTHB = "".join(chr(c) for c in [85, 100, 80, 50])
ETDRXA = "".join(chr(c) for c in [67, 70, 71, 49, 52])
ETIXQV = "".join(chr(c) for c in [83, 79, 117, 116, 52])
EUHNNX = 456
EUTOPH = "".join(chr(c) for c in [75, 54, 48, 48])
EXLSXU = "".join(chr(c) for c in [80, 53])
EZFETD = 460
FCRTFM = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 108])
FEFJTA = 367
FEGZUQ = "".join(chr(c) for c in [72, 73, 71, 72])
FETDRX = 461
FFTTID = 351
FIKJPU = "".join(chr(c) for c in [75, 56, 48, 48])
FJBIAM = 275
FJTACC = 262
FMNHTB = "".join(chr(c) for c in [85, 110, 107, 110, 111, 119, 110])
FSROGM = "".join(chr(c) for c in [83, 79, 117, 116, 49, 50, 67, 117, 114])
FTHECV = 319
FTSIFJ = "".join(chr(c) for c in [83, 119, 109, 65, 100, 99])
FTTIDU = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 79, 118, 101, 114, 72, 101, 97, 116]
)
FUBJLO = 450
FWRKIN = "".join(chr(c) for c in [67, 72, 73, 76, 76])
FXQGLR = "".join(chr(c) for c in [79, 70, 70])
FYLJUI = 378
FZCZOL = "".join(chr(c) for c in [67, 70, 71, 50, 50])
FZDGKE = "".join(chr(c) for c in [80, 49, 76])
GCRHYU = 478
GDSBDJ = 311
GETIXQ = 322
GKEAKS = "".join(chr(c) for c in [80, 51, 72])
GLRAHE = 259
GMDDPM = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
GQPLSP = "".join(chr(c) for c in [77, 69, 68])
GSELHB = "".join(chr(c) for c in [80, 97, 99, 107, 76, 111, 103, 84, 114, 105, 103])
GTYIYW = "".join(chr(c) for c in [49, 54, 75])
GUCYRA = 374
GVUNXN = 294
GYOUSP = "".join(chr(c) for c in [80, 117, 114, 103, 101])
HBSKSO = "".join(chr(c) for c in [85, 100, 80, 53])
HBVWVU = "".join(
    chr(c) for c in [82, 104, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
HBXIBH = 327
HECVYY = "".join(chr(c) for c in [])
HEOCTH = 4
HFTHEC = "".join(chr(c) for c in [77, 101, 110, 117])
HIUSOO = "".join(chr(c) for c in [85, 100, 80, 117, 109, 112, 84, 105, 109, 101])
HNNXWE = 457
HTBJEU = "".join(chr(c) for c in [77, 73, 65])
HTZBBE = 341
HUGTYI = "".join(chr(c) for c in [80, 97, 99, 107, 77, 101, 109, 82, 97, 110, 103, 101])
HUOJRJ = "".join(chr(c) for c in [85, 100, 76, 105])
HWDAFI = "".join(chr(c) for c in [75, 52])
HXEKVK = "".join(
    chr(c) for c in [71, 69, 67, 75, 79, 95, 53, 48, 48, 48, 87, 95, 67, 69]
)
HYUAXN = "".join(
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
HZVOAC = "".join(chr(c) for c in [83, 79, 117, 116, 52, 67, 117, 114])
IACQFF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 50, 72, 83, 116, 117, 99, 107]
)
IAMJMA = "".join(chr(c) for c in [72, 101, 97, 116, 105, 110, 103])
IBHZVO = "".join(chr(c) for c in [83, 79, 117, 116, 51, 67, 117, 114])
IBXTIA = "".join(chr(c) for c in [80, 50, 72, 83, 116, 117, 99, 107])
IBXYBQ = "".join(chr(c) for c in [69, 69, 49, 95, 69, 69, 50, 95, 69, 82, 82])
ICXQIE = 1
IDNIBX = 283
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
IFJBIA = "".join(
    chr(c) for c in [82, 101, 97, 108, 83, 101, 116, 80, 111, 105, 110, 116, 71]
)
IGYOUS = 273
IHBXIB = "".join(chr(c) for c in [83, 79, 117, 116, 49, 67, 117, 114])
IIDNIB = "".join(chr(c) for c in [75, 105, 110, 80, 117, 109, 112, 79, 102, 102])
IJUGSE = 300
IKFWRK = "".join(chr(c) for c in [72, 80, 67, 65, 117, 116, 111, 77, 111, 100, 101])
IKJPUN = "".join(chr(c) for c in [75, 54, 48, 48, 72, 69])
ILXWAJ = "".join(
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
INEJNI = "".join(chr(c) for c in [72, 69, 65, 84, 95, 79, 78])
INELWU = 453
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
IPMDMP = 473
IPOUYN = "".join(chr(c) for c in [83, 84, 65, 82, 84])
IRYXBQ = 352
IUSOOQ = 303
IUXFEF = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 83, 101, 101, 100]
)
IVDNQG = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 73, 68])
IVEMVC = "".join(chr(c) for c in [67, 70, 71, 49, 55])
IVLASS = "".join(chr(c) for c in [78, 79, 84, 95, 73, 78, 83, 84, 65, 76, 76, 69, 68])
IXQVXO = "".join(chr(c) for c in [83, 79, 117, 116, 53])
IYWSKW = "".join(chr(c) for c in [54, 52, 75])
JBIAMJ = "".join(
    chr(c) for c in [68, 105, 115, 112, 108, 97, 121, 101, 100, 84, 101, 109, 112, 71]
)
JEUTOP = "".join(chr(c) for c in [105, 110, 88, 77])
JHIUSO = 370
JIGYOU = "".join(chr(c) for c in [67, 108, 101, 97, 110])
JJJVYF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 82, 101, 103, 83, 108, 111, 112, 101]
)
JJVYFC = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 73, 68])
JLOINE = "".join(chr(c) for c in [67, 70, 71, 52])
JMAOAW = 279
JMCBFE = "".join(chr(c) for c in [85, 100, 65, 117, 120, 84, 105, 109, 101])
JNIBXY = "".join(
    chr(c) for c in [67, 79, 73, 76, 95, 83, 69, 78, 83, 79, 82, 95, 69, 82, 82]
)
JPUNRJ = "".join(chr(c) for c in [73, 78, 86, 65, 76, 73, 68, 95, 84, 89, 80, 69])
JQRJJJ = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 78, 111, 70, 108, 111, 69, 114, 114]
)
JRJHIU = 363
JTACCP = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76])
JUGSEL = "".join(
    chr(c)
    for c in [80, 97, 99, 107, 78, 117, 109, 98, 101, 114, 79, 102, 67, 111, 110, 102]
)
JUIKFW = "".join(
    chr(c) for c in [72, 80, 67, 72, 101, 97, 116, 82, 101, 113, 117, 101, 115, 116]
)
JUTYEK = 3
JVDQLA = "".join(
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
JVHFTH = 274
JVYFCR = 285
JWMNZM = 272
JYKLGQ = "".join(chr(c) for c in [83, 119, 109, 65, 99, 116, 105, 118, 101])
JYMOUN = 266
JZTATD = 360
KBDFSR = 344
KCWAON = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
KEAKST = "".join(chr(c) for c in [80, 51, 76])
KFWRKI = "".join(chr(c) for c in [72, 69, 65, 84])
KHTZBB = "".join(chr(c) for c in [83, 79, 117, 116, 55, 67, 117, 114])
KINEJN = 379
KJPUNR = "".join(chr(c) for c in [75, 51, 48, 48])
KLGQPL = 313
KMLOIJ = 297
KPHUOJ = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48])
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
KVKZIL = "".join(
    chr(c) for c in [71, 69, 67, 75, 79, 95, 55, 53, 48, 48, 87, 95, 85, 76]
)
KWIVDN = "".join(chr(c) for c in [67, 69])
KXSJWM = "".join(
    chr(c)
    for c in [82, 101, 109, 111, 116, 101, 78, 98, 79, 102, 80, 104, 97, 115, 101, 115]
)
KZILXW = "".join(
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
LAIIDN = "".join(
    chr(c)
    for c in [84, 104, 101, 114, 109, 105, 115, 116, 97, 110, 99, 101, 69, 114, 114]
)
LASSAK = "".join(chr(c) for c in [84, 82, 69, 65, 68, 77, 73, 76, 76])
LGQPLS = "".join(chr(c) for c in [78, 79])
LHBQNR = "".join(chr(c) for c in [70, 117, 108, 108])
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
LOIJUG = 299
LOINEL = 452
LRAHEO = "".join(chr(c) for c in [76, 79])
LSIPMD = 472
LSPFTS = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 83, 119, 109, 80, 117, 114, 103, 101]
)
LWUEUH = "".join(chr(c) for c in [67, 70, 71, 55])
LXWAJV = 284
MAOAWB = "".join(
    chr(c)
    for c in [69, 120, 116, 80, 114, 111, 98, 101, 68, 101, 116, 101, 99, 116, 101, 100]
)
MCBFEG = 369
MCGETI = 321
MCVDSS = "".join(chr(c) for c in [83, 79, 117, 116, 54])
MDDPMX = 348
MDMPSC = 474
MEAOES = 375
MFZDGK = "".join(chr(c) for c in [80, 49, 72])
MHXEKV = "".join(chr(c) for c in [71, 69, 78, 69, 82, 73, 67])
MJIGYO = 381
MJMAOA = "".join(
    chr(c) for c in [84, 101, 109, 112, 78, 111, 116, 86, 97, 108, 105, 100]
)
MJVHFT = "".join(
    chr(c) for c in [83, 116, 105, 99, 107, 68, 101, 116, 101, 99, 116, 101, 100]
)
MKQTDK = 332
MLOIJU = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 118])
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
MPSCTT = 475
MVCYWO = 466
MXFUBJ = 449
NBLKXS = 268
NCUGUC = "".join(
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
NEJNIB = "".join(chr(c) for c in [67, 72, 73, 76, 76, 95, 79, 78])
NELWUE = "".join(chr(c) for c in [67, 70, 71, 54])
NFZCZO = 469
NHTBJE = "".join(chr(c) for c in [77, 97, 115, 73, 66, 67])
NIBXTI = "".join(chr(c) for c in [80, 49, 72, 83, 116, 117, 99, 107])
NIBXYB = "".join(
    chr(c) for c in [65, 77, 66, 73, 69, 78, 84, 95, 84, 69, 77, 80, 95, 69, 82, 82]
)
NKMLOI = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 73, 68])
NMHXEK = 389
NNXWEE = "".join(chr(c) for c in [67, 70, 71, 49, 48])
NPYYLI = "".join(chr(c) for c in [80, 65, 82, 84, 73, 65, 76])
NQGVUN = 293
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
NQTMFZ = "".join(chr(c) for c in [83, 79, 117, 116, 49])
NRJZTA = 358
NRSJMC = 306
NRXCHW = "".join(chr(c) for c in [75, 50, 48, 48])
NXNKML = "".join(
    chr(c) for c in [80, 97, 99, 107, 83, 116, 97, 116, 117, 115, 76, 105, 98]
)
NXWEEZ = 458
NZMJIG = 380
OACMCV = 331
OAWBSI = 280
OCTHBS = 2
OESVZS = "".join(chr(c) for c in [76, 73])
OGMDDP = 347
OIJUGS = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 82, 101, 108])
OINELW = "".join(chr(c) for c in [67, 70, 71, 53])
OJRJHI = "".join(chr(c) for c in [85, 100, 87, 97, 116, 101, 114, 102, 97, 108, 108])
OLSIPM = "".join(chr(c) for c in [67, 70, 71, 50, 52])
ONFZCZ = "".join(chr(c) for c in [67, 70, 71, 50, 49])
ONPYYL = "".join(chr(c) for c in [85, 78, 76, 79, 67, 75])
OOQNRS = "".join(chr(c) for c in [85, 100, 76, 105, 103, 104, 116, 84, 105, 109, 101])
OPHUGT = "".join(chr(c) for c in [105, 110, 89, 84])
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
PMDMPS = "".join(chr(c) for c in [67, 70, 71, 50, 54])
PMXFUB = "".join(chr(c) for c in [67, 70, 71, 49])
POUYNQ = "".join(chr(c) for c in [78, 69, 87])
PQIPOU = "".join(chr(c) for c in [73, 68, 76, 69])
PSCTTG = "".join(chr(c) for c in [67, 70, 71, 50, 56])
PYYLIU = "".join(chr(c) for c in [70, 85, 76, 76])
QBMJVH = "".join(chr(c) for c in [72, 111, 117, 114, 115])
QEXLSX = "".join(chr(c) for c in [80, 52])
QFFTTI = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 75, 105, 110, 80, 117, 109, 112, 79, 102, 102]
)
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
QGVUNX = "".join(chr(c) for c in [80, 97, 99, 107, 67, 111, 114, 101, 82, 101, 108])
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
QLAIID = "".join(
    chr(c) for c in [84, 104, 101, 114, 109, 70, 117, 115, 101, 69, 114, 114]
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
QNRSJM = "".join(chr(c) for c in [85, 100, 76, 49, 50, 48, 84, 105, 109, 101])
QNRXCH = 357
QPLSPF = "".join(chr(c) for c in [69, 88, 84, 82, 69, 77, 69])
QRJJJV = "".join(chr(c) for c in [83, 108, 97, 118, 101, 72, 76, 69, 114, 114])
QSNQLN = 392
QTDKHT = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 50])
QTMFZD = 320
QVXOIH = "".join(chr(c) for c in [83, 79, 117, 116, 72, 116, 114])
QXPICX = 388
RAHEOC = "".join(chr(c) for c in [72, 73])
RAPUME = "".join(
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
RAZMKQ = "".join(chr(c) for c in [83, 79, 117, 116, 49, 49])
RHYUAX = 479
RJHIUS = "".join(chr(c) for c in [85, 100, 65, 117, 120])
RJJJVY = "".join(
    chr(c)
    for c in [83, 108, 97, 118, 101, 82, 101, 103, 80, 114, 111, 98, 101, 69, 114, 114]
)
RJZTAT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 118])
RKINEJ = "".join(chr(c) for c in [72, 80, 67, 83, 116, 97, 116, 101])
ROGMDD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116, 67, 117, 114])
RSJMCB = "".join(
    chr(c)
    for c in [85, 100, 87, 97, 116, 101, 114, 70, 97, 108, 108, 84, 105, 109, 101]
)
RTFMNH = "".join(chr(c) for c in [80, 97, 99, 107, 84, 121, 112, 101])
RURAZM = "".join(chr(c) for c in [83, 79, 117, 116, 57])
RXAIVE = 463
RXCHWD = "".join(chr(c) for c in [75, 52, 48, 48])
RYXBQF = "".join(
    chr(c)
    for c in [83, 105, 100, 101, 72, 101, 97, 116, 105, 110, 103, 68, 101, 103, 71]
)
SAKQXP = 386
SBDJQR = 314
SCTTGC = 476
SELHBQ = 316
SIFJBI = "".join(chr(c) for c in [79, 118, 101, 114, 84, 101, 109, 112])
SIPMDM = "".join(chr(c) for c in [67, 70, 71, 50, 53])
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
SKWIVD = "".join(chr(c) for c in [85, 76])
SNQLNM = "".join(
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
SOKPHU = "".join(chr(c) for c in [79, 78])
SOOQNR = 304
SPBWJY = "".join(chr(c) for c in [67, 80, 79, 84])
SPFTSI = 353
SROGMD = 346
SRURAZ = "".join(chr(c) for c in [83, 79, 117, 116, 56])
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
SSBVNA = 479
SSRURA = "".join(chr(c) for c in [83, 79, 117, 116, 55])
SSUHBV = 387
STSEMC = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
SUHBVW = "".join(
    chr(c) for c in [82, 104, 70, 108, 111, 68, 101, 116, 101, 99, 116, 101, 100]
)
SXUJUT = "".join(chr(c) for c in [66, 76])
TACCPQ = "".join(chr(c) for c in [82, 69, 77, 79, 84, 69])
TATDZX = 361
TBJEUT = "".join(chr(c) for c in [68, 74, 83, 52])
TDKHTZ = "".join(chr(c) for c in [83, 79, 117, 116, 54, 67, 117, 114])
TDRXAI = 462
TDZXNQ = 376
TFMNHT = 289
TGCRHY = "".join(chr(c) for c in [67, 70, 71, 51, 48])
THBSKS = "".join(chr(c) for c in [85, 100, 80, 52])
THECVY = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
TIACQF = "".join(
    chr(c) for c in [83, 108, 97, 118, 101, 80, 49, 72, 83, 116, 117, 99, 107]
)
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
TSIFJB = 355
TTGCRH = 477
TTIDUB = "".join(
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
TYEKCW = "".join(chr(c) for c in [77, 83, 84, 82, 95, 72, 69, 65, 84, 69, 82])
TYIYWS = "".join(chr(c) for c in [51, 50, 75])
TZBBEK = "".join(chr(c) for c in [83, 79, 117, 116, 56, 67, 117, 114])
UAXNCU = 371
UBJLOI = "".join(chr(c) for c in [67, 70, 71, 51])
UBSSUH = 354
UCYRAP = "".join(chr(c) for c in [70, 76, 79, 87, 95, 79, 75])
UEUHNN = "".join(chr(c) for c in [67, 70, 71, 56])
UGSELH = 301
UGTYIY = 290
UGUCYR = "".join(
    chr(c) for c in [105, 110, 70, 108, 111, 69, 114, 114, 111, 114, 84, 121, 112, 101]
)
UHBVWV = "".join(chr(c) for c in [82, 104, 72, 119, 72, 76])
UHNNXW = "".join(chr(c) for c in [67, 70, 71, 57])
UIKFWR = "".join(
    chr(c)
    for c in [72, 80, 67, 67, 104, 105, 108, 108, 82, 101, 113, 117, 101, 115, 116]
)
UJUTYE = "".join(chr(c) for c in [79, 51])
UMEAOE = "".join(
    chr(c) for c in [70, 111, 114, 99, 101, 67, 104, 101, 99, 107, 70, 108, 111]
)
UNBLKX = "".join(
    chr(c) for c in [82, 101, 109, 111, 116, 101, 69, 99, 111, 110, 68, 117, 114]
)
UNRJZT = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 73, 68])
UNXNKM = 295
UOJRJH = 307
UQEXLS = "".join(chr(c) for c in [80, 51])
URAZMK = "".join(chr(c) for c in [83, 79, 117, 116, 49, 48])
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
UTOPHU = "".join(chr(c) for c in [105, 110, 84, 101, 114, 102, 97, 99, 101])
UTYEKC = "".join(chr(c) for c in [76, 49, 50, 48])
UXFEFJ = 365
VCYWON = "".join(chr(c) for c in [67, 70, 71, 49, 57])
VDNQGV = 291
VDQLAI = "".join(
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
VDSSRU = "".join(chr(c) for c in [70, 97, 110])
VEMVCY = 465
VHFTHE = 6
VLASSA = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
VOACMC = "".join(chr(c) for c in [83, 79, 117, 116, 53, 67, 117, 114])
VUBYGD = "".join(
    chr(c) for c in [82, 104, 78, 111, 70, 108, 111, 88, 84, 114, 105, 101, 115]
)
VUNXNK = "".join(
    chr(c) for c in [80, 97, 99, 107, 67, 111, 110, 102, 105, 103, 76, 105, 98]
)
VWVUBY = "".join(
    chr(c) for c in [82, 104, 72, 114, 75, 105, 110, 78, 111, 70, 108, 111]
)
VXOIHB = 326
VYFCRT = "".join(chr(c) for c in [80, 97, 99, 107, 66, 111, 111, 116, 82, 101, 118])
VYYPIP = "".join(
    chr(c) for c in [65, 99, 99, 101, 115, 115, 111, 114, 121, 79, 112, 116]
)
VZSSBV = 66
WAJVDQ = "".join(
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
WAONPY = "".join(chr(c) for c in [76, 111, 99, 107, 77, 111, 100, 101])
WBSIRY = 281
WDAFIK = "".join(chr(c) for c in [75, 53])
WEEZFE = 459
WJYKLG = "".join(chr(c) for c in [83, 119, 109, 80, 117, 114, 103, 101])
WMNZMJ = "".join(
    chr(c)
    for c in [80, 114, 111, 103, 79, 117, 116, 112, 117, 116, 65, 99, 99, 101, 115, 115]
)
WONFZC = 468
WSKWIV = "".join(chr(c) for c in [80, 97, 99, 107, 82, 101, 103, 105, 111, 110])
WUEUHN = 455
WVUBYG = 309
XAIVEM = "".join(chr(c) for c in [67, 70, 71, 49, 54])
XBQFYL = "".join(
    chr(c) for c in [73, 110, 71, 114, 105, 100, 68, 101, 116, 101, 99, 116, 101, 100]
)
XCHWDA = "".join(chr(c) for c in [75, 56, 53])
XEKVKZ = "".join(
    chr(c) for c in [71, 69, 67, 75, 79, 95, 55, 53, 48, 48, 87, 95, 67, 69]
)
XFEFJT = "".join(
    chr(c) for c in [68, 101, 97, 108, 101, 114, 76, 111, 99, 107, 75, 101, 121]
)
XFUBJL = "".join(chr(c) for c in [67, 70, 71, 50])
XIBHZV = 328
XLSXUJ = 260
XNCUGU = 372
XNKMLO = 296
XOIHBX = "".join(chr(c) for c in [72, 84, 82])
XPICXQ = 0
XQIEFX = 257
XQVXOI = 324
XSJWMN = 271
XTIACQ = "".join(chr(c) for c in [82, 101, 108, 97, 121, 83, 116, 117, 99, 107])
XUJUTY = "".join(chr(c) for c in [67, 80])
XWAJVD = "".join(
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
XWEEZF = "".join(chr(c) for c in [67, 70, 71, 49, 49])
XYBQSN = "".join(chr(c) for c in [79, 84, 72, 69, 82, 95, 69, 82, 82])
YEKCWA = 5
YFCRTF = 287
YGDSBD = "".join(chr(c) for c in [105, 110, 84, 67, 105, 112, 68, 101, 108, 97, 121])
YIYWSK = "".join(chr(c) for c in [52, 56, 75])
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
YRAPUM = "".join(
    chr(c) for c in [77, 79, 68, 69, 95, 49, 95, 65, 78, 68, 95, 50, 95, 70, 65, 73, 76]
)
YUAXNC = "".join(chr(c) for c in [105, 110, 70, 108, 111, 82, 97, 116, 105, 111])
YWONFZ = "".join(chr(c) for c in [67, 70, 71, 50, 48])
YXBQFY = 377
YYPIPI = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 83, 101, 108, 101, 99, 116]
)
ZBBEKB = 342
ZCQBMJ = "".join(chr(c) for c in [82, 104, 87, 97, 116, 101, 114, 84, 101, 109, 112])
ZCZOLS = 470
ZDGKEA = "".join(chr(c) for c in [80, 50, 72])
ZFETDR = "".join(chr(c) for c in [67, 70, 71, 49, 51])
ZILXWA = 390
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
ZMKQTD = "".join(chr(c) for c in [83, 68, 105, 114, 101, 99, 116])
ZOLSIP = 471
ZSSBVN = 256
ZTATDZ = "".join(chr(c) for c in [75, 101, 121, 112, 97, 100, 82, 101, 108])
ZUQEXL = "".join(chr(c) for c in [80, 50])
ZVOACM = 330
ZXNQTM = "".join(chr(c) for c in [82, 69, 83, 69, 84])
ACCPQI = [JTACCP, TACCPQ]
AHEOCT = [FXQGLR, LRAHEO, RAHEOC]
AMJMAO = [HECVYY, IAMJMA, IAMJMA, IAMJMA]
AOESVZ = []
ASSAKQ = [IVLASS, VLASSA, LASSAK]
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
ESVZSS = [
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
    OESVZS,
]
GZUQEX = [FXQGLR, FEGZUQ, EGZUQE]
HBQNRX = [ELHBQN, LHBQNR]
KQTDKH = [
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
LSXUJU = [FXQGLR, FEGZUQ]
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
PLSPFT = [LGQPLS, LRAHEO, GQPLSP, RAHEOC, QPLSPF]
PUMEAO = [UCYRAP, CYRAPU, YRAPUM, RAPUME, APUMEA]
PUNRJZ = [
    NRXCHW,
    RXCHWD,
    XCHWDA,
    CHWDAF,
    HWDAFI,
    WDAFIK,
    DAFIKJ,
    AFIKJP,
    FIKJPU,
    HECVYY,
    HECVYY,
    HECVYY,
    IKJPUN,
    KJPUNR,
    JPUNRJ,
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
SVZSSB = [
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
UBYGDS = [HECVYY, VUBYGD, VUBYGD, VUBYGD]
UYNQJY = [PQIPOU, QIPOUY, IPOUYN, POUYNQ, OUYNQJ]
VKZILX = [MHXEKV, HXEKVK, XEKVKZ, EKVKZI, KVKZIL]
WIVDNQ = [SKWIVD, KWIVDN]
WRKINE = [KFWRKI, FWRKIN]
XNQTMF = [DZXNQT, ZXNQTM]
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
YWSKWI = [GTYIYW, TYIYWS, YIYWSK, IYWSKW]
YYLIUX = [ONPYYL, NPYYLI, PYYLIU]


class GeckoLogStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return VZSSBV

    @property
    def begin(self):
        return ZSSBVN

    @property
    def end(self):
        return SSBVNA

    @property
    def all_device_keys(self):
        return ESVZSS

    @property
    def user_demand_keys(self):
        return SVZSSB

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
            BQSNQL: GeckoBoolStructAccessor(self.struct, BQSNQL, QSNQLN, XPICXQ, None),
            SNQLNM: GeckoBoolStructAccessor(self.struct, SNQLNM, QSNQLN, ICXQIE, None),
            NQLNMH: GeckoBoolStructAccessor(self.struct, NQLNMH, QSNQLN, OCTHBS, None),
            QLNMHX: GeckoBoolStructAccessor(self.struct, QLNMHX, QSNQLN, JUTYEK, None),
            LNMHXE: GeckoEnumStructAccessor(
                self.struct, LNMHXE, NMHXEK, None, VKZILX, None, None, None
            ),
            KZILXW: GeckoWordStructAccessor(self.struct, KZILXW, ZILXWA, None),
            ILXWAJ: GeckoBoolStructAccessor(self.struct, ILXWAJ, LXWAJV, XPICXQ, None),
            XWAJVD: GeckoBoolStructAccessor(self.struct, XWAJVD, LXWAJV, ICXQIE, None),
            WAJVDQ: GeckoBoolStructAccessor(self.struct, WAJVDQ, AJVDQL, XPICXQ, None),
            JVDQLA: GeckoBoolStructAccessor(self.struct, JVDQLA, AJVDQL, ICXQIE, None),
            VDQLAI: GeckoBoolStructAccessor(self.struct, VDQLAI, DQLAII, XPICXQ, None),
            QLAIID: GeckoBoolStructAccessor(self.struct, QLAIID, JVHFTH, JUTYEK, None),
            LAIIDN: GeckoBoolStructAccessor(self.struct, LAIIDN, BWJYKL, XPICXQ, None),
            AIIDNI: GeckoBoolStructAccessor(self.struct, AIIDNI, BWJYKL, ICXQIE, None),
            IIDNIB: GeckoBoolStructAccessor(self.struct, IIDNIB, IDNIBX, OCTHBS, None),
            DNIBXT: GeckoBoolStructAccessor(self.struct, DNIBXT, IDNIBX, JUTYEK, None),
            NIBXTI: GeckoBoolStructAccessor(self.struct, NIBXTI, LXWAJV, JUTYEK, None),
            IBXTIA: GeckoBoolStructAccessor(self.struct, IBXTIA, LXWAJV, HEOCTH, None),
            BXTIAC: GeckoBoolStructAccessor(self.struct, BXTIAC, LXWAJV, YEKCWA, None),
            XTIACQ: GeckoBoolStructAccessor(self.struct, XTIACQ, LXWAJV, VHFTHE, None),
            TIACQF: GeckoBoolStructAccessor(self.struct, TIACQF, AJVDQL, JUTYEK, None),
            IACQFF: GeckoBoolStructAccessor(self.struct, IACQFF, AJVDQL, HEOCTH, None),
            ACQFFT: GeckoBoolStructAccessor(self.struct, ACQFFT, AJVDQL, YEKCWA, None),
            CQFFTT: GeckoBoolStructAccessor(self.struct, CQFFTT, AJVDQL, VHFTHE, None),
            QFFTTI: GeckoBoolStructAccessor(self.struct, QFFTTI, FFTTID, OCTHBS, None),
            FTTIDU: GeckoBoolStructAccessor(self.struct, FTTIDU, FFTTID, JUTYEK, None),
            TTIDUB: GeckoBoolStructAccessor(self.struct, TTIDUB, IRYXBQ, JUTYEK, None),
            TIDUBS: GeckoBoolStructAccessor(self.struct, TIDUBS, SPFTSI, XPICXQ, None),
            IDUBSS: GeckoBoolStructAccessor(self.struct, IDUBSS, SPFTSI, ICXQIE, None),
            DUBSSU: GeckoBoolStructAccessor(self.struct, DUBSSU, UBSSUH, XPICXQ, None),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, None),
            SUHBVW: GeckoBoolStructAccessor(self.struct, SUHBVW, OAWBSI, XPICXQ, None),
            UHBVWV: GeckoBoolStructAccessor(self.struct, UHBVWV, IDNIBX, XPICXQ, None),
            HBVWVU: GeckoBoolStructAccessor(self.struct, HBVWVU, IDNIBX, ICXQIE, None),
            BVWVUB: GeckoBoolStructAccessor(self.struct, BVWVUB, IDNIBX, HEOCTH, None),
            VWVUBY: GeckoBoolStructAccessor(self.struct, VWVUBY, WVUBYG, XPICXQ, None),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, WVUBYG, ICXQIE, UBYGDS, None, HEOCTH, None
            ),
            BYGDSB: GeckoBoolStructAccessor(self.struct, BYGDSB, WVUBYG, JUTYEK, None),
            YGDSBD: GeckoWordStructAccessor(self.struct, YGDSBD, GDSBDJ, None),
            DSBDJQ: GeckoBoolStructAccessor(self.struct, DSBDJQ, SBDJQR, XPICXQ, None),
            BDJQRJ: GeckoBoolStructAccessor(self.struct, BDJQRJ, DJQRJJ, XPICXQ, None),
            JQRJJJ: GeckoBoolStructAccessor(self.struct, JQRJJJ, DJQRJJ, ICXQIE, None),
            QRJJJV: GeckoBoolStructAccessor(self.struct, QRJJJV, FFTTID, XPICXQ, None),
            RJJJVY: GeckoBoolStructAccessor(self.struct, RJJJVY, FFTTID, ICXQIE, None),
            JJJVYF: GeckoBoolStructAccessor(self.struct, JJJVYF, FFTTID, HEOCTH, None),
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
                self.struct, WSKWIV, UGTYIY, OCTHBS, WIVDNQ, None, OCTHBS, None
            ),
            IVDNQG: GeckoWordStructAccessor(self.struct, IVDNQG, VDNQGV, None),
            DNQGVU: GeckoByteStructAccessor(self.struct, DNQGVU, NQGVUN, None),
            QGVUNX: GeckoByteStructAccessor(self.struct, QGVUNX, GVUNXN, None),
            VUNXNK: GeckoByteStructAccessor(self.struct, VUNXNK, UNXNKM, None),
            NXNKML: GeckoByteStructAccessor(self.struct, NXNKML, XNKMLO, None),
            NKMLOI: GeckoWordStructAccessor(self.struct, NKMLOI, KMLOIJ, None),
            MLOIJU: GeckoByteStructAccessor(self.struct, MLOIJU, LOIJUG, None),
            OIJUGS: GeckoByteStructAccessor(self.struct, OIJUGS, IJUGSE, None),
            JUGSEL: GeckoWordStructAccessor(self.struct, JUGSEL, UGSELH, None),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, SELHBQ, None, HBQNRX, None, OCTHBS, AKQXPI
            ),
            BQNRXC: GeckoEnumStructAccessor(
                self.struct, BQNRXC, QNRXCH, None, PUNRJZ, None, None, None
            ),
            UNRJZT: GeckoWordStructAccessor(self.struct, UNRJZT, NRJZTA, None),
            RJZTAT: GeckoByteStructAccessor(self.struct, RJZTAT, JZTATD, None),
            ZTATDZ: GeckoByteStructAccessor(self.struct, ZTATDZ, TATDZX, None),
            ATDZXN: GeckoEnumStructAccessor(
                self.struct, ATDZXN, TDZXNQ, None, XNQTMF, None, None, AKQXPI
            ),
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
                self.struct, SSRURA, VXOIHB, None, DSSRUR, None, None, AKQXPI
            ),
            SRURAZ: GeckoEnumStructAccessor(
                self.struct, SRURAZ, HBXIBH, None, DSSRUR, None, None, AKQXPI
            ),
            RURAZM: GeckoEnumStructAccessor(
                self.struct, RURAZM, XIBHZV, None, DSSRUR, None, None, AKQXPI
            ),
            URAZMK: GeckoEnumStructAccessor(
                self.struct, URAZMK, BHZVOA, None, DSSRUR, None, None, AKQXPI
            ),
            RAZMKQ: GeckoEnumStructAccessor(
                self.struct, RAZMKQ, ZVOACM, None, DSSRUR, None, None, AKQXPI
            ),
            AZMKQT: GeckoEnumStructAccessor(
                self.struct, AZMKQT, OACMCV, None, DSSRUR, None, None, AKQXPI
            ),
            ZMKQTD: GeckoEnumStructAccessor(
                self.struct, ZMKQTD, MKQTDK, None, KQTDKH, None, None, AKQXPI
            ),
            QTDKHT: GeckoEnumStructAccessor(
                self.struct, QTDKHT, CMCVDS, None, KQTDKH, None, None, AKQXPI
            ),
            TDKHTZ: GeckoByteStructAccessor(self.struct, TDKHTZ, DKHTZB, AKQXPI),
            KHTZBB: GeckoByteStructAccessor(self.struct, KHTZBB, HTZBBE, AKQXPI),
            TZBBEK: GeckoByteStructAccessor(self.struct, TZBBEK, ZBBEKB, AKQXPI),
            BBEKBD: GeckoByteStructAccessor(self.struct, BBEKBD, BEKBDF, AKQXPI),
            EKBDFS: GeckoByteStructAccessor(self.struct, EKBDFS, KBDFSR, AKQXPI),
            BDFSRO: GeckoByteStructAccessor(self.struct, BDFSRO, DFSROG, AKQXPI),
            FSROGM: GeckoByteStructAccessor(self.struct, FSROGM, SROGMD, AKQXPI),
            ROGMDD: GeckoByteStructAccessor(self.struct, ROGMDD, OGMDDP, AKQXPI),
            GMDDPM: GeckoByteStructAccessor(self.struct, GMDDPM, MDDPMX, AKQXPI),
            HYUAXN: GeckoBoolStructAccessor(self.struct, HYUAXN, JVHFTH, YEKCWA, None),
            YUAXNC: GeckoByteStructAccessor(self.struct, YUAXNC, UAXNCU, AKQXPI),
            AXNCUG: GeckoByteStructAccessor(self.struct, AXNCUG, XNCUGU, AKQXPI),
            NCUGUC: GeckoByteStructAccessor(self.struct, NCUGUC, CUGUCY, AKQXPI),
            UGUCYR: GeckoEnumStructAccessor(
                self.struct, UGUCYR, GUCYRA, None, PUMEAO, None, None, AKQXPI
            ),
            UMEAOE: GeckoBoolStructAccessor(
                self.struct, UMEAOE, MEAOES, XPICXQ, AKQXPI
            ),
            EAOESV: GeckoBoolStructAccessor(self.struct, EAOESV, TDZXNQ, XPICXQ, None),
        }

#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYT v66'
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
ACCPQI = 45
ACMCVD = 7
ACQFFT = 114
ADXLUB = "".join(chr(c) for c in [78, 79, 82, 77, 65, 76])
AFIKJP = "".join(
    chr(c) for c in [65, 117, 120, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
AHEOCT = 37
AIIDNI = "".join(chr(c) for c in [72, 69, 65, 84, 95, 87, 95, 66, 79, 79, 83, 84])
AIVEMV = "".join(
    chr(c)
    for c in [
        77,
        111,
        100,
        101,
        75,
        101,
        121,
        65,
        115,
        73,
        110,
        118,
        101,
        114,
        116,
        68,
        105,
        115,
        112,
        108,
        97,
        121,
        75,
        101,
        121,
    ]
)
AKQXPI = "".join(chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108])
AKSTSE = "".join(chr(c) for c in [83, 76, 69, 69, 80])
AOAWBS = 58
AOESVZ = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        55,
    ]
)
AONPYY = 23
APUMEA = 143
ASSAKQ = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
AWBSIR = 59
AXNCUG = "".join(
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
        100,
        105,
        99,
        97,
        116,
        101,
        100,
        80,
        117,
        109,
        112,
        115,
    ]
)
AZMKQT = "".join(chr(c) for c in [71, 82, 69, 69, 78])
BDFSRO = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
BDJQRJ = 87
BEKBDF = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
BFEGZU = "".join(chr(c) for c in [70, 51])
BGJFJN = "".join(chr(c) for c in [90, 111, 110, 101, 50, 84, 121, 112, 101])
BHZVOA = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
BIAMJM = "".join(chr(c) for c in [76, 111])
BJEUTO = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
BJLOIN = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
BLKXSJ = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
BMIKGN = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 49]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = 78
BQNRXC = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
BQSNQL = "".join(chr(c) for c in [70])
BSIRYX = 60
BSKSOK = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
BSSUHB = "".join(
    chr(c)
    for c in [
        77,
        105,
        110,
        105,
        109,
        117,
        109,
        73,
        110,
        112,
        117,
        116,
        67,
        117,
        114,
        114,
        101,
        110,
        116,
    ]
)
BVNAXA = "".join(chr(c) for c in [90, 111, 110, 101, 49, 76, 101, 100])
BWJYKL = 32
BXIBHZ = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
BXYBQS = 1
BYGDSB = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
CBFEGZ = "".join(chr(c) for c in [70, 50])
CCPQIP = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
CHWDAF = 72
CMCVDS = "".join(
    chr(c)
    for c in [
        75,
        101,
        121,
        112,
        97,
        100,
        84,
        104,
        101,
        114,
        97,
        112,
        121,
        83,
        117,
        112,
        112,
        111,
        114,
        116,
    ]
)
CPOUBM = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 49]
)
CPQIPO = 46
CQBMJV = 0
CQFFTT = "".join(chr(c) for c in [85, 76, 95, 67, 69])
CRHYUA = "".join(chr(c) for c in [80, 50, 95, 84, 79, 95, 80, 53])
CRTFMN = "".join(chr(c) for c in [79, 117, 116, 49, 49, 70, 117, 115, 101])
CTHBSK = 39
CTTGCR = "".join(
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
        80,
        117,
        109,
        112,
        115,
        85,
        115,
        101,
        100,
    ]
)
CUGUCY = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        49,
    ]
)
CVDSSR = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 22
CXQIEF = 14
CYRAPU = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        51,
    ]
)
CYWONF = "".join(
    chr(c)
    for c in [
        76,
        111,
        119,
        101,
        114,
        83,
        101,
        116,
        112,
        111,
        105,
        110,
        116,
        77,
        101,
        110,
        117,
    ]
)
CZOLSI = "".join(
    chr(c)
    for c in [
        68,
        101,
        97,
        108,
        101,
        114,
        76,
        111,
        99,
        107,
        83,
        117,
        112,
        112,
        111,
        114,
        116,
    ]
)
DAFIKJ = "".join(
    chr(c)
    for c in [
        67,
        108,
        101,
        97,
        110,
        117,
        112,
        79,
        110,
        67,
        117,
        115,
        116,
        111,
        109,
        75,
        101,
        121,
    ]
)
DDPMXF = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
DFSROG = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
DGKEAK = 132
DJQRJJ = "".join(chr(c) for c in [79, 117, 116, 54, 70, 117, 115, 101])
DMPSCT = "".join(
    chr(c)
    for c in [69, 120, 101, 114, 99, 105, 115, 101, 67, 111, 110, 116, 114, 111, 108]
)
DNIBXT = "".join(chr(c) for c in [65, 85, 84, 79, 95, 83, 65, 86, 69, 82])
DNQGVU = 106
DPMXFU = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
DQLAII = "".join(
    chr(c) for c in [67, 111, 111, 108, 90, 111, 110, 101, 77, 111, 100, 101]
)
DRXAIV = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
DSBDJQ = 86
DSSRUR = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
DUBSSU = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
DXLUBG = "".join(chr(c) for c in [83, 84, 65, 84, 85, 83])
DZXNQT = 75
EAKSTS = "".join(chr(c) for c in [79, 70, 70])
EAOESV = 147
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EEZFET = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
EFJTAC = 43
EFXQGL = 16
EGZUQE = "".join(chr(c) for c in [70, 50, 50])
EKBDFS = 111
EKCWAO = 21
EKVKZI = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
ELHBQN = 10
ELWUEU = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
EMCGET = "".join(chr(c) for c in [78, 79, 84, 95, 65, 76, 76, 79, 87, 69, 68])
EMVCYW = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
EOCTHB = 38
ESVZSS = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        56,
    ]
)
ETDRXA = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
ETIXQV = 34
EUHNNX = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
EUTOPH = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
EZFETD = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
FCPOUB = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 52]
)
FCRTFM = 92
FEFJTA = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
FEGZUQ = "".join(chr(c) for c in [70, 50, 49])
FETDRX = "".join(chr(c) for c in [65, 115, 112, 101, 110])
FFTTID = "".join(chr(c) for c in [85, 76])
FIKJPU = "".join(
    chr(c)
    for c in [
        81,
        117,
        105,
        99,
        107,
        79,
        110,
        79,
        102,
        102,
        67,
        117,
        115,
        116,
        111,
        109,
        75,
        101,
        121,
    ]
)
FJNTTU = "".join(chr(c) for c in [90, 111, 110, 101, 51, 84, 121, 112, 101])
FJTACC = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
FLSIJU = "".join(chr(c) for c in [51])
FMNHTB = 94
FOUURI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 52]
)
FSROGM = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 57
FTTIDU = "".join(chr(c) for c in [67, 69])
FUBJLO = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
FWRKIN = 29
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
FZCZOL = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
FZDGKE = 130
GCRHYU = "".join(chr(c) for c in [65, 76, 76, 95, 80, 85, 77, 80, 83])
GDSBDJ = "".join(chr(c) for c in [79, 117, 116, 52, 70, 117, 115, 101])
GETIXQ = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
GJFJNT = "".join(chr(c) for c in [90, 111, 110, 101, 51, 76, 101, 100])
GKEAKS = "".join(chr(c) for c in [83, 105, 108, 101, 110, 116, 77, 111, 100, 101])
GLRAHE = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
GMDDPM = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
GNVFOU = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 49]
)
GQPLSP = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
GSELHB = 8
GTYIYW = 101
GUCYRA = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        50,
    ]
)
GVUNXN = "".join(chr(c) for c in [70, 50, 50, 76, 105, 110, 101])
GYOUSP = 0
GZUQEX = "".join(chr(c) for c in [70, 50, 51])
HBQNRX = 71
HBSKSO = 40
HBVWVU = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = "".join(chr(c) for c in [56, 65])
HNNXWE = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
HTBJEU = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 70, 117, 115, 101])
HTZBBE = "".join(
    chr(c)
    for c in [
        75,
        101,
        121,
        112,
        97,
        100,
        66,
        97,
        99,
        107,
        108,
        105,
        103,
        104,
        116,
        69,
        100,
        105,
        116,
    ]
)
HUGTYI = 100
HUOJRJ = "".join(chr(c) for c in [50, 65])
HWDAFI = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
HYUAXN = "".join(chr(c) for c in [80, 52, 95, 65, 78, 68, 95, 80, 53])
IACQFF = "".join(
    chr(c)
    for c in [
        77,
        97,
        120,
        78,
        117,
        109,
        98,
        101,
        114,
        79,
        102,
        80,
        104,
        97,
        115,
        101,
        115,
    ]
)
IAMJMA = "".join(chr(c) for c in [72, 105])
IBHZVO = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
IBXTIA = "".join(chr(c) for c in [66, 79, 84, 72, 95, 72, 69, 65, 84])
IBXYBQ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 51])
IDNIBX = "".join(chr(c) for c in [65, 85, 84, 79, 95, 87, 95, 66, 79, 79, 83, 84])
IDUBSS = 52
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 53])
IEVBVH = "".join(
    chr(c)
    for c in [
        82,
        101,
        109,
        105,
        110,
        100,
        101,
        114,
        115,
        78,
        111,
        116,
        66,
        108,
        105,
        110,
        107,
        105,
        110,
        103,
        76,
        69,
        68,
    ]
)
IFJBIA = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
IHBXIB = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
IIDNIB = "".join(chr(c) for c in [72, 69, 65, 84, 95, 83, 65, 86, 69, 82])
IJUGSE = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
IJUZMR = "".join(
    chr(c)
    for c in [
        83,
        116,
        97,
        116,
        117,
        115,
        76,
        105,
        103,
        104,
        116,
        78,
        111,
        114,
        109,
        97,
        108,
        67,
        111,
        108,
        111,
        114,
    ]
)
IKGNVF = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 51]
)
IKJPUN = 5
ILXWAJ = 68
INEJNI = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
INELWU = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPMDMP = "".join(chr(c) for c in [78, 79, 95, 69, 88, 69, 82, 67, 73, 83, 69])
IPOUYN = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
IRYXBQ = 61
IUSOOQ = "".join(chr(c) for c in [57, 65])
IUXFEF = 41
IVDNQG = 105
IVEMVC = 112
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IXQVXO = "".join(chr(c) for c in [50, 52, 104])
IYWSKW = "".join(chr(c) for c in [70, 50, 51, 67, 117, 114, 114, 101, 110, 116])
JBIAMJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
JEUTOP = 97
JFJNTT = 125
JHIUSO = "".join(chr(c) for c in [55, 65])
JIGYOU = "".join(chr(c) for c in [79, 119, 110])
JJJVYF = "".join(chr(c) for c in [79, 117, 116, 56, 70, 117, 115, 101])
JJVYFC = 90
JLOINE = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
JMAOAW = 1
JMCBFE = 163
JNIBXY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
JNTTUV = "".join(chr(c) for c in [90, 111, 110, 101, 52, 76, 101, 100])
JPUNRJ = 76
JQRJJJ = 88
JRJHIU = "".join(chr(c) for c in [53, 65])
JTACCP = 44
JUGSEL = 116
JUIKFW = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
JUTYEK = 19
JUZMRK = "".join(chr(c) for c in [80, 85, 82, 80, 76, 69])
JVDQLA = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [79, 117, 116, 57, 70, 117, 115, 101])
JWMNZM = 55
JYKLGQ = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
JYMOUN = "".join(
    chr(c)
    for c in [
        87,
        97,
        116,
        101,
        114,
        102,
        97,
        108,
        108,
        86,
        97,
        108,
        118,
        101,
        79,
        110,
        67,
        80,
    ]
)
JZTATD = 73
KBDFSR = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
KCWAON = "".join(chr(c) for c in [79, 117, 116, 49, 49])
KEAKST = 157
KFWRKI = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
KGNVFO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 52]
)
KHTZBB = 8
KINEJN = 30
KJPUNR = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
KLGQPL = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
KMLOIJ = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
KPHUOJ = "".join(chr(c) for c in [48, 65])
KQTDKH = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
KQXPIC = "".join(chr(c) for c in [65, 85, 88])
KSOKPH = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 80, 117, 109, 112, 67, 117, 114, 114, 101, 110, 116]
)
KVFCPO = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 50]
)
KVKZIL = 35
KXSJWM = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KZILXW = 66
LAIIDN = "".join(chr(c) for c in [67, 72, 73, 76, 76])
LASSAK = "".join(chr(c) for c in [70, 97, 110])
LHBQNR = "".join(
    chr(c)
    for c in [
        69,
        99,
        111,
        110,
        80,
        114,
        111,
        103,
        65,
        118,
        97,
        105,
        108,
        97,
        98,
        108,
        101,
    ]
)
LIUXFE = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
LJUIKF = 28
LKXSJW = 80
LNMHXE = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
LOIJUG = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
LOINEL = "".join(chr(c) for c in [74, 97, 122, 122, 105])
LRAHEO = 36
LSIJUZ = "".join(chr(c) for c in [52])
LSIPMD = "".join(
    chr(c) for c in [69, 120, 101, 114, 99, 105, 115, 101, 84, 121, 112, 101]
)
LSPFTS = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
LSXUJU = 17
LUBGJF = "".join(chr(c) for c in [90, 111, 110, 101, 50, 76, 101, 100])
LWUEUH = "".join(chr(c) for c in [80, 68, 67])
LXWAJV = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
MAOAWB = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
MCBFEG = "".join(chr(c) for c in [70, 49])
MCGETI = "".join(chr(c) for c in [65, 76, 76, 79, 87, 69, 68])
MCVDSS = 110
MDDPMX = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
MEAOES = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        54,
    ]
)
MFZDGK = "".join(chr(c) for c in [80, 114, 111, 103, 79, 117, 116, 68, 117, 114])
MHXEKV = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
MIKGNV = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 51, 84, 111, 79, 117, 116, 50]
)
MJIGYO = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
MJMAOA = "".join(
    chr(c) for c in [65, 117, 120, 65, 115, 66, 117, 98, 98, 108, 101, 71, 101, 110]
)
MJVHFT = 12
MKQTDK = "".join(chr(c) for c in [66, 76, 85, 69])
MLOIJU = 4
MNHTBJ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
MNZMJI = 56
MOUNBL = "".join(chr(c) for c in [79, 117, 116, 76, 105])
MPSCTT = 134
MRKVFC = "".join(
    chr(c) for c in [77, 97, 112, 112, 105, 110, 103, 69, 110, 97, 98, 108, 101]
)
MVCYWO = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
MXFUBJ = "".join(chr(c) for c in [67, 111, 97, 115, 116])
NAXADX = "".join(chr(c) for c in [82, 71, 66])
NCUGUC = 136
NEJNIB = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
NELWUE = "".join(chr(c) for c in [77, 65, 65, 88])
NHTBJE = 95
NIBXTI = "".join(chr(c) for c in [73, 78, 84, 69, 82, 78, 65, 76, 95, 72, 69, 65, 84])
NIBXYB = 63
NKMLOI = 3
NMHXEK = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
NNXWEE = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
NPYYLI = 24
NQGVUN = "".join(chr(c) for c in [70, 50, 49, 76, 105, 110, 101])
NQJYMO = 119
NQLNMH = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
NRSJMC = "".join(chr(c) for c in [49, 53, 65])
NRXCHW = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
NTTUVR = 126
NVFOUU = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 50]
)
NXNKML = 109
NXWEEZ = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
NZMJIG = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
OACMCV = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
OAWBSI = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
OESVZS = 149
OGMDDP = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
OIHBXI = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
OIJUGS = 6
OINELW = "".join(chr(c) for c in [76, 65])
OJRJHI = "".join(chr(c) for c in [52, 65])
OKPHUO = "".join(chr(c) for c in [78, 111, 116, 95, 83, 101, 116])
OLSIPM = 121
ONFZCZ = "".join(chr(c) for c in [70, 111, 114, 90, 111, 110, 101, 115])
ONPYYL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
OOQNRS = "".join(chr(c) for c in [49, 50, 65])
OPHUGT = 99
OQNRSJ = "".join(chr(c) for c in [49, 51, 65])
OUBMIK = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 51]
)
OUNBLK = 79
OUSPBW = 118
OUURIE = "".join(
    chr(c)
    for c in [
        83,
        116,
        97,
        116,
        117,
        115,
        76,
        105,
        103,
        104,
        116,
        82,
        101,
        109,
        105,
        110,
        100,
        101,
        114,
        115,
        67,
        111,
        108,
        111,
        114,
    ]
)
OUYNQJ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
PBWJYK = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
PFTSIF = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
PHUGTY = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
PHUOJR = "".join(chr(c) for c in [49, 65])
PICXQI = 13
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
PMDMPS = "".join(chr(c) for c in [83, 87, 73, 77, 95, 69, 88, 69, 82, 67, 73, 83, 69])
PMXFUB = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
POUBMI = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 50]
)
POUYNQ = 48
PQIPOU = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
PSCTTG = "".join(
    chr(c)
    for c in [85, 83, 69, 95, 83, 84, 65, 78, 68, 65, 82, 68, 95, 80, 85, 77, 80, 83]
)
PUMEAO = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        53,
    ]
)
PUNRJZ = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [76, 105, 110, 101, 51])
QFFTTI = 51
QFYLJU = "".join(chr(c) for c in [80, 49])
QGVUNX = 107
QIEFXQ = 15
QIPOUY = 47
QJYMOU = 2
QLAIID = 115
QLNMHX = 31
QNRSJM = "".join(chr(c) for c in [49, 52, 65])
QPLSPF = 27
QRJJJV = "".join(chr(c) for c in [79, 117, 116, 55, 70, 117, 115, 101])
QSNQLN = "".join(chr(c) for c in [67])
QTDKHT = "".join(chr(c) for c in [67, 89, 65, 78])
QTMFZD = "".join(
    chr(c) for c in [80, 114, 111, 103, 79, 117, 116, 83, 116, 97, 114, 116]
)
QVXOIH = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
RAHEOC = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
RAPUME = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        52,
    ]
)
RAZMKQ = "".join(chr(c) for c in [82, 69, 68])
RFLSIJ = "".join(chr(c) for c in [50])
RHYUAX = "".join(chr(c) for c in [80, 51, 95, 84, 79, 95, 80, 53])
RJHIUS = "".join(chr(c) for c in [54, 65])
RJJJVY = 89
RJZTAT = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
RKINEJ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
RKVFCP = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 49]
)
ROGMDD = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
RTFMNH = 93
RURAZM = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
RXAIVE = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 95, 83, 112, 97, 115])
RXCHWD = 82
RYXBQF = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
SAKQXP = "".join(chr(c) for c in [72, 84, 82, 50])
SBDJQR = "".join(chr(c) for c in [79, 117, 116, 53, 70, 117, 115, 101])
SBVNAX = 155
SELHBQ = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
SEMCGE = "".join(
    chr(c)
    for c in [
        83,
        117,
        115,
        112,
        101,
        110,
        100,
        83,
        105,
        108,
        101,
        110,
        116,
        84,
        111,
        82,
        101,
        103,
        117,
        108,
        97,
        116,
        101,
    ]
)
SIFJBI = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
SIPMDM = 133
SIRYXB = "".join(
    chr(c)
    for c in [
        70,
        105,
        108,
        116,
        79,
        110,
        84,
        105,
        109,
        101,
        68,
        117,
        114,
        105,
        110,
        103,
        79,
        84,
    ]
)
SJMCBF = "".join(
    chr(c) for c in [72, 101, 97, 116, 80, 117, 109, 112, 70, 117, 115, 101]
)
SJWMNZ = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
SKSOKP = 50
SKWIVD = 104
SOKPHU = 161
SOOQNR = "".join(chr(c) for c in [49, 49, 65])
SPBWJY = 120
SROGMD = "".join(chr(c) for c in [65, 108, 112, 115])
SSAKQX = "".join(chr(c) for c in [79, 78, 90, 69, 78])
SSBVNA = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        49,
        48,
    ]
)
SSRURA = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
SSUHBV = 122
STSEMC = "".join(
    chr(c) for c in [83, 105, 108, 101, 110, 116, 68, 117, 114, 97, 116, 105, 111, 110]
)
SUHBVW = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
SVZSSB = 151
SXUJUT = "".join(chr(c) for c in [79, 117, 116, 55])
TACCPQ = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
TATDZX = "".join(chr(c) for c in [83, 108, 97, 118, 101])
TBJEUT = 96
TDKHTZ = "".join(chr(c) for c in [87, 72, 73, 84, 69])
TDRXAI = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
TDZXNQ = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
TFMNHT = "".join(chr(c) for c in [79, 117, 116, 49, 50, 70, 117, 115, 101])
TGCRHY = "".join(chr(c) for c in [78, 79, 95, 80, 85, 77, 80])
THBSKS = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 162
TIDUBS = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
TIXQVX = "".join(chr(c) for c in [65, 109, 80, 109])
TMFZDG = 128
TOPHUG = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
TSEMCG = 158
TSIFJB = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
TTGCRH = 135
TTUVRF = "".join(chr(c) for c in [90, 111, 110, 101, 52, 84, 121, 112, 101])
TUVRFL = "".join(
    chr(c) for c in [78, 117, 109, 98, 101, 114, 79, 102, 90, 111, 110, 101, 115]
)
TYEKCW = 20
TYIYWS = "".join(chr(c) for c in [70, 50, 50, 67, 117, 114, 114, 101, 110, 116])
TZBBEK = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
UBGJFJ = 124
UBJLOI = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
UBMIKG = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 50, 84, 111, 79, 117, 116, 52]
)
UBSSUH = 53
UBYGDS = 84
UCYRAP = 139
UEUHNN = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
UGSELH = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
UGTYIY = "".join(chr(c) for c in [70, 50, 49, 67, 117, 114, 114, 101, 110, 116])
UGUCYR = 137
UHBVWV = 74
UHNNXW = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
UIKFWR = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
UJUTYE = "".join(chr(c) for c in [79, 117, 116, 56])
UMEAOE = 145
UNBLKX = "".join(chr(c) for c in [76, 73])
UNRJZT = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
UNXNKM = "".join(chr(c) for c in [70, 50, 51, 76, 105, 110, 101])
UOJRJH = "".join(chr(c) for c in [51, 65])
UQEXLS = "".join(chr(c) for c in [76, 105, 110, 101, 50])
URAZMK = "".join(
    chr(c)
    for c in [
        75,
        101,
        121,
        112,
        97,
        100,
        66,
        97,
        99,
        107,
        108,
        105,
        103,
        104,
        116,
        67,
        111,
        108,
        111,
        114,
    ]
)
URIEVB = "".join(
    chr(c) for c in [83, 65, 77, 69, 95, 65, 83, 95, 78, 79, 82, 77, 65, 76]
)
USOOQN = "".join(chr(c) for c in [49, 48, 65])
USPBWJ = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
UTOPHU = 98
UTYEKC = "".join(chr(c) for c in [79, 117, 116, 57])
UURIEV = 164
UVRFLS = 127
UXFEFJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
UYNQJY = 49
UZMRKV = "".join(chr(c) for c in [79, 82, 65, 78, 71, 69])
VDNQGV = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
VDQLAI = 77
VDSSRU = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
VEMVCY = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
VFCPOU = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 49, 84, 111, 79, 117, 116, 51]
)
VFOUUR = "".join(
    chr(c) for c in [77, 97, 112, 90, 111, 110, 101, 52, 84, 111, 79, 117, 116, 51]
)
VHDVRI = 66
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
VLASSA = "".join(chr(c) for c in [])
VNAXAD = 123
VOACMC = 6
VRFLSI = "".join(chr(c) for c in [49])
VUBYGD = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
VUNXNK = 108
VWVUBY = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
VXOIHB = 64
VYFCRT = 91
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
VZSSBV = "".join(
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
        80,
        117,
        109,
        112,
        67,
        111,
        109,
        98,
        105,
        110,
        97,
        116,
        105,
        111,
        110,
        57,
    ]
)
WAJVDQ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
WAONPY = "".join(chr(c) for c in [79, 117, 116, 49, 50])
WBSIRY = "".join(
    chr(c)
    for c in [
        67,
        112,
        79,
        102,
        102,
        84,
        105,
        109,
        101,
        68,
        117,
        114,
        105,
        110,
        103,
        79,
        84,
    ]
)
WDAFIK = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
WEEZFE = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
WIVDNQ = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
WJYKLG = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
WMNZMJ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
WONFZC = "".join(chr(c) for c in [70, 111, 114, 83, 112, 101, 101, 100, 115])
WSKWIV = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
WUEUHN = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
WVUBYG = 83
XADXLU = "".join(chr(c) for c in [90, 111, 110, 101, 49, 84, 121, 112, 101])
XBQFYL = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
XCHWDA = "".join(
    chr(c)
    for c in [
        69,
        99,
        111,
        110,
        67,
        111,
        110,
        116,
        114,
        111,
        108,
        97,
        98,
        108,
        101,
        77,
        97,
        110,
        117,
        97,
        108,
        108,
        121,
    ]
)
XEKVKZ = 3
XFEFJT = 42
XFUBJL = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
XIBHZV = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 54])
XNCUGU = "".join(
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
        78,
        117,
        109,
        98,
        101,
        114,
        79,
        102,
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
XNKMLO = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
XNQTMF = 160
XOIHBX = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 50])
XQGLRA = 26
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 52])
XSJWMN = 54
XTIACQ = "".join(
    chr(c)
    for c in [
        71,
        101,
        110,
        101,
        114,
        105,
        99,
        72,
        101,
        97,
        116,
        80,
        117,
        109,
        112,
        73,
        68,
    ]
)
XUJUTY = 18
XWAJVD = 70
XWEEZF = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
XYBQSN = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
YBQSNQ = 33
YEKCWA = "".join(chr(c) for c in [79, 117, 116, 49, 48])
YFCRTF = "".join(chr(c) for c in [79, 117, 116, 49, 48, 70, 117, 115, 101])
YGDSBD = 85
YIYWSK = 102
YKLGQP = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
YLIUXF = 25
YLJUIK = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
YMOUNB = 4
YNQJYM = "".join(
    chr(c) for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 65, 115, 67, 80]
)
YOUSPB = "".join(
    chr(c)
    for c in [87, 97, 116, 101, 114, 102, 97, 108, 108, 84, 105, 109, 101, 79, 117, 116]
)
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YRAPUM = 141
YUAXNC = "".join(chr(c) for c in [80, 53, 95, 79, 78, 76, 89])
YWONFZ = "".join(
    chr(c) for c in [83, 105, 110, 103, 108, 101, 80, 117, 109, 112, 75, 101, 121]
)
YWSKWI = 103
YXBQFY = 62
YYLIUX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZBBEKB = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZCZOLS = 113
ZDGKEA = "".join(chr(c) for c in [80, 114, 111, 103, 79, 117, 116, 70, 114, 101, 113])
ZFETDR = "".join(chr(c) for c in [73, 100, 111, 108])
ZILXWA = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
ZMJIGY = 81
ZMKQTD = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
ZOLSIP = "".join(chr(c) for c in [76, 111, 99, 107, 69, 110, 97, 98, 108, 101, 100])
ZSSBVN = 153
ZTATDZ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
ZUQEXL = "".join(chr(c) for c in [76, 105, 110, 101, 49])
ZVOACM = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
ZXNQTM = "".join(
    chr(c)
    for c in [80, 114, 111, 103, 79, 117, 116, 65, 99, 99, 101, 115, 115, 111, 114, 121]
)
AJVDQL = [INEJNI, WAJVDQ]
AMJMAO = [BIAMJM, IAMJMA]
ATDZXN = [VLASSA, ZTATDZ, TATDZX]
AXADXL = [NAXADX, TDKHTZ]
BBEKBD = [TZBBEK, ZBBEKB]
BVHDVR = []
BVWVUB = [INEJNI, HBVWVU]
BXTIAC = [LAIIDN, AIIDNI, IIDNIB, IDNIBX, DNIBXT, NIBXTI, IBXTIA]
CGETIX = [EMCGET, MCGETI]
DKHTZB = [EAKSTS, RAZMKQ, AZMKQT, ZMKQTD, MKQTDK, KQTDKH, QTDKHT, TDKHTZ]
EJNIBX = [INEJNI, NEJNIB]
EVBVHD = [
    BMJVHF,
    XPICXQ,
    ICXQIE,
    XQIEFX,
    IEFXQG,
    FXQGLR,
    KSOKPH,
    SJMCBF,
    XLSXUJ,
    SXUJUT,
    UJUTYE,
    UTYEKC,
    YEKCWA,
    KCWAON,
    WAONPY,
    ONPYYL,
    YYLIUX,
    MOUNBL,
]
EXLSXU = [MCBFEG, CBFEGZ, BFEGZU, FEGZUQ, EGZUQE, GZUQEX, ZUQEXL, UQEXLS, QEXLSX]
FJBIAM = [TSIFJB, SIFJBI, IFJBIA]
FYLJUI = [JVHFTH, QFYLJU, PIPIVL]
HBXIBH = [OIHBXI, IHBXIB]
HXEKVK = [NMHXEK, MHXEKV]
HZVOAC = [IBHZVO, BHZVOA]
IGYOUS = [MJIGYO, JIGYOU]
IKFWRK = [JUIKFW, UIKFWR]
KSTSEM = [JVHFTH, EAKSTS, VLASSA, AKSTSE]
KWIVDN = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, ZUQEXL, UQEXLS, QEXLSX]
LGQPLS = [WJYKLG, JYKLGQ, YKLGQP, KLGQPL]
MDMPSC = [IPMDMP, PMDMPS]
NBLKXS = [
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    UNBLKX,
]
NFZCZO = [JVHFTH, WONFZC, ONFZCZ, VLASSA]
NQTMFZ = [
    JVHFTH,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    PIVLAS,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    SSAKQX,
    VLASSA,
    VLASSA,
    VLASSA,
    KQXPIC,
]
NRJZTA = [PUNRJZ, UNRJZT]
PYYLIU = [
    JVHFTH,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    PIPIVL,
]
QGLRAH = [
    JVHFTH,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    IVLASS,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    SAKQXP,
]
QNRXCH = [JVHFTH, PLSPFT, BQNRXC]
QXPICX = [
    JVHFTH,
    VHFTHE,
    HFTHEC,
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
    VLASSA,
    VLASSA,
    ASSAKQ,
    VLASSA,
    VLASSA,
    VLASSA,
    SSAKQX,
    VLASSA,
    SAKQXP,
    AKQXPI,
    KQXPIC,
]
RIEVBV = [URIEVB, TDKHTZ, AZMKQT, JUZMRK, ZMKQTD, QTDKHT, UZMRKV, EAKSTS]
RSJMCB = [
    OKPHUO,
    KPHUOJ,
    PHUOJR,
    HUOJRJ,
    UOJRJH,
    OJRJHI,
    JRJHIU,
    RJHIUS,
    JHIUSO,
    HIUSOO,
    IUSOOQ,
    USOOQN,
    SOOQNR,
    OOQNRS,
    OQNRSJ,
    QNRSJM,
    NRSJMC,
]
SCTTGC = [PSCTTG]
SIJUZM = [VLASSA, VRFLSI, RFLSIJ, FLSIJU, LSIJUZ]
SNQLNM = [BQSNQL, QSNQLN]
SPFTSI = [PLSPFT, LSPFTS]
SRURAZ = [DSSRUR, SSRURA]
TTIDUB = [FFTTID, FTTIDU]
UAXNCU = [TGCRHY, GCRHYU, CRHYUA, RHYUAX, HYUAXN, YUAXNC, VLASSA, VLASSA]
VBVHDV = [UNBLKX]
VCYWON = [EMVCYW, MVCYWO, VLASSA, VLASSA]
WRKINE = [PIPIVL, QFYLJU]
XAIVEM = [
    KBDFSR,
    BDFSRO,
    DFSROG,
    FSROGM,
    SROGMD,
    ROGMDD,
    OGMDDP,
    GMDDPM,
    MDDPMX,
    DDPMXF,
    DPMXFU,
    PMXFUB,
    MXFUBJ,
    XFUBJL,
    FUBJLO,
    UBJLOI,
    BJLOIN,
    JLOINE,
    LOINEL,
    OINELW,
    INELWU,
    NELWUE,
    ELWUEU,
    LWUEUH,
    WUEUHN,
    UEUHNN,
    EUHNNX,
    UHNNXW,
    HNNXWE,
    NNXWEE,
    NXWEEZ,
    XWEEZF,
    WEEZFE,
    EEZFET,
    EZFETD,
    ZFETDR,
    FETDRX,
    ETDRXA,
    TDRXAI,
    DRXAIV,
    RXAIVE,
]
XLUBGJ = [ADXLUB, DXLUBG]
XQVXOI = [JVHFTH, TIXQVX, IXQVXO]
ZMRKVF = [MKQTDK, TDKHTZ, AZMKQT, JUZMRK, ZMKQTD, QTDKHT, UZMRKV, EAKSTS]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return VHDVRI

    @property
    def output_keys(self):
        return EVBVHD

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, QXPICX, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, QXPICX, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, QXPICX, None, None, QBMJVH
            ),
            XQIEFX: GeckoEnumStructAccessor(
                self.struct, XQIEFX, QIEFXQ, None, QXPICX, None, None, QBMJVH
            ),
            IEFXQG: GeckoEnumStructAccessor(
                self.struct, IEFXQG, EFXQGL, None, QXPICX, None, None, QBMJVH
            ),
            FXQGLR: GeckoEnumStructAccessor(
                self.struct, FXQGLR, XQGLRA, None, QGLRAH, None, None, QBMJVH
            ),
            GLRAHE: GeckoByteStructAccessor(self.struct, GLRAHE, LRAHEO, QBMJVH),
            RAHEOC: GeckoByteStructAccessor(self.struct, RAHEOC, AHEOCT, QBMJVH),
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoByteStructAccessor(self.struct, OCTHBS, CTHBSK, QBMJVH),
            THBSKS: GeckoByteStructAccessor(self.struct, THBSKS, HBSKSO, QBMJVH),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, QBMJVH),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, RSJMCB, None, None, QBMJVH
            ),
            SJMCBF: GeckoEnumStructAccessor(
                self.struct, SJMCBF, JMCBFE, None, EXLSXU, None, None, QBMJVH
            ),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, QXPICX, None, None, QBMJVH
            ),
            SXUJUT: GeckoEnumStructAccessor(
                self.struct, SXUJUT, XUJUTY, None, QXPICX, None, None, QBMJVH
            ),
            UJUTYE: GeckoEnumStructAccessor(
                self.struct, UJUTYE, JUTYEK, None, QXPICX, None, None, QBMJVH
            ),
            UTYEKC: GeckoEnumStructAccessor(
                self.struct, UTYEKC, TYEKCW, None, QXPICX, None, None, QBMJVH
            ),
            YEKCWA: GeckoEnumStructAccessor(
                self.struct, YEKCWA, EKCWAO, None, QXPICX, None, None, QBMJVH
            ),
            KCWAON: GeckoEnumStructAccessor(
                self.struct, KCWAON, CWAONP, None, QXPICX, None, None, QBMJVH
            ),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, None, QXPICX, None, None, QBMJVH
            ),
            ONPYYL: GeckoEnumStructAccessor(
                self.struct, ONPYYL, NPYYLI, None, PYYLIU, None, None, QBMJVH
            ),
            YYLIUX: GeckoEnumStructAccessor(
                self.struct, YYLIUX, YLIUXF, None, PYYLIU, None, None, QBMJVH
            ),
            LIUXFE: GeckoByteStructAccessor(self.struct, LIUXFE, IUXFEF, QBMJVH),
            UXFEFJ: GeckoByteStructAccessor(self.struct, UXFEFJ, XFEFJT, QBMJVH),
            FEFJTA: GeckoByteStructAccessor(self.struct, FEFJTA, EFJTAC, QBMJVH),
            FJTACC: GeckoByteStructAccessor(self.struct, FJTACC, JTACCP, QBMJVH),
            TACCPQ: GeckoByteStructAccessor(self.struct, TACCPQ, ACCPQI, QBMJVH),
            CCPQIP: GeckoByteStructAccessor(self.struct, CCPQIP, CPQIPO, QBMJVH),
            PQIPOU: GeckoByteStructAccessor(self.struct, PQIPOU, QIPOUY, QBMJVH),
            IPOUYN: GeckoByteStructAccessor(self.struct, IPOUYN, POUYNQ, QBMJVH),
            OUYNQJ: GeckoByteStructAccessor(self.struct, OUYNQJ, UYNQJY, QBMJVH),
            YNQJYM: GeckoBoolStructAccessor(
                self.struct, YNQJYM, NQJYMO, QJYMOU, QBMJVH
            ),
            JYMOUN: GeckoBoolStructAccessor(
                self.struct, JYMOUN, NQJYMO, YMOUNB, QBMJVH
            ),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, NBLKXS, None, None, None
            ),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, None),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoByteStructAccessor(self.struct, SJWMNZ, JWMNZM, QBMJVH),
            WMNZMJ: GeckoByteStructAccessor(self.struct, WMNZMJ, MNZMJI, QBMJVH),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, ZMJIGY, GYOUSP, IGYOUS, None, QJYMOU, QBMJVH
            ),
            YOUSPB: GeckoByteStructAccessor(self.struct, YOUSPB, OUSPBW, QBMJVH),
            USPBWJ: GeckoByteStructAccessor(self.struct, USPBWJ, SPBWJY, QBMJVH),
            PBWJYK: GeckoEnumStructAccessor(
                self.struct, PBWJYK, BWJYKL, None, LGQPLS, None, None, QBMJVH
            ),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, QPLSPF, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, FJBIAM, None, None, QBMJVH
            ),
            JBIAMJ: GeckoEnumStructAccessor(
                self.struct, JBIAMJ, ZMJIGY, QJYMOU, AMJMAO, None, QJYMOU, QBMJVH
            ),
            MJMAOA: GeckoBoolStructAccessor(
                self.struct, MJMAOA, NQJYMO, JMAOAW, QBMJVH
            ),
            MAOAWB: GeckoByteStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoByteStructAccessor(self.struct, OAWBSI, AWBSIR, QBMJVH),
            WBSIRY: GeckoByteStructAccessor(self.struct, WBSIRY, BSIRYX, QBMJVH),
            SIRYXB: GeckoByteStructAccessor(self.struct, SIRYXB, IRYXBQ, QBMJVH),
            RYXBQF: GeckoByteStructAccessor(self.struct, RYXBQF, YXBQFY, QBMJVH),
            XBQFYL: GeckoEnumStructAccessor(
                self.struct, XBQFYL, BQFYLJ, None, FYLJUI, None, None, QBMJVH
            ),
            YLJUIK: GeckoEnumStructAccessor(
                self.struct, YLJUIK, LJUIKF, None, IKFWRK, None, None, QBMJVH
            ),
            KFWRKI: GeckoEnumStructAccessor(
                self.struct, KFWRKI, FWRKIN, None, WRKINE, None, None, QBMJVH
            ),
            RKINEJ: GeckoEnumStructAccessor(
                self.struct, RKINEJ, KINEJN, None, EJNIBX, None, None, QBMJVH
            ),
            JNIBXY: GeckoByteStructAccessor(self.struct, JNIBXY, NIBXYB, QBMJVH),
            IBXYBQ: GeckoTempStructAccessor(self.struct, IBXYBQ, BXYBQS, QBMJVH),
            XYBQSN: GeckoEnumStructAccessor(
                self.struct, XYBQSN, YBQSNQ, None, SNQLNM, None, None, QBMJVH
            ),
            NQLNMH: GeckoEnumStructAccessor(
                self.struct, NQLNMH, QLNMHX, None, WRKINE, None, None, QBMJVH
            ),
            LNMHXE: GeckoEnumStructAccessor(
                self.struct, LNMHXE, ZMJIGY, XEKVKZ, HXEKVK, None, QJYMOU, QBMJVH
            ),
            EKVKZI: GeckoByteStructAccessor(self.struct, EKVKZI, KVKZIL, QBMJVH),
            VKZILX: GeckoTempStructAccessor(self.struct, VKZILX, KZILXW, QBMJVH),
            ZILXWA: GeckoTempStructAccessor(self.struct, ZILXWA, ILXWAJ, QBMJVH),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XWAJVD, None, AJVDQL, None, None, QBMJVH
            ),
            JVDQLA: GeckoByteStructAccessor(self.struct, JVDQLA, VDQLAI, QBMJVH),
            DQLAII: GeckoEnumStructAccessor(
                self.struct, DQLAII, QLAIID, None, BXTIAC, None, None, QBMJVH
            ),
            XTIACQ: GeckoByteStructAccessor(self.struct, XTIACQ, TIACQF, QBMJVH),
            IACQFF: GeckoByteStructAccessor(self.struct, IACQFF, ACQFFT, QBMJVH),
            CQFFTT: GeckoEnumStructAccessor(
                self.struct, CQFFTT, QFFTTI, None, TTIDUB, None, None, QBMJVH
            ),
            TIDUBS: GeckoByteStructAccessor(self.struct, TIDUBS, IDUBSS, QBMJVH),
            DUBSSU: GeckoByteStructAccessor(self.struct, DUBSSU, UBSSUH, QBMJVH),
            BSSUHB: GeckoByteStructAccessor(self.struct, BSSUHB, SSUHBV, QBMJVH),
            SUHBVW: GeckoEnumStructAccessor(
                self.struct, SUHBVW, UHBVWV, None, BVWVUB, None, None, QBMJVH
            ),
            VWVUBY: GeckoEnumStructAccessor(
                self.struct, VWVUBY, WVUBYG, None, EXLSXU, None, None, QBMJVH
            ),
            VUBYGD: GeckoEnumStructAccessor(
                self.struct, VUBYGD, UBYGDS, None, EXLSXU, None, None, QBMJVH
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, YGDSBD, None, EXLSXU, None, None, QBMJVH
            ),
            GDSBDJ: GeckoEnumStructAccessor(
                self.struct, GDSBDJ, DSBDJQ, None, EXLSXU, None, None, QBMJVH
            ),
            SBDJQR: GeckoEnumStructAccessor(
                self.struct, SBDJQR, BDJQRJ, None, EXLSXU, None, None, QBMJVH
            ),
            DJQRJJ: GeckoEnumStructAccessor(
                self.struct, DJQRJJ, JQRJJJ, None, EXLSXU, None, None, QBMJVH
            ),
            QRJJJV: GeckoEnumStructAccessor(
                self.struct, QRJJJV, RJJJVY, None, EXLSXU, None, None, QBMJVH
            ),
            JJJVYF: GeckoEnumStructAccessor(
                self.struct, JJJVYF, JJVYFC, None, EXLSXU, None, None, QBMJVH
            ),
            JVYFCR: GeckoEnumStructAccessor(
                self.struct, JVYFCR, VYFCRT, None, EXLSXU, None, None, QBMJVH
            ),
            YFCRTF: GeckoEnumStructAccessor(
                self.struct, YFCRTF, FCRTFM, None, EXLSXU, None, None, QBMJVH
            ),
            CRTFMN: GeckoEnumStructAccessor(
                self.struct, CRTFMN, RTFMNH, None, EXLSXU, None, None, QBMJVH
            ),
            TFMNHT: GeckoEnumStructAccessor(
                self.struct, TFMNHT, FMNHTB, None, EXLSXU, None, None, QBMJVH
            ),
            MNHTBJ: GeckoEnumStructAccessor(
                self.struct, MNHTBJ, NHTBJE, None, EXLSXU, None, None, QBMJVH
            ),
            HTBJEU: GeckoEnumStructAccessor(
                self.struct, HTBJEU, TBJEUT, None, EXLSXU, None, None, QBMJVH
            ),
            BJEUTO: GeckoEnumStructAccessor(
                self.struct, BJEUTO, JEUTOP, None, EXLSXU, None, None, QBMJVH
            ),
            EUTOPH: GeckoByteStructAccessor(self.struct, EUTOPH, UTOPHU, QBMJVH),
            TOPHUG: GeckoByteStructAccessor(self.struct, TOPHUG, OPHUGT, QBMJVH),
            PHUGTY: GeckoByteStructAccessor(self.struct, PHUGTY, HUGTYI, QBMJVH),
            UGTYIY: GeckoByteStructAccessor(self.struct, UGTYIY, GTYIYW, QBMJVH),
            TYIYWS: GeckoByteStructAccessor(self.struct, TYIYWS, YIYWSK, QBMJVH),
            IYWSKW: GeckoByteStructAccessor(self.struct, IYWSKW, YWSKWI, QBMJVH),
            WSKWIV: GeckoEnumStructAccessor(
                self.struct, WSKWIV, SKWIVD, None, KWIVDN, None, None, QBMJVH
            ),
            WIVDNQ: GeckoEnumStructAccessor(
                self.struct, WIVDNQ, IVDNQG, None, KWIVDN, None, None, QBMJVH
            ),
            VDNQGV: GeckoEnumStructAccessor(
                self.struct, VDNQGV, DNQGVU, None, KWIVDN, None, None, QBMJVH
            ),
            NQGVUN: GeckoEnumStructAccessor(
                self.struct, NQGVUN, QGVUNX, None, KWIVDN, None, None, QBMJVH
            ),
            GVUNXN: GeckoEnumStructAccessor(
                self.struct, GVUNXN, VUNXNK, None, KWIVDN, None, None, QBMJVH
            ),
            UNXNKM: GeckoEnumStructAccessor(
                self.struct, UNXNKM, NXNKML, None, KWIVDN, None, None, QBMJVH
            ),
            XNKMLO: GeckoByteStructAccessor(self.struct, XNKMLO, NKMLOI, QBMJVH),
            KMLOIJ: GeckoTimeStructAccessor(self.struct, KMLOIJ, MLOIJU, QBMJVH),
            LOIJUG: GeckoTimeStructAccessor(self.struct, LOIJUG, OIJUGS, QBMJVH),
            IJUGSE: GeckoTimeStructAccessor(self.struct, IJUGSE, JUGSEL, QBMJVH),
            UGSELH: GeckoTimeStructAccessor(self.struct, UGSELH, GSELHB, QBMJVH),
            SELHBQ: GeckoTimeStructAccessor(self.struct, SELHBQ, ELHBQN, QBMJVH),
            LHBQNR: GeckoEnumStructAccessor(
                self.struct, LHBQNR, HBQNRX, None, QNRXCH, None, None, QBMJVH
            ),
            NRXCHW: GeckoBoolStructAccessor(
                self.struct, NRXCHW, RXCHWD, GYOUSP, QBMJVH
            ),
            XCHWDA: GeckoBoolStructAccessor(
                self.struct, XCHWDA, CHWDAF, QJYMOU, QBMJVH
            ),
            HWDAFI: GeckoBoolStructAccessor(
                self.struct, HWDAFI, CHWDAF, GYOUSP, QBMJVH
            ),
            WDAFIK: GeckoBoolStructAccessor(
                self.struct, WDAFIK, CHWDAF, JMAOAW, QBMJVH
            ),
            DAFIKJ: GeckoBoolStructAccessor(
                self.struct, DAFIKJ, CHWDAF, XEKVKZ, QBMJVH
            ),
            AFIKJP: GeckoBoolStructAccessor(
                self.struct, AFIKJP, CHWDAF, YMOUNB, QBMJVH
            ),
            FIKJPU: GeckoBoolStructAccessor(
                self.struct, FIKJPU, CHWDAF, IKJPUN, QBMJVH
            ),
            KJPUNR: GeckoEnumStructAccessor(
                self.struct, KJPUNR, JPUNRJ, None, NRJZTA, None, None, QBMJVH
            ),
            RJZTAT: GeckoEnumStructAccessor(
                self.struct, RJZTAT, JZTATD, None, ATDZXN, None, None, QBMJVH
            ),
            TDZXNQ: GeckoByteStructAccessor(self.struct, TDZXNQ, DZXNQT, QBMJVH),
            ZXNQTM: GeckoEnumStructAccessor(
                self.struct, ZXNQTM, XNQTMF, None, NQTMFZ, None, None, QBMJVH
            ),
            QTMFZD: GeckoTimeStructAccessor(self.struct, QTMFZD, TMFZDG, QBMJVH),
            MFZDGK: GeckoTimeStructAccessor(self.struct, MFZDGK, FZDGKE, QBMJVH),
            ZDGKEA: GeckoByteStructAccessor(self.struct, ZDGKEA, DGKEAK, QBMJVH),
            GKEAKS: GeckoEnumStructAccessor(
                self.struct, GKEAKS, KEAKST, None, KSTSEM, None, None, QBMJVH
            ),
            STSEMC: GeckoTimeStructAccessor(self.struct, STSEMC, TSEMCG, QBMJVH),
            SEMCGE: GeckoEnumStructAccessor(
                self.struct, SEMCGE, NQJYMO, XEKVKZ, CGETIX, None, QJYMOU, QBMJVH
            ),
            GETIXQ: GeckoEnumStructAccessor(
                self.struct, GETIXQ, ETIXQV, None, XQVXOI, None, None, QBMJVH
            ),
            QVXOIH: GeckoWordStructAccessor(self.struct, QVXOIH, VXOIHB, QBMJVH),
            XOIHBX: GeckoEnumStructAccessor(
                self.struct, XOIHBX, ZMJIGY, JMAOAW, HBXIBH, None, QJYMOU, QBMJVH
            ),
            BXIBHZ: GeckoBoolStructAccessor(
                self.struct, BXIBHZ, ZMJIGY, YMOUNB, QBMJVH
            ),
            XIBHZV: GeckoEnumStructAccessor(
                self.struct, XIBHZV, ZMJIGY, IKJPUN, HZVOAC, None, QJYMOU, QBMJVH
            ),
            ZVOACM: GeckoBoolStructAccessor(
                self.struct, ZVOACM, ZMJIGY, VOACMC, QBMJVH
            ),
            OACMCV: GeckoBoolStructAccessor(
                self.struct, OACMCV, ZMJIGY, ACMCVD, QBMJVH
            ),
            CMCVDS: GeckoBoolStructAccessor(
                self.struct, CMCVDS, MCVDSS, GYOUSP, QBMJVH
            ),
            CVDSSR: GeckoBoolStructAccessor(
                self.struct, CVDSSR, MCVDSS, JMAOAW, QBMJVH
            ),
            VDSSRU: GeckoEnumStructAccessor(
                self.struct, VDSSRU, MCVDSS, QJYMOU, SRURAZ, None, QJYMOU, QBMJVH
            ),
            RURAZM: GeckoEnumStructAccessor(
                self.struct, RURAZM, MCVDSS, XEKVKZ, SRURAZ, None, QJYMOU, QBMJVH
            ),
            URAZMK: GeckoEnumStructAccessor(
                self.struct, URAZMK, MCVDSS, YMOUNB, DKHTZB, None, KHTZBB, QBMJVH
            ),
            HTZBBE: GeckoEnumStructAccessor(
                self.struct, HTZBBE, MCVDSS, ACMCVD, BBEKBD, None, QJYMOU, QBMJVH
            ),
            AIVEMV: GeckoBoolStructAccessor(
                self.struct, AIVEMV, IVEMVC, JMAOAW, QBMJVH
            ),
            VEMVCY: GeckoEnumStructAccessor(
                self.struct, VEMVCY, IVEMVC, QJYMOU, VCYWON, None, YMOUNB, QBMJVH
            ),
            CYWONF: GeckoBoolStructAccessor(
                self.struct, CYWONF, IVEMVC, YMOUNB, QBMJVH
            ),
            YWONFZ: GeckoEnumStructAccessor(
                self.struct, YWONFZ, IVEMVC, VOACMC, NFZCZO, None, YMOUNB, QBMJVH
            ),
            FZCZOL: GeckoByteStructAccessor(self.struct, FZCZOL, ZCZOLS, QBMJVH),
            CZOLSI: GeckoBoolStructAccessor(
                self.struct, CZOLSI, NQJYMO, GYOUSP, QBMJVH
            ),
            ZOLSIP: GeckoByteStructAccessor(self.struct, ZOLSIP, OLSIPM, QBMJVH),
            LSIPMD: GeckoEnumStructAccessor(
                self.struct, LSIPMD, SIPMDM, None, MDMPSC, None, None, QBMJVH
            ),
            DMPSCT: GeckoEnumStructAccessor(
                self.struct, DMPSCT, MPSCTT, None, SCTTGC, None, None, QBMJVH
            ),
            CTTGCR: GeckoEnumStructAccessor(
                self.struct, CTTGCR, TTGCRH, GYOUSP, UAXNCU, None, KHTZBB, QBMJVH
            ),
            AXNCUG: GeckoBoolStructAccessor(
                self.struct, AXNCUG, TTGCRH, ACMCVD, QBMJVH
            ),
            XNCUGU: GeckoByteStructAccessor(self.struct, XNCUGU, NCUGUC, QBMJVH),
            CUGUCY: GeckoWordStructAccessor(self.struct, CUGUCY, UGUCYR, QBMJVH),
            GUCYRA: GeckoWordStructAccessor(self.struct, GUCYRA, UCYRAP, QBMJVH),
            CYRAPU: GeckoWordStructAccessor(self.struct, CYRAPU, YRAPUM, QBMJVH),
            RAPUME: GeckoWordStructAccessor(self.struct, RAPUME, APUMEA, QBMJVH),
            PUMEAO: GeckoWordStructAccessor(self.struct, PUMEAO, UMEAOE, QBMJVH),
            MEAOES: GeckoWordStructAccessor(self.struct, MEAOES, EAOESV, QBMJVH),
            AOESVZ: GeckoWordStructAccessor(self.struct, AOESVZ, OESVZS, QBMJVH),
            ESVZSS: GeckoWordStructAccessor(self.struct, ESVZSS, SVZSSB, QBMJVH),
            VZSSBV: GeckoWordStructAccessor(self.struct, VZSSBV, ZSSBVN, QBMJVH),
            SSBVNA: GeckoWordStructAccessor(self.struct, SSBVNA, SBVNAX, QBMJVH),
            BVNAXA: GeckoEnumStructAccessor(
                self.struct, BVNAXA, VNAXAD, GYOUSP, AXADXL, None, QJYMOU, None
            ),
            XADXLU: GeckoEnumStructAccessor(
                self.struct, XADXLU, VNAXAD, JMAOAW, XLUBGJ, None, QJYMOU, None
            ),
            LUBGJF: GeckoEnumStructAccessor(
                self.struct, LUBGJF, UBGJFJ, GYOUSP, AXADXL, None, QJYMOU, None
            ),
            BGJFJN: GeckoEnumStructAccessor(
                self.struct, BGJFJN, UBGJFJ, JMAOAW, XLUBGJ, None, QJYMOU, None
            ),
            GJFJNT: GeckoEnumStructAccessor(
                self.struct, GJFJNT, JFJNTT, GYOUSP, AXADXL, None, QJYMOU, None
            ),
            FJNTTU: GeckoEnumStructAccessor(
                self.struct, FJNTTU, JFJNTT, JMAOAW, XLUBGJ, None, QJYMOU, None
            ),
            JNTTUV: GeckoEnumStructAccessor(
                self.struct, JNTTUV, NTTUVR, GYOUSP, AXADXL, None, QJYMOU, None
            ),
            TTUVRF: GeckoEnumStructAccessor(
                self.struct, TTUVRF, NTTUVR, JMAOAW, XLUBGJ, None, QJYMOU, None
            ),
            TUVRFL: GeckoEnumStructAccessor(
                self.struct, TUVRFL, UVRFLS, GYOUSP, SIJUZM, None, KHTZBB, None
            ),
            IJUZMR: GeckoEnumStructAccessor(
                self.struct, IJUZMR, UVRFLS, XEKVKZ, ZMRKVF, None, KHTZBB, QBMJVH
            ),
            MRKVFC: GeckoBoolStructAccessor(self.struct, MRKVFC, UVRFLS, ACMCVD, None),
            RKVFCP: GeckoBoolStructAccessor(self.struct, RKVFCP, VNAXAD, YMOUNB, None),
            KVFCPO: GeckoBoolStructAccessor(self.struct, KVFCPO, VNAXAD, IKJPUN, None),
            VFCPOU: GeckoBoolStructAccessor(self.struct, VFCPOU, VNAXAD, VOACMC, None),
            FCPOUB: GeckoBoolStructAccessor(self.struct, FCPOUB, VNAXAD, ACMCVD, None),
            CPOUBM: GeckoBoolStructAccessor(self.struct, CPOUBM, UBGJFJ, YMOUNB, None),
            POUBMI: GeckoBoolStructAccessor(self.struct, POUBMI, UBGJFJ, IKJPUN, None),
            OUBMIK: GeckoBoolStructAccessor(self.struct, OUBMIK, UBGJFJ, VOACMC, None),
            UBMIKG: GeckoBoolStructAccessor(self.struct, UBMIKG, UBGJFJ, ACMCVD, None),
            BMIKGN: GeckoBoolStructAccessor(self.struct, BMIKGN, JFJNTT, YMOUNB, None),
            MIKGNV: GeckoBoolStructAccessor(self.struct, MIKGNV, JFJNTT, IKJPUN, None),
            IKGNVF: GeckoBoolStructAccessor(self.struct, IKGNVF, JFJNTT, VOACMC, None),
            KGNVFO: GeckoBoolStructAccessor(self.struct, KGNVFO, JFJNTT, ACMCVD, None),
            GNVFOU: GeckoBoolStructAccessor(self.struct, GNVFOU, NTTUVR, YMOUNB, None),
            NVFOUU: GeckoBoolStructAccessor(self.struct, NVFOUU, NTTUVR, IKJPUN, None),
            VFOUUR: GeckoBoolStructAccessor(self.struct, VFOUUR, NTTUVR, VOACMC, None),
            FOUURI: GeckoBoolStructAccessor(self.struct, FOUURI, NTTUVR, ACMCVD, None),
            OUURIE: GeckoEnumStructAccessor(
                self.struct, OUURIE, UURIEV, YMOUNB, RIEVBV, None, KHTZBB, QBMJVH
            ),
            IEVBVH: GeckoBoolStructAccessor(self.struct, IEVBVH, UURIEV, ACMCVD, None),
        }

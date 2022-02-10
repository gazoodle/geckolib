#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v58'
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
ACCPQI = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
ACQFFT = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AJVDQL = "".join(chr(c) for c in [71, 82, 69, 69, 78])
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 51])
AMJMAO = 10
AONPYY = "".join(
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
AWBSIR = 82
BDJQRJ = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
BFEGZU = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
BIAMJM = 8
BJEUTO = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
BLKXSJ = 31
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
BSIRYX = 72
BSKSOK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BSSUHB = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
BVWVUB = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
BXTIAC = 7
BXYBQS = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
BYGDSB = "".join(chr(c) for c in [77, 65, 65, 88])
CBFEGZ = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
CCPQIP = 29
CQBMJV = 0
CQFFTT = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
CRTFMN = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
CTHBSK = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
CXQIEF = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
DJQRJJ = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
DNIBXT = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
DQLAII = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
DSBDJQ = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
DUBSSU = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = 28
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
EJNIBX = "".join(chr(c) for c in [50, 52, 104])
EKCWAO = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
EKVKZI = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EUTOPH = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
EXLSXU = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
FCRTFM = "".join(chr(c) for c in [65, 115, 112, 101, 110])
FEFJTA = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
FFTTID = "".join(chr(c) for c in [65, 108, 112, 115])
FJBIAM = 23
FJTACC = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 4
FTTIDU = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
GDSBDJ = "".join(chr(c) for c in [80, 68, 67])
GLRAHE = 38
GQPLSP = 74
GYOUSP = "".join(
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
GZUQEX = 27
HBVWVU = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 56
HTBJEU = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
HUGTYI = 58
HUOJRJ = 80
HXEKVK = "".join(
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
IACQFF = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
IAMJMA = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
IBXYBQ = 64
ICXQIE = 16
IDNIBX = "".join(
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
IDUBSS = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
IGYOUS = 77
IIDNIB = 8
IKFWRK = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
ILXWAJ = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
INEJNI = 34
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
IRYXBQ = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
IUSOOQ = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
IUXFEF = 78
IVLASS = "".join(chr(c) for c in [72, 84, 82])
JBIAMJ = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
JHIUSO = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
JIGYOU = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
JJJVYF = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
JJVYFC = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
JMAOAW = 71
JMCBFE = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
JQRJJJ = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
JRJHIU = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
JTACCP = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
JUIKFW = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
JUTYEK = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
JVDQLA = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
JWMNZM = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
JYKLGQ = 52
JYMOUN = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
KCWAON = 58
KFWRKI = "".join(chr(c) for c in [83, 108, 97, 118, 101])
KINEJN = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
KLGQPL = 53
KQXPIC = 14
KSOKPH = "".join(chr(c) for c in [79, 117, 116, 76, 105])
KVKZIL = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
KXSJWM = 35
KZILXW = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
LAIIDN = "".join(chr(c) for c in [87, 72, 73, 84, 69])
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
LIUXFE = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
LKXSJW = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
LNMHXE = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
LSXUJU = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
LXWAJV = "".join(
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
MAOAWB = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
MCBFEG = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
MHXEKV = 5
MJMAOA = "".join(
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
MJVHFT = 12
MNHTBJ = "".join(
    chr(c)
    for c in [
        81,
        117,
        105,
        99,
        107,
        79,
        102,
        102,
        75,
        101,
        121,
        69,
        110,
        97,
        98,
        108,
        101,
    ]
)
MNZMJI = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
MOUNBL = "".join(chr(c) for c in [70])
NBLKXS = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
NEJNIB = "".join(chr(c) for c in [65, 109, 80, 109])
NHTBJE = 45
NIBXTI = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
NIBXYB = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
NPYYLI = "".join(
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
NQJYMO = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
NQLNMH = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
NRSJMC = 2
NZMJIG = 70
OAWBSI = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
OCTHBS = 42
OJRJHI = 54
OKPHUO = "".join(chr(c) for c in [76, 73])
ONPYYL = 60
OOQNRS = "".join(chr(c) for c in [79, 119, 110])
OUNBLK = "".join(chr(c) for c in [67])
OUSPBW = "".join(chr(c) for c in [85, 76, 95, 67, 69])
PBWJYK = "".join(chr(c) for c in [67, 69])
PFTSIF = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
PHUOJR = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 53])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
POUYNQ = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
PQIPOU = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
PYYLIU = 61
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QFFTTI = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
QFYLJU = 76
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = 30
QJYMOU = 1
QLAIID = "".join(chr(c) for c in [67, 89, 65, 78])
QLNMHX = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
QNRSJM = 0
QPLSPF = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
QRJJJV = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
QSNQLN = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
QXPICX = "".join(chr(c) for c in [79, 117, 116, 52])
RAHEOC = 39
RJHIUS = 55
RJJJVY = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
RKINEJ = 75
RSJMCB = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
RTFMNH = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
RYXBQF = 1
SAKQXP = 13
SBDJQR = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
SIFJBI = 6
SIRYXB = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
SJMCBF = 32
SJWMNZ = 66
SKSOKP = 41
SNQLNM = 4
SOKPHU = 79
SOOQNR = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
SPBWJY = "".join(chr(c) for c in [85, 76])
SPFTSI = 3
SSAKQX = "".join(chr(c) for c in [79, 117, 116, 50])
SSUHBV = "".join(chr(c) for c in [67, 111, 97, 115, 116])
SUHBVW = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
SXUJUT = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
TBJEUT = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
TFMNHT = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 44
TIDUBS = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
TSIFJB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
TTIDUB = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
TYEKCW = "".join(chr(c) for c in [72, 105])
UBSSUH = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
UBYGDS = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
UHBVWV = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
UIKFWR = 73
UOJRJH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UQEXLS = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
USOOQN = 81
USPBWJ = 51
UTOPHU = 46
UTYEKC = "".join(chr(c) for c in [76, 111])
UXFEFJ = "".join(chr(c) for c in [80, 49])
UYNQJY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
VDQLAI = "".join(chr(c) for c in [66, 76, 85, 69])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
VLASSA = "".join(chr(c) for c in [])
VUBYGD = "".join(chr(c) for c in [76, 65])
VWVUBY = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
VYFCRT = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [82, 69, 68])
WAONPY = 59
WBSIRY = "".join(
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
WJYKLG = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
WMNZMJ = 68
WRKINE = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
WVUBYG = "".join(chr(c) for c in [74, 97, 122, 122, 105])
XBQFYL = 3
XEKVKZ = 43
XLSXUJ = 57
XPICXQ = 15
XQGLRA = 37
XQIEFX = 18
XSJWMN = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
XTIACQ = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
XUJUTY = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
XWAJVD = "".join(chr(c) for c in [79, 70, 70])
XYBQSN = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
YBQSNQ = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
YFCRTF = "".join(chr(c) for c in [73, 100, 111, 108])
YGDSBD = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
YKLGQP = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
YLIUXF = 62
YLJUIK = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
YMOUNB = 33
YNQJYM = 63
YOUSPB = 26
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(
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
YYLIUX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = "".join(chr(c) for c in [78, 105, 103, 104, 116])
ZUQEXL = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
AIIDNI = [XWAJVD, WAJVDQ, AJVDQL, JVDQLA, VDQLAI, DQLAII, QLAIID, LAIIDN]
AOAWBS = [JVHFTH, ZUQEXL, MAOAWB]
ASSAKQ = [
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
    VLASSA,
    VLASSA,
    VLASSA,
    LASSAK,
]
BQSNQL = [XYBQSN, YBQSNQ]
BWJYKL = [SPBWJY, PBWJYK]
CPQIPO = [PIPIVL, UXFEFJ]
FEGZUQ = [JMCBFE, MCBFEG, CBFEGZ, BFEGZU]
FMNHTB = [
    IACQFF,
    ACQFFT,
    CQFFTT,
    QFFTTI,
    FFTTID,
    FTTIDU,
    TTIDUB,
    TIDUBS,
    IDUBSS,
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
    UBYGDS,
    BYGDSB,
    YGDSBD,
    GDSBDJ,
    DSBDJQ,
    SBDJQR,
    BDJQRJ,
    DJQRJJ,
    JQRJJJ,
    QRJJJV,
    RJJJVY,
    JJJVYF,
    JJVYFC,
    JVYFCR,
    VYFCRT,
    YFCRTF,
    FCRTFM,
    CRTFMN,
    RTFMNH,
    TFMNHT,
]
FWRKIN = [VLASSA, IKFWRK, KFWRKI]
HBSKSO = [
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
IBXTIA = [DNIBXT, NIBXTI]
JEUTOP = [TBJEUT, BJEUTO, VLASSA, VLASSA]
JNIBXY = [JVHFTH, NEJNIB, EJNIBX]
KPHUOJ = [
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
    OKPHUO,
]
LJUIKF = [FYLJUI, YLJUIK]
MJIGYO = [IPOUYN, ZMJIGY]
NMHXEK = [QLNMHX, LNMHXE]
OPHUGT = [OKPHUO]
OQNRSJ = [SOOQNR, OOQNRS]
OUYNQJ = [IPOUYN, POUYNQ]
PHUGTY = []
PLSPFT = [IPOUYN, QPLSPF]
QEXLSX = [ZUQEXL, UQEXLS]
QIEFXQ = [
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
]
TACCPQ = [FJTACC, JTACCP]
TOPHUG = [BMJVHF, SSAKQX, AKQXPI, QXPICX, PICXQI, CXQIEF, CTHBSK, KSOKPH]
UJUTYE = [LSXUJU, SXUJUT, XUJUTY]
UNBLKX = [MOUNBL, OUNBLK]
XFEFJT = [JVHFTH, UXFEFJ, PIPIVL]
YEKCWA = [UTYEKC, TYEKCW]
ZILXWA = [VKZILX, KZILXW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return HUGTYI

    @property
    def output_keys(self):
        return TOPHUG

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, ASSAKQ, None, None, QBMJVH
            ),
            SSAKQX: GeckoEnumStructAccessor(
                self.struct, SSAKQX, SAKQXP, None, ASSAKQ, None, None, QBMJVH
            ),
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, None, ASSAKQ, None, None, QBMJVH
            ),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, None, ASSAKQ, None, None, QBMJVH
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, ASSAKQ, None, None, QBMJVH
            ),
            CXQIEF: GeckoEnumStructAccessor(
                self.struct, CXQIEF, XQIEFX, None, QIEFXQ, None, None, QBMJVH
            ),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, THBSKS, None, HBSKSO, None, None, QBMJVH
            ),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, QBMJVH),
            KSOKPH: GeckoEnumStructAccessor(
                self.struct, KSOKPH, SOKPHU, None, KPHUOJ, None, None, None
            ),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, None),
            UOJRJH: GeckoByteStructAccessor(self.struct, UOJRJH, OJRJHI, QBMJVH),
            JRJHIU: GeckoByteStructAccessor(self.struct, JRJHIU, RJHIUS, QBMJVH),
            JHIUSO: GeckoByteStructAccessor(self.struct, JHIUSO, HIUSOO, QBMJVH),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, QNRSJM, OQNRSJ, None, NRSJMC, QBMJVH
            ),
            RSJMCB: GeckoEnumStructAccessor(
                self.struct, RSJMCB, SJMCBF, None, FEGZUQ, None, None, QBMJVH
            ),
            EGZUQE: GeckoEnumStructAccessor(
                self.struct, EGZUQE, GZUQEX, None, QEXLSX, None, None, QBMJVH
            ),
            EXLSXU: GeckoEnumStructAccessor(
                self.struct, EXLSXU, XLSXUJ, None, UJUTYE, None, None, QBMJVH
            ),
            JUTYEK: GeckoEnumStructAccessor(
                self.struct, JUTYEK, USOOQN, NRSJMC, YEKCWA, None, NRSJMC, QBMJVH
            ),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoByteStructAccessor(self.struct, NPYYLI, PYYLIU, QBMJVH),
            YYLIUX: GeckoByteStructAccessor(self.struct, YYLIUX, YLIUXF, QBMJVH),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, XFEFJT, None, None, QBMJVH
            ),
            FEFJTA: GeckoEnumStructAccessor(
                self.struct, FEFJTA, EFJTAC, None, TACCPQ, None, None, QBMJVH
            ),
            ACCPQI: GeckoEnumStructAccessor(
                self.struct, ACCPQI, CCPQIP, None, CPQIPO, None, None, QBMJVH
            ),
            PQIPOU: GeckoEnumStructAccessor(
                self.struct, PQIPOU, QIPOUY, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoByteStructAccessor(self.struct, UYNQJY, YNQJYM, QBMJVH),
            NQJYMO: GeckoTempStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoEnumStructAccessor(
                self.struct, JYMOUN, YMOUNB, None, UNBLKX, None, None, QBMJVH
            ),
            NBLKXS: GeckoEnumStructAccessor(
                self.struct, NBLKXS, BLKXSJ, None, CPQIPO, None, None, QBMJVH
            ),
            LKXSJW: GeckoByteStructAccessor(self.struct, LKXSJW, KXSJWM, QBMJVH),
            XSJWMN: GeckoTempStructAccessor(self.struct, XSJWMN, SJWMNZ, QBMJVH),
            JWMNZM: GeckoTempStructAccessor(self.struct, JWMNZM, WMNZMJ, QBMJVH),
            MNZMJI: GeckoEnumStructAccessor(
                self.struct, MNZMJI, NZMJIG, None, MJIGYO, None, None, QBMJVH
            ),
            JIGYOU: GeckoByteStructAccessor(self.struct, JIGYOU, IGYOUS, QBMJVH),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoEnumStructAccessor(
                self.struct, OUSPBW, USPBWJ, None, BWJYKL, None, None, QBMJVH
            ),
            WJYKLG: GeckoByteStructAccessor(self.struct, WJYKLG, JYKLGQ, QBMJVH),
            YKLGQP: GeckoByteStructAccessor(self.struct, YKLGQP, KLGQPL, QBMJVH),
            LGQPLS: GeckoEnumStructAccessor(
                self.struct, LGQPLS, GQPLSP, None, PLSPFT, None, None, QBMJVH
            ),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, QBMJVH),
            PFTSIF: GeckoTimeStructAccessor(self.struct, PFTSIF, FTSIFJ, QBMJVH),
            TSIFJB: GeckoTimeStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoTimeStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoTimeStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoTimeStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoEnumStructAccessor(
                self.struct, MJMAOA, JMAOAW, None, AOAWBS, None, None, QBMJVH
            ),
            OAWBSI: GeckoBoolStructAccessor(
                self.struct, OAWBSI, AWBSIR, QNRSJM, QBMJVH
            ),
            WBSIRY: GeckoBoolStructAccessor(
                self.struct, WBSIRY, BSIRYX, NRSJMC, QBMJVH
            ),
            SIRYXB: GeckoBoolStructAccessor(
                self.struct, SIRYXB, BSIRYX, QNRSJM, QBMJVH
            ),
            IRYXBQ: GeckoBoolStructAccessor(
                self.struct, IRYXBQ, BSIRYX, RYXBQF, QBMJVH
            ),
            YXBQFY: GeckoBoolStructAccessor(
                self.struct, YXBQFY, BSIRYX, XBQFYL, QBMJVH
            ),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, LJUIKF, None, None, QBMJVH
            ),
            JUIKFW: GeckoEnumStructAccessor(
                self.struct, JUIKFW, UIKFWR, None, FWRKIN, None, None, QBMJVH
            ),
            WRKINE: GeckoByteStructAccessor(self.struct, WRKINE, RKINEJ, QBMJVH),
            KINEJN: GeckoEnumStructAccessor(
                self.struct, KINEJN, INEJNI, None, JNIBXY, None, None, QBMJVH
            ),
            NIBXYB: GeckoWordStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, USOOQN, RYXBQF, BQSNQL, None, NRSJMC, QBMJVH
            ),
            QSNQLN: GeckoBoolStructAccessor(
                self.struct, QSNQLN, USOOQN, SNQLNM, QBMJVH
            ),
            NQLNMH: GeckoEnumStructAccessor(
                self.struct, NQLNMH, USOOQN, MHXEKV, NMHXEK, None, NRSJMC, QBMJVH
            ),
            HXEKVK: GeckoBoolStructAccessor(
                self.struct, HXEKVK, XEKVKZ, QNRSJM, QBMJVH
            ),
            EKVKZI: GeckoBoolStructAccessor(
                self.struct, EKVKZI, XEKVKZ, RYXBQF, QBMJVH
            ),
            KVKZIL: GeckoEnumStructAccessor(
                self.struct, KVKZIL, XEKVKZ, NRSJMC, ZILXWA, None, NRSJMC, QBMJVH
            ),
            ILXWAJ: GeckoEnumStructAccessor(
                self.struct, ILXWAJ, XEKVKZ, XBQFYL, ZILXWA, None, NRSJMC, QBMJVH
            ),
            LXWAJV: GeckoEnumStructAccessor(
                self.struct, LXWAJV, XEKVKZ, SNQLNM, AIIDNI, None, IIDNIB, QBMJVH
            ),
            IDNIBX: GeckoEnumStructAccessor(
                self.struct, IDNIBX, XEKVKZ, BXTIAC, IBXTIA, None, NRSJMC, QBMJVH
            ),
            MNHTBJ: GeckoBoolStructAccessor(
                self.struct, MNHTBJ, NHTBJE, QNRSJM, QBMJVH
            ),
            HTBJEU: GeckoEnumStructAccessor(
                self.struct, HTBJEU, NHTBJE, NRSJMC, JEUTOP, None, SNQLNM, QBMJVH
            ),
            EUTOPH: GeckoByteStructAccessor(self.struct, EUTOPH, UTOPHU, QBMJVH),
        }

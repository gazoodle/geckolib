#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InYJ v58'
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
ACCPQI = 30
AIIDNI = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
AJVDQL = 73
AKQXPI = "".join(chr(c) for c in [79, 117, 116, 50])
AMJMAO = "".join(chr(c) for c in [70, 51])
AOAWBS = "".join(chr(c) for c in [79, 117, 116, 50, 70, 117, 115, 101])
AONPYY = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
ASSAKQ = "".join(chr(c) for c in [80, 114, 111, 116, 101, 99, 116, 105, 111, 110])
AWBSIR = "".join(chr(c) for c in [79, 117, 116, 51, 70, 117, 115, 101])
BDJQRJ = "".join(chr(c) for c in [66, 76, 85, 69])
BFEGZU = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
BIAMJM = "".join(chr(c) for c in [70, 49])
BJEUTO = "".join(chr(c) for c in [66, 97, 114, 101, 102, 111, 111, 116])
BLKXSJ = "".join(
    chr(c) for c in [78, 111, 116, 73, 110, 115, 116, 97, 108, 108, 101, 100]
)
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [70, 50, 67, 117, 114, 114, 101, 110, 116])
BQNRXC = 46
BQSNQL = 10
BSIRYX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 49, 70, 117, 115, 101])
BSKSOK = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
BSSUHB = "".join(
    chr(c) for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 111, 112]
)
BVWVUB = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 67, 104, 97, 110, 103, 101]
)
BWJYKL = 77
BXTIAC = 64
BXYBQS = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
BYGDSB = "".join(
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
CBFEGZ = 27
CCPQIP = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
CPQIPO = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
CQBMJV = 0
CQFFTT = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
CRTFMN = 44
CTHBSK = 79
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = "".join(
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
DJQRJJ = "".join(chr(c) for c in [77, 65, 71, 69, 78, 84, 65])
DNIBXT = "".join(chr(c) for c in [50, 52, 104])
DNQGVU = "".join(chr(c) for c in [83, 117, 110, 114, 105, 115, 101])
DSBDJQ = "".join(chr(c) for c in [71, 82, 69, 69, 78])
DUBSSU = "".join(
    chr(c)
    for c in [72, 101, 97, 116, 101, 114, 83, 111, 102, 116, 83, 116, 97, 114, 116]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFJTAC = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
EFXQGL = 37
EJNIBX = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
EKCWAO = "".join(
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
EKVKZI = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
ELHBQN = "".join(chr(c) for c in [83, 72, 79, 87, 95, 65, 76, 76, 95, 77, 83, 71])
EOCTHB = 39
EUTOPH = "".join(chr(c) for c in [66, 101, 108, 108, 97, 103, 105, 111])
EXLSXU = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
FCRTFM = "".join(chr(c) for c in [67, 117, 115, 116, 111, 109, 101, 114, 73, 68])
FEGZUQ = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
FFTTID = "".join(
    chr(c)
    for c in [66, 108, 111, 119, 101, 114, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
FJBIAM = "".join(chr(c) for c in [79, 117, 116, 49, 70, 117, 115, 101])
FJTACC = 29
FMNHTB = "".join(
    chr(c) for c in [69, 110, 100, 108, 101, 115, 115, 80, 111, 111, 108, 115]
)
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
FTTIDU = "".join(chr(c) for c in [70, 114, 101, 101, 80, 117, 109, 112, 75, 101, 121])
FWRKIN = "".join(chr(c) for c in [70, 51, 76, 105, 110, 101])
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [70, 51, 67, 117, 114, 114, 101, 110, 116])
GDSBDJ = "".join(chr(c) for c in [82, 69, 68])
GLRAHE = 40
GQPLSP = "".join(chr(c) for c in [67, 69])
GSELHB = "".join(
    chr(c) for c in [73, 110, 102, 111, 77, 115, 103, 67, 111, 110, 102, 105, 103]
)
GTYIYW = "".join(chr(c) for c in [72, 111, 116, 115, 112, 114, 105, 110, 103])
GVUNXN = "".join(chr(c) for c in [86, 105, 107, 105, 110, 103])
GYOUSP = 68
GZUQEX = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
HBQNRX = "".join(
    chr(c) for c in [75, 101, 121, 112, 97, 100, 79, 112, 116, 105, 111, 110, 115, 52]
)
HBVWVU = "".join(
    chr(c)
    for c in [67, 117, 115, 116, 111, 109, 75, 101, 121, 69, 110, 97, 98, 108, 101, 100]
)
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HIUSOO = 0
HTBJEU = "".join(chr(c) for c in [65, 114, 116, 101, 115, 105, 97, 110])
HUGTYI = "".join(chr(c) for c in [68, 121, 110, 97, 115, 116, 121])
HUOJRJ = 56
HWDAFI = 58
HXEKVK = 72
IACQFF = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
IAMJMA = "".join(chr(c) for c in [70, 50])
IBXTIA = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
IBXYBQ = 23
ICXQIE = 16
IDNIBX = "".join(chr(c) for c in [65, 109, 80, 109])
IDUBSS = 5
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
IGYOUS = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IIDNIB = 34
IKFWRK = "".join(chr(c) for c in [70, 50, 76, 105, 110, 101])
ILXWAJ = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
INEJNI = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 63
IRYXBQ = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114, 70, 117, 115, 101])
IUSOOQ = 2
IUXFEF = 28
IVDNQG = "".join(chr(c) for c in [83, 116, 114, 111, 110, 103])
IVLASS = "".join(chr(c) for c in [72, 84, 82])
IYWSKW = "".join(chr(c) for c in [76, 65])
JBIAMJ = 83
JEUTOP = "".join(chr(c) for c in [66, 101, 97, 99, 104, 99, 111, 109, 98, 101, 114])
JIGYOU = 66
JJJVYF = 8
JJVYFC = "".join(
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
JMAOAW = "".join(chr(c) for c in [76, 105, 110, 101, 50])
JNIBXY = 6
JQRJJJ = "".join(chr(c) for c in [67, 89, 65, 78])
JRJHIU = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
JUGSEL = "".join(
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
JUIKFW = 104
JUTYEK = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
JVDQLA = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
JVHFTH = "".join(chr(c) for c in [78, 65])
JVYFCR = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101])
JWMNZM = "".join(chr(c) for c in [73, 110, 116, 111, 84, 117, 98])
JYKLGQ = 26
KCWAON = 60
KFWRKI = 105
KINEJN = 3
KLGQPL = 51
KMLOIJ = "".join(chr(c) for c in [65, 115, 112, 101, 110])
KPHUOJ = 55
KQXPIC = 13
KSOKPH = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
KVKZIL = 1
KWIVDN = "".join(chr(c) for c in [80, 68, 67])
KZILXW = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
LAIIDN = 75
LASSAK = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
LGQPLS = "".join(chr(c) for c in [85, 76])
LIUXFE = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
LJUIKF = "".join(chr(c) for c in [70, 49, 76, 105, 110, 101])
LKXSJW = "".join(
    chr(c) for c in [80, 114, 101, 115, 115, 117, 114, 101, 83, 119, 105, 116, 99, 104]
)
LNMHXE = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
LOIJUG = "".join(chr(c) for c in [84, 105, 116, 97, 110, 95, 83, 112, 97, 115])
LRAHEO = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
LSPFTS = 52
LSXUJU = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
LXWAJV = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
MCBFEG = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
MHXEKV = "".join(
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
MJIGYO = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
MJMAOA = "".join(chr(c) for c in [76, 105, 110, 101, 49])
MJVHFT = 12
MLOIJU = "".join(chr(c) for c in [84, 104, 101, 114, 109, 111, 83, 112, 97, 115])
MNHTBJ = "".join(chr(c) for c in [87, 101, 108, 108, 105, 115])
MNZMJI = 3
MOUNBL = 31
NBLKXS = "".join(chr(c) for c in [105, 110, 70, 108, 111])
NEJNIB = 4
NHTBJE = "".join(chr(c) for c in [65, 108, 112, 115])
NIBXYB = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114, 50])
NKMLOI = "".join(chr(c) for c in [73, 100, 111, 108])
NMHXEK = 82
NPYYLI = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
NQGVUN = "".join(
    chr(c) for c in [83, 117, 112, 101, 114, 105, 111, 114, 83, 112, 97, 115]
)
NQJYMO = "".join(chr(c) for c in [70])
NQLNMH = "".join(
    chr(c) for c in [79, 85, 84, 83, 73, 68, 69, 95, 70, 73, 76, 84, 69, 82]
)
NRSJMC = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
NRXCHW = 47
NXNKML = "".join(chr(c) for c in [67, 108, 101, 97, 114, 119, 97, 116, 101, 114])
NZMJIG = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
OAWBSI = 84
OCTHBS = "".join(chr(c) for c in [79, 117, 116, 76, 105])
OIJUGS = "".join(chr(c) for c in [73, 98, 101, 114, 83, 112, 97])
OJRJHI = 81
OKPHUO = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
ONPYYL = 62
OOQNRS = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
OPHUGT = "".join(chr(c) for c in [67, 111, 97, 115, 116])
OQNRSJ = 32
OUNBLK = "".join(
    chr(c) for c in [70, 108, 111, 119, 68, 101, 116, 101, 99, 116, 111, 114]
)
OUSPBW = 70
OUYNQJ = 1
PBWJYK = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
PFTSIF = 53
PHUGTY = "".join(
    chr(c) for c in [68, 105, 109, 101, 110, 115, 105, 111, 110, 95, 111, 110, 101]
)
PHUOJR = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
PICXQI = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
POUYNQ = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
PYYLIU = 78
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
QFFTTI = 4
QFYLJU = 99
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
QGVUNX = "".join(
    chr(c) for c in [83, 112, 97, 95, 73, 110, 100, 117, 115, 116, 114, 105, 101, 115]
)
QIEFXQ = 36
QIPOUY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
QJYMOU = "".join(chr(c) for c in [67])
QLAIID = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
QNRSJM = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
QNRXCH = "".join(
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
QRJJJV = "".join(chr(c) for c in [87, 72, 73, 84, 69])
QSNQLN = "".join(
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
QXPICX = "".join(chr(c) for c in [79, 117, 116, 51])
RAHEOC = 15
RJHIUS = "".join(chr(c) for c in [79, 119, 110])
RKINEJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
RSJMCB = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
RTFMNH = "".join(chr(c) for c in [71, 101, 110, 101, 114, 105, 99])
RYXBQF = 87
SBDJQR = "".join(chr(c) for c in [89, 69, 76, 76, 79, 87])
SELHBQ = "".join(
    chr(c) for c in [72, 73, 68, 69, 95, 68, 69, 84, 65, 73, 76, 69, 68, 95, 77, 83, 71]
)
SIFJBI = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
SIRYXB = 86
SJMCBF = "".join(
    chr(c) for c in [70, 105, 108, 116, 80, 49, 68, 117, 114, 79, 110, 108, 121]
)
SJWMNZ = "".join(chr(c) for c in [73, 110, 116, 111, 80, 105, 112, 105, 110, 103])
SKSOKP = 80
SKWIVD = "".join(chr(c) for c in [77, 97, 114, 113, 117, 105, 115])
SNQLNM = 71
SOKPHU = 54
SOOQNR = 48
SPFTSI = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
SSAKQX = "".join(chr(c) for c in [65, 85, 88])
SSUHBV = 7
SUHBVW = "".join(
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
SXUJUT = "".join(chr(c) for c in [76, 111])
TACCPQ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
TBJEUT = "".join(chr(c) for c in [65, 114, 99, 116, 105, 99])
TFMNHT = "".join(chr(c) for c in [72, 121, 100, 114, 111, 112, 111, 111, 108])
THBSKS = "".join(chr(c) for c in [76, 73])
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
TOPHUG = "".join(chr(c) for c in [66, 117, 108, 108, 102, 114, 111, 103])
TSIFJB = 74
TTIDUB = "".join(chr(c) for c in [76, 97, 115, 116, 80, 117, 109, 112, 75, 101, 121])
TYEKCW = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
TYIYWS = "".join(chr(c) for c in [74, 97, 99, 117, 122, 122, 105])
UBSSUH = 6
UBYGDS = "".join(
    chr(c) for c in [66, 114, 101, 97, 107, 101, 114, 67, 104, 97, 110, 103, 101]
)
UGSELH = 45
UGTYIY = "".join(chr(c) for c in [70, 111, 117, 114, 95, 87, 105, 110, 100])
UHBVWV = 43
UNBLKX = 25
UNXNKM = "".join(chr(c) for c in [79, 107, 101, 97, 110, 111, 115])
UOJRJH = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
UQEXLS = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
USOOQN = "".join(chr(c) for c in [65, 117, 120, 84, 105, 109, 101, 79, 117, 116])
USPBWJ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
UTOPHU = "".join(
    chr(c)
    for c in [76, 101, 105, 115, 117, 114, 101, 95, 80, 114, 111, 100, 95, 73, 110, 100]
)
UTYEKC = 58
UXFEFJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
UYNQJY = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
VDNQGV = "".join(chr(c) for c in [83, 117, 110, 114, 97, 110, 115])
VDQLAI = "".join(chr(c) for c in [83, 108, 97, 118, 101])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(
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
VLASSA = "".join(chr(c) for c in [])
VUNXNK = "".join(
    chr(c) for c in [87, 87, 79, 95, 87, 104, 105, 114, 108, 99, 97, 114, 101]
)
VWVUBY = "".join(
    chr(c) for c in [78, 79, 95, 82, 69, 83, 84, 82, 73, 67, 84, 73, 79, 78]
)
VYFCRT = "".join(chr(c) for c in [69, 110, 97, 98, 108, 101])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
WAONPY = 61
WBSIRY = 85
WIVDNQ = "".join(
    chr(c)
    for c in [80, 114, 101, 109, 105, 117, 109, 95, 76, 101, 105, 115, 117, 114, 101]
)
WJYKLG = "".join(
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
WRKINE = 106
WSKWIV = "".join(chr(c) for c in [77, 65, 65, 88])
WVUBYG = "".join(
    chr(c)
    for c in [80, 65, 83, 83, 87, 79, 82, 68, 95, 80, 82, 79, 84, 69, 67, 84, 69, 68]
)
XBQFYL = 98
XEKVKZ = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
XFEFJT = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
XNKMLO = "".join(chr(c) for c in [68, 101, 108, 117, 120, 101])
XPICXQ = 14
XQGLRA = 38
XQIEFX = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
XSJWMN = "".join(
    chr(c) for c in [80, 114, 111, 98, 101, 76, 111, 99, 97, 116, 105, 111, 110]
)
XTIACQ = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
XUJUTY = "".join(chr(c) for c in [72, 105])
XYBQSN = 8
YBQSNQ = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
YEKCWA = 59
YGDSBD = "".join(chr(c) for c in [79, 70, 70])
YIYWSK = "".join(chr(c) for c in [74, 97, 122, 122, 105])
YKLGQP = "".join(chr(c) for c in [85, 76, 95, 67, 69])
YLJUIK = 100
YMOUNB = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
YNQJYM = 33
YOUSPB = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YWSKWI = "".join(chr(c) for c in [80, 114, 111, 95, 70, 108, 111, 97, 116])
YXBQFY = "".join(chr(c) for c in [70, 49, 67, 117, 114, 114, 101, 110, 116])
YYLIUX = "".join(chr(c) for c in [80, 49])
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 76
ZMJIGY = 35
ZUQEXL = 57
ACQFFT = [TIACQF, IACQFF]
AHEOCT = [
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
CHWDAF = []
CXQIEF = [
    JVHFTH,
    VHFTHE,
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
DQLAII = [VLASSA, JVDQLA, VDQLAI]
EGZUQE = [BFEGZU, FEGZUQ]
FEFJTA = [UXFEFJ, XFEFJT]
HBSKSO = [
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
    THBSKS,
]
IFJBIA = [CCPQIP, SIFJBI]
IJUGSE = [
    RTFMNH,
    TFMNHT,
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
    PHUGTY,
    HUGTYI,
    UGTYIY,
    GTYIYW,
    TYIYWS,
    YIYWSK,
    IYWSKW,
    YWSKWI,
    WSKWIV,
    SKWIVD,
    KWIVDN,
    WIVDNQ,
    IVDNQG,
    VDNQGV,
    DNQGVU,
    NQGVUN,
    QGVUNX,
    GVUNXN,
    VUNXNK,
    UNXNKM,
    NXNKML,
    XNKMLO,
    NKMLOI,
    KMLOIJ,
    MLOIJU,
    LOIJUG,
    OIJUGS,
]
JHIUSO = [JRJHIU, RJHIUS]
JMCBFE = [QNRSJM, NRSJMC, RSJMCB, SJMCBF]
JTACCP = [PIPIVL, YYLIUX]
JYMOUN = [NQJYMO, QJYMOU]
KXSJWM = [NBLKXS, BLKXSJ, LKXSJW]
LHBQNR = [SELHBQ, ELHBQN, VLASSA, VLASSA]
MAOAWB = [BIAMJM, IAMJMA, AMJMAO, VLASSA, VLASSA, VLASSA, MJMAOA, JMAOAW]
NIBXTI = [JVHFTH, IDNIBX, DNIBXT]
PQIPOU = [CCPQIP, CPQIPO]
QLNMHX = [JVHFTH, BFEGZU, NQLNMH]
QPLSPF = [LGQPLS, GQPLSP]
RJJJVY = [YGDSBD, GDSBDJ, DSBDJQ, SBDJQR, BDJQRJ, DJQRJJ, JQRJJJ, QRJJJV]
RXCHWD = [BMJVHF, AKQXPI, QXPICX, PICXQI, LRAHEO, OCTHBS]
SAKQXP = [
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
    VLASSA,
    VLASSA,
    VLASSA,
    VLASSA,
    ASSAKQ,
    VLASSA,
    VLASSA,
    SSAKQX,
]
SPBWJY = [CCPQIP, USPBWJ]
TIDUBS = [FTTIDU, TTIDUB]
UIKFWR = [VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, VLASSA, MJMAOA, JMAOAW]
UJUTYE = [SXUJUT, XUJUTY]
VUBYGD = [VWVUBY, WVUBYG]
WMNZMJ = [SJWMNZ, JWMNZM]
XCHWDA = [THBSKS]
XLSXUJ = [UQEXLS, QEXLSX, EXLSXU]
XWAJVD = [ILXWAJ, LXWAJV]
YFCRTF = [JVYFCR, VYFCRT]
YLIUXF = [JVHFTH, YYLIUX, PIPIVL]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return HWDAFI

    @property
    def output_keys(self):
        return RXCHWD

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, SAKQXP, None, None, QBMJVH
            ),
            AKQXPI: GeckoEnumStructAccessor(
                self.struct, AKQXPI, KQXPIC, None, SAKQXP, None, None, QBMJVH
            ),
            QXPICX: GeckoEnumStructAccessor(
                self.struct, QXPICX, XPICXQ, None, SAKQXP, None, None, QBMJVH
            ),
            PICXQI: GeckoEnumStructAccessor(
                self.struct, PICXQI, ICXQIE, None, CXQIEF, None, None, QBMJVH
            ),
            XQIEFX: GeckoByteStructAccessor(self.struct, XQIEFX, QIEFXQ, QBMJVH),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoEnumStructAccessor(
                self.struct, LRAHEO, RAHEOC, None, AHEOCT, None, None, QBMJVH
            ),
            HEOCTH: GeckoByteStructAccessor(self.struct, HEOCTH, EOCTHB, QBMJVH),
            OCTHBS: GeckoEnumStructAccessor(
                self.struct, OCTHBS, CTHBSK, None, HBSKSO, None, None, None
            ),
            BSKSOK: GeckoByteStructAccessor(self.struct, BSKSOK, SKSOKP, None),
            KSOKPH: GeckoByteStructAccessor(self.struct, KSOKPH, SOKPHU, QBMJVH),
            OKPHUO: GeckoByteStructAccessor(self.struct, OKPHUO, KPHUOJ, QBMJVH),
            PHUOJR: GeckoByteStructAccessor(self.struct, PHUOJR, HUOJRJ, QBMJVH),
            UOJRJH: GeckoEnumStructAccessor(
                self.struct, UOJRJH, OJRJHI, HIUSOO, JHIUSO, None, IUSOOQ, QBMJVH
            ),
            USOOQN: GeckoByteStructAccessor(self.struct, USOOQN, SOOQNR, QBMJVH),
            OOQNRS: GeckoEnumStructAccessor(
                self.struct, OOQNRS, OQNRSJ, None, JMCBFE, None, None, QBMJVH
            ),
            MCBFEG: GeckoEnumStructAccessor(
                self.struct, MCBFEG, CBFEGZ, None, EGZUQE, None, None, QBMJVH
            ),
            GZUQEX: GeckoEnumStructAccessor(
                self.struct, GZUQEX, ZUQEXL, None, XLSXUJ, None, None, QBMJVH
            ),
            LSXUJU: GeckoEnumStructAccessor(
                self.struct, LSXUJU, OJRJHI, IUSOOQ, UJUTYE, None, IUSOOQ, QBMJVH
            ),
            JUTYEK: GeckoByteStructAccessor(self.struct, JUTYEK, UTYEKC, QBMJVH),
            TYEKCW: GeckoByteStructAccessor(self.struct, TYEKCW, YEKCWA, QBMJVH),
            EKCWAO: GeckoByteStructAccessor(self.struct, EKCWAO, KCWAON, QBMJVH),
            CWAONP: GeckoByteStructAccessor(self.struct, CWAONP, WAONPY, QBMJVH),
            AONPYY: GeckoByteStructAccessor(self.struct, AONPYY, ONPYYL, QBMJVH),
            NPYYLI: GeckoEnumStructAccessor(
                self.struct, NPYYLI, PYYLIU, None, YLIUXF, None, None, QBMJVH
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, FEFJTA, None, None, QBMJVH
            ),
            EFJTAC: GeckoEnumStructAccessor(
                self.struct, EFJTAC, FJTACC, None, JTACCP, None, None, QBMJVH
            ),
            TACCPQ: GeckoEnumStructAccessor(
                self.struct, TACCPQ, ACCPQI, None, PQIPOU, None, None, QBMJVH
            ),
            QIPOUY: GeckoByteStructAccessor(self.struct, QIPOUY, IPOUYN, QBMJVH),
            POUYNQ: GeckoTempStructAccessor(self.struct, POUYNQ, OUYNQJ, QBMJVH),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, YNQJYM, None, JYMOUN, None, None, QBMJVH
            ),
            YMOUNB: GeckoEnumStructAccessor(
                self.struct, YMOUNB, MOUNBL, None, JTACCP, None, None, QBMJVH
            ),
            OUNBLK: GeckoEnumStructAccessor(
                self.struct, OUNBLK, UNBLKX, None, KXSJWM, None, None, QBMJVH
            ),
            XSJWMN: GeckoEnumStructAccessor(
                self.struct, XSJWMN, OJRJHI, MNZMJI, WMNZMJ, None, IUSOOQ, QBMJVH
            ),
            NZMJIG: GeckoByteStructAccessor(self.struct, NZMJIG, ZMJIGY, QBMJVH),
            MJIGYO: GeckoTempStructAccessor(self.struct, MJIGYO, JIGYOU, QBMJVH),
            IGYOUS: GeckoTempStructAccessor(self.struct, IGYOUS, GYOUSP, QBMJVH),
            YOUSPB: GeckoEnumStructAccessor(
                self.struct, YOUSPB, OUSPBW, None, SPBWJY, None, None, QBMJVH
            ),
            PBWJYK: GeckoByteStructAccessor(self.struct, PBWJYK, BWJYKL, QBMJVH),
            WJYKLG: GeckoByteStructAccessor(self.struct, WJYKLG, JYKLGQ, QBMJVH),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, QPLSPF, None, None, QBMJVH
            ),
            PLSPFT: GeckoByteStructAccessor(self.struct, PLSPFT, LSPFTS, QBMJVH),
            SPFTSI: GeckoByteStructAccessor(self.struct, SPFTSI, PFTSIF, QBMJVH),
            FTSIFJ: GeckoEnumStructAccessor(
                self.struct, FTSIFJ, TSIFJB, None, IFJBIA, None, None, QBMJVH
            ),
            FJBIAM: GeckoEnumStructAccessor(
                self.struct, FJBIAM, JBIAMJ, None, MAOAWB, None, None, QBMJVH
            ),
            AOAWBS: GeckoEnumStructAccessor(
                self.struct, AOAWBS, OAWBSI, None, MAOAWB, None, None, QBMJVH
            ),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, MAOAWB, None, None, QBMJVH
            ),
            BSIRYX: GeckoEnumStructAccessor(
                self.struct, BSIRYX, SIRYXB, None, MAOAWB, None, None, QBMJVH
            ),
            IRYXBQ: GeckoEnumStructAccessor(
                self.struct, IRYXBQ, RYXBQF, None, MAOAWB, None, None, QBMJVH
            ),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoByteStructAccessor(self.struct, BQFYLJ, QFYLJU, QBMJVH),
            FYLJUI: GeckoByteStructAccessor(self.struct, FYLJUI, YLJUIK, QBMJVH),
            LJUIKF: GeckoEnumStructAccessor(
                self.struct, LJUIKF, JUIKFW, None, UIKFWR, None, None, QBMJVH
            ),
            IKFWRK: GeckoEnumStructAccessor(
                self.struct, IKFWRK, KFWRKI, None, UIKFWR, None, None, QBMJVH
            ),
            FWRKIN: GeckoEnumStructAccessor(
                self.struct, FWRKIN, WRKINE, None, UIKFWR, None, None, QBMJVH
            ),
            RKINEJ: GeckoByteStructAccessor(self.struct, RKINEJ, KINEJN, QBMJVH),
            INEJNI: GeckoTimeStructAccessor(self.struct, INEJNI, NEJNIB, QBMJVH),
            EJNIBX: GeckoTimeStructAccessor(self.struct, EJNIBX, JNIBXY, QBMJVH),
            NIBXYB: GeckoTimeStructAccessor(self.struct, NIBXYB, IBXYBQ, QBMJVH),
            BXYBQS: GeckoTimeStructAccessor(self.struct, BXYBQS, XYBQSN, QBMJVH),
            YBQSNQ: GeckoTimeStructAccessor(self.struct, YBQSNQ, BQSNQL, QBMJVH),
            QSNQLN: GeckoEnumStructAccessor(
                self.struct, QSNQLN, SNQLNM, None, QLNMHX, None, None, QBMJVH
            ),
            LNMHXE: GeckoBoolStructAccessor(
                self.struct, LNMHXE, NMHXEK, HIUSOO, QBMJVH
            ),
            MHXEKV: GeckoBoolStructAccessor(
                self.struct, MHXEKV, HXEKVK, IUSOOQ, QBMJVH
            ),
            XEKVKZ: GeckoBoolStructAccessor(
                self.struct, XEKVKZ, HXEKVK, HIUSOO, QBMJVH
            ),
            EKVKZI: GeckoBoolStructAccessor(
                self.struct, EKVKZI, HXEKVK, KVKZIL, QBMJVH
            ),
            VKZILX: GeckoBoolStructAccessor(
                self.struct, VKZILX, HXEKVK, MNZMJI, QBMJVH
            ),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, ZILXWA, None, XWAJVD, None, None, QBMJVH
            ),
            WAJVDQ: GeckoEnumStructAccessor(
                self.struct, WAJVDQ, AJVDQL, None, DQLAII, None, None, QBMJVH
            ),
            QLAIID: GeckoByteStructAccessor(self.struct, QLAIID, LAIIDN, QBMJVH),
            AIIDNI: GeckoEnumStructAccessor(
                self.struct, AIIDNI, IIDNIB, None, NIBXTI, None, None, QBMJVH
            ),
            IBXTIA: GeckoWordStructAccessor(self.struct, IBXTIA, BXTIAC, QBMJVH),
            XTIACQ: GeckoEnumStructAccessor(
                self.struct, XTIACQ, OJRJHI, KVKZIL, ACQFFT, None, IUSOOQ, QBMJVH
            ),
            CQFFTT: GeckoBoolStructAccessor(
                self.struct, CQFFTT, OJRJHI, QFFTTI, QBMJVH
            ),
            FFTTID: GeckoEnumStructAccessor(
                self.struct, FFTTID, OJRJHI, IDUBSS, TIDUBS, None, IUSOOQ, QBMJVH
            ),
            DUBSSU: GeckoBoolStructAccessor(
                self.struct, DUBSSU, OJRJHI, UBSSUH, QBMJVH
            ),
            BSSUHB: GeckoBoolStructAccessor(
                self.struct, BSSUHB, OJRJHI, SSUHBV, QBMJVH
            ),
            SUHBVW: GeckoBoolStructAccessor(
                self.struct, SUHBVW, UHBVWV, HIUSOO, QBMJVH
            ),
            HBVWVU: GeckoBoolStructAccessor(
                self.struct, HBVWVU, UHBVWV, KVKZIL, QBMJVH
            ),
            BVWVUB: GeckoEnumStructAccessor(
                self.struct, BVWVUB, UHBVWV, IUSOOQ, VUBYGD, None, IUSOOQ, QBMJVH
            ),
            UBYGDS: GeckoEnumStructAccessor(
                self.struct, UBYGDS, UHBVWV, MNZMJI, VUBYGD, None, IUSOOQ, QBMJVH
            ),
            BYGDSB: GeckoEnumStructAccessor(
                self.struct, BYGDSB, UHBVWV, QFFTTI, RJJJVY, None, JJJVYF, QBMJVH
            ),
            JJVYFC: GeckoEnumStructAccessor(
                self.struct, JJVYFC, UHBVWV, SSUHBV, YFCRTF, None, IUSOOQ, QBMJVH
            ),
            JUGSEL: GeckoBoolStructAccessor(
                self.struct, JUGSEL, UGSELH, HIUSOO, QBMJVH
            ),
            GSELHB: GeckoEnumStructAccessor(
                self.struct, GSELHB, UGSELH, IUSOOQ, LHBQNR, None, QFFTTI, QBMJVH
            ),
            HBQNRX: GeckoByteStructAccessor(self.struct, HBQNRX, BQNRXC, QBMJVH),
            QNRXCH: GeckoBoolStructAccessor(
                self.struct, QNRXCH, NRXCHW, HIUSOO, QBMJVH
            ),
        }

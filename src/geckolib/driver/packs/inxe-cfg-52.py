#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v52'
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
ACCPQI = "".join(chr(c) for c in [65, 76, 87, 65, 89, 83, 95, 79, 78])
AHEOCT = "".join(chr(c) for c in [79, 117, 116, 53, 67, 117, 114])
AIIDNI = "".join(chr(c) for c in [66, 111, 116, 104, 83, 112, 101, 101, 100, 115])
AJVDQL = "".join(chr(c) for c in [65, 109, 80, 109])
AKQXPI = 14
AMJMAO = 70
AOAWBS = 77
AONPYY = 81
ASSAKQ = "".join(chr(c) for c in [79, 117, 116, 50])
AWBSIR = 51
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
BIAMJM = 68
BLKXSJ = "".join(
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
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
BQSNQL = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
BSIRYX = "".join(chr(c) for c in [67, 69])
BSKSOK = 18
BWJYKL = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
BXYBQS = 82
CBFEGZ = 45
CPQIPO = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 54])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 56
CXQIEF = 26
DNIBXT = "".join(
    chr(c) for c in [83, 101, 108, 102, 67, 108, 101, 97, 110, 77, 115, 103]
)
DQLAII = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EJNIBX = 71
EKCWAO = 55
EKVKZI = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = 49
FEFJTA = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FEGZUQ = 46
FJBIAM = 66
FJTACC = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 31
FWRKIN = 6
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
GLRAHE = 38
GQPLSP = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
GYOUSP = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
GZUQEX = 47
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 55])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 49, 49])
HXEKVK = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
IAMJMA = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
IBXYBQ = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
IIDNIB = "".join(
    chr(c) for c in [72, 105, 103, 104, 83, 112, 101, 101, 100, 79, 110, 108, 121]
)
IKFWRK = 4
ILXWAJ = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
INEJNI = 10
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
IRYXBQ = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
IUXFEF = 32
IVLASS = "".join(chr(c) for c in [])
JBIAMJ = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
JHIUSO = 24
JIGYOU = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
JMCBFE = 44
JNIBXY = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
JRJHIU = 23
JTACCP = 27
JUIKFW = 3
JUTYEK = 80
JVDQLA = "".join(chr(c) for c in [50, 52, 104])
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = 78
JYKLGQ = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
JYMOUN = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
KCWAON = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
KFWRKI = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
KINEJN = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
KLGQPL = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 49, 48])
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 52])
KSOKPH = 19
KVKZIL = 73
KXSJWM = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
KZILXW = "".join(chr(c) for c in [83, 108, 97, 118, 101])
LAIIDN = "".join(
    chr(c)
    for c in [80, 117, 109, 112, 49, 85, 115, 101, 114, 65, 99, 99, 101, 115, 115]
)
LGQPLS = 1
LIUXFE = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
LJUIKF = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
LKXSJW = 61
LNMHXE = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(chr(c) for c in [67])
LSXUJU = 79
LXWAJV = 75
MAOAWB = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
MHXEKV = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
MJIGYO = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
MJMAOA = "".join(chr(c) for c in [78, 105, 103, 104, 116])
MJVHFT = 12
MOUNBL = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
NBLKXS = 60
NEJNIB = "".join(
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
NIBXTI = 4
NMHXEK = 76
NPYYLI = "".join(chr(c) for c in [79, 119, 110])
NQJYMO = "".join(chr(c) for c in [72, 105])
NQLNMH = "".join(
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
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
NZMJIG = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
OAWBSI = "".join(chr(c) for c in [85, 76, 95, 67, 69])
OCTHBS = 50
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 50])
OKPHUO = 20
ONPYYL = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OOQNRS = 41
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
OUNBLK = 59
PBWJYK = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
PFTSIF = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
PHUOJR = 21
PICXQI = 16
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = "".join(chr(c) for c in [70])
POUYNQ = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
PQIPOU = 57
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QFYLJU = 74
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
QLAIID = 64
QLNMHX = 3
QNRSJM = 42
QPLSPF = 33
QSNQLN = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
QXPICX = 15
RAHEOC = 39
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RKINEJ = 8
RSJMCB = 43
RYXBQF = 52
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 51])
SIFJBI = 35
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
SJWMNZ = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 56])
SNQLNM = 1
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 57])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
SPBWJY = 30
SSAKQX = 13
SXUJUT = "".join(chr(c) for c in [76, 73])
TACCPQ = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TIACQF = 52
TSIFJB = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
TYEKCW = 54
UIKFWR = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
UJUTYE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UNBLKX = "".join(
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
UOJRJH = 22
UQEXLS = 48
USOOQN = 25
USPBWJ = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
UTYEKC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UXFEFJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
UYNQJY = "".join(chr(c) for c in [80, 117, 114, 103, 101, 83, 112, 101, 101, 100])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = 34
WAONPY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
WBSIRY = "".join(chr(c) for c in [85, 76])
WMNZMJ = "".join(chr(c) for c in [80, 49])
WRKINE = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
XBQFYL = 53
XFEFJT = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 53])
XQGLRA = 37
XQIEFX = "".join(chr(c) for c in [72, 84, 82])
XSJWMN = 62
XWAJVD = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
XYBQSN = "".join(
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
YBQSNQ = 72
YEKCWA = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
YKLGQP = 63
YLIUXF = 2
YMOUNB = 58
YNQJYM = "".join(chr(c) for c in [76, 111])
YOUSPB = 29
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
YYLIUX = 0
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZMJIGY = 28
ZUQEXL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BXTIAC = [SXUJUT]
CCPQIP = [TACCPQ, ACCPQI]
EFJTAC = [UXFEFJ, XFEFJT, FEFJTA]
HIUSOO = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    PIPIVL,
]
IBXTIA = [
    BMJVHF,
    ASSAKQ,
    SAKQXP,
    KQXPIC,
    XPICXQ,
    ICXQIE,
    CTHBSK,
    HBSKSO,
    SKSOKP,
    SOKPHU,
    KPHUOJ,
    HUOJRJ,
    OJRJHI,
    RJHIUS,
    IUSOOQ,
    XLSXUJ,
]
IDNIBX = [AIIDNI, IIDNIB]
IGYOUS = [MJIGYO, JIGYOU]
JMAOAW = [PBWJYK, MJMAOA]
LASSAK = [
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
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    VLASSA,
]
MNZMJI = [JVHFTH, WMNZMJ, PIPIVL]
NIBXYB = [JVHFTH, JNIBXY]
OUSPBW = [PIPIVL, WMNZMJ]
OUYNQJ = [QIPOUY, IPOUYN, POUYNQ]
PYYLIU = [ONPYYL, NPYYLI]
QIEFXQ = [
    JVHFTH,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    XQIEFX,
]
QJYMOU = [YNQJYM, NQJYMO]
SIRYXB = [WBSIRY, BSIRYX]
SPFTSI = [PLSPFT, LSPFTS]
VDQLAI = [JVHFTH, AJVDQL, JVDQLA]
WJYKLG = [PBWJYK, BWJYKL]
XEKVKZ = [MHXEKV, HXEKVK]
XTIACQ = []
XUJUTY = [
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    IVLASS,
    SXUJUT,
]
YLJUIK = [PBWJYK, FYLJUI]
ZILXWA = [IVLASS, VKZILX, KZILXW]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return TIACQF

    @property
    def output_keys(self):
        return IBXTIA

    @property
    def accessors(self):
        return {
            ZCQBMJ: GeckoByteStructAccessor(self.struct, ZCQBMJ, CQBMJV, QBMJVH),
            BMJVHF: GeckoEnumStructAccessor(
                self.struct, BMJVHF, MJVHFT, None, LASSAK, None, None, QBMJVH
            ),
            ASSAKQ: GeckoEnumStructAccessor(
                self.struct, ASSAKQ, SSAKQX, None, LASSAK, None, None, QBMJVH
            ),
            SAKQXP: GeckoEnumStructAccessor(
                self.struct, SAKQXP, AKQXPI, None, LASSAK, None, None, QBMJVH
            ),
            KQXPIC: GeckoEnumStructAccessor(
                self.struct, KQXPIC, QXPICX, None, LASSAK, None, None, QBMJVH
            ),
            XPICXQ: GeckoEnumStructAccessor(
                self.struct, XPICXQ, PICXQI, None, LASSAK, None, None, QBMJVH
            ),
            ICXQIE: GeckoEnumStructAccessor(
                self.struct, ICXQIE, CXQIEF, None, QIEFXQ, None, None, QBMJVH
            ),
            IEFXQG: GeckoByteStructAccessor(self.struct, IEFXQG, EFXQGL, QBMJVH),
            FXQGLR: GeckoByteStructAccessor(self.struct, FXQGLR, XQGLRA, QBMJVH),
            QGLRAH: GeckoByteStructAccessor(self.struct, QGLRAH, GLRAHE, QBMJVH),
            LRAHEO: GeckoByteStructAccessor(self.struct, LRAHEO, RAHEOC, QBMJVH),
            AHEOCT: GeckoByteStructAccessor(self.struct, AHEOCT, HEOCTH, QBMJVH),
            EOCTHB: GeckoByteStructAccessor(self.struct, EOCTHB, OCTHBS, QBMJVH),
            CTHBSK: GeckoEnumStructAccessor(
                self.struct, CTHBSK, THBSKS, None, LASSAK, None, None, QBMJVH
            ),
            HBSKSO: GeckoEnumStructAccessor(
                self.struct, HBSKSO, BSKSOK, None, LASSAK, None, None, QBMJVH
            ),
            SKSOKP: GeckoEnumStructAccessor(
                self.struct, SKSOKP, KSOKPH, None, LASSAK, None, None, QBMJVH
            ),
            SOKPHU: GeckoEnumStructAccessor(
                self.struct, SOKPHU, OKPHUO, None, LASSAK, None, None, QBMJVH
            ),
            KPHUOJ: GeckoEnumStructAccessor(
                self.struct, KPHUOJ, PHUOJR, None, LASSAK, None, None, QBMJVH
            ),
            HUOJRJ: GeckoEnumStructAccessor(
                self.struct, HUOJRJ, UOJRJH, None, LASSAK, None, None, QBMJVH
            ),
            OJRJHI: GeckoEnumStructAccessor(
                self.struct, OJRJHI, JRJHIU, None, LASSAK, None, None, QBMJVH
            ),
            RJHIUS: GeckoEnumStructAccessor(
                self.struct, RJHIUS, JHIUSO, None, HIUSOO, None, None, QBMJVH
            ),
            IUSOOQ: GeckoEnumStructAccessor(
                self.struct, IUSOOQ, USOOQN, None, HIUSOO, None, None, QBMJVH
            ),
            SOOQNR: GeckoByteStructAccessor(self.struct, SOOQNR, OOQNRS, QBMJVH),
            OQNRSJ: GeckoByteStructAccessor(self.struct, OQNRSJ, QNRSJM, QBMJVH),
            NRSJMC: GeckoByteStructAccessor(self.struct, NRSJMC, RSJMCB, QBMJVH),
            SJMCBF: GeckoByteStructAccessor(self.struct, SJMCBF, JMCBFE, QBMJVH),
            MCBFEG: GeckoByteStructAccessor(self.struct, MCBFEG, CBFEGZ, QBMJVH),
            BFEGZU: GeckoByteStructAccessor(self.struct, BFEGZU, FEGZUQ, QBMJVH),
            EGZUQE: GeckoByteStructAccessor(self.struct, EGZUQE, GZUQEX, QBMJVH),
            ZUQEXL: GeckoByteStructAccessor(self.struct, ZUQEXL, UQEXLS, QBMJVH),
            QEXLSX: GeckoByteStructAccessor(self.struct, QEXLSX, EXLSXU, QBMJVH),
            XLSXUJ: GeckoEnumStructAccessor(
                self.struct, XLSXUJ, LSXUJU, None, XUJUTY, None, None, None
            ),
            UJUTYE: GeckoByteStructAccessor(self.struct, UJUTYE, JUTYEK, None),
            UTYEKC: GeckoByteStructAccessor(self.struct, UTYEKC, TYEKCW, QBMJVH),
            YEKCWA: GeckoByteStructAccessor(self.struct, YEKCWA, EKCWAO, QBMJVH),
            KCWAON: GeckoByteStructAccessor(self.struct, KCWAON, CWAONP, QBMJVH),
            WAONPY: GeckoEnumStructAccessor(
                self.struct, WAONPY, AONPYY, YYLIUX, PYYLIU, None, YLIUXF, QBMJVH
            ),
            LIUXFE: GeckoEnumStructAccessor(
                self.struct, LIUXFE, IUXFEF, None, EFJTAC, None, None, QBMJVH
            ),
            FJTACC: GeckoEnumStructAccessor(
                self.struct, FJTACC, JTACCP, None, CCPQIP, None, None, QBMJVH
            ),
            CPQIPO: GeckoEnumStructAccessor(
                self.struct, CPQIPO, PQIPOU, None, OUYNQJ, None, None, QBMJVH
            ),
            UYNQJY: GeckoEnumStructAccessor(
                self.struct, UYNQJY, AONPYY, YLIUXF, QJYMOU, None, YLIUXF, QBMJVH
            ),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoByteStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoByteStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoByteStructAccessor(self.struct, BLKXSJ, LKXSJW, QBMJVH),
            KXSJWM: GeckoByteStructAccessor(self.struct, KXSJWM, XSJWMN, QBMJVH),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, MNZMJI, None, None, QBMJVH
            ),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, ZMJIGY, None, IGYOUS, None, None, QBMJVH
            ),
            GYOUSP: GeckoEnumStructAccessor(
                self.struct, GYOUSP, YOUSPB, None, OUSPBW, None, None, QBMJVH
            ),
            USPBWJ: GeckoEnumStructAccessor(
                self.struct, USPBWJ, SPBWJY, None, WJYKLG, None, None, QBMJVH
            ),
            JYKLGQ: GeckoByteStructAccessor(self.struct, JYKLGQ, YKLGQP, QBMJVH),
            KLGQPL: GeckoTempStructAccessor(self.struct, KLGQPL, LGQPLS, QBMJVH),
            GQPLSP: GeckoEnumStructAccessor(
                self.struct, GQPLSP, QPLSPF, None, SPFTSI, None, None, QBMJVH
            ),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, OUSPBW, None, None, QBMJVH
            ),
            TSIFJB: GeckoByteStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoTempStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoTempStructAccessor(self.struct, JBIAMJ, BIAMJM, QBMJVH),
            IAMJMA: GeckoEnumStructAccessor(
                self.struct, IAMJMA, AMJMAO, None, JMAOAW, None, None, QBMJVH
            ),
            MAOAWB: GeckoByteStructAccessor(self.struct, MAOAWB, AOAWBS, QBMJVH),
            OAWBSI: GeckoEnumStructAccessor(
                self.struct, OAWBSI, AWBSIR, None, SIRYXB, None, None, QBMJVH
            ),
            IRYXBQ: GeckoByteStructAccessor(self.struct, IRYXBQ, RYXBQF, QBMJVH),
            YXBQFY: GeckoByteStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoEnumStructAccessor(
                self.struct, BQFYLJ, QFYLJU, None, YLJUIK, None, None, QBMJVH
            ),
            LJUIKF: GeckoByteStructAccessor(self.struct, LJUIKF, JUIKFW, QBMJVH),
            UIKFWR: GeckoTimeStructAccessor(self.struct, UIKFWR, IKFWRK, QBMJVH),
            KFWRKI: GeckoTimeStructAccessor(self.struct, KFWRKI, FWRKIN, QBMJVH),
            WRKINE: GeckoTimeStructAccessor(self.struct, WRKINE, RKINEJ, QBMJVH),
            KINEJN: GeckoTimeStructAccessor(self.struct, KINEJN, INEJNI, QBMJVH),
            NEJNIB: GeckoEnumStructAccessor(
                self.struct, NEJNIB, EJNIBX, None, NIBXYB, None, None, QBMJVH
            ),
            IBXYBQ: GeckoBoolStructAccessor(
                self.struct, IBXYBQ, BXYBQS, YYLIUX, QBMJVH
            ),
            XYBQSN: GeckoBoolStructAccessor(
                self.struct, XYBQSN, YBQSNQ, YLIUXF, QBMJVH
            ),
            BQSNQL: GeckoBoolStructAccessor(
                self.struct, BQSNQL, YBQSNQ, YYLIUX, QBMJVH
            ),
            QSNQLN: GeckoBoolStructAccessor(
                self.struct, QSNQLN, YBQSNQ, SNQLNM, QBMJVH
            ),
            NQLNMH: GeckoBoolStructAccessor(
                self.struct, NQLNMH, YBQSNQ, QLNMHX, QBMJVH
            ),
            LNMHXE: GeckoEnumStructAccessor(
                self.struct, LNMHXE, NMHXEK, None, XEKVKZ, None, None, QBMJVH
            ),
            EKVKZI: GeckoEnumStructAccessor(
                self.struct, EKVKZI, KVKZIL, None, ZILXWA, None, None, QBMJVH
            ),
            ILXWAJ: GeckoByteStructAccessor(self.struct, ILXWAJ, LXWAJV, QBMJVH),
            XWAJVD: GeckoEnumStructAccessor(
                self.struct, XWAJVD, WAJVDQ, None, VDQLAI, None, None, QBMJVH
            ),
            DQLAII: GeckoWordStructAccessor(self.struct, DQLAII, QLAIID, QBMJVH),
            LAIIDN: GeckoEnumStructAccessor(
                self.struct, LAIIDN, AONPYY, SNQLNM, IDNIBX, None, YLIUXF, QBMJVH
            ),
            DNIBXT: GeckoBoolStructAccessor(
                self.struct, DNIBXT, AONPYY, NIBXTI, QBMJVH
            ),
        }

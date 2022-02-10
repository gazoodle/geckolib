#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v50'
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
AJVDQL = 50
AKQXPI = 14
AMJMAO = "".join(chr(c) for c in [67, 69])
AOAWBS = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
AONPYY = 85
ASSAKQ = "".join(chr(c) for c in [79, 117, 116, 50])
AWBSIR = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
BIAMJM = 51
BLKXSJ = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
BQSNQL = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
BSIRYX = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
BSKSOK = 19
BWJYKL = "".join(chr(c) for c in [70])
BXYBQS = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
CBFEGZ = 46
CPQIPO = "".join(
    chr(c) for c in [79, 84, 65, 99, 116, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 54])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 56
CXQIEF = 17
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EJNIBX = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
EKCWAO = 55
EKVKZI = 34
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = 50
FEFJTA = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FEGZUQ = 47
FJBIAM = 81
FJTACC = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 74
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
GLRAHE = 38
GQPLSP = 35
GYOUSP = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
GZUQEX = 48
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 55])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 49, 49])
HXEKVK = 79
IAMJMA = "".join(chr(c) for c in [85, 76])
IBXYBQ = 3
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
IKFWRK = 75
ILXWAJ = 68
INEJNI = 76
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = 59
IRYXBQ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
IUXFEF = 32
IVLASS = "".join(chr(c) for c in [])
JBIAMJ = "".join(chr(c) for c in [85, 76, 95, 67, 69])
JHIUSO = 25
JIGYOU = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
JMAOAW = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
JMCBFE = 45
JNIBXY = 1
JRJHIU = 24
JTACCP = 27
JUIKFW = 10
JUTYEK = 84
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
JYMOUN = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
KCWAON = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
KFWRKI = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
KINEJN = "".join(
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
KLGQPL = 31
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 49, 48])
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 52])
KSOKPH = 20
KVKZIL = "".join(chr(c) for c in [65, 109, 80, 109])
KXSJWM = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
LGQPLS = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
LIUXFE = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
LJUIKF = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
LKXSJW = 28
LNMHXE = "".join(chr(c) for c in [83, 108, 97, 118, 101])
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
LSXUJU = 83
MAOAWB = 52
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
MHXEKV = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
MJIGYO = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
MJVHFT = 12
MOUNBL = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
NEJNIB = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
NIBXYB = "".join(
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
NPYYLI = "".join(chr(c) for c in [79, 119, 110])
NQJYMO = "".join(
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
NQLNMH = 77
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
NZMJIG = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
OAWBSI = 53
OCTHBS = 41
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 50])
OKPHUO = 21
ONPYYL = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OOQNRS = 42
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
OUNBLK = 82
OUSPBW = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
OUYNQJ = 60
PBWJYK = 33
PFTSIF = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
PHUOJR = 22
PICXQI = 16
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 70
POUYNQ = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
PQIPOU = 57
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QFYLJU = 6
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
QJYMOU = 64
QLNMHX = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
QNRSJM = 43
QPLSPF = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
QXPICX = 15
RAHEOC = 39
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RKINEJ = 86
RSJMCB = 44
RYXBQF = 3
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 51])
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 56])
SNQLNM = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 57])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
SPBWJY = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
SPFTSI = 72
SSAKQX = 13
SXUJUT = "".join(chr(c) for c in [76, 73])
TACCPQ = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
THBSKS = 18
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = "".join(chr(c) for c in [78, 105, 103, 104, 116])
TYEKCW = 54
UIKFWR = "".join(
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
UJUTYE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UNBLKX = "".join(chr(c) for c in [80, 49])
UOJRJH = 23
UQEXLS = 49
USOOQN = 26
USPBWJ = 1
UTYEKC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UXFEFJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
UYNQJY = "".join(
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
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = "".join(chr(c) for c in [50, 52, 104])
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAONPY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
WBSIRY = 78
WJYKLG = "".join(chr(c) for c in [67])
WMNZMJ = 29
WRKINE = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
XBQFYL = 4
XEKVKZ = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
XFEFJT = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 53])
XQGLRA = 37
XQIEFX = "".join(chr(c) for c in [72, 84, 82])
XSJWMN = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
XYBQSN = 80
YBQSNQ = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
YEKCWA = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
YKLGQP = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
YLIUXF = 2
YLJUIK = 8
YMOUNB = 66
YNQJYM = 62
YOUSPB = 67
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
YYLIUX = 0
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
ZMJIGY = 30
ZUQEXL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
CCPQIP = [TACCPQ, ACCPQI]
EFJTAC = [UXFEFJ, XFEFJT, FEFJTA]
FWRKIN = [JVHFTH, KFWRKI]
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
IGYOUS = [MJIGYO, JIGYOU]
JYKLGQ = [BWJYKL, WJYKLG]
KZILXW = [JVHFTH, KVKZIL, VKZILX]
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
LXWAJV = [
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
MJMAOA = [IAMJMA, AMJMAO]
MNZMJI = [PIPIVL, UNBLKX]
NBLKXS = [JVHFTH, UNBLKX, PIPIVL]
NMHXEK = [IVLASS, QLNMHX, LNMHXE]
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
QSNQLN = [YBQSNQ, BQSNQL]
SIFJBI = [MJIGYO, TSIFJB]
SIRYXB = [MJIGYO, BSIRYX]
SJWMNZ = [KXSJWM, XSJWMN]
WAJVDQ = []
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
XWAJVD = [SXUJUT]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return AJVDQL

    @property
    def output_keys(self):
        return LXWAJV

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
            CPQIPO: GeckoTempStructAccessor(self.struct, CPQIPO, PQIPOU, QBMJVH),
            QIPOUY: GeckoByteStructAccessor(self.struct, QIPOUY, IPOUYN, QBMJVH),
            POUYNQ: GeckoWordStructAccessor(self.struct, POUYNQ, OUYNQJ, QBMJVH),
            UYNQJY: GeckoWordStructAccessor(self.struct, UYNQJY, YNQJYM, QBMJVH),
            NQJYMO: GeckoWordStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoEnumStructAccessor(
                self.struct, MOUNBL, OUNBLK, None, NBLKXS, None, None, QBMJVH
            ),
            BLKXSJ: GeckoEnumStructAccessor(
                self.struct, BLKXSJ, LKXSJW, None, SJWMNZ, None, None, QBMJVH
            ),
            JWMNZM: GeckoEnumStructAccessor(
                self.struct, JWMNZM, WMNZMJ, None, MNZMJI, None, None, QBMJVH
            ),
            NZMJIG: GeckoEnumStructAccessor(
                self.struct, NZMJIG, ZMJIGY, None, IGYOUS, None, None, QBMJVH
            ),
            GYOUSP: GeckoByteStructAccessor(self.struct, GYOUSP, YOUSPB, QBMJVH),
            OUSPBW: GeckoTempStructAccessor(self.struct, OUSPBW, USPBWJ, QBMJVH),
            SPBWJY: GeckoEnumStructAccessor(
                self.struct, SPBWJY, PBWJYK, None, JYKLGQ, None, None, QBMJVH
            ),
            YKLGQP: GeckoEnumStructAccessor(
                self.struct, YKLGQP, KLGQPL, None, MNZMJI, None, None, QBMJVH
            ),
            LGQPLS: GeckoByteStructAccessor(self.struct, LGQPLS, GQPLSP, QBMJVH),
            QPLSPF: GeckoTempStructAccessor(self.struct, QPLSPF, PLSPFT, QBMJVH),
            LSPFTS: GeckoTempStructAccessor(self.struct, LSPFTS, SPFTSI, QBMJVH),
            PFTSIF: GeckoEnumStructAccessor(
                self.struct, PFTSIF, FTSIFJ, None, SIFJBI, None, None, QBMJVH
            ),
            IFJBIA: GeckoByteStructAccessor(self.struct, IFJBIA, FJBIAM, QBMJVH),
            JBIAMJ: GeckoEnumStructAccessor(
                self.struct, JBIAMJ, BIAMJM, None, MJMAOA, None, None, QBMJVH
            ),
            JMAOAW: GeckoByteStructAccessor(self.struct, JMAOAW, MAOAWB, QBMJVH),
            AOAWBS: GeckoByteStructAccessor(self.struct, AOAWBS, OAWBSI, QBMJVH),
            AWBSIR: GeckoEnumStructAccessor(
                self.struct, AWBSIR, WBSIRY, None, SIRYXB, None, None, QBMJVH
            ),
            IRYXBQ: GeckoByteStructAccessor(self.struct, IRYXBQ, RYXBQF, QBMJVH),
            YXBQFY: GeckoTimeStructAccessor(self.struct, YXBQFY, XBQFYL, QBMJVH),
            BQFYLJ: GeckoTimeStructAccessor(self.struct, BQFYLJ, QFYLJU, QBMJVH),
            FYLJUI: GeckoTimeStructAccessor(self.struct, FYLJUI, YLJUIK, QBMJVH),
            LJUIKF: GeckoTimeStructAccessor(self.struct, LJUIKF, JUIKFW, QBMJVH),
            UIKFWR: GeckoEnumStructAccessor(
                self.struct, UIKFWR, IKFWRK, None, FWRKIN, None, None, QBMJVH
            ),
            WRKINE: GeckoBoolStructAccessor(
                self.struct, WRKINE, RKINEJ, YYLIUX, QBMJVH
            ),
            KINEJN: GeckoBoolStructAccessor(
                self.struct, KINEJN, INEJNI, YLIUXF, QBMJVH
            ),
            NEJNIB: GeckoBoolStructAccessor(
                self.struct, NEJNIB, INEJNI, YYLIUX, QBMJVH
            ),
            EJNIBX: GeckoBoolStructAccessor(
                self.struct, EJNIBX, INEJNI, JNIBXY, QBMJVH
            ),
            NIBXYB: GeckoBoolStructAccessor(
                self.struct, NIBXYB, INEJNI, IBXYBQ, QBMJVH
            ),
            BXYBQS: GeckoEnumStructAccessor(
                self.struct, BXYBQS, XYBQSN, None, QSNQLN, None, None, QBMJVH
            ),
            SNQLNM: GeckoEnumStructAccessor(
                self.struct, SNQLNM, NQLNMH, None, NMHXEK, None, None, QBMJVH
            ),
            MHXEKV: GeckoByteStructAccessor(self.struct, MHXEKV, HXEKVK, QBMJVH),
            XEKVKZ: GeckoEnumStructAccessor(
                self.struct, XEKVKZ, EKVKZI, None, KZILXW, None, None, QBMJVH
            ),
            ZILXWA: GeckoWordStructAccessor(self.struct, ZILXWA, ILXWAJ, QBMJVH),
        }

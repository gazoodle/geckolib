#!/usr/bin/python3
"""
    GeckoConfigStruct - A class to manage the ConfigStruct for 'InXE v51'
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
AJVDQL = 64
AKQXPI = 14
AMJMAO = 77
AOAWBS = "".join(chr(c) for c in [67, 69])
AONPYY = 81
ASSAKQ = "".join(chr(c) for c in [79, 117, 116, 50])
AWBSIR = "".join(chr(c) for c in [78, 98, 80, 104, 97, 115, 101, 115])
BFEGZU = "".join(chr(c) for c in [79, 117, 116, 49, 49, 67, 117, 114])
BLKXSJ = "".join(chr(c) for c in [68, 114, 97, 105, 110, 77, 111, 100, 101])
BMJVHF = "".join(chr(c) for c in [79, 117, 116, 49])
BQFYLJ = "".join(chr(c) for c in [70, 105, 108, 116, 70, 114, 101, 113])
BQSNQL = 3
BSIRYX = "".join(
    chr(c) for c in [73, 110, 112, 117, 116, 67, 117, 114, 114, 101, 110, 116]
)
BSKSOK = 18
BWJYKL = "".join(chr(c) for c in [83, 101, 116, 112, 111, 105, 110, 116, 71])
BXYBQS = "".join(
    chr(c) for c in [79, 102, 102, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
CBFEGZ = 45
CPQIPO = "".join(chr(c) for c in [79, 116, 79, 112, 116, 105, 111, 110])
CQBMJV = 0
CTHBSK = "".join(chr(c) for c in [79, 117, 116, 54])
CVYYPI = "".join(chr(c) for c in [80, 52, 72])
CWAONP = 56
CXQIEF = 26
ECVYYP = "".join(chr(c) for c in [80, 51, 76])
EFXQGL = 36
EGZUQE = "".join(chr(c) for c in [79, 117, 116, 49, 50, 67, 117, 114])
EJNIBX = 82
EKCWAO = 55
EOCTHB = "".join(chr(c) for c in [79, 117, 116, 72, 116, 82, 67, 117, 114])
EXLSXU = 49
FEFJTA = "".join(chr(c) for c in [70, 105, 108, 116, 80, 49])
FEGZUQ = 46
FJBIAM = 70
FJTACC = "".join(chr(c) for c in [67, 112, 85, 115, 97, 103, 101])
FTHECV = "".join(chr(c) for c in [80, 50, 72])
FTSIFJ = 66
FWRKIN = 10
FXQGLR = "".join(chr(c) for c in [79, 117, 116, 50, 67, 117, 114])
FYLJUI = "".join(chr(c) for c in [70, 105, 108, 116, 83, 116, 97, 114, 116])
GLRAHE = 38
GYOUSP = 30
GZUQEX = 47
HBSKSO = "".join(chr(c) for c in [79, 117, 116, 55])
HECVYY = "".join(chr(c) for c in [80, 51, 72])
HEOCTH = 40
HFTHEC = "".join(chr(c) for c in [80, 49, 76])
HUOJRJ = "".join(chr(c) for c in [79, 117, 116, 49, 49])
HXEKVK = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114])
IAMJMA = "".join(
    chr(c) for c in [78, 111, 72, 101, 97, 116, 80, 101, 114, 105, 111, 100]
)
IBXYBQ = "".join(
    chr(c)
    for c in [83, 111, 97, 107, 79, 110, 67, 117, 115, 116, 111, 109, 75, 101, 121]
)
ICXQIE = "".join(chr(c) for c in [79, 117, 116, 72, 116, 114])
IEFXQG = "".join(chr(c) for c in [79, 117, 116, 49, 67, 117, 114])
IFJBIA = "".join(chr(c) for c in [69, 99, 111, 110, 84, 121, 112, 101])
IGYOUS = "".join(chr(c) for c in [79, 51, 84, 121, 112, 101])
IKFWRK = 8
ILXWAJ = "".join(chr(c) for c in [65, 109, 80, 109])
IPIVLA = "".join(chr(c) for c in [79, 51])
IPOUYN = "".join(
    chr(c) for c in [65, 108, 119, 97, 121, 115, 69, 110, 97, 98, 108, 101, 100]
)
IRYXBQ = "".join(chr(c) for c in [73, 110, 112, 117, 116, 77, 101, 110, 117])
IUSOOQ = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50])
IUXFEF = 32
IVLASS = "".join(chr(c) for c in [])
JBIAMJ = "".join(chr(c) for c in [78, 105, 103, 104, 116])
JHIUSO = 24
JMAOAW = 51
JMCBFE = 44
JNIBXY = "".join(
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
JRJHIU = 23
JTACCP = 27
JUIKFW = 6
JUTYEK = 80
JVHFTH = "".join(chr(c) for c in [78, 65])
JWMNZM = 28
JYKLGQ = "".join(chr(c) for c in [84, 101, 109, 112, 85, 110, 105, 116, 115])
JYMOUN = "".join(
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
KCWAON = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 79, 117, 116])
KFWRKI = "".join(chr(c) for c in [69, 99, 111, 110, 68, 117, 114])
KINEJN = "".join(chr(c) for c in [65, 118, 97, 105, 108, 97, 98, 108, 101])
KLGQPL = "".join(chr(c) for c in [70])
KPHUOJ = "".join(chr(c) for c in [79, 117, 116, 49, 48])
KQXPIC = "".join(chr(c) for c in [79, 117, 116, 52])
KSOKPH = 19
KVKZIL = "".join(chr(c) for c in [83, 108, 97, 118, 101, 67, 111, 110, 102, 105, 103])
KXSJWM = "".join(chr(c) for c in [80, 49])
KZILXW = "".join(chr(c) for c in [84, 105, 109, 101, 70, 111, 114, 109, 97, 116])
LGQPLS = "".join(chr(c) for c in [67])
LIUXFE = "".join(
    chr(c) for c in [70, 105, 108, 116, 73, 110, 116, 101, 114, 102, 97, 99, 101]
)
LJUIKF = "".join(chr(c) for c in [70, 105, 108, 116, 68, 117, 114])
LKXSJW = 78
LRAHEO = "".join(chr(c) for c in [79, 117, 116, 52, 67, 117, 114])
LSPFTS = "".join(
    chr(c) for c in [67, 111, 111, 108, 100, 111, 119, 110, 84, 105, 109, 101]
)
LSXUJU = 79
LXWAJV = "".join(chr(c) for c in [50, 52, 104])
MAOAWB = "".join(chr(c) for c in [85, 76])
MCBFEG = "".join(chr(c) for c in [79, 117, 116, 49, 48, 67, 117, 114])
MHXEKV = 73
MJIGYO = 29
MJMAOA = "".join(chr(c) for c in [85, 76, 95, 67, 69])
MJVHFT = 12
MNZMJI = "".join(chr(c) for c in [65, 108, 119, 97, 121, 115])
MOUNBL = "".join(
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
NBLKXS = 62
NEJNIB = "".join(chr(c) for c in [85, 68, 80, 114, 111, 103, 69, 99, 111, 110])
NIBXYB = 72
NMHXEK = "".join(chr(c) for c in [77, 97, 115, 116, 101, 114, 83, 108, 97, 118, 101])
NPYYLI = "".join(chr(c) for c in [79, 119, 110])
NQJYMO = "".join(
    chr(c)
    for c in [67, 112, 79, 110, 84, 105, 109, 101, 68, 117, 114, 105, 110, 103, 79, 84]
)
NQLNMH = "".join(
    chr(c) for c in [78, 111, 66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67]
)
NRSJMC = "".join(chr(c) for c in [79, 117, 116, 56, 67, 117, 114])
OCTHBS = 50
OJRJHI = "".join(chr(c) for c in [79, 117, 116, 49, 50])
OKPHUO = 20
ONPYYL = "".join(chr(c) for c in [83, 104, 97, 114, 101, 100])
OOQNRS = 41
OQNRSJ = "".join(chr(c) for c in [79, 117, 116, 55, 67, 117, 114])
OUNBLK = 61
OUSPBW = "".join(chr(c) for c in [84, 111, 103, 103, 108, 101])
PBWJYK = 63
PFTSIF = "".join(
    chr(c) for c in [77, 105, 110, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
PHUOJR = 21
PICXQI = 16
PIPIVL = "".join(chr(c) for c in [67, 80])
PIVLAS = "".join(chr(c) for c in [76, 49, 50, 48])
PLSPFT = 31
POUYNQ = "".join(
    chr(c) for c in [87, 105, 116, 104, 83, 80, 79, 118, 101, 114, 57, 53, 70]
)
PQIPOU = 57
QBMJVH = "".join(chr(c) for c in [65, 76, 76])
QEXLSX = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 50, 67, 117, 114])
QFYLJU = 3
QGLRAH = "".join(chr(c) for c in [79, 117, 116, 51, 67, 117, 114])
QIPOUY = "".join(chr(c) for c in [68, 105, 115, 97, 98, 108, 101, 100])
QJYMOU = 59
QLAIID = 51
QLNMHX = "".join(chr(c) for c in [66, 108, 111, 119, 101, 114, 79, 110, 73, 50, 67])
QNRSJM = 42
QPLSPF = "".join(chr(c) for c in [72, 101, 97, 116, 101, 114, 80, 117, 109, 112])
QSNQLN = "".join(
    chr(c) for c in [77, 117, 108, 116, 105, 75, 101, 121, 79, 112, 116, 105, 111, 110]
)
QXPICX = 15
RAHEOC = 39
RJHIUS = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116])
RKINEJ = 71
RSJMCB = 43
RYXBQF = 74
SAKQXP = "".join(chr(c) for c in [79, 117, 116, 51])
SIFJBI = 68
SIRYXB = 53
SJMCBF = "".join(chr(c) for c in [79, 117, 116, 57, 67, 117, 114])
SJWMNZ = "".join(chr(c) for c in [79, 51, 85, 115, 97, 103, 101])
SKSOKP = "".join(chr(c) for c in [79, 117, 116, 56])
SNQLNM = 76
SOKPHU = "".join(chr(c) for c in [79, 117, 116, 57])
SOOQNR = "".join(chr(c) for c in [79, 117, 116, 54, 67, 117, 114])
SPBWJY = "".join(
    chr(c) for c in [79, 51, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
SPFTSI = 35
SSAKQX = 13
SXUJUT = "".join(chr(c) for c in [76, 73])
TACCPQ = "".join(chr(c) for c in [83, 84, 65, 78, 68, 65, 82, 68])
THBSKS = 17
THECVY = "".join(chr(c) for c in [80, 50, 76])
TSIFJB = "".join(
    chr(c) for c in [77, 97, 120, 83, 101, 116, 112, 111, 105, 110, 116, 71]
)
TYEKCW = 54
UIKFWR = "".join(chr(c) for c in [69, 99, 111, 110, 83, 116, 97, 114, 116])
UJUTYE = "".join(chr(c) for c in [76, 105, 103, 104, 116, 73, 110, 116, 115])
UNBLKX = "".join(
    chr(c)
    for c in [70, 105, 108, 116, 83, 117, 115, 112, 101, 110, 100, 84, 105, 109, 101]
)
UOJRJH = 22
UQEXLS = 48
USOOQN = 25
UTYEKC = "".join(chr(c) for c in [80, 117, 109, 112, 84, 105, 109, 101, 79, 117, 116])
UXFEFJ = "".join(chr(c) for c in [80, 117, 114, 103, 101, 79, 110, 108, 121])
UYNQJY = "".join(chr(c) for c in [79, 84, 84, 114, 105, 103, 103, 101, 114, 71])
VHFTHE = "".join(chr(c) for c in [80, 49, 72])
VKZILX = 75
VLASSA = "".join(chr(c) for c in [70, 117, 108, 108, 79, 110])
VYYPIP = "".join(chr(c) for c in [80, 52, 76])
WAJVDQ = "".join(
    chr(c)
    for c in [65, 109, 98, 105, 97, 110, 116, 79, 72, 84, 114, 105, 103, 65, 68, 67]
)
WAONPY = "".join(chr(c) for c in [76, 49, 50, 48, 84, 105, 109, 101, 114])
WBSIRY = 52
WJYKLG = 1
WMNZMJ = "".join(chr(c) for c in [70, 105, 108, 116, 101, 114])
WRKINE = "".join(
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
XEKVKZ = "".join(chr(c) for c in [83, 108, 97, 118, 101])
XFEFJT = "".join(chr(c) for c in [70, 105, 108, 116, 67, 80])
XLSXUJ = "".join(chr(c) for c in [79, 117, 116, 76, 105])
XPICXQ = "".join(chr(c) for c in [79, 117, 116, 53])
XQGLRA = 37
XQIEFX = "".join(chr(c) for c in [72, 84, 82])
XYBQSN = 1
YBQSNQ = "".join(
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
YEKCWA = "".join(
    chr(c) for c in [76, 105, 103, 104, 116, 84, 105, 109, 101, 79, 117, 116]
)
YKLGQP = 33
YLIUXF = 2
YLJUIK = 4
YMOUNB = 60
YNQJYM = 58
YOUSPB = "".join(chr(c) for c in [83, 116, 97, 110, 100, 97, 114, 100])
YPIPIV = "".join(chr(c) for c in [66, 76, 79])
YXBQFY = "".join(chr(c) for c in [68, 117, 97, 108, 80, 97, 99, 107])
YYLIUX = 0
YYPIPI = "".join(chr(c) for c in [80, 53])
ZCQBMJ = "".join(
    chr(c) for c in [67, 111, 110, 102, 105, 103, 78, 117, 109, 98, 101, 114]
)
ZILXWA = 34
ZMJIGY = "".join(chr(c) for c in [79, 51, 80, 117, 109, 112])
ZUQEXL = "".join(chr(c) for c in [68, 105, 114, 101, 99, 116, 67, 117, 114])
BIAMJM = [YOUSPB, JBIAMJ]
CCPQIP = [TACCPQ, ACCPQI]
DQLAII = []
EFJTAC = [UXFEFJ, XFEFJT, FEFJTA]
EKVKZI = [IVLASS, HXEKVK, XEKVKZ]
GQPLSP = [KLGQPL, LGQPLS]
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
INEJNI = [JVHFTH, KINEJN]
JIGYOU = [PIPIVL, KXSJWM]
JVDQLA = [
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
LNMHXE = [NQLNMH, QLNMHX]
NZMJIG = [WMNZMJ, MNZMJI]
OAWBSI = [MAOAWB, AOAWBS]
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
USPBWJ = [YOUSPB, OUSPBW]
VDQLAI = [SXUJUT]
XBQFYL = [YOUSPB, YXBQFY]
XSJWMN = [JVHFTH, KXSJWM, PIPIVL]
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
XWAJVD = [JVHFTH, ILXWAJ, LXWAJV]


class GeckoConfigStruct:
    def __init__(self, struct_):
        self.struct = struct_

    @property
    def version(self):
        return QLAIID

    @property
    def output_keys(self):
        return JVDQLA

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
            UYNQJY: GeckoByteStructAccessor(self.struct, UYNQJY, YNQJYM, QBMJVH),
            NQJYMO: GeckoByteStructAccessor(self.struct, NQJYMO, QJYMOU, QBMJVH),
            JYMOUN: GeckoByteStructAccessor(self.struct, JYMOUN, YMOUNB, QBMJVH),
            MOUNBL: GeckoByteStructAccessor(self.struct, MOUNBL, OUNBLK, QBMJVH),
            UNBLKX: GeckoByteStructAccessor(self.struct, UNBLKX, NBLKXS, QBMJVH),
            BLKXSJ: GeckoEnumStructAccessor(
                self.struct, BLKXSJ, LKXSJW, None, XSJWMN, None, None, QBMJVH
            ),
            SJWMNZ: GeckoEnumStructAccessor(
                self.struct, SJWMNZ, JWMNZM, None, NZMJIG, None, None, QBMJVH
            ),
            ZMJIGY: GeckoEnumStructAccessor(
                self.struct, ZMJIGY, MJIGYO, None, JIGYOU, None, None, QBMJVH
            ),
            IGYOUS: GeckoEnumStructAccessor(
                self.struct, IGYOUS, GYOUSP, None, USPBWJ, None, None, QBMJVH
            ),
            SPBWJY: GeckoByteStructAccessor(self.struct, SPBWJY, PBWJYK, QBMJVH),
            BWJYKL: GeckoTempStructAccessor(self.struct, BWJYKL, WJYKLG, QBMJVH),
            JYKLGQ: GeckoEnumStructAccessor(
                self.struct, JYKLGQ, YKLGQP, None, GQPLSP, None, None, QBMJVH
            ),
            QPLSPF: GeckoEnumStructAccessor(
                self.struct, QPLSPF, PLSPFT, None, JIGYOU, None, None, QBMJVH
            ),
            LSPFTS: GeckoByteStructAccessor(self.struct, LSPFTS, SPFTSI, QBMJVH),
            PFTSIF: GeckoTempStructAccessor(self.struct, PFTSIF, FTSIFJ, QBMJVH),
            TSIFJB: GeckoTempStructAccessor(self.struct, TSIFJB, SIFJBI, QBMJVH),
            IFJBIA: GeckoEnumStructAccessor(
                self.struct, IFJBIA, FJBIAM, None, BIAMJM, None, None, QBMJVH
            ),
            IAMJMA: GeckoByteStructAccessor(self.struct, IAMJMA, AMJMAO, QBMJVH),
            MJMAOA: GeckoEnumStructAccessor(
                self.struct, MJMAOA, JMAOAW, None, OAWBSI, None, None, QBMJVH
            ),
            AWBSIR: GeckoByteStructAccessor(self.struct, AWBSIR, WBSIRY, QBMJVH),
            BSIRYX: GeckoByteStructAccessor(self.struct, BSIRYX, SIRYXB, QBMJVH),
            IRYXBQ: GeckoEnumStructAccessor(
                self.struct, IRYXBQ, RYXBQF, None, XBQFYL, None, None, QBMJVH
            ),
            BQFYLJ: GeckoByteStructAccessor(self.struct, BQFYLJ, QFYLJU, QBMJVH),
            FYLJUI: GeckoTimeStructAccessor(self.struct, FYLJUI, YLJUIK, QBMJVH),
            LJUIKF: GeckoTimeStructAccessor(self.struct, LJUIKF, JUIKFW, QBMJVH),
            UIKFWR: GeckoTimeStructAccessor(self.struct, UIKFWR, IKFWRK, QBMJVH),
            KFWRKI: GeckoTimeStructAccessor(self.struct, KFWRKI, FWRKIN, QBMJVH),
            WRKINE: GeckoEnumStructAccessor(
                self.struct, WRKINE, RKINEJ, None, INEJNI, None, None, QBMJVH
            ),
            NEJNIB: GeckoBoolStructAccessor(
                self.struct, NEJNIB, EJNIBX, YYLIUX, QBMJVH
            ),
            JNIBXY: GeckoBoolStructAccessor(
                self.struct, JNIBXY, NIBXYB, YLIUXF, QBMJVH
            ),
            IBXYBQ: GeckoBoolStructAccessor(
                self.struct, IBXYBQ, NIBXYB, YYLIUX, QBMJVH
            ),
            BXYBQS: GeckoBoolStructAccessor(
                self.struct, BXYBQS, NIBXYB, XYBQSN, QBMJVH
            ),
            YBQSNQ: GeckoBoolStructAccessor(
                self.struct, YBQSNQ, NIBXYB, BQSNQL, QBMJVH
            ),
            QSNQLN: GeckoEnumStructAccessor(
                self.struct, QSNQLN, SNQLNM, None, LNMHXE, None, None, QBMJVH
            ),
            NMHXEK: GeckoEnumStructAccessor(
                self.struct, NMHXEK, MHXEKV, None, EKVKZI, None, None, QBMJVH
            ),
            KVKZIL: GeckoByteStructAccessor(self.struct, KVKZIL, VKZILX, QBMJVH),
            KZILXW: GeckoEnumStructAccessor(
                self.struct, KZILXW, ZILXWA, None, XWAJVD, None, None, QBMJVH
            ),
            WAJVDQ: GeckoWordStructAccessor(self.struct, WAJVDQ, AJVDQL, QBMJVH),
        }

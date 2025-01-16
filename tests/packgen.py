"""PackGen - A tool to generate .py files to interface with different Gecko packs."""

import os
import xml.etree.ElementTree as ET

# The XML file to process
XML_FILE = "../src/geckolib/SpaPackStruct_39.0.0.0.xml"

CODE_PATH = "../src/geckolib/driver/packs"

IMPORTED_CLASSES = [
    "GeckoByteStructAccessor",
    "GeckoWordStructAccessor",
    "GeckoTimeStructAccessor",
    "GeckoBoolStructAccessor",
    "GeckoEnumStructAccessor",
    "GeckoTempStructAccessor",
]

OBFUSCATE_CONSTANTS = False
OBFUSCATE_STRINGS = False
OBFUSCATE_LISTS = False

KEY_GEN_STRING = (
    "ZCQBMJVHFTHECVYYPIPIVLASSAKQXPICXQIEFXQGLRAHEOCTHB"
    "SKSOKPHUOJRJHIUSOOQNRSJMCBFEGZUQEXLSXUJUTYEKCWAONP"
    "YYLIUXFEFJTACCPQIPOUYNQJYMOUNBLKXSJWMNZMJIGYOUSPBW"
    "JYKLGQPLSPFTSIFJBIAMJMAOAWBSIRYXBQFYLJUIKFWRKINEJN"
    "IBXYBQSNQLNMHXEKVKZILXWAJVDQLAIIDNIBXTIACQFFTTIDUB"
    "SSUHBVWVUBYGDSBDJQRJJJVYFCRTFMNHTBJEUTOPHUGTYIYWSK"
    "WIVDNQGVUNXNKMLOIJUGSELHBQNRXCHWDAFIKJPUNRJZTATDZX"
    "NQTMFZDGKEAKSTSEMCGETIXQVXOIHBXIBHZVOACMCVDSSRURAZ"
    "MKQTDKHTZBBEKBDFSROGMDDPMXFUBJLOINELWUEUHNNXWEEZFE"
    "TDRXAIVEMVCYWONFZCZOLSIPMDMPSCTTGCRHYUAXNCUGUCYRAP"
    "UMEAOESVZSSBVNAXADXLUBGJFJNTTUVRFLSIJUZMRKVFCPOUBM"
    "IKGNVFOUURIEVBVHDVRIDKEYGGVYKLTQLVHSVSIBEXLTPOXIUV"
    "MKZHWOGXXYOJQSGMECYXMPYDZQJJVGBXEPCVNTHXRMKNGOCHJQ"
    "POFBLCEPRIGFDGMVYQBFAFDCSKLIGALKHWUZIHNIZLIPOQENPA"
    "ZGZHHINXPEEBOYRRCWAQDPFURZPYMBVMJRRQNGEUYFDSXQGXRI"
    "LLYBEAACCJTUBFDQNGTPFSPCJARHSEFXPQWEWXGLLXEIJITFMX"
    "ZSNCLQDZOFKZFMYAIDFLQBQFYEHYQNYGFHHLEOFXZYOBDNKIBE"
    "VINWHJQAESJKPNDWQLKWRJYBXGPSRTIARBMRDNFXQXWYPLHUJG"
    "GEAAQZNWHTURFSZLKCIINQGOOELGYEPUDDEQSWFFXPGLWKZLXE"
    "EYOWUZYRWVZGTHCAYHYIVOXHNIAOMUTRSFVTKJHFLMNXAGICYS"
    "NSFVFABZDVIPGULJYRCNDQIOBMQNSSLAOICANHIQVEAXGMHUWQ"
    "ETNDNXCGLCHACQUDTRQOEOWGUWXRXOTCTZEDNNMVVZWVGHCNZG"
    "GGWTDTTSGUOWFMILNGBJTUAJSMTMJNJRRILCNRSRTCTYUSPFHU"
    "PUBRBTXDXPQQGJCCFHPFETVRCZKYBEQLKPUQEKQNZTIYEWGSVH"
    "MHRHKWQWQDAMWADGPSJHXFCDKCZQZLQSEOYGGKCZLMWWSWSQHX"
    "QENBGMGVHPQFUKXOKCGJTVDAMGSYUBZNXZPMALNKLLKAPEGHZS"
    "JOUXDYGFZVBJZZRUOKQKXJSEWJJMZHYBMKBECKEDAVBOZILCKI"
    "YQHIJCNRJCDDDSYRLWHEOQTMAUCPQFTQCWQAPHFBQMHXBVUCAQ"
    "FDMVAVBOFDYQNMCFXEGGXHRYPUCNVSPHAPEACQJFZELCQLCTYI"
    "SGIHJPXCRZFSILBRMFHRPCGFCCDXALIINPWVSCAWTLCVBANBWQ"
    "MBMBXKOOHXSGSJHJARJTEFBYVVEEPVVIVDJNMXWEUGGSDSSISC"
    "SMGSSGMEMQJQRXHTFRJKBSPUYPPVMPMXMBXRPOMESMKJVWIVHT"
    "OHZGGYOOTFAJELSUCIMFIOKUGIZIWNSNFUKFZJFCEWSZNDZAPX"
    "DWCJETMBZVVKZDPJAGRVAYPVZTEMDGJZWYEBQQGPNAOFSUEIEX"
    "OYACCVLBMOJGKLFAZMVEHOXGVXIXNTBVGTZEHBYEFOVGWYUCZZ"
    "OBRGBGNISMENSUYACIPPKKQTWAHYQBWRJOMRYBPQAMHORMHTHC"
    "IHFNIGVMDSSNHUTLMLAHXHJZCOBYQYZLSMXDSGIEJZDUISXUXK"
    "JLKBNZCXRQJAZAPSKCCGMAQPBYNUQBVSLNPWQWFFJSXVRWXGYA"
    "HPAHWWIZDTUTFIKEJCJDCUTEGDDGSCSDZJHOPDZPDCWEFRJSKQ"
    "YWCQRFLDYRHRLNSYUVJTWCGLMEXPZSOJCATUQIPSDUXPIFOXQW"
    "BEOATVYEZUURWWVSBHCDVYPMTISQLKSFZZXVUYGALUDZJXZE"
)

module_constants = {}


def write_python_preamble(file) -> None:
    """Write shebang, but this I think is not needed now."""
    file.write("#!/usr/bin/python3\n")


def write_module_init(file):
    write_python_preamble(file)
    file.write(f"from ..accessor import {', '.join(IMPORTED_CLASSES)}\n\n")
    file.write(f"__all__ = {IMPORTED_CLASSES}\n")


def write_pack_preamble(file, plateform_name, plateform_type, version):
    write_python_preamble(file)
    file.write('"""\n')
    file.write(f"    GeckoPack - A class to manage the pack for '{plateform_name}'\n")
    file.write('"""\n')
    file.write("\n")
    file.write("\n")
    file.write("class GeckoPack:\n")
    file.write("    def __init__(self, struct_):\n")
    file.write("        self.struct = struct_\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def name(self):\n")
    file.write(f"        return '{plateform_name}'\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def type(self):\n")
    file.write(f"        return {plateform_type}\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def revision(self):\n")
    file.write(f"        return {version}\n")


def write_import(file):
    file.write(f"from . import {', '.join(IMPORTED_CLASSES)}\n")
    file.write("\n")


def gen_uniq_key(val):
    while True:
        # candidate_key = "".join([chr(random.randint(65, 90)) for i in range(6)])
        candidate_key = KEY_GEN_STRING[
            len(module_constants) : len(module_constants) + 6
        ]
        if candidate_key not in module_constants:
            return candidate_key
        raise Exception(f"Ooops! at {len(module_constants)} with key '{candidate_key}'")


def add_constant(val):
    """Add a constant to the module constants returning the key"""
    global module_constants

    if OBFUSCATE_LISTS and isinstance(val, list):
        val = [add_constant(f'"{item}"') for item in val]

    # Do we already have this value stashed ?
    for var in module_constants:
        if module_constants[var] == val:
            return var if OBFUSCATE_CONSTANTS else module_constants[var]

    # Otherwise stash it
    key = gen_uniq_key(val)
    module_constants[key] = val
    return key if OBFUSCATE_CONSTANTS else val


def reset_constants():
    global module_constants
    module_constants = {}


def write_constant_value(file, val):
    if OBFUSCATE_STRINGS and isinstance(val, str) and val.startswith('"'):
        file.write(f"''.join(chr(c) for c in {[ord(ch) for ch in val[1:-1]]})\n")
    elif OBFUSCATE_LISTS and isinstance(val, list):
        file.write(f"[{', '.join(val)}]\n")
    else:
        file.write(f"{val}\n")


def write_constants(file):
    global module_constants
    if len(module_constants) == 0:
        return
    if not OBFUSCATE_CONSTANTS:
        return
    file.write("# Constants for this class\n")
    for var in sorted(module_constants):
        val = module_constants[var]
        if OBFUSCATE_LISTS and isinstance(val, list):
            continue
        file.write(f"{var} = ")
        write_constant_value(file, module_constants[var])
    if OBFUSCATE_LISTS:
        # Now the lists
        for var in sorted(module_constants):
            val = module_constants[var]
            if not isinstance(val, list):
                continue
            file.write(f"{var} = ")
            write_constant_value(file, module_constants[var])

    file.write("\n")


def write_log_preamble(file, plateform_name, logstruct):
    write_python_preamble(file)
    file.write('"""\n')
    file.write(
        f"    GeckoLogStruct - A class to manage the LogStruct for '{plateform_name}"
        f" v{logstruct.attrib['LibRev']}'\n"
    )
    file.write('"""\n')
    file.write("\n")
    write_import(file)

    logstruct.attrib["LibRev"] = add_constant(int(logstruct.attrib["LibRev"]))
    logstruct.attrib["Begin"] = add_constant(int(logstruct.attrib["Begin"]))
    logstruct.attrib["End"] = add_constant(int(logstruct.attrib["End"]))

    write_constants(file)
    file.write("\n")
    file.write("class GeckoLogStruct:\n")
    file.write("    def __init__(self, struct_):\n")
    file.write("        self.struct = struct_\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def version(self):\n")
    file.write(f"        return {logstruct.attrib['LibRev']}\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def begin(self):\n")
    file.write(f"        return {logstruct.attrib['Begin']}\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def end(self):\n")
    file.write(f"        return {logstruct.attrib['End']}\n")


def write_cfg_preamble(file, plateform_name, configstruct):
    write_python_preamble(file)
    file.write('"""\n')
    file.write(
        f"    GeckoConfigStruct - A class to manage the ConfigStruct for"
        f" '{plateform_name} v{configstruct.attrib['LibRev']}'\n"
    )
    file.write('"""\n')
    file.write("\n")
    write_import(file)

    configstruct.attrib["LibRev"] = add_constant(int(configstruct.attrib["LibRev"]))

    write_constants(file)
    file.write("\n")
    file.write("class GeckoConfigStruct:\n")
    file.write("    def __init__(self, struct_):\n")
    file.write("        self.struct = struct_\n")
    file.write("\n")
    file.write("    @property\n")
    file.write("    def version(self):\n")
    file.write(f"        return {configstruct.attrib['LibRev']}\n")


def generate_accessor_constants(xml):
    for element in xml.findall(".//*[@Pos]"):
        add_constant(f'"{element.tag}"')
        element.attrib["Pos"] = add_constant(element.attrib["Pos"])
        if "Items" in element.attrib:
            items = element.attrib["Items"].split("|")
            element.attrib["Items"] = add_constant(items)
        if "Item" in element.attrib:
            items = element.attrib["Item"].split("|")
            element.attrib["Item"] = add_constant(items)
        if "BitPos" in element.attrib:
            element.attrib["BitPos"] = add_constant(int(element.attrib["BitPos"]))
        if "Size" in element.attrib:
            element.attrib["Size"] = add_constant(int(element.attrib["Size"]))
        if "MaxItems" in element.attrib:
            element.attrib["MaxItems"] = add_constant(int(element.attrib["MaxItems"]))
        if "RW" in element.attrib:
            element.attrib["RW"] = add_constant(f'"{element.attrib["RW"]}"')

    output_paths = [
        './HCOutputConfig/*[@Type="Enum"]',
        './LCOutputConfig/*[@Type="Enum"]',
        './LVOutputConfig/*[@Type="Enum"]',
    ]

    all_outputs = [
        element.tag for xpath in output_paths for element in xml.findall(xpath)
    ]

    xml.attrib["AllOutputs"] = add_constant(all_outputs)

    all_devices = [element.tag for element in xml.findall("./DeviceStatus/*")] + ["LI"]
    xml.attrib["AllDevices"] = add_constant(all_devices)

    user_demands = [
        element.tag
        for element in xml.findall("./UserDemands/*")
        if element.tag.startswith("Ud")
    ]
    xml.attrib["UserDemands"] = add_constant(user_demands)

    # Errors are all properties in the <ErrorMessages> tag, anything with Err in the name
    known_err_tags = ["OverTemp", "TempNotValid", "SlaveOverTemp"]
    errors = [element.tag for element in xml.findall("./ErrorMessages/*")] + [
        element.tag
        for element in xml.findall(".//*")
        if element.tag.endswith("Err") or element.tag in known_err_tags
    ]
    errors = list(set(errors))  # Dedupe
    xml.attrib["ErrorMessages"] = add_constant(errors)


def write_get_accessors(file, xml):
    file.write("\n")
    file.write("    @property\n")
    file.write("    def accessors(self):\n")
    file.write("        return {\n")
    for element in xml.findall(".//*[@Pos]"):
        if element.tag.startswith("CFG"):
            continue
        if element.tag.startswith("CustomerID"):
            continue
        if element.tag.startswith("K600"):
            continue
        tag = f'"{element.tag}"'
        pos = element.attrib["Pos"]
        type = f'"{element.attrib["Type"]}"'
        bitpos = None
        if "BitPos" in element.attrib:
            bitpos = element.attrib["BitPos"]
        items = None
        if "Items" in element.attrib:
            items = f"{element.attrib['Items']}"
        # "PowerState" in mas-ibc-32k-log-1.py looks like a bug
        if "Item" in element.attrib:
            items = f"{element.attrib['Item']}"
        size = None
        if "Size" in element.attrib:
            size = element.attrib["Size"]
        maxitems = None
        if "MaxItems" in element.attrib:
            maxitems = element.attrib["MaxItems"]
        rw = None
        if "RW" in element.attrib:
            rw = element.attrib["RW"]

        file.write(f"            {add_constant(tag)}: ")
        if type == '"Byte"':
            assert items == None
            assert size == None
            assert bitpos == None
            assert maxitems == None
            file.write(
                f"GeckoByteStructAccessor(self.struct, {add_constant(tag)}, {pos}, {rw}),\n"
            )
        elif type == '"Bool"':
            assert items == None
            assert maxitems == None
            # In inxm-log-4 & in-xml-log-5 it is 2, but this is wrong
            if OBFUSCATE_CONSTANTS:
                assert size == None or module_constants[size] == 2
            else:
                assert size == None or size == 2
            file.write(
                f"GeckoBoolStructAccessor(self.struct, {add_constant(tag)}, {pos}, {bitpos}, {rw}),\n"
            )
        # MrStream log v3 has lowercase "word"
        elif type == '"Word"' or type == '"word"':
            assert items == None
            assert size == None
            assert bitpos == None
            assert maxitems == None

            if "temp" in element.tag.lower() or "setpoint" in element.tag.lower():
                file.write(
                    f"GeckoTempStructAccessor(self.struct, {add_constant(tag)}, {pos}, {rw}),\n"
                )
            else:
                file.write(
                    f"GeckoWordStructAccessor(self.struct, {add_constant(tag)}, {pos}, {rw}),\n"
                )
        elif type == '"Enum"':
            assert items != None
            file.write(
                f"GeckoEnumStructAccessor(self.struct, {add_constant(tag)}, {pos}, {bitpos}, {items}, {size}, {maxitems}, {rw}),\n"
            )
        elif type == '"Time"':
            assert items == None
            assert size == None
            assert bitpos == None
            assert maxitems == None
            file.write(
                f"GeckoTimeStructAccessor(self.struct, {add_constant(tag)}, {pos}, {rw}),\n"
            )
        else:
            file.write(
                f"GeckoStructAccessor(self.struct, {add_constant(tag)}, {pos}, {type}, {bitpos}, {items}, {size}, {maxitems}, {rw}),\n"
            )

    file.write("        }\n")


def write_output_keys(file, xml):
    file.write("\n")
    file.write("    @property\n")
    file.write("    def output_keys(self):\n")
    file.write(f"        return {xml.attrib['AllOutputs']}\n")


def write_all_device_keys(file, xml):
    file.write("\n")
    file.write("    @property\n")
    file.write("    def all_device_keys(self):\n")
    file.write(f"        return {xml.attrib['AllDevices']}\n")


def write_user_demand_keys(file, xml):
    file.write("\n")
    file.write("    @property\n")
    file.write("    def user_demand_keys(self):\n")
    file.write(f"        return {xml.attrib['UserDemands']}\n")


def write_error_keys(file, xml):
    file.write("\n")
    file.write("    @property\n")
    file.write("    def error_keys(self):\n")
    file.write(f"        return {xml.attrib['ErrorMessages']}\n")


def build_log_struct(plateform_name, logstruct):
    reset_constants()
    generate_accessor_constants(logstruct)
    module = f"{CODE_PATH}/{plateform_name.lower()}-log-{logstruct.attrib['LibRev']}.py"
    with open(module, "w") as file:
        write_log_preamble(file, plateform_name, logstruct)
        write_all_device_keys(file, logstruct)
        write_user_demand_keys(file, logstruct)
        write_error_keys(file, logstruct)
        write_get_accessors(file, logstruct)


def build_config_struct(plateform_name, configstruct):
    reset_constants()
    generate_accessor_constants(configstruct)
    module = (
        f"{CODE_PATH}/{plateform_name.lower()}-cfg-{configstruct.attrib['LibRev']}.py"
    )
    with open(module, "w") as file:
        write_cfg_preamble(file, plateform_name, configstruct)
        write_output_keys(file, configstruct)
        write_get_accessors(file, configstruct)


def build_plateform(plateform, version):
    segment = plateform.attrib["Segment"]
    if not segment == "aMainControl":
        return

    plateform_name = plateform.attrib["Name"]

    # Create path for pack code modules
    if not os.path.exists(CODE_PATH):
        os.mkdir(CODE_PATH)

    with open(CODE_PATH + "/__init__.py", "w") as fs:
        write_module_init(fs)

    module = f"{CODE_PATH}/{plateform_name.lower()}.py"
    with open(module, "w") as file:
        write_pack_preamble(file, plateform_name, plateform.attrib["Type"], version)

        for logstruct in plateform.findall("./LogStructures/LogStructure"):
            build_log_struct(plateform_name, logstruct)
        for configstruct in plateform.findall("./ConfigStructures/ConfigStructure"):
            build_config_struct(plateform_name, configstruct)


def build_pack_code():
    spa_pack = ET.parse(XML_FILE)

    # Get struct version
    version = f'"{spa_pack.find("./SpaPackStruct/FileRevision").attrib["Number"]}"'
    print(f"Spa Pack Struct version {version} being used to generate code")

    # For each platform, generate code for it
    for plateform in spa_pack.findall("./Plateform"):
        build_plateform(plateform, version)


if __name__ == "__main__":
    build_pack_code()

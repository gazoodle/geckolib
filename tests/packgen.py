"""PackGen - A tool to generate .py files to interface with different Gecko packs."""  # noqa: INP001

import xml.etree.ElementTree as ET
from io import TextIOWrapper
from pathlib import Path
from typing import Any

# The XML file to process
XML_FILE = "../src/geckolib/SpaPackStruct_39.0.0.0.xml"

CODE_PATH = "../src/geckolib/driver/packs"

ACCESSOR_IMPORTED_CLASSES = [
    "GeckoBoolStructAccessor",
    "GeckoByteStructAccessor",
    "GeckoEnumStructAccessor",
    "GeckoStructAccessor",
    "GeckoTempStructAccessor",
    "GeckoTimeStructAccessor",
    "GeckoWordStructAccessor",
]

STRUCT_IMPORTED_CLASES = ["GeckoAsyncStructure"]

IMPORTED_CLASSES = ACCESSOR_IMPORTED_CLASSES + STRUCT_IMPORTED_CLASES
IMPORTED_CLASSES.sort()

OBFUSCATE_CONSTANTS = False
OBFUSCATE_STRINGS = False
OBFUSCATE_LISTS = False
USE_LOGGING = False

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


class PackGenerator:
    """Class to wrap pack generator."""

    def __init__(self) -> None:
        """Initialize the class."""
        self.module_constants = {}

    def write_module_init(self, file: TextIOWrapper) -> None:
        """Write a module inititalization file."""
        file.write('"""Pack Module Initialization."""\n\n')
        file.write(
            f"from geckolib.driver.accessor import {', '.join(ACCESSOR_IMPORTED_CLASSES)}\n"  # noqa: E501
        )
        file.write(
            "from geckolib.driver.async_spastruct import GeckoAsyncStructure\n\n"
        )
        file.write(f"__all__ = {IMPORTED_CLASSES}\n")

    def write_pack_preamble(
        self,
        file: TextIOWrapper,
        plateform_name: str,
        plateform_type: str,
        plateform_segment: str,
        version: str,
    ) -> None:
        """Write the preamble for this class."""
        file.write('"""')
        file.write(f"GeckoPack - A class to manage the pack for '{plateform_name}'")
        file.write('.""" # noqa: N999\n')
        file.write("\n")
        file.write("from . import GeckoAsyncStructure\n")
        file.write("\n")
        file.write("class GeckoPack:\n")
        file.write('    """A GeckoPack class for a specific spa."""\n')
        file.write("\n")
        file.write("    def __init__(self, struct_:GeckoAsyncStructure) -> None:\n")
        file.write('        """Initialize the GeckoPack class."""\n')
        file.write("        self.struct = struct_\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def name(self) -> str:\n")
        file.write('        """Get the plateform name."""\n')
        file.write(f"        return '{plateform_name}'\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def plateform_type(self) -> int:\n")
        file.write('        """Get the plateform type."""\n')
        file.write(f"        return {plateform_type}\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def plateform_segment(self) -> str:\n")
        file.write('        """Get the plateform segment."""\n')
        file.write(f"        return '{plateform_segment}'\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def revision(self) -> str:\n")
        file.write('        """Get the SpaPackStruct revision."""\n')
        file.write(f"        return {version}\n")

    def write_import(self, file: TextIOWrapper) -> None:
        """Write the import lines."""
        if USE_LOGGING:
            file.write("import logging\n\n")
        file.write(f"from . import {', '.join(IMPORTED_CLASSES)}\n")
        file.write("\n")
        if USE_LOGGING:
            file.write("_LOGGER = logging.getLogger(__name__)\n")

    def gen_uniq_key(
        self,
    ) -> str:
        """Generaate unique key."""
        candidate_key = KEY_GEN_STRING[
            len(self.module_constants) : len(self.module_constants) + 6
        ]
        if candidate_key not in self.module_constants:
            return candidate_key
        msg = f"Ooops! at {len(self.module_constants)} with key '{candidate_key}'"
        raise KeyError(msg)

    def add_constant(self, val: Any) -> Any:
        """Add a constant to the module constants returning the key."""
        if OBFUSCATE_LISTS and isinstance(val, list):
            val = [self.add_constant(f'"{item}"') for item in val]

        # Do we already have this value stashed ?
        for var in self.module_constants:
            if self.module_constants[var] == val:
                return var if OBFUSCATE_CONSTANTS else self.module_constants[var]

        # Otherwise stash it
        key = self.gen_uniq_key()
        self.module_constants[key] = val
        return key if OBFUSCATE_CONSTANTS else val

    def reset_constants(
        self,
    ) -> None:
        """Reset the module constants to nothing."""
        self.module_constants = {}

    def write_constant_value(self, file: TextIOWrapper, val: Any) -> None:
        """Write the constant value, or obfuscate it if needed."""
        if OBFUSCATE_STRINGS and isinstance(val, str) and val.startswith('"'):
            file.write(f"''.join(chr(c) for c in {[ord(ch) for ch in val[1:-1]]})\n")
        elif OBFUSCATE_LISTS and isinstance(val, list):
            file.write(f"[{', '.join(val)}]\n")
        else:
            file.write(f"{val}\n")

    def write_constants(self, file: TextIOWrapper) -> None:
        """Write the module constants."""
        if len(self.module_constants) == 0:
            return
        if not OBFUSCATE_CONSTANTS:
            return
        file.write("# Constants for this class\n")
        for var in sorted(self.module_constants):
            val = self.module_constants[var]
            if OBFUSCATE_LISTS and isinstance(val, list):
                continue
            file.write(f"{var} = ")
            self.write_constant_value(file, self.module_constants[var])
        if OBFUSCATE_LISTS:
            # Now the lists
            for var in sorted(self.module_constants):
                val = self.module_constants[var]
                if not isinstance(val, list):
                    continue
                file.write(f"{var} = ")
                self.write_constant_value(file, self.module_constants[var])

        file.write("\n")

    def write_log_preamble(
        self, file: TextIOWrapper, plateform_name: str, logstruct: ET.Element
    ) -> None:
        """Write the log file preamble."""
        file.write('"""')
        file.write(
            f"GeckoLogStruct - A class to manage the LogStruct for '{plateform_name}"
            f" v{logstruct.attrib['LibRev']}'"
        )
        file.write('."""')
        file.write(" # noqa: N999\n")
        file.write("\n\n")
        self.write_import(file)

        logstruct.attrib["LibRev"] = self.add_constant(int(logstruct.attrib["LibRev"]))
        logstruct.attrib["Begin"] = self.add_constant(int(logstruct.attrib["Begin"]))
        logstruct.attrib["End"] = self.add_constant(int(logstruct.attrib["End"]))

        self.write_constants(file)
        file.write("\n")
        file.write("class GeckoLogStruct:\n")
        file.write('    """Log Struct Class."""\n')
        file.write("\n")
        file.write("    def __init__(self, struct_:GeckoAsyncStructure) -> None:\n")
        file.write('        """Initialize the log struct class."""\n')
        file.write("        self.struct = struct_\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def version(self) -> int:\n")
        file.write('        """Get the log struct class version."""\n')
        file.write(f"        return {logstruct.attrib['LibRev']}\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def begin(self) -> int:\n")
        file.write('        """Get the offset start."""\n')
        file.write(f"        return {logstruct.attrib['Begin']}\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def end(self) -> int:\n")
        file.write('        """Get the offset end."""\n')
        file.write(f"        return {logstruct.attrib['End']}\n")

    def write_cfg_preamble(
        self, file: TextIOWrapper, plateform_name: str, configstruct: ET.Element
    ) -> None:
        """Write a config structure class."""
        file.write('"""')
        file.write(
            f"GeckoConfigStruct - A class to manage the ConfigStruct for"
            f" '{plateform_name} v{configstruct.attrib['LibRev']}'"
        )
        file.write('."""')
        file.write(" # noqa: N999")
        file.write("\n\n")
        self.write_import(file)

        configstruct.attrib["LibRev"] = self.add_constant(
            int(configstruct.attrib["LibRev"])
        )

        self.write_constants(file)
        file.write("\n")
        file.write("class GeckoConfigStruct:\n")
        file.write('    """Config Struct Class."""\n')
        file.write("\n")
        file.write("    def __init__(self, struct_:GeckoAsyncStructure) -> None:\n")
        file.write('        """Initialize the config struct class."""\n')
        file.write("        self.struct = struct_\n")
        file.write("\n")
        file.write("    @property\n")
        file.write("    def version(self) -> int:\n")
        file.write('        """Get the config struct class version."""\n')
        file.write(f"        return {configstruct.attrib['LibRev']}\n")

    def generate_accessor_constants(self, xml: ET.Element) -> None:
        """Generate all the accessor constants."""
        for element in xml.findall(".//*[@Pos]"):
            self.add_constant(f'"{element.tag}"')
            element.attrib["Pos"] = self.add_constant(element.attrib["Pos"])
            if "Items" in element.attrib:
                items = element.attrib["Items"].split("|")
                element.attrib["Items"] = self.add_constant(items)
            if "Item" in element.attrib:
                items = element.attrib["Item"].split("|")
                element.attrib["Item"] = self.add_constant(items)
            if "BitPos" in element.attrib:
                element.attrib["BitPos"] = self.add_constant(
                    int(element.attrib["BitPos"])
                )
            if "Size" in element.attrib:
                element.attrib["Size"] = self.add_constant(int(element.attrib["Size"]))
            if "MaxItems" in element.attrib:
                element.attrib["MaxItems"] = self.add_constant(
                    int(element.attrib["MaxItems"])
                )
            if "RW" in element.attrib:
                element.attrib["RW"] = self.add_constant(f'"{element.attrib["RW"]}"')

        output_paths = [
            './HCOutputConfig/*[@Type="Enum"]',
            './LCOutputConfig/*[@Type="Enum"]',
            './LVOutputConfig/*[@Type="Enum"]',
        ]

        all_outputs = [
            element.tag for xpath in output_paths for element in xml.findall(xpath)
        ]

        xml.attrib["AllOutputs"] = self.add_constant(all_outputs)

        all_devices = [element.tag for element in xml.findall("./DeviceStatus/*")] + [
            "LI"
        ]
        xml.attrib["AllDevices"] = self.add_constant(all_devices)

        user_demands = [
            element.tag
            for element in xml.findall("./UserDemands/*")
            if element.tag.startswith("Ud")
        ]
        xml.attrib["UserDemands"] = self.add_constant(user_demands)

        # Errors are all properties in the <ErrorMessages> tag,
        # anything with Err in the name
        known_err_tags = ["OverTemp", "TempNotValid", "SlaveOverTemp"]
        errors = [element.tag for element in xml.findall("./ErrorMessages/*")] + [
            element.tag
            for element in xml.findall(".//*")
            if element.tag.endswith("Err") or element.tag in known_err_tags
        ]
        errors = list(set(errors))  # Dedupe
        errors.sort()
        xml.attrib["ErrorMessages"] = self.add_constant(errors)

    def _write_one_accessor(
        self, file: TextIOWrapper, path: str, element: ET.Element
    ) -> None:
        tag = f'"{element.tag}"'
        pos = element.attrib["Pos"]
        accessor_type = f'"{element.attrib["Type"]}"'
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

        file.write(f"            {self.add_constant(tag)}: ")
        if accessor_type == '"Byte"':
            file.write(
                f"GeckoByteStructAccessor(self.struct, {self.add_constant(path)}, {pos}, {rw}),\n"  # noqa: E501
            )
        elif accessor_type == '"Bool"':
            # In inxm-log-4 & in-xml-log-5 it is 2, but this is wrong
            if OBFUSCATE_CONSTANTS:
                assert size is None or self.module_constants[size] == 2  # noqa: PLR2004, S101
            else:
                assert size in (None, 2)  # noqa: S101
            file.write(
                f"GeckoBoolStructAccessor(self.struct, {self.add_constant(path)}, {pos}, {bitpos}, {rw}),\n"  # noqa: E501
            )
        # MrStream log v3 has lowercase "word"
        elif accessor_type in ('"Word"', '"word"'):
            if "temp" in element.tag.lower() or "setpoint" in element.tag.lower():
                file.write(
                    f"GeckoTempStructAccessor(self.struct, {self.add_constant(path)}, {pos}, {rw}),\n"  # noqa: E501
                )
            else:
                file.write(
                    f"GeckoWordStructAccessor(self.struct, {self.add_constant(path)}, {pos}, {rw}),\n"  # noqa: E501
                )
        elif accessor_type == '"Enum"':
            file.write(
                f"GeckoEnumStructAccessor(self.struct, {self.add_constant(path)}, {pos}, {bitpos}, {items}, {size}, {maxitems}, {rw}),\n"  # noqa: E501
            )
        elif accessor_type == '"Time"':
            file.write(
                f"GeckoTimeStructAccessor(self.struct, {self.add_constant(path)}, {pos}, {rw}),\n"  # noqa: E501
            )
        else:
            file.write(
                f"GeckoStructAccessor(self.struct, {self.add_constant(tag)}, {pos}, {type}, {bitpos}, {items}, {size}, {maxitems}, {rw}),\n"  # noqa: E501
            )

    def write_get_accessors(self, file: TextIOWrapper, xml: ET.Element) -> None:  # noqa: PLR0912, PLR0915
        """Write the accessors for the spa pack structure."""
        file.write("\n")
        file.write("    @property\n")
        file.write("    def accessors(self) -> dict[str, GeckoStructAccessor]:\n")
        file.write('        """The structure accessors."""\n')
        if USE_LOGGING:
            file.write("        _LOGGER.info('Getting expensive accessors')\n")
        file.write("        return {\n")
        for parent in xml.findall("./*"):
            if "Pos" in parent.attrib:
                path = f'"{xml.tag}/{parent.tag}"'
                self._write_one_accessor(file, path, parent)

            for element in parent.findall("./*[@Pos]"):
                if element.tag.startswith("CFG"):
                    continue

                path = f'"{xml.tag}/{parent.tag}/{element.tag}"'
                self._write_one_accessor(file, path, element)

        file.write("        }\n")

    def write_output_keys(self, file: TextIOWrapper, xml: ET.Element) -> None:
        """Write the keys for the detected output modules into the class."""
        file.write("\n")
        file.write("    @property\n")
        file.write("    def output_keys(self) -> list[str]:\n")
        file.write('        """Output keys property."""\n')
        file.write(f"        return {xml.attrib['AllOutputs']}\n")

    def write_all_device_keys(self, file: TextIOWrapper, xml: ET.Element) -> None:
        """Write the all device keys property."""
        file.write("\n")
        file.write("    @property\n")
        file.write("    def all_device_keys(self) -> list[str]:\n")
        file.write('        """Get all device keys."""\n')
        file.write(f"        return {xml.attrib['AllDevices']}\n")

    def write_user_demand_keys(self, file: TextIOWrapper, xml: ET.Element) -> None:
        """Write the user demand keys property."""
        file.write("\n")
        file.write("    @property\n")
        file.write("    def user_demand_keys(self) -> list[str]:\n")
        file.write('        """Get all user demand keys."""\n')
        file.write(f"        return {xml.attrib['UserDemands']}\n")

    def write_error_keys(self, file: TextIOWrapper, xml: ET.Element) -> None:
        """Write error keys propoerty."""
        file.write("\n")
        file.write("    @property\n")
        file.write("    def error_keys(self) -> list[str]:\n")
        file.write('        """Get all error keys."""\n')
        file.write(f"        return {xml.attrib['ErrorMessages']}\n")

    def build_log_struct(
        self, plateform_name: str, _plateform: ET.Element, logstruct: ET.Element
    ) -> None:
        """Build log structure."""
        self.reset_constants()
        self.generate_accessor_constants(logstruct)
        module = (
            f"{CODE_PATH}/{plateform_name.lower()}-log-{logstruct.attrib['LibRev']}.py"
        )
        with Path(module).open("w") as file:
            self.write_log_preamble(file, plateform_name, logstruct)
            self.write_all_device_keys(file, logstruct)
            self.write_user_demand_keys(file, logstruct)
            self.write_error_keys(file, logstruct)
            self.write_get_accessors(file, logstruct)

    def build_config_struct(
        self, plateform_name: str, _plateform: ET.Element, configstruct: ET.Element
    ) -> None:
        """Build configuration structure."""
        self.reset_constants()
        self.generate_accessor_constants(configstruct)
        module = f"{CODE_PATH}/{plateform_name.lower()}-cfg-{configstruct.attrib['LibRev']}.py"  # noqa: E501
        with Path(module).open("w") as file:
            self.write_cfg_preamble(file, plateform_name, configstruct)
            self.write_output_keys(file, configstruct)
            self.write_get_accessors(file, configstruct)

    def build_plateform(self, plateform: ET.Element, version: str) -> None:
        """Build Plateform files."""
        segment = plateform.attrib["Segment"]
        # if segment != "aMainControl":
        #   return

        plateform_name = plateform.attrib["Name"]

        # Create path for pack code modules
        if not Path(CODE_PATH).exists():
            Path(CODE_PATH).mkdir()

        with Path(CODE_PATH + "/__init__.py").open("w") as file:
            self.write_module_init(file)

        module = f"{CODE_PATH}/{plateform_name.lower()}.py"
        with Path(module).open("w") as file:
            self.write_pack_preamble(
                file,
                plateform_name,
                plateform.attrib["Type"],
                plateform.attrib["Segment"],
                version,
            )

            for logstruct in plateform.findall("./LogStructures/LogStructure"):
                self.build_log_struct(plateform_name, plateform, logstruct)
            for configstruct in plateform.findall("./ConfigStructures/ConfigStructure"):
                self.build_config_struct(plateform_name, plateform, configstruct)

    def build_pack_code(self) -> None:
        """Build all the code from the SpaPackStruct.xml file."""
        spa_pack = ET.parse(XML_FILE)  # noqa: S314

        # Get struct version
        version_element = spa_pack.find("./SpaPackStruct/FileRevision")
        if version_element is None:
            raise SyntaxError
        version = f'"{version_element.attrib["Number"]}"'
        print(f"Spa Pack Struct version {version} being used to generate code")  # noqa: T201

        # For each platform, generate code for it
        for plateform in spa_pack.findall("./Plateform"):
            self.build_plateform(plateform, version)


if __name__ == "__main__":
    pg = PackGenerator()
    pg.build_pack_code()

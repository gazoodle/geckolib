""" Constants Class """


class GeckoConstants:
    """
    GeckoConstants is a literal class so that we can program in a mostly DRY fashion,
    for example a filename or url would be present as would values that could be changed
    and might be difficult to discover inline, but some constants that form part of a functions
    documented behaviour might not be here, e.g. 'rw' as a parameter to open()
    """

    INCLUDE_DUMMY_SPA = False
    INTOUCH2_PORT = 10022
    MAX_PACKET_SIZE = 8192
    DISCOVERY_TIMEOUT_IN_SECONDS = 4
    DISCOVERY_RETRY_COUNT_TO_FIND_ANY_SPA = 3
    PING_TIMEOUT_IN_SECONDS = 4
    PING_FREQUENCY_IN_SECONDS = 15

    BROADCAST_ADDRESS = "255.255.255.255"
    MESSAGE_ENCODING = "latin1"
    FORMAT_CLIENT_IDENTIFIER = "IOS{0}"

    SPA_PACK_STRUCT_FILE = "SpaPackStruct.xml"
    SPA_PACK_STRUCT_URL = "http://intouch.geckoal.com/gecko/prod/SpaPackStruct.xml"
    # XPaths and attributes for SpaPackStruct
    SPA_PACK_REVISION_XPATH = "./SpaPackStruct/FileRevision"
    SPA_PACK_REVISION_ATTRIB = "Number"
    SPA_PACK_PLATEFORM_XPATH = "./Plateform"
    SPA_PACK_NAME_ATTRIB = "Name"
    SPA_PACK_CONFIG_XPATH = "./ConfigStructures/ConfigStructure[@LibRev='{0}']"
    SPA_PACK_LOG_XPATH = "./LogStructures/LogStructure[@LibRev='{0}']"
    SPA_PACK_STRUCT_POS_ATTRIB = "Pos"
    SPA_PACK_STRUCT_TYPE_ATTRIB = "Type"
    SPA_PACK_STRUCT_BITPOS_ATTRIB = "BitPos"
    SPA_PACK_STRUCT_ITEMS_ATTRIB = "Items"
    SPA_PACK_STRUCT_SIZE_ATTRIB = "Size"
    SPA_PACK_STRUCT_WORD_TYPE = "Word"
    SPA_PACK_STRUCT_TIME_TYPE = "Time"
    SPA_PACK_STRUCT_MAXITEMS_ATTRIB = "MaxItems"
    SPA_PACK_STRUCT_BOOL_TYPE = "Bool"
    SPA_PACK_STRUCT_ENUM_TYPE = "Enum"
    SPA_PACK_STRUCT_POS_ELEMENTS_XPATH = ".//*[@Pos]"
    SPA_PACK_STRUCT_WORD_TYPE_ELEMENTS_XPATH = './/*[@Type="Word"]'
    SPA_PACK_STRUCT_BEGIN_ATTRIB = "Begin"
    SPA_PACK_STRUCT_END_ATTRIB = "End"
    SPA_PACK_STRUCT_READ_WRITE_ATTRIB = "RW"
    # Accessor keys for SpaPackStruct
    KEY_PACK_TYPE = "PackType"
    KEY_PACK_CONFIG_ID = "PackConfID"
    KEY_PACK_CONFIG_REV = "PackConfRev"
    KEY_PACK_CONFIG_REL = "PackConfRel"
    KEY_CONFIG_NUMBER = "ConfigNumber"
    KEY_TEMP_UNITS = "TempUnits"
    KEY_RH_WATER_TEMP = "RhWaterTemp"
    KEY_SETPOINT_G = "SetpointG"
    KEY_REAL_SETPOINT_G = "RealSetPointG"
    KEY_DISPLAYED_TEMP_G = "DisplayedTempG"
    KEY_PUMP_1 = "P1"
    KEY_PUMP_2 = "P2"
    KEY_PUMP_3 = "P3"
    KEY_PUMP_4 = "P4"
    KEY_PUMP_5 = "P5"
    KEY_BLOWER = "BL"

    KEY_USER_DEMAND_LIGHT = "UdLi"

    EXCEPTION_MESSAGE_NO_SPA_PACK = "Cannot find spa pack for {0}"
    EXCEPTION_MESSAGE_NOT_WRITABLE = (
        "Cannot set value for {0}. This status array item doesn't allow writing"
    )

    # Message pseudo xml parts
    MESSAGE_HELLO = "<HELLO>{0}</HELLO>"
    MESSAGE_PART_PACKET = "<PACKT>{0}</PACKT>"
    MESSAGE_PART_DATAS = "<DATAS>{0}</DATAS>"
    MESSAGE_PART_CONNECTION_NAMES = "<SRCCN>{0}</SRCCN><DESCN>{1}</DESCN>"

    # Command & response pseudo xml content
    REQUEST_AND_RESPONSE_PING = ("APING", b"APING")
    REQUEST_AND_RESPONSE_GET_VERSION = ("AVERS", b"SVERS")
    REQUEST_AND_RESPONSE_GET_CHANNEL = ("CURCH", b"CHCUR")
    REQUEST_AND_RESPONSE_GET_CONFIG = ("SFILE", b"FILES")
    REQUEST_AND_RESPONSE_GET_STATUS = ("STATU", b"STATV")
    REQUEST_AND_RESPONSE_PARTIAL_STATUS = ("STATQ", b"STATP")
    REQUEST_AND_RESPONSE_PACK_COMMAND = ("SPACK", b"PACKS")
    REQUEST_AND_RESPONSE_GET_ACTIVE_WATERCARE = ("GETWC", b"WCGET")
    REQUEST_AND_RESPONSE_SET_ACTIVE_WATERCARE = ("SETWC", b"WCSET")

    # Pack commands
    PACK_COMMAND_KEY_PRESS = 57
    PACK_COMMAND_SET_VALUE = 70

    # Gecko keypad constants
    KEYPAD_PUMP_1 = 1
    KEYPAD_PUMP_2 = 2
    KEYPAD_PUMP_3 = 3
    KEYPAD_PUMP_4 = 4
    KEYPAD_PUMP_5 = 5
    KEYPAD_BLOWER = 6
    KEYPAD_LIGHT = 16
    KEYPAD_UP = 21
    KEYPAD_DOWN = 22

    # Pack outputs
    PACK_OUTPUTS_XPATHS = [
        './HCOutputConfig/*[@Type="Enum"]',
        './LCOutputConfig/*[@Type="Enum"]',
        './LVOutputConfig/*[@Type="Enum"]',
    ]
    SPA_PACK_DEVICE_XPATH = "./DeviceStatus/*"
    SPA_PACK_USER_DEMANDS = "./UserDemands/*"

    DEVICE_CLASS_PUMP = "PUMP"
    DEVICE_CLASS_BLOWER = "BLOWER"
    DEVICE_CLASS_LIGHT = "LIGHT"

    # Spa devices and accessories, dictionary of tuples
    #   ID: Description, keypad, structure key, class
    DEVICES = {
        "P1": ("Pump 1", KEYPAD_PUMP_1, KEY_PUMP_1, DEVICE_CLASS_PUMP),
        "P2": ("Pump 2", KEYPAD_PUMP_2, KEY_PUMP_2, DEVICE_CLASS_PUMP),
        "P3": ("Pump 3", KEYPAD_PUMP_3, KEY_PUMP_3, DEVICE_CLASS_PUMP),
        "P4": ("Pump 4", KEYPAD_PUMP_4, KEY_PUMP_4, DEVICE_CLASS_PUMP),
        "P5": ("Pump 5", KEYPAD_PUMP_5, KEY_PUMP_5, DEVICE_CLASS_PUMP),
        "BL": ("Blower", KEYPAD_BLOWER, KEY_BLOWER, DEVICE_CLASS_BLOWER),
        "LI": ("Lights", KEYPAD_LIGHT, KEY_USER_DEMAND_LIGHT, DEVICE_CLASS_LIGHT),
    }

    # Buttons, list of tuples
    #   ID, Description, KeyPad ID
    BUTTONS = [
        ("P1", "Pump 1 Button", KEYPAD_PUMP_1),
        ("P2", "Pump 2 Button", KEYPAD_PUMP_2),
        ("P3", "Pump 3 Button", KEYPAD_PUMP_3),
        ("P4", "Pump 4 Button", KEYPAD_PUMP_4),
        ("P5", "Pump 5 Button", KEYPAD_PUMP_5),
        ("BLOWER", "Blower Button", KEYPAD_BLOWER),
        ("LIGHT", "Lights Button", KEYPAD_LIGHT),
        ("UP", "Up Button", KEYPAD_UP),
        ("DOWN", "Down Button", KEYPAD_DOWN),
    ]

    REGEX_DOT_STAR = "(.*)"

    WATERCARE_MODE = (
        AwayFromHome,
        Standard,
        EnergySaving,
        SuperEnergySaving,
        Weekender,
    ) = range(5)

    WATERCARE_MODE_STRING = [
        "Away From Home",
        "Standard",
        "Energy Saving",
        "Super Energy Saving",
        "Weekender",
    ]
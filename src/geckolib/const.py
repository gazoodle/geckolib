""" Constants Class """


class GeckoConstants:
    """
    GeckoConstants is a literal class so that we can program in a mostly DRY fashion,
    for example a filename or url would be present as would values that could be changed
    and might be difficult to discover inline, but some constants that form part of a
    functions documented behaviour might not be here, e.g. 'rw' as a parameter to open()
    """

    INCLUDE_DUMMY_SPA = False
    INTOUCH2_PORT = 10022
    MAX_PACKET_SIZE = 8192
    # Mininum time to wait for initial spa discovery even if one spa has responded
    DISCOVERY_INITIAL_TIMEOUT_IN_SECONDS = 4
    # Maximum time to wait for full discovery if no spas have responded
    DISCOVERY_TIMEOUT_IN_SECONDS = 10
    # Maximum time to wait for full connection for a responding spa
    CONNECTION_TIMEOUT_IN_SECONDS = 30
    PING_TIMEOUT_IN_SECONDS = 4
    PING_FREQUENCY_IN_SECONDS = 15
    PING_DEVICE_NOT_RESPONDING_TIMEOUT = 60
    FACADE_UPDATE_FREQUENCY_IN_SECONDS = 30

    BROADCAST_ADDRESS = "<broadcast>"
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
    KEY_HEATING = "Heating"
    KEY_COOLINGDOWN = "CoolingDown"
    KEY_PUMP_1 = "P1"
    KEY_PUMP_2 = "P2"
    KEY_PUMP_3 = "P3"
    KEY_PUMP_4 = "P4"
    KEY_PUMP_5 = "P5"
    KEY_BLOWER = "BL"
    KEY_WATERFALL = "Waterfall"
    KEY_CIRCULATING_PUMP = "CP"
    KEY_OZONE = "O3"
    KEY_SMW_ACTIVE = "SwmActive"
    KEY_SWM_RISK = "SwmRisk"
    KEY_FILTER_PURGE = "Purge"
    KEY_FILTER_CLEAN = "Clean"

    KEY_USER_DEMAND_LIGHT = "UdLi"

    EXCEPTION_MESSAGE_NO_SPA_PACK = "Cannot find spa pack for {0}"
    EXCEPTION_MESSAGE_NOT_WRITABLE = (
        "Cannot set value for {0}. This status array item doesn't allow writing"
    )

    # Water heater status
    WATER_HEATER_HEATING = "Heating"
    WATER_HEATER_COOLING = "Cooling"
    WATER_HEATER_IDLE = "Idle"

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
    KEYPAD_WATERFALL = 23

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
    DEVICE_CLASS_OTHER = "OTHER"

    # Spa devices and accessories, dictionary of tuples
    #   ID: Description, keypad, structure key, class
    DEVICES = {
        "P1": ("Pump 1", KEYPAD_PUMP_1, KEY_PUMP_1, DEVICE_CLASS_PUMP),
        "P2": ("Pump 2", KEYPAD_PUMP_2, KEY_PUMP_2, DEVICE_CLASS_PUMP),
        "P3": ("Pump 3", KEYPAD_PUMP_3, KEY_PUMP_3, DEVICE_CLASS_PUMP),
        "P4": ("Pump 4", KEYPAD_PUMP_4, KEY_PUMP_4, DEVICE_CLASS_PUMP),
        "P5": ("Pump 5", KEYPAD_PUMP_5, KEY_PUMP_5, DEVICE_CLASS_PUMP),
        "BL": ("Blower", KEYPAD_BLOWER, KEY_BLOWER, DEVICE_CLASS_BLOWER),
        "Waterfall": ("Waterfall", KEYPAD_WATERFALL, KEY_WATERFALL, DEVICE_CLASS_PUMP),
        "LI": ("Lights", KEYPAD_LIGHT, KEY_USER_DEMAND_LIGHT, DEVICE_CLASS_LIGHT),
    }

    BINARY_SENSORS = [
        (
            "Circulating Pump",
            KEY_CIRCULATING_PUMP,
            DEVICE_CLASS_PUMP,
        ),
        ("Pump Run", "PumpRun", DEVICE_CLASS_PUMP),
        ("Ozone", KEY_OZONE, DEVICE_CLASS_OTHER),
        ("Smart Winter Mode:Active", KEY_SMW_ACTIVE, DEVICE_CLASS_OTHER),
        ("Filter Status:Clean", KEY_FILTER_CLEAN, DEVICE_CLASS_OTHER),
        ("Filter Status:Purge", KEY_FILTER_PURGE, DEVICE_CLASS_OTHER),
    ]

    SENSORS = [("Smart Winter Mode:Risk", KEY_SWM_RISK)]

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

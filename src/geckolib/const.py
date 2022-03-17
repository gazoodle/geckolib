""" Constants Class """


class GeckoConstants:
    """
    GeckoConstants is a literal class so that we can program in a mostly DRY fashion,
    for example a filename or url would be present as would values that could be changed
    and might be difficult to discover inline, but some constants that form part of a
    functions documented behaviour might not be here, e.g. 'rw' as a parameter to open()
    """

    INTOUCH2_PORT = 10022
    # Maximum time to wait for full connection for a responding spa
    CONNECTION_TIMEOUT_IN_SECONDS = 45

    CONNECTION_STEP_PAUSE_IN_SECONDS = 0  # Time between connection steps
    MAX_RF_ERRORS_BEFORE_HALT = 50
    ASYNCIO_SLEEP_TIMEOUT_FOR_YIELD = 0.001

    BROADCAST_ADDRESS = "<broadcast>"
    MESSAGE_ENCODING = "latin1"
    FORMAT_CLIENT_IDENTIFIER = "IOS{0}"

    # XPaths and attributes for SpaPackStruct
    SPA_PACK_STRUCT_BYTE_TYPE = "Byte"
    SPA_PACK_STRUCT_WORD_TYPE = "Word"
    SPA_PACK_STRUCT_TIME_TYPE = "Time"
    SPA_PACK_STRUCT_BOOL_TYPE = "Bool"
    SPA_PACK_STRUCT_ENUM_TYPE = "Enum"
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
    KEY_ECON_ACTIVE = "EconActive"

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
    KEYPAD_ECOMODE = 0

    # Pack outputs
    DEVICE_CLASS_PUMP = "PUMP"
    DEVICE_CLASS_BLOWER = "BLOWER"
    DEVICE_CLASS_LIGHT = "LIGHT"
    DEVICE_CLASS_SWITCH = "SWITCH"
    DEVICE_CLASS_OTHER = "OTHER"

    ECON_ACTIVE_DESCRIPTION = "Economy Mode"

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

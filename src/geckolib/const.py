"""Constants Class."""


class GeckoConstants:
    """
    All the constants in one place.

    GeckoConstants is a literal class so that we can program in a mostly DRY fashion,
    for example a filename or url would be present as would values that could be changed
    and might be difficult to discover inline, but some constants that form part of a
    functions documented behaviour might not be here, e.g. 'rw' as a parameter to open()
    """

    INTOUCH2_PORT = 10022
    # Maximum time to wait for full connection for a responding spa
    CONNECTION_TIMEOUT_IN_SECONDS = 45
    # Async Locator sleep times
    ASYNC_LOCATOR_BROADCAST_SLEEP = 1
    # Simulator min time between responses to broadcast <HELLO>
    SIMULATOR_MIN_TIME_BETWEEN_HELLO_BROADCAST_RESPONSES = 1

    CONNECTION_STEP_PAUSE_IN_SECONDS = None  # Time between connection steps
    MAX_RF_ERRORS_BEFORE_HALT = 50

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
    KEY_PACK_CORE_ID = "PackCoreID"
    KEY_PACK_CORE_REV = "PackCoreRev"
    KEY_PACK_CORE_REL = "PackCoreRel"
    KEY_CONFIG_NUMBER = "ConfigNumber"
    KEY_TEMP_UNITS = "TempUnits"
    KEY_RH_WATER_TEMP = "RhWaterTemp"
    KEY_SETPOINT_G = "SetpointG"
    KEY_REAL_SETPOINT_G = "RealSetPointG"
    KEY_DISPLAYED_TEMP_G = "DisplayedTempG"
    KEY_HEATING = "Heating"
    KEY_COOLINGDOWN = "CoolingDown"
    KEY_TEMP_NOT_VALID = "TempNotValid"
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
    KEY_INGRID_DETECTED = "InGridDetected"
    KEY_MODBUS_HEATPUMP_DETECTED = "ModbusHeatPumpDetected"
    KEY_COOLZONE_DETECTED = "CoolZoneDetected"
    KEY_COOLZONE_MODE = "CoolZoneMode"
    KEY_LOCKMODE = "LockMode"
    KEY_STANDBY = "QuietState"

    KEY_MRSTEAM_USER_MODE = "UserMode"
    KEY_MRSTEAM_USER_AROMA = "UserAroma"
    KEY_MRSTEAM_USER_CHROMA = "UserChroma"
    KEY_MRSTEAM_USER_SETPOINT_G = "UserSetpointG"
    KEY_MRSTEAM_USER_RUNTIME = "UserRuntime"

    KEY_MRSTEAM_HEATER_OUTPUT = "HeaterOutput"
    KEY_MRSTEAM_AROMA_OUTPUT = "AromaOutput"
    KEY_MRSTEAM_CHROMA_OUTPUT = "ChromaOutput"
    KEY_MRSTEAM_REMAINING_RUNTIME = "RemainingRuntime"
    KEY_MRSTEAM_MAX_RUNTIME = "MaxRuntime"

    KEY_MIN_SETPOINT_G = "MinSetpointG"
    KEY_MAX_SETPOINT_G = "MaxSetpointG"

    KEY_USER_DEMAND_LIGHT = "UdLi"

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
    KEYPAD_LIGHT_120 = 17
    KEYPAD_UP = 21
    KEYPAD_DOWN = 22
    KEYPAD_WATERFALL = 23
    KEYPAD_AUX = 24
    KEYPAD_ECOMODE = 0

    # Pack outputs
    DEVICE_CLASS_PUMP = "PUMP"
    DEVICE_CLASS_BLOWER = "BLOWER"
    DEVICE_CLASS_LIGHT = "LIGHT"
    DEVICE_CLASS_SWITCH = "SWITCH"
    DEVICE_CLASS_OTHER = "OTHER"

    ECON_ACTIVE_DESCRIPTION = "Economy Mode"

    BINARY_SENSORS = [  # noqa: RUF012
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
        ("Heating", KEY_HEATING, DEVICE_CLASS_OTHER),
    ]

    SENSORS = [("Smart Winter Mode:Risk", KEY_SWM_RISK)]  # noqa: RUF012

    WATERCARE_MODE = (
        AwayFromHome,
        Standard,
        EnergySaving,
        SuperEnergySaving,
        Weekender,
    ) = range(5)

    WATERCARE_MODE_STRING = [  # noqa: RUF012
        "Away From Home",
        "Standard",
        "Energy Saving",
        "Super Energy Saving",
        "Weekender",
    ]

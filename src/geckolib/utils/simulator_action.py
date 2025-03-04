"""Simulator action class."""

# ruff: noqa: N802

import logging
from typing import Any

_LOGGER = logging.getLogger(__name__)


class GeckoSimulatorAction:
    """Define the action for various simulator events."""

    def set_connections(self, connections: list[str]) -> None:
        """Set the internal connections variable."""
        self._connections = connections

    ############################################################################
    #
    #               The accessors that we want to interact with
    #
    # User demands
    UdP1: Any
    UdVSP1: Any
    UdP2: Any
    UdP3: Any
    UdVSP3: Any
    UdP4: Any
    UdP5: Any
    UdBL: Any
    UdWaterfall: Any
    UdAux: Any
    UdLi: Any
    UdL120: Any
    UdQuietTime: Any
    SetpointG: Any

    # Mr.Steam
    UserMode: Any
    HeaterOutput: Any
    UserAroma: Any
    AromaOutput: Any
    UserChroma: Any
    ChromaOutput: Any

    # Support accessors
    P1: Any
    P2: Any
    P3: Any
    P4: Any
    P5: Any
    BL: Any
    Waterfall: Any
    L120: Any
    CP: Any
    QuietState: Any
    EconActive: Any

    # Water heater
    DisplayedTempG: Any
    RealSetPointG: Any
    MSTR_HEATER: Any
    Heating: Any
    HeaterPump: Any
    TempUnits: Any
    UserRuntime: Any
    RemainingRuntime: Any

    # Utility accessors
    CheckFlo: Any
    UdPumpTime: Any
    UdWaterFallTime: Any
    UdAuxTime: Any
    UdLightTime: Any
    UdL120Time: Any

    Pump1AsVSP: Any
    Pump3AsVSP: Any
    WaterfallAsCP: Any

    _connections: list[str]

    ############################################################################
    #
    #               The keypad buttons we want to handle
    #
    def on_KEYPAD_PUMP_1(self) -> None:
        """Handle keypad pump 1."""
        if self.Pump1AsVSP:
            self.UdVSP1 = self._next_pump_value(self.UdVSP1, vsp=True)
        else:
            self.UdP1 = self._next_pump_value(self.UdP1, "P1L")

    def on_KEYPAD_PUMP_2(self) -> None:
        """Handle keypad pump 2."""
        self.UdP2 = self._next_pump_value(self.UdP2, "P2L")

    def on_KEYPAD_PUMP_3(self) -> None:
        """Handle keypad pump 3."""
        if self.Pump3AsVSP:
            self.UdVSP3 = self._next_pump_value(self.UdVSP3, vsp=True)
        else:
            self.UdP3 = self._next_pump_value(self.UdP3, "P3L")

    def on_KEYPAD_PUMP_4(self) -> None:
        """Handle keypad pump 4."""
        self.UdP4 = self._next_pump_value(self.UdP4, "P4L")

    def on_KEYPAD_PUMP_5(self) -> None:
        """Handle keypad pump 5."""
        self.UdP5 = self._next_pump_value(self.UdP5, "P5L")

    def on_KEYPAD_BLOWER(self) -> None:
        """Handle blower keypad button."""
        self.UdBL = "ON" if self.UdBL == "OFF" else "OFF"

    def on_KEYPAD_WATERFALL(self) -> None:
        """Handle waterfall button."""
        self.UdWaterfall = "ON" if self.UdWaterfall == "OFF" else "OFF"

    def on_KEYPAD_AUX(self) -> None:
        """Handle aux button."""
        self.UdAux = "ON" if self.UdAux == "OFF" else "OFF"

    def _next_pump_value(
        self, ud: str | int, low_conn: str = "NA", *, vsp: bool = False
    ) -> str | int:
        if vsp:
            return (ud + 20) % 120
        two_speed = low_conn in self._connections
        if two_speed:
            return "LO" if ud == "OFF" else "HI" if ud == "LO" else "OFF"
        return "HI" if ud == "OFF" else "OFF"

    def on_KEYPAD_LIGHT(self) -> None:
        """Handle keypad for light."""
        self.UdLi = "HI" if self.UdLi == "OFF" else "OFF"

    def on_KEYPAD_LIGHT_120(self) -> None:
        """Handle keypad for light 2."""
        self.UdL120 = "ON" if self.UdL120 == "OFF" else "OFF"

    def on_KEYPAD_UP(self) -> None:
        """Handle keypad temp up."""
        self.SetpointG += 0.5 if self.TempUnits == "C" else 1.0

    def on_KEYPAD_DOWN(self) -> None:
        """Handle keypad temp down."""
        self.SetpointG -= 0.5 if self.TempUnits == "C" else 1.0

    ############################################################################
    #
    #               The pack properties that we want to watch
    #
    def on_UdP1(self) -> None:
        """Handle UdP1 changes."""
        if self.UdP1 == "HI":
            self.P1 = "HIGH"

        elif self.UdP1 == "LO":
            self.P1 = "LOW"

        else:
            self.P1 = "OFF"

    def on_UdP2(self) -> None:
        """Handle UdP2 changes."""
        if self.UdP2 == "HI":
            self.P2 = "HIGH"

        elif self.UdP2 == "LO":
            self.P2 = "LOW"

        else:
            self.P2 = "OFF"

    def on_UdP3(self) -> None:
        """Handle UdP3 changes."""
        if self.UdP3 == "HI":
            self.P3 = "HIGH"

        elif self.UdP3 == "LO":
            self.P3 = "LOW"

        else:
            self.P3 = "OFF"

    def on_UdP4(self) -> None:
        """Handle UdP4 changes."""
        if self.UdP4 == "HI":
            self.P4 = "HIGH"

        elif self.UdP4 == "LO":
            self.P4 = "LOW"

        else:
            self.P4 = "OFF"

    def on_UdP5(self) -> None:
        """Handle UdP5 changes."""
        if self.UdP5 == "HI":
            self.P5 = "HIGH"

        elif self.UdP5 == "LO":
            self.P5 = "LOW"

        else:
            self.P5 = "OFF"

    def on_UdBL(self) -> None:
        """Handle UdBL changes."""
        self.BL = self.UdBL

    def on_UdWaterfall(self) -> None:
        """Handle UdWaterfall changes."""
        self.Waterfall = self.UdWaterfall

    def on_UdAux(self) -> None:
        """Handle UdAux changes."""
        if self.UdAux == "ON":
            self.UdAuxTime = 20
        else:
            self.UdAuxTime = 0

    def on_UdLi(self) -> None:
        """Handle UdLi changes."""
        self.UdLightTime = 60 if self.UdLi == "HI" else 0

    def on_UdL120(self) -> None:
        """Handle UdL120 changes."""
        self.UdL120Time = 60 if self.UdL120 == "ON" else 0
        self.L120 = "ON" if self.UdL120 == "ON" else "OFF"

    def on_P1(self) -> None:
        """Handle changes to P1."""
        self._pump_helper()

    def on_P2(self) -> None:
        """Handle changes to P2."""
        self._pump_helper()

    def on_P3(self) -> None:
        """Handle changes to P3."""
        self._pump_helper()

    def on_P4(self) -> None:
        """Handle changes to P4."""
        self._pump_helper()

    def on_P5(self) -> None:
        """Handle changes to P5."""
        self._pump_helper()

    def on_BL(self) -> None:
        """Handle changes to BL."""
        self._pump_helper()

    def on_Waterfall(self) -> None:
        """Handle changes to Waterfall."""
        if self.Waterfall == "ON":
            self.UdWaterFallTime = 30
        else:
            self.UdWaterFallTime = 0

    def on_QuietState(self) -> None:
        """Handle quiet state."""
        if self.QuietState == "OFF":
            self.UdQuietTime = 29
            self.UdP1 = "OFF"
            self.UdVSP1 = 0
            self.UdP2 = "OFF"
            self.UdP3 = "OFF"
            self.UdP4 = "OFF"
            self.UdP5 = "OFF"
            self.UdBL = "OFF"
            self.UdWaterfall = "OFF"
            self.UdAux = "OFF"
            self.UdVSP3 = 0
        else:
            self.UdQuietTime = 0

    def on_SetpointG(self) -> None:
        """Handle changes to setpoint."""
        self._temp_helper()

    def on_UserMode(self) -> None:
        """Handle Mr.Steam user mode."""
        self.HeaterOutput = self.UserMode == "ON"
        if self.UserRuntime == 0:
            self.UserRuntime = 2
        if self.HeaterOutput:
            self.RemainingRuntime = self.UserRuntime

    def on_UserAroma(self) -> None:
        """Handle Mr.Steam aroma mode."""
        self.AromaOutput = self.UserAroma == "ON"

    def on_UserChroma(self) -> None:
        """Handle Mr.Steam chroma mode."""
        self.ChromaOutput = self.UserChroma == "ON"

    def on_UserRuntime(self) -> None:
        """Handle Mr.Steam user runtime change."""
        self.RemainingRuntime = self.UserRuntime

    ############################################################################
    #
    #               Timer routines
    #

    def every_second(self, _total_seconds: int) -> None:
        """Perform action every second."""
        self._pump_helper()
        self._temp_helper()

    def every_minute(self, _total_minutes: int) -> None:
        """Perform action every minute."""

    def every_hour(self, _total_hours: int) -> None:
        """Perform action every minute."""

    ############################################################################
    #
    #               Support and help routines
    #

    def _pump_helper(self) -> None:
        if all(
            [
                self.P1 == "OFF",
                self.P2 == "OFF",
                self.P3 == "OFF",
                self.P4 == "OFF",
                self.P5 == "OFF",
                self.BL == "OFF",
            ]
        ):
            self.CheckFlo = False
            self.UdPumpTime = 0
        else:
            self.CheckFlo = True
            self.UdPumpTime = 15

    def _temp_helper(self) -> None:
        if any(
            [
                self.RealSetPointG is None,
                self.SetpointG is None,
                self.DisplayedTempG is None,
            ]
        ):
            return

        # Set the real setpoint temperature
        self.RealSetPointG = self.SetpointG

        # Handle heating and cooling
        if self.DisplayedTempG >= self.RealSetPointG:
            # We're at temperature, so we turn off heaters etc
            if self.MSTR_HEATER is not None:
                self.MSTR_HEATER = "OFF"
            if self.Heating is not None:
                if isinstance(self.Heating, bool):
                    self.Heating = False
                else:
                    self.Heating = ""

            self.CP = "OFF"

        elif self.DisplayedTempG < self.RealSetPointG - 0.5:
            # Below 0.5C of the setpoint, turn stuff on
            if self.MSTR_HEATER is not None:
                self.MSTR_HEATER = "ON"
            if self.Heating is not None:
                if isinstance(self.Heating, bool):
                    self.Heating = True
                else:
                    self.Heating = "Heating"

            self.CP = "ON"

    @property
    def is_heating(self) -> bool:
        """Determine if heating is being done."""
        if self.MSTR_HEATER is not None:
            return self.MSTR_HEATER == "ON"
        if self.Heating is not None:
            if isinstance(self.Heating, bool):
                return self.Heating
            return self.Heating != ""
        return False

    def check_thermodynamics(self, _elapsed_time: int) -> None:
        """Check thermodynamics for the spa."""
        # If there is no heating, then the water temperature drops
        delta: float = 0.2 if self.TempUnits == "F" else 0.1
        if self.DisplayedTempG is not None:
            if self.is_heating:
                self.DisplayedTempG += delta
            else:
                self.DisplayedTempG -= delta

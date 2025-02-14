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
    UdLi: Any
    QuietState: Any
    UdQuietTime: Any

    # Support accessors
    P1: Any
    P2: Any
    P3: Any

    # Utility accessors
    CheckFlo: Any
    UdPumpTime: Any
    UdLightTime: Any
    UdL120Time: Any

    Pump1AsVSP: Any
    Pump3AsVSP: Any

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
        """Handle keypage for light."""
        self.UdLi = "HI" if self.UdLi == "OFF" else "OFF"

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

    def on_UdLi(self) -> None:
        """Handle UdLi changes."""
        self.UdLightTime = 60 if self.UdLi == "HI" else 0

    def on_P1(self) -> None:
        """Handle changes to P1."""
        self._pump_helper()

    def on_P2(self) -> None:
        """Handle changes to P2."""
        self._pump_helper()

    def on_P3(self) -> None:
        """Handle changes to P3."""
        self._pump_helper()

    def on_QuietState(self) -> None:
        """Handle quiet state."""
        if self.QuietState == "OFF":
            self.UdQuietTime = 29
            self.UdP1 = "OFF"
            self.UdVSP1 = 0
            self.UdP2 = "OFF"
            self.UdP3 = "OFF"
            self.UdVSP3 = 0
        else:
            self.UdQuietTime = 0

    ############################################################################
    #
    #               Support and help routines
    #

    def _pump_helper(self) -> None:
        if all([self.P1 == "OFF", self.P2 == "OFF", self.P3 == "OFF"]):
            self.CheckFlo = False
            self.UdPumpTime = 0
        else:
            self.CheckFlo = True
            self.UdPumpTime = 15

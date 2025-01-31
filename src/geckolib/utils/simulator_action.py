"""Simulator action class."""

# ruff: noqa: N802

import logging
from typing import Any

_LOGGER = logging.getLogger(__name__)


class GeckoSimulatorAction:
    """Define the action for various simulator events."""

    ############################################################################
    #
    #               The accessors that we want to interact with
    #
    # User demands
    UdP1: Any
    UdP2: Any

    # Support accessors
    P1: Any
    P2: Any

    # Utility accessors
    CheckFlo: Any
    UdPumpTime: Any

    ############################################################################
    #
    #               The keypad buttons we want to handle
    #
    def on_KEYPAD_PUMP_1(self) -> None:
        """Handle keypad pump 1."""
        self.UdP1 = "HI" if self.UdP1 == "OFF" else "OFF"

    def on_KEYPAD_PUMP_2(self) -> None:
        """Handle keypad pump 2."""
        self.UdP2 = "HI" if self.UdP2 == "OFF" else "OFF"

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

    def on_P1(self) -> None:
        """Handle changes to P1."""
        self._pump_helper()

    def on_P2(self) -> None:
        """Handle changes to P1."""
        self._pump_helper()

    ############################################################################
    #
    #               Support and help routines
    #

    def _pump_helper(self) -> None:
        if all([self.P1 == "OFF", self.P2 == "OFF"]):
            self.CheckFlo = False
            self.UdPumpTime = 0
        else:
            self.CheckFlo = True
            self.UdPumpTime = 15

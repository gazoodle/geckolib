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
    UdP1: Any
    P1: Any
    CheckFlo: Any
    UdPumpTime: Any

    ############################################################################
    #
    #               The keypad buttons we want to handle
    #
    def on_KEYPAD_PUMP_1(self) -> None:
        """Handle keypad pump 1."""
        self.UdP1 = "HI" if self.UdP1 == "OFF" else "OFF"

    ############################################################################
    #
    #               The pack properties that we want to watch
    #
    def on_UdP1(self) -> None:
        """Handle UdP1 changes."""
        if self.UdP1 == "HI":
            self.P1 = "HIGH"
            self.CheckFlo = True
            self.UdPumpTime = 15

        elif self.UdP1 == "LO":
            self.P1 = "LOW"
            self.CheckFlo = True
            self.UdPumpTime = 15

        else:
            self.P1 = "OFF"
            self.CheckFlo = False
            self.UdPumpTime = 0

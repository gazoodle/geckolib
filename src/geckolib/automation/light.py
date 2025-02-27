"""Gecko Lights."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any

from geckolib.automation.power import GeckoPower
from geckolib.const import GeckoConstants

if TYPE_CHECKING:
    from geckolib.automation.async_facade import GeckoAsyncFacade


class GeckoLight(GeckoPower):
    """The base class of lights."""

    def __init__(self, facade: GeckoAsyncFacade, name: str, key: str) -> None:
        """Initialize the light class."""
        super().__init__(facade, name, key)
        self.device_class = GeckoConstants.DEVICE_CLASS_LIGHT

    @property
    @abstractmethod
    def is_on(self) -> bool:
        """Determine if the light is on or not."""
        raise NotImplementedError

    @property
    @abstractmethod
    def state(self) -> str:
        """Get the state of the light."""
        raise NotImplementedError

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the light ON, but does nothing if it is already ON."""
        raise NotImplementedError

    async def async_turn_off(self) -> None:
        """Turn the device OFF, but does nothing if it is already OFF."""
        raise NotImplementedError

    def __str__(self) -> str:
        """Stringize."""
        return f"{self.name}: {self.state}"

    @property
    def monitor(self) -> str:
        """Get a monitor string."""
        return f"{self.key}: {self.state}"


class GeckoLightLi(GeckoLight):
    """Class for the Li light."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the Li light."""
        super().__init__(facade, "Light", "LI")
        if "LI" in self.facade.spa.struct.connections:
            self.set_availability(is_available=True)

        if self.is_available:
            self._state_accessor = self.facade.spa.accessors["UdLi"]
            self._state_accessor.watch(self._on_change)

    @property
    def is_on(self) -> bool:
        """Determine if the light is on or not."""
        return self.state != "OFF"

    @property
    def state(self) -> str:
        """Get the state of the light."""
        return self._state_accessor.value

    async def async_turn_on(self, **_kwargs: Any) -> None:
        """Turn the light ON, but does nothing if it is already ON."""
        if self.is_on:
            return
        await self._state_accessor.async_set_value("HI")

    async def async_turn_off(self, **_kwargs: Any) -> None:
        """Turn the light OFF, but does nothing if it is already OFF."""
        if not self.is_on:
            return
        await self._state_accessor.async_set_value("OFF")


class GeckoLightL120(GeckoLight):
    """Class for the L120 light."""

    def __init__(self, facade: GeckoAsyncFacade) -> None:
        """Initialize the L120 light."""
        super().__init__(facade, "Light 2", "L120")
        if "L120" in self.facade.spa.struct.connections:
            self.set_availability(is_available=True)

        if self.is_available:
            self._state_accessor = self.facade.spa.accessors["UdL120"]
            self._state_accessor.watch(self._on_change)

    @property
    def is_on(self) -> bool:
        """Determine if the light is on or not."""
        return self.state != "OFF"

    @property
    def state(self) -> str:
        """Get the state of the light."""
        return self._state_accessor.value

    async def async_turn_on(self, **_kwargs: Any) -> None:
        """Turn the light ON, but does nothing if it is already ON."""
        if self.is_on:
            return
        await self._state_accessor.async_set_value("ON")

    async def async_turn_off(self, **_kwargs: Any) -> None:
        """Turn the light OFF, but does nothing if it is already OFF."""
        if not self.is_on:
            return
        await self._state_accessor.async_set_value("OFF")

from typing import override
from greenthumb_core.core.components.time.time_actions import ReadTime, WaitForTime
from greenthumb_core.core.components.serial_port.serial_actions import BinarySetSerialPinOn, BinarySetSerialPinOff
from greenthumb_core.core.components.time.time_component import TimeComponent
from greenthumb_core.core.components.serial_port.serial_components import SerialComponent
from greenthumb_core.core.components.time.time_triggers import EveryNSeconds
from greenthumb_core.domains.i_action import I_Action
from greenthumb_core.domains.i_task import I_Task
from greenthumb_core.domains.i_trigger import I_Trigger


class SerialPinBinaryControl(I_Task):
    """
    A task that sets a serial pin to a specific state (ON/OFF).
    This task can be used to control devices connected to the serial port.
    """

    def __init__(self, name: str, pin_number: int, trigger_interval: int = 30, on_duration: int = 600):
        self._name = "set_serial_pin"
        self._description = "Sets a serial pin to ON or OFF."
        self.time_component = TimeComponent()
        self.time_component.initialize()
        self.serial_component = SerialComponent(name, pin_number=pin_number)
        self.serial_component.initialize()
        self._actions = [
            ReadTime(self.time_component),
            BinarySetSerialPinOn(self.serial_component),
            WaitForTime(self.time_component, on_duration),  # Wait for on_duration seconds after setting the pin
            BinarySetSerialPinOff(self.serial_component)  # Set the pin OFF after waiting
        ]
        self._trigger = EveryNSeconds(trigger_interval, self.time_component)  # Trigger every trigger_interval seconds

    @override
    @property
    def name(self) -> str:
        return self._name

    @override
    @property
    def description(self) -> str:
        return self._description

    @override
    @property
    def actions(self) -> list[I_Action]:
        return self._actions

    @override
    @property
    def trigger(self) -> I_Trigger:
        return self._trigger

    @override
    def cleanup(self):
        self.time_component.shutdown()
        self.serial_component.shutdown()

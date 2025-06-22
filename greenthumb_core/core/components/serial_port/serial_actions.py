from typing import override
from greenthumb_core.core.components.serial_port.serial_components import SerialComponent
from greenthumb_core.domains.i_action import I_Action
import time


class BinarySetSerialPinOn(I_Action):
    """
    An action that sets a binary value on a serial pin.
    """

    def __init__(self, component: SerialComponent):
        self._name = "set_pin_on"
        self._description = "Sets a pin to ON."
        self.component: SerialComponent = component

    @override
    @property
    def name(self) -> str:
        return self._name

    @override
    @property
    def description(self) -> str:
        return self._description

    @override
    def execute(self) -> None:
        if self.component.serial_connection is None:
            raise ValueError("Serial connection is not initialized.")
        try:
            cmd = f"Pin {self.component.pin_number} ON"
            self.component.serial_connection.reset_input_buffer()
            self.component.serial_connection.reset_output_buffer()
            self.component.serial_connection.write((cmd.strip() + "\n").encode())
            print(f"Executing command: {cmd.strip()}")
            time.sleep(0.1)  # Give device time to respond
            response = self.component.serial_connection.readline()
            if response:
                print("[Serial Device]:", response.decode().strip())
        except Exception as e:
            print("Error writing to serial pin:", e)


class BinarySetSerialPinOff(I_Action):
    """
    An action that sets a binary value on a serial pin.
    """

    def __init__(self, component: SerialComponent):
        self._name = "set_pin_off"
        self._description = "Sets a pin to OFF."
        self.component: SerialComponent = component

    @override
    @property
    def name(self) -> str:
        return self._name

    @override
    @property
    def description(self) -> str:
        return self._description

    @override
    def execute(self) -> None:
        if self.component.serial_connection is None:
            raise ValueError("Serial connection is not initialized.")
        try:
            cmd = f"Pin {self.component.pin_number} OFF"
            self.component.serial_connection.reset_input_buffer()
            self.component.serial_connection.reset_output_buffer()
            self.component.serial_connection.write((cmd.strip() + "\n").encode())
            print(f"Executing command: {cmd.strip()}")
            time.sleep(0.1)  # Give device time to respond
            response = self.component.serial_connection.readline()
            if response:
                print("[Serial Device]:", response.decode().strip())
        except Exception as e:
            print("Error writing to serial pin:", e)

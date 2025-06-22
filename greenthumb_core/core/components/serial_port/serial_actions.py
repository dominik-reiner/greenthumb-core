from datetime import datetime
from typing import override
from greenthumb_core.core.components.serial_port.serial_components import SerialComponent
from greenthumb_core.domains.i_action import I_Action


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
    def execute(self) -> datetime:
        try:
            cmd = f"Pin {self.component.serial_connection.pin} ON"
            self.component.serial_connection.write((cmd.strip() + "\n").encode())
            response = self.component.serial_connection.readline()
            if response:
                print("[Serial Device]:", response.decode().strip())
        except Exception as e:
            print("Error writing to serial pin:", e)
        finally:
            self.component.serial_connection.close()


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
    def execute(self) -> datetime:
        try:
            cmd = f"Pin {self.component.serial_connection.pin} OFF"
            self.component.serial_connection.write((cmd.strip() + "\n").encode())
            response = self.component.serial_connection.readline()
            if response:
                print("[Serial Device]:", response.decode().strip())
        except Exception as e:
            print("Error writing to serial pin:", e)
        finally:
            self.component.serial_connection.close()

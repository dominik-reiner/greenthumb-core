from typing import override
import serial
from greenthumb_core.domains.i_component import I_Component


class SerialComponent(I_Component):
    """
    A component that provides serial port related functionality.
    This component can be used to interact with serial ports, send and receive data,
    and perform other serial communication operations.
    """

    def __init__(self, name: str, serial_port: str = '/dev/ttyACM0', baudrate: int = 9600, pin_number: int = 7):
        self._name = name
        self._description = "Provides serial port related functionality."
        self.serial_port = serial_port
        self.baudrate = baudrate
        self.pin_number = pin_number
        self.serial_connection = None

    @override
    @property
    def name(self) -> str:
        return self._name

    @override
    @property
    def description(self) -> str:
        return self._description

    @override
    def initialize(self):
        self.serial_connection = serial.Serial(self.serial_port, self.baudrate, timeout=1)
        import time
        time.sleep(2)  # wait after opening serial port

    @override
    def shutdown(self):
        self.serial_connection.close()

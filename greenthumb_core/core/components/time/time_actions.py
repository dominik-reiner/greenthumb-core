from datetime import datetime
from typing import override
from greenthumb_core.core.components.time.time_component import TimeComponent
from greenthumb_core.domains.i_action import I_Action


class ReadTime(I_Action):
    """
    An action that reads the current time.
    """

    def __init__(self, component: TimeComponent):
        self._name = "read_time"
        self._description = "Reads the current time from the system."
        self.component = component

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
        if self.component.datetime is None:
            raise ValueError("Component datetime is not initialized.")
        current_time = self.component.datetime.now()
        print(f"Current time: {current_time}")
        return current_time


class WaitForTime(I_Action):
    """
    An action that waits for a specific time.
    This action can be used to pause execution for a certain time.
    """

    def __init__(self, component: TimeComponent, wait_time: int):
        self._name = "wait_for_time"
        self._description = "Waits a specified time."
        self.component: TimeComponent = component
        self.wait_time: int = wait_time

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
        if self.component.datetime is None:
            raise ValueError("Component datetime is not initialized.")
        print(f"Waiting for {self.wait_time} seconds...")
        current_time = self.component.datetime.now()
        end_time = current_time.timestamp() + self.wait_time
        while current_time.timestamp() < end_time:
            current_time = self.component.datetime.now()
        print(f"Waited for {self.wait_time} seconds. Current time: {current_time}")

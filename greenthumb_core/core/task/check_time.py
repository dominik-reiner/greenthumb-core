from typing import override
from greenthumb_core.core.components.time.time_actions import ReadTime
from greenthumb_core.core.components.time.time_component import TimeComponent
from greenthumb_core.core.components.time.time_triggers import EveryNSeconds
from greenthumb_core.domains.i_action import I_Action
from greenthumb_core.domains.i_task import I_Task
from greenthumb_core.domains.i_trigger import I_Trigger


class CheckTime(I_Task):
    """
    A task that checks the current time and returns it.
    This task can be used to verify if the system time is correct or to perform time-based operations.
    """

    def __init__(self, trigger_interval: int = 5):
        self._name = "check_time"
        self._description = "Checks the current time from the system."
        self.time_component = TimeComponent()
        self.time_component.initialize()
        self._actions = [
            ReadTime(self.time_component)
        ]
        self._trigger = EveryNSeconds(trigger_interval, self.time_component)

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

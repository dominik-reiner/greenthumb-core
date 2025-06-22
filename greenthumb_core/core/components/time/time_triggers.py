from typing import override
from greenthumb_core.core.components.time.time_actions import ReadTime
from greenthumb_core.core.components.time.time_component import TimeComponent
from greenthumb_core.domains.i_trigger import I_Trigger


class EveryNSeconds(I_Trigger):
    """
    A trigger that activates every N seconds.
    This trigger can be used to perform periodic tasks at regular intervals.
    """

    def __init__(self, interval_seconds: int, component: TimeComponent):
        self.component = component
        self.action = ReadTime(component)
        self._interval_seconds = interval_seconds
        self._last_triggered = None  # Use None to indicate never triggered

    @override
    def should_trigger(self) -> bool:
        print("Checking if trigger should activate.")
        current_time = self.action.execute()
        if self._last_triggered is None:
            self._last_triggered = current_time
            return True
        if (current_time - self._last_triggered).total_seconds() >= self._interval_seconds:
            self._last_triggered = current_time
            return True
        return False

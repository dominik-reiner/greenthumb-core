from abc import ABC, abstractmethod

from greenthumb_core.domains.i_action import I_Action
from greenthumb_core.domains.i_component import I_Component


class I_Trigger(ABC):
    """
    Interface for a trigger in the GreenThumb application.
    A trigger is an event or condition that initiates a task.
    It always uses the return value of an action to determine if it should execute.
    This interface defines the methods that any trigger should implement.
    """
    component: I_Component
    action: I_Action

    @abstractmethod
    def should_trigger(self) -> bool:
        """
        Determines whether the trigger should activate based on the result
        of an action.
        Args:
            action_result: The result returned by the action.
        Returns:
            bool: True if the trigger condition is met, False otherwise.
        """
        pass

from abc import ABC, abstractmethod

from greenthumb_core.domains.i_action import I_Action
from greenthumb_core.domains.i_trigger import I_Trigger


class I_Task(ABC):
    """
    Interface for a task in the GreenThumb application.
    This interface defines the methods that any task should implement.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Get the name of the task.
        This property should return a string that identifies the task.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Get the description of the task.
        This property should return a string that describes what the task does.
        """
        pass

    @property
    @abstractmethod
    def actions(self) -> list[I_Action]:
        """
        Get the list of actions associated with the task.
        This property should return a list of actions that can be performed as part of the task.
        """
        pass

    @property
    @abstractmethod
    def trigger(self) -> I_Trigger:
        """
        Get the trigger action for the task.
        This property should return the action that initiates the task.
        """
        pass

    def run(self):
        """
        Run the task.
        This method should contain the core logic of the task.
        """
        if self.trigger.should_trigger():
            print(f"Trigger condition met for task: {self.name}")
            for action in self.actions:
                try:
                    print(f"Executing action: {action.name}")
                    action.execute()
                except Exception as e:
                    print(f"Error executing action {action.name}: {e}")
        else:
            print(f"Trigger condition not met for task: {self.name}, skipping actions.")

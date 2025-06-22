from abc import ABC, abstractmethod

from greenthumb_core.domains.i_component import I_Component


class I_Action(ABC):
    """
    Interface for an action in the GreenThumb application.
    This interface defines the methods that any action should implement.
    """
    component: I_Component

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Get the name of the action.
        This property should return a string that identifies the action.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Get the description of the action.
        This property should return a string that describes what the action does.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Execute the action.
        This method should contain the core logic of the action.
        """
        pass

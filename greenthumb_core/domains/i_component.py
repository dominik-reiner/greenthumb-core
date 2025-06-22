from abc import ABC, abstractmethod


class I_Component(ABC):
    """
    Interface for components in the GreenThumb application.
    This interface defines the methods that any component should implement.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Get the name of the component.
        This property should return a string that identifies the component.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Get the description of the component.
        This property should return a string that describes what the component does.
        """
        pass

    def initialize(self):
        """
        Initialize the component.
        This method should set up any necessary state or resources for the component.
        """
        pass

    def shutdown(self):
        """
        Clean up resources and perform any necessary shutdown operations.
        This method should be called when the component is no longer needed.
        """
        pass

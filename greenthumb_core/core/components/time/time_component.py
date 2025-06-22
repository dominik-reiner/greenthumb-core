from typing import override
from greenthumb_core.domains.i_component import I_Component
from datetime import datetime


class TimeComponent(I_Component):
    """
    A component that provides time-related functionality.
    This component can be used to get the current time, format it, and perform other time-related operations.
    """

    def __init__(self):
        self._name = "Time Component"
        self._description = "Provides time-related functionality."
        self.datetime: datetime | None = None

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
        self.datetime = datetime

    @override
    def shutdown(self):
        self.datetime = None

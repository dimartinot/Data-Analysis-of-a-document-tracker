from abc import ABC, abstractmethod

class AbstractGUI(ABC):
    """Abstract class to inherit from when creating a new type of GUI"""

    def __init__(self, operator):
        super().__init__()
        self.operator = operator

    @abstractmethod
    def show(self):
        """Abstract method to override that implements the displaying of the GUI"""
        pass
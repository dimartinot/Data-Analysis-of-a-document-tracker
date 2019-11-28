from abc import ABC, abstractmethod

class AbstractOperator(ABC):
    """Abstract class to inherit from when creating a new type of Operator"""

    def __init__(self, data):
        super().__init__()
        self.data = data

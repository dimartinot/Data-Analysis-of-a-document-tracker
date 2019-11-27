from abc import ABC, abstractmethod

class AbstractOperator(ABC):

    def __init__(self, data):
        super().__init__()
        self.data = data
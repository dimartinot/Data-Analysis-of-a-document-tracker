from abc import ABC, abstractmethod

class AbstractDataset(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def get_item(self, index):
        pass
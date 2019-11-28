from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """Abstract factory class to inherit from when creating a factory for a new family of dataset/operator"""

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def load_dataset(self, path):
        pass

    @abstractmethod
    def get_operator(self, dataset):
        pass
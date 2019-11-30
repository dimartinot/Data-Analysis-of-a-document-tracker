# Libraries import
from abc import ABC, abstractmethod

# Local files import
from classes.abstract.AbstractDataset import AbstractDataset
from classes.abstract.AbstractOperator import AbstractOperator

class AbstractFactory(ABC):
    """Abstract factory class to inherit from when creating a factory for a new family of dataset/operator"""

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def load_dataset(self, path) -> AbstractDataset:
        pass

    @abstractmethod
    def get_operator(self, dataset: AbstractDataset) -> AbstractOperator:
        pass
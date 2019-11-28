#libraries imports
import os
import random
import string
import inspect

#local file imports
from classes.abstract.AbstractFactory import AbstractFactory
from classes.exception.NotFoundFileException import NotFoundFileException
from classes.exception.IncorrectInputDataException import IncorrectInputDataException
from classes.ISSUU.IssuuDataset import IssuuDataset
from classes.ISSUU.IssuuOperator import IssuuOperator

class IssuuFactory(AbstractFactory):
    """Factory class that instantiates the ISSUU family of classes (dataset/operator)"""

    def __init__(self):
        super().__init__()

    def _load_dataset_from_file(self, path):
        """Private method that loads a dataset from a .json file according to the Issuu format"""
        if (path != None and os.path.exists(path)):
            f_content = open(path, "r").read()
            return IssuuDataset(f_content)
        else:
            raise NotFoundFileException()

        return IssuuDataset(None)


    def _load_dataset_from_string(self, string):
        """Private method that loads a dataset from a string according to the Issuu Format"""
        assert(type(string)==str)
        if (string != None):
            return IssuuDataset(string)
        else:
            raise IncorrectInputDataException()

    def load_dataset(self, path=None, content=None):
        """Public method that loads a dataset from either a string or a filepath"""
        if (path is not None):
            return self._load_dataset_from_file(path)
        else:
            return self._load_dataset_from_string(content)   

    def get_operator(self, dataset):
        return IssuuOperator(dataset)
# libraries import
import pandas as pd
import inspect
import re
import unittest
import numpy as np

# local files import
from classes.abstract.AbstractDataset import AbstractDataset
from classes.exception.IncorrectInputDataException import IncorrectInputDataException

class IssuuDataset(AbstractDataset):
    """Holds the data of an Issuu-syntaxed dataset"""

    def __init__(self, data):
        """data is expected to be a string"""
        assert(type(data) == str)

        #Regular expression to transform the data as a list of json 
        l = re.findall(r"{(.*)}"
                ,data)
        if (l == []):
            raise IncorrectInputDataException()
        #format this to be a json list
        new = "[{"+"},\n{".join(l)+"}]"

        #transform this list into a pandas dataframe
        try:
            self._data = pd.read_json(new)
        except:
            raise IncorrectInputDataException()
        self._size = None


    def size(self):
        """Methods that lazy loads the size of the dataset"""
        if self._size == None:
            # faster than self._data.shape[0]
            self._size = len(self._data.index)
        return self._size

    def get_item(self, index, as_dict=False):
        """Methods that retrieves an item at a given index"""
        if (index < 0 or index >= self._data.shape[0]):
            raise IndexError("Provided index is out of bound")
        if (as_dict):
            row = self._data.iloc[index, :]
            # drops columns with nan, that are symptoms of missing values in the field but takes unuseful space
            row_dict = row.dropna().to_dict()
            return row_dict
        return self._data.iloc[index,:]

    def as_dataframe(self):
        """Returns its Pandas DataFrame component"""
        return self._data
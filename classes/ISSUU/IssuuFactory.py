#libraries imports
import os
import random
import string
import inspect

#local file imports
from classes.abstract.AbstractFactory import AbstractFactory
from classes.abstract.AbstractDataset import AbstractDataset
from classes.abstract.AbstractOperator import AbstractOperator

from classes.exception.NotFoundFileException import NotFoundFileException
from classes.exception.IncorrectInputDataException import IncorrectInputDataException
from classes.exception.IncorrectDatasetInstanceException import IncorrectDatasetInstanceException
from classes.exception.IncorrectOperatorInstanceException import IncorrectOperatorInstanceException

from classes.ISSUU.IssuuDataset import IssuuDataset
from classes.ISSUU.IssuuOperator import IssuuOperator
from classes.ISSUU.IssuuGUI import IssuuGUI

def join_list_str(x):
    return ''.join(str(x))

class IssuuFactory(AbstractFactory):
    """Factory class that instantiates the ISSUU family of classes (dataset/operator)"""

    LINE_BY_LINE_READING = 500

    def __init__(self):
        super().__init__()

    def _load_dataset_from_file(self, path):
        """Private method that loads a dataset from a .json file according to the Issuu format"""

        if (path != None and os.path.exists(path)):

            f =  open(path, "r")
                # try:
                #     # mmap.PROT_READ is UNIX based
                #     map_file = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
                # except:
                #     # mmap.ACCESS_READ is Windows based
                #     map_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

            res = f.readlines()
            f.close()
            str_content = ''.join(res)

            return IssuuDataset(str_content, path)
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
        """Public method that loads a correctly instantiated Operator"""
        if (isinstance(dataset, IssuuDataset)):
            return IssuuOperator(dataset)
        elif (isinstance(dataset, AbstractDataset)):
            # Error raised in the case the passed variable is of dataset type but not the instance of the Issuu dataset family
            raise IncorrectDatasetInstanceException()
        else:    
            # Error raised if the input is not even a dataset
            raise IncorrectInputDataException()
            
    def launch_GUI(self, operator, doc_uid = None, user_uid = None):
        """Public method that loads the GUI"""
        if (isinstance(operator, IssuuOperator)):
            return IssuuGUI(operator, doc_uid, user_uid)
        elif (isinstance(operator, AbstractOperator)):
            raise IncorrectOperatorInstanceException()
        else:
            raise IncorrectInputDataException()
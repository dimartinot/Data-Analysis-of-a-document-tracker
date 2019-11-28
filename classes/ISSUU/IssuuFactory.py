#libraries imports
import os
import random
import string
import inspect
from multiprocessing import Pool
import mmap

#local file imports
from classes.abstract.AbstractFactory import AbstractFactory
from classes.exception.NotFoundFileException import NotFoundFileException
from classes.exception.IncorrectInputDataException import IncorrectInputDataException
from classes.ISSUU.IssuuDataset import IssuuDataset
from classes.ISSUU.IssuuOperator import IssuuOperator

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

            #pool = Pool(os.cpu_count() - 1)

            return IssuuDataset(str_content)
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
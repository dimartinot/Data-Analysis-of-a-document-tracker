#libraries imports
import os
import random
import string
import inspect

#local file imports
from classes.abstract.AbstractFactory import AbstractFactory
from classes.exception.NotFoundFileException import NotFoundFileException
from classes.exception.IncorrectInputDataException import IncorrectInputDataException
from classes.test.UnitTest import UnitTest
from classes.ISSUU.IssuuDataset import IssuuDataset

class IssuuFactory(AbstractFactory):

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
        if (string == None):
            return IssuuDataset(string)
        else:
            raise IncorrectInputDataException()

    def load_dataset(self, path=None, content=None):
        """Public method that loads a dataset from either a string or a filepath"""
        if (path is not None):
            return self._load_dataset_from_file(path)
        else:
            return self._load_dataset_from_string(content)   

    class Test(UnitTest):
        factory = IssuuFactory()

        file_content = """
            {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "impression",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause_type": "page" }
            {   "ts": 1393631990,    "visitor_uuid": "9a83c97f415601a6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",    "visitor_ip": "03a2602450304bd4",    "visitor_country": "AR",    "visitor_referrer": "0aefac0a2bd221ab",    "env_type": "reader",    "env_doc_id": "131203154832-9b8594b7ec211f7e1a0782fd9883a42c",    "env_adid": null,    "event_type": "read",    "subject_type": "doc",    "subject_doc_id": "131203154832-9b8594b7ec211f7e1a0782fd9883a42c",    "subject_page": 0,    "cause": null }
            {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "pageread",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause": null }
            {   "ts": 1393631989,    "visitor_uuid": "64bf70296da2f9fd",    "visitor_username": null,    "visitor_source": "internal",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0",    "visitor_ip": "06f49269e749a837",    "visitor_country": "VE",    "visitor_referrer": "64f729926497515c",    "env_type": "reader",    "env_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "env_adid": null,    "event_type": "pagereadtime",    "event_readtime": 797,    "subject_type": "doc",    "subject_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "subject_page": 10,    "cause": null }
        """

        def test_load_dataset_not_existing_file(self):
            """Tests the case of a non existing file or None string passed"""
            print("IssuuFactory.load_dataset_not_existing_file")
            has_exception = False
            # Generates a random name of size 10
            random_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])+".json"
            try:
                factory.load_dataset(path=random_name)
            except:
                has_exception = True
            UnitTest.affirm(has_exception)
        
        def test_load_dataset_from_string(self):
            """Tests the load of a dataset from a faulty string"""
            random_content = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
            try:
                factory.load_dataset_from_file(content=random_content)
            except:
                has_exception = True

            UnitTest.affirm(has_exception)
        # def test_load_dataset_check_size(self):
        #     """Tests the file has been correctly loaded"""
        #     print("IssuuFactory.load_dataset_check_size")
        #     # Generates a file to test

        #     f = open("_tmp.json", "w")
        #     f.write(file_content)
        #     f.close()
            
        #     factory.load_dataset("_tmp.json")
        #     os.remove("_tmp.json")
        #     UnitTest.affirm(factory.size() == 4)

if __name__ == "__main__":
    test = IssuuFactory.Test()
    # get all attributes from the class Test
    attrs = (getattr(test, name) for name in dir(test))
    # get all attributes that are test functions
    methods = filter(inspect.ismethod, attrs)
    # for each test function: execute it
    for method in methods:
        method()
# libraries import
import pandas as pd
import inspect
import re

# local files import
from classes.test.UnitTest import UnitTest
from classes.abstract.AbstractDataset import AbstractDataset
from classes.exception.IncorrectInputDataException import IncorrectInputDataException

class IssuuDataset(AbstractDataset):
    """This class holds the data of an Issuu-syntaxed dataset"""
    def __init__(self, data):
        """data is expected to be a string"""
        assert(type(data) == str)

        #Regular expression to transform the data as a list of json 
        l = re.findall(r"{(.*)}"
                ,data)
        if (l == "[]"):
            raise IncorrectInputDataException
        #format this to be a json list
        new = "[{"+"},\n{".join(l)+"}]"

        #transform this list into a pandas dataframe
        self._data = pd.read_json(new)
        self._size = None


    def size(self):
        """Methods that lazy loads the size of the dataset"""
        if self._size == None:
            # faster than self._data.shape[0]
            self._size = len(self._data.index)
        return self._size

    def get_item(self, index):
        """Methods that retrieves an item at a given index"""
        if (index <= 0 or index >= self._data.shape[0]):
            raise IndexError("Provided index is out of bound")
        return self._data.iloc[index,:]

    class Test(UnitTest):

        file_content = """
            {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "impression",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause_type": "page" }
            {   "ts": 1393631990,    "visitor_uuid": "9a83c97f415601a6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",    "visitor_ip": "03a2602450304bd4",    "visitor_country": "AR",    "visitor_referrer": "0aefac0a2bd221ab",    "env_type": "reader",    "env_doc_id": "131203154832-9b8594b7ec211f7e1a0782fd9883a42c",    "env_adid": null,    "event_type": "read",    "subject_type": "doc",    "subject_doc_id": "131203154832-9b8594b7ec211f7e1a0782fd9883a42c",    "subject_page": 0,    "cause": null }
            {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "pageread",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause": null }
            {   "ts": 1393631989,    "visitor_uuid": "64bf70296da2f9fd",    "visitor_username": null,    "visitor_source": "internal",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0",    "visitor_ip": "06f49269e749a837",    "visitor_country": "VE",    "visitor_referrer": "64f729926497515c",    "env_type": "reader",    "env_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "env_adid": null,    "event_type": "pagereadtime",    "event_readtime": 797,    "subject_type": "doc",    "subject_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "subject_page": 10,    "cause": null }
        """

        def test_dataset_size(self):
            """Tests the case of a non existing file or None string passed"""
            print("IssuuDataset.size")
            
            UnitTest.affirm(False)

if __name__ == "__main__":
    test = IssuuDataset.Test()
    attrs = (getattr(test, name) for name in dir(test))
    methods = filter(inspect.ismethod, attrs)
    for method in methods:
        method()
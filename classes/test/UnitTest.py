# libraries import
import os
import random
import string
import inspect
import unittest
import json
import numpy as np

# local files import
from classes.abstract.AbstractDataset import AbstractDataset
from classes.abstract.AbstractOperator import AbstractOperator
from classes.abstract.AbstractGUI import AbstractGUI
from classes.exception.NotFoundFileException import NotFoundFileException
from classes.exception.IncorrectInputDataException import IncorrectInputDataException
from classes.exception.IncorrectDatasetInstanceException import IncorrectDatasetInstanceException
from classes.ISSUU.IssuuFactory import IssuuFactory
from classes.ISSUU.IssuuDataset import IssuuDataset
from classes.ISSUU.IssuuOperator import IssuuOperator

# The basic unit testing class

class UnitTest(unittest.TestCase):

    factory = IssuuFactory()

    file_content = """
        {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "impression",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause_type": "page" }
        {   "ts": 1393631990,    "visitor_uuid": "9a83c97f415601a6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36",    "visitor_ip": "03a2602450304bd4",    "visitor_country": "AR",    "visitor_referrer": "0aefac0a2bd221ab",    "env_type": "reader",    "env_doc_id": "131203154832-9b8594b7ec211f7e1a0782fd9883a42c",    "env_adid": null,    "event_type": "read",    "subject_type": "doc",    "subject_doc_id": "131203154832-9b8594b7ec211f7e1a0782fd9883a42c",    "subject_page": 0,    "cause": null }
        {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "pageread",    "subject_type": "doc",    "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "subject_page": 23,    "cause": null }
        {   "ts": 1393631989,    "visitor_uuid": "64bf70296da2f9fd",    "visitor_username": null,    "visitor_source": "internal",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0",    "visitor_ip": "06f49269e749a837",    "visitor_country": "VE",    "visitor_referrer": "64f729926497515c",    "env_type": "reader",    "env_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "env_adid": null,    "event_type": "pagereadtime",    "event_readtime": 797,    "subject_type": "doc",    "subject_doc_id": "130705172251-3a2a725b2bbd5aa3f2af810acf0aeabb",    "subject_page": 10,    "cause": null }
    """

    def test_load_dataset_not_existing_file(self):
        """Tests the case of a non existing file or None string"""
        # Generates a random filename of size 10
        random_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])+".json"
        with self.assertRaises(NotFoundFileException):
            self.factory.load_dataset(path=random_name)
    
    def test_load_dataset_from_gibberish_string(self):
        """Tests the load of a dataset from a faulty string"""
        # Generates a random string of size 10
        random_content = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(10)])
        with self.assertRaises(IncorrectInputDataException):
            self.factory.load_dataset(content=random_content)

    def test_load_dataset_from_empty_string(self):
        """Tests the load of a dataset from a faulty string"""
        # Generates a random string of size 10
        content = ''
        with self.assertRaises(IncorrectInputDataException):
            self.factory.load_dataset(content=content)

    def test_load_dataset_from_correct_string(self):
        """Tests the load of a dataset from a correct string"""
        dataset = self.factory.load_dataset(content=self.file_content)
        third_dict = json.loads("""{"ts": 1393631989, "visitor_uuid": "745409913574d4c6", "visitor_source": "external", "visitor_device": "browser", "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]", "visitor_ip": "0e1c9cd3d6c22c65", "visitor_country": "MX", "visitor_referrer": "ab11264107143c5f", "env_type": "reader", "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", "event_type": "pageread", "subject_type": "doc", "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", "subject_page": 23}""")


        self.assertDictEqual(third_dict,dataset.get_item(2, as_dict=True))

    def test_get_operator_none(self):
        """Tests the loading of an operator when given None argument"""
        with self.assertRaises(IncorrectInputDataException):
            self.factory.get_operator(None)

    def test_get_operator_wrong_type(self):
        """Tests the loading of an operator when given wrongly typed argument"""
        with self.assertRaises(IncorrectInputDataException):
            self.factory.get_operator(5)
    
    def test_get_operator(self):
        """Tests the correct loading of an operator"""
        dataset = self.factory.load_dataset(content=self.file_content)
        self.assertTrue(isinstance(self.factory.get_operator(dataset), AbstractOperator))

    def test_dataset_size(self):
        """Tests the case of a non existing file or None string passed"""  

        dataset = self.factory.load_dataset(content=self.file_content)

        self.assertEqual(dataset.size(), 4, "Dataset is sized as expected")

    def test_dataset_get_item_negative_out_of_bound(self):
        """Tests the case of an out of bound index (< 0)"""

        dataset = self.factory.load_dataset(content=self.file_content)

        with (self.assertRaises(IndexError)):
            dataset.get_item(-1)
    
    def test_dataset_get_item_out_of_upper_bound(self):
        """Tests the case of an out of bound index (>= size)"""

        dataset = self.factory.load_dataset(content=self.file_content)

        with (self.assertRaises(IndexError)):
            dataset.get_item(-1)

    def test_dataset_get_item(self):
        """Tests the load of a dataset from a correct string"""
        dataset = self.factory.load_dataset(content=self.file_content)
        first_dict = json.loads("""{"ts": 1393631989, "visitor_uuid": "745409913574d4c6", "visitor_source": "external", "visitor_device": "browser", "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]", "visitor_ip": "0e1c9cd3d6c22c65", "visitor_country": "MX", "visitor_referrer": "ab11264107143c5f", "env_type": "reader", "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", "event_type": "impression", "subject_type": "doc", "subject_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", "subject_page": 23, "cause_type": "page"}""")

        self.assertDictEqual(first_dict,dataset.get_item(0, as_dict=True))

    def test_view_by_browser_not_simplified(self):
        """Tests view by browser"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)

        val_count = operator.view_by_browser(plot=False)

        self.assertEqual(val_count[0], 2)
        self.assertEqual(val_count.size, 3)
        self.assertEqual(val_count.keys()[0],
        "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]")

    def test_view_by_browser_simplified(self):
        """Tests view by browser with simplified data"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.view_by_browser(simplified=True, plot=False)

        self.assertEqual(val_count[0], 4)
        self.assertEqual(val_count.size, 1)
        self.assertEqual(val_count.keys()[0], "Mozilla")

    def test_view_by_country_unexisting_doc_code(self):
        """Tests view by country with non existing document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.view_by_country(doc_id="schmilblick", plot=False)

        self.assertEqual(val_count.size, 0)
    
    def test_view_by_country_none_doc_code(self):
        """Tests view by country with None document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        with self.assertRaises(IncorrectInputDataException):
            _ = operator.view_by_country(doc_id=None, plot=False)

    def test_view_by_country_existing_doc_code(self):
        """Tests view by country with existing document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.view_by_country(doc_id="140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", plot=False)

        self.assertEqual(val_count[0], 2)
        self.assertEqual(val_count.size, 1)
        self.assertEqual(val_count.keys()[0], "MX")

    def test_view_by_continent_unexisting_doc_code(self):
        """Tests view by country with non existing document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.view_by_continent(doc_id="schmilblick", plot=False)

        self.assertEqual(val_count.size, 0)
    
    def test_view_by_continent_none_doc_code(self):
        """Tests view by country with None document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        with self.assertRaises(IncorrectInputDataException):
            _ = operator.view_by_continent(doc_id=None, plot=False)

    def test_view_by_continent_existing_doc_code(self):
        """Tests view by country with existing document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.view_by_continent(doc_id="140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", plot=False)

        self.assertEqual(val_count[0], 2)
        self.assertEqual(val_count.size, 1)
        self.assertEqual(val_count.keys()[0], "NA")

    def test_also_likes_unexisting_doc_code(self):
        """Tests also likes functionality with non existing document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.also_likes(doc_id="schmilblick", plot=False)

        self.assertEqual(type(val_count), np.ndarray)
        self.assertEqual(val_count.size, 0)

    def test_also_likes_none_doc_code(self):
        """Tests also likes functionality with None document code"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        
        with self.assertRaises(IncorrectInputDataException):
            _ = operator.also_likes(doc_id=None, plot=False)

    def test_also_likes_existing_doc_code(self):
        """Tests also likes functionality with existing document code"""
        file_content_up = self.file_content +"""
                {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "pageread",    "subject_type": "doc",    "subject_doc_id": "130325130327-d5889c2cf2e642b6867cb9005e12297f",    "subject_page": 23,    "cause": null }
        """
        dataset = self.factory.load_dataset(content=file_content_up)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.also_likes(doc_id="140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", plot=False)

        self.assertEqual(type(val_count), np.ndarray)
        self.assertEqual(val_count.size, 1)
        self.assertEqual(val_count[0], "130325130327-d5889c2cf2e642b6867cb9005e12297f")

    def test_also_likes_existing_doc_code_nonexisting_user(self):
        """Tests also likes functionality with existing document code and unknown user id"""
        file_content_up = self.file_content +"""
                {   "ts": 1393631989,    "visitor_uuid": "745409913574d4c6",    "visitor_username": null,    "visitor_source": "external",    "visitor_device": "browser",    "visitor_useragent": "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]",    "visitor_ip": "0e1c9cd3d6c22c65",    "visitor_country": "MX",    "visitor_referrer": "ab11264107143c5f",    "env_type": "reader",    "env_doc_id": "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0",    "env_adid": null,    "event_type": "pageread",    "subject_type": "doc",    "subject_doc_id": "130325130327-d5889c2cf2e642b6867cb9005e12297f",    "subject_page": 23,    "cause": null }
        """
        dataset = self.factory.load_dataset(content=file_content_up)
        operator = self.factory.get_operator(dataset)
        
        val_count = operator.also_likes(doc_id="140228202800-6ef39a241f35301a9a42cd0ed21e5fb0", user_id="schmilblick", plot=False)

        self.assertEqual(type(val_count), np.ndarray)
        self.assertEqual(val_count.size, 1)

    def test_launch_gui_none(self):
        """Tests the loading of the GUI when given None argument"""
        with self.assertRaises(IncorrectInputDataException):
            self.factory.launch_GUI(None)

    def test_launch_gui_wrong_type(self):
        """Tests the launch of the GUI when given wrongly typed argument"""
        with self.assertRaises(IncorrectInputDataException):
            self.factory.launch_GUI(5)
    
    def test_launch_gui(self):
        """Tests the correct loading of the GUI"""
        dataset = self.factory.load_dataset(content=self.file_content)
        operator = self.factory.get_operator(dataset)
        self.assertTrue(isinstance(self.factory.launch_GUI(operator), AbstractGUI))
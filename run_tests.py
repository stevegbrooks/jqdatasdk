
import AbstractTest
import jqdatasdk as jq
import utils
import re

from importlib import reload
_ = reload(AbstractTest)
_ = reload(utils)
_ = reload(jq)

import unittest

class TestInit(unittest.TestCase):
    def test_init(self):
        """
        Test that the imported JQDataSDK lib is the local one
        """
        self.assertTrue(jq.__version__ == "2.0.0")

class TestGetPrice(AbstractTest.TestWaffleWrap): 
    function = jq.get_price
    def test_definition(self):
        actual_func_def = self.get_definition(self.function)
        self.assertEqual(
            actual_func_def, 
            "get_price(tickers, start_date=None, end_date=None, \
                       frequency='daily', fields=None, count=None, \
                       skip_paused=False, fq='pre', panel=True, \
                       fill_paused=True)"
        )

if __name__ == '__main__':
    utils.jq_login("secret.yml")
    unittest.main()
    jq.logout()

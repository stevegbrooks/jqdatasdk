
import AbstractTest
import jqdatasdk as jq
import utils

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

if __name__ == '__main__':
    utils.jq_login("secret.yml")
    unittest.main()
    jq.logout()

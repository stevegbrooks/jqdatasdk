from importlib import reload
import pandas as pd
import utils
import jqdatasdk as jq
_ = reload(utils)
_ = reload(jq)

import unittest

class TestInputs(unittest.TestCase):
    
    def test_get_price(self):
        """
        Test that the get_price function's first param is called 'tickers'.
        (This is the only test needed for this function.)
        """
        #tests that its called 'tickers'
        jq.get_price(tickers = ['000001.XSHE', '000002.XSHE'], count = 1)
        #tests that its first
        jq.get_price(['000001.XSHE', '000002.XSHE'], count = 1)
        #tests that passing a single ticker has the same output as a list of tickers of len = 1
        df_actual = jq.get_price('000001.XSHE', count = 1)
        df_expected = jq.get_price(['000001.XSHE'], count = 1)
        self.assertTrue(df_actual.equals(df_expected))


class TestOutputs(unittest.TestCase):

    def test_get_price(self):
        """
        Test that the get_price function returns a pandas dataframe
        """
        df = jq.get_price('000001.XSHE', count = 1)
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    utils.jq_login("secret.yml")
    unittest.main()
    jq.logout()

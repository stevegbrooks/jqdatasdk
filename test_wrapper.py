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
        jq.get_price(tickers = ['000001.XSHE', '000002.XSHE'], count = 1)
        jq.get_price(['000001.XSHE', '000002.XSHE'], count = 1)


class TestOutputs(unittest.TestCase):

    def test_get_price(self):
        """
        Test that the get_price function returns a pandas dataframe
        """
        df = jq.get_price('000001.XSHE', start_date='2015-01-01', end_date='2015-01-02')
        self.assertIsInstance(df, pd.DataFrame)

if __name__ == '__main__':
    utils.jq_login("secret.yml")
    unittest.main()
    jq.logout()

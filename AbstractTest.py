import unittest
import pandas as pd

class TestWaffleWrap(unittest.TestCase):

    function = None
    
    def test_definition(self):
        """
        Test that the function definition aligns with Google Sheet specs
        """
        #has params called 'tickers' and 'count'
        self.function(tickers = '000001.XSHE', count = 1)
        #tickers is first param
        self.function('000001.XSHE', count = 1)
    
    def test_tickers_param(self):
        """
        Tests that passing a single ticker has the same output 
        as a list of tickers of len = 1
        """
        df_actual = self.function(tickers = '000001.XSHE', count = 1)
        df_expected = self.function(tickers = ['000001.XSHE'], count = 1)
        self.assertTrue(df_actual.equals(df_expected))

    def test_output_type(self):
        """
        Test that the function returns a pandas dataframe
        """
        df = self.function(tickers = '000001.XSHE', count = 1)
        self.assertIsInstance(df, pd.DataFrame)
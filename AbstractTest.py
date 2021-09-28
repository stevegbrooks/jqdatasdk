import unittest
import pandas as pd
import inspect
import re

class TestWaffleWrap(unittest.TestCase):

    function = None

    def get_definition(self, function):
        """
        Get the function definition from the function's source code
        """
        source = inspect.getsource(function)
        #grab everything between def and :
        regex = re.compile(r'(?=(def ))([^:]*)') 
        if len(regex.findall(source)[0]) > 0:
            #extract function definition and clean up
            func_def = regex.findall(source)[0][1]
            func_def = re.sub(r'\s+', ' ', func_def)
            func_def = re.sub(r'\n', ' ', func_def)
            func_def = re.sub(r'\t', ' ', func_def)
            return func_def
        else:
            raise ValueError('Function definition not found')
    
    def test_definition(self):
        """
        Test that the function definition aligns with Google Sheet specs
        This test is so variable from function to function, 
        that we define it separately each time
        """
        raise NotImplementedError 
    
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
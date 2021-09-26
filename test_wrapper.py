from importlib import reload
import utils
import jqdatasdk as jq
_ = reload(utils)
_ = reload(jq)

import unittest

class TestInputs(unittest.TestCase):
    
    def test_get_price():
        pass


if __name__ == '__main__':
    utils.jq_login("secret.yml")
    unittest.main()





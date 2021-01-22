"""Testing code for null_count function from helper_functions"""

import unittest
import pandas as pd
from lambdata_temsychen.helper_functions import null_count

df = pd.read_csv(
     'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')

class TestHelperFunctions(unittest.TestCase):

    def test_null_count(self):
        self.assertEqual(null_count(df), None)


if __name__ == '__main__':
    unittest.main()

    

import unittest
import pandas as pd
import sys,os
import dvc.api
from tqdm import tqdm as tq

# for i in tq(range(1),desc="fetching data \n "):
data_url=dvc.api.get_url('data/final_data.csv','https://github.com/Blvisse/Breast-Cancer-Causality.git','data-v2')
data=pd.read_csv(data_url)

class TestData(unittest.TestCase):

    def test_checkNulls(self):
    
        for i in tq(range(1),desc="carrying out test"):
             pass

        self.assertEqual(data['diagnosis'].isnull().sum(),0)

        
    def check_duplicates(self):
            
        for i in tq(range(1),desc="carrying  test for duplicate entries"):
            pass
        dupCount=len(data)-len(data.drop_duplicates())
        self.assertEqual(dupCount,0)


if __name__ == '__main__':
    unittest.main()
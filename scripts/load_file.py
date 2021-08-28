import pandas as pd
import dvc.api
from tqdm import tqdm as tq
import logging
import sys


# logging.basicConfig(filename='..\logs\load_data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


"""
This script loads data from the dvc remote storage 

"""

def get_data(storage,repo,version):

    try:
        for i in tq(range(1), desc="Loading data from dvc"):
            logging.info("Loading data from dvc storage")
            data=dvc.api.get_url(storage,repo,version)
            data=pd.read_csv(data)
        return data

    except Exception as e:
        logging.error("System run into an error safely exiting")
        print ( "System run into an error" )
        sys.exit(1)


if (__name__== '__main__'):
    data=get_data('data/final_data.csv','https://github.com/Blvisse/Breast-Cancer-Causality.git','data-v2')
    print(data)
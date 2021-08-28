import pandas as pd
import numpy as np
import logging
from tqdm import tqdm as tq 

logging.basicConfig(filename='..\logs\data_prep.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)



#calculating the number of null values
def null_values(df):
    
    #get the number of null values in the system
    try:
        print(" #### Calculating Missing Values ##### \n")
        for i in tq(range(1),desc="Fetching data"):
        
            logging.info("#### Calculating missing values #### \n")
            
            sumofNull=df.isna().sum()
            percentage=sumofNull/len(df)*100
        print(" #### Done #### \n ")
            
            
        
        print("#### Creating data frame #### \n ")
        
        for i in tq(range(1),desc="Creating DataFrame"):
            valuesdf=pd.DataFrame(data=[sumofNull,percentage])
            valuesdf=valuesdf.T
            valuesdf.columns=["Total Missing","Percentage Missing"]
        print(" #### Done #### ")
        logging.info("Missing values calculated")

        return valuesdf
            
    except Exception as e:
        
        print(" !!! Error File Not Found  !!!!! \n")
        print(" !!! Program Failed !!!!! \n")
        logging.error(" !!! Error Program Failed !!!!! \n")
        logging.error("Safely exiting the program")
        print("Safely exiting the program")
        sys.exit(1)


#get duplicate count 
def dropDuplicates(data):
    try:
        df=pd.read_csv(data)
        
        logging.debug("Launching duplicates search")
        for i in tq(range(1),desc="Detecting duplicates"):

            
            df=df.drop_duplicates()
            
        for i in tq(range(1),desc="Report on Duplicates "):
            dupCount=len(df)-len(df.drop_duplicates())
                
        print ("There are {} duplicates in the dataset\n".format(dupCount))
        logging.info("Number of duplicates in the datset are {} ".format(dupCount))

            

        return data 
    except Exception as e:
        logging.info("An error has occured")
        logging.error("The follocing error occured {} ".format(e.__class__))
        print("The following error occured {} ".format(e.__class__))


if (__name__== '__main__'):
    dropDuplicates('../data/final_data.csv')
    
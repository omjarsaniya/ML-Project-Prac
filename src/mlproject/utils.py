import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv # pyright: ignore[reportMissingImports]
import pymysql # pyright: ignore[reportMissingModuleSource]

import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


load_dotenv()
host=os.getenv('host') 
user=os.getenv('user')
password=os.getenv('password')
db=os.getenv('db')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established successfully", mydb)
        df=pd.read_sql_query("SELECT * FROM students", mydb)
        print(df.head())

        return df
    
    except Exception as e:
        raise CustomException(e,sys)
    


def save_object(file_path, obj):
    try:
        logging.info("Saving object started")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
        
        logging.info(f"Object saved successfully at {file_path}")
    
    except Exception as e:
        logging.error(f"Error saving object: {e}")
        raise CustomException(e, sys)
    

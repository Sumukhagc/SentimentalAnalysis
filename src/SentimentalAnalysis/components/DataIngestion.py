from src.SentimentalAnalysis.entity import DataIngestionConfig
from src.SentimentalAnalysis.logging import logger
from pathlib import Path
import zipfile
import os
import urllib.request as request  

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_data(self):
        if(not os.path.exists(self.config.local_data_file)):
            filename,headers=request.urlretrieve(self.config.source_url,self.config.local_data_file)
            logger.info("Downloaded the data successfully")
        else:
            logger.info("Data already exists")

    def unzip_data(self):
        unzip_dir_path=self.config.root_dir
        os.makedirs(unzip_dir_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_dir_path)

            
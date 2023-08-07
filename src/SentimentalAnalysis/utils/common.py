import os
from pathlib import Path
from src.SentimentalAnalysis.logging import logger
import yaml
import dill 

def read_yaml(path:Path):
    try:
        with open(path) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info("Successfully read the yaml file")
            return content
    except:
        raise Exception("Failed to load yaml file")

def create_directories(directories:list):
    for directory in directories:
        os.makedirs(directory,exist_ok=True)
        logger.info("Created file successfully ")

def getsize(path):
    return os.path.getsize(path)        


def save_obj(file_path,obj):
    try:
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj) 
    except Exception as e:
        raise Exception(e)

def load_model(file_path):
    try:
        with open(file_path,"rb") as f:
            obj= dill.load(f)
            return obj

    except Exception as e:
        raise Exception(e)       
import os
from pathlib import Path
from src.SentimentalAnalysis.logging import logger
import yaml
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
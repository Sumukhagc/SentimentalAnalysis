from src.SentimentalAnalysis.pipeline.DataIngestionPipeline import DataIngestionPipeline
from src.SentimentalAnalysis.pipeline.DataTransformationPipeline import DataTransformationPipeline
from src.SentimentalAnalysis.pipeline.ModelTrainerPipeline import ModelTrainerPipeline
from src.SentimentalAnalysis.logging import logger
from tensorflow.keras.models import load_model
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import re
import pickle
try:
    data=DataIngestionPipeline()
    data.main()
except Exception as e:
    logger.info("Exception ",e)   

try:
    data=DataTransformationPipeline()
    X,Y,embedding_layer=data.main()
except Exception as e:
    logger.info("Exception ",e)   

try:
    model=ModelTrainerPipeline()
    model.main(X,Y,embedding_layer)
except Exception as e:
    logger.info("Exception ",e)       


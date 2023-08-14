import re
from src.SentimentalAnalysis.constants import URL_PATTERN,USER_PATTERN,HASHTAG_PATTERN
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from src.SentimentalAnalysis.utils.common import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
class PredictionPipeline:
    def __init__(self) -> None:
        self.lemmatizer=WordNetLemmatizer()
        None
    def preprocess(self,text):
        review=re.sub('@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+',' ',text)
        review=review.lower()
        review=review.split()
        review=[word for word in review if not word in stopwords.words('english')]
        tokenizer=load_model('artifacts/data_transformation/tokens.pkl')
        review=pad_sequences(tokenizer.texts_to_sequences([review]), maxlen=300)
        return review
    
    def predict(self,tweet:str):
        model=load_model('artifacts/model_trainer/sentiment.pkl')
        result=model.predict(self.preprocess(tweet))
        return result
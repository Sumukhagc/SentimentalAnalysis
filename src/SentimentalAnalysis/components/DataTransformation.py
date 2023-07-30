from src.SentimentalAnalysis.config.configuration import DataTransformationConfig
import nltk
import re
import os
import dill
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.SentimentalAnalysis.constants import *
import pandas as pd
import tensorflow
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences
from src.SentimentalAnalysis.logging import logger
import joblib
class DataTransformation:
    def __init__(self,config:DataTransformationConfig) -> None:
        self.config=config
        self.lemmatizer=WordNetLemmatizer()
        nltk.download('omw-1.4')
        nltk.download('punkt')
        self.stop_words=set(stopwords.words('english'))
        
    def preprocess(self,tweet:str):
        tweet=tweet.lower()
        tweet=re.sub(USER_PATTERN,'',tweet)
        tweet=re.sub(HASHTAG_PATTERN,'',tweet)
        tweet=re.sub(URL_PATTERN,'',tweet)
        tweet=re.sub('[^A-Za-z0-9]',' ',tweet)
        tweet=[self.lemmatizer.lemmatize(word) for word in tweet.split() if not word in self.stop_words]
        tweet=" ".join(tweet)
        return tweet    

    def load_data(self):
        data_path=self.config.data_path
        data=pd.read_csv(data_path,encoding='latin',names=['sentiment','tweet_num','timestamp','flag','twitter_id','tweet'])
        data.drop(['tweet_num','timestamp','flag','twitter_id'],inplace=True,axis=1)
        return data
    
    def transform_data(self):
        data=self.load_data()
        data['tweet']=data['tweet'].apply(self.preprocess) 
        one_hot_representation=[one_hot(sentence,vocabulary_size) for sentence in data['tweet']]
        embedded_docs=pad_sequences(one_hot_representation,maxlen=sentence_length,padding='post')
        path=self.config.root_dir
        file_path=os.path.join(path,'preprocessor.pkl')
        with open(file_path,'w') as f:
            logger.info(f"Created pickle file")

        with open(file_path,"wb") as file_obj:
            dill.dump(embedded_docs,file_obj) 
        logger.info('Data transformation done..')
        

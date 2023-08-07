from src.SentimentalAnalysis.config.configuration import DataTransformationConfig
import nltk
import re
import os
import dill
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from src.SentimentalAnalysis.constants import *
import pandas as pd
from gensim.models.word2vec import Word2Vec
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Embedding
from sklearn.model_selection import train_test_split
from src.SentimentalAnalysis.logging import logger
from src.SentimentalAnalysis.utils.common import save_obj
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
        logger.info("data loading done" )
        return data

    def split_data(self,X,Y):
        X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,random_state=42)
        return X_train,X_test,Y_train,Y_test

    def transform_data(self):
        data=self.load_data()
        data['tweet']=data['tweet'].apply(self.preprocess)
        logger.info("Preprocess done")
        X=data['tweet']
        Y=data['sentiment'] 
        Y=Y.replace({4:1})
        documents=[sentence.split() for sentence in X]
        w2_vec_model=Word2Vec(vector_size=100, window=5, min_count=3, workers=4)
        w2_vec_model.build_vocab(documents)
        w2_vec_model.train(documents,total_words=len(documents),epochs=25)
        tokenizer=Tokenizer()
        tokenizer.fit_on_texts(X)
        tokenizer_path=os.path.join(self.config.root_dir,'tokens.pkl')
        save_obj(tokenizer_path,tokenizer)
        X=pad_sequences(tokenizer.texts_to_sequences(X),maxlen=50,padding='pre')
        X_train,X_test,Y_train,Y_test=self.split_data(X,Y)
        X_train_path=os.path.join(self.config.root_dir,'X_train.pkl')
        X_test_path=os.path.join(self.config.root_dir,'X_test.pkl')
        Y_train_path=os.path.join(self.config.root_dir,'Y_train.pkl')
        Y_test_path=os.path.join(self.config.root_dir,'Y_test.pkl')
        save_obj(X_train_path,X_train)
        save_obj(X_test_path,X_test)
        save_obj(Y_train_path,Y_train)
        save_obj(Y_test_path,Y_test)
        vocabulary_size=len(tokenizer.word_index)+1
        embedding_matrix=np.zeros((vocabulary_size,100))
        logger.info("Embedding matrix created")
        for word,i in tokenizer.word_index.items():
            if word in w2_vec_model.wv:
                embedding_matrix[i]=w2_vec_model.wv[word]   
        embedding_layer = Embedding(vocabulary_size, 100, weights=[embedding_matrix], trainable=False)
        logger.info("Embedding done")
        path=os.path.join(self.config.root_dir,'embeddings.pkl')
        save_obj(path,embedding_layer)
        return X,Y,embedding_layer
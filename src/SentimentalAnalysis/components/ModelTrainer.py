import os
from src.SentimentalAnalysis.entity import ModelTrainerConfig 
from src.SentimentalAnalysis.constants import *
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM,Bidirectional,Embedding,Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping
import pickle
import pandas as pd
import numpy as np
from src.SentimentalAnalysis.utils.common import load_model
from src.SentimentalAnalysis.logging import logger
class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig) -> None:
        self.config=config


    def train_model(self,A,B,layer):
        embedding_layer=load_model('artifacts/data_transformation/embeddings.pkl')
        model=Sequential([
        embedding_layer,
        Dropout(0.4),
        LSTM(units=100,dropout=0.2,recurrent_dropout=0.2),
        Dense(units=16,activation='relu'),
        Dense(units=1,activation='sigmoid')
])
        
        model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
        X_train=load_model('artifacts/data_transformation/X_train.pkl')
        Y_train=load_model('artifacts/data_transformation/Y_train.pkl')
        history=model.fit(x=X_train,y=Y_train,batch_size=1024,epochs=15,validation_split=0.2)
        self.save_model(model)
    
    def save_model(self,model):
        file_path=os.path.join(self.config.root_dir,'model.h5')
        model.save(file_path)
        

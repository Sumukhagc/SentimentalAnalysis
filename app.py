from src.SentimentalAnalysis.pipeline.DataIngestionPipeline import DataIngestionPipeline
from src.SentimentalAnalysis.pipeline.DataTransformationPipeline import DataTransformationPipeline
from src.SentimentalAnalysis.pipeline.ModelTrainerPipeline import ModelTrainerPipeline
from src.SentimentalAnalysis.pipeline.PredictionPipeline import PredictionPipeline
from src.SentimentalAnalysis.logging import logger
from tensorflow.keras.models import load_model
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import re
import pickle
from flask import Flask,render_template,redirect,request


app=Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/predict',methods=['GET','POST'])
def result():
   if request.method == 'POST':
      tweet = request.form['tweet']
      print(type(tweet))
      prediction_pipeline=PredictionPipeline()
      result=prediction_pipeline.predict(tweet)
      result=float(result[0][0])
      if result>=0.5:
         sentiment='positive'
      else:
         sentiment='negetive'   
      
      return render_template("predict.html",sentiment=sentiment)

if __name__ == '__main__':
   app.run(debug = True)
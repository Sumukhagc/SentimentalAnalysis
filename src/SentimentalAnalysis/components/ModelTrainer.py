from src.SentimentalAnalysis.entity import ModelTrainerConfig 
import pickle
class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig) -> None:
        self.config=config

    def load_preprocessor_model(self):
        data_path=self.config.data_path
        file = open(data_path,'rb')
        preprocessed_model=pickle.load(file)
        


        

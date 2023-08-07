from src.SentimentalAnalysis.components.ModelTrainer import ModelTrainer
from src.SentimentalAnalysis.config.configuration import ConfigurationManager
from src.SentimentalAnalysis.entity import ModelTrainerConfig

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self,X,Y,embedding_layer):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model=ModelTrainer(model_trainer_config)
        model.train_model(X,Y,embedding_layer)
        


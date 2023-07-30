from src.SentimentalAnalysis.components.ModelTrainer import ModelTrainer
from src.SentimentalAnalysis.config.configuration import ConfigurationManager
from src.SentimentalAnalysis.entity import ModelTrainerConfig

class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model=ModelTrainer(model_trainer_config)
        model.load_preprocessor_model()



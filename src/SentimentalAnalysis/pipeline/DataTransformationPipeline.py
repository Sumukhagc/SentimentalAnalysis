from src.SentimentalAnalysis.components.DataTransformation import DataTransformation
from src.SentimentalAnalysis.config.configuration import ConfigurationManager
from src.SentimentalAnalysis.entity import DataTransformationConfig
class DataTransformationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(data_transformation_config)
        data_transformation.transform_data()
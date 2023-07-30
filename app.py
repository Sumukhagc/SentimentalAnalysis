from src.SentimentalAnalysis.pipeline.DataIngestionPipeline import DataIngestionPipeline
from src.SentimentalAnalysis.pipeline.DataTransformationPipeline import DataTransformationPipeline
from src.SentimentalAnalysis.pipeline.ModelTrainerPipeline import ModelTrainerPipeline
from src.SentimentalAnalysis.logging import logger
try:
    data=DataIngestionPipeline()
    data.main()
except Exception as e:
    logger.info("Exception ",e)   

try:
    data=DataTransformationPipeline()
    #data.main()
except Exception as e:
    logger.info("Exception ",e)   

try:
    model=ModelTrainerPipeline()
    model.main()
except Exception as e:
    logger.info("Exception ",e)       
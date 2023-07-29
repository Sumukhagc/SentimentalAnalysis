from src.SentimentalAnalysis.pipeline.DataIngestionPipeline import DataIngestionPipeline
from src.SentimentalAnalysis.logging import logger
try:
    data=DataIngestionPipeline()
    data.main()
except Exception as e:
    logger.info("Exception ",e)   
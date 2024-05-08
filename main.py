from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngesionTrainingPipeline
from cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
    obj = DataIngesionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
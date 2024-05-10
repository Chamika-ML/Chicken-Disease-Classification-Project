from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngesionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrePareBaseModelTrainingPipeline
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


STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
    obj = PrePareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
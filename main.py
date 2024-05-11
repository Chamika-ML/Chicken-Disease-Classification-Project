from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngesionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrePareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeLine
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


STAGE_NAME = "Evaluation stage"

try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e




try:
    logger.info(f"****************************")
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    obj = EvaluationPipeLine()
    obj.main()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<")
except Exception as e:
    raise e
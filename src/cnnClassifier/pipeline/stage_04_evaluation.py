

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Evaluation stage"

class EvaluationPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


# for dvc
if __name__ == "__main__":
    try:
        logger.info(f"****************************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = EvaluationPipeLine()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<")
    except Exception as e:
        raise e
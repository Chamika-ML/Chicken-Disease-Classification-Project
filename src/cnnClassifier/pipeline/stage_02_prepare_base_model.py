from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger

STAGE_NAME = "Prepare base model"



class PrePareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        # create dirctory and get related configuration variables
        prepare_base_model_cofig  = config.get_prepare_base_model_cofig()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_cofig)
        # donwload and update the pretrained mode
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


# for DVC 
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = PrePareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
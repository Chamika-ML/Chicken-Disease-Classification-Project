
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
STAGE_NAME = "Data Ingestion stage"

class DataIngesionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager() # create artifacts folder
            data_ingestion_config = config.get_data_ingestion_config() # return data ingestion related paths
            data_ingestion = DataIngestion(config=data_ingestion_config) # initialized data ingestion object with related paths 
            data_ingestion.download_file() # download the dataset 
            data_ingestion.extract_zip_file() # extract the downloaded data zip file to  artifacts/data_ingestion folder
        except Exception as e:
            raise e
        
# for dvc 
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
        obj = DataIngesionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

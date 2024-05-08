import os 
import urllib.request as request
import zipfile
from cnnClassifier import logger 
from cnnClassifier.utils.common import get_size
from pathlib import Path
from cnnClassifier.entity.confing_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) :
        self.config = config

    def download_file(self):
        # if the data set not downloaded previously
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"file already exist of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        # create unzip folder artifacts/data_ingestion
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        # unzip the downloaded file and saved it in artifacts/data_ingestion folder
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

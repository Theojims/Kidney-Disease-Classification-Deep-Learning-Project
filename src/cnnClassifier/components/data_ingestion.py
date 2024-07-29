from cnnClassifier import logger
from cnnClassifier.entity.config_entity import (DataIngestionConfig)
import os
import gdown
import zipfile

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config


    def download_file(self):
        try:

            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f'downloading dataset from{dataset_url} to fold{zip_download_dir}')
            prefix  = "https://drive.google.com/uc?/export=download&id="
            file_id = dataset_url.split("/")[5]
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f'downloading dataset from{dataset_url} to fold{zip_download_dir} completed')
        except Exception as e:
            raise e

    def extract_zip(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zipref:
            zipref.extractall(unzip_path)


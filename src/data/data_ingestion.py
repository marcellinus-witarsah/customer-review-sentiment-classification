import os
import sys
from dotenv import load_dotenv, find_dotenv
import zipfile
load_dotenv(find_dotenv())
sys.path.append(os.getenv("PROJECT_FOLDER"))
from src.utils.common import logger
from src.entities.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Instantiate `DataIngestion` class

        Args:
            config (DataIngestionConfig): configuration for data ingestion
        """
        logger.info("Instantiate `DataIngestion` class")
        self.config = config

    def extract_zip_file(self):
        """Extract `.zip` file"""
        logger.info("Extract .zip file")
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.source_path, "r") as zip_ref:
            zip_ref.extractall(unzip_dir)
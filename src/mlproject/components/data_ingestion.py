import os
from pathlib import Path

import urllib.request as request
import zipfile
from src.mlproject import logger
from src.mlproject.utils.common import get_size
from src.mlproject.entity.config_entity import DataIngestionConfig
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
# Initialiser l'instance de DataIngestion avec sa configuration spécifique.

    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_dir,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

#S'assurer que le fichier de données est disponible localement (et éviter de le télécharger plusieurs fois inutilement).

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
  #Décompresser les fichiers de données pour pouvoir ensuite les utiliser dans le pipeline (préparation, nettoyage, transformation, etc.
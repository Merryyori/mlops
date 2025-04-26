from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml, create_directories
from pathlib import Path
from src.mlproject.entity.config_entity import DataIngestionConfig
from src.mlproject.entity.config_entity import DataValidationConfig
CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
#Crée le répertoire racine défini dans config.yaml, probablement pour stocker les résultats ou fichiers intermédiaires (artifacts).

    #accessing the data from  config
    def get_data_ingestion_config(self) -> DataIngestionConfig: # we only need to return the variabls defined 
        #Prépare la configuration pour l’étape de data ingestion (chargement initial des données).
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_dir=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )
#Instancie un objet DataIngestionConfig (probablement un @dataclass) avec les valeurs extraites du YAML.
        return data_ingestion_config
        #Retourne cette config à une autre partie du pipeline, qui s’en servira pour télécharger et préparer les données.

           
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
    


    
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
#information label
#timestamp that the code was executed and the error message
project_name="mlproject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init _. py",
    f"src/{project_name}/components/_init _. py",
    f"src/{project_name}/utils/_init _. py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/_init _. py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/_init _. py",
    f"src/{project_name}/entity/_init _. py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/_init _. py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filepath in list_of_files:
    filepath = Path(filepath) #convertir chaque ligne en windows path
    filedir, filename = os.path.split(filepath)

    if filedir !="": #if folder directory is not empty
        os.makedirs(filedir, exist_ok=True)  # Fixed: Changed `exit_ok` to `exist_ok`
        logging.info(f"Creating directory: {filedir} for the file : {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open (filepath,"w") as f: #trying to create a file
            pass
        logging.info(f"creating empty files : {filepath}") #try to log the information

    else:
        logging.info(f"{filename} is already exists")
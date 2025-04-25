import os
import sys
import logging
#initializing loging stream: starting at asctime then it will save the log level
#and witch module u're running this code
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"



log_dir="logs" #creating log folder
log_filepath= os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #it will save all the loogins
        
        logging.StreamHandler(sys.stdout)#print my log in my terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")#initalizing logging
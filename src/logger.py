#This is a customized logger module designed to create log files.
import os
import sys
import logging
from pathlib import Path
from datetime import datetime

#Defining a logging function
def setup_logging(log_level=logging.INFO):
    #Create log directory if it doesn't exist
    current_path=Path(__file__)
    #go to root folder
    root_path=current_path.parent.parent
    #check if the folder exist in root folder
    module_log_path=root_path/'logs'
    module_log_path.mkdir(exist_ok=True)
    #Define log filename with current datetime
    logfilename=datetime.now().strftime("logs/logs_%d-%m-%Y.log")
    
    #setup logging configuration
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s: %(levelname)s: %(filename)s: %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S',
        handlers=[
            logging.FileHandler(logfilename),
            logging.StreamHandler()
        ]
    )

"""
if(__name__=="__main__"):
    setup_logging()
    #let's see
    logging.error("Testing purpose if log is working as expected or not")"""
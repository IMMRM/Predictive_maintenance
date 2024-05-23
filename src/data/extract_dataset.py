import os
import sys
import logging
from pathlib import Path
from zipfile import ZipFile
from src.logger import setup_logging


#function to extract the zipped dataset
def extract_dataset(input_path:Path,output_path:Path):
    with ZipFile(file=input_path) as f:
        f.extractall(path=output_path)
        input_file_name=input_path.stem+input_path.suffix

def main():
    #current_file_path
    current_file_path=Path(__file__)
    #go to root
    root=current_file_path.parent.parent.parent
    #raw data directory path
    raw_data=root/'data'/'raw'
    #output path
    output_data=root/'data'/'extracted'
    #make directory for output
    output_data.mkdir(exist_ok=True)
    #input path for zip files
    input_path=root/'data'/'raw'
    setup_logging()
    logging.info("The extraction of file {0} is started".format(input_path/'zipped_data.zip'))
    extract_dataset(input_path/'zipped_data.zip',output_path=output_data)
    logging.info("The file {0} has been successfully extracted from {1} to {2}".format(input_path/'zipped_data.zip',input_path,output_data))

if(__name__=="__main__"):
    main()

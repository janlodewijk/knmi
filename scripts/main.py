from dotenv import load_dotenv
from utils import setup_logger
from extract import extract
import os
import logging

load_dotenv()

if __name__ == '__main__':
    setup_logger()
    logging.basicConfig(level=logging.INFO)

url = 'https://api.dataplatform.knmi.nl/open-data/v1/datasets/knmi_synop_hourly_decoded/versions/1/files'
api_key = os.getenv('knmi_api')

file_path = extract(url, api_key)
print(file_path)
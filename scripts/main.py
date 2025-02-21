from dotenv import load_dotenv
from utils import setup_logger
from extract import extract
from transform import transform
import os
import logging

load_dotenv()

if __name__ == '__main__':
    setup_logger()
    logging.basicConfig(level=logging.INFO)

url = 'https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/vorigemaand.zip'
api_key = os.getenv('knmi_api')

extract(url)

file_path = 'data/raw/vorigemaand.txt'

df = transform(file_path)

print(df.head())
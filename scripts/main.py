from dotenv import load_dotenv
from utils import setup_logger
from extract import extract
from load import load
from transform import transform
import os
import logging



load_dotenv()

if __name__ == '__main__':
    setup_logger()
    logging.basicConfig(level=logging.INFO)

url = 'https://cdn.knmi.nl/knmi/map/page/klimatologie/gegevens/uurgegevens/vorigemaand.zip'
api_key = os.getenv('knmi_api')
file_path = 'data/raw/vorigemaand.txt'

# Perform the ETL process
extract(url)
df = transform(file_path)
load(df)
print(df.shape)
print(df.nunique())
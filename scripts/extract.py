import requests
from dotenv import load_dotenv
import os

load_dotenv()

params = {
    'api_key': os.getenv('knmi_api')
}

response = requests.get(url='https://api.dataplatform.knmi.nl/open-data/v1/datasets/knmi_synop_hourly_decoded/versions/1/files', params=params)
response.raise_for_status()
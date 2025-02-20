import requests
import logging
from datetime import datetime
import os

def extract(url, api_key, save_path='data/raw'):
    """
    Extracts data from the KNMI API.
    
    Args:
        api_key (str): The API key for the KNMI API.

    Returns:
        Raw data from the KNMI API.
    """
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    try:
        # Make a GET request to the KNMI API
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logging.info('Successful API request')
        
        #Parse the JSON response and retrieve the keys
        json_response = response.json()['files']
        
        # Convert last modified date to datetime object
        for i in json_response:
            i['lastModified'] = datetime.strptime(i['lastModified'], '%Y-%m-%dT%H:%M:%S%z')
        
        # Identify the file with the max timestamp
        latest_file = max(json_response, key=lambda x: x['lastModified'])
        
        # Retrieve only the filename of the file with the max timestamp
        latest_file_name = latest_file['filename']
        logging.info(f'Latest file found: {latest_file_name}')
        
        # Use the extracted filename to download the file
        download_url = f'https://api.dataplatform.knmi.nl/open-data/v1/datasets/knmi_synop_hourly_decoded/versions/1/files/{latest_file_name}'
        
        try:
            # Make a GET request to the download the file
            response_2 = requests.get(download_url, headers=headers)
            response_2.raise_for_status()
            logging.info(f'Successful file downloaded {latest_file_name}')
            
            # Make sure the save path exists
            os.makedirs(save_path, exist_ok=True)
            
            # Save the file to the specified path
            file_path = os.path.join(save_path, latest_file_name)
            with open(file_path, 'wb') as file:
                file.write(response_2.content)
                logging.info(f'File saved to {file_path}')
                return file_path            
            
        except requests.exceptions.RequestException as e:
            logging.error(f'Error during file download: {e}')
            return None
         
    except requests.exceptions.RequestException as e:
        logging.error(f'Error during API request: {e}')
        return None
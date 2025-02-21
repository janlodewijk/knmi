import requests
import logging
import os
from zipfile import ZipFile

def extract(url, save_path='data/raw/'):
    """
    Extracts weather data from the last month from the KNMI API.
    
    Args:
        url (str): The download URL.

    Returns:
        Weather data from the last month.
    """
    
    try:
        # Make a GET request to download the file
        response = requests.get(url)
        response.raise_for_status()
        logging.info('Succesful URL request')
        
        knmi_data = response.content
        
        # Make sure the save path exists
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        # Save the file to the specified path:
        with open(os.path.join(save_path, 'data.zip'), 'wb') as f:
            f.write(knmi_data)
            logging.info('Zip file saved')

        # Extract the data from the zip file
        try:
            with ZipFile(os.path.join(save_path, 'data.zip'), 'r') as zip_ref:
                zip_ref.extractall(save_path)
                logging.info('Zip file unzipped')
                
                # Close the zip file
                zip_ref.close()
                
                # Remove the zip file
                os.remove(os.path.join(save_path, 'data.zip'))
                logging.info('Original zip file removed')
                
        except Exception as e:
            logging.error(f'Error extracting zip file: {e}')
            return None        
        
    except requests.exceptions.RequestException as e:
        logging.error(f'Error: {e}')
        return None
    

    

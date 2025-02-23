import os
import pandas as pd
import logging

def load(df, file_path='data/processed/weather_data.csv'):
    """
    Saves the transformed data to a CSV file.
    
    Args:
        df (pandas.DataFrame): The transformed data.
        file_path (str): The path to save the CSV file.
    
    Returns:
        None
    """
    
    # Check if the file already exists
    if os.path.isfile(file_path):
        existing_data = pd.read_csv(file_path)
        
        # Add the new data to the existing data
        complete_data = pd.concat([existing_data, df])
        
        print('Shape before dropping duplicates', complete_data.shape)
        
        # Drop the duplicates
        complete_data = complete_data.drop_duplicates(subset=['station_number', 'date', 'hour'], keep='last').reset_index(drop=True)
        
        print('Shape after dropping duplicates', complete_data.shape)
        
        # Save data to the file path
        complete_data.to_csv(file_path, mode='w', index=False)
        logging.info('New data successfully added to existing data')
        
    
    else:
        # Save the data to a CSV file
        df.to_csv(file_path, index=False)
        logging.info('New data successfully saved')
        print('Shape  of new data', df.shape)

    
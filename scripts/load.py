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
        
        complete_data.loc[:, 'date'] = pd.to_datetime(complete_data['date']).dt.strftime('%Y-%m-%d')
        complete_data.loc[:, 'hour'] = complete_data['hour'].astype(str).str.zfill(2)
        complete_data.loc[:, 'datetime'] = pd.to_datetime(complete_data['datetime'])
        
        # Drop the duplicates
        complete_data = complete_data.drop_duplicates(subset=['station_number', 'date', 'hour'], keep='last').reset_index(drop=True)
        
        # Save data to the file path
        complete_data.to_csv(file_path, mode='w', index=False)
        logging.info('New data successfully added to existing data')
        
    else:
        # Save the data to a CSV file
        df.to_csv(file_path, index=False)
        logging.info('New data successfully saved')

    
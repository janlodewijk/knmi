import pandas as pd
import logging
import numpy as np

def transform(file_path):
    """
    Transforms the raw data into a pandas DataFrame.

    Args:
        file_path (str): Path to the raw data file.
    
    Returns:
        A pandas DataFrame containing the transformed data.
    """
    
    # Open text file
    with open(file_path, 'r') as f:
        lines = f.readlines()[31:]
    

    # Extract column names (now the first line of lines)
    # column_names = [col.strip() for col in lines[0].lstrip('#').split(',')]
    column_names =['station_number', 'date', 'hour', 'wind_direction', 'avg_windspeed_1h', 'wind_speed_last_10m', 'highest_gust', 'temp_time_observation', 'min_temp', 'dewpoint_temp', 'sun_duration_decimals', 'global_radiation', 'precip_dur_decim', 'hourly_precip_mm', 'air_press_hPa', 'horiz_visib', 'cloud_cover_oct', 'rel_humid_perc', 'weather_code_0_99', 'indicator_weather_code', 'fog', 'rain', 'snow', 'thunder', 'ice_formation']
    
    # Convert each line of data to a list of values
    data = []
    
    for line in lines[2:]:
        values = [value.strip() for value in line.split(',')]
        data.append(values)
    
    # Load data into an pandas dataframe
    df = pd.DataFrame(data, columns=column_names)
    
    # Filter out the relevant columns
    relevant_data = df[['station_number', 'date', 'hour', 'wind_direction', 'avg_windspeed_1h', 'temp_time_observation', 'precip_dur_decim', 'hourly_precip_mm', 'air_press_hPa', 'fog', 'snow', 'thunder']]
    
    # Convert missing values to NaN
    relevant_data = relevant_data.replace('', np.nan)
    
    # Filter for stations with temperature data
    weather_data = relevant_data.dropna(subset=['temp_time_observation'])
    
    # Reset filter
    weather_data = weather_data.reset_index(drop=True)
    
    logging.info('Data successfully transformed')
    return weather_data    
    

    


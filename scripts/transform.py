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
    

    # Take column names from description in first lines of the text file
    column_names =['station_number', 'date', 'hour', 'wind_direction', 'avg_windspeed_1h', 'wind_speed_last_10m', 'highest_gust', 'temp_time_observation', 'min_temp', 'dewpoint_temp', 'sun_duration_decimals', 'global_radiation', 'precip_dur_decim', 'hourly_precip_mm', 'air_press_hPa', 'horiz_visib', 'cloud_cover_oct', 'rel_humid_perc', 'weather_code_0_99', 'indicator_weather_code', 'fog', 'rain', 'snow', 'thunder', 'ice_formation']
    
    # Convert each line of data to a list of values
    data = []
    
    for line in lines[2:]:
        values = [value.strip() for value in line.split(',')]
        data.append(values)
    
    # Load data into an pandas dataframe
    df = pd.DataFrame(data, columns=column_names)
    
    # Filter out the relevant columns
    relevant_data = df[['station_number', 'date', 'hour', 'wind_direction', 'avg_windspeed_1h', 'temp_time_observation', 'precip_dur_decim', 'hourly_precip_mm', 'air_press_hPa', 'fog', 'snow', 'thunder']].copy()
    
    # Convert missing values to NaN
    relevant_data = relevant_data.replace('', np.nan)
    
    # Filter for stations with temperature data
    weather_data = relevant_data.dropna(subset=['temp_time_observation']).copy()
    
    # Make sure the data is in the right format. Use .loc to avoid SettingWithCopyWarning
    weather_data.loc[:, 'station_number'] = weather_data['station_number'].astype(int)
    weather_data.loc[:, 'date'] = pd.to_datetime(weather_data['date']).dt.strftime('%Y-%m-%d')
    
    # Subtract 1 from each hour to get the coming hour instead of the past hour
    weather_data.loc[:, 'hour'] = weather_data['hour'].astype(float).astype(int) - 1
    
    # Convert the hour to a string with leading zeros if needed
    weather_data.loc[:, 'hour'] = weather_data['hour'].astype(str).str.zfill(2)
    
    print(weather_data['date'].unique())
    print(weather_data['hour'].unique())
    
    # Combine date and hour to create a datetime column
    weather_data.loc[:, 'datetime'] = pd.to_datetime(weather_data['date'] + ' ' + weather_data['hour'], format='%Y-%m-%d %H')
    
    # Convert numerical columns to proper data types
    num_cols = ['avg_windspeed_1h', 'temp_time_observation', 'precip_dur_decim', 'hourly_precip_mm', 'air_press_hPa']
    for col in num_cols:
        weather_data.loc[:, col] = pd.to_numeric(weather_data[col], errors='coerce')  # Convert to float, setting errors to NaN
    
    # Divide the temperature by 10 to get the actual temperature
    weather_data.loc[:, 'temp_time_observation'] = weather_data['temp_time_observation'] / 10
    
    # Convert categorical/weather-related columns to string and remove spaces
    categorical_cols = ['wind_direction', 'fog', 'snow', 'thunder']
    for col in categorical_cols:
        weather_data.loc[:, col] = weather_data[col].astype(str).str.strip()
    
    # Reset filter
    weather_data = weather_data.reset_index(drop=True)
    
    logging.info('Data successfully transformed')
    return weather_data    
    

    


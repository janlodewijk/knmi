import pandas as pd

def temperature_trends(file_path='data/processed/weather_data.csv'):
    """
        Plots the temperatur over the last measured 24 hours, week and month.
        Args:
            file_path (str): The path to the file.

        Returns:
            A plot of the temperatures of the last 24 hours, week and month.
    """
    
    # Read the data from the file
    weather_data = pd.read_csv(file_path)
    
    # Select the columns needed for temperature analysis
    temp_data = weather_data[['station_number', 'datetime', 'temp_time_observation']]
    


    
    print(temp_data.head())
    print(temp_data.dtypes)
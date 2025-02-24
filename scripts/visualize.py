import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def temperature_trends(file_path='data/processed/weather_data.csv'):
    """
        Plots the temperatur over the last measured 24 hours, week and month.
        Args:
            file_path (str): The path to the file.

        Returns:
            A plot of the temperatures of the last 24 hours, week and month.
    """
    
    # Read the data from the file
    weather_data = pd.read_csv(file_path).copy()
    
    # Select the columns needed for temperature analysis
    temperature_data = weather_data[['station_number', 'datetime', 'temp_time_observation']].copy()
    
    # Convert datetime column to datetime type
    temperature_data['datetime'] = pd.to_datetime(temperature_data['datetime'])

    # Group the data by datetime, calculate the mean and reset index
    avg_temperature = temperature_data.groupby('datetime').mean().reset_index()
    
    # Plot the temperature trends with Seaborn
    fig = plt.figure(figsize=(12, 6))
    sns.lineplot(data=avg_temperature, x='datetime', y='temp_time_observation')
    
    # Set the title and labels
    plt.title('Temperature Trends')
    plt.xlabel('Date and time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    
    return fig

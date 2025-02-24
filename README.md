🌦️ Weather Data ETL Project

📌 Overview

This project fetches, processes, and visualizes weather data from the Dutch KNMI API. It follows an ETL (Extract, Transform, Load) pipeline and stores the data in CSV format for further analysis using Matplotlib and Seaborn.

🚀 Features

✅ Fetches hourly weather data from the KNMI API or direct KNMI downloads
✅ Cleans and transforms data into a structured format
✅ Saves processed data as a CSV file with incremental updates
✅ Removes duplicate entries to ensure data consistency
✅ Generates visualizations using Matplotlib & Seaborn
✅ Automates the ETL pipeline with modular scripts

💅 Project Structure

weather-data-etl/
│── venv/                # Virtual environment (not committed to Git)
│── data/                # Folder for storing raw and processed data
│   ├── raw/             # Raw JSON/CSV/ZIP files from the API
│   ├── processed/       # Cleaned & transformed data
│   ├── weather_data.csv # Main processed data file
│── notebooks/           # Jupyter Notebooks for EDA & testing visualizations
│── reports/             # Reports and final visualizations
│   ├── figures/         # Saved PNGs, PDFs of final plots
│── scripts/             # Python scripts for ETL pipeline
│   ├── extract.py       # Fetch data from KNMI API or KNMI site
│   ├── transform.py     # Clean & preprocess data
│   ├── load.py          # Store data (CSV, database)
│   ├── visualize.py     # Generate plots & reports
│   ├── main.py          # Main script to run ETL pipeline & visualization
│── outputs/             # Optional: Model results, additional reports
│── .gitignore           # Ignore unnecessary files (e.g., venv, large datasets)
│── .env                 # Environment variables (API keys, etc.)
│── requirements.txt     # Dependencies for easy setup
│── README.md            # Project overview & instructions

🛋️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/yourusername/weather-data-etl.git
cd weather-data-etl

2️⃣ Create and Activate a Virtual Environment

Windows (Command Prompt)

python -m venv venv
venv\Scripts\activate

macOS/Linux (Terminal)

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the root folder and add your KNMI API key (if needed):

API_KEY=your_knmi_api_key_here

5️⃣ Run the ETL Pipeline

Extract Data from the API or KNMI website:

python scripts/extract.py

Transform and Clean Data:

python scripts/transform.py

Load Data into CSV with incremental updates:

python scripts/load.py

Generate Visualizations:

python scripts/main.py

📊 Data Fields

This project collects the following weather data:

Field

Description

Unit

datetime

Date & hour of measurement

UTC

station_number

Weather station ID

Text

wind_direction

Wind direction

Degrees

avg_windspeed_1h

Average wind speed (1h)

m/s

temp_time_observation

Temperature at time of observation

°C

precip_dur_decim

Duration of precipitation

Hours

hourly_precip_mm

Rainfall amount (hourly)

mm

air_press_hPa

Air pressure

hPa

fog

Fog indicator

0/1

snow

Snow indicator

0/1

thunder

Thunderstorm indicator

0/1

📊 Visualizations

This project includes line plots showing temperature trends over time:

Hourly temperature trends (last 24 hours)

Daily temperature trends (last 7 days & last month)

Wind speed & precipitation correlation analysis

Example Temperature Trend Plot

![Sample Plot](reports/figures/temperature_trend.png)

💜 License

This project is open-source and available under the MIT License.
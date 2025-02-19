# 🌦️ Weather Data ETL Project

## 📌 Overview
This project fetches, processes, and visualizes weather data from the **Dutch KNMI API**. It follows an **ETL (Extract, Transform, Load)** pipeline and stores the data in CSV format for further analysis using Matplotlib and Seaborn.

## 🚀 Features
✅ Fetches **hourly** weather data from the KNMI API  
✅ Cleans and transforms data into a structured format  
✅ Saves processed data as a CSV file  
✅ Visualizes weather trends using **Matplotlib & Seaborn**  
✅ Automates the ETL pipeline with modular scripts  

## 💄 Project Structure
```
weather-data-etl/
│── venv/                # Virtual environment (not committed to Git)
│── data/                # Folder for storing raw and processed data
│   ├── raw/             # Raw JSON/CSV files from the API
│   ├── processed/       # Cleaned & transformed data
│   ├── weather_data.csv # Main processed data file
│── notebooks/           # Jupyter Notebooks for EDA & visualization
│── scripts/             # Python scripts for ETL pipeline
│   ├── extract.py       # Fetch data from KNMI API
│   ├── transform.py     # Clean & preprocess data
│   ├── load.py          # Store data (CSV, database)
│   ├── visualize.py     # Generate plots & reports
│── .gitignore           # Ignore unnecessary files (e.g., venv, large datasets)
│── .env                 # Environment variables (API keys, etc.)
│── requirements.txt     # Dependencies for easy setup
│── README.md            # Project overview & instructions
```

## 📦 Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/weather-data-etl.git
cd weather-data-etl
```

### **2️⃣ Create and Activate a Virtual Environment**
#### *Windows (Command Prompt)*
```sh
python -m venv venv
venv\Scripts\activate
```
#### *macOS/Linux (Terminal)*
```sh
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
- Create a `.env` file in the root folder and add your **KNMI API key**:
```sh
API_KEY=your_knmi_api_key_here
```

### **5️⃣ Run the ETL Pipeline**
- **Extract Data** from the API:
```sh
python scripts/extract.py
```
- **Transform and Clean Data**:
```sh
python scripts/transform.py
```
- **Load Data into CSV or Database**:
```sh
python scripts/load.py
```
- **Generate Visualizations**:
```sh
python scripts/visualize.py
```

## 📊 Data Fields
This project collects the following weather data:
| Field            | Description                | Unit  |
|-----------------|--------------------------|-------|
| **timestamp**   | Date & time of measurement | UTC   |
| **temperature** | Air temperature           | °C    |
| **precipitation** | Rainfall amount         | mm    |
| **wind_speed**  | Wind velocity            | m/s   |
| **wind_direction** | Wind direction        | Degrees |
| **latitude**    | Station latitude         | °      |
| **longitude**   | Station longitude        | °      |
| **station_name** | Weather station name    | Text  |
| **time_zone**   | Time zone of data        | UTC/local |
| **data_source** | Source of the data       | KNMI API |

## 📈 Sample Visualization
*(Example: Temperature & Wind Speed Over Time)*
![Sample Plot](example_plot.png)

## 💜 License
This project is open-source and available under the **MIT License**.


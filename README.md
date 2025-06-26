# Sensor Batch Storage System

This project implements a Dockerized data system for storing environmental sensor data in batches. It was developed as part of the Data Engineering portfolio project (DLBDSEDE02) at IU International University of Applied Sciences.

## 📌 Project Goal

To design and deploy a portable, scalable data storage solution that ingests environmental sensor data (temperature, humidity, CO2, etc.) in batch format and makes it accessible for future front-end and analytical applications.

## 🗃️ Dataset

- **Source**: [Kaggle IoT Telemetry Dataset](https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k)
- **Type**: CSV with temperature, humidity, and other sensor readings

## 🧰 Tech Stack

- **Database**: MongoDB (Docker containerized)
- **Programming Language**: Python
- **Tools**: Docker, Docker Compose, PyMongo

## 🐳 Dockerized Setup

To run the project locally:

```bash
# Clone the repository
git clone https://github.com/fatimagulomova/sensor-batch-storage-system.git
cd sensor-batch-storage-system

# Build and run the Docker container
docker-compose up --build

```

## 🌐 Accessing Mongo Express
Once the containers are up, open your browser and go to:

```bash
http://localhost:8081
```
* Username: admin
* Password: admin123

## 📂 File Structure
sensor-batch-storage-system/
│
├── data/
│   ├── iot_telemetry_data.csv         # Raw dataset
│   └── sample_cleaned_sensors.csv     # Cleaned and reduced version
│
├── scripts/
│   ├── clean_csv.py                   # Cleans and filters raw sensor data
│   └── load_data.py                   # Loads cleaned data into MongoDB
│
├── Dockerfile                         # Environment setup for Python
├── docker-compose.yml                 # MongoDB + Mongo Express + App service
└── README.md                          # Project description

## 🚀 How It Works
**clean_csv.py** processes the raw CSV and generates a cleaned version
**load_data.py** connects to the running MongoDB container and loads **sample_cleaned_sensors.csv** into the sensor_data collection
**Mongo Express** provides a web interface to verify data loading

## 📝 Author
Fotimakhon Gulomova – [LinkedIn](https://www.linkedin.com/in/fatima-gulamova/)
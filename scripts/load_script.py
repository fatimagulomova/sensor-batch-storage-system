import pandas as pd
from pymongo import MongoClient
import os
import time

# Config
BATCH_SIZE = 1000  

# MongoDB Connection
host = os.getenv("MONGO_HOST", "localhost")
port = int(os.getenv("MONGO_PORT", 27017))
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
auth_db = os.getenv("MONGO_AUTH_DB", "admin")

client = MongoClient(
    host=host,
    port=port,
    username=username,
    password=password,
    authSource=auth_db,
)

db = client["sensor_data"]
collection = db["readings"]


try: 
    df = pd.read_csv("data/sample_cleaned_sensors.csv")

    # Batch insert
    total = len(df)

    for i in range(0, total, BATCH_SIZE):
        batch = df[i:i+BATCH_SIZE]
        collection.insert_many(batch.to_dict(orient="records"))
        print(f"Inserted batch {i//BATCH_SIZE + 1}: {len(batch)} records.")
        time.sleep(1)

except FileNotFoundError as err:
    print("No file")
    df = pd.read_csv("data/iot_telemetry_data.csv")
    sample_data = df.dropna().sample(frac=0.1, random_state=42)
    
    total = len(sample_data)

    for i in range(0, total, BATCH_SIZE):
        batch = sample_data[i:i+BATCH_SIZE]
        collection.insert_many(batch.to_dict(orient="records"))
        print(f"Inserted batch {i//BATCH_SIZE + 1}: {len(batch)} records.")
        time.sleep(1)

print(f"Finished inserting {total} records in batches of {BATCH_SIZE}.")


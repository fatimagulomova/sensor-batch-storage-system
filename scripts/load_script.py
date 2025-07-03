import pandas as pd
from pymongo import MongoClient, errors
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


try:

    client = MongoClient(
        host=host,
        port=port,
        username=username,
        password=password,
        authSource=auth_db,
    )

    print("Connected to MongoDB successfully.")

except errors.ServerSelectionTimeoutError as err:
    print("Could not connect to MongoDB:", err)
    exit(1) 


db = client["sensor_data"]
collection = db["readings"]

def insert_data(df):

    # Batch insert
    total = len(df)

    try:

        for i in range(0, total, BATCH_SIZE):
            batch = df[i:i+BATCH_SIZE]
            collection.insert_many(batch.to_dict(orient="records"))
            print(f"Inserted batch {i//BATCH_SIZE + 1}: {len(batch)} records.")
            time.sleep(1)

    except errors.BulkWriteError as bwe:
        print(f"Bulk write error on batch {i//BATCH_SIZE + 1}:", bwe.details)

    time.sleep(1)
    print(f"Finished inserting {total} records in batches of {BATCH_SIZE}.")


try: 
    df = pd.read_csv("data/sample_cleaned_sensors.csv")
    insert_data(df)

except FileNotFoundError as err:
    print("sample_cleaned_sensors.csv not found. Falling back to raw data.")

    try:
        df = pd.read_csv("data/iot_telemetry_data.csv")
        sample_data = df.dropna().sample(frac=0.1, random_state=42)
        
        insert_data(sample_data)

    except FileNotFoundError:
        print("No CSV files found in /data directory. Exiting.")


# ✅ Verification Note:
# After running this script and Docker Compose, 
# you can verify the inserted data using Mongo Express at http://localhost:8081
# with Username: admin; Password: admin123
# Navigate to the 'sensor_data' database and 'readings' collection.
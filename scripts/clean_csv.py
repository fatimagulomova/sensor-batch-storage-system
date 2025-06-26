import pandas as pd

# Load and fix header manually
df = pd.read_csv("data/iot_telemetry_data.csv", header=0, skip_blank_lines=True)

# Drop extra unnamed or misaligned columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Drop fully empty rows
df = df.dropna(how='all')
sample_data = df.sample(frac=0.1, random_state=42)

# Save cleaned file
sample_data.to_csv("data/sample_cleaned_sensors.csv", index=False)

print(sample_data.head())
print(sample_data.shape)
print("Columns:", sample_data.columns.tolist())

print("CSV cleaned and saved as data/cleaned_sensors.csv")

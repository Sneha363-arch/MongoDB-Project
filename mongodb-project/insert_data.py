import pandas as pd
from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["bigdata"]
collection = db["students"]

# load CSV
df = pd.read_csv("students.csv")

# OPTIONAL: clean column names (remove spaces)
df.columns = df.columns.str.strip()

# convert to dictionary
data = df.to_dict(orient="records")

# insert into MongoDB
collection.insert_many(data)

print("Inserted records:", len(data))
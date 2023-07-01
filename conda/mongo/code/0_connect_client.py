import os
from dotenv import load_dotenv
from dataclasses import dataclass

import pymongo

load_dotenv()

MONGODB_URL = os.environ.get("MONGODB_URL")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASSWORD = os.environ.get("MONGODB_PASSWORD")

MONGODB_SERVER = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_URL}"

client = pymongo.MongoClient(MONGODB_SERVER)
# db = client.get_database("monthly-report")
client.list_database_names()

# print(client.list_database_names())
# # print(db)

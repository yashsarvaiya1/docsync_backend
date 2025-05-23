from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
print("MONGO_URI:", os.getenv("MONGO_URI"))
db = client["docsyncdb"]

users_collection = db["users"]
folders_collection = db["folders"]
documents_collection = db["documents"]
auth_codes_collection = db["auth_codes"]

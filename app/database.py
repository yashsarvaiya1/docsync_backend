from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["docsyncdb"]

users_collection = db["users"]
folders_collection = db["folders"]
documents_collection = db["documents"]
auth_codes_collection = db["auth_codes"]
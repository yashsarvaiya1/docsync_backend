from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "docsync"

client = None
db = None

users_collection = None
folders_collection = None
documents_collection = None
auth_codes_collection = None

async def connect_to_mongo():
    global client, db, users_collection, folders_collection, documents_collection, auth_codes_collection
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client[DB_NAME]
    users_collection = db["users"]
    folders_collection = db["folders"]
    documents_collection = db["documents"]
    auth_codes_collection = db["auth_codes"]

async def close_mongo_connection():
    global client
    client.close()

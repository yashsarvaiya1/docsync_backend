from datetime import datetime
from bson import ObjectId
from app.database import folders_collection
import uuid

def create_folder(uid: str, name: str) -> dict:
    folder = {
        "folder_id": str(uuid.uuid4()),
        "uid": uid,
        "name": name,
        "created_at": datetime.utcnow()
    }
    folders_collection.insert_one(folder)
    return folder

def get_folders_by_user(uid: str) -> list:
    return list(folders_collection.find({"uid": uid}))

def get_folder_by_id(folder_id: str) -> dict:
    return folders_collection.find_one({"folder_id": folder_id})

def update_folder(folder_id: str, name: str) -> dict:
    folders_collection.update_one(
        {"folder_id": folder_id},
        {"$set": {"name": name}}
    )
    return get_folder_by_id(folder_id)

def delete_folder(folder_id: str) -> bool:
    result = folders_collection.delete_one({"folder_id": folder_id})
    return result.deleted_count > 0

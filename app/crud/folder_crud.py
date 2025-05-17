from datetime import datetime
import uuid
from app.database import folders_collection
from app.models.folder_model import Folder

def create_folder(uid:str,name:str) -> dict:
    folder_data = {
        "folder_id":str(uuid.uuid4()),
        "uid":uid,
        "name":name,
        "created_at":datetime.utcnow(),
        "updated_at":datetime.utcnow(),
    }
    folders_collection.insert_one(folder_data)
    return folder_data

def get_folder_by_user(uid:str) -> list:
    return list(folders_collection.find({"uid":uid}))

def update_folder_name(folder_id: str, new_name: str) -> dict:
    result = folders_collection.find_one_and_update(
        {"folder_id": folder_id},
        {"$set": {"name": new_name, "updated_at": datetime.utcnow()}},
        return_document=True
    )
    return result or {"error": "Folder not found"}

def delete_folder(folder_id: str) -> dict:
    result = folders_collection.delete_one({"folder_id": folder_id})
    if result.deleted_count:
        return {"status": "Folder deleted"}
    return {"error": "Folder not found"}
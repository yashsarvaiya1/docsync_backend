import uuid
from datetime import datetime
from app.database import folders_collection

def create_folder(uid: str, name: str) -> dict:
    folder = {
        "folder_id": str(uuid.uuid4()),
        "uid": uid,
        "name": name,
        "created_at": datetime.utcnow()
    }
    folders_collection.insert_one(folder)
    return folder

def get_user_folders(uid: str):
    return list(folders_collection.find({"uid": uid}))

def update_folder_name(folder_id: str, new_name: str):
    folders_collection.update_one({"folder_id": folder_id}, {"$set": {"name": new_name}})
    return {"message": "Folder updated"}

def delete_folder(folder_id: str):
    folders_collection.delete_one({"folder_id": folder_id})
    return {"message": "Folder deleted"}

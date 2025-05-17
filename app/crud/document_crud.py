# app/crud/document_crud.py

from datetime import datetime
import uuid
from app.database import documents_collection

def create_document(data: dict) -> dict:
    doc_data = {
        "doc_id": str(uuid.uuid4()),
        "uid": data["uid"],
        "folder_id": data["folder_id"],
        "title": data["title"],
        "file_urls": data["file_urls"],
        "tags": data.get("tags", {}),
        "issue_date": data.get("issue_date"),
        "expire_date": data.get("expire_date"),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    documents_collection.insert_one(doc_data)
    return doc_data

def get_documents_by_user(uid: str) -> list:
    return list(documents_collection.find({"uid": uid}))

def get_documents_by_folder(folder_id: str) -> list:
    return list(documents_collection.find({"folder_id": folder_id}))

def update_document(doc_id: str, updates: dict) -> dict:
    updates["updated_at"] = datetime.utcnow()
    result = documents_collection.find_one_and_update(
        {"doc_id": doc_id},
        {"$set": updates},
        return_document=True
    )
    return result or {"error": "Document not found"}

def delete_document(doc_id: str) -> dict:
    result = documents_collection.delete_one({"doc_id": doc_id})
    if result.deleted_count:
        return {"status": "Document deleted"}
    return {"error": "Document not found"}

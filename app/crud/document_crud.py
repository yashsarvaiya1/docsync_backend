from datetime import datetime
from app.database import documents_collection
import uuid

def create_document(uid: str, doc_data: dict) -> dict:
    document = {
        "document_id": str(uuid.uuid4()),
        "uid": uid,
        "title": doc_data["title"],
        "folder_id": doc_data["folder_id"],
        "tags": doc_data.get("tags", {}),
        "issue_date": doc_data.get("issue_date"),
        "expire_date": doc_data.get("expire_date"),
        "files": doc_data["files"],
        "created_at": datetime.utcnow()
    }
    documents_collection.insert_one(document)
    return document

def get_documents_by_user(uid: str) -> list:
    return list(documents_collection.find({"uid": uid}))

def get_document_by_id(document_id: str) -> dict:
    return documents_collection.find_one({"document_id": document_id})

def update_document(document_id: str, update_data: dict) -> dict:
    documents_collection.update_one(
        {"document_id": document_id},
        {"$set": update_data}
    )
    return get_document_by_id(document_id)

def delete_document(document_id: str) -> bool:
    result = documents_collection.delete_one({"document_id": document_id})
    return result.deleted_count > 0

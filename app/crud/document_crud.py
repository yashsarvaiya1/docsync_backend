import uuid
from datetime import datetime
from app.database import documents_collection

def create_document(data: dict):
    document = {
        "doc_id": str(uuid.uuid4()),
        "uid": data["uid"],
        "folder_id": data["folder_id"],
        "title": data["title"],
        "file_url": data["file_url"],
        "tags": data.get("tags", {}),
        "issue_date": data.get("issue_date"),
        "expiry_date": data.get("expiry_date"),
        "created_at": datetime.utcnow()
    }
    documents_collection.insert_one(document)
    return document

def get_documents(uid: str):
    return list(documents_collection.find({"uid": uid}))

def update_document(doc_id: str, data: dict):
    documents_collection.update_one({"doc_id": doc_id}, {"$set": data})
    return {"message": "Document updated"}

def delete_document(doc_id: str):
    documents_collection.delete_one({"doc_id": doc_id})
    return {"message": "Document deleted"}

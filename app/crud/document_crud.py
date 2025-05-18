import uuid
from datetime import datetime, time
from app.database import documents_collection

def create_document(data: dict):
    document = {
        "doc_id": str(uuid.uuid4()),
        "uid": data["uid"],
        "folder_id": data["folder_id"],
        "title": data["title"],
        "file_url": data["file_url"],
        "tags": data.get("tags", {}),
        "issue_date": datetime.combine(data["issue_date"], time.min) if data.get("issue_date") else None,
        "expiry_date": datetime.combine(data["expiry_date"], time.min) if data.get("expiry_date") else None,
        "created_at": datetime.utcnow()
    }
    documents_collection.insert_one(document)
    document.pop("_id", None)
    return document

def get_documents(uid: str):
    documents = list(documents_collection.find({"uid": uid}))
    for doc in documents:
        doc.pop("_id", None)
    return documents

def get_document_by_id(doc_id: str):
    doc = documents_collection.find_one({"doc_id": doc_id})
    if doc:
        doc.pop("_id", None)
    return doc or {"message": "Document not found"}

def get_documents_by_folder(folder_id: str):
    documents = list(documents_collection.find({"folder_id": folder_id}))
    for doc in documents:
        doc.pop("_id", None)
    return documents

def update_document(doc_id: str, data: dict):
    if "issue_date" in data and data["issue_date"]:
        data["issue_date"] = datetime.combine(data["issue_date"], time.min)
    if "expiry_date" in data and data["expiry_date"]:
        data["expiry_date"] = datetime.combine(data["expiry_date"], time.min)
    documents_collection.update_one({"doc_id": doc_id}, {"$set": data})
    return {"message": "Document updated"}

def delete_document(doc_id: str):
    documents_collection.delete_one({"doc_id": doc_id})
    return {"message": "Document deleted"}



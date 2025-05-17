from fastapi import APIRouter, HTTPException
from typing import List
from app.models.document_model import DocumentCreate, DocumentUpdate
from app.crud import document_crud

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/", response_model=dict)
def create_document(payload: DocumentCreate, uid: str):
    document = document_crud.create_document(uid=uid, doc_data=payload.dict())
    return document

@router.get("/{uid}", response_model=List[dict])
def get_documents(uid: str):
    docs = document_crud.get_documents_by_user(uid)
    return docs

@router.put("/{document_id}", response_model=dict)
def update_document(document_id: str, payload: DocumentUpdate):
    doc = document_crud.get_document_by_id(document_id)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    updated = document_crud.update_document(document_id, payload.dict(exclude_none=True))
    return updated

@router.delete("/{document_id}", response_model=dict)
def delete_document(document_id: str):
    success = document_crud.delete_document(document_id)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"detail": "Document deleted"}

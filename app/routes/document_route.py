# app/routes/document_route.py

from fastapi import APIRouter
from app.schemas.document_schema import DocumentCreate, DocumentUpdate
from app.crud import document_crud

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/")
def create_document(payload: DocumentCreate):
    return document_crud.create_document(payload.dict())

@router.get("/user/{uid}")
def get_documents_by_user(uid: str):
    return document_crud.get_documents_by_user(uid)

@router.get("/folder/{folder_id}")
def get_documents_by_folder(folder_id: str):
    return document_crud.get_documents_by_folder(folder_id)

@router.put("/{doc_id}")
def update_document(doc_id: str, payload: DocumentUpdate):
    return document_crud.update_document(doc_id, payload.dict(exclude_unset=True))

@router.delete("/{doc_id}")
def delete_document(doc_id: str):
    return document_crud.delete_document(doc_id)

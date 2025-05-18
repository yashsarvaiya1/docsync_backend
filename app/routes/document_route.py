from fastapi import APIRouter
from app.schemas.document_schema import DocumentCreate, DocumentUpdate
from app.crud import document_crud

router = APIRouter(prefix="/documents", tags=["Documents"])

@router.post("/")
def create_doc(payload: DocumentCreate):
    return document_crud.create_document(payload.dict())

@router.get("/{uid}")
def get_docs(uid: str):
    return document_crud.get_documents(uid)

@router.get("/doc/{doc_id}")
def get_doc_by_id(doc_id: str):
    return document_crud.get_document_by_id(doc_id)

@router.get("/folder/{folder_id}")
def get_docs_by_folder(folder_id: str):
    return document_crud.get_documents_by_folder(folder_id)

@router.put("/{doc_id}")
def update_doc(doc_id: str, payload: DocumentUpdate):
    return document_crud.update_document(doc_id, payload.dict(exclude_unset=True))

@router.delete("/{doc_id}")
def delete_doc(doc_id: str):
    return document_crud.delete_document(doc_id)

from fastapi import APIRouter, HTTPException
from app.schemas.folder_schema import FolderCreate, FolderUpdate
from app.crud import folder_crud

router = APIRouter(prefix="/folders", tags=["Folders"])

@router.post("/")
def create_folder(payload: FolderCreate):
    return folder_crud.create_folder(payload.uid, payload.name)

@router.get("/{uid}")
def get_folders(uid: str):
    return folder_crud.get_user_folders(uid)

@router.put("/{folder_id}")
def rename_folder(folder_id: str, payload: FolderUpdate):
    return folder_crud.update_folder_name(folder_id, payload.name)

@router.delete("/{folder_id}")
def remove_folder(folder_id: str):
    return folder_crud.delete_folder(folder_id)

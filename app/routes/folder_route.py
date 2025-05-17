from fastapi import APIRouter, HTTPException
from typing import List
from app.models.folder_model import FolderCreate, FolderUpdate
from app.crud import folder_crud

router = APIRouter(prefix="/folders", tags=["Folders"])

@router.post("/", response_model=dict)
def create_folder(payload: FolderCreate, uid: str):
    folder = folder_crud.create_folder(uid=uid, name=payload.name)
    return folder

@router.get("/{uid}", response_model=List[dict])
def get_folders(uid: str):
    folders = folder_crud.get_folders_by_user(uid)
    return folders

@router.put("/{folder_id}", response_model=dict)
def update_folder(folder_id: str, payload: FolderUpdate):
    folder = folder_crud.get_folder_by_id(folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder not found")
    updated = folder_crud.update_folder(folder_id, payload.name)
    return updated

@router.delete("/{folder_id}", response_model=dict)
def delete_folder(folder_id: str):
    success = folder_crud.delete_folder(folder_id)
    if not success:
        raise HTTPException(status_code=404, detail="Folder not found")
    return {"detail": "Folder deleted"}

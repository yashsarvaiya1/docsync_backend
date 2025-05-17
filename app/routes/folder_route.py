# app/routes/folder_route.py

from fastapi import APIRouter
from app.crud import folder_crud
from app.schemas.folder_schema import FolderCreate
from pydantic import BaseModel

router = APIRouter(prefix="/folders", tags=["Folders"])

@router.post("/")
def create_folder(folder: FolderCreate):
    return folder_crud.create_folder(folder.uid, folder.name)

@router.get("/{uid}")
def get_folders(uid: str):
    return folder_crud.get_folders_by_user(uid)

class FolderUpdate(BaseModel):
    new_name: str

@router.put("/{folder_id}")
def update_folder(folder_id: str, payload: FolderUpdate):
    return folder_crud.update_folder_name(folder_id, payload.new_name)

@router.delete("/{folder_id}")
def delete_folder(folder_id: str):
    return folder_crud.delete_folder(folder_id)

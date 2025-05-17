from fastapi import APIRouter, HTTPException
from app.crud import user_crud
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["User"])

@router.get("/{uid}", response_model=User)
def get_user(uid: str):
    user = user_crud.get_user_by_uid(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{uid}", response_model=User)
def update_user(uid: str, updated_data: dict):
    user = user_crud.update_user(uid, updated_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found or not updated")
    return user

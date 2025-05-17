from fastapi import APIRouter, HTTPException
from app.database import users_collection
from app.models.user_model import User

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{uid}", response_model=User)
async def get_user(uid: str):
    user = await users_collection.find_one({"uid": uid})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

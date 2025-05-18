import uuid
from datetime import datetime, timedelta
from app.database import users_collection, auth_codes_collection

def create_or_get_user(email: str) -> dict:
    existing = users_collection.find_one({"email": email})
    if existing:
        existing.pop("_id", None)
        return existing
    user = {
        "uid": str(uuid.uuid4()),
        "email": email,
        "username": email.split('@')[0],
        "created_at": datetime.utcnow()
    }
    users_collection.insert_one(user)
    user.pop("_id", None)
    return user

def store_otp(email: str, code: str):
    auth_codes_collection.update_one(
        {"email": email},
        {"$set": {
            "code": code,
            "expires_at": datetime.utcnow() + timedelta(minutes=10)
        }},
        upsert=True
    )

def verify_otp(email: str, code: str) -> bool:
    record = auth_codes_collection.find_one({"email": email})
    if not record:
        return False
    if record["code"] != code:
        return False
    if datetime.utcnow() > record["expires_at"]:
        return False
    return True

def get_user_by_uid(uid: str) -> dict:
    user = users_collection.find_one({"uid": uid})
    if not user:
        return None
    user.pop("_id", None)
    return user


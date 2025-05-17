from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    uid: str
    email: EmailStr
    username: str
    created_at: datetime

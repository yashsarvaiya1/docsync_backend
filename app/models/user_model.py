from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    uid: str
    email: str
    username: str
    created_at: datetime

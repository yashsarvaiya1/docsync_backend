from pydantic import BaseModel
from datetime import datetime

class Folder(BaseModel):
    folder_id: str
    uid: str
    name: str
    created_at: datetime

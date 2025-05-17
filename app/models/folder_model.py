from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Folder(BaseModel):
    folder_id:str
    uid: str
    name:str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
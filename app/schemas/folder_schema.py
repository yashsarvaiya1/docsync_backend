from pydantic import BaseModel
from typing import Optional

class FolderCreate(BaseModel):
    name: str
    uid: str

class FolderUpdate(BaseModel):
    name: Optional[str] = None

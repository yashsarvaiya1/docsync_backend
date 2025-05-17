from pydantic import BaseModel
from typing import Optional

class DocumentCreate(BaseModel):
    uid: str
    folder_id: Optional[str]
    title: str
    url: str

class DocumentUpdate(BaseModel):
    title: Optional[str]
    folder_id: Optional[str]
    url: Optional[str]

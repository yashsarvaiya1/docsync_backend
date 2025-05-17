from pydantic import BaseModel, Field
from typing import Optional, Dict
from datetime import datetime

class DocumentBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    folder_id: str
    tags: Optional[Dict[str, str]] = None
    issue_date: Optional[datetime] = None
    expire_date: Optional[datetime] = None

class DocumentCreate(DocumentBase):
    files: list[str]  # URLs of uploaded files

class DocumentUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    folder_id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    issue_date: Optional[datetime] = None
    expire_date: Optional[datetime] = None
    files: Optional[list[str]] = None

class DocumentInDB(DocumentBase):
    document_id: str
    uid: str
    created_at: datetime

    class Config:
        orm_mode = True

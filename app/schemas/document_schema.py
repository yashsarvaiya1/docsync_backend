from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import datetime

class DocumentTag(BaseModel):
    key: str
    value: str

class DocumentBase(BaseModel):
    title: str = Field(..., min_length=1)
    folder_id: str
    files: List[str]  # URLs of uploaded files
    tags: Optional[List[DocumentTag]] = []
    issue_date: Optional[datetime]
    expiry_date: Optional[datetime]

class DocumentCreate(DocumentBase):
    uid: str  # User ID

class DocumentUpdate(BaseModel):
    title: Optional[str]
    folder_id: Optional[str]
    files: Optional[List[str]]
    tags: Optional[List[DocumentTag]]
    issue_date: Optional[datetime]
    expiry_date: Optional[datetime]

class DocumentInDB(DocumentBase):
    document_id: str
    uid: str
    created_at: datetime

    class Config:
        orm_mode = True

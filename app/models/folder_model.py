from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class FolderBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

class FolderCreate(FolderBase):
    pass

class FolderUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)

class FolderInDB(FolderBase):
    id: str
    uid: str
    created_at: datetime

    class Config:
        orm_mode = True

# app/schemas/document_schema.py

from pydantic import BaseModel
from typing import Optional, List, Dict
from datetime import datetime

class DocumentCreate(BaseModel):
    uid: str
    folder_id: str
    title: str
    file_urls: List[str]
    tags: Optional[Dict[str, str]] = {}
    issue_date: Optional[datetime] = None
    expire_date: Optional[datetime] = None

class DocumentUpdate(BaseModel):
    title: Optional[str]
    tags: Optional[Dict[str, str]]
    issue_date: Optional[datetime]
    expire_date: Optional[datetime]

from pydantic import BaseModel
from typing import Optional, Dict,List
from datetime import date

class DocumentCreate(BaseModel):
    uid: str
    folder_id: Optional[str]
    title: str
    file_url: List[str]
    tags: Optional[Dict[str, str]] = {}
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None

class DocumentUpdate(BaseModel):
    title: Optional[str] = None
    folder_id: Optional[str] = None
    file_url: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None
    issue_date: Optional[date] = None
    expiry_date: Optional[date] = None

from pydantic import BaseModel
from typing import Optional,List,Dict
from datetime import datetime

class Document(BaseModel):
    doc_id: str
    uid: str
    folder_id: str
    title: str
    file_urls: List[str]
    tags: Optional[Dict[str, str]] = {}
    issue_date: Optional[datetime]
    expire_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
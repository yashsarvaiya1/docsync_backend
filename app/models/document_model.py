from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class Document(BaseModel):
    doc_id: str
    uid: str
    folder_id: str
    title: str
    file_url: List[str]
    tags: Optional[Dict[str, str]]
    issue_date: Optional[datetime]
    expiry_date: Optional[datetime]
    created_at: datetime

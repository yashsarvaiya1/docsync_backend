from pydantic import BaseModel, Field
from typing import Optional

class FolderCreateSchema(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)

class FolderUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)

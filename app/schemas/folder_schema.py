from pydantic import BaseModel

class FolderCreate(BaseModel):
    uid:str
    name:str
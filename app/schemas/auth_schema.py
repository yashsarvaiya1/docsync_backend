from pydantic import BaseModel, EmailStr

class EmailSchema(BaseModel):
    email: EmailStr

class VerifySchema(BaseModel):
    email: EmailStr
    code: str
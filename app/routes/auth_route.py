from fastapi import APIRouter, HTTPException
from app.schemas.auth_schema import EmailSchema, VerifySchema
from app.core.email_utils import send_verification_email
from app.crud import user_crud
import random

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/request-verification")
def request_verification(payload: EmailSchema):
    code = str(random.randint(1000, 9999))
    user_crud.store_otp(payload.email, code)
    send_verification_email(payload.email, code)
    return {"message": "Verification code sent"}

@router.post("/verify-code")
def verify_code(payload: VerifySchema):
    is_valid = user_crud.verify_otp(payload.email, payload.code)
    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid or expired code")
    
    user = user_crud.create_or_get_user(payload.email)
    return {"uid": user["uid"], "email": user["email"]}

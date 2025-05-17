from fastapi import APIRouter, File, UploadFile
from typing import List
from app.core.cloudinary_utils import upload_file_to_cloudinary

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/")
async def upload_files(files: List[UploadFile] = File(...)):
    urls = []
    for file in files:
        result = upload_file_to_cloudinary(file)
        if "url" in result:
            urls.append(result["url"])
        else:
            return {"error": result["error"]}
    return {"uploaded_urls": urls}

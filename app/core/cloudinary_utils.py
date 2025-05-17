import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    secure=True,
    cloud_name=os.getenv("CLOUDINARY_URL").split("@")[-1],
)

def upload_file_to_cloudinary(file, folder="docsync"):
    try:
        result = cloudinary.uploader.upload(
            file.file,
            folder=folder,
            resource_type="auto",
        )
        return {"url": result["secure_url"]}
    except Exception as e:
        return {"error": str(e)}

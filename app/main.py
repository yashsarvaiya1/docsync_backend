from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import folder_route
from app.routes import document_route
from app.routes import upload_route
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(folder_route.router)
app.include_router(document_route.router)
app.include_router(upload_route.router)

@app.get("/")
def root():
    return {"message": "DocSync backend is running"}

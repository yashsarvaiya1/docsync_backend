from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    auth_route,
    user_route,
    folder_route,
    document_route,
    upload_route
)
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="DocSync API", version="1.0")

# CORS (for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering routers
app.include_router(auth_route.router)
app.include_router(user_route.router)
app.include_router(folder_route.router)
app.include_router(document_route.router)
app.include_router(upload_route.router)

@app.get("/")
def root():
    return {"message": "DocSync Backend is Live!"}

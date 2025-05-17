from fastapi import FastAPI
from app.routes import (
    auth_route,
    user_route,
    folder_route,
    document_route,
    upload_route,
)
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI(title="DocSync Backend API")

app.include_router(auth_route.router)
app.include_router(user_route.router)
app.include_router(folder_route.router)
app.include_router(document_route.router)
app.include_router(upload_route.router)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

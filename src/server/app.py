from fastapi import FastAPI
from server.routes.file_catalog import router as FileCatalogRouter
app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}


app.include_router(FileCatalogRouter, tags=["File Catalog"], prefix="/api/v1/catalog")
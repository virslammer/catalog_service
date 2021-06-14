
from fastapi import  FastAPI
from routes import catalog
# from database import SessionLocal, engine





# models.Base.metadata.create_all(bind=engine)
tags_metadata = [
    {
        "name":"Authentication",
        "description":"""
        - Register new User and generate Access token . 
        - Or press on Authorize Button on the right corner to login and test API on this page . 
        - Test account: id:minhanh / password:123"""
    },
    {
        "name": "Catalog",
        "description": "Add tags to uploaded file on Minio",
    }
]
app = FastAPI(
    docs_url="/",
    redoc_url=None,
    title="File Ingestor Service",
    description="Rest API service for DMP",
    version="1.0",
    openapi_tags=tags_metadata)
app.include_router(catalog.router)



# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

import uvicorn
import os

if 'HOST' in os.environ.keys():
    
    HOST = os.environ['HOST']
else:
    HOST = 'localhost'

if 'PORT' in os.environ.keys():
    
    PORT = int(os.environ['PORT'])
else:
    PORT = 8000


if __name__ == "__main__":
    uvicorn.run(
        "server.app:app", 
        host=HOST, 
        port=PORT, 
        reload=True 
        )

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

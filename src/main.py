import uvicorn
import os
HOST = os.environ['HOST']
PORT = int(os.environ['PORT'])


if __name__ == "__main__":
    uvicorn.run("server.app:app", host=HOST, port=PORT, reload=True)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

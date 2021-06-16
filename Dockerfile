FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./ /catalog_service/
WORKDIR /catalog_service/
RUN pip install --default-timeout=100 fastapi==0.65.2 uvicorn==0.14.0 pymongo==3.11.4 motor==2.4.0
ENV MONGO_CONNECTION_URL="mongodb://172.24.192.1:27017"
ENV HOST=0.0.0.0
ENV PORT=8000
EXPOSE 8000
CMD ["python", "src/main.py"]
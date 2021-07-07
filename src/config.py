import os
if "MONGO_CONNECTION_URL" in os.environ.keys():
    MONGO_DETAILS = os.environ["MONGO_CONNECTION_URL"]
else:
    MONGO_DETAILS = "mongodb://localhost:27017"
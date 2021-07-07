from config import MONGO_DETAILS
import motor.motor_asyncio
from bson.objectid import ObjectId
# from config import MONGO_DETAILS

# MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.catalog

file_catalog_collection = database.get_collection("file_catalog")


def file_catalog_helper(file_catalog) -> dict:
    return {
        "id": str(file_catalog["_id"]),
        "file_name": file_catalog["file_name"],
        "file_type": file_catalog["file_type"],
        "ingestor_routines": file_catalog["ingestor_routines"],
        "description": file_catalog["description"],
        "source": file_catalog["source"],
        "tag": file_catalog["tag"]
    }


# Retrieve all files catalog present in the database
async def retrieve_files_catalog():
    file_catalogs = []
    async for file_catalog in file_catalog_collection.find():
        file_catalogs.append(file_catalog_helper(file_catalog))
    return file_catalogs


# Add a new file catalog into to the database
async def add_file_catalog(file_catalog_data: dict) -> dict:
    print(file_catalog_data, flush=True)
    file_catalog = await file_catalog_collection.insert_one(file_catalog_data)
    new_file_catalog = await file_catalog_collection.find_one({"_id": file_catalog.inserted_id})
    return file_catalog_helper(new_file_catalog)


# Retrieve a file catalog with a matching ID
async def retrieve_file_catalog(id: str) -> dict:
    file_catalog = await file_catalog_collection.find_one({"_id": ObjectId(id)})
    if file_catalog:
        return file_catalog_helper(file_catalog)

# Retrieve a file catalog with a matching file name
async def retrieve_file_catalog_by_name(file_name: str) -> dict:
    print("Check mongo")
    file_catalog = await file_catalog_collection.find_one({"file_name": file_name})
    
    if file_catalog:
        return file_catalog_helper(file_catalog)


# Update a file catalog with a matching ID
async def update_file_catalog(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    file_catalog = await file_catalog_collection.find_one({"_id": ObjectId(id)})
    if file_catalog:
        updated_file_catalog = await file_catalog_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_file_catalog:
            return True
        return False


# Delete a file catalog from the database
async def delete_file_catalog(id: str):
    file_catalog = await file_catalog_collection.find_one({"_id": ObjectId(id)})
    if file_catalog:
        await file_catalog_collection.delete_one({"_id": ObjectId(id)})
        return True

# Delete a file catalog from the database
async def delete_file_catalog_by_file_name(file_name: str):
    file_catalog = await file_catalog_collection.find_one({"file_name": file_name})
    if file_catalog:
        await file_catalog_collection.delete_one({"_id": file_catalog['_id']})
        return True
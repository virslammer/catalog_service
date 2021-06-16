
from server.models.file_catalog import CreateFileCatalogModel, ErrorResponseModel, FileCatalogSchema, ResponseModel
from fastapi import APIRouter, Body, File
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_file_catalog,
    delete_file_catalog,
    delete_file_catalog_by_file_name,
    retrieve_file_catalog,
    retrieve_file_catalog_by_name,
    retrieve_files_catalog,
)


# from .auth import get_current_user

router = APIRouter(
    prefix="/file",
    responses={404: {"description": "Not found"}}
)


'''
------------------------------ 
        FILE CATALOG API 
------------------------------
'''

@router.post("/", response_description="File catalog added into the database")
async def add_file_catalog_data(file_catalog: FileCatalogSchema = Body(...)):
    file_catalog = jsonable_encoder(file_catalog)
    
    check_file_catalog = retrieve_file_catalog_by_name(file_catalog['file_name'])
    if check_file_catalog:
        await delete_file_catalog_by_file_name(file_catalog['file_name'])
    new_file_catalog = await add_file_catalog(file_catalog)
    return ResponseModel(new_file_catalog, "File catalog added successfully.")


@router.get("/", response_description="Files catalog retrieved")
async def get_files_catalog():
    """
    Get all files catalog in Database

    """
    files_catalog = await retrieve_files_catalog()
    if files_catalog:
        return ResponseModel(files_catalog, "Files catalog data retrieved successfully")
    return ResponseModel(files_catalog, "Empty list returned")


@router.get("/{id}", response_description="File catalog data retrieved")
async def get_file_catalog_data(id):
    file_catalog = await retrieve_file_catalog(id)
    if file_catalog:
        return ResponseModel(file_catalog, "File catalog data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "File catalog doesn't exist.")
    
@router.get("/filter/{file_name}", response_description="File catalog data retrieved")
async def get_file_catalog_data_by_file_name(file_name:str):
    file_catalog = await retrieve_file_catalog_by_name(file_name)
    if file_catalog:
        return ResponseModel(file_catalog, "File catalog data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "File catalog doesn't exist.")

# @router.delete("/{id}", response_description="Student data deleted from the database")
# async def delete_student_data(id: str):
#     deleted_student = await delete_student(id)
#     if deleted_student:
#         return ResponseModel(
#             "Student with ID: {} removed".format(id), "Student deleted successfully"
#         )
#     return ErrorResponseModel(
#         "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
#     )
    

from fastapi import Depends, APIRouter, HTTPException 
from typing import List

# from .auth import get_current_user

router = APIRouter(
    prefix="/catalog",
    tags=["Catalog"],
    responses={404: {"description": "Not found"}}
)


'''
------------------------------ 
        CATALOG API 
------------------------------
'''


@router.get('/')
def get_all_catalog():
    """
    Get all answers in Database

    """
    return "Hello world"
    
@router.get('/{file_name}')
def get_catalog_by_file_name():


    pass

    

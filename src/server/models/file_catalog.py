from typing import Dict, List, Optional
from fastapi.param_functions import File

from pydantic import BaseModel, Field


class FileCatalogSchema(BaseModel):
    file_name: str = Field(...)
    file_type: str = Field(...)
    ingestor_routines: List = Field(...)
    description: str 
    source: str 
    tag: Dict

    class Config:
        schema_extra = {
            "example": {
                "file_name": "well1_abc",
                "file_type": "las",
                "ingestor_routines": [{"LASIngestor":{"datasetDescriptor":"common:wkshop:wellbore-dataset_descriptor-1.5","overwriteSchema":False}}],
                "description": "Well Summary",
                "source": "onewkShop",
                "tag" : {
                    "well_name":"well1",
                    "well_bore":"abc"
                }
            }
        }

class CreateFileCatalogModel(BaseModel):
    file_name: str = Field(...)
    file_type: str = Field(...)
    file_obj: bytes = File(...)
    class Config:
        schema_extra = {
            "example": {
                "file_name": "well1_abc",
                "file_type": "las",
                "file_obj": "well1_abc.las"
            }
        }

class UpdateFileCatalogModel(BaseModel):
    file_name: Optional[str]
    file_type: Optional[str]
    ingestor_routines: Optional[List]
    description: Optional[str]
    source: Optional[str]
    tag: Optional[Dict]

    class Config:
        schema_extra = {
            "example": {
                "file_name": "well1_abc",
                "file_type": "las",
                "ingestor_routines": "[{\"LASIngestor\":{\"datasetDescriptor\":\"common:wkshop:wellbore-dataset_descriptor-1.5\",\"overwriteSchema\":false}}]",
                "description": "Well Summary",
                "source": "onewkShop",
                "tag" : {
                    "well_name":"well1",
                    "well_bore":"abc"
                }
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
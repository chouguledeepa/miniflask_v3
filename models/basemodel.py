"""
This module defines a pydantic basemodel to be used by another
pydantic models (resource models aka "datamodels")
"""

from pydantic import BaseModel, validator
from datetime import datetime
from typing import Union


class Base(BaseModel):
    """common attributes available in all resources"""

    created: Union[str, datetime]
    edited: Union[str, datetime]
    url: str

    @validator("created")
    def check_created(cls, created):
        if isinstance(created, str):
            return datetime.strptime(created, "%d-%m-%y")
        return created

    @validator("edited")
    def check_edited(cls, edited):
        if isinstance(edited, str):
            return datetime.strptime(edited, "%d-%m-%y")
        return edited


if __name__ == "__main__":
    data = {
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/",
    }

    obj = Base(**data)
    print(obj.created)
    print(type(obj.created))
    print("****" * 10)
    print(obj)

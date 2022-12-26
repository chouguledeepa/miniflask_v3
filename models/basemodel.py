"""
This module defines a pydantic basemodel to be used by another
pydantic models (resource models aka "datamodels")
"""

from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    """common attributes available in all resources"""

    created: datetime
    edited: datetime
    url: str


if __name__ == "__main__":
    data = {
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/",
    }

    breakpoint()

    obj = Base(**data)
    print(obj.created)
    print(type(obj.created))
    print("****" * 10)
    print(obj)

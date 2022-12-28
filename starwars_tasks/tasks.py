"""

http://127.0.0.1:5000/tasks/taskone
http://127.0.0.1:5000/tasks/tasktwo
http://127.0.0.1:5000/tasks/taskthree
http://127.0.0.1:5000/tasks/taskfour

"""


# third party imports
import requests

# relative imports (non-local)
from flask import Blueprint
from typing import Optional, List
from pydantic import parse_obj_as

# imports (local packages)
from utils.randgen import ProduceChars
from models.datamodels.characters import Character_

from models.dal.dml import insert_resource


def get_chars(obj_: ProduceChars) -> Optional[List[int]]:
    characters_ = []  # [1, 4, 5, 13, ....]
    for i in obj_:
        characters_.append(i)

    return characters_


starwars_v1 = Blueprint("starwars", __name__, url_prefix="/tasks")


@starwars_v1.route("/taskone")
def task_one():
    """The Star Wars API lists 82 main characters in the Star Wars saga. For the
    first task, we would like you to use a random number generator that picks a
    number between 1-82. Using these random numbers you will be pulling 15
    characters from the API using Python."""

    start = 1
    stop = 83

    print(__name__)
    print("current module getting executed")

    home_url = "https://swapi.dev"
    relative = "/api/people/{0}"  # magic string

    print(f"[ INFO ] producing random 2 characters...")
    obj = ProduceChars(start, stop)
    characters = get_chars(obj)

    print(f"[ INFO ] done - producing random 2 characters")

    output = []
    for num_ in characters:  # [1, 2]
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using - {absolute_url}  =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        response["char_id"] = num_
        char_ = Character_(**response)

        table_name = "characters"
        primary_key_ = "char_id"
        primary_val_ = char_.char_id

        columns_ = ["name", "mass", "hair_color", "skin_color", "eye_color", "gender"]

        values_ = [
            char_.name,
            char_.mass,
            char_.hair_color,
            char_.skin_color,
            char_.eye_color,
            char_.gender,
        ]

        count = insert_resource(table_name, primary_key_, primary_val_, columns_, values_)
        output.append({"records_count": count, "name": char_.name})

        # TODO
        # Do exception handling for `from pymysql import IntegrityError`
        # In exception block try `upsert query`

    # serialization of multiple records into pydantic model
    # for validating response
    # response = parse_obj_as(list(output))

    # TODO convert response into flask Response object
    # from flask import Response
    # Response(obj, status=<>, mimetype=<>)
    return {"success": 200}

"""

http://127.0.0.1:5000/tasks/taskone
http://127.0.0.1:5000/tasks/tasktwo
http://127.0.0.1:5000/tasks/taskthree
http://127.0.0.1:5000/tasks/taskfour

"""


# third party imports
import json
import requests

# relative imports (non-local)
from flask import Blueprint, Response
from typing import Optional, List
from pydantic import parse_obj_as

# imports (local packages)
from utils.randgen import ProduceChars
from models.datamodels.characters import Character_

from models.dal.dml import upsert_characters


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

    char_names = []
    char_ids_fetched = []
    for num_ in characters:  # [1, 2]
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using - {absolute_url}  =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        response["char_id"] = num_
        char_ = Character_(**response)
        char_names.append(char_.name)
        char_ids_fetched.append(char_.char_id)
        count_ = upsert_characters(char_, absolute_url)

    output = {
        "char_ids_fetched": char_ids_fetched,
        "records_affected": count_,
        "names": char_names
    }
    return Response(json.dumps(output), status=201, mimetype="application/json")

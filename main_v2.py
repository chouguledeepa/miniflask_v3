# third party imports
import requests
from flask import Flask

# relative imports (non-local)
from typing import Optional, List

# imports (local packages)
from utils.randgen import ProduceChars
from models.datamodels.characters import Character_

from models.dal.dml import insert_resource


# application instantiation
app = Flask(__name__)


def get_chars(obj_: ProduceChars) -> Optional[List[int]]:
    characters_ = []  # [1, 4, 5, 13, ....]
    for i in obj_:
        characters_.append(i)

    return characters_


@app.route("/taskone")
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

        insert_resource(table_name, primary_key_, primary_val_, columns_, values_)

    return {"success": 200}

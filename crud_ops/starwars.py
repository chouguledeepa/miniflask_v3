"""
http://127.0.0.1:5000/swapi/people
http://127.0.0.1:5000/swapi/films (plural API endpoint)
http://127.0.0.1:5000/swapi/films/1 (singular API endpoint)
http://127.0.0.1:5000/swapi/species
http://127.0.0.1:5000/swapi/vehicles
http://127.0.0.1:5000/swapi/starships
http://127.0.0.1:5000/swapi/planets
"""

import json
from flask import Blueprint, Response, Flask
from models.dal.dml import fetch_resources, fetch_resource


crud_app = Blueprint("crud_app", __name__, url_prefix="/swapi")


@crud_app.route("/people", methods=["GET"])
def get_characters():
    result = fetch_resources("starwarsDB.characters")
    return Response(json.dumps(result), status=200, mimetype="application/json")


# plural API endpoint
@crud_app.route("/films", methods=["GET"])
def get_films():
    result = fetch_resources("starwarsDB.film")

    from models.datamodels.films import FilmResponse

    from pydantic import parse_obj_as
    films = parse_obj_as(list[FilmResponse], result)
    response_obj = json.dumps([film.dict() for film in films])
    return Response(response_obj, status=200, mimetype="application/json")


# singular API endpoint
@crud_app.route("/films/<int:index>", methods=["GET"])
def get_film(index):
    result = fetch_resource(
        "starwarsDB.film",
        filter_column="film_id",
        filter_value=index
    )

    from models.datamodels.films import FilmResponse
    from pydantic import parse_obj_as
    final = parse_obj_as(list(FilmResponse), result)

    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/starships", methods=["GET"])
def get_starships():
    result = fetch_resources("starwarsDB.starships")
    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/vehicles", methods=["GET"])
def get_vehicles():
    result = fetch_resources("starwarsDB.vehicles")
    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/planets", methods=["GET"])
def get_planets():
    result = fetch_resources("starwarsDB.planets")
    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/species", methods=["GET"])
def get_species():
    result = fetch_resources("starwarsDB.species")
    return Response(json.dumps(result), status=200, mimetype="application/json")

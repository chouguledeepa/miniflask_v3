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
from models.datamodels.films import FilmResponse

crud_app = Blueprint("crud_app", __name__, url_prefix="/swapi")


@crud_app.route("/people", methods=["GET"])
def get_characters():

    # TODO - copy films plural endpoint and implement here
    result = fetch_resources("starwarsDB.characters")
    return Response(json.dumps(result), status=200, mimetype="application/json")


# plural API endpoint
@crud_app.route("/films", methods=["GET"])
def get_films():
    result = fetch_resources("starwarsDB.film")

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

    if result:
        response_obj = FilmResponse(**result[0])
        return Response(response_obj.json(), status=200, mimetype="application/json")
    else:
        response_obj = {"ERROR": f"No records found for ID - {index}"}
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


# TODO : implement singular endpoint for each and every resource
# planet, character, species, vehicles, starships


@crud_app.route("/starships", methods=["GET"])
def get_starships():
    # TODO - copy films plural endpoint and implement here
    result = fetch_resources("starwarsDB.starships")
    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/vehicles", methods=["GET"])
def get_vehicles():
    # TODO - copy films plural endpoint and implement here
    result = fetch_resources("starwarsDB.vehicles")
    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/planets", methods=["GET"])
def get_planets():
    # TODO - copy films plural endpoint and implement here
    result = fetch_resources("starwarsDB.planets")
    return Response(json.dumps(result), status=200, mimetype="application/json")


@crud_app.route("/species", methods=["GET"])
def get_species():
    # TODO - copy films plural endpoint and implement here
    result = fetch_resources("starwarsDB.species")
    return Response(json.dumps(result), status=200, mimetype="application/json")

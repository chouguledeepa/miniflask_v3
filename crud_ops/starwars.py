"""
http://127.0.0.1:5000/swapi/people
http://127.0.0.1:5000/swapi/films (plural API GET, POST endpoint)
http://127.0.0.1:5000/swapi/films/1 (singular API endpoint)
http://127.0.0.1:5000/swapi/species
http://127.0.0.1:5000/swapi/vehicles
http://127.0.0.1:5000/swapi/starships
http://127.0.0.1:5000/swapi/planets

##

GET
POST
PATCH



"""

import json
from flask import Blueprint, Response, Flask, request
from pydantic.error_wrappers import ValidationError
from models.dal.dml import fetch_resources, fetch_resource, __delete_resource
from models.datamodels.films import FilmResponse, Film_, PatchFilm_
from models.dal.dml import insert_resource, upsert_films

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


@crud_app.route("/films", methods=["DELETE"])
def delete_films():
    """
    There are 2 types of parameters
    - PATH variable
    - QUERY parameter
    Returns:

    """

    film_id = int(request.args.get("film_id"))
    result = __delete_resource("starwarsDB.film", "film_id", film_id)

    if result == 0:
        response_obj = {
            "ERROR": f"no records found to delete against film_id {film_id}"
        }
        return Response(
            json.dumps(response_obj), status=200, mimetype="application/json"
        )

    response_obj = {"message": f"successfully deleted records - {film_id}"}
    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@crud_app.route("/films", methods=["PUT"])
def put_films():
    request_data = request.json
    try:
        film_data = Film_(**request_data)
    except ValidationError as ex:
        return Response(
            json.dumps({"message": "bad request"}),
            status=400,
            mimetype="application/json",
        )
    home_url = "https://swapi.dev"
    relative = "/api/film/{num_}"  # magic string
    absolute_url = home_url + relative.format(num_=film_data.film_id)

    result = upsert_films(film_data, absolute_url)

    success_msg = "New record created successfully"

    response_obj = {
        "records_count": result,
        "film_name": film_data.title,
        "message": success_msg if result else "Existing record updated",
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@crud_app.route("/films", methods=["PATCH"])
def patch_films():
    request_data = request.json
    film_data = PatchFilm_(**request_data)

    home_url = "https://swapi.dev"
    relative = "/api/film/{num_}"  # magic string
    absolute_url = home_url + relative.format(num_=film_data.film_id)

    result = upsert_films(film_data, absolute_url)

    success_msg = "New record created successfully"

    response_obj = {
        "records_count": result,
        "film_name": film_data.title,
        "message": success_msg if result else "Existing record updated",
    }

    return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@crud_app.route("/films", methods=["POST"])
def post_films():

    request_data = request.json
    film_data = Film_(**request_data)

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date.strftime("%y-%m-%d"),
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]

    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

    success_msg = "record created successfully"

    response_obj = {
        "records_count": result,
        "film_name": film_data.title if result else "",
        "message": success_msg if result else "ERROR",
    }

    return Response(
        json.dumps(response_obj),
        status=201 if result else 409,
        mimetype="application/json",
    )


# singular API endpoint
@crud_app.route("/films/<int:index>", methods=["GET"])
def get_film(index):
    result = fetch_resource(
        "starwarsDB.film", filter_column="film_id", filter_value=index
    )

    if result:
        response_obj = FilmResponse(**result[0])
        return Response(response_obj.json(), status=200, mimetype="application/json")
    else:
        response_obj = {"ERROR": f"No records found for ID - {index}"}
        return Response(
            json.dumps(response_obj), status=200, mimetype="application/json"
        )


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

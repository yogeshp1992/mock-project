import json
import requests
from flask import Blueprint, request, Response
from dal.dml import fetch_resource, insert_resource
from models.datamodels.characters import Character_
from models.datamodels.films import Film_
from models.datamodels.planets import Planet_
from models.datamodels.starships import Starship_
from models.datamodels.species import Species_
from pydantic import parse_obj_as, error_wrappers

from pydantic import BaseModel, validator
from typing import Union, Optional

from resources.starwars import starwar_app

# Blueprit class instantiation
star_app = Blueprint("star", __name__, url_prefix="/star")


@star_app.route("/wel")
def welcome():
    return "hello world from star sub-application"


@star_app.route("/people")
def fetch_data():
    data = fetch_resource("people")
    characters = data.get("results")
    characters = parse_obj_as(list[Character_], characters)
    response = {
        "count": data.get("count"),
        "message": "successful"
    }
    return response


@star_app.route("/films")
def film_fetch_data():
    data = fetch_resource("films")
    film = data.get("results")
    film = parse_obj_as(list[Film_], film)
    response = {
        "count": data.get("count"),
        "message": "successful"
    }
    return response


@star_app.route("/planets")
def planet_fetch_data():
    data = fetch_resource("planets")
    planet = data.get("results")
    planet = parse_obj_as(list[Planet_], planet)
    response = {
        "count": data.get("count"),
        "message": "successful"
    }
    return response


@star_app.route("/starships")
def starship_fetch_data():
    data = fetch_resource("starships")
    starships = data.get("results")
    starships = parse_obj_as(list[Starship_], starships)
    response = {
        "count": data.get("count"),
        "message": "successful"
    }
    return response


@star_app.route("/species")
def species_fetch_data():
    response = requests.get("https://swapi.dev/api/species/")
    data = response.json()
    species = data.get("results")
    species = parse_obj_as(list[Species_], species)
    response = {
        "count": data.get("count"),
        "message": "successful"
    }
    return response


@star_app.route("/films", methods=["POST"])
def post_films():
    request_data = request.json
    breakpoint()
    try:
        film_data = Film_(**request_data)
        return request_data
    except:
        error_wrappers.ValidationError
    film_columns = ["film", "film_id", film_data.episode_id,
        "name",
        "sr.no"
    ]

    film_values = [
        film_data.name,
        film_data.sr.no
    ]
    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

@starwar_app.route("/selfi", methods=["POST"])
def self_films():
    request_data = request.json
    breakpoint()
    try:
        self_data = info_(**request_data)
    except:
        error_wrappers.ValidationError
    film_columns = ["namee",
                    "villege"
                    "education"
                    "course"
                    ]

    film_values = [
        self_data.namee,
        self_data.villege,
        self_data.education,
        self_data.course
    ]
    result = insert_resource("myinf", "char_id", 111111,
                             film_columns, film_values
                             )
    return result

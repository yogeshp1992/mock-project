"""

GET
POST
DELETE
PATCH
PUT
"""

from flask import Blueprint
starwar_app = Blueprint("starwars", __name__, url_prefix="/starwars")


@starwar_app.route("/welcome")
def welcome():
    return "hello world from starwars sub-application"
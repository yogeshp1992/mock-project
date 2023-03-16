from flask import Flask

from resources.starwars import starwar_app
from tasks.api import tasks_app


app = Flask(__name__)


# register all the sub-applications here
app.register_blueprint(starwar_app)
app.register_blueprint(tasks_app)

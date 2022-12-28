"""
# BRD :: Business Requirement Document

data source1 - https://swapi.dev/api      - starwarsAPI
    API endpoint1 - /people - names of characters who's height > 30
    API endpoint2 - /films - names of films where "Luke" is main character

data source 2 - aws server data storage   - stocksAPI
    API endpoint1 - /stocks
    API endpoint1 - /funds



MAIN_API -       starwarsAPI
                 stocksAPI


MICRO-SERVICE

API endpoints -

http://127.0.0.1:5000/taskone
http://127.0.0.1:5000/tasktwo
http://127.0.0.1:5000/taskthree
http://127.0.0.1:5000/taskfour

"""


# third party imports
from flask import Flask
from starwars_tasks.tasks import starwars_v1
from crud_ops.starwars import crud_app


# application instantiation
app = Flask(__name__)


# registering sub-applications with main flask application
app.register_blueprint(starwars_v1)
app.register_blueprint(crud_app)
print(app.blueprints)

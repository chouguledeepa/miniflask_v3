from flask import Flask
from flask_restful import Resource, Api, reqparse
from models.datamodels.films import Film_
from models.dal.dml import fetch_resource
from abc import ABC


parser = reqparse.RequestParser()


class ResourceBase(Resource, ABC):

    def __init__(self):
        super().__init__()

    def character_names(self):
        # TODO - character name manipulation logic



class Films(ResourceBase):
    def get(self):
        # TODO - logic to get all film data
        return {'hello': 'world'}

    def post(self):
        args = parser.parse_args()
        ## TODO - you'll get request body
        ## TODO - you'll either use pydantic model / marshmallow
        ## TODO - create DB entry
        ## TODO - generate response in agreed format (pydantic)
        return {'hello': 'world'}


app = Flask(__name__)

api = Api(app)
api.add_resource(Films, '/')
api.add

if __name__ == '__main__':
    app.run(debug=True)

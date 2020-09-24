import os
from flask_restful import Api, Resource
import flask
from tinydb import TinyDB, Query
import json
import get_data
db = TinyDB('data.json')
get_data.get_data(db)
## DB lookup
def get_country_name(code) :
    db = TinyDB('data.json')
    country = Query()
    doc = db.get( country['code'] == code)
    return doc

def get_country_code(name) :
    db = TinyDB('data.json')
    country = Query()
    doc = db.get( country['name'] == name)
    return doc

## Flask API

app = flask.Flask(__name__)
api = Api(app)



class CountryCode(Resource):
    def get(self,name):
        response = get_country_code(name)
        return response

class CountryName(Resource):
    def get(self,code):
        response = get_country_name(code)
        return response

class Health(Resource):
    def get(self):
        response = get_country_code('India')['code']
        if response=='IN':
            return {'status':'OK'}
        else:
            return {'status':'FAILED'}

class Diag(Resource):
    def get(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'data_dump.json')
        with open(my_file, 'r') as f:
            response=json.loads(f.read())
        return response


api.add_resource(Health, "/health")
api.add_resource(Diag, "/diag")
api.add_resource(CountryCode, "/convert/<string:name>")
api.add_resource(CountryName, "/convert_name/<string:code>")


if __name__ == '__main__' :
    app.run( host="0.0.0.0")


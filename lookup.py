
from flask_restful import Api, Resource
import flask
from tinydb import TinyDB, Query
import json



def get_country_name(code) :
    db = TinyDB('data.json')
    country = Query()
    doc = db.get( country['code'] == code)
    #print(doc)
    return doc

def get_country_code(name) :
    db = TinyDB('data.json')
    country = Query()
    doc = db.get( country['name'] == name)
    #print(doc)
    return doc


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
        with open('data_dump.json', 'r') as f:
            response=json.loads(f.read())
        return response


api.add_resource(Health, "/health")
api.add_resource(Diag, "/diag")
api.add_resource(CountryCode, "/convert/<string:name>")
api.add_resource(CountryName, "/convert_name/<string:code>")


if __name__ == '__main__' :
    app.run(debug=True)


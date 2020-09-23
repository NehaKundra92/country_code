from flask_restful import Api, Resource
import flask
from tinydb import TinyDB, Query
import json
db = TinyDB('data.json')
country = Query()
doc = db.get( country['name'] == 'India')
print(doc)

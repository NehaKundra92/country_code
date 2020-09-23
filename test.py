from tinydb import TinyDB, Query
import json
db = TinyDB('data.json')
country = Query()
doc = db.get(country['name'] == 'India')
print(doc['code'])
with open('data_dump.json', 'r') as f:
    print(type(f.read()))


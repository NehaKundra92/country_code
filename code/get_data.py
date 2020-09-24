import requests
from tinydb import TinyDB
import json
import os


'''
URL="https://www.travel-advisory.info/api"
res= requests.get(URL)
result=res.json()
with open ('data_dump.json', 'w') as f:
    json.dump(result, f)
    '''

def get_data(db):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'data_dump.json')
    with open(my_file, 'r') as file :
        data = json.loads(file.read())

    for i in data['data'].items() :

        country_data = {}
        country_data['name'] = i[1]['name']
        country_data['code'] = i[0]
        db.insert(country_data)

if __name__ == '__main__' :
    db = TinyDB('data.json')
    table = db.table('_default', cache_size=None)
    get_data(db)











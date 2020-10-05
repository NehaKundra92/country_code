import requests
from tinydb import TinyDB
import json
import os


def dataApiStatus():
    URL = "https://www.travel-advisory.info/api"
    res = requests.get(URL)
    return res

def get_data():
    db = TinyDB('data.json')
    res=dataApiStatus()
    result = res.json()
    for i in result['data'].items() :

        country_data = {}
        country_data['name'] = i[1]['name']
        country_data['code'] = i[0]
        db.insert(country_data)

if __name__ == '__main__' :
    db = TinyDB('data.json')
    table = db.table('_default', cache_size=None)





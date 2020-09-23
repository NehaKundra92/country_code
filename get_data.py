import requests
from tinydb import TinyDB
import json
db=TinyDB('data.json')
URL="https://www.travel-advisory.info/api"
res= requests.get(URL)
result=res.json()
with open ('data_dump.json', 'w') as f:
    json.dump(result, f)



for i in result['data'].items():
    country_data={}
    country_data['name']=i[1]['name']
    country_data['code']=i[0]
    db.insert(country_data)









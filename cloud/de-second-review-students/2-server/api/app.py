import json
from fastapi import FastAPI, HTTPException

client = FastAPI()

@client.get('/healthcheck')
def handle_healthcheck():
    return {'message': 'all ok'}

@client.get('/doughnuts/info')
def get_doughnuts(max_calories: int = 9999999, allow_nuts: bool = True):
    response = {'results': []}
    with open('../data/doughnuts.json', 'r') as data:
        for line in json.loads(data.read())["doughnut_data"]:
            if line['calories'] <= max_calories:
                if allow_nuts:
                    response['results'].append({'doughnut_type': line['doughnut_type'], 'price': line['price']})
                else:
                    if line['contains_nuts'] != True:
                        response['results'].append({'doughnut_type': line['doughnut_type'], 'price': line['price']})
    if response['results'] == []:
        raise HTTPException(status_code=204)
    return response



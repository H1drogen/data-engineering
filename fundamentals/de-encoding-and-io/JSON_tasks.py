import json
from json import *

def JSON_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-16') as f:
        file = json.load(f)
        return file['Cars']

# JSON_to_dict('./data/cars.json')

def collection_of_car_makes(file_path):
    with open(file_path, 'r', encoding='utf-16') as f:
        file = json.load(f)
        collection = set()
        for entry in file['Cars']:
            collection.add(entry['make'])
        return collection

# collection_of_car_makes('./data/cars.json')


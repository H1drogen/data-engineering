import json

import requests


# Write a function called get_pets that does the same as the Task 2 but for pets.
# The endpoint is https://nc-leaks.herokuapp.com/api/people/:username/pets;

def get_pets():
    with open('../task_1/northcoders.json', 'r', encoding='utf-8') as data:
        pets = []
        for line in json.loads(data.read()):
            response = requests.get(url='https://nc-leaks.herokuapp.com/api/people/' + line['username'] + '/pets')
            if response.status_code == 404:
                continue
            pets.append(response.json())
    return json.dumps(pets)


print(get_pets())

import requests
import json

from task_1.task_1 import get_people
from task_2.task_2 import get_interest
from task_3.task_3 import get_pets


# Create a function called scavenge_for_nc_data that uses all of the functions you created in Tasks 1-3 to automate your hunt for data.

def scavenge_for_nc_data():
    base_data = json.loads(get_people())
    interest_data = json.loads(get_interest())
    pets_data = json.loads(get_pets())

    for person in base_data:
        username = person.get('username')
        for interest in interest_data:
            if username == interest['person']['username']:
                person['interests'] = interest['person']['interests']
        for pet in pets_data:
            if username == pet['person']['pets']:
                person['interests'] = pet['person']['pets']
    return json.dumps(base_data)

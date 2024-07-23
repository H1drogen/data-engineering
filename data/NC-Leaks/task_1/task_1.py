# ### Task 1

# Write a function called `get_people` that will retrieve list of all the available people on the `northcoders` server . This should:

# 1. Use the [`requests`](https://pypi.org/project/requests/) module to make a request to `https://nc-leaks.herokuapp.com/api/people`.
# 2. Once you have the response body as a useable dictionary, look through the people to find anyone who has `northcoders` as the workplace.
# 3. Save these `northcoders` employees to a file called `northcoders.json`.

import requests
import json



def get_people():
    my_url = 'https://nc-leaks.herokuapp.com/api/people'
    data_response = requests.get(url=my_url)
    response = data_response.json()
    northcoders = []
    for person in response['people']:
        if 'northcoders' in person['job']['workplace']:
            northcoders.append(person)
    return json.dumps(northcoders)

print(get_people())


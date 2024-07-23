# ### Task 2

# Write a function called `get_interests` that uses the newly found usernames for each northcoder to retrieve information on everyone's interests. This function should:

# 1. Read the `northcoders.json` file you created in task 1
# 2. For every person, use their `username` and make a request to `https://nc-leaks.herokuapp.com/api/people/:username/interests` to get their interests.
# 3. Each response will be a JSON with a person key. Collect up the data on this `person` key into a list.
# 4. Once you have all responses in the list, save it to a file called `interests.json`.
import json
import requests

def get_interest():
    with open('../task_1/northcoders.json', 'r', encoding='utf-8') as data:
        interests = []
        for line in json.loads(data.read()):
            response = requests.get(url='https://nc-leaks.herokuapp.com/api/people/'+line['username']+'/interests')
            interests.append(response.json())
    return json.dumps(interests)
print(get_interest())

    
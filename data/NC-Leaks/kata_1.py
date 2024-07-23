import requests
# Make a request using the requests module to the following endpoint to get the instructions left for you: /api/top-secret
# Once you have your instructions, save them in a markdown file (a file with a .md extension)
# Hint: The body of the response will be in JSON format. Don't save the whole JSON to a file, but instead extract the instructions from the JSON and save those as markdown.

my_url = 'https://nc-leaks.herokuapp.com/api/top-secret'
response = requests.get(url=my_url)
json_response = response.json()
instructions = json_response['instructions']
print(instructions)
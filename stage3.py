import requests
import json

api_token = "87077d8cec8244ce87b5f720efca70af"
url_haystack = "http://challenge.code2040.org/api/haystack"
url_validate = "http://challenge.code2040.org/api/haystack/validate"
index = 0
value_to_find = 'needle'
array = 'haystack'

json_data = {"token": api_token}

request = requests.post(url_haystack, json_data)

#Calling the json decoder.
json = request.json()

value_to_find = json[value_to_find]

for element in json[array]:
    if element == value_to_find:
        break
    index += 1

json_data = {"token": api_token, "needle": index}
send_data = requests.post(url_validate, json_data)

print send_data.text

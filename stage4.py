import requests
import json

api_token = "87077d8cec8244ce87b5f720efca70af"
url_prefix = "http://challenge.code2040.org/api/prefix"
url_validate = "http://challenge.code2040.org/api/prefix/validate"
prefix = 'prefix'
array = 'array'
container = []

json_data = {'token': api_token}

request = requests.post(url_prefix, json_data)

#Decoding the json data
json = request.json()
prefix = json[prefix]
array = json[array]

#Storing all the elements that don't contain the prefix in a list.
for element in array:
    if prefix != element[:len(prefix)]:
        container.append(element)

json_data = {"token": api_token, "array": container}
#Before we send the json data back we have to encode it.
send_data = requests.post(url_validate, json=json_data)

print send_data.text


import requests
import json

api_token = "87077d8cec8244ce87b5f720efca70af"
url_prefix = "http://challenge.code2040.org/api/prefix"
prefix = 'prefix'
array = 'array'
container = []

json_data = {'token': api_token}

request = requests.post(url_prefix, json_data)

json = request.json()
prefix = json[prefix]
array = json[array]

print "Prefix:", prefix

for element in array:
    if prefix != element[:len(prefix)]:
        print element

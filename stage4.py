import requests
import json

api_token = "87077d8cec8244ce87b5f720efca70af"
url_prefix = "http://challenge.code2040.org/api/prefix"
prefix = 'prefix'
array = 'array'

json_data = {'token': api_token}

request = requests.post(url_prefix, json_data)

print request.text

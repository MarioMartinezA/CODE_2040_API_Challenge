import requests
import json

api_token = "87077d8cec8244ce87b5f720efca70af"
url_haystack = "http://challenge.code2040.org/api/haystack"

json_data = {"token": api_token}

request = requests.post(url_haystack, json_data)

print request.text

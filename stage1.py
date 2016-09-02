import requests
import json


api_token = "87077d8cec8244ce87b5f720efca70af"
github = "https://github.com/MarioMartinezA/CODE_2040_API_Challenge"
url_register = "http://challenge.code2040.org/api/register"
json_data = {"token": api_token, "github": github}

#Sending the token and github url
request = requests.post(url_register, json_data)

print request.text

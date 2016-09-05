import requests
import json

api_token = "87077d8cec8244ce87b5f720efca70af"
github = "https://github.com/MarioMartinezA/CODE_2040_API_Challenge"
url_reverse = "http://challenge.code2040.org/api/reverse"
url_validate = "http://challenge.code2040.org/api/reverse/validate"

json_data = {"token": api_token}

request = requests.post(url_reverse, json_data)


#Reversing the string
reverse_string = request.text
reverse_string = reverse_string[::-1]

json_data = {"token": api_token, "string": reverse_string}
send_data = requests.post(url_validate, json_data)


print send_data.text



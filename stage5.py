import json
import requests
import datetime
import dateutil.parser as dp

api_token = "87077d8cec8244ce87b5f720efca70af"
url_dating = "http://challenge.code2040.org/api/dating"
url_validate = "http://challenge.code2040.org/api/dating/validate"

json_data = {"token": api_token}
date = "datestamp"
interval = "interval"

iso8601_format = "%Y-%m-%dT%H:%M:%SZ"

request = requests.post(url_dating, json_data)

#Grabbing the date and the interval
json = request.json()
date = json[date]
interval = json[interval]

print date, interval

#Stripping the time from the string
timestamp = datetime.datetime.strptime(date, iso8601_format)

#Adding the seconds to the time
interval = long(interval)
timestamp = timestamp + datetime.timedelta(seconds = interval)
new_time = timestamp.isoformat()
new_time = str(new_time) + 'Z'

print new_time

json_data = {"token": api_token, "datestamp": new_time}

send_data = requests.post(url_validate, json=json_data)

print send_data.text



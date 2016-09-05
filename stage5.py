import json
import requests
import datetime

api_token = "87077d8cec8244ce87b5f720efca70af"
url_dating = "http://challenge.code2040.org/api/dating"
json_data = {"token": api_token}
date = "datestamp"
interval = "interval"
iso8601_format = "%Y-%m-%dT%H:%M:%S%fZ" 

request = requests.post(url_dating, json_data)

json = request.json()
date = json[date]
interval = json[interval]

#Stripping the time from the string
timestamp = datetime.datetime.strptime(date, iso8601_format)

#Adding the seconds to the time
timestamp = timestamp + datetime.timedelta(seconds=int(interval))

#Converting it to a string
timestamp = str(timestamp)

#Formatting our string back to it's original format
timestamp = timestamp.replace(' ', 'T')
timestamp = timestamp.replace('.', 'Z')

print date
print timestamp[:len(timestamp) - 6]





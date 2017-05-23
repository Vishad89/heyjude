import requests
import json

parameters = {"lat": 68, "lon" : -99}

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.status_code)
#print (response.content)
data = response.json()
print (type(data))
print (data)
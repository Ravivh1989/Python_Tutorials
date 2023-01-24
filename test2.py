import requests
import json
response = requests.get("https://api.openaq.org/v1/measurements?city=Paris&parameter=pm25")
response.status_code

response_json = response.json()
json_string = json.dumps(response_json)
print(json_string)

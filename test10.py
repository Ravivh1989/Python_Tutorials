# import requests

# url = requests.get('http://127.0.0.1:5000/home/Ravi')

import requests
api_url = "http://127.0.0.1:5000/home/Amith"
response = requests.get(api_url)
print(response.text)
# import urllib library
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "https://api.github.com"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the json response
print(data_json)

# for key,value in data_json.items():
#     if key == 'events_url':
#         print(value)



userlist = []
others = []
for i in data_json:
    if i.startswith('user'):
        userlist.append(i)
    else:
        others.append(i)

eventlist = []

for i in others:
    if i.startswith('events'):
        eventlist.append(i)
    

# print(eventlist)
# with open('./files/user.txt', 'w') as file:
#     file.write(str(userlist))

# with open('./files/other.txt', 'w') as file2:
#     file2.write(str(others))
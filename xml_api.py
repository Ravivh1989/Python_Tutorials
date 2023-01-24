import requests

xml = """<?xml version="1.0" encoding="utf-8"?>
<Request>
   <Login>login</Login>
   <Password>password</Password>
</Request>"""

headers = {'Content-Type': 'application/xml'} 
r = requests.post('https://reqbin.com/echo/post/xml', data=xml, headers=headers)

print(r.text)
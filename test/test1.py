# encoding = utf-8

import requests
import json

url = "http://test.server.com/users"

parms = {'user': 'abc', 'pwd': '123'}
headers = { 'Content-Type': 'application/json;charset=utf-8'}

res = requests.post (url, data=parms, headers=headers)

text = res.text

print (json.loads (text))
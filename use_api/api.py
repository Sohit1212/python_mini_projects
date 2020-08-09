import requests
import json

baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc':'887445005711'}

response = requests.get(baseUrl,params=parameters)
print(response.url)
content = response.content
data = json.loads(content)

title = data['items'][0]['title']
brand = data['items'][0]['brand']

print("Title: %s \nBrand: %s" % (title,brand))

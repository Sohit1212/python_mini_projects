import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/weather'
parameters = {'q':'Nagpur,IN', 'appid':'14c9cee20f2b8e897d0c7b6ab571934f'}

response = requests.get(baseUrl,params=parameters)
content = response.content
print(content)

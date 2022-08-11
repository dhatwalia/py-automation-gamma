from urllib import response
import requests

keyPart1 = 'b77a02d9b416d307'
keyPart2 = 'e0e89867ae902a51'
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': keyPart1 + keyPart2, 'q': 'Toronto,CA'}
response = requests.get(baseUrl, params=parameters)
print(response.content)

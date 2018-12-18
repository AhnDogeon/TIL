# import requests
# # url = 'https://api.darksky.net/forecast/7214b67b19c9d40bfa0d8d64ec638240/37.501826,%20127.039649'

# # res = requests.get(url)
# # data=res.json()

# # print(data)
# # print(data['currently']['summary'])


## pypi를 통한 조금 더 쉬운 api 따오기
from darksky import forecast
multicampus = forecast('7214b67b19c9d40bfa0d8d64ec638240', 37.501311, 127.037471)
print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

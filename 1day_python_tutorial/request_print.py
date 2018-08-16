import requests

url = "http://ip-api.com/json/naver.com"
data = requests.get(url)
data = data.json()
print(data['lat'],data['lon'])
print(data)


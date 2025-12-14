import requests

respone=requests.get(url=" https://api.sunrise-sunset.org/json")

print(respone.status_code)
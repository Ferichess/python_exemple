import requests

base_url = "https://reqres.in/"
endpoint = "api/users"
url = base_url + endpoint

paramters = {"page": 2}

response = requests.get(url, params=paramters)
print(response.url)

if response.status_code == 200:
    print("Request is Successful and Status code is 200", response.status_code)
else:
    print("Request is not Successful")

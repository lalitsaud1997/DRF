import requests
URL = "http://127.0.0.1:8000/stuinfo/4"
req_info = requests.get(url=URL)
json_data = req_info.json()
print(json_data)
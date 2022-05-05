#(step-5)
import json
import requests

URL = "http://127.0.0.1:8000/stucreate/"
data = {
    'name':'lalit saud',
    'roll':'202',
    'city':'nepal'
}

json_data = json.dumps(data)
response = requests.post(url=URL, data=json_data)
data = response.json()
print(data)
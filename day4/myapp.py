import requests
import json
URL = "http://127.0.0.1:8000/studentapi/"

#For Data Read:
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data=json_data)
    data = res.json()
    print(data)
get_data(2)

#For Data Create:
def post_data():
    data = {
        'name':'Lalit Saud',
        'roll':1,
        'city':'Kathmandu'
    }
    json_data = json.dumps(data)
    response = requests.post(url=URL, data=json_data)
    data = response.json()
    print(data)
# post_data()

#For Update Data....(partial=True in serializer data for partial update),
#  and(partial=True remove in serializer data for complete data)
#and using PUT method....
def update_data():
    data = {
        'id':4,
        'name':'Anita Rokaya',
        'roll':13,
    }
    json_data = json.dumps(data)
    response = requests.put(url=URL, data=json_data)
    data = response.json()
    print(data)
# update_data()

# For Delete data.....
def delete_data():
    data = {
        'id':6
    }
    json_data = json.dumps(data)
    response = requests.delete(url=URL, data=json_data)
    data = response.json()
    print(data)
# delete_data()
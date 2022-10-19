import requests

header = {'Authorization': 'Bearer 150edfeb55bd9ec52f556b50a4f61a50d9967296'}
endpoint = "http://localhost:8000/api/products/"


data = {
    "title": "New title again",
    "price":50.99
    }

get_response = requests.post(endpoint, json=data, headers=header)
print(get_response.json())
from urllib import request
import requests
from getpass import getpass


endpoint = "http://localhost:8000/api/auth/"
username = input("What is your username?\n")
password = getpass("What is your password?\n")

auth_response = requests.post(endpoint, json={'username':username, 'password':password})
print(auth_response.json())

if auth_response.status_code ==200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Bearer {token}"
    }

    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
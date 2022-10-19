import requests

endpoint = "http://localhost:8000/api/products/26543213532/"

get_reponse = requests.get(endpoint)
print(get_reponse.json())

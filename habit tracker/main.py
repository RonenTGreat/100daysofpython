import requests
from datetime import datetime

USERNAME = "ronenthegreat"
TOKEN = "eihidunijdoiidnife09udy"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hr",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2022, month=8, day=14)
post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3"
}
# response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(response.text)
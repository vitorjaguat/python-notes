import requests
import os
import datetime as dt

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'jaguat'
TOKEN = os.environ.get('PIXELA_APIKEY')


# Creating user:
user_params = {
    "token": TOKEN,
    "username": "jaguat",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# Creating a graph:
# https://docs.pixe.la/entry/post-graph

colors = {
    "green": "shibafu",
    "red": "momiji",
    "blue": "sora",
    "yellow": "ichou",
    "purple": "ajisai",
    "black": "kuro"
}

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id": "b2d-xyz", #can create any id
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "kuro"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
# print(headers["X-USER-TOKEN"])

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Creating a pixel in the graph
GRAPH_ID = graph_config["id"]
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
pixel_headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_config = {
    # "date": str(dt.date.today()).replace('-', ''),
    "date": dt.datetime.now().strftime('%Y%m%d'),
    "quantity": input('How many kilometers did you cycle today? ')
}

response = requests.post(url=pixel_endpoint, headers=pixel_headers, json=pixel_config)
print(response.text)


# PUT and DELETE requests:
date = dt.datetime(year=2023, month=7, day=2).strftime("%Y%m%d")
put_endpoint = f'{pixel_endpoint}/{date}'
put_headers = pixel_headers
put_config = {
    "quantity": "23.3"
}

# response = requests.put(url=put_endpoint, headers=put_headers, json=put_config)
# print(response.text)

response = requests.delete(url=put_endpoint, headers=put_headers)
# print(response.text)

# https://pixe.la/v1/users/jaguat/graphs/b2d-xyz.html


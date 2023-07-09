from pprint import pprint
import requests
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = 'https://api.sheety.co/8f1bbcc5c1484f27433771ec3c8c8d59/flightDeals/prices'
        self.sheety_headers = {
            "Authorization": "Bearer " + os.environ.get('SHEETY_TOKEN')
        }

    def get_prices(self):
        response = requests.get(self.sheety_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        return response.json()
    
    def update_sheet(self, id, column, data):
        put_url = self.sheety_endpoint + '/' + str(id)
        body = {
            "price": {
                column: data
            }
        }
        response = requests.put(url=put_url, headers=self.sheety_headers, json=body)
        pprint(response.text)
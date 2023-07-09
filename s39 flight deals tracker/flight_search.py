import requests
from pprint import pprint
import datetime as dt
from flight_data import FlightData
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
        self.TEQUILA_API_KEY = os.environ.get('TEQUILA_KIWI_APIKEY')

    def get_destination_code(self, city_name):
        endpoint = self.TEQUILA_ENDPOINT + '/locations/query'
        params = {
            "term": city_name,
            "location_types": "city"
        }
        headers = {
            "apikey": self.TEQUILA_API_KEY,
        }
        response = requests.get(url=endpoint, headers=headers, params=params)
        code = response.json()['locations'][0]['code']
        # pprint(response.json())
        return code
    
    def search_flight(self, from_city, to_city):
        endpoint = self.TEQUILA_ENDPOINT + '/v2/search'
        tequila_params = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_to": (dt.datetime.today() + dt.timedelta(days=180)).strftime('%d/%m/%Y'),
            "date_from": (dt.datetime.today() + dt.timedelta(days=1)).strftime('%d/%m/%Y'),
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "one_for_city": 1,
            "curr": "BRL",
            "max_stopovers": 0
        }
        tequila_headers = {
            "apikey": self.TEQUILA_API_KEY
        }
        response = requests.get(url=endpoint, params=tequila_params, headers=tequila_headers)
        
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f'No direct flights found for {to_city}')
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: R${flight_data.price}")
            return flight_data
    

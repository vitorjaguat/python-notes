#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
import requests
import os
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

TEQUILA_KIWI_APIKEY = os.environ.get('TEQUILA_KIWI_APIKEY')

ORIGIN_CITY_IATA = "RIO"

data_manager = DataManager()
sheet_data = data_manager.get_prices()
notification_manager = NotificationManager()

# print(FlightSearch().get_destination_code('Rio de Janeiro'))

for row in sheet_data['prices']:
    # check if there is any row with no Iata code:
    if not row['iataCode']:
        flight_search = FlightSearch()
        iata_code = flight_search.get_destination_code(row['city'])

        data_manager.update_sheet(id=row['id'], column='iataCode', data=iata_code)

for row in sheet_data['prices']:
    # search flights for each destination:
    flight_search = FlightSearch()
    flight_data = flight_search.search_flight(from_city=ORIGIN_CITY_IATA, to_city=row['iataCode'])
    if flight_data:
        pprint(vars(flight_data))
        if float(flight_data.price) < float(row['lowestPrice']):
            notification_manager.send_notification(message=f"Low price alert! Only £{flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.out_date} to {flight_data.return_date}.")


# flight_search = FlightSearch()
# riolon = flight_search.search_flight(from_city='RIO', to_city='LON')
# pprint(riolon['data'][0]['price'])
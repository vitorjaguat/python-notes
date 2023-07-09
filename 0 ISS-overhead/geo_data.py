import requests
from datetime import datetime
import os

class GeoData:
    def __init__(self):
        self.OPENWEATHER_KEY = os.environ.get('OPENWEATHER_KEY')
        self.MY_LAT = -22.967404
        self.MY_LONG = -43.191294
        self.city_name = 'Rio de Janeiro, Brasil'


    def find_latlon(self):
        params = {
            "q": self.city_name,
            "appid": self.OPENWEATHER_KEY
        }
        print(self.OPENWEATHER_KEY)
        response = requests.get('http://api.openweathermap.org/geo/1.0/direct', params=params)
        data = response.json()
        print(data)
        self.MY_LAT = data[0]['lat']
        self.MY_LON = data[0]['lon']


    def check_proximity(self):
        """Your position is within +5 or -5 degrees of the ISS position."""
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        self.find_latlon()

        is_close_enough = self.MY_LAT-5 <= iss_latitude <= self.MY_LAT+5 and self.MY_LONG-5 <= iss_longitude <= self.MY_LONG+5
        return is_close_enough
    
    def is_dark(self):
        """checks if is dark enough to be see the ISS"""
        parameters = {
            "lat": self.MY_LAT,
            "lng": self.MY_LONG,
            "formatted": 0,
        }

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        time_now = datetime.now()
        now_hour = time_now.hour
        # return now_hour >= sunrise or now_hour <= sunset
        return True
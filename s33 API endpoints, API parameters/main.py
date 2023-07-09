import requests
import datetime

#SIMPLE REQUEST (NO PARAMETERS)
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# print(response.status_code)
# response.raise_for_status() # raise an exception if status_code is not 200

# data = response.json()
# latitude = data['iss_position']
# longitude = data['iss_position']
# print(data)


#REQUEST WITH PARAMETERS
MY_LAT = -22.967404
MY_LON = -43.191294

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0
}

# https://api.sunrise-sunset.org/json?lat=-22.967404&lng=-43.191294
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise= data['results']['sunrise'].split('T')[1].split(':')
sunset= data['results']['sunset'].split('T')[1].split(':')
print(sunrise)

time_now = datetime.datetime.now()
print(time_now)
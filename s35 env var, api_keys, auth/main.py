import requests
import os

#https://stackoverflow.com/questions/29003305/sending-telegram-message-from-python
# telegram jaguat_weather_bot api:
telegram_token = os.environ.get("JAGUAT_WEATHER_TG_TOKEN")
chat_id = os.environ.get("JAGUAT_WEATHER_TG_CHATID")

def telegram_bot_sendtext(bot_message):
   bot_token = telegram_token
   bot_chatID = chat_id
   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


# https://home.openweathermap.org/
api_key = os.environ.get("OWM_API_KEY")

parameters = {
    "lat": -22.906847,
    "lon": -43.172897,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly']
print(response.json())
weather_data_12 = [item['weather'][0]['id'] for item in weather_data[:12]]
print(weather_data_12)

if 500 in weather_data_12:
    print('Yes, it will rain.')
    telegram_bot_sendtext('It will rain today.')






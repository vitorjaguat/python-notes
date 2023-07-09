import requests
from datetime import datetime
import smtplib
import time
from geo_data import GeoData
from telegram import TelegramNotification

geo_data = GeoData()
telegram_notification = TelegramNotification()





        

def set_interval(func, interval): # emulating JS's setInterval
    while True:
        if geo_data.is_dark() and geo_data.check_proximity():
            func()
            print('Sent notification!')
        else:
            print('Not yet.')
        time.sleep(interval)

# set_interval(send_email_notification, 60)



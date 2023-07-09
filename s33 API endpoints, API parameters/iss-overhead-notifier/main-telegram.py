import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -22.967404
MY_LONG = -43.191294


#Your position is within +5 or -5 degrees of the ISS position.
def check_proximity():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    is_close_enough = MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5
    return is_close_enough




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    now_hour = time_now.hour
    return now_hour >= sunrise or now_hour <= sunset


def send_email_notification():
    my_email = 'jaguattt@gmail.com'
    pw = 'secret!'
    pw_app = 'secret!'
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw_app)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs='vitorbutkus@gmail.com', 
            msg=f"Subject:Look to the sky!\n\nThe ISS is now visible in your location.")
        

def set_interval(func, interval): # emulating JS's setInterval
    while True:
        if is_dark() and check_proximity():
            func()
            print('Sent notification!')
        else:
            print('Not yet.')
        time.sleep(interval)

set_interval(send_email_notification, 60)



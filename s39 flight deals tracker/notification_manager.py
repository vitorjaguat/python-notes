import os
import requests

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_notification(self, message):
        telegram_token = os.environ.get("JAGUAT_TESTBOT_TOKEN")
        chat_id = os.environ.get("JAGUAT_TESTBOT_CHATID")

        send_message_endpoint = 'https://api.telegram.org/bot' + telegram_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_message_endpoint)

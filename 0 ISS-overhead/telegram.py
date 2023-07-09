import requests
import time
import os
from geo_data import GeoData

class TelegramNotification:
    def __init__(self):
        self.BOT_TOKEN = os.environ.get('JAGUAT_TESTBOT_TOKEN')
        self.UPDATES_URL = f'https://api.telegram.org/bot{self.BOT_TOKEN}/getUpdates'
        self.get_updates()

    def get_updates(self):
        while True:
            response = requests.get(self.UPDATES_URL)
            data = response.json()

            # check if there are updates
            if 'result' in data and len(data['result']) > 0:
                updates = data['result']

                # process each update
                for update in updates:
                    # get update_id, chat_id and text message
                    update_id = update['update_id']
                    message_text = update['message']['text']
                    chat_id = update['message']['chat']['id']
                    print(message_text)

                    # compose response to user
                    if message_text == '/start':
                        response_text = 'Olá! Digite /cidade/NOME DA SUA CIDADE para checar se a ISS está passando por aí agora.'
                    elif message_text == '/check':
                        geo_data = GeoData()
                        is_close = geo_data.check_proximity()
                        if is_close:
                            response_text = 'Olhe para o céu! A ISS está passando pela sua cidade.'
                        else:
                            response_text = 'Não será possível avistar a ISS sobre a sua cidade neste momento.'
                    elif '/cidade/' in message_text:
                        geo_data = GeoData()
                        geo_data.city_name = message_text.replace('/cidade/', '')
                        self.send_response(chatid=chat_id, text=f'Obtendo dados para {geo_data.city_name}')
                        is_close = geo_data.check_proximity()
                        if is_close:
                            response_text = f'Olhe para o céu! A ISS está passando por {geo_data.city_name}.'
                        else:
                            response_text = f'Não será possível avistar a ISS sobre {geo_data.city_name} neste momento.'

                    else:
                        response_text = 'Desculpe, não consigo processar essa mensagem.'

                    #send response to user
                    self.send_response(chatid=chat_id, text=response_text)

                    # mark the update as processed
                    self.UPDATES_URL = f'https://api.telegram.org/bot{self.BOT_TOKEN}/getUpdates?offset={update_id+1}'

                # keep getting updates
                continue

            # wait 1s before getting new updates
            time.sleep(1)

    def send_response(self, chatid, text):
        response_url = f'https://api.telegram.org/bot{self.BOT_TOKEN}/sendMessage'
        params = {
            "chat_id": chatid,
            "text": text
        }
        requests.get(response_url, params=params)




            
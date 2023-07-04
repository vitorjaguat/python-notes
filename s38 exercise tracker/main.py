import requests
import os
import datetime as dt

# Transform user input in organized data using the natural language api from NutriotionIx

NUTRITIONIX_ID = os.environ.get('NUTRITIONIX_ID')
NUTRITIONIX_APIKEY = os.environ.get('NUTRITIONIX_APIKEY')
print(NUTRITIONIX_APIKEY)
print(NUTRITIONIX_ID)

nutr_headers = {
    "x-app-key": NUTRITIONIX_APIKEY,
    "x-app-id": NUTRITIONIX_ID,
    "Content-Type": "application/json"
}
nutr_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
nutr_body = {
    "query": input('Describe the exercise you did today. '),
    "gender": "male",
    "weight_kg": 72.5,
    "height_cm": 173.0,
    "age": 40
}

response = requests.post(url=nutr_endpoint, headers=nutr_headers, json=nutr_body)

exercise_data = response.json()
print(exercise_data)


# Inserting organized data in Google Sheets via SheetsAPI

sheety_endpoint = 'https://api.sheety.co/8f1bbcc5c1484f27433771ec3c8c8d59/myWorkouts/workouts'
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + os.environ.get('SHEETY_TOKEN')
}
sheety_body = {
    "workout": {
        "date": dt.date.today().strftime('%d/%m/%Y'),
        "time": dt.datetime.now().strftime('%H:%M:%S'),
        "exercise": exercise_data['exercises'][0]['name'].title(),
        "duration": exercise_data['exercises'][0]['duration_min'],
        "calories": exercise_data['exercises'][0]['nf_calories']
    }
}

response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_body)
# response.raise_for_status()run 34min
print(response.text)
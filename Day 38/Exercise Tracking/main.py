import requests
from datetime import datetime
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")

NT_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_WORKOUTS_ENDPOINT = os.getenv("SHEETY_WORKOUTS_ENDPOINT")

exercise_text = input("Tell me which exercise you did?: ")

headers = {"x-app-id": NUTRITIONIX_APP_ID, 'x-app-key': NUTRITIONIX_API_KEY}

parameters = {
    'query': exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(NT_EXERCISE_ENDPOINT,
                         json=parameters,
                         headers=headers)
response.raise_for_status()
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

bearer_headers = {"Authorization": f"Bearer {os.getenv('SHEETY_WORKOUTS_TOKEN')}"}

for exercise in result['exercises']:
  sheet_inputs = {
      "workout": {
          "date": today_date,
          "time": now_time,
          "exercise": exercise["name"].title(),
          "duration": exercise["duration_min"],
          "calories": exercise["nf_calories"]
      }
  }
  print(sheet_inputs)
  sheet_response = requests.post(SHEETY_WORKOUTS_ENDPOINT,
                                 json=sheet_inputs,
                                 headers=bearer_headers)

  print(sheet_response.text)

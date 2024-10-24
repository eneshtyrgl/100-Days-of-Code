import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
my_number = os.getenv("PHONE_NUMBER")
MY_LAT = float(os.getenv("LATITUDE")) # Your latitude
MY_LONG = float(os.getenv("LONGITUDE")) # Your longitude

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_=twilio_number, # YOUR TWILIO VIRTUAL NUMBER
        to=my_number #YOUR TWILIO VERIFIED REAL NUMBER
    )
    print(message.status)
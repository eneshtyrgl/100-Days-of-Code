import requests
from datetime import datetime
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv(".venv/.env")


MY_LAT = float(os.getenv("LATITUDE")) # Your latitude
MY_LONG = float(os.getenv("LONGITUDE")) # Your longitude



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

time_now = datetime.now().hour
print(f"Sunrise: {sunrise}\nSunset: {sunset}\nTime Now: {time_now}")
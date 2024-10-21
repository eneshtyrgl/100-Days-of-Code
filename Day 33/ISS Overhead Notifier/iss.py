import requests
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


MY_LAT = float(os.getenv("LATITUDE")) # Your latitude
MY_LONG = float(os.getenv("LONGITUDE")) # Your longitude


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

print(f"Latitude: {iss_latitude}\nLongitude: {iss_longitude}")

#Your position is within +5 or -5 degrees of the iss position.
if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    print("ISS is overhead")
else:
    print("ISS is not overhead")
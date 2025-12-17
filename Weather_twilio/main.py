import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_ACCOUNT_AUTH")
weather_id = os.getenv("WEATHER_API_APPID")

message_id=os.getenv("TWILIO_MESSAGE_ID")
#i am using free trail so my phone details
phone=os.getenv("PHONE")

if not account_sid:
    raise ValueError("TWILIO_ACCOUNT_SID not set")

print("Keys loaded successfully")


url="https://api.openweathermap.org/data/2.5/forecast?"

parm={
    "lat" :-6.175110,
    "lon" : -106.865036,
    "appid" : weather_id,
    "cnt" : 4,
}

response=requests.get(url=url,params=parm)
response.raise_for_status()

weather_info=response.json()



rain=False

for hour_data in weather_info["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code) <700:
        rain=True
print(weather_info["list"][0]["weather"][0]["id"])
if (rain):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid=message_id,
    body="High chance of rain dont forget to take your umbrella!!",
    to=phone
    )

    print(message.status)
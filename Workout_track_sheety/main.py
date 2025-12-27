import requests
from datetime import  datetime as dt   
from dotenv import load_dotenv
import os
import tkinter as tk

load_dotenv()

GENDER = "male"
WEIGHT_KG = 60
HEIGHT_CM = 170
AGE = 20

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_url=os.getenv("SHEETY_URL")

API_ID=os.getenv("API_ID")
API_KEY=os.getenv("API_KEY")

headers = {
    "Content-Type": "application/json",
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

text=input("Which exercise you did: ")
data = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url, headers=headers, json=data)
result = response.json()

today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")
print(now_time)



for exercise in result["exercises"]:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_url, json=sheet_data)
    print(sheet_response.text)

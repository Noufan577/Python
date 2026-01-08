import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

class DataManager:
    SHEETY_ENDPOINT = "https://api.sheety.co/a89ca8383f258c2d9b433d0556644b6e/flightPreferdDeals/prices"
    
    sheet_data={}
    def __init__(self):
        self.token = os.getenv("SHEETY_TOKEN")
        if not self.token:
            raise ValueError("SHEETY_TOKEN not found")

        self.headers = {
            "Authorization": f"Bearer {self.token}"
        }

    def get_update_data(self):
        response = requests.get(
            url=self.SHEETY_ENDPOINT,
            headers=self.headers
        )
        response.raise_for_status()

        self.sheet_data=response.json()["prices"]
        return self.sheet_data
    
    def update_destination_codes(self):
        for city in self.sheet_data:
            put_url = f"{self.SHEETY_ENDPOINT}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=put_url,
                json=new_data,
                headers=self.headers
            )
            
            print(response.text)
        

import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
class FlightSearch:


    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.token_expiures_at = 0

        if not self.api_key or not self.api_secret:
            raise ValueError("Amadeus API credentials missing")

        self.access_token = self.get_token()

    def get_token(self):
        if time.time() < self.token_expiures_at:
            return self.access_token
        data = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.post(
            url=self.TOKEN_ENDPOINT,
            data=data,
            headers=headers
        )
        response.raise_for_status()
        self.token_expiures_at = time.time() + response.json()["expires_in"]-60  # Refresh 1 minute before expiry

        return response.json()["access_token"]

    def get_code(self, cityname):
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        params = {
            "keyword": cityname,
            "max": 1
        }

        response = requests.get(
            url=self.CITY_SEARCH_ENDPOINT,
            headers=headers,
            params=params
        )

        response.raise_for_status()
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {cityname}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {cityname}.")
            return "Not Found"



        return code
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
  

        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                    "For details on status codes, check the API documentation:\n"
                    "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                    "-reference")
            print("Response body:", response.text)
            return None

        return response.json()




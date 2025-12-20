import requests                     
import datetime as dt                
from newsapi import NewsApiClient    
from twilio.rest import Client       
from dotenv import load_dotenv     
import os                            

load_dotenv()  

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API = "https://www.alphavantage.co/query?"

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_ACCOUNT_AUTH")
TWILIO_MESSAGE_ID = os.getenv("TWILIO_MESSAGE_ID")
PHONE = os.getenv("PHONE")

stock_par = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_API, params=stock_par)
response.raise_for_status()  

data = response.json()["Time Series (Daily)"]

dates = list(data.keys())
latest_day = dates[0]
previous_day = dates[1]

latest_close = float(data[latest_day]["4. close"])
previous_close = float(data[previous_day]["4. close"])

percent_change = ((latest_close - previous_close) / previous_close) * 100
percent_change = round(percent_change, 2)


if abs(percent_change) >= 0:

    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    news = newsapi.get_everything(
        q=COMPANY_NAME,
        language="en",
        sort_by="publishedAt",
        page_size=3
    )

    articles = news["articles"]
    #chnage message a sper your wish trail version of twilio has limitation in sending long and emojis with messages
    arrow = "+" if percent_change > 0 else "-"

    headlines = [a["title"] for a in articles]

    sms_body = (
        f"{STOCK} {arrow}{abs(percent_change)}% "
        f"{headlines[0][:40]}, "
        f"{headlines[1][:40]}, "
        f"{headlines[2][:40]}"
    )

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        messaging_service_sid=TWILIO_MESSAGE_ID,
        body=sms_body,
     
       to=PHONE
    )

    print("Message status:", message.status)

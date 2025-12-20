Stock News SMS Alert

A Python script that checks the daily stock price of Tesla (TSLA) and sends an SMS alert with the top 3 related news headlines if the price changes by 5% or more.

What it does

Fetches stock data from Alpha Vantage

Calculates percentage change between last two trading days

Gets top 3 news headlines from NewsAPI

Sends a short SMS using Twilio

Uses environment variables to keep API keys safe

Requirements
pip install requests newsapi-python twilio python-dotenv

Environment Variables (.env)
STOCK_API_KEY=your_alpha_vantage_key
NEWS_API_KEY=your_newsapi_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_ACCOUNT_AUTH=your_twilio_auth_token
TWILIO_MESSAGE_ID=your_twilio_messaging_service_sid
PHONE=your_verified_phone_number

Run
python main.py

Notes


.env file is ignored by Git for security

Stock symbol used: TSLA

APIs Used

Alpha Vantage

NewsAPI

Twilio
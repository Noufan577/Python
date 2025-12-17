🌦️ Weather Alert SMS (Python)

This is a simple Python script that checks the weather forecast using the OpenWeather API and sends an SMS alert using Twilio if rain is expected.

📂 Project Structure
project-folder/
│
└── main.py


(API keys are stored securely using environment variables.)

🛠️ Requirements

Python 3

Internet connection

Twilio account (trial or paid)

OpenWeather API key

📦 Python Libraries Used
pip install requests twilio python-dotenv

🔐 Environment Variables Setup

Create a .env file in the same folder as main.py and add:

TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_ACCOUNT_AUTH=your_twilio_auth_token
TWILIO_MESSAGE_ID=your_twilio_messaging_service_sid
PHONE=+91XXXXXXXXXX
WEATHER_API_APPID=your_openweather_api_key


⚠️ Do not upload .env to GitHub

▶️ How to Run the Project
python main.py

⚙️ How the Script Works

Loads API keys from environment variables

Fetches weather forecast using latitude and longitude

Checks upcoming weather conditions

If rain is detected, sends an SMS alert

Prints message status to console

☔ Rain Detection Logic
if condition_code < 700:
    rain = True


Weather codes below 700 indicate rain or storms.

📱 Example SMS Alert
High chance of rain dont forget to take your umbrella!!

⚠️ Important Notes

Twilio trial accounts can send SMS only to verified numbers

OpenWeather API keys may take 10–30 minutes to activate

Latitude and longitude can be changed in main.py

🧠 Learning Purpose

This project is created for learning API integration, environment variables, and SMS alerts using Python.
Amazon Price Tracker

This is a Python script that checks the price of an Amazon product and sends an email notification when the price drops below a target value.

The project uses requests and BeautifulSoup for scraping and SMTP for sending email alerts.

Features

Fetches product page HTML using HTTP requests

Uses a browser-based User-Agent header to avoid request blocking

Extracts product title and price using BeautifulSoup

Compares the price with a predefined target value

Sends an email notification when the price condition is met

Stores credentials securely using environment variables

Requirements

Python 3.x

Python Libraries
pip install requests beautifulsoup4 python-dotenv

Project Structure
Amazon_price_Tracker/
│
├── main.py
├── .env
├── README.md

Environment Variables

Create a .env file in the project directory:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
SMTP_ADDRESS=smtp.gmail.com


An app password must be used instead of the normal email password.

How It Works

The script sends an HTTP request to the product page with a browser User-Agent header

The HTML response is parsed using BeautifulSoup

The product title and price are extracted from the page

The extracted price is compared with the target price

If the condition is met, an email alert is sent

Notes

Using a valid browser User-Agent allows the script to retrieve the price data successfully in many cases.
However, Amazon may still restrict access depending on location, IP, or request frequency.

How to Run
python main.py

Disclaimer

This project is intended for educational purposes only.
Scraping websites may violate their terms of service.
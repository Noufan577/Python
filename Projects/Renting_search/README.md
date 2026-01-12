Zillow Data Scraper to Google Form

This project scrapes property listings from a Zillow-like website and automatically submits the collected data into a Google Form using Selenium.

What this project does

Fetches property listings from a Zillow clone website

Extracts:

Property address

Monthly price

Property link

Automatically fills and submits a Google Form for each property

Technologies Used

Python

Requests

BeautifulSoup

Selenium (Chrome WebDriver)

Project Flow

Send an HTTP request to the Zillow clone website

Parse the HTML using BeautifulSoup

Collect addresses, prices, and links

Open Google Form using Selenium

Fill the form fields and submit data automatically

Requirements

Make sure you have the following installed:

Python 3.x

Google Chrome

ChromeDriver (compatible with your Chrome version)

Install required Python libraries:

pip install requests beautifulsoup4 selenium

How to Run

Clone this repository

Update the Google Form link in the script

Make sure the form input XPaths match your Google Form

Run the script:

python main.py

Notes

time.sleep() is used to wait for the form to load (can be replaced with WebDriverWait)

Google Form structure may change, so XPaths might need updates

This project is for learning and automation practice purposes

Possible Improvements

Use WebDriverWait instead of sleep

Add exception handling

Store scraped data in CSV before submission

Make form field selection more dynamic

Disclaimer

This project is created for educational purposes only.
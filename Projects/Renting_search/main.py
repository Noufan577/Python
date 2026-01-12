# Scrapes property data (address, price, link) from Zillow clone using BeautifulSoup
# and submits the collected data to a Google Form using Selenium

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Headers added to avoid request blocking
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9",
}

# Google Form link where data will be submitted
gform_link = "GIVE YOUR GOOGLE FORM LINK HERE"

# Fetch Zillow clone page
response = requests.get(
    url="https://appbrewery.github.io/Zillow-Clone/",
    headers=header
)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract property listing links
links = [link.get("href") for link in soup.find_all(
    name="a",
    class_="property-card-link"
)]

# Extract property addresses
all_address = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [
    address.get_text().replace(" | ", " ").strip()
    for address in all_address
]

# Extract property prices and clean the text
all_price = soup.select(".PropertyCardWrapper span")
all_prices = [
    price.get_text().replace("/mo", "").split("+")[0]
    for price in all_price
    if "$" in price.text
]

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open Google Form
driver.get(gform_link)

# Loop through all properties and submit form for each
for n in range(len(links)):

    driver.get(gform_link)
    time.sleep(2)

    # Locate input fields in the form
    address = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    price = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )
    link = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    )

    submit_button = driver.find_element(
        by=By.XPATH,
        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'
    )

    # Fill form inputs
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(links[n])

    # Submit the form
    submit_button.click()

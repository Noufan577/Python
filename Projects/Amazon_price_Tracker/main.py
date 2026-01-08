import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")

TARGET_PRICE = "SET_YOUR_TARGET_PRICE_HERE"  # e.g., 1500.00
URL = "YOUR_PRODUCT_LINK_HERE"


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9",
}


response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span",class_="a-offscreen").getText()
price_float = float(
    price.replace("₹", "").replace(",", "").strip()
)

title = soup.find(id="productTitle").get_text().strip()

print(price_float)
print(title)

if price_float <= TARGET_PRICE:
    message = f"{title} is now ${price_float}!"

    try:
        with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            result = connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs="TO_EMAIL_ADDRESS",
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )

        if result == {}:
            print(" Email sent successfully")
        else:
            print(" Email failed:", result)

    except Exception as e:
        print(" Error sending email:", e)
else:
    print("Price is still higher than target")

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

}
date=input("Enter the date you want to find top songs to in YYYY-MM-DD format: ")

URL="https://www.billboard.com/charts/hot-100/"+date

response=requests.get(url=URL,headers=headers)

soup=BeautifulSoup(response.text,"html.parser")

Songs=[i.getText().strip() for i in soup.select("li ul li h3")]





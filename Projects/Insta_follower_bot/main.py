from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
load_dotenv()
import time

import os


SIMILAR_ACCOUNT = "cheff"
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASS")


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        wait = WebDriverWait(self.driver, 5)

        # Wait for username field
        username = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )

        password = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        # Handle "Save Login Info" popup
        try:
            not_now = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[contains(text(),'Not now')]")
                )
            )
            not_now.click()
        except:
            pass  # popup may not appear

        # Handle "Turn on Notifications" popup
        try:
            not_now2 = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(),'Not Now')]")
                )
            )
            not_now2.click()
        except:
            pass


        



    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium.common.exceptions import NoSuchElementException, TimeoutException

ACCOUNT_EMAIL = "noufan123@gmail.com"
ACCOUNT_PASSWORD = "noufan@123"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Open site
driver.get(GYM_URL)

def login():
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(EC.visibility_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = wait.until(EC.visibility_of_element_located((By.ID, "password-input")))
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
    submit_btn.click()

    # Wait for schedule page
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def book_class(booking_button):
    booking_button.click()
    wait.until(lambda d: booking_button.text == "Booked")

retry(login, description="login")

day_classes = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group-']")


booked_count = 0
waitlist_count = 0
already_booked_count = 0

processed_classes = []


for day in day_classes:

    dayy = day.find_element(By.TAG_NAME, "h2").text


    if "Tue" in dayy or "Thu" in dayy:
        classes_on_tues = day.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

        for cls in classes_on_tues:
            time_text = cls.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
            if "6:00" in time_text:
                class_name = cls.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
                book_btn = cls.find_element(By.CSS_SELECTOR, "div div button[id^='book-button-']")
                book_btn.click()

                class_info = f"{class_name} on {dayy}"
                
                
                if book_btn.text == "Booked":
                    print(f"✓ Already booked: {class_name} on {dayy}")
                    already_booked_count += 1
                    processed_classes.append(f"[Booked] {class_info}")
                elif book_btn.text == "Waitlisted":
                    print(f"✓ Already on waitlist: {class_name} on {dayy}")
                    already_booked_count += 1
                    processed_classes.append(f"[Waitlisted] {class_info}")
                elif book_btn.text == "Book Class":
                    book_btn.click()
                    print(f"✓ Successfully booked: {class_name} on {dayy}")
                    booked_count += 1
                    processed_classes.append(f"[New Booking] {class_info}")
                    time.sleep(0.5)
                elif book_btn.text == "Join Waitlist":
                    book_btn.click()
                    print(f"✓ Joined waitlist for: {class_name} on {dayy}")
                    waitlist_count += 1
                    processed_classes.append(f"[New Waitlist] {class_info}")
                    time.sleep(0.5)
                break
total_booked = booked_count + waitlist_count + already_booked_count
my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

# Wait for My Bookings page to load
wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

# Find ALL booking cards (both confirmed and waitlist)
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

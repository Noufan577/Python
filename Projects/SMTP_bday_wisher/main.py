import random
import datetime as dt
import smtplib
import pandas as pd
import os

my_mail="noufankufi@gmail.com"
password="your_pass"
fp = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
month = now.month
day = now.day

# Filter today's birthdays
req = fp[(fp["month"] == month) & (fp["day"] == day)]

if not req.empty:
    for _, row in req.iterrows():

        name = row["name"]
        email = row["email"]

        folder = r"C:\Users\noufa\OneDrive\Desktop\ml\python\Python\SMTP_bday_wisher\letter_templates"
        letters = [f for f in os.listdir(folder) if f.endswith(".txt")]
        letter_file = random.choice(letters)

        with open(os.path.join(folder, letter_file), "r") as file:
            letter_content = file.read()

        final_letter = letter_content.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com",587) as conn:
            conn.starttls()
            conn.login(my_mail,password)
            conn.sendmail(from_addr=my_mail,to_addrs=email,
                          msg=final_letter)
            

else:
    print("No birthdays today")

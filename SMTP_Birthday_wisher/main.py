from smtplib import SMTP



with SMTP("smtp.google.com",587) as conn:
    conn.starttls()
    conn.login("noufankufi@gmail.com","password")
    conn.sendmail(
    from_addr="noufankufi@gmail.com",
    to_addrs="noufann96@gmail.com@gmail.com",
    msg="Subject:Hello!\n\nThis is a test email."
)


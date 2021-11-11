import requests
from bs4 import BeautifulSoup
import smtplib

URL = "http://gog.ba/shop/laptopi/830-lenovo-l5-15imh05-20550.html"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

title = soup.find(itemprop="name").get_text().strip()
price = soup.find(id="our_price_display").get_text().strip()[0]

print(title)
print(price)

BUY_PRICE = 2000
price_as_float = float(price)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587 
GMAIL_USERNAME = 'your.email@gmail.com' 
GMAIL_PASSWORD = 'epicpassword69'  

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
        connection.starttls()
        result = connection.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        connection.sendmail(
            from_addr=GMAIL_USERNAME,
            to_addrs=GMAIL_USERNAME,
            msg=f"Subject:Laptop on sale!\n\n{message}\n{URL}"
        )
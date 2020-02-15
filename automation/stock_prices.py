from bs4 import BeautifulSoup
import requests
import smtplib
from time import sleep
from privacy import username, pw, receiver


class Agent:
    def check_price(self):
        global aktueller_preis

        url = "https://www.boerse.de/aktien/Abbott-Aktie/US0028241000"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")

        aktueller_preis = soup.find("span", itemprop="price").get_text()
        aktueller_preis = float(aktueller_preis.replace(",", "."))

        print(type(aktueller_preis))

    def send_mail(self):
        server = smtplib.SMTP("smtp.gmail.com", port=587)
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()

        server.login(username, pw)
        print("login to Email worked")

        subject = "Ihre Abbott-Aktie ist gestiegen!"

        message = f"Subject:{subject}\n\nDer neue Preis ist {aktueller_preis}Euro"
        server.sendmail(username, receiver, message)
        server.quit()


Agent().check_price()
if aktueller_preis > 83.00:
    Agent().send_mail()

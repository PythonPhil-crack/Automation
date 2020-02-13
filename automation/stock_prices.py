from selenium import webdriver
import smtplib
from time import sleep
from privacy import username, pw, receiver


class Agent:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def check_price(self):

        self.driver.get(
            "https://www.google.com/search?q=abott+stcok&oq=abott+stcok&aqs=chrome..69i57j0l7.5354j1j8&sourceid=chrome&ie=UTF-8")
        sleep(2)

        global aktueller_preis
        aktueller_preis = self.driver.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/g-card-section[1]/div/g-card-section/span[1]/span/span[1]").text
        aktueller_preis = float(aktueller_preis[0]+aktueller_preis[1])
        print(aktueller_preis)

        self.driver.quit()

    def send_mail(self):
        self.driver.quit()
        server = smtplib.SMTP("mail.gmx.net", port=587)
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()

        server.login(username, pw)
        print("login to Email worked")

        subject = "Ihre Aktie ist gestiegen!"

        message = f"Betreff: {subject}\n\n Der neue Preis ist {aktueller_preis}$"
        server.sendmail(username, receiver, message)
        server.quit()


Agent().check_price()
Agent().send_mail()

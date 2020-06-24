import requests
from bs4 import BeautifulSoup
import string
import time

URL = 'https://www.flipkart.com/samsung-galaxy-a80-ghost-white-128-gb/p/itmfghz3ckgjgp2b?pid=MOBFGHZ2CC2PW5TJ&cmpid=product.share.pp'

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}


class Del:
    def __init__(self, keep=string.digits):
        self.comp = dict((ord(c), c) for c in keep)

    def __getitem__(self, k):
        return self.comp.get(k)


def sendEmail():
    emailBody = {
        "to": "akx.sonu@gmail.com",
        "subject": "Samsung A80 Price drop",
        "msg": "Price fall below Rs.25000. Click here : "+URL
    }
    emailURL = 'https://us-central1-sghindi-744ab.cloudfunctions.net/userFunction/v1/user/testmail'
    requests.post(emailURL, data=emailBody)

    emailBody = {
        "to": "pratidhi.com",
        "subject": "Samsung A80 Price drop",
        "msg": "Price fall below Rs.25000. Click here : "+URL
    }
    emailURL = 'https://us-central1-sghindi-744ab.cloudfunctions.net/userFunction/v1/user/testmail'
    requests.post(emailURL, data=emailBody)


def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).text
    buyButton = soup.find(
        "button", {"class": "_2AkmmA _2Npkh4 _2kuvG8 _7UHT_c"})

    DD = Del()
    p = price.translate(DD)

    if(float(p) < 25000 and buyButton != None):
        print(p)
        print('price dropped.. sending email')
        sendEmail()
    print(p)
    # sendEmail()


while(True):
    checkPrice()
    time.sleep(120)

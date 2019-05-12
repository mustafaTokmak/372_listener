import requests
import time
from bs4 import BeautifulSoup
from telegram_bot import telegram_bot_sendtext
import schedule


def get_webpage():
    url = "http://biluser:3722019bilsummer@pages.cpsc.ucalgary.ca/~ozyert/372/372.html"
    response = requests.get(url)
    source = BeautifulSoup(response.content, "lxml")
    announcements = str(source.find(attrs={"class": "col-sm-12 col-md-7 bio"}))
    return announcements


def get_oldpage():
    # refresh_page()
    data = ""
    try:
        with open('page.html', 'r') as f:
            data = f.read()
    except:
        return data
    if(data == ""):
        return data
    source = BeautifulSoup(data, "lxml")
    announcements = str(source.find(attrs={"class": "col-sm-12 col-md-7 bio"}))
    return announcements


def refresh_page():
    url = "http://biluser:3722019bilsummer@pages.cpsc.ucalgary.ca/~ozyert/372/372.html"
    response = requests.get(url)
    source = BeautifulSoup(response.content, "lxml")
    data = str(source)
    with open('page.html', 'w') as f:
        f.write(data)


def get_message():
    url = "http://biluser:3722019bilsummer@pages.cpsc.ucalgary.ca/~ozyert/372/372.html"
    response = requests.get(url)
    source = BeautifulSoup(response.content, "lxml")
    abc = source.find(attrs={"class": "col-sm-12 col-md-7 bio"})
    l = []
    for child in abc.descendants:
        if(child != "\n"):
            l.append(child)
    return l[-1]


def compare_and_send():
    oldpage = get_oldpage()
    webpage = get_webpage()
    if(oldpage == ""):
        message = "error in oldpage"
        telegram_bot_sendtext(message)
    if(webpage == ""):
        message = "error in webpage"
        telegram_bot_sendtext(message)
    if(webpage != oldpage):
        print("run")
        message = "New Note in 372 Page: \n\n"
        try:
            message += get_message()
        except:
            message += "message is emtpy CHECK Website"
        print(telegram_bot_sendtext(message))
        refresh_page()


schedule.every().hour.do(compare_and_send)
while True:
    schedule.run_pending()
    time.sleep(1)

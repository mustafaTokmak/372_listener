import requests
import time
from bs4 import BeautifulSoup
from telegram_bot import telegram_bot_sendtext, send_all_user
import schedule


def get_webpage():
    url = "http://biluser:3722019bilsummer@pages.cpsc.ucalgary.ca/~ozyert/372/372.html"
    try:
        response = requests.get(url)
        text = response.text[:100]
        source = BeautifulSoup(response.content, "lxml")
        announcements = str(source.find(
            attrs={"class": "col-sm-12 col-md-7 bio"}))
    except:
        announcements = ""
    return str(announcements)


def get_oldpage():
    # refresh_page()
    data = ""
    try:
        with open('page.html', 'r') as f:
            data = f.read()
        source = BeautifulSoup(data, "lxml")
        announcements = str(source.find(
            attrs={"class": "col-sm-12 col-md-7 bio"}))
        return str(announcements)
    except:
        return data
    if(data == ""):
        return data


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
    t = time.strftime("%Y-%d-%m %H:%M:%S", time.gmtime())
    print(t)
    oldpage = get_oldpage()
    webpage = get_webpage()

    if(oldpage == ""):
        message = "error in oldpage"
        send_all_user(message)
    if(webpage == ""):
        message = "error in webpage"
        send_all_user(message)
    if(webpage != oldpage):
        print("run")
        message = "New Note in 372 Page: \n\n"
        try:
            message += get_message()
        except:
            message += "message is emtpy CHECK Website"
        refresh_page()


def call():
    t = time.strftime("%Y-%d-%m %H:%M:%S", time.gmtime())
    send_all_user(str(t))


#schedule.every(5).seconds.do(compare_and_send)
schedule.every().hour.do(compare_and_send)
while True:
    schedule.run_pending()
    time.sleep(1)

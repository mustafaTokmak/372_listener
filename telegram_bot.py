import time
import schedule
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '840440318:AAHsHQIkblBMJUsSzE5zMe0CVT0vUdsra5c'
    bot_chatID = '198917570'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


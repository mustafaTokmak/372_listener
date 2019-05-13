import time
import schedule
import requests
bil_372_listener = '840440318:AAHsHQIkblBMJUsSzE5zMe0CVT0vUdsra5c'
mtokmak_playground = '808638931:AAHeG2DXep1qzo-y2U6AhvIFncooUuAyY9w'
bot_token = bil_372_listener

def telegram_bot_sendtext(bot_message):
    bot_chatID = '198917570'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def send_all_user(bot_message):
    get_updates_url = "http://api.telegram.org/bot"+bot_token+"/getUpdates"
    response = requests.get(get_updates_url)
    result_arr = response.json()["result"]
    chat_ids =[]
    for result in result_arr:
        chat_id = str(result["message"]["from"]["id"])
        if (not (chat_id in chat_ids)):
            chat_ids.append(chat_id)
    print(chat_ids)
    for bot_chatID in chat_ids:
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        


#telegram_bot_sendtext("sssss")

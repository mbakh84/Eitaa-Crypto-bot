from time import sleep
import requests

def send_message(message:str):
    
    TOKEN = "bot289853:8123ecc3-5827-4c76-9f8a-3ba47a7eeb7c"
    CHANNEL_username = "Crypto_Live"
    url = f"https://eitaayar.ir/api/{TOKEN}/sendMessage"

    try_counter = 0
    while(try_counter < 10):
        params = {
            'chat_id': CHANNEL_username,
            'text': message,
        }

        response = requests.post(url, params=params)
        if response.status_code == 200 and response.json()['ok'] == True:
            return 1
        try_counter += 1
        sleep(3000)

        if(try_counter == 10):
            return 0

#for warning to very high changes
# def send_message(message:str, notification:bool):
    
#     TOKEN = "bot289853:8123ecc3-5827-4c76-9f8a-3ba47a7eeb7c"
#     CHANNEL_username = "Crypto_Live"
#     url = f"https://eitaayar.ir/api/{TOKEN}/sendMessage"

#     try_counter = 0
#     while(try_counter < 10):
#         params = {
#             'chat_id': CHANNEL_username,
#             'text': message,
#             'notification_disable': notification
#         }

#         response = requests.post(url, params=params)
#         if response.status_code == 200 and response.json()['ok'] == True:
#             return 1
#         try_counter += 1
#         sleep(3000)

#         if(try_counter == 10):
#             return 0

def issue_message():
    TOKEN = "bot289853:8123ecc3-5827-4c76-9f8a-3ba47a7eeb7c"
    CHANNEL_username = "Crypto_Live"
    url = f"https://eitaayar.ir/api/{TOKEN}/sendMessage"

    params = {
            'chat_id': CHANNEL_username,
            'text': 'we got some technical issues!'
        }

    response = requests.post(url, params=params)
    if response.status_code == 200 and response.json()['ok'] == True:
        return 1
    return 0
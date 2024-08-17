from time import sleep
import requests

def send_message(message:str):
    
    TOKEN = "***"
    CHANNEL_username = "Crypto_Live"
    url = f"https://eitaayar.ir/api/{TOKEN}/sendMessage"

    params = {
        'chat_id': CHANNEL_username,
        'text': message,
    }

    try_counter = 0

    while(try_counter < 10):
        response = requests.post(url, params=params)
        if response.status_code == 200 and response.json()['ok'] == True:
            return 1
        try_counter += 1
        sleep(3)


    if(try_counter == 10):
        return 0

def issue_message():
    TOKEN = "***"
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

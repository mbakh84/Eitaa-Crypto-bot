from coin_class import coin
from crypto_API_connection import connect_to_API,request_for_price
from eita_API_connection import send_message,issue_message
from time import sleep

Key = '7f0c0909-32ae-466d-ad91-e58b46a31508'
url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

session = connect_to_API(Key, url)

coin_list = [
    coin(0, "Bitcoin", "BTC"),
    coin(0, "Ethereum", "ETH"),
    coin(0, "BNB", "BNB"),
    coin(0, "Solana", "SOL"),
    coin(0, "XRP", "XRP")
]

while(1):
    try:
        send_message('⚠️⚠️⚠️')
        for crypto in coin_list:
            crypto.price = request_for_price(crypto, session, url)
            send_message(f'{crypto.name} : {crypto.price}')
        sleep(300)
        
    
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        issue_message()
        break


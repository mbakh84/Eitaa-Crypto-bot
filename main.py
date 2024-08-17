from coin_class import coin
from crypto_API_connection import connect_to_API,request_for_data
from eita_API_connection import send_message,issue_message
from time import sleep

Key = '7f0c0909-32ae-466d-ad91-e58b46a31508'
auth_url = 'https://pro-api.coinmarketcap.com'
price_url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

session = connect_to_API(Key, auth_url)

coin_list = [
    coin(0, "Bitcoin", "BTC", 0),
    coin(0, "Ethereum", "ETH", 0),
    coin(0, "BNB", "BNB", 0),
    coin(0, "Solana", "SOL", 0),
    coin(0, "XRP", "XRP", 0)
]

while(1):
    try:
        message = '⚠️⚠️⚠️\n'
        for crypto in coin_list:
            crypto.price = request_for_data(crypto, session, price_url)
            message += f'{crypto.symbol} : {crypto.price}\n'
        if send_message(message) == 0:
            raise RuntimeError
        sleep(300)
        
    except:
        issue_message()
        break


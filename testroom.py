
from coin_class import coin
from crypto_API_connection import connect_to_API
import json

Key = '7f0c0909-32ae-466d-ad91-e58b46a31508'
url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

session = connect_to_API(Key, url)

BTC = coin(0, "Bitcoin", "BTC")
ETH = coin(0, "Ethereum", "ETH")
BNB = coin(0, "BNB", "BNB")
SOL = coin(0, "Solana", "SOL")
XRP = coin(0, "XRP", "XRP")
# DOGE = coin(0, "DOGE", "Dogecoin")

coin_list = [BTC, ETH, BNB, SOL, XRP]

#sending request for API
try:
    for crypto in coin_list:
        parameters = {
        'amount':'1',
        'symbol': crypto.symbol,
        }
        response = session.get(url, params=parameters)
        data = response.json()['data']
        print(data)
#   print(len(data))
#   for i in data:
#     print(f"{i['name']}      {i['quote']['USD']['price']}")
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
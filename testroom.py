from requests import Session
from coin_class import coin

Key = '7f0c0909-32ae-466d-ad91-e58b46a31508'
url = 'https://pro-api.coinmarketcap.com'

url = url
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': Key,
}
session = Session()
session.headers.update(headers)

parameters = {
    'amount':'1',
    'symbol': 'BTC',
    }
response = session.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/latest', params=parameters)
raw_data = response.json()
print(response)

# parameters = {
#     'symbol': "BTC",
#     }
# change_url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/ohlcv/latest'

# response = session.get(change_url, params=parameters)
# print(response.status_code)
# raw_data = response.json()["data"]
# print(raw_data)

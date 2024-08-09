from requests import Session
from coin_class import coin

Key = '7f0c0909-32ae-466d-ad91-e58b46a31508'
url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

url = url
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': Key,
}
session = Session()
session.headers.update(headers)

parameters = {
    'amount':'1',
    'symbol': "BTC",
    }
response = session.get(url, params=parameters)
raw_data = response.json()['data']
for item in raw_data:
    print(item)
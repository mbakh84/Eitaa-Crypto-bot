from requests import Session
from coin_class import coin

def connect_to_API(Key:str,url:str):
    url = url
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': Key,
    }
    session = Session()
    session.headers.update(headers)
    return session

def request_for_data(crypto:coin, session:Session, price_url:str):
    parameters = {
        'amount':'1',
        'symbol': crypto.symbol,
        }
    response = session.get(price_url, params=parameters)
    raw_data = response.json()['data']
    for item in raw_data:
        if item['name'] == crypto.name:
            return (round(float(item['quote']['USD']['price']), 3))
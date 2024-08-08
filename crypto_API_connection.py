from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
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

def request_for_price(crypto:coin, session:Session, url:str):
    parameters = {
        'amount':'1',
        'symbol': crypto.symbol,
        }
    response = session.get(url, params=parameters)
    raw_data = response.json()['data']
    for item in raw_data:
        if item['name'] == crypto.name:
            return float(item['quote']['USD']['price'])
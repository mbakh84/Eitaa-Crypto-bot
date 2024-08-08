from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

def connect_to_API(Key:str,url:str):
    url = url
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': Key,
    }
    session = Session()
    session.headers.update(headers)
    return session
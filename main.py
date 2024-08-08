from coin_class import coin
from crypto_API_connection import connect_to_API,request_for_price

Key = '7f0c0909-32ae-466d-ad91-e58b46a31508'
url = 'https://pro-api.coinmarketcap.com/v2/tools/price-conversion'

session = connect_to_API(Key, url)

BTC = coin(0, "Bitcoin", "BTC")
ETH = coin(0, "Ethereum", "ETH")
BNB = coin(0, "BNB", "BNB")
SOL = coin(0, "Solana", "SOL")
XRP = coin(0, "XRP", "XRP")

coin_list = [BTC, ETH, BNB, SOL, XRP]

try:
    for crypto in coin_list:
        crypto.price = request_for_price(crypto, session, url)
        print(f'{crypto.name}    {crypto.price}')
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# def send_message(message):
#     try_counter = 0
#     while(try_counter < 10):
#         url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#         params = {
#             'chat_id': CHANNEL_ID,
#             'text': message
#         }
#         response = requests.post(url, params=params)
#         if response.status_code == 200:
#             break
#         try_counter += 1
#         if(try_counter == 10):
#             exit(0)


# driver = webdriver.Chrome()
# #start webdriver

# count_of_cryptos = 8 #count of cryptos which we extract thier datas

# crypto_ID = {78:"BTC",7841:"ETH",6746:"USDT",8665:"SOL",2649:"BNB",80:"XRP",6739:"USDC",3498:"DOGE"}
# #in this type of datas, we have access to a data with an specific ID; this dictionary save the IDs

# while(1):
#     price_list = {"BTC":0,"ETH":0,"USDT":0,"SOL":0,"BNB":0,"XRP":0,"USDC":0,"DOGE":0} #this dictionary will save the extracted price
#     for i in range(count_of_cryptos):
#         driver.get(f"https://fcsapi.com/api-v3/crypto/latest?id={list(crypto_ID.keys())[i]}&access_key=8CNLQ22cKi2m2Evhq96xs")
#         pre_element = driver.find_element(By.XPATH,"//pre")
        
#         pre_text = pre_element.text
#         pre_text = pre_text.split('"c":"')
#         pre_text.pop(0)
#         raw_price = ""
#         for j in pre_text[0]:
#             if j == '"':
#                 break
#             else:
#                 raw_price += j

#         price_list[list(price_list.keys())[i]] = float(raw_price)
#         sleep(30)
#     print(price_list)
#     message = f"BTC : {price_list["BTC"]}\nETH : {price_list["ETH"]}\nUSDT : {price_list["USDT"]}\nSOL : {price_list["SOL"]}\nBNB : {price_list["BNB"]}\nXRP : {price_list["XRP"]}\nUSDC : {price_list["USDC"]}\nDOGE : {price_list["DOGE"]}"
#     send_message(message)
    
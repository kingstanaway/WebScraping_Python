import requests
from bs4 import BeautifulSoup as bs

# BITCOIN
url2 = "https://www.coindesk.com/price/bitcoin"

r = requests.get(url2)

soup2 = bs(r.content, "html.parser")
btc_price = soup2.find("div", {"class":"price-large"})

print("BTC: " + btc_price.text)

# ETHEREUM
url = "https://www.coindesk.com/price/ethereum"

r = requests.get(url)

soup = bs(r.content, "html.parser")
eth_price = soup.find("div", {"class":"price-large"})

print("ETH: " + eth_price.text)

# CARDANO
url3 = "https://www.coindesk.com/price/cardano"

r = requests.get(url3)

soup3 = bs(r.content, "html.parser")
ada_price = soup3.find("div", {"class":"price-large"})

print("ADA: " + ada_price.text)

# RIPPLE
url4 = "https://www.coindesk.com/price/xrp"

r = requests.get(url4)

soup4 = bs(r.content, "html.parser")
xrp_price = soup4.find("div", {"class":"price-large"})

print("XRP: " + xrp_price.text)

# DOGE
url5 = "https://www.coindesk.com/price/dogecoin"

r = requests.get(url5)

soup5 = bs(r.content, "html.parser")
doge_price = soup5.find("div", {"class":"price-large"})

print("DOGE: " + doge_price.text)
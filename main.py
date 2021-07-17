import requests
from bs4 import BeautifulSoup
import time
import requests
import datetime

url_usd_rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

full_page = requests.get(url_usd_rub, headers=headers)


soup = BeautifulSoup(full_page.content, 'html.parser')

convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
usd = convert[0].text.replace(',', '.')


url = 'https://yobit.net/api/3/ticker/btc_usd'
r = requests.get(url)
response = r.json()

sell_price = response["btc_usd"]["sell"]
priceUSD = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price USD {sell_price:.2f}'

priceRUB = float(sell_price) * float(usd)
priceRUB = f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price RUB {priceRUB:.2f}'
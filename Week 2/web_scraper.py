import requests #module to make http/https request 
import html5lib #small parser package for html5
from bs4 import BeautifulSoup

amazon_url= "https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_3?keywords=laptop&qid=1579030370&sr=8-3"

agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"

agent_header= {
	"User-Agent" : agent
}

amazon_page = requests.get(amazon_url, headers=agent_header)

soup = BeautifulSoup(amazon_page.content,"html5lib")

price_span = str(soup.find(id="priceblock_ourprice"))
print(price_span)
price = ''
for char in price_span:
	if char.isdigit() is True:
		price += char
	if char == ".":
		price += char 
print(price)
price = float(price)
max_price = 800
if price <= max_price:
	print("yo you can buy it now")

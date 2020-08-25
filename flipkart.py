import urllib.request
import urllib.parse
import urllib.error
import re
from bs4 import BeautifulSoup
import ssl

url = 'https://www.flipkart.com/harry-potter-philosopher-s-stone/p/itmfc5dhvrkh5jqp?pid=9781408855652'

# ignore ssl certifcate errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# print(soup)
# fetchImage
image = soup.findAll("div", {"class": "_2_AcLJ"})
image = image[0].get('style')
image = re.findall('url\(([^)]+)\)', image)
image = image[0]

# fetchTitle
title = soup.findAll("span", {"class": "_35KyD6"})
title = title[0].text
print(title)

# fetchRating
rating = soup("div", {"class": "hGSR34"})
rating = rating[0].text
print(rating)

# fetchImage
price = soup("div", {"class": "_3qQ9m1"})
price = price[0].text
print(price[1:])

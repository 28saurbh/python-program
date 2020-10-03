# Python program to scrape website
# and save quotes from website
import requests
import time
from bs4 import BeautifulSoup
import csv

URL = "https://www.flipkart.com/apple-iphone-xs-space-grey-64-gb/p/itmf944ees7rprte?pid=MOBF944E5FTGHNCR&lid=LSTMOBF944E5FTGHNCRAH33S3&marketplace=FLIPKART&srno=s_1_2&otracker=search&otracker1=search&fm=SEARCH&iid=3bdbc1fe-fb28-4b87-b9dd-5cfa9bca72f7.MOBF944E5FTGHNCR.SEARCH&ppt=sp&ppn=sp&ssid=dh4th365ow0000001584871616021&qH=0b3f45b266a97d70"
source2 = "https://www.amazon.in/Apple-iPhone-Xs-Max-64GB/dp/B07J3CJM4N/ref=sr_1_4?dchild=1&keywords=Apple+iPhone+XS+%28Space+Grey%2C+64+GB%29&qid=1584873760&s=electronics&sr=1-4"
wait_imp = 10
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

print("Connecting to Flipkart")
# wd.implicitly_wait(wait_imp)
f_price = soup.find(class_="_1uv9Cb")
pr_name = soup.find(class_="_9E25nV")
product = pr_name.text
r_price = f_price.text
print(product)
print(r_price)
print(" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)

print("Connecting to Amazon")
amazon = requests.get(source2)
soup1 = BeautifulSoup(amazon.content, 'html5lib')
# a_price = wd.find_element_by_id("priceblock_ourprice")
a_price = soup1.find(class_="a-size-medium a-color-price priceBlockBuyingPriceString")
print(a_price)
print(" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)

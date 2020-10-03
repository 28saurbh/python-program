# importing modules
import requests
from bs4 import BeautifulSoup
import lxml

# URL for scrapping data
url = 'https://www.worldometers.info/coronavirus/'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

# print(soup)
# main = soup.find(class_='content-inner')
# print(main.prettify())
name = soup.find(id='maincounter-wrap')
# case = name.find('h1')
print(name.text)
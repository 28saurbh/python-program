import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.skymetweather.com/forecast/weather/india/madhya%20pradesh/narsinghpur/gadarwara/extended-forecast')
soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find(id='seveldayforecastExtended')
print(content)
temp = soup.find_all(class_='bktibx')
print(temp[1])






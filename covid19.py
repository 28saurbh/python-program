import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.worldometers.info/coronavirus/country/india/')
soup = BeautifulSoup(page.content, 'html.parser')
main = soup.find_all(class_='col-md-8')
number = [data.find(class_='maincounter-number').get_text() for data in main]
print(number)
name = 'Coronavirus Cases:'


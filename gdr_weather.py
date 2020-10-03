from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


url = 'https://www.theweathernetwork.com/in/weather/madhya-pradesh/gadarwara'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

print(soup.prettify())

block = soup.find(id='main_content')
# print(block)
city = block.find(class_='wx-info_card')
update = block.find(class_='obs-area')

print(city.text)
# print(update)

# d = webdriver.Chrome()
d = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

d.get('https://www.theweathernetwork.com/in/weather/madhya-pradesh/gadarwara')
cel = d.find_element_by_class_name('unitwrap')
game_time = d.find_element_by_class_name('temp')
print(game_time.text, cel.text)
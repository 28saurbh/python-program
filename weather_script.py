import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.X2DGvGgzZPY')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
# print(items[0])

# print(items[0].find(class_='period-name').get_text())
# print(items[0].find(class_='short-desc').get_text())
# print(items[0].find(class_='temp').get_text())

period_name = [item.find(class_='period-name').get_text() for item in items]
short_desc = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]

# print(period_name, short_desc, temperatures)

weather_stuff = pd.DataFrame(
    {
        'period': period_name,
        'short_desc': short_desc,
        'temperatures': temperatures
    })
print(weather_stuff)
weather_stuff.to_csv('weather.csv')
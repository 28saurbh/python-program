import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.flipkart.com/search?q=inphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='container')
phone = week.find_all(class_='_3wU53n')

print(BeautifulSoup.prettify(phone[0]))








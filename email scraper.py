import re

text = 'This is main Email 28saurbh@gmail.com second one is 2809sourabh@gmail.com and outllok account is ' \
       'garewal28@outlook.com '

pattern = re.compile("[A-Za-z0-9\_\-]+\@[A-Za-z0-9\_\-]+\.[A-Za-z0-9\_\-]+")
# result = pattern.search(text)
result = pattern.findall(text)
print(result)

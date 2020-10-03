list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']

zipped = list(zip(list1, list2))
print(zipped)

# unzip the list

unzipped = list(zip(*zipped))
print(unzipped)

for l1, l2 in zip(list1, list2):
    print(l1, end=' ')
    print(l2)

items = ['Apple', 'Bananas', 'orange']
count = [4, 5, 8]
price = [1, 0.35, 0.33]
sentence = []
for (items, count, price) in zip(items, count, price):
    items, count, price = str(items), str(count), str(price)
    temp = 'I bought ' + count + ' ' + items + ' at ' + price + ' each rupee'
    sentence.append(temp)

print(sentence)



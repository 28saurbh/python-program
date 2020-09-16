import datetime

# print today date
today = datetime.date.today()
print(today)

# print entered date
birthday = datetime.date(2001, 9, 28)
print(birthday)

# print intermedite day
since_of_day = (today - birthday).days
print(since_of_day)

# print date after 10 days you have enter
tdalta = datetime.timedelta(days=10)
print(today + tdalta)

# print month, day, weekday
print(today.month)
print(today.day)
print(today.weekday())

# print time, date, datetime
print(datetime.time(20, 50, 10, 10))
print(datetime.date(2000, 9, 9))
print(datetime.datetime(2001, 9, 28, 20, 44, 34, 234))

# print date and time after 10 hours
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)

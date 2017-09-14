import datetime

today = datetime.date.today()
print today
print today.strftime('We are the %d %b %y')

timestamp = today.strftime('%H-%m-%s')
print timestamp

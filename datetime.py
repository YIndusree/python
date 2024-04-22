import datetime
today_date=datetime.date.today()
current_time=datetime.datetime.now().time()
today_day=today_date.strftime("%A")
print("today's date:",today_date)
print("current time:",current_time)
print("today's day:",today_day) 
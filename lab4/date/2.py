import datetime
y=datetime.datetime.now()
x=y-datetime.timedelta(days=1)
z=y+datetime.timedelta(days=1)
print(f'Yesterday-{x}\nToday-{y}\nTomorrow-{z}')
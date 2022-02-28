import datetime

l=list(map(int,input('Choose date:\n').split()))
date=datetime.date(l[0],l[1],l[2])-datetime.timedelta(days=5)
print (date)
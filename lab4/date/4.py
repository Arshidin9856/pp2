import datetime
l=list(map(int,input("First date:").split()))
i=list(map(int,input("Second date:").split()))

x=datetime.datetime(l[0],l[1],l[2])
y=datetime.datetime(i[0],i[1],i[2])
print((y-x).total_seconds())

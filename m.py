l=[]
a=1
d=[]
while a!='0':
    c=input()
    a=c
    if c!='0':
        d.append(c)
        l.append(c.split())
m=[]
y=[]
d.sort()
print(d)

'''for i in range(len(d)):
    for j in l:
        if d[i]==j[0] and m[i]==j[1] and y[i]==j[2]:
  '''         
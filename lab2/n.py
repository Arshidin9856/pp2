l=[]
a=1
s=''
while a!=0:
    c=input()
    a=int(c)
    if c!='0':
        l.append(c)
if len(l)%2==0:
    for i in range(int(len(l)/2)):
        s+=str(int(l[i])+int(l[-(i+1)])) 
        s+=" "
    print (s.strip())
else:
    c=len(l)//2
    m=l[c]
    l.pop(c)
    for i in range(int(len(l)/2)):
        s+=str(int(l[i])+int(l[-(i+1)])) 
        s+=" "
    s+=m
    print(s)
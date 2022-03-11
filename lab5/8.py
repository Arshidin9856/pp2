import re 
x=input()  # Hello World <-- HelloWorld 
l=x
z=[]
for i in l:
    if ord(i)>=65 and ord(i)<=90 and l.find(i) not in z:
        z.append(l.find(i))
        
    elif ord(i)>=65 and ord(i)<=90 and l.rfind(i) not in z:
        z.append(l.rfind(i))
        

res=''
for j in range(len(x)):
    p=True
    for i in z:
        if j==i:
            res+=' ' + x[j]
            p=False
    if p : res+=x[j]    
res=res.strip()
print(res)
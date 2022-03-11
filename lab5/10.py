from ast import Lambda
import re 
x=input()  # hello_world <-- HelloWorld 
lower=x.lower()
z=[]
for i in x:
    if (ord(i)>=65 and ord(i)<=90):
        z.append(x.index(i))
        #print(x.index(i))
res=''
for j in range(len(lower)):
    p=True
    for i in z:
        if j==i:
            res+=' ' + lower[j]
            p=False
    if p : res+=lower[j]    
res=res.strip()
m=re.sub("[ ]" , "_" , res)
print(m)
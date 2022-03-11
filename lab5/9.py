import re 
x= input()  #HelloWorld --> Hello World
c=0
s=''
for i in range(len(x)):
      
    if ord(x[i])>=65 and ord(x[i])<=90 and i!=0:
        s+=" "
        
    s+=x[i]
print(s)
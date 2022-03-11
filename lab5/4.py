import re 
x= input()
y=re.findall("[A-Z][a-z]+" , x)


print(y)
from ast import Lambda
import re 
x= input()  # hello_world --> HelloWorld
q=re.split("_" , x)
z=''
for i in q :  
    x=i
    i=x.capitalize()
    
    z+=i 
print(z)
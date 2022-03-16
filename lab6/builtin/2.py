s=input()
upp=0
low=0
for i in s :
    if ord(i)>=65 and ord(i)<=90: upp+=1
    if ord(i)>=97 and ord(i)<=122: low+=1
    
print(f'in {s} we have {upp} - upper case letter and {low} -lower case letter')     

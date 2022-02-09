s=input() #([][]{[]})
l=[]
c=0
try:
    for i in s:
        if  i=='}' and len(l)!=0 and l[c-1]=='{':
            l.pop()
            c-=2
        if  i==']' and len(l)!=0 and l[c-1]=='[':
            l.pop()
            c-=2
        if  i==')' and len(l)!=0 and l[c-1]=='(':
            l.pop()
            c-=2
        if i=='(' or i=='[' or i=='{':
            l.append(i) #l ['(']
    
        c+=1
except:
    l.append(0)  
if len(l)==0:
    print('Yes')
else:
    print('No')
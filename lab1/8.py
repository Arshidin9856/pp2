s=input() #windiws
t=input() #w
res=""

f=s.find(t) #f=0
if (not(f==-1)):
    res+=str(f)
    
l=s.rfind(t) 
if (not(l==f) and l!=-1):
    res+=" "
    res+=str(l)
if len(res)!=0:
    print (res)
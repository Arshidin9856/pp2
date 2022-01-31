a=input()
res=0
#101         1 0 1 1*2^2 +0 +1=5
b=len(a)
    
for i in a:
    res=res+(int(i)*(2**(b-1)))
    
    b=b-1


print (res)
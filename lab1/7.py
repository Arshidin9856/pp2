a=input()
res=0
#101         1 0 1 1*2^2 +0 +1=5
b=len(a)
i=0  
def toDecimal(a,res,b):
    global i    
    if b==0:
        print (res)
        return
    res+=int(a[i])*(2**(b-1))
    i+=1
    toDecimal(a,res,b-1)
   
toDecimal(a,res,b)

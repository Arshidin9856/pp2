a=list(input().split()) #2 3 1 1 4 ==> 2 - 1 - 1 - 4 + 221116164884861152250006566606950000015
#print(a)                              2 - 3 - 4 +
l=[] # 3
i=int(a[0])
#print(a[int(a[i])-1])
while a[len(a)-1] not in l:
    if int(a[i])!=0:
        i=i+int(a[i])
        try:
           l.append(a[i])
        except:
            l.append(a[i-1])
    else:
        i=i-1
        if i>0:
            while i>0:
                if int(a[i])!=0:
                    i=i+int(a[i])
                    l.append(a[i])
                else :
                    i=i-1   
                     
print(l)
'''def jump(a,i):
    
    
jump(a,i)'''
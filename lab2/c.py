n=int(input())
l=[]
for i in range (n):
    if i==0:
        l.append(list(range(n)))
    else:
        p=[]
        p.append(i)
        for j in range(1,n):
            if i == j:
                p.append(i*j)
            else:
               p.append(0)
        l.append(p)
for i in l:
    ans=''
    for j in i:
        ans+=str(j)
        ans+=' '
    print (ans)        

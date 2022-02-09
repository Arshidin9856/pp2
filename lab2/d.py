n=int(input())
l=[]
if n%2==0:
    for i in range (n):
        p=[] # #..... if n=6
        z=0
        while z<=i:
            z+=1    
            p.append('#')
        for i in range (i+1,n):
            p.append('.')
        l.append(p)
else:
    for i in range (n):
        p=[] # ....# if n=5
        
        for x in range (n-i-1):
            p.append('.')
        for j in range(i+1):
            p.append('#')
        l.append(p)

for i in l:
    ans=''
    for j in i:
        ans+=str(j)
        
    print (ans)   

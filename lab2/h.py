xo=input()
yo=list(xo.split())

n= int(input())
l=[]
for i in range (n):
    s=input()
    z=list(s.split())
    z.append(0)
    l.append(z)
dist=[]
q=[int(yo[0]),int(yo[1])]
for i in range(len(l)):
    p=[int(l[i][0]),int(l[i][1])]
   
    l[i][2]=((p[0]-q[0])**2)+((p[1]-q[1])**2)
    dist.append(l[i][2])
#print(l)
se=set(dist)
dist=list(se)
dist.sort()
for i in dist:
    for j in range(len(l)):
        ans=''
        if l[j][2]==i:
            ans+=l[j][0]+' ' + l[j][1]
            print(ans)
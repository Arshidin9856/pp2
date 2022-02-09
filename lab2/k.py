s=input()
l=[]

l=s.split()

for i in range(len(l)):
    if not(l[i].isalpha()):
        r=l[i][:-1]
        l[i]=r
p=set(l)
res=list(p)
res.sort()
print(len(res))
for i in res:
    print (i)

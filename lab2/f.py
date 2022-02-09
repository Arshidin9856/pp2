n=int(input())
names=[]
num=[]
for i in range(n):
    s=input()
    r=s.split()
    names.append(r[0])
    num.append(r[1])
sname=[]
for i in names:
    if i not in sname:
        sname.append(i) 

l=[]
for i in range(len(sname)):
    sum=0
    for j in range(len(names)):
        if sname[i]==names[j]:
            sum+=int(num[j])
    l.append(sum)
lcopy=l.copy()
lcopy.sort()
ans=[]
for i in range(len(sname)):
    if lcopy[-1]==l[i]:
        ans.append(sname[i] + ' is lucky!')
    else:
        ans.append(sname[i]+' has to receive ' +f'{lcopy[-1]-l[i]}'+' tenge')
ans.sort()
for i in ans :
    print (i)
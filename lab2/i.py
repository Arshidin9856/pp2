from dis import dis


n= int(input())
l=[]
disk=[]
for i in range(n):
    s=input()
    p=s.split()
    if p[0]=='1':
        l.append(p[1])
    else :
        disk.append(l[0])
        l.pop(0)
s=''    
for i in disk:
    s+=i 
    s+=' '
print (s)
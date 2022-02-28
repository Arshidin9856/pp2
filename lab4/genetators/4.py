def threefour(a,b):
    while a <= b:
        yield a**2
        a += 1

b=list(map(int,input().split()))

li=list(threefour(b[0],b[1]))
s=''
for i in li:
    s+=str(i)+','

print(s[:len(s)-1])
l=[]
for i in range (b[0],b[1]+1):
    l.append(i**2)

print(l==li)


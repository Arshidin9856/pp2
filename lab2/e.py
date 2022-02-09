
s=input()
if len(s.split())!=2:
    n=s
    x=input()
else:
    n,x=s.split(' ',1)
l=[]
for i in range(int(n)):
    l.append(int(x)+2*i)
xor=0
for i in l:
    #1^2^3^4^5^6^7^...
    xor^=i
print(xor)
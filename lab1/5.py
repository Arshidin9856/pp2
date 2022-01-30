s=input()
f=0
sec=-1
b=True
for i in s:
    if (i==" "):
        b=False

    if b:
        f+=1
    else:
        sec+=1
a=int(s[:f])
#print(a)
c=int(s[f:])
#print (c)
cnt=0


for i in range(2,a):
    if a%i==0:
        cnt+=1

if a<=500 and cnt==0 and c%2==0:
    print('Good job!')
else:
    print("Try next time!")

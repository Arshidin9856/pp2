n= int(input())
l=[]
for i in range(n):
    s=input()
    U=False
    L=False
    D=False
    for j in s:
        if ord(j)>=65 and ord(j)<=90:
            U=True
        if ord(j)>=97 and ord(j)<=122:
            L=True
        if ord(j)>=48 and ord(j)<=57:
            D=True
    if U and L and D:
        if s not in l:
            l.append(s)
print(len(l))
l.sort()
for i in l:
    print(i)
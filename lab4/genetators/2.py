def Even(n):
    num = 0
    while num <= n:
        if num%2==0:
            yield num
        num += 1
n=int(input())
li=Even(n)
s=''
for i in li:
    s+=str(i)+','

print(s[:len(s)-1])

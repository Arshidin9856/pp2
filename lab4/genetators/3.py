def threefour(n):
    num = 0
    while num <= n:
        if num%12==0:
            yield num
        num += 1
n=int(input())
li=threefour(n)
s=''
for i in li:
    s+=str(i)+','

print(s[:len(s)-1])

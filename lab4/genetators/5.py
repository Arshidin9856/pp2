def threefour(n):
    num = n
    while num >=0:
        yield num
        num -= 1
n=int(input())
li=threefour(n)
s=''
for i in li:
    s+=str(i)+','

print(s[:len(s)-1])

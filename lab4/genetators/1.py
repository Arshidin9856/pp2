def Square(n):
    num = 1
    while num <= n:
        yield num**2
        num += 1
n=int(input())
li=Square(n)
for i in li: print(i)

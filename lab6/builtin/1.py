import math


l=list(map(int,input().split()))
 

# print(type(l))

# x=math.prod(l)
q=1
def mult(n):
    global q
    q=q*n
    return q
x=list(map(mult,l))
print(x[-1])

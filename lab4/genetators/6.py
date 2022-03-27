from re import I


x=input()
def odd(x):
    z=1
    cnt=0
    for i in x:
        if cnt==z:
            yield i
            z+=2
        cnt+=1
l=list(odd(x))
print(l)        
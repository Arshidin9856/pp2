a=int(input())
b=input()

if b=='k':
    c=a
    c/=1024
    if not(type(c)==int):
       x=int(input())
       print('%.xf' %c)
    else:
        print(int(c))
else:
    a=1024*a
    if not(type(a)==int):
       c=int(input())
       print('%.int(c)f' %a)
    else:
        print(int(a))


   

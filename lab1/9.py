a=int(input())
list=[]
for i in range(0,a):
    c=input()
    list.append(c)
for i in range(0,a):
    if list[i][-10:]=='@gmail.com':
        print(list[i][:-10])
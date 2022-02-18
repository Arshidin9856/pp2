def Histogram(l):
    for i in l:
        s=''
        for j in range(i):
            s+='*'
        print(s)



Histogram(list(map(int,input().split())))
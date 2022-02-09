a= input()
l=list(input().split())
li=[]
for i in l:
    li.append(int (i))
li.sort()
print(li[-1]*li[-2])
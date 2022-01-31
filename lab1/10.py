a=input()
res=''
words=a.rsplit(' ')
for i in words:
    if len(i)>=3:
        res+=i
        res+=' '

print (res)
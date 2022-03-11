import re 
x= input()
y=re.sub("[.]|[ ]|[,]" ,":" , x)


print(y)
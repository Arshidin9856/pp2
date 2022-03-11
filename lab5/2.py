import re 
x= input()
y=re.search("ab{3}|ab{2}" , x)
print(y)
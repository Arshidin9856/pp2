f=open("input.txt","r")
# print(f.read())
cnt=0
for line in f:
    cnt+=1
    # print(line)
print(f"input.txt have {cnt} lines")    
f.close()
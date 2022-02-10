data = [int(i) for i in input().split()]


has_way=[False for i in data[1:]]

has_way.append(True)
for i in range(len(data)-2,-1,-1):
    if data[i]>=has_way.index(True)-i:
       has_way[i]=True

if has_way[0]:
    print(1)
else:
    print(0)

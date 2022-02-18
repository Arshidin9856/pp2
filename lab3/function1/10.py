def list_to_set(l):
    li=[]
    for i in l:
        if i not in li:
            li.append(i)
    print(li)
list_to_set(input().split())
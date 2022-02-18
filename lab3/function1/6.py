def words_reversed(l):
    s=''
    q=''
    for j in l:
        q+=j
        q+=' '
    for i in range(len(l),0,-1):
        s+=l[i-1]
        s+=' '        
        
    print(f'{q} --> {s}')

words_reversed(input().split())
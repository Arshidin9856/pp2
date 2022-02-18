from itertools import permutations
l=list()
def all_permutation(s):
    l=list(permutations(s))
    for i in l:
        a=''
        for j in i:
            a+=j
        print(a)
all_permutation(input())
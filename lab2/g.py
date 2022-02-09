n = int(input())
demons = []
for i in range(n):
    d, w = [i for i in input().split()]
    demons.append(w)
m = int(input())
for i in range(m):
    h, a, k = [z for z in input().split()]
    k = int(k)
    while k > 0 and a in demons:
        demons.remove(a)
        k -= 1
print(f'Demons left: {len(demons)}')
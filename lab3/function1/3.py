def solve(numheads,numlegs):
    b=False
    for i in range(numheads):
        #print (i)
        if numlegs==(i+1)*4+(numheads-i-1)*2:
            b=True
            print(f'{i+1} -rabbits \n{numheads-i-1} - chickens')
        if b==False and numlegs==(i+1)*2+(numheads-i-1)*4:
                print(f'{numheads-i-1} -rabbits \n{i+1} - chickens')
s=input().split()
solve(int(s[0]),int(s[1]))      
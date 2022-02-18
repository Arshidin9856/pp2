spy=[]
def spy_game(nums):
    for i in range(len(nums)):
        if  nums[i]=='0' or  nums[i]=='7':
            spy.append(nums[i])     
    if len(spy)>2:
        try:
            for i in range(len(spy)):
                if spy[i]=='0' and spy[i+1]=='0' and spy[i+1+1]=='7':
                    return True
                else: return False
        except:
            return False
def has_33(nums):
    try:
        for i in range(len(nums)):
            if nums[i]==nums[i+1] and nums[i]=='3':
                return True   
    except: 
        return False
A=input().split()
a=has_33(A)
b=spy_game(A)        
if a and b:
    print("Both spy and 33")
elif a: print("only 33")
elif b: print("only spy")
else : print ("not spy and nod 33")


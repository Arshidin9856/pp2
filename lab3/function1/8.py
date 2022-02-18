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
   
print(spy_game(input().split()) )
'''
spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
'''
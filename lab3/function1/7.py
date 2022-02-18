def has_33(nums):
    try:
        for i in range(len(nums)):
            if nums[i]==nums[i+1] and nums[i]=='3':
                return True   
    except: 
        return False
print(has_33(input().split()))
'''
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''
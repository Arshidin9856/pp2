def has_33(nums):
    
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1] and nums[i]=='3':
                return True   
        return False
print(has_33(input().split()))
'''
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
'''
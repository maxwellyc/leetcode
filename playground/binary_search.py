def helper(nums,p,q,target):
    n = q+p
    mid = n//2
    print (p,q)
    if q > p:
        if target > nums[mid]:
            return helper(nums,mid+1,q,target)
        elif target < nums[mid]:
            return helper(nums,p,mid,target)
        elif target == nums[mid]:
            return mid
    return -1


nums = [-1,0,3,5,9,12]
k = len(nums)
target = 9
print (helper(nums,0,k,target))

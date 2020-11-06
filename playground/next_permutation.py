def main(nums):
    n = len(nums)
    if n<2: return
    for i in range(n-1,0,-1):
        if nums[i]>nums[i-1]:
            s_ind = i-1
            break
    if i == 1 and nums[i]<=nums[i-1]:
        nums.sorted()
        return
    for i in range(s_ind+1,n):
        if i == n-1 or nums[i+1]<=nums[s_ind]:
            nums[s_ind],nums[i] = nums[i],nums[s_ind]
            break
    tail = (n-1-s_ind)//2
    for i in range(tail):
        nums[s_ind+i+1],nums[n-1-i] = nums[n-1-i],nums[s_ind+i+1]

nums = [5,4,7,5,3,2,1]
main(nums)
print (nums)

# Binary search template analysis:
# https://leetcode.com/explore/learn/card/binary-search/136/template-analysis/935/
# I think the major difference is that at each step
# do you still want m to be in your next search space. if you do, you need l = m or r = m
# to ensure that. In template 2, l = m+1 because r=m will remain m in the search
# space, and you explicitly do not need m if condition for l to move is triggered.
# It always helps to think about the previous while loop before termination,
# was it because l moved and triggered the termination, if so, what does this new l's element mean?
# What was the previous l such that it triggered the move?
# OR, was it r moved that triggered the termination, if so, what does this new r's element mean?
# What was the previous r such that it triggered the move?
# These are valid questions that you need to think about, it's a major part of the code,
# not something that you should guess, or know before hand because of some template you
# use, it differes case by case, depending on the problem at hand.
# So don't be lazy or afraid to run manual tests, think about the previous while loop.

def binarySearch(nums, target):
    l,r = 0,len(nums)
    while l<r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l=m+1
        else:
            r=m
    return l if (l!=len(nums) and nums[l] == target) else -1

# return location to insert target in sorted array num, set left is true to
# insert leftmost, otherwise rightmost
# !!! note you need to check if nums[l] == target to be sure if target is in array
# otherwise you're only finding insertion point.
# also check if l = len(nums), this happens when target > max(nums)
def extreme_insertion_index(nums, target, left):
    l, r = 0, len(nums)
    while l < r:
        m = (l + r) // 2
        if nums[m] > target or (left and target == nums[m]):
            r = m
        else: # nums[m] <= target
            l = m+1
    return l


def temp1(nums, target):
    l,r = 0,len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l=m+1
        else:
            r=m-1
    return -1


def temp3(nums, target):
    l,r = 0,len(nums)-1
    while l+1<r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l=m
        else:
            r=m
    if nums[l] == target:
        return l
    if nums[r] == target:
        return r
    return -1
#       0 1 2 3 4 5 6 7 8 9 10
nums = [1,1,1,2,3,3,3,4,5,5,5]
target = 2
print ("nums\t",nums)
print ("ind\t",list(range(len(nums))))
print (f'{target} can be inserted before index (leftmost) ',extreme_insertion_index(nums, target, 1))
print (f'{target} can be inserted before index (rightmost)',extreme_insertion_index(nums, target, 0))

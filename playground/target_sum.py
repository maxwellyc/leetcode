def findTargetSumWays(nums,S):
    stack = [(0,0)]; count = 0; visited = {(0,0):1}
    n = len(nums); nums_sum = sum(nums)
    sum_left = [nums_sum]
    for i in range(1,n):
        sum_left.append(sum_left[-1]-nums[i])
    print (sum_left)
    while stack:
        sums, lvl = stack.pop(0)
        new_num = nums[lvl]
        a = sums + new_num
        b = sums - new_num
        if lvl < n-1:
            if (a,lvl+1) in visited:
                visited[(a,lvl+1)] += visited[(sums,lvl)]
            elif S - a <= sum_left[lvl]:
                stack.append((a,lvl+1))
                visited[(a,lvl+1)] = visited[(sums,lvl)]
            if (b,lvl+1) in visited:
                visited[(b,lvl+1)] += visited[(sums,lvl)]
            elif S - b <= sum_left[lvl]:
                stack.append((b,lvl+1))
                visited[(b,lvl+1)] = visited[(sums,lvl)]
        elif lvl == n-1:
            if a == S: count += visited[(sums,lvl)]
            if b == S: count += visited[(sums,lvl)]

    return count

nums=[0,0,0,0,0,0,0,0,1]; S = 1
print (findTargetSumWays(nums,S))

def splitArray(nums, m):
    n = len(nums); A = [0]; sums=0
    for i in nums:
        sums += i
        A.append(sums)
    if m == 1: return A[-1]
    # estimate for even split
    s = A[-1]/m; cur_max = 0
    # location to cut
    l,r = 1,n+1; head = 0
    while m>1:
        m-=1
        r = n
        while l<r:
            mid = (l+r)//2
            if A[mid]-A[head] <= s:
                l=mid+1
            else:
                r=mid
        if (((A[l]-A[head])-s)-(A[n]-A[l]-(A[-1]-s)))<(((A[l-1]-A[head])-s)-(A[n]-A[l-1]-(A[-1]-s))):
            l = l-1
        cur_max = max(cur_max,A[l]-A[head])
        head = l
    cur_max = max(cur_max,A[n]-A[l])

    return cur_max

nums=[1,200]
m=2
print (splitArray(nums, m))

nums = [1,1,7,7]
memo = {} # [(set(arr),len(arr))] # calc(a,b) can be memo-ed
tgt = 24

def calc(a,b):
    if (a,b) not in memo and (b,a) not in memo:
        ans = []
        ans.extend([a+b,a*b,a-b,b-a])
        if a != 0:
            ans.append(b/a)
        if b != 0:
            ans.append(a/b)
        memo[(a,b)] = memo[(b,a)] = set(ans)
    return memo[(a,b)]

def judge(arr):
    #print (arr,"***********")
    n = len(arr)
    if n == 2:
        for val in calc(arr[0],arr[1]):
            if abs(val - tgt) < 0.001:
                print (arr,tgt)
                return True
    for i in range(n-1):
        for j in range(i+1,n):
            others = arr[:i]+arr[i+1:j]+arr[j+1:]
            pool = calc(arr[i],arr[j])
            #print (others, pool, [arr[i],arr[j]])
            for p in pool:
                # n = 4, problem becomes can 3 elements form 24
                # n = 3, problem becomes can 2 elements form 24
                if judge(others + [p]):
                    return True
    return False
print(judge(nums))

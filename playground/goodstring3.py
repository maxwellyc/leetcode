def goodString2(n):
    K = n
    # choose y from x
    def C(x, y):
        num = 1
        denom = 1
        for i in range(x, x-y,-1):
            num *= i
        for j in range(1, y+1):
            denom *= j
        return num / denom

    def helper(path, peak):
        if len(path) == n:
            return 1 if peak else 0
        elif len(path) > n: return 0
        ans = 0
        for i in range(K):
            if i in path:
                continue
            # if peaked
            if peak and i < path[-1]:
                ans += helper(path+[i], True)
            elif not peak:
                # peak now
                if i > path[-1]:
                    ans += helper(path+[i], True)
                # peak later
                elif i < path[-1]:
                    ans += helper(path+[i], False)
        return ans

    res = 0
    for i in range(K):
        this = helper([i], False)
        res += this
        # print (i,this)

    return res * C(26,n)

if __name__ == '__main__':
    print (goodString2(5))

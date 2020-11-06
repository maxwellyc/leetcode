from goodstring2 import goodString2
def goodString(n):

    # given x integers 0 to x-1, how many combinations of monotonically (increasing)
    # array of length m can we create
    # we'll add memoization later
    memo = {}
    def comb(m, x):
        if (m,x) in memo:
            return memo[(m,x)]
        # elif x == 0:
        #     return 0
        elif m == 0:
            return 1
        elif m == x:
            return 1
        elif m == 1:
            return x
        elif m > x:
            return 0
        else:
            count = 0
            for y in range(x):
                curr = comb(m-1, y)
                # if curr == 0: break
                count += curr
            memo[(m,x)] = count
        return count
    ans = 0
#    return comb(n,26) * (n-1)
    for i in range(26):
        for k in range(n):
            # letter[i] at index k of the good string GS
            # 1. GS[k:] needs to be all smaller than letter[i], mono decreasing
            # 2. GS[:k-1] needs to have at least one smaller than letter[i], mono decreasing
            # 3. no repeat letters, so whatever smaller letters
            #    used in GS[k:] can't appear in GS[:k-1]
            # 4. GS[k] > GS[k-1], perhaps we can start anchoring GS[k-1] given letter[i]

    return ans

N = 3
print (goodString(N))
print (goodString2(N))

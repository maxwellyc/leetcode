def goodString2(n):
    # choose y from x, combinatorics
    def C(x, y):
        num = 1
        denom = 1
        for i in range(x, x-y,-1):
            num *= i
        for j in range(1, y+1):
            denom *= j
        return num / denom

    def f(n):
        if n == 2:
            return 1
        return 2*f(n-1) + n-1

    return f(n) * C(26,n)


if __name__ == '__main__':
    print (goodString2(5))

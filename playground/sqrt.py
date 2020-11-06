def mySqrt(x):
    if not x: return x
    if x < 4: return 1
    l, r = 1, x
    while l < r:
        m = l + (r-l)//2
        print (l,r,m)
        s = m*m
        if s == x:
            return m
        elif s < x:
            l = m+1
        else:
            r = m-1
    return m

print (mySqrt(8))

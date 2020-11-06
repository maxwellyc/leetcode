def generateParenthesis(n):
    a,b = 0,0
    # a is number of "(", b is number of ")"
    # maintain b<=a before each operation
    # if b==a, only add "(", if b<a, add "(" or ")"
    # but total of each must be less than n
    # after adding, recursively go down.
    ans1,ans2=[],set()
    def helper(a,b,prev):
        if a<n:
            if b==a:
                helper(a+1,b,prev+"(")
            else:
                helper(a+1,b,prev+"(")
                helper(a,b+1,prev+")")
        elif a==n:
            while b < n:
                prev+=")"
                b+=1
            ans1.append(prev)
            ans2.add(prev)

    helper(0,0,"")
    return len(ans1),len(ans2)

print (generateParenthesis(10))

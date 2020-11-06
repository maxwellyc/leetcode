def numSquares(n):
    pool = []
    for i in range(1,n+1):
        if i*i < n:
            pool.append(i*i)
        elif i*i == n:
            return 1

    stack, visited = [0], set()
    ans = 0
    while stack:
        ans += 1; new_stack = []
        for num in stack:
            for ps in pool:
                summed = num + ps
                if summed == n:
                    return ans
                if summed < n and summed not in visited:
                    visited.add(summed)
                    new_stack.append(summed)
        stack = new_stack

print (numSquares(1))

def count_substring_zero(A):
    dp = [0]*(len(A)+1)
    count = 0
    for i in range(len(A)):
        if A[i] == '0':
            dp[i+1] = dp[i] + 1
            count += dp[i+1]
    return count


A = "10011000"
print (count_substring_zero(A))

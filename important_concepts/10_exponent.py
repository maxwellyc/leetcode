import time
# calculate x^n, n is integer
# we can do this recursively, but there's extra division (more expensive than multiplication)
# we could replace division by bit shifting, however, if we could transform
# this into iterative, we could perhaps save resurive overhead
# iterative uses binary bit, if n = 8+2+1 = 11, bin(n) = 1011
# so we need x^8, x^2, x^1, or inversely , x^1, x^2, x^8 in our multiplication
ans = 1
def recursive_exponent(x, n):
    if n == 0:
        return 1
    ans = recursive_exponent(x, n>>1)
    ans = ans*ans
    if n%2:
        ans = ans*x
    return ans

def iterative_exponent(x, n):
    ans = 1
    # careful with the while loop condition
    # because arithmetic bit right shift will get you -1 eventually
    while n > 0:
        if n & 1: # check smallest bit
            ans *= x
        n >>= 1
        x = x*x
    return ans



t1 = time.time()
for i in range(1000000):
    recursive_exponent(2, 100)
t2 = time.time()
print (t2-t1, " seconds")
t1 = time.time()
for i in range(1000000):
    iterative_exponent(2, 100)
t2 = time.time()
print (t2-t1, " seconds")

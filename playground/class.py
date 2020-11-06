class A:
    x = 1

class B(A):
    pass

B.x = 2
print (A.x, B.x)

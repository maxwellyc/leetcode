def binary(x):
    rev=[]; ans="";neg=0
    if x < abs(x): neg=1; x = abs(x)
    while x:
        if x%2:
            rev+="1"
        else:
            rev+="0"
        x = x//2
        
        
    while rev:
        ans += rev.pop()
    if neg: print ("-"+ans)
    else: print (ans)


binary(3)

def main(s):
    n = len(s)
    if not n: return 0
    j,ans,d = 0,0,{}
    # j is start index of trailing no-repeat substring
    for i,c in enumerate(s):
        if c in d:
            print (i,j)
            ans = max(ans,i-j)
            j = max(j,d[c]+1)
            print (j)
        elif i == len(s)-1:
            ans = max(ans,i-j+1)
        d[c] = i
    
    return ans

s = "monstemr"
print (main(s))

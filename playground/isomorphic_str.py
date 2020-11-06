def isIsomorphic( s, t):
    l,m = {},{}
    for i,c in enumerate(s):
        if c not in l:
            l[c] = (-1,)
        l[c]+=(i,)
    
    for i,c in enumerate(t):
        if c not in m:
            m[c] = (-1,)
        m[c]+=(i,)
    
    v1 = set(l.values())
    v2 = set(m.values())
    print (v1,v2)
    if not (v1-v2):
        return True
    else:
        return False

s = 'paper'
t = 'title'
print (isIsomorphic( s, t))

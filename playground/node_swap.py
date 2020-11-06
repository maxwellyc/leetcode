def reverse(s):
    #s = [s[-i] for i in range(1,len(s))]
    c = []
    for i in range(1,len(s)+1):
        c += s[-i]
    print (c)
    s = c

s = ["h","e","l","l","o"]
reverse(s)
print (s)

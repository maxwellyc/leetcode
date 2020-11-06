def calc(a,b,c):
    if c == "+": return a+b
    elif c == "-": return a-b
    elif c == "*": return a*b
    elif c == "/": return int(a/b)

def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def helper(tokens):
    print (tokens)
    if len(tokens) <= 2: return int(tokens.pop())
    c = tokens.pop()
    x = tokens[-1]
    if is_num(x):
        b = int(tokens.pop())
        x = tokens[-1]
        if is_num(x):
            a = int(tokens.pop())
            return calc(a,b,c)
        else:
            a = helper(tokens)
    else:
        b = helper(tokens)
        a = helper(tokens)
    return calc(a,b,c)

tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print(helper(tokens))

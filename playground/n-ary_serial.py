class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def deserialize(data):
    if not data: return None
    def isNum(x):
        try:
            float(x)
            return True
        except:
            return False

    ind = 0
    root = None
    childs = []
    prev = [] # previous level of parent nodes that needs to be connected to children
    # '1,#*3,2,4,#*5,6,**#**'
    while ind < len(data):
        if data[ind] == '#':
            ind += 1
        elif data[ind] == '*':
            pa = prev.pop(0)
            pa.children = childs
            childs = []
            ind += 1
        elif data[ind] == ',':
            ind += 1
        else:
            s = ind # start index of number
            while isNum(data[ind]):
                ind += 1 # keep reading number
            if s == ind: continue
            nn = Node(int(data[s:ind])) # create node
            if root == None:
                root = nn
            else:
                childs.append(nn)
            prev.append(nn) # each node on this level is a parent for the next level
            print (ind,nn.val,len(childs), len(prev))
            # although it could have 0 child
    print('complete',root.val, len(root.children))


data = '1,#3,2,4,*#5,6,***#**'
deserialize(data)

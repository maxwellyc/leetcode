import collections
def openLock(deadends,target):
    def nb(node):
        for i in range(4):
            x = int(node[i])
            for j in (-1,1):
                yield node[:i]+str((x+j)%10)+node[i+1:]
    if target == "0000": return 0
    if "0000" in deadends: return -1
    d_set = set(deadends)
    queue = collections.deque([("0000", 0)])
    visited = {"0000"}
    while queue:
        node, step = queue.popleft()
        if node  == target: return step
        if node in d_set: continue
        for nei in nb(node):
            if nei not in visited:
                visited.add(nei)
                queue.append((nei,step+1))
    return -1

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print (openLock(deadends,target))

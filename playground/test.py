# DFS inorder
def inorder_dfs(root):
    stack = []
    res = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack: return res
        root = stack.pop()
        res.append(root.val)
        root = root.right

def inorder_dfs2(root):
    res = []
    def helper(root):
        if not root: return
        helper(root.left)
        res.append(root.val)
        helper(root.right)
    helper(root)
    return res

def preorder_dfs(root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res

def preorder_dfs2(root):
    res = []
    def helper(root):
        if not root: return
        res.append(root.val)
        helper(root.left)
        helper(root.right)
    helper(root)
    return res

def postorder_dfs(root):
    if not root: return []
    stack = [root]
    res = []
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    return res[::-1]

def postorder_dfs(root):
    res = []
    def helper(root):
        if not root: return
        helper(root.left)
        helper(root.right)
        res.append(root.val)
    helper(root)
    return res

def BFS_iterative(root):
    if not root: return
    q = [root]
    res = []
    while q:
        new_q = []; lvl = []
        for node in q:
            lvl.append(node.val)
            for child in node.children:
                new_q.append(child)
        q = new_q
        res.append(lvl)
    return res

def BFS_recursive(root):
    levels = []
    def helper(root,lvl):
        if len(levels) == l:
            levels.append([])
        levels[l].append(root.val)
        if root.left:
            helper(root.left,lvl+1)
        if root.right
            helper(root.right,lvl+1)
    helper(root, 0)
    return levels

def binary(A,target):
    l, r = 0, len(A)
    while l < r:
        m = l + (r - l ) // 2
        if A[m] == target:
            return m
        elif A[m] < target:
            l = m + 1
        else:
            r = m
    return l if (l != len(A) and A[l] == target) else -1

def insert_index(A, target, left):
    l, r = 0, len(A)
    while l < r:
        m = l + (r - l ) // 2
        if A[m] > target or (left and A[m] == target):
            r = m
        else:
            l = m + 1
    return l

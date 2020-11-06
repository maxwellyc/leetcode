#################### IN-ORDER DFS ####################
# In-order traversal is to traverse the left subtree first (the entire subtree).
# Then visit the root.
# Finally, traverse the right subtree.
# Typically, for binary search tree, we can retrieve all the data in sorted
# order using in-order traversal.

## Iterative
def inOrder_iterative(root: TreeNode):
    res, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        # at this point, top of the stack is the leftmost, bottom node
        # which we'll pop first later on.
        if not stack:
            return res
        root = stack.pop()
        res.append(root.val)
        root = root.right

## Recursive 1
def inorderTraversal(root: TreeNode):
    def helper(node):
        if node:
            helper(node.left)
            res.append(node.val)
            helper(node.right)
    res = []
    helper(root)
    return res
# reviewed 2/13/2020

#################### PRE-ORDER DFS ####################
# Pre-order traversal is to visit the root (node) first.
# Then traverse the left subtree.
# Finally, traverse the right subtree.

## Iterative
def preOrder_iterative(root: TreeNode):
    if not root: return []
    stack = [root]; List = []
    while stack:
        r = stack.pop()
        List.append(r.val)
        # this reverse of order is due to stack's LIFO (last in first out)
        if r.right:
            stack.append(r.right)
        if r.left:
            stack.append(r.left)
    return List
# reviewed 2/13/2020

## Recursive 1
def preorderTraversal(root: TreeNode):
    def helper(node):
        if node:
            res.append(node.val)
            helper(node.left)
            helper(node.right)
    res = []
    helper(root)
    return res
# reviewed 2/13/2020

#################### POST-ORDER DFS ####################
# Post-order traversal is to traverse the left subtree first.
# Then traverse the right subtree.
# Finally, visit the root.
# It is worth noting that when you delete nodes in a tree,
# deletion process will be in post-order. That is to say, when you delete a node,
# you will delete its left child and its right child before you delete the node itself.
# Also, post-order is widely use in mathematical expression.
# It is easier to write a program to parse a post-order expression.

## Iterative
def postOrder_iterative(root: TreeNode):
    if not root: return []
    res, stack = [], [root]
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    return res[::-1]
# reviewed 2/13/2020

## Recursive 1
def postorderTraversal(root: TreeNode):
    def helper(node):
        if node:
            helper(node.left)
            helper(node.right)
            res.append(node.val)
    res = []
    helper(root)
    return res
# reviewed 2/13/2020

#################### BFS ####################
# returns List[List[]], each level is a separate sub-list

# Iterative
def BFS_iterative():
    if not root: return []
    child, List = [root], []
    while child:
        childVal = []; newChild = []
        for q in child:
            childVal.append(q.val)
            if q.left: newChild.append(q.left)
            if q.right: newChild.append(q.right)
        child = newChild
        List.append(childVal)
    return List

# Recursive
# basically all values will be stored in its corresponding sub-array
# due to the "level" variable that's being passed on, and since left always
# comes first, the order within a level will be correct.
def BFS_recursive():
    if not root: return []
    levels = []
    def helper(node,level):
        if len(levels) == level:
            levels.append([]) # initialize new level sub-array
        levels[level].append(node.val)
        if node.left:
            helper(node.left, level+1)
        if node.right:
            helper(node.right, level+1)
    helper(root,0)
    return levels

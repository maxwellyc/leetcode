class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build(inord,preord,flag='root'):
    r_val = preord[0]
    root = TreeNode(r_val)
    ind = inord.index(r_val)
    print (ind)
    if ind > 0:
        root.left = build(inord[:ind],preord[1:ind+1],'left')
    if ind < len(inord)-1:
        root.right = build(inord[ind+1:],preord[ind+1:],'right')
    return root

preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]

build(inorder, preorder)

class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten(head):
    if not head: return None
    def travel(node):
        print (f"{node.val} call")
        while node:
            q = node.next
            if not q: tail = node
            if node.child:
                print (node.val,node.child.val)
                node.next = node.child
                node.child.prev = node
                t = travel(node.child)
                if q:
                    q.prev = t
                t.next= q
                print (node.val,node.child.val)
                node.child = None
        
            node = node.next
        return tail
    travel(head)
    return head

c = Node(3,None,None,None)
b = Node(2,None,None,c)
head = Node(1,None,None,b)

flatten(head)


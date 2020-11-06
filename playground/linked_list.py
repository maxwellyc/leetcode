class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        root = self.head
        for i in range(index):
            root = root.next
            if not root:
                return -1
        return root.val


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
            self.len += 1
            return
        new = Node(val)
        new.next = self.head
        self.head = new
        self.len += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.head = Node(val)
            self.len += 1
            return
        root = self.head
        while root.next:
            root = root.next
        root.next = Node(val)
        self.len += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.len: return
        elif index == self.len:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            root = self.head
            for i in range(index-1):
                root = root.next
            new = Node(val)
            new.next = root.next
            root.next = new
            self.len += 1



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.len: return
        elif index == 0:
            if self.head:
                self.head = self.head.next
                self.len -= 1
            return
        else:
            root = self.head
            for i in range(index):
                prev = root
                root = root.next
            prev.next = root.next
        self.len -= 1

obj = MyLinkedList()
#param_1 = obj.get(index)
# obj.addAtHead(1)
# obj.addAtTail(3)
obj.addAtIndex(0,10)
obj.addAtIndex(0,20)
obj.addAtIndex(1,30)
print (obj.get(0), obj.get(1), obj.get(2))
obj.deleteAtIndex(2)
obj.deleteAtIndex(0)
print (obj.get(0), obj.get(1), obj.get(2))

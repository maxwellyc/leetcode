class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.d = {}
        self.c = capacity
        self.oldest = None
        self.newest = None
        self.key_node = {}
        self.size = 0

    def get(self, key):
        if key in self.d:
            self.LRU_update(key)
            print (self.d)
            output = []
            node = self.oldest
            while node:
                output.append(node.val)
                node = node.next
            print ("old>",output,"<new")
            print (f"old pointer: {self.oldest.val}; new pointer: {self.newest.val}")
            print (f"GET {key}: ",self.d[key])
            return self.d[key]
        else:
            print (f"GET {key}: -1")
            return -1

    def put(self, key, value):
        if key not in self.d:
            self.size+=1
        self.LRU_update(key)
        self.d[key] = value
        print (self.d)
        output = []
        node = self.oldest
        while node:
            output.append(node.val)
            node = node.next
        print ("old>",output,"<new")
        print (f"old pointer: {self.oldest.val}; new pointer: {self.newest.val}")
    
    
    def LRU_update(self,key):
        if key not in self.d:
            # create new node
            incoming = Node(key)
            self.key_node[key] = incoming
            prev_new = self.newest
            if prev_new:
                # connect previous newest with incoming
                prev_new.next = incoming
                # change newest pointer to incoming node
            else:
                self.oldest = incoming
            incoming.prev = prev_new
            self.newest = incoming
            # delete from dictionary and update oldest only when
            # cache capacity is reached
            if self.size > self.c:
                prev_old = self.oldest
                # delete oldest key from dictionary
                self.d.pop(prev_old.val)
                self.key_node.pop(prev_old.val)
                # shift oldest pointer to next oldest
                self.oldest = prev_old.next
                self.oldest.prev = None
                # reduce size by one, we keep size to know when to
                # delete.
                self.size-=1
                print (f"#########DELETING########## KEY{prev_old.val}")
        # key already in cache, we need to update its position only
        else:
            prev_new = self.newest
            prev_old = self.oldest
            cur = self.key_node[key]
            if key != self.newest.val:
                NEXT,PREV = cur.next,cur.prev
                # if None, means cur is oldest
                if PREV:
                    PREV.next = NEXT
                else:
                    self.oldest = NEXT
                NEXT.prev = PREV
                prev_new.next,cur.prev,cur.next = cur,prev_new,None
                self.newest = cur



# Your LRUCache object will be instantiated and called as such:
command = ["LRUCache","put","put","get","put","get","put","get","get","get"]

input = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

OUT= []
for ind,com in enumerate(command):
    if com == "LRUCache":
        print("INIT**************************")
        A = LRUCache(input[ind][0])
        OUT.append(None)
        print ("\n")
    elif com == "get":
        print(f"GET {input[ind][0]}**************************")
        OUT.append(A.get(input[ind][0]))
        print ("\n")
    else:
        print(f"PUT {input[ind]}**************************")
        A.put(input[ind][0],input[ind][1])
        OUT.append(None)
        print ("\n")

print (OUT)

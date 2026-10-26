class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # map key to node 
        self.left = Node(0,0) #least used
        self.right = Node(0,0) # most recent  
        self.left.next, self.right.prev = self.right, self.left
        
    def get(self, key: int) -> int:
        # also update most recent pointer, by remove it and then add it to the right 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1 
        
    # update the value if key already exist by remove, create new, insert
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        # check capacity every insert, remove lru from linked list, and hashmap
        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]



    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        

    def insert(self, node):
        # insert at right
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev

    


        #hashmap [key: val (pointer to the doublely link list)]
        # each node has prev, next 
        # check capacity, remove lru, add new node, updaate hashmap, update the left lru and mru pointer


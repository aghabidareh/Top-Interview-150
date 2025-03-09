class LRUCache(object):
    class node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity):
        self.size = capacity
        self.c_size = 0
        self.d = {}
        self.head = None
        self.tail = None

    def delete_n_sift_node(self, node):
        if node == self.tail:
            return
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = None
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def get(self, key):
        if key in self.d:
            self.delete_n_sift_node(self.d[key])
            return self.d[key].val
        else:
            return -1

    def put(self, key, value):
        if key in self.d:
            self.d[key].val = value
            self.delete_n_sift_node(self.d[key])
        else:
            if self.c_size == self.size:
                self.d.pop(self.head.key)
                self.head = self.head.next
                if self.head:
                    self.head.prev = None
                else:
                    self.tail = None
                self.c_size -= 1

            node = self.node(key, value)
            self.d[key] = node
            if self.tail:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                self.tail = node
                self.head = node
            self.c_size += 1
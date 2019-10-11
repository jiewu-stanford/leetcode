'''
Title     : 146. LRU Cache
Problem   : https://leetcode.com/problems/lru-cache/description/
'''
'''
use ordered dictionary to remember the order of insertion
Reference: https://leetcode.com/problems/lru-cache/discuss/45952/Python-concise-solution-with-comments-(Using-OrderedDict).
'''
import collections
class LRUCache(object):

    def __init__(self, capacity):
        self.orderedic = collections.OrderedDict() 
        self.capacity = capacity

    def get(self, key):
        if key not in self.orderedic: return -1
        val = self.orderedic.pop(key)
        self.orderedic[key] = val   # set it as the newest insertion
        return val

    def put(self, key, value):
        if key in self.orderedic:
            self.orderedic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.orderedic.popitem(last=False)   # remove the first (key, val) pair
        self.orderedic[key] = value

''' use list to maintain insertion order explicitly instead of using OrderedDict(), ibid. '''
class LRUCache(object):

    def __init__(self, capacity):
        self.order = []
        self.cache = {}
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.order.remove(key)
        self.order.append(key)
        return val

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.cache.pop(self.order[0])
                self.order.pop(0)
        self.cache[key] = value
        self.order.append(key)
'''
use doubly linked list to realize time O(1) removal
Reference: https://leetcode.com/problems/lru-cache/discuss/202067/Python-or-O(1)-tm-146
Reference: https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList
'''
class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.next, self.prev = {}, {}
        self.head, self.tail = 'dummy_head_val', 'dummy_tail_val'   # they are not the first and last node of the list, they are instead linked to the first and last node
        self.connect(self.head, self.tail)

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.remove(key)
        self.append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache:
            self.remove(key)
        else:
            if len(self.cache) > self.capacity:
                self.remove(self.next[self.head])
        self.append(key, value)

    def connect(self, a, b):
        self.next[a], self.prev[b] = b, a

    def remove(self, key):
        self.connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache[key]

    def append(self, key, value):
        self.cache[key] = value
        self.connect(self.prev[self.tail], key)
        self.connect(key, self.tail)   # prev <--> key <--> tail
        if len(self.cache) > self.capacity:
            self.remove(self.next[self.head])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
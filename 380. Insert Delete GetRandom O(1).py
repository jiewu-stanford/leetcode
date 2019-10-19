'''
Title     : 380. Insert Delete GetRandom O(1)
Problem   : https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
''' Reference: https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python '''
import random
class RandomizedSet(object):

    def __init__(self):
        self.num = []
        self.pos = {}

    def insert(self, val):
        if val in self.pos: return False
        self.pos[val] = len(self.num)
        self.num.append(val)
        return True

    def remove(self, val):
        if val not in self.pos: return False
        indx = self.pos[val]
        last = self.num[-1]
        self.num[indx] = last
        self.num.pop()
        self.pos[last] = indx        
        del self.pos[val]
        return True

    def getRandom(self):
        return random.choice(self.num)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
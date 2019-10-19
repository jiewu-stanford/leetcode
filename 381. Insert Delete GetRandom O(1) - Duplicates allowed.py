'''
Title     : 381. Insert Delete GetRandom O(1) - Duplicates allowed
Problem   : https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
'''
''' Reference: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/141075/Python-simple-and-readable-solution-100-ms-beats-98 '''
import collections
class RandomizedCollection(object):
    def __init__(self):
        self.num = []
        self.pos = collections.defaultdict(set)

    def insert(self, val):
        flag = val not in self.pos   # duplicates allowed thus do not return False as in the 380. solution
        self.pos[val].add(len(self.num))
        self.num.append(val)
        return flag

    def remove(self, val):
        if val not in self.pos: return False
        if self.num[-1] != val:
            indx = self.pos[val].pop()
            last = self.num[-1]
            self.num[indx] = last
            self.pos[last].discard(len(self.num)-1)
            self.pos[last].add(indx)   # self.pos[last] = indx
        else:
            self.pos[val].discard(len(self.num)-1)
        self.num.pop()
        if not self.pos[val]: del self.pos[val]   # there may be duplicate remaining
        return True

    def getRandom(self):
        return random.choice(self.num)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
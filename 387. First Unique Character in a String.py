'''
Title     : 387. First Unique Character in a String
Problem   : https://leetcode.com/problems/first-unique-character-in-a-string/
'''
''' straightforward dictionary bookkeeping '''
class Solution(object):
    def firstUniqChar(self, s):
        d, seen = {}, set()
        for i, c in enumerate(s):
            if c not in seen:
                d[c] = i
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values()) if d else -1

''' use counter() to count all at once, one line '''
import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.find(c) for c, v in collections.Counter(s).items() if v == 1] or [-1])
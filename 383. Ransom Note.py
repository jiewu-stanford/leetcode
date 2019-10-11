'''
Title     : 383. Ransom Note
Problem   : https://leetcode.com/problems/ransom-note/
'''
''' one line counter() comparison '''
import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

''' step-by-step check, easily comprehensible '''
import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = collections.Counter(magazine)
        for c in ransomNote:
            if c not in d:
                return False
            else:
                d[c] -= 1
                if d[c] < 0: return False
        return True
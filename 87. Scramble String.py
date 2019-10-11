'''
Title     : 87. Scramble String
Problem   : https://leetcode.com/problems/scramble-string/
'''
'''
recursive solution
Reference: https://leetcode.com/problems/scramble-string/discuss/29459/Python-recursive-solution
'''
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 != l2 or sorted(s1) != sorted(s2):
            return False
        if l1 < 4 or s1 == s2:
            return True
        for i in range(1, l1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
'''
recursive solution with memoization
Reference: https://leetcode.com/problems/scramble-string/discuss/29452/Python-dp-solutions-(with-and-without-memorization)
'''
class Solution:
    def __init__(self):
        self.d = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.d: return self.d[(s1, s2)]
        l1, l2 = len(s1), len(s2)
        if l1 != l2 or sorted(s1) != sorted(s2):
            self.d[(s1,s2)] = False; return False
        if l1 < 4 or s1 == s2:
            self.d[(s1,s2)] = True; return True
        for i in range(1, l1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                self.d[(s1,s2)] = True; return True
        self.d[(s1,s2)] = False; return False
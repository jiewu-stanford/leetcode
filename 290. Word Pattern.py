'''
Title     : 290. Word Pattern
Problem   : https://leetcode.com/problems/word-pattern/
'''
'''
adapt the 205. solution
Reference: https://leetcode.com/problems/word-pattern/discuss/73433/Short-in-Python
'''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        return len(set(zip(s,t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

''' with helper function, ibid. '''
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        return self.helper(pattern) == self.helper(str.split())

    def helper(self, s):
        d = {}
        count = []
        for i, item in enumerate(s):
            if item not in d:
                d[item] = i
            count.append(d[item])
        return count
'''
Title     : 392. Is Subsequence
Problem   : https://leetcode.com/problems/is-subsequence/
'''
'''
straightforward iterative two-pointer solution
Reference: https://leetcode.com/problems/is-subsequence/discuss/87421/Python-simple-solution
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: i += 1
            j += 1
        return i == len(s)
'''
clever use of all()
Reference: https://leetcode.com/problems/is-subsequence/discuss/87258/2-lines-Python
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)
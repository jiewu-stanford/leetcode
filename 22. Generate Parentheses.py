'''
Title     : 22. Generate Parentheses
Problem   : https://leetcode.com/problems/generate-parentheses/
'''
''' recursive helper function, l = number of allowed '(', r = number of allowed ')' '''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, '', n, n)
        return res
    
    def helper(self, res, acc, l, r):
        if l == 0 and r == 0:
            res.append(acc)
        if l > 0:
            self.helper(res, acc+'(', l-1, r)
        if l < r:
            self.helper(res, acc+')', l, r-1)
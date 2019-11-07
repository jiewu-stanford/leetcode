'''
Title     : 459. Repeated Substring Pattern
Problem   : https://leetcode.com/problems/repeated-substring-pattern/
'''
''' Reference: https://leetcode.com/problems/repeated-substring-pattern/discuss/94455/1-line-in-Python '''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[:i+1]*(len(s)//(i+1)) == s:
                return True
        return False
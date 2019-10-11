'''
Title     : 161. One Edit Distance ($$$)
Problem   : https://leetcode.com/problems/one-edit-distance/
          : https://www.lintcode.com/problem/one-edit-distance/description
'''
''' Reference: https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/161%20One%20Edit%20Distance.py '''
class Solution:
    def isOneEditDistance(self, s, t):
        dif = abs(len(s) - len(t))
        if dif > 1 or s == t: return False
        if dif == 0:   # one edit = one replacement
            return sum([s[i]!=t[i] for i in range(len(s))]) == 1
        if len(s) > len(t): s, t = t, s
        for i in range(len(s)):
            if s[i] != t[i]: return s[i:] == t[i+1:]
        return True   # the difference is the last character
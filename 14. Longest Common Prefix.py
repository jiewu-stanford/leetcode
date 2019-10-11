'''
Title     : 14. Longest Common Prefix
Problem   : https://leetcode.com/problems/longest-common-prefix/
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i >= len(s) or s[i] != strs[0][i]:   # if any one of strings has a different character (including space)
                    return strs[0][:i]
        return strs[0]
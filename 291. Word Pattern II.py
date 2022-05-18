'''
Title     : 291. Word Pattern II ($$$)
Problem   : https://leetcode.com/problems/word-pattern-ii/description/
          : https://www.lintcode.com/problem/word-pattern-ii/description
'''
'''
recursion carried out through substring, note that different from 290. we have to guess how to split the string to match the pattern
Reference: https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/291%20Word%20Pattern%20II.py
'''
class Solution:
    def wordPatternMatch(self, pattern, str):      
        w2p, p2w = {}, {}   # maintain two dictionaries to map between w(ord) and p(attern)
        return self.helper(pattern, str, w2p, p2w)
    
    def helper(self, pattern, s, w2p, p2w):
        if not pattern and not str: return True
        elif not pattern and str: return False
        elif pattern and not str: return False
        p = pattern[0]
        for j in range(len(s)):
            w = s[:j+1]
            if p not in p2w and w not in w2p:
                w2p[w], p2w[p] = p, w
                if self.helper(pattern[1:], s[j+1:], w2p, p2w):
                    return True
                else:
                    del w2p[w], p2w[p]   # delete the wrong guess
            elif p in p2w and w == p2w[p]:
                if self.helper(pattern[1:], s[j+1:], w2p, p2w):
                    return True
        return False
'''
recursion carried out through index
Reference: https://www.cnblogs.com/lightwindy/p/9736251.html
'''
class Solution:
    def wordPatternMatch(self, pattern, str):
        if not pattern and not str: return True
        if (not pattern and str) or (pattern and not str): return False
        w2p, p2w = {}, {}
        return self.helper(pattern, str, 0, 0, w2p, p2w)
    
    def helper(self, pattern, s, i, j, w2p, p2w):
        isMatch = False
        if i == len(pattern) and j == len(s): isMatch = True
        elif i < len(pattern) and j < len(s):
            p = pattern[i]
            if p not in p2w:
                for k in range(j, len(s)):
                    w = s[j:k+1]
                    if w not in w2p:
                        w2p[w], p2w[p] = p, w
                        isMatch = self.helper(pattern, s, i+1, k+1, w2p, p2w)
                        del w2p[w]; del p2w[p]
                    if isMatch: break            
            else:
                w = p2w[p]
                if w == s[j:j+len(w)]:
                    isMatch = self.helper(pattern, s, i+1, j+len(w), w2p, p2w)
        return isMatch
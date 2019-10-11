'''
Title     : 44. Wildcard Matching
Problem   : https://leetcode.com/problems/wildcard-matching/description/
'''
'''
DP solution adapted from the 10. solution
Reference: https://leetcode.com/problems/wildcard-matching/discuss/256025/Python-DP-with-illustration
'''
class Solution(object):
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        dp = [[False]*(lp+1) for _ in range(ls+1)]   # dp[i][j] = True means p[:j] matches s[:i]
        dp[0][0] = True
        for j in range(1, lp+1):
            if p[j-1] != '*':
                break   # nothing to match till the first non-'*' character in p
            else:
                dp[0][j] = True
        for i in range(1, ls+1):
            for j in range(1, lp+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='?')
                else:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]   # since * can be any sequence (e.g. 'ab' match with '*') no need to check s[i-1], again dp[i-1][j] is to include p[:j-1] == '' case
        return dp[-1][-1]
'''
O(1) iterative solution scanning through the pattern one character by one character, use a variable 'prevMatched' to keep track of previous '*' position
because we may need to go back to it for including additional s characters that are not matched by subsequent p characters
Reference: https://leetcode.com/problems/wildcard-matching/discuss/17897/14-line-Python-solution-beats-78.82
'''
class Solution(object):
    def isMatch(self, s, p):
        if not p: return not s
        ls, lp = len(s), len(p)
        i, j = 0, 0
        startMatching, prevMatched = 0, -1
        while i < ls:
            if j < lp and (p[j]=='?' or p[j]==s[i]):
                i += 1
                j += 1
            elif j < lp and p[j]=='*':
                startMatching, prevMatched = i, j
                j += 1
            elif prevMatched >= 0:
                i, startMatching = startMatching, startMatching + 1
                j = prevMatched + 1   # p[j] != s[i] or '?' or '*' so have to use the previous '*' to cover s[i]
            else:
                return False
        while j < lp and p[j] == '*':
            j += 1
        return j == lp
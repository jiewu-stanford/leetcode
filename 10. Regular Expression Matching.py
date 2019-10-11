'''
Title     : 10. Regular Expression Matching
Problem   : https://leetcode.com/problems/regular-expression-matching/description/
'''
'''
DP solution, two indices but not the conventional 2D, one for the string and one for the pattern
Reference: https://leetcode.com/problems/regular-expression-matching/discuss/168534/Python-short-mem-search-beat-99
'''
class Solution(object):
    def isMatch(self, s, p):
        ls, lp = len(s), len(p)
        dp = [[False]*(lp+1) for _ in range(ls+1)]   # dp[i][j] = True means p[:j] matches s[:i]
        dp[0][0] = True
        for i in range(ls+1):
            for j in range(1, lp+1):
                if p[j-1] != '*':
                    dp[i][j] = i>=1 and dp[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                    dp[i][j] =  ( j>=2 and dp[i][j-2] ) or \
                                ( i>=1 and dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.') )   # since * can be 0 p[j-2:j] can be null thus match s[:i] with p[:j-2], match s[:i-1] with p[:j] instead of p[:j-2] because the latter may be empty e.g. s = 'aa' vs. p = 'a*'
        return dp[-1][-1]

''' recursive solution with memory, ibid. '''
class Solution(object):
    def isMatch(self, s, p):
        if not p: return not s
        self.memo = {}
        if (s, p) in self.memo: return self.memo[(s, p)]
        res = False
        if len(p) > 1 and p[1] == '*':
            res = self.isMatch(s, p[2:]) or \
                (s!='' and (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:], p))   # cannot swap s[0]==p[0] and s[1:] match p otherwise TLE, match s[1:] with p instead of p[2:] again because the latter may be empty
        else:
            res = s!='' and (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:], p[1:])
        self.memo[(s, p)] = res
        return res
'''
Title     : 91. Decode Ways
Problem   : https://leetcode.com/problems/decode-ways/description/
'''
'''
1D DP solution, just need to be careful about whether to go back one digit dp[i-1] or two digits dp[i-2]
Reference: https://leetcode.com/problems/decode-ways/discuss/30529/Readable-Python-DP-Solution
'''
class Solution(object):
    def numDecodings(self, s):
        if not s: return 1
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 1 if s[0]!='0' else 0
        
        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i - 1]
            if s[i-2] != '0' and int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
'''
recursive solution checking single digit or double digit explicitly, TLE though
Reference: https://leetcode.com/problems/decode-ways/discuss/30382/Python-recursive-and-DP-solution
'''
class Solution(object):
    def numDecodings(self, s):
        if not s: return 1
        if s[0] == '0': return 0
        if self.isDoubleDigit(s[:2]):
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])
        else:
            return self.numDecodings(s[1:])

    def isDoubleDigit(self, num):
        return len(num)==2 and 9 < int(num) < 27
'''
use recursive helper function with memo to overcome TLE
Reference: https://leetcode.com/problems/decode-ways/discuss/240637/Python-solution
'''
class Solution(object):
    def numDecodings(self, s):
        def helper(i):
            if i in d: return d[i]
            if i >= len(s): return 1
            res = 0
            if 1 <= int(s[i]) <= 9:
                res += helper(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                res += helper(i+2)
            d[i] = res
            return res

        d = {}
        return helper(0) if s else 1
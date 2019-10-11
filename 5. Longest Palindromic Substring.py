'''
Title     : 5. Longest Palindromic Substring
Problem   : https://leetcode.com/problems/longest-palindromic-substring/
'''
'''
2D DP solution, dp[i][j] = True means s[i:j+1] is a valid palindrome
Reference: https://leetcode.com/problems/longest-palindromic-substring/discuss/121496/Python-DP-solution
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, max_len, n = '', 0, len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            res = s[i]
            max_len = 1
            
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = s[i:i+2]
                max_len = 2
                
        for j in range(n):
            for i in range(0, j-1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if max_len < j - i + 1:
                        res = s[i:j+1]
                        max_len = j - i + 1
        return res
'''
more intuitive expansion approach
Reference: https://github.com/Garvit244/Leetcode/blob/master/1-100q/05.py
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s, l, r):
            while 0 <= l and r < len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            even_len = expand(s, i, i+1)
            odd_len = expand(s, i, i)
            length = max(even_len, odd_len)
            if length > end - start:
                start = i - (length-1) // 2
                end = i + length // 2
                
        return s[start:end+1]
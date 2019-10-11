'''
Title     : 159. Longest Substring with At Most Two Distinct Characters ($$$)
Problem   : https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
          : https://www.lintcode.com/problem/longest-substring-with-at-most-two-distinct-characters/description
'''
'''
brute force comparison without counter recording characters' latest position/number of repetition
Reference: https://blog.csdn.net/zhangpeterx/article/details/100051285
'''
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s: return 0
        start, prevstart, res = -1, 0, 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if s[i] != s[start] and start > -1:
                    res = max(res, i-prevstart)
                    prevstart = start + 1
                start = i - 1   # since s[i] != s[i-1] we already found two distinct characters
        return max(res, len(s)-prevstart)   # do not forget to compare with the last segment
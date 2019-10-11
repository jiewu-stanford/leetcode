'''
Title     : 3. Longest Substring Without Repeating Characters
Problem   : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
'''
one-pointer approach
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1781/Python-solution-with-comments
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        d, res, start = {}, 0, 0
        for i, c in enumerate(s):
            if c in d:
                res = max(res, i-start)
                start = max(start, d[c]+1)   # start = d[c] + 1 would mistakingly include other repeated characters, e.g. d['a'] = 0 in 'abba' thus should use max() to prevent start from going back
            d[c] = i
        return max(res, len(s)-start)   # do not forget to compare with the last non-repetitive segment
'''
two-pointer approach
Reference: https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/211683/Python-3-Clean-and-Correct
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        chars, res, l, r = set(), 0, 0, 0
        while l < len(s) and r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                res = max(res, r-l)
            else:
                chars.remove(s[l])
                l += 1
        return res
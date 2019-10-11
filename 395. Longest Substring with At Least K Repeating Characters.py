'''
Title     : 395. Longest Substring with At Least K Repeating Characters
Problem   : https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
'''
'''
recursive solution, the trick is to split according to the characters which is not repeated enough times and then continue the search on individual segments
Reference: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87768/4-lines-Python
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
'''
iterative divide-and-conquer solution spelling out the .split() and recursive step explicitly
Reference: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/87799/Python-56ms-solution
'''
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        count = collections.Counter(s)
        chars = set([c for c in count if count[c] < k])
        if not chars: return len(s)
        
        start, intervals = 0, []
        while start < len(s):
            c = s[start]
            if c not in chars:
                end = start
                while end < len(s):
                    if s[end] not in chars: end += 1
                    else: break
                intervals.append([start, end])
                start = end
            else:
                start += 1
                
        res = 0
        for i, j in intervals:
            res = max(res, self.longestSubstring(s[i:j], k))
        return res
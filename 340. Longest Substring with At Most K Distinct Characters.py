'''
Title     : 340. Longest Substring with At Most K Distinct Characters ($$$)
Problem   : https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
          : https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/description
'''
'''
user a dictionary to record distinct characters and their latest position
Reference: http://www.voidcn.com/article/p-dotdzqhl-bqe.html
'''
class Solution: 
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s: return 0
        res, start, d = 0, 0, dict()
        for i, c in enumerate(s):
            d[c] = i
            while len(d) > k:
                start = min(d.values())
                del d[s[start]]
                start += 1
            res = max(res, i-start+1)
        return res
'''
use a counter to record the number of distinct characters instead of using a dictionary to record the previous position
Reference: https://www.cnblogs.com/lightwindy/p/8537211.html
'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s: return 0
        res, start, count, visited = 0, 0, 0, [0 for _ in range(256)]   # convert to ASCII to speed up comparison
        for i, c in enumerate(s):
            if visited[ord(c)] == 0: count += 1
            visited[ord(c)] += 1
            while count > k:
                visited[ord(s[start])] -= 1
                if visited[ord(s[start])] == 0: count -= 1
                start += 1
            res = max(res, i-start+1)
        return res
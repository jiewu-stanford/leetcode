'''
Title     : 11. Container With Most Water
Problem   : https://leetcode.com/problems/container-with-most-water/description/
'''
''' Reference: https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms '''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        while l < r:
            width = r - l
            if height[l] < height[r]:
                res = max(res, height[l]*width)
                l += 1   # move to right to see if higher left bar exists
            else:
                res = max(res, height[r]*width)
                r -= 1   # move to left to see if higher right bar exists
        return res
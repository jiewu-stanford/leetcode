'''
Title     : 209. Minimum Size Subarray Sum
Problem   : https://leetcode.com/problems/minimum-size-subarray-sum/
'''
''' Reference: https://leetcode.com/problems/minimum-size-subarray-sum/discuss/59247/Python-easy-to-understand-solution-with-comments. '''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cumsum = l = r = 0
        L = len(nums)
        res = L + 1
        while r < L:
            cumsum += nums[r]
            while cumsum >= s:
                res = min(res, r - l + 1)
                cumsum -= nums[l]
                l += 1
            r += 1
        return res if res <= L else 0
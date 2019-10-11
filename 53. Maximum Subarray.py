'''
Title     : 53. Maximum Subarray
Problem   : https://leetcode.com/problems/maximum-subarray/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        cumsum = maxsum = nums[0]
        for num in nums[1:]:
            cumsum = max(cumsum+num, num)
            maxsum = max(maxsum, cumsum)
        return maxsum
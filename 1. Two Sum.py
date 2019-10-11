'''
Title     : 1. Two Sum
Problem   : https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2: return []
        d = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in d:
                return [i, d[diff]]   # [the second of the pair, the first of the pair]
            else:
                d[val] = i
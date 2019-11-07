'''
Title     : 485. Max Consecutive Ones
Problem   : https://leetcode.com/problems/max-consecutive-ones/
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, res = 0, 0
        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0
        return res
'''
Title     : 268. Missing Number
Problem   : https://leetcode.com/problems/missing-number/description/
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)   # n*(n+1)//2 is the arithmetic sequence sum
'''
bit manipulation, using XOR to eliminate all repeated numbers (one from nums, one from indices), directly adapted from the 136. solution
Reference: https://leetcode.com/problems/missing-number/discuss/70094/Python-O(n)-time-O(1)-space-solutions
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        for n in nums:
            res ^= n
        return res
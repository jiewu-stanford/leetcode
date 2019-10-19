'''
Title     : 136. Single Number
Problem   : https://leetcode.com/problems/single-number/
'''
''' use set() to extract distinct numbers '''
class Solution(object):
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)

''' use Counter() to count numbers '''
from collections import Counter
class Solution(object):
    def singleNumber(self, nums):
        counts = Counter(nums)
        for val, freq in counts.items():
            if freq == 1:
                return val

''' use dict() to count numbers '''
class Solution(object):
    def singleNumber(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for val, freq in d.items():
            if freq == 1:
                return val
'''
use bitwise xor operation
Reference: https://leetcode.com/problems/single-number/discuss/43000/Python-different-solutions.
'''
class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res

''' use bitwise xor operation and reduce(), ibid. '''
from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x ^ y, nums)   # return reduce(lambda x, y: x ^ y, nums, 0) is also OK
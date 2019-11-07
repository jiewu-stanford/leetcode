'''
Title     : 414. Third Maximum Number
Problem   : https://leetcode.com/problems/third-maximum-number/
'''
''' Reference: https://leetcode.com/problems/third-maximum-number/discuss/90207/Intuitive-and-Short-Python-solution '''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = -float('inf')
        for n in nums:
            if n in (a, b, c): continue
            if n > a: n, a = a, n
            if n > b: n, b = b, n
            if n > c: n, c = c, n
        return a if c == -float('inf') else c

''' Reference: https://leetcode.com/problems/third-maximum-number/discuss/90201/A-python-amusing-solution-which-actually-beats-98... '''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]
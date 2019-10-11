'''
Title     : 303. Range Sum Query - Immutable
Problem   : https://leetcode.com/problems/range-sum-query-immutable/description/
'''
class NumArray(object):

    def __init__(self, nums):
        self.cumsum = [0]
        for num in nums:
            self.cumsum += self.cumsum[-1] + num,   # , to convert non-iterable int to iterable tuple

    def sumRange(self, i, j):
        return self.cumsum[j+1] - self.cumsum[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
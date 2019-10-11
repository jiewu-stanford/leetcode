'''
Title     : 307. Range Sum Query - Mutable
Problem   : https://leetcode.com/problems/range-sum-query-mutable/description/
'''
class NumArray(object):

    def __init__(self, nums):
        self.nums = nums

    def update(self, i, val):
        self.nums[i] = val

    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])
'''
adapt the 303. solution and use binary indexed tree (BIT) to store the prefix sums so as to speed up the cumsum
Reference: https://leetcode.com/problems/range-sum-query-mutable/discuss/75730/148ms-Python-solution-Binary-Indexed-Tree
'''
class NumArray(object):

    def __init__(self, nums):
        self.nums = [0] * len(nums)
        self.BIT = [0] * (len(nums)+1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, i, val):
        dif, self.nums[i] = val - self.nums[i], val
        i += 1   # BIT node index starts from 1
        while i < len(self.BIT):
            self.BIT[i] += dif
            i += (i & -i)   # to next node

    def cumsum(self, k):
        res = 0
        while k:
            res += self.BIT[k]
            k -= (k & -k)   # to parent node
        return res

    def sumRange(self, i, j):
        return self.cumsum(j+1) - self.cumsum(i)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
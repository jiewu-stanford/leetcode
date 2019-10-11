'''
Title     : 213. House Robber II
Problem   : https://leetcode.com/problems/house-robber-ii/
'''
'''
decompose into two interlacing the 198. problem
Reference: https://leetcode.com/problems/house-robber-ii/discuss/230657/Python-solution
Reference: https://leetcode.com/problems/house-robber-ii/discuss/164055/Python-or-tm
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) < 3: return max(nums)
        return max(self.rob_noncyclic(nums[1:]), self.rob_noncyclic(nums[:-1]))

    def rob_noncyclic(self, nums: List[int]) -> int:
        nums = [0,0] + nums
        for i, n in enumerate(nums[2:], 2):
            nums[i] = max(nums[i-2]+n, nums[i-1])
        return nums[-1]
'''
still use the decomposition + concise implementation of the 198. solution without using helper function
Reference: https://leetcode.com/problems/house-robber-ii/discuss/59979/My-Python-Solution
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        elif n < 4: return max(nums)
        first, second = 0, 0   # keep track of both first max and second max
        for i in nums[:-1]:
            first, second = second, max(first+i, second)
        res = second
        first, second = 0, 0
        for i in nums[1:]:
            first, second = second, max(first+i, second)
        return max(res, second)
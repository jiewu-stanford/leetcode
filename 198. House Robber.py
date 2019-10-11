'''
Title     : 198. House Robber
Problem   : https://leetcode.com/problems/house-robber/
'''
'''
recursive solution, similar to binary search, simple but slow
Reference: https://leetcode.com/problems/house-robber/discuss/55853/Python-simple-solution
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1:
            return nums[0]
        else:
            k = n // 2
            return max(self.rob(nums[0:k])+self.rob(nums[k+1:]), self.rob(nums[0:k-1])+self.rob(nums[k:]))
'''
clever enumeration with padding
Reference: https://leetcode.com/problems/house-robber/discuss/55868/3-line-python-solution
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0,0] + nums   # prepending 0's
        for i, n in enumerate(nums[2:], 2):
            nums[i] = max(nums[i-2]+n, nums[i-1])   # change nums directly
        return nums[-1]
'''
1D DP solution
Reference: https://leetcode.com/problems/house-robber/discuss/55933/Python-simple-DP-solution-O(n)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n < 3: return max(nums)
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]
'''
Title     : 377. Combination Sum IV
Problem   : https://leetcode.com/problems/combination-sum-iv/
'''
'''
recursive solution adapted from the 39. solution, the only difference is that startindex = 0 always, albeit TLE
Reference: https://leetcode.com/problems/combination-sum-iv/discuss/85145/Python-DP-and-DFS-Solution
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = []
        self.helper(nums, target, [], res)
        return len(res)

    def helper(self, nums, k, acc, res):
        if k < 0:
            return
        elif k == 0:
            res.append(acc)
            return
        else:
            for i in range(0, len(nums)):   # repetition is allowed that always start searching from beginning
                self.helper(nums, k-nums[i], acc+[nums[i]], res)
'''
dynamic programming solution, ibid. and
Reference: https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num > i:
                    break
                else:
                    dp[i] += dp[i-num]
        return dp[target]
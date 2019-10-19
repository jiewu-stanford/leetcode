'''
Title     : 90. Subsets II
Problem   : https://leetcode.com/problems/subsets-ii/
'''
''' 
note that it is very cumbersome to produce duplicate power set first and then find the distinct elements
because list and set are mutable thus are not hashable therefore lists of lists/sets cannot be converted to sets
the fastest is to adapt the 78. recursion + loop solution for no duplicates (sort + duplicate checking)
Reference: https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS)
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        nums.sort()   # now needs sorting, for checking nums[i-1] == nums[i] below
        self.helper(nums, 0, [], res)   # cannot pass nums.sort() here
        return res

    def helper(self, nums, startindex, acc, res):
        res.append(acc)
        for i in range(startindex, len(nums)):
            if i > startindex and nums[i-1] == nums[i]:
                continue
            self.helper(nums, i+1, acc+[nums[i]], res)
'''
iterative solution, direct implementation of step-by-step power set building but use Counter() to add numbers by cohort (group of identical numbers) instead of individually
because individual addition leads to duplicate e.g. pset of [1, 2, 2] built from pset of [1,2] we get [1] + [2] = [1, 2] and [1, 2] + [] = [1, 2]
Reference: https://leetcode.com/problems/subsets-ii/discuss/171626/Python-solution
'''
from collections import Counter
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res, counts = [[]], Counter(nums)
        for key, val in counts.items():
            tmp = []
            for subset in res:
                for i in range(1, val+1):
                    tmp.append(subset+[key]*i)
            res += tmp
        return res
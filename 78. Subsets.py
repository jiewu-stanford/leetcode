'''
Title     : 78. Subsets
Problem   : https://leetcode.com/problems/subsets/
'''
'''
iterative solution, direct implementation of step-by-step power set building
Reference: https://leetcode.com/problems/subsets/discuss/216279/Python-solution
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = [[]]
        for n in nums:
            for i in range(len(res)):
                res.append(res[i]+[n])
        return res
'''
recursion + loop solution
Reference: https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        self.helper(nums, 0, [], res)
        return res

    def helper(self, nums, startindex, acc, res):
        res.append(acc)
        for i in range(startindex, len(nums)):
            self.helper(nums, i+1, acc+[nums[i]], res)

''' use the fact that the number of power sets = 2**len(nums), ibid. '''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []        
        res, n = [], len(nums)
        for i in range(1 << n):
            tmp = []
            for j in range(n):
                if i & (1<<j):   # bitwise AND, requires binary conversion
                    tmp.append(nums[j])
            res.append(tmp)
        return res

''' use reduce() + different types of x and y, ibid. '''
from functools import reduce
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda combs, elem: combs + [comb + [elem] for comb in combs], nums, [[]])

''' use combinations() + two generators, ibid. '''
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [comb for n in range(len(nums)+1) for comb in combinations(nums, n)]
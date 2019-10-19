'''
Title     : 77. Combinations
Problem   : https://leetcode.com/problems/combinations/
'''
'''
recursion based on loop
Reference: https://leetcode.com/problems/combinations/discuss/26990/Easy-to-understand-Python-solution-with-comments
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(range(1,n+1), k, 0, [], res)
        return res

    def helper(self, nums, k, startindex, acc, res):
        if k == 0:
            res.append(acc)
        elif k <= len(nums):
            for i in range(startindex, len(nums)):
                self.helper(nums, k-1, i+1, acc+[nums[i]], res)
'''
recursion based on mathematical induction
Reference: https://leetcode.com/problems/combinations/discuss/170834/Python-solution
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0: return [[]]
        return [c + [i] for i in range(n,k-1,-1) for c in self.combine(i-1,k-1)]   # range(n,k-1,-1) = [n,n-1,...,k]
'''
iterative solution, two iterators: (1) previous combinations (2) remaining integers
Reference: https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        for _ in range(k):
            # a self-built (via appendleft [i]+) hypothesis, all c's in res are ascending hence range(1, c[0]) represents remaining integers
            res = [[i] + c for c in res for i in range(1, c[0] if c else n+1)]
        return res

''' reduce() solution, reduce() is simply a concise way to implement the loop above '''
from functools import reduce
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [[]]
        return reduce(lambda combs, _: [[i] + c for c in combs for i in range(1, c[0] if c else n+1)], range(k), res)
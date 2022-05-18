'''
Title     : 216. Combination Sum III
Problem   : https://leetcode.com/problems/combination-sum-iii/
'''
'''
recursive solution, combination of the 77. and 40. solution
Reference: https://leetcode.com/problems/combination-sum-iii/discuss/60805/Easy-to-understand-Python-solution-(backtracking)
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.helper(range(1,10), k, n, 0, [], res)
        return res
    
    def helper(self, nums, k, target, startindex, acc, res):
        if k < 0 or target < 0:
            return
        elif k == 0 and target == 0:
            res.append(acc)
            return
        else:
            for i in range(startindex, len(nums)):
                self.helper(nums, k-1, target-nums[i], i+1, acc+[nums[i]], res)
'''
filter the result of the 77. iterative solution
Reference: https://leetcode.com/problems/combination-sum-iii/discuss/60624/Clean-167-liners-(AC)
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = [[]]
        for _ in range(k):
            res = [[i] + c for c in res for i in range(1, c[0] if c else 10)]
        return [c for c in res if sum(c)==n]

''' reduce() solution, reduce() is simply a concise way to implement the loop '''
from functools import reduce
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = reduce(lambda combs,_: [[i] + c for c in combs for i in range(1, c[0] if c else 10)], range(k), [[]])
        return [c for c in res if sum(c)==n]
'''
step-by-step search through
Reference: https://leetcode.com/problems/combination-sum-iii/discuss/60833/Python-40ms-iterative-solution
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = [[0]]
        for i in reversed(range(k)):
            level = []
            for c in res:
                total = c.pop()
                startindex = c[-1] if c else 0
                for j in range(startindex+1, 10):
                    comb = c + [j]
                    if total + j*(i+1) > n:   # min sum of the rest
                        break
                    elif i == 0:
                        if total + j == n:
                            level.append(comb)
                    else:
                        comb.append(total+j)
                        level.append(comb)
            res = level
        return res
'''
Title     : 39. Combination Sum
Problem   : https://leetcode.com/problems/combination-sum/
'''
'''
directly adapte the 78. recursion + loop solution, backtrack upon reducing target instead of incrementing startindex
Reference: https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(candidates, target, 0, [], res)
        return res

    def helper(self, nums, target, startindex, acc, res):
        if target < 0:
            return
        elif target == 0:
            res.append(acc)
            return
        else:
            for i in range(startindex, len(nums)):
                self.helper(nums, target-nums[i], i, acc+[nums[i]], res)
'''
iteration solution
Reference: https://leetcode.com/problems/combination-sum/discuss/16814/Simple-and-fast-DFS-solution-python-AC-98ms
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()   # for total to approach target from below and break if overshooted
        res, stack = [], [(0, 0, [])]
        while stack:
            total, startindex, combs = stack.pop()
            if total == target:
                res.append(combs)
            else:
                for i in range(startindex, len(candidates)):
                    newt = total + candidates[i]
                    if newt > target:
                        break
                    else:
                        stack.append((newt, i, combs+[candidates[i]]))
        return res
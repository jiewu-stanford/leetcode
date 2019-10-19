'''
Title     : 40. Combination Sum II
Problem   : https://leetcode.com/problems/combination-sum-ii/
'''
'''
directly adapted from the 39. solution, just add sort + duplicate checking
Reference: https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution.
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()   # need for checking repetition candidates[i-1] == candidates[i] below
        self.helper(candidates, target, 0, [], res)
        return res

    def helper(self, candidates, target, startindex, acc, res):
        if target < 0:
            return
        elif target == 0:
            res.append(acc)
            return
        else:
            for i in range(startindex, len(candidates)):
                if i > startindex and candidates[i-1] == candidates[i]:
                    continue
                self.helper(candidates, target-candidates[i], i+1, acc+[candidates[i]], res)   # i+1 since can only use once (vs. the 39. solution)
'''
similary we can also modify the 39. iteration solution accordingly
Reference: https://leetcode.com/problems/combination-sum-ii/discuss/17019/Python-iterative-solution
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, stack = [], [(0, 0, [])]
        while stack:
            total, startindex, res = stack.pop()
            if total == target:
                result.append(res)
            else:
                for i in range(startindex, len(candidates)):
                    if (i > startindex) and (candidates[i-1] == candidates[i]):
                        continue
                    t = total + candidates[i]
                    if t > target:
                        break
                    else:
                        stack.append((t, i+1, res+[candidates[i]]))
        return result
'''
dynamical programming solution (1D)
Reference: https://leetcode.com/problems/combination-sum-ii/discuss/16870/DP-solution-in-Python
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set() for _ in range(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num-1, -1):
                for comb in dp[t-num]:
                    dp[t].add(comb + (num,))
        return list(dp[-1])
'''
Title     : 282. Expression Add Operators
Problem   : https://leetcode.com/problems/expression-add-operators/description/
'''
'''
DFS solution with recursive helper function
Reference: https://leetcode.com/problems/expression-add-operators/discuss/128460/simple-Python-DFS-that-beats-100
'''
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []
        res = []

        def helper(startindex, expr, val, prev):
            if val == target and startindex == len(num):
                res.append(expr)
                return
            # if startindex < len(num) and max(1,abs(prev))*(int(num[startindex:])) < abs(target-val):   # target not reachable
                return
            for i in range(startindex, len(num)):
                curr = num[startindex:i+1]
                if len(curr) != len(str(int(curr))):   # prevent '00','01',... treated as one number
                    break
                if startindex == 0:
                    helper(i+1, curr, int(curr), int(curr))
                else:
                    helper(i+1, expr+'+'+curr, val+int(curr), int(curr))
                    helper(i+1, expr+'-'+curr, val-int(curr), -int(curr))   # -curr is interpreted as +(-curr)
                    helper(i+1, expr+'*'+curr, val-prev+prev*int(curr), prev*int(curr))   # since * has precedence over + we have to roll back +prev
        
        helper(0, '', 0, 0)
        return res
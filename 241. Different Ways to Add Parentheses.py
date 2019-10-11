'''
Title     : 241. Different Ways to Add Parentheses
Problem   : https://leetcode.com/problems/different-ways-to-add-parentheses/description/
'''
'''
recursive solution + list comprehension, key fact to realize is that since we can add parenthesis at will 
we can split input arbitrarily to obtain two meaningful parts for evaluation without worrying about unpaired parenthesis
Reference: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66350/1-11-lines-Python-9-lines-C%2B%2B
'''
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        return [a+b if c=='+' else a-b if c=='-' else a*b   # note the special if...else statement structure
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
'''
the list comprehension is spelled out in the following
Reference: https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-solution-(divide-and-conquer)
'''
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit(): return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                res.extend(a+b if c=='+' else a-b if c=='-' else a*b for a in left for b in right)
        return res
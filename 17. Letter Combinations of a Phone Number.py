'''
Title     : 17. Letter Combinations of a Phone Number
Problem   : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
'''
simple dictionary bookkeeping + double generator
Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8063/Python-solution
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        combs = ['']
        for d in digits:
            combs = [c + q for c in combs for q in dic[d]]
        return combs
'''
again the for loop can be concisely implemented by reduce()
Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8070/One-line-python-solution
'''
from functools import reduce
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        return reduce(lambda combs, d: [c + q for c in combs for q in dic[d]], digits, [''])
'''
recursive solution, directly adapted from the 77. solution
Reference: https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8067/Python-easy-to-understand-backtracking-solution
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        dic = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", '8':"tuv", '9':"wxyz"}
        res = []
        self.helper(digits, dic, 0, '', res)
        return res

    def helper(self, digits, dic, startindex, acc, res):
        if len(acc) == len(digits):
            res.append(acc)
        else:
            for i in range(startindex, len(digits)):
                for j in dic[digits[i]]:
                    self.helper(digits, dic, i+1, acc+j, res)
'''
Title     : 254. Factor Combinations ($$$)
Problem   : https://leetcode.com/problems/factor-combinations/
          : https://www.lintcode.com/problem/factor-combinations/
'''
'''
DFS helper function, O(n^2) time, find all factors and then find their combinations through backtracking, TLE
Reference: http://weihan.online/blog/eugenejw.github.io/_site/2017/10/leetcode-254.html
'''
class Solution:
    def getFactors(self, n):
        if n <= 0: return []
        res = []
        factors = [i for i in range(2,n) if n % i == 0]
        self.helper(n, 2, [], res, factors)
        return res
        
    def helper(self, t, factor, combs, res, factors):
        if t == 1:
            if len(combs) > 0: res.append(combs[:])
            return res
        for f in factors:
            if factor <= f <= t and t % f == 0:
                combs.append(f)
                self.helper(t//f, f, combs, res, factors)
                combs.pop()
'''
simultaneously finding factors and forming combinations, O(nlogn) time, note that binary search for add/subtrace becomes sqrt search for multiplication/division
Reference: https://www.cnblogs.com/lightwindy/p/9363808.html
'''
class Solution:
    def getFactors(self, n):
        if n <= 0: return []
        res, factors = [], []
        self.helper(n, res, factors)
        return res
        
    def helper(self, t, res, factors):
        i = 2 if not factors else factors[-1]   # start from the largest factor < sqrt(n)
        while i <= t//i:
            if t % i == 0:
                factors.append(i)
                factors.append(t//i)
                res.append(list(factors))
                factors.pop()
                self.helper(t//i, res, factors)
                factors.pop()
            i += 1
'''
binary search O(nlogn) with memoization
Reference: https://github.com/criszhou/LeetCode-Python/blob/master/254.%20Factor%20Combinations.py
'''
import math
class Solution:
    factorCache = dict()
    def getFactors(self, n, includeN=False):
        if n <= 0: return []
        if n not in self.factorCache:
            res = [[n]]
            for f in range(2, int(math.sqrt(n))+1):
                if n % f == 0:
                    res.extend(([f]+factors) for factors in self.getFactors(n//f,includeN=True) if factors[0]>=f)   # in ascending order to avoid repetition
            self.factorCache[n] = res
        res = list(self.factorCache[n])
        if not includeN: res.remove([n])
        return res
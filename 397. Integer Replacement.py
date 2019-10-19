'''
Title     : 397. Integer Replacement
Problem   : https://leetcode.com/problems/integer-replacement/description/
'''
'''
recursive solution, straightforward but do not forget the min()
Reference: https://leetcode.com/problems/integer-replacement/discuss/88053/3-Lines-Python-Recursive-AC-Solution
'''
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1: return 0
        if n % 2:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        else:
            return 1 + self.integerReplacement(n//2)
'''
with memoization decorator, see how much it can improve (about 10-fold), not necessary for solving this problem but good to see how decorator works
Reference: https://leetcode.com/problems/integer-replacement/discuss/88057/Python-top-down-approach.-Memoization-saves-hundreds-of-ms-(345ms-greater-36ms)
'''
class memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)   # evaluate f if args are not a key of memo
        return self.memo[args]

@memoize
def helper(n):
        if n == 1: return 0
        if n % 2:
            return 1 + min(helper(n+1), helper(n-1))
        else:
            return 1 + helper(n//2)

class Solution:
    def integerReplacement(self, n: int) -> int:
        return helper(n)
'''
Title     : 306. Additive Number
Problem   : https://leetcode.com/problems/additive-number/
'''
'''
iterative solution, just check all possible additive cases for the first two numbers, the rest can then be inferred from them
Reference: https://leetcode.com/problems/additive-number/discuss/75578/Python-solution
'''
import itertools
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3: return False
        for i, j in itertools.combinations(range(1,n), 2):   # for i, j in itertools.combinations(range(1,n//3*2+1), 2): since need to leave at least 1/3 for the sum
            a, b = num[:i], num[i:j]
            if a != str(int(a)) or b != str(int(b)): continue   # contains leading 0s
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j): break
                j += len(c)
                a, b = b, c
            if j == n: return True
        return False
'''
recursive solution through Fibonacci number sequence generation pattern matching
Reference: https://leetcode.com/problems/additive-number/discuss/75631/Share-a-python-solution-not-that-fast-but-easy-to-understand
'''
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3: return False
        for i in range(n-2):   # for i in range(n//2): since can only be within first half
            for j in range(i+1, n-1):   # for j in range(i+1, n//3*2): since need to leave at least 1/3 for the sum
                a, b = int(num[:i+1]), int(num[i+1:j+1])
                if ((a == 0 and i == 0) or num[0] != '0') and \
                    ((b == 0 and i+1 == j) or num[i+1] != '0') and \
                    self.fibonacciSeq(a, b, len(num)-j-1) == num[j+1:]: return True   # need to check leading 0s
        return False

    def fibonacciSeq(self, a, b, k):
        c = a + b
        res = str(c)
        while len(res) < k:
            a, b = b, c
            c = a + b
            res += str(c)
        return res
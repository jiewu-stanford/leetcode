'''
Title     : 372. Super Pow (XXX)
Problem   : https://leetcode.com/problems/super-pow/
'''
'''
recursive solution based on the math: (1) n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337 (2) if b = m*10 + d, we have a**b == (a**d)*(a**10)**m
Reference: https://leetcode.com/problems/super-pow/discuss/84467/Simple-python-solution-using-recursion
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b: return 1
        return pow(a, b.pop(), 1337) * self.superPow(pow(a, 10, 1337), b)%1337
'''
Fermat theorem + Chinese remainder theorem (XXX)
Reference: https://leetcode.com/problems/super-pow/discuss/84475/Fermat-and-Chinese-Remainder
'''
from functools import reduce
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def mod(p):
            return pow(a, reduce(lambda e, d: (10*e + d) % (p-1), b, 0), p) if a%p else 0
        return (764 * mod(7) + 574 * mod(191)) % 1337
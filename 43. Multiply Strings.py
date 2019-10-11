'''
Title     : 43. Multiply Strings
Problem   : https://leetcode.com/problems/multiply-strings/
'''
from functools import reduce
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        i1 = int(reduce(lambda x, y: 10*x+y, num1.split()))
        i2 = int(reduce(lambda x, y: 10*x+y, num2.split()))
        return str(i1*i2)
'''
Title     : 191. Number of 1 Bits
Problem   : https://leetcode.com/problems/number-of-1-bits/description/
'''
class Solution(object):
    def hammingWeight(self, n):
        res = 0
        while n:
            res += n & 1
            n //= 2
        return res

class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
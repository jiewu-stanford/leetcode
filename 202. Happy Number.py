'''
Title     : 202. Happy Number
Problem   : https://leetcode.com/problems/happy-number/
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            n = sum([int(i)**2 for i in str(n)])   # follow the given recipe for calculating the next number
        return n == 1
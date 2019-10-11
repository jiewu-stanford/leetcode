'''
Title     : 342. Power of Four
Problem   : https://leetcode.com/problems/power-of-four/
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0: return False
        while num % 4 == 0:
            num = num // 4
        return True if num == 1 else False
'''
use the binary representation of 4 = '0b100', count the number of '0' in the representation
Reference: https://leetcode.com/problems/power-of-four/discuss/80645/Python-one-line-clear-solution-without-loop-and-ifelse
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num-1) == 0 and len(bin(num))%2 == 1
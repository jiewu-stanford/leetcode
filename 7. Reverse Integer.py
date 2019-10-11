'''
Title     : 7. Reverse Integer (XXX)
Problem   : https://leetcode.com/problems/reverse-integer/
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = int('-'+str(x)[:0:-1])   # s[:0:-1] = (s[::-1])[:-1]
        return res if abs(res) < 2**31 else 0
'''
single out sign and a fancier use of bit shift approach
Reference: https://leetcode.com/problems/reverse-integer/discuss/4517/Python-two-accepted-solutions
'''
class Solution:
    def reverse(self, x: int) -> int:
        sign = +1 if x >=0 else -1
        res = int(str(sign*x)[::-1])   # sign*x = abs(x)

        if res < (1 << 31):   # 1<<31 = 2**31, more generally x << y = x*(2**y), ref: https://stackoverflow.com/questions/22832615/what-do-and-mean-in-python
            return res*sign
        else:
            return 0
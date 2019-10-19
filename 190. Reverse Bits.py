'''
Title     : 190. Reverse Bits
Problem   : https://leetcode.com/problems/reverse-bits/description/
'''
'''
modify from the 191. solution
Reference: https://leetcode.com/problems/reverse-bits/discuss/54740/Python-AC-with-63ms-3lines
'''
class Solution:
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (n & 1) + (res << 1)   # note that + has precedence over bit manipulation
            n //= 2
        return res
'''
flip bit one by one
Reference: https://leetcode.com/problems/reverse-bits/discuss/54975/Different-Python-solutions
'''
class Solution:
    def reverseBits(self, n):
        bits, i = [0]*32, 0
        while n:
            bits[i] = n % 2
            n //= 2
            i += 1
        res = 0
        for i in range(32):
            res = res*2 + bits[i]
        return res
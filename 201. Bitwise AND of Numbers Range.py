'''
Title     : 201. Bitwise AND of Numbers Range
Problem   : https://leetcode.com/problems/bitwise-and-of-numbers-range/
'''
'''
count the number of '1's which remain 1 throughout the scan from m to n using bitwise xor, padding zeros after them
Reference: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56848/Share-a-simple-four-line-python-solution-using-bit-operation
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n: return m
        zeros = len(bin(m^n)) - 2
        return (n >> zeros) * (2**zeros)
'''
the bitwise AND of the range is keeping the common bits of m and n from left to right until the first bit that they are different, padding zeros for the rest
Reference: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56719/JavaPython-easy-solution-with-explanation
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
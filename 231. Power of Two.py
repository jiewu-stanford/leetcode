'''
Title     : 231. Power of Two
Problem   : https://leetcode.com/problems/super-pow/
'''
'''
bit manipulation: a power of n has a binary representation n = 100...00, thus n - 1 = 011...11 and their bitwise AND yield 000...00
Reference: https://leetcode.com/problems/power-of-two/discuss/64027/Python-one-line-solution
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & n-1)
'''
work directly on the binary representation of n = 100...00, just count how many '1' there are, for a power of 2 there must be only one '1'
Reference: https://leetcode.com/problems/power-of-two/discuss/64062/One-line-python-solution-use-bitcount
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1')==1
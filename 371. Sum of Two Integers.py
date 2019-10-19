'''
Title     : 371. Sum of Two Integers (XXX)
Problem   : https://leetcode.com/problems/sum-of-two-integers/
'''
''' Reference: https://leetcode.com/problems/sum-of-two-integers/discuss/84282/Python-solution-with-no-%22%2B-*%22-completely-bit-manipulation-guaranteed '''
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF   # 32 bits integer max
        MIN = 0x80000000   # 32 bits interger min
        mask = 0xFFFFFFFF   # mask to get last 32 bits
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask    # ^ gets different bits, & gets double 1s, << moves carry
                                                            # if a is negative, get a's 32 bits complement positive first
                                                            # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
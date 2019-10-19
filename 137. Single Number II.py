'''
Title     : 137. Single Number II
Problem   : https://leetcode.com/problems/single-number-ii/description/
'''
'''
directly adapted from the 136. solution
Reference: https://leetcode.com/problems/single-number-ii/discuss/43300/My-simple-python-solution
'''
class Solution(object):
    def singleNumber(self, nums):
        res = 3*sum(set(nums)) - sum(nums)
        return res // 2
'''
bit manipulation, look at bits one by one, sum all numbers at that bit position and take the remainder of % 3
Reference: https://leetcode.com/problems/single-number-ii/discuss/43350/Very-easy-to-understand-Python-code
'''
class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for i in range(32):
            bit = 0
            for num in nums:
                if num & (1 << i):
                    bit += 1
            bit %= 3
            if i != 31:
                res += bit << i
            elif bit == 1:   # find '1' on the bit representing sign i.e. it is a negative number
                res -= 1 << 31
        return res
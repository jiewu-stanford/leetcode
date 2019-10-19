'''
Title     : 260. Single Number III
Problem   : https://leetcode.com/problems/single-number-iii/description/
'''
'''
still use the set() trick as in the 136. solution
Reference: https://leetcode.com/problems/single-number-iii/discuss/68907/Naive-Python
'''
class Solution(object):
    def singleNumber(self, nums):
        once, twice = set(), set()
        for num in nums:
            if num not in once:
                once.add(num)
            else:
                twice.add(num)
        return list(once - twice)
'''
bit manipulation, use the i & -i trick of locating the node index in BIT to locate the last '1' bit in the binary form of xor = a ^ b, use this to distinguish a and b (recall the truth table of XOR)
Reference: http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/
Reference: https://stackoverflow.com/questions/15395317/meaning-of-bitwise-and-of-a-positive-and-negative-number
'''
class Solution(object):
    def singleNumber(self, nums):
        xor = reduce(lambda x, y: x ^ y, nums)
        lastOne = xor & -xor
        a = b = 0
        for num in nums:
            if num & lastOne:
                a ^= num
            else:
                b ^= num
        return [a, b]
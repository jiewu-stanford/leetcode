'''
Title     : 66. Plus One
Problem   : https://leetcode.com/problems/plus-one/
'''
'''
step-by-step direct implementation of arithmetic using divmod()
https://leetcode.com/problems/plus-one/discuss/159471/Python-solution
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)
            if carry == 0:
                return digits
        return [1]+digits   # there is carry in the leading digit thus appendleft a '1'
'''
whole number conversion via reduce() function
Reference: https://leetcode.com/problems/plus-one/discuss/24378/Python-easy-to-follow-solutions
'''
from functools import reduce
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = reduce(lambda x, y: 10*x+y, digits) + 1
        return map(int, list(str(num)))
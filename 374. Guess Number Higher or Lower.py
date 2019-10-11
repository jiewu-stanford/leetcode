'''
Title     : 374. Guess Number Higher or Lower
Problem   : https://leetcode.com/problems/guess-number-higher-or-lower/
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num): pass
''' Reference: https://leetcode.com/problems/guess-number-higher-or-lower/discuss/84708/Standard-binary-search-in-Python '''
class Solution(object):
    def guessNumber(self, n):
        low, high = 1, n
        if guess(low) == 0: return low
        if guess(high) == 0: return high
        while low < high:
            mid = (low + high) // 2
            res = guess(mid)
            if res < 0:
                high = mid
            elif res > 0:
                low = mid
            else:
                return mid
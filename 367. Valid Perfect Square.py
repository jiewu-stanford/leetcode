'''
Title     : 367. Valid Perfect Square
Problem   : https://leetcode.com/problems/valid-perfect-square/
'''
''' binary search again, compare with the 69. Sqrt(x) '''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            if num == mid * mid:
                return True
            elif num < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
        return False
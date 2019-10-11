'''
Title     : 69. Sqrt(x)
Problem   : https://leetcode.com/problems/sqrtx/
'''
'''
binary search
Reference: https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn)).
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid*mid:
                r = mid - 1
            else:
                l = mid + 1
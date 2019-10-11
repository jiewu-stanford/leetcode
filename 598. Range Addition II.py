'''
Title     : 598. Range Addition II
Problem   : https://leetcode.com/problems/range-addition-ii/
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m * n
        x, y = zip(*ops)
        return min(x) * min(y)

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for a, b in ops:
            m = min(m, a); n = min(n, b)
        return m * n
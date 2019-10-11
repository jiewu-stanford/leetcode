'''
Title     : 52. N-Queens II
Problem   : https://leetcode.com/problems/n-queens-ii/description/
'''
''' simply change what to return in the 51. solution '''
class Solution:
    def totalNQueens(self, n: int) -> int:
        def helper(queens, ijDiff, ijSum):
            p = len(queens)
            if p == n:
                self.res += 1   # res.append(queens) in the 51. solution
                return None
            for q in range(n):
                if q not in queens and p-q not in ijDiff and p+q not in ijSum:
                    helper(queens+[q], ijDiff+[p-q], ijSum+[p+q])
        self.res = 0
        helper([], [], [])
        return self.res
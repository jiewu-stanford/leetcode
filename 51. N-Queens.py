'''
Title     : 51. N-Queens
Problem   : https://leetcode.com/problems/n-queens/
'''
'''
DFS solution, the depth handles one safety rule: no two queens are placed in the same row (hence row index omitted)
whereas the queen label handles one safety rule: no two queens are in the same column (treat it as column index), hence we only need to check
(1) not in the same diagonal i.e. i - j != p - q and (2) not in the same anti-diagonal i.e. i + j != p + q (recall diagonal is y = x - b, antidiagonal is y = -x + a)
Reference: https://leetcode.com/problems/n-queens/discuss/19810/Fast-short-and-easy-to-understand-python-solution-11-lines-76ms
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(queens, ijDiff, ijSum):
            p = len(queens)   # depth, row index
            if p == n:
                res.append(queens)
                return None
            for q in range(n):   # label, column index
                if q not in queens and p-q not in ijDiff and p+q not in ijSum:
                    helper(queens+[q], ijDiff+[p-q], ijSum+[p+q])
        res = []
        helper([], [], [])
        return [['.'*j + 'Q' + '.'*(n-j-1) for j in solution] for solution in res]
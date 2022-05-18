'''
Title     : 289. Game of Life
Problem   : https://leetcode.com/problems/game-of-life/description/
'''
'''
iterative solution implementing the rules step-by-step, using 4 instead of 2 states
Reference: https://leetcode.com/problems/game-of-life/discuss/73229/Python-solution-easy-to-understand
'''
import itertools
class Solution:
    """ 0 = now dead and -> dead,   1 = now live and -> live,   2 = now dead but -> live,   3 = now live but -> dead """
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        def isAlive(r, c):
            return r not in (-1, rows) and c not in (-1, cols) and board[r][c] in (1,2)

        for r, c in itertools.product(range(rows), range(cols)):
            liveNeighbor = sum([isAlive(i,j) for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1),(r-1,c-1),(r+1,c+1),(r-1,c+1),(r+1,c-1)]])
            if board[r][c] == 1:
                board[r][c] = 2 if (liveNeighbor < 2 or liveNeighbor > 3) else 1
            else:
                board[r][c] = 3 if (liveNeighbor == 3) else 0

        for r, c in itertools.product(range(rows), range(cols)):
            board[r][c] = 1 if board[r][c] in (1, 3) else 0
'''
Title     : 36. Valid Sudoku
Problem   : https://leetcode.com/problems/valid-sudoku/description/
'''
'''
set up helper function to check each condition
Reference: https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution
'''
class Solution(object):
    def isValidSudoku(self, board):
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board)

    def isValidRow(self, board):
        for row in board:
            if not self.isValid(row): return False
        return True

    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isValid(col): return False
        return True

    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.isValid(square): return False
        return True

    def isValid(self, nums):
        res = [num for num in nums if num != '.']
        return len(res) == len(set(res))
'''
iterative solution without helper function, traverse and check
Reference: https://leetcode.com/problems/valid-sudoku/discuss/160227/Python-solution
'''
class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                a = i // 3; b = j // 3
                num = board[i][j]
                if num in rows[i] or num in cols[j] or num in squares[a][b]:
                    return False
                else:
                    rows[i].add(num);   cols[j].add(num);   squares[a][b].add(num)
        return True
'''
the three set() can be combined into one
Reference: https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
'''
class Solution(object):
    def isValidSudoku(self, board):
        seen = sum(([(c, i), (j, c), (i//3, j//3, c)]   # (c, i) vs. (j, c) to avoid (i, c) == (j, c)
                    for i in range(9) for j in range(9)
                    for c in [board[i][j]] if c != '.'), [])   # sum(array, []) is to flatten out the array into 1D list
        return len(seen) == len(set(seen))
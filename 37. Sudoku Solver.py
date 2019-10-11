'''
Title     : 37. Sudoku Solver
Problem   : https://leetcode.com/problems/sudoku-solver/description/
'''
'''
DFS solution adapted from the 36. iterative solution carrying out checking and assignment simultaneously through recursive helper function
Reference: https://leetcode.com/problems/sudoku-solver/discuss/140837/Python-very-simple-backtracking-solution-using-dictionaries-and-queue-~100-ms-beats-~90
'''
from collections import defaultdict, deque
class Solution(object):
    def solveSudoku(self, board):
        rows, cols, squares, unassigned = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j]);   cols[j].add(board[i][j]);   squares[(i//3,j//3)].add(board[i][j])
                else:
                    unassigned.append((i, j))

        def helper():
            if not unassigned: return True
            i, j = unassigned[0]
            for digit in {'1','2','3','4','5','6','7','8','9'}:
                if digit not in rows[i] and digit not in cols[j] and digit not in squares[(i//3,j//3)]:
                    board[i][j] = digit
                    rows[i].add(digit);   cols[j].add(digit);   squares[(i//3,j//3)].add(digit)
                    unassigned.popleft()
                    if helper():
                        return True
                    else:   # do not pass validity checking (cf. the 36. solution) thus roll back the assignment 
                        board[i][j] = '.'
                        rows[i].remove(digit);   cols[j].remove(digit);   squares[(i//3,j//3)].remove(digit)
                        unassigned.appendleft((i, j))
            return False

        helper()
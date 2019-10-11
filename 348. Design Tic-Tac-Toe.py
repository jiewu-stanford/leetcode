'''
Title     : 348. Design Tic-Tac-Toe ($$$)
Problem   : https://leetcode.com/problems/design-tic-tac-toe/
          : https://www.lintcode.com/problem/design-tic-tac-toe/description
'''
'''
construct n*n grid, use different symbols to record different player's moves
Reference: https://blog.csdn.net/danspace1/article/details/86616981
'''
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.grid = [[' ']*n for _ in range(n)]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            mark = 'X'
        else:
            mark = 'O'
        self.grid[row][col] = mark
        
        n = len(self.grid)
        sum_of_row = sum([self.grid[row][j] == mark for j in range(n)])
        sum_of_col = sum([self.grid[i][col] == mark for i in range(n)])
        sum_of_diag = sum([self.grid[i][i] == mark for i in range(n)])
        sum_of_anti = sum([self.grid[i][n-1-i] == mark for i in range(n)])   # anti(diagonal)
        if sum_of_row == n or sum_of_col == n or sum_of_diag == n or sum_of_anti == n:
            return player
        else:
            return 0
'''
without constructing the grid, use tuple to record both players' moves
Reference: https://www.codetd.com/article/3200361
'''
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """        
        self.size = n
        self.rows = [[0, 0] for _ in range(n)]   # [player1, player2]
        self.cols = [[0, 0] for _ in range(n)]
        self.diag = [0, 0]
        self.anti = [0, 0]   # anti(diagonal)

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        p = player - 1   # 0 for player 1 .vs. 1 for player2
        self.rows[row][p] += 1
        self.cols[col][p] += 1
        if row == col:
            self.diag[p] += 1
        if col == self.size-1-row:
            self.anti[p] += 1
        if any( self.rows[row][p] == self.size,
                self.cols[col][p] == self.size,
                self.diag[p] == self.size,
                self.anti[p] == self.size): return player
        return 0    
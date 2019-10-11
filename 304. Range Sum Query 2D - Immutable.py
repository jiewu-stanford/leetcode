'''
Title     : 304. Range Sum Query 2D - Immutable
Problem   : https://leetcode.com/problems/range-sum-query-2d-immutable/description/
'''
'''
extend the 303. solution from 1D to 2D, now the cumsum is the sum of all cells from the first cell (1,1) up to the current cell (i,j)---these are coordinates, -1 to get indices
Reference: https://leetcode.com/problems/range-sum-query-2d-immutable/discuss/288258/Python-6-liner-easy-to-understand-%2B-concise
Graph: https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
'''
class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix: return
        r, c = len(matrix), len(matrix[0])
        self.cumsum = [[0]*(c+1) for _ in range(r+1)]
        for i in range(1, r+1):
            for j in range(1, c+1):
                self.cumsum[i][j] = self.cumsum[i-1][j] + self.cumsum[i][j-1] - self.cumsum[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.cumsum[row2+1][col2+1] - self.cumsum[row1][col2+1] - self.cumsum[row2+1][col1] + self.cumsum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
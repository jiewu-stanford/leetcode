'''
Title     : 308. Range Sum Query 2D - Mutable ($$$)
Problem   : https://leetcode.com/problems/range-sum-query-2d-mutable/description/
          : https://www.lintcode.com/problem/range-sum-query-2d-mutable/
'''
''' straightforward adaptation of the 304. solution but TLE '''
class NumMatrix(object):

    def __init__(self, matrix):
        if not matrix: return
        self.matrix = matrix
        self.r, self.c = len(matrix), len(matrix[0])
        self.cumsum = [[0]*(self.c+1) for _ in range(self.r+1)]
        for i in range(1, self.r+1):
            for j in range(1, self.c+1):
                self.cumsum[i][j] = self.cumsum[i-1][j] + self.cumsum[i][j-1] - self.cumsum[i-1][j-1] + matrix[i-1][j-1]

    def update(self, row, col, val):
        dif, self.matrix[row][col] = val - self.matrix[row][col], val
        for i in range(row+1, self.r+1):
            for j in range(col+1, self.c+1):
                self.cumsum[i][j] += dif

    def sumRegion(self, row1, col1, row2, col2):
        return self.cumsum[row2+1][col2+1] - self.cumsum[row1][col2+1] - self.cumsum[row2+1][col1] + self.cumsum[row1][col1]
'''
adapt the 304. solution and use binary indexed tree (BIT) to store the prefix sums so as to speed up the cumsum
Reference: http://fernisoites.blogspot.com/2016/08/308-range-sum-query-2d-mutable.html
'''
class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix: return
        self.matrix = matrix
        self.r, self.c = len(matrix), len(matrix[0])
        cumsums = [[0]*(self.c+1) for _ in range(self.r+1)]
        self.BIT = [[0]*(self.c+1) for _ in range(self.r+1)]
        for i in range(1, self.r+1):
            for j in range(1, self.c+1):
                cumsums[i][j] = cumsums[i-1][j] + cumsums[i][j-1] - cumsums[i-1][j-1] + matrix[i-1][j-1]
        for i in range(1, self.r+1):
            previ = i - (i & -i)
            for j in range(1, self.c+1):
                prevj = j - (j & -j)
                self.BIT[i][j] = cumsums[i][j] - cumsums[previ][j] - cumsums[i][prevj] + cumsums[previ][prevj]   # matrix[i-1][j-1] = cumsums[i][j] - cumsums[i-1][j] - cumsums[i][j-1] + cumsums[i-1][j-1]

    def update(self, row, col, val):
        dif, self.matrix[row][col] = val - self.matrix[row][col], val
        i, j = row + 1, col + 1
        while i <= self.r:
            while j <= self.c:
                self.BIT[i][j] += dif
                j += (j & -j)   # to next node
            i += (i & -i)
            j = col + 1

    def cumsum(self, row, col):
        i, j = row + 1, col + 1
        res = 0
        while i > 0:
            while j > 0:
                res += self.BIT[i][j]
                j -= (j & -j)   # to parent node
            i -= (i & -i)
            j = col + 1
        return res
        
    def sumRegion(self, row1, col1, row2, col2):
        return self.cumsum(row2,col2) - self.cumsum(row1-1,col2) - self.cumsum(row2,col1-1) + self.cumsum(row1-1,col1-1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
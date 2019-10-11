'''
Title     : 59. Spiral Matrix II
Problem   : https://leetcode.com/problems/spiral-matrix-ii/
'''
'''
clever use of direction variable to define and change row index, column index increment
Reference: https://leetcode.com/problems/spiral-matrix-ii/discuss/22469/If-we-can't-write-data-to-the-matrix-we-change-the-directiona-simple-python-solution
'''
class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0]*n for _ in range(n)]
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        x, y, j = 0, 0, 0
        for i in range(1, n*n+1):
            matrix[x][y] = i
            dx, dy = dirs[j % 4]
            if -1 < x+dx < n and -1 < y+dy < n and matrix[x+dx][y+dy] == 0:
                x, y = x + dx, y + dy
            else:
                j += 1
                dx, dy = dirs[j % 4]
                x, y = x + dx, y + dy
        return matrix
'''
two common math ideas:
(1) borrow what is solved i.e. the 54. solution
(2) approaching solution from the other end i.e. assigning index to value rather than assigning value to index
Reference: https://leetcode.com/problems/spiral-matrix-ii/discuss/22443/9-lines-python-solution
'''
class Solution(object):
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        coords = [[(i,j) for j in range(n)] for i in range(n)]
        i = 1
        while coords:
            for x, y in coords.pop(0):
                matrix[x][y] = i
                i += 1
            coords = list(zip(*coords))[::-1]
        return matrix
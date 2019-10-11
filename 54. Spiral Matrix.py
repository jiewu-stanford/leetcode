'''
Title     : 54. Spiral Matrix
Problem   : https://leetcode.com/problems/spiral-matrix/
'''
'''
spriral = recursively delete first row and rotate the remaining counter-clockwise
Reference: https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
'''
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        spiralMatrix = []
        for j in range(len(matrix[0])-1, -1, -1):
            lst = []
            for i in range(1, len(matrix), 1):
                lst.append(matrix[i][j])
            spiralMatrix.append(lst)
        return matrix[0] + self.spiralOrder(spiralMatrix)
'''
step-by-step follow the spiral i.e. left to right => top to bottom => right to left => bottom to top by using pop() and pop(0)
Reference: https://leetcode.com/problems/spiral-matrix/discuss/20821/An-iterative-Python-solution
'''
class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res.extend(matrix.pop(0))
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res